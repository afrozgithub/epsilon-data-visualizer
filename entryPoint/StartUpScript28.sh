echo "Starting Tool Handler"

echo "Retrieving code base name from command line"
echo "Note, codebase name MUST be the same as the name in the codebase directory"
echo $CODE_BASE_NAME

echo "CODE_BASE_NAME: "
CODE_BASE_NAME=$1


echo "Set ENTRY_POINT directory: "
ENTRY_POINT=$(pwd)
echo $ENTRY_POINT


echo "Set up JDepend"
echo "Set JDEPEND_HOME directory: "
cd ../libs/jdepend/jdepend-2.9.1
JDEPEND_HOME=$(pwd)
echo $JDEPEND_HOME

echo "Set CODE_BASE"
cd $ENTRY_POINT/../codebases/$CODE_BASE_NAME
CODE_BASE=$(pwd)
echo $CODE_BASE

if [ "which brew" == "" ]; then
	echo "Install brew"
	ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	brew doctor

else 
	echo "brew already installed"
fi

if [ "which mvn" == "" ]; then
	echo "Install mvn"
	brew update
	brew install maven

else 
	echo "maven already installed"
fi

echo "Compiling with Maven"
mvn compile


echo "Changing permissions for $JDEPEND_HOME"
chmod -R a+x $JDEPEND_HOME

echo "Adding JDepend to CLASSPATH"
export CLASSPATH=$CLASSPATH:$JDEPEND_HOME/lib/jdepend-2.9.1.jar

echo "Run ant build script"

if [ "ant -version" == "" ]; then
	echo "Install ant"
	brew update
	brew install ant

else 
	echo "ant installed"
fi

echo "Go to JDEPEND_HOME"
cd $JDEPEND_HOME

echo "Call ant jar"
ant jar

echo "Run JDepend on codebase to produce XML"
cd $JDEPEND_HOME/build

 # get class fiels
echo "Java Command"
java jdepend.xmlui.JDepend -file $ENTRY_POINT/../parser/"$CODE_BASE_NAME"_JDependOutput.XML $ENTRY_POINT/../codebases/$CODE_BASE_NAME
echo "Run PMD on codebase to produce XML"

# # navigate to bin of pmd
cd "$ENTRY_POINT/../libs/pmd/bin"

# # call run command 
./run.sh pmd -d $ENTRY_POINT/../codebases/$CODE_BASE_NAME -f xml -r $ENTRY_POINT/../parser/"$CODE_BASE_NAME"_PMDOutput.xml -R rulesets/java/basic.xml

echo "Call JDependParser with XML to produce JSON"

cd $ENTRY_POINT/../parser/

echo $(pwd)

python3 $ENTRY_POINT/../parser/JDependParser.py $CODE_BASE_NAME

echo "Call PMDParser with JSON and XML to produce JSON"

python3 $ENTRY_POINT/../parser/PMDParser.py $CODE_BASE_NAME

echo "Copy the output to website directory"

cp "$CODE_BASE_NAME"_output.json $ENTRY_POINT/../website/data.json

echo "Open the website"

open $ENTRY_POINT/../website/site.html
