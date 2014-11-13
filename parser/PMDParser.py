import xml.etree.ElementTree as ET
import json
import sys

if (sys.argv[1] == "" ):
# accept command line arguments
	print("Did not pass command line argument: Please pass codebase name")
	# sys.exit
else:
	code_base = sys.argv[1]
	print("Running script on " + code_base)

json_file_name = code_base + '_JDependParserOutput.json'

# Take in the JSON file outputted from JDepend parser
with open(json_file_name) as json_file:
	json_data = json.load(json_file)

# Take in a xml file outputted from PMD
xml_file_name = code_base + '_PMDOutput.xml'
xml_data = ET.parse(xml_file_name)
root = xml_data.getroot()

# Parse out the packageName, the class name, and the violated rule from the xml 
for file in root.findall('file'):
	for violation in file.findall('violation'):
		rule = violation.get('rule')
		packageName = violation.get('package')
		className = violation.get('class')
		class_violation = { "className" : className, "violation" : rule }
		# Insert the violation and className into
        # the JSON Object of the matching package
		for key in json_data:
			json_package = key['packageName']
			if json_package == packageName:
				key['contents'].append(class_violation)

output_file_name = code_base + '_output.json'

# Output the new XML File
with open(output_file_name, 'w') as outfile:
	print("Dumping to " + output_file_name)
	json.dump(json_data, outfile, indent=0)

