1. Third Party Library
We used the Natural Language Toolkit (NLTK) for this assignment. The installation guide can be found at NLTK's website at www.nltk.org/install.html. 

2. Dataset
We have all our source codes and datasets stored in our Git repository. You may download a zip version from https://github.com/thetwelveoaks/NLP by choosing 'Clone or download'->'Download ZIP'. 

Alternatively, you may clone our Git repository. First please make sure you have Git installed on your local computer. The comprehensive Git installation guide can be found at https://git-scm.com/book/en/v2/Getting-Started-Installing-Git. Choose a method that suits your platform. 
With Git installed, you may clone our repository through either command line or GUI (if you have installed) at either:
HTTPS: https://github.com/thetwelveoaks/NLP.git or
SSH: git@github.com:thetwelveoaks/NLP.git

In your downloads, the file 'dataset/Posts.xml' is the original dataset we downloaded from Stack Exchange data dump. The file 'dataset/APIs_Fully_Annotated.xml' is our annotation results after auto-annotation and manual inspection. 

3. Directory Listing and Installation Guide

Below shows a detailed explanation of each file under 'dataset/'. 

API_Sample.xml				The selected 100 posts for API recognition without annotation
APIs.xml					All posts that contain at least one API
APIs_Auto_Annotated.xml		The auto-annotated results
APIs_Fully_Annotated.xml	The auto_annotated results after manual inspection
Posts.xml					The original corpus
Posts_HTML_FREE.xml			Intermediate results after trimming HTML tags
falneg.txt					All false negatives after API recognition
falpos.txt					All false positives after API recognition
stop_word.txt				A list of stop words defined by NLTK

All our codes are written in Python 3.5.2. Please make sure you have the correct version of Python interpreter installed. 
To run our codes is simple. In command line, just use the following command
python 'file_name.py' or
python3 'file_name.py'
to run a particular file. You may also use Python IDLE. 

## Note: all source codes are written on a Macintosh machine. As such, the format of the file path may be different if you run our codes on a Windows machine. Please change all the file paths if necessary ##

You may run our source code files in the following orders:
python data_collection.py 	To get statistics about the corpus
python pos_stem.py 			To get the results for stemming and POS tagging

For API annotation and API recognition:
python remove_html.py  		To remove HTML tags; output to 'dataset/Posts_HTML_FREE.xml'
python extract_api.py 		To get posts containing at least one API; output to 'dataset/APIs.xml'
python annotate_api.py 		To randomly select 100 posts and apply auto annotation; output to 'dataset/API_Sample.xml' and 'dataset/APIs_Auto_Annotated.xml'
python recognise_api.py 	To recognise APIs; output false positives to 'dataset/falpos.txt'; output false negatives to 'dataset/falneg.txt'
utilities.py 				Contains common functions and constants; you don't need to run it. 

4. Output Interpretation
For data collection, stemming and POS tagging, the output is directed to Python terminal. There are labels in front of each output, so they should be self-explanatory. 

For API annotation and recognition, however, the output is redirected to files. The final false positives and false negatives are collected in 'dataset/falpos.txt' and 'dataset/falneg.txt'. Each line represents an API that causes that error. 