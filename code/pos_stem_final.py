import nltk, re, pprint, random from nltk import word_tokenize from
nltk.stem import * from xml.dom import minidom

   

##Stemming

stop_words = [line.rstrip('\n') for line in open("../dataset/stop_word.txt","r")][:-2]
input_txt = ""

xmldoc = minidom.parse("../dataset/Posts.xml")
posts = xmldoc.getElementsByTagName("posts")[0]
rows = posts.getElementsByTagName("row")
for row in rows:
    body= row.attributes["Body"].value
    input_txt += body[3:-5]

    
input_txt = input_txt.lower()
tokens= word_tokenize(input_txt)
token_list = set(tokens)
for word in stop_words:
    token_list.discard(word)


word_count=[]



for i in token_list:
    word_count.append([tokens.count(i),i])
    
word_count.sort(reverse=True)#list of word counts in reverse order

for num in range(20):#return top 20 words
    print(word_count[num][1])

stem_tokens=[PorterStemmer().stem(word) for word in tokens]
stem_token_list=set(stem_tokens)

stem_word_count=[]

for i in stem_token_list:
    stem_word_count.append([stem_tokens.count(i),i])
    

stem_word_count.sort(reverse=True)
for num in range(20):
    print(stem_word_count[num][1])


##Pos_Tagging
input_pos_txt = ""##can we manually input 10 sentences for this part since we also have to 
input_pos_txt = input_pos_txt.()
pos_tokens= word_tokenize(input_pos_txt)
nltk.pos_tag(pos_tokens)
