Python Word Parser
==================

***Function:*** Python script to count the most used words in books, your writings, essays etc. fed in the format of a text file. 

Usage
-----

1.) To run from terminal/cmd, 'cd' to the directory where you have the script downloaded and save the contents of the source file to a text file or in any other format openable by a text editor. 

	$python ParsertoFile.py [path of your source text file] [enter the top x words used you'd like to view]

2.) To add a word to the ignore-list (words that are overlookd during the processing), simply open up the file, and add the word as a string to the 'ignore' tuple.

Sample Usage Case
------------------

***Input: The Book of Revelations***

	$python ParsertoFile.py /home/andrew/KJVRevelations.txt 4
	
***Output***	

	I : 167 
	God : 94
	seven : 54
	beast : 42

Wow, the Revelations is really metal!
