Softwares to be used:

1) Pycharm version 4
2) python 3.4

Packages needed :

1) tweepy
2) nltk
3) after installing nltk do import nltk and then nltk.download() and then download all
4) pickle
5) scikit-learn


Training the classifiers again and again takes a lot of time, so pickle package , which is used to dump the python ojects to the files
are used.We check the


Points to be Noted:
1.Regarding the directory structure of the project
Major-Project-1 /
			source --> containes only source files and modules.
			resources --> containes some notes, references etc.
			outputFiles --> containes all the text files, output Files, cleaned Files
			classifiers --> Contains all the classifiers trained

Now, to open/ write any file , all we need to do is following:
	1) import ownModule
	2) Specify the name of the folder our file is present in and to it append the file name.
	E.g.
	file_folder = ownModule.createFileFolder('outputFiles')
    file_folder += os.path.sep
    file_folder +="Some file name in outputFiles"
Note:Python is platform independent language(to a great extent).So , the os package provides a value os.path.sep that provides os dependent path
 separators
2.os.path.isfile function can check if a file exist or not.This is very useful.For instance, if a classifier doesn't exist,
we need to train a new one
