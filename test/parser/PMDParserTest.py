#os.system('python3 ..\parser\PMDParser.py ')

#import os 

#foo = os.path.dirname(os.path.dirname(PMDParserTest.py))
#print (foo)

#BASE_DIR = os.path#.join( os.path.dirname( __file__ ), '..' )

#print (BASE_DIR)

import shutil
import inspect, os
filename = (inspect.getfile(inspect.currentframe()))
filepath = os.path.dirname(os.path.abspath(filename))
print (filepath) # script directory

newfilepath = filepath.replace('test/parser', 'parser/')
print (newfilepath)



shutil.copy (newfilepath+'PMDParser.py',filepath)
shutil.copy (newfilepath+'JDependParserOutputMock.json',filepath)
shutil.copy (newfilepath+'PMDParser.xml',filepath)

