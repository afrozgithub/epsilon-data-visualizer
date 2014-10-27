import xml.etree.ElementTree as ET
import json

# import sys
# filename = sys.argv[1]

# Take in the JSON file outputted from JDepend parser
with open('JDependParserOutputMock.json') as json_file:
	json_data = json.load(json_file)

# Take in a xml file outputted from PMD
xml_data = ET.parse('PMDOutputMock.xml')
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

# Output the new XML File
with open('data.json', 'w') as outfile:
  json.dump(json_data, outfile, indent=0)

