epsilon-data-visualizer
=======================
####StartUpScript.sh Instructions:

To run code on a new code base
1.  Download Java code base off github.  (note: the code base needs to have a pom file).
2.  Save the code base at ../codebases/<codebasename>
3.  Change the permissions of StartUpScript.sh with "chmod 777 StartUpScript.sh"
4.  On your mac, run the shell script with ". StartUpScript.sh <codebasename>"
5.  A website with the visualization will open.

Warning:  homebrew and maven will be installed if they are not already so the startup script may take some time.
		  the JAVA_HOME environment variable will be changed in order for maven to run correctly.
