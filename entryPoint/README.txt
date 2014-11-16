epsilon-data-visualizer
=======================
####StartUpScript.sh Instructions:

To visualize a new code base

1.  Download a Java code base from Github.  (note: the code base must have a pom.xml file).

2.  Save the code base at ../codebases/<codebasename>

3.  Change the permissions of StartUpScript.sh with "chmod 777 StartUpScript.sh"

4.  On your Mac, run the shell script with ". StartUpScript.sh <codebasename>"

5.  A website with the visualization will open.

Warning:  Homebrew and Maven will be installed if they are not already so the startup script may take some time.
		  The JAVA_HOME environment variable will be changed in order for maven to run correctly.
