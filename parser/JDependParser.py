# Parse JDepend into JSON format
# Version 1

# import statements-----------------------------------------------
import re
import xml.etree.ElementTree as ET
import json


# with open('TEST.json') as json_file:
# 	json_data = json.load(json_file)


# take in an xml file
xml_data = ET.parse('JDependMock.xml')
root = xml_data.getroot()

package_dependency_list = []
for packages in root.findall('Packages'):
	for package in packages.findall('Package'):
		packageName = package.get('name')
		dependencyList = []
		for dependsUpon in package.findall('DependsUpon'):
			for dependency in dependsUpon.findall('Package'):
				dependencyToAppend = dependency.text
				dependencyList.append(dependencyToAppend)
		package_dependencies = { "packageName" : packageName, "dependecies" : str(dependencyList), "contents" : [] }
		package_dependency_list.append(package_dependencies)
		# print(repr(package_dependencies))
		# json_data = {"package_dependencies" : package_dependencies}


with open('JDependParserOutput.json', 'w') as outfile:
	json.dump(package_dependency_list, outfile, indent=0)
