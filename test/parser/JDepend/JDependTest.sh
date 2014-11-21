

# Run this file and compare the 2 output JSON PMD files

echo "Set JDEPEND_TEST directory: "
JDEPEND_TEST=$(pwd)
echo $JDEPEND_TEST

echo "Set PARSER directory: "
cd $JDEPEND_TEST/../../../parser/
PARSER=$(pwd)
echo $PARSER

echo "Run JDepend.py with $JDEPEND_TEST/JDependMock_JDependOutput"
python3 $PARSER/JDependParser.py $JDEPEND_TEST/JDependMock

echo "Copy the output to the test directory"
cp $JDEPEND_TEST/JDependMock_JDependOutput.xml $JDEPEND_TEST/JDEPENDTEST_output.json 

echo "Remove old test files"
sudo rm $JDEPEND_TEST/JDependMock_JDependOutput.xml

diff --unified $JDEPEND_TEST/JDEPENDTEST_output.json $JDEPEND_TEST/JDependMock_JDependParserOutput