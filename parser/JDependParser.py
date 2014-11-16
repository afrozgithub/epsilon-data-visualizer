# Parse JDepend into JSON format
# Version 1

# import statements-----------------------------------------------
import re
import xml.etree.ElementTree as ET
import json
import sys

# with open('TEST.json') as json_file:
# 	json_data = json.load(json_file)


# if (len(sys.argv) > 1):
if (sys.argv[1] == "" ):
# accept command line arguments
	print("Did not pass command line argument: Please pass codebase name")
	# sys.exit
else:
	code_base = sys.argv[1]
	print("Running script on " + code_base)

# accept xml
xml_file = code_base + '_JDependOutput.xml'
xml_data = ET.parse(xml_file)
root = xml_data.getroot()


package_dependency_list = []
for packages in root.findall('Packages'):
	for package in packages.findall('Package'):
		packageName = package.get('name')
		dependencyList = []
		for dependsUpon in package.findall('DependsUpon'):
			for dependency in dependsUpon.findall('Package'):
				dependencyToAppend = dependency.text
				dependencyList.append(str(dependencyToAppend))
		package_dependencies = { "packageName" : packageName, "dependencies" : dependencyList, "contents" : [] }
		package_dependency_list.append(package_dependencies)
		# print(repr(package_dependencies))
		# json_data = {"package_dependencies" : package_dependencies}

# output to JSON
json_outfile = code_base + '_JDependParserOutput.json'

with open(json_outfile, 'w') as outfile:
	print("Dumping to" + json_outfile)
	json.dump(package_dependency_list, outfile, indent=0)
