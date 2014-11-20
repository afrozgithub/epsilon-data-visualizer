

echo "Set PARSER_TEST directory"
PARSER_TEST=$(pwd)
echo $PARSER_TEST

echo "Set PARSER directory"
cd $PARSER_TEST/../../../parser/
PARSER=$(pwd)
echo $PARSER

echo "Copy over test files"
cp $PARSER_TEST/PMDTEST_PMDOutput.xml $PARSER/PMDTEST_PMDOutput.xml

cp $PARSER_TEST/PMDTEST_JDependParserOutput.json $PARSER/PMDTEST_JDependParserOutput.json 

echo "Call PMDParser with JSON and XML Test output to produce JSON"
python3 $PARSER/PMDParser.py PMDTEST

echo "Copy the output file back to the test directory"

cp $PARSER/PMDTEST_output.json $PARSER_TEST/PMDTEST_output.json 

echo "Remove old test files"
#sudo rm $PARSER/PMDTEST_JDependParserOutput.json
#sudo rm $PARSER/PMDTEST_PMDOutput.xml
#sudo rm $PARSER/PMDTEST_output.json

diff --unified $PARSER_TEST/PMDTEST_output.json $PARSER_TEST/PMD_Test_Data.json