import nltk, re, pprint, random, nltk.data
from nltk import word_tokenize
from nltk.stem import *
from xml.dom import minidom
from string import punctuation
from nltk.corpus import stopwords
from collections import Counter

   

##Stemming

stopwords=set(stopwords.words('english'))
input_txt = ""

def clean_html(html):
    """
    Copied from NLTK package.
    Remove HTML markup from the given string.

    :param html: the HTML string to be cleaned
    :type html: str
    :rtype: str
    """

    # First we remove inline JavaScript/CSS:
    cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
    # Then we remove html comments. This has to be done before removing regular
    # tags since comments can contain '>' characters.
    cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
    # Next we can remove the remaining tags:
    cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
    # Finally, we deal with whitespace
    cleaned = re.sub(r"&nbsp;", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    return cleaned.strip()

def remove_url(text):
    text = re.sub(r"(?:\@|https?\://)\S+", "", text)
    return text


xmldoc = minidom.parse("../dataset/Posts.xml")
posts = xmldoc.getElementsByTagName("posts")[0]
rows = posts.getElementsByTagName("row")


for row in rows:
	body= row.attributes["Body"].value
	body = clean_html(body)
	body = remove_url(body)
	input_txt += body

    
tokens= word_tokenize(input_txt)
token_set = set(tokens)

count = Counter()

for word in tokens:
    word=word.lower()
    if word in stopwords:
        continue
    elif set(word) & set(punctuation) == set() :
        count.update([word])
    else:
        continue
		
result=[k for k,_ in count.most_common(20)]

print(result)

P_count= Counter()

for word in tokens:
	word=word.lower()
	if word in stopwords:
		continue
	elif set(word) & set(punctuation)== set():
		stemmed=PorterStemmer().stem(word)
		P_count.update([stemmed])
	else:
		continue
P_result = [k for k,_ in P_count.most_common(20)]
print(P_result)

P_orig = [[]] * 20
for i in range(20):
	for word in token_set:
		if PorterStemmer().stem(word) == P_result[i]:
			P_orig[i].append(word)

##Pos_Tagging

##These are the 10 sentences that were obtained from sampling and included in the report for analysis of pos tagging
##                 "I have a rooted Nexus One and want to remove some of the pre-installed applications, like Amazon MP3, for example."
##                 "I made a partition to install applications on the SD Card using Apps2SD."
##                 "Heres an alternative to the 3D Gallery its a 2dGallery they updates very fast!"
##                 "Both rooting and using a prepaid SIM seem a bit extreme."
##                 "A bug in the latest version of Chrome can cause this in certain circumstances (low memory being one)."
##                 "What package were you using in Odin to flash your phone?"
##                 "I'm trying to factory reset nexus 7."
##                 "When we receive a call the ringtone is very slow for the first 3 secs and after that the ringtone plays with full volume."
##                 "I just woke up this morning and my photos and music weren't displayed in their respective apps."
##                 "A mate recently used my mobile facebook app to log into his account."
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

input_pos_txt = random.sample(tokenizer.tokenize(input_txt),10)

for sentence in input_pos_txt:
    pos_tokens= word_tokenize(sentence)
    pos_sentence=nltk.pos_tag(pos_tokens)
    print(pos_sentence)
