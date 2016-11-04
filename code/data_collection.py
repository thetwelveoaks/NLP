from xml.dom import minidom


xmldoc = minidom.parse("../dataset/Posts.xml")
posts = xmldoc.getElementsByTagName("posts")[0]
rows = posts.getElementsByTagName("row")
question = 0
answer = 0
answerctone =0
answercttwo =0
answerctmore= 0
answerct3=0
answerct4=0
answerct5=0
answerct6 =0
numberofwords=0

for row in rows:
    postTypeId = int(row.attributes["PostTypeId"].value)
    if(postTypeId==1):
        question= question +1
        answercount = int(row.attributes["AnswerCount"].value)
        if(answercount == 1): answerctone = answerctone+1
        elif (answercount == 2): answercttwo = answercttwo +1
        elif( answercount ==3): answerct3 = answerct3 +1
        elif( answercount ==4): answerct4 = answerct4 +1
        elif( answercount ==5): answerct5 = answerct5 +1
        elif( answercount ==6): answerct6 = answerct6 +1
        elif( answercount >6): answerctmore = answerctmore +1
    else: answer= answer +1
    body= row.attributes["Body"].value
    numberofwords= len(body.split()) + numberofwords
 
total= question + answer
print("question count ",question) #38321
print("answer count ",answer)  #47532
print("one answer count ",answerctone) #16914
print("two answer count ",answercttwo) #6155
print("three answer count ",answerct3)#2303
print("four answer count ",answerct4)#933
print("five answer count ",answerct5)#438
print("six answer count ",answerct6)#212
print("more than 6 answer count ",answerctmore) #279
print("no answer ", question-answerctone-answercttwo-answerctmore-answerct3-answerct4-answerct5-answerct6) #11087
print("one answer percentage ",answerctone/question) #44.14%
print("two answer percentage ",answercttwo/question) #16.06%
print("more than two answer percentage ",answerctmore/question) #10.87%
print("no answer ", (question-answerctone-answercttwo-answerctmore-answerct3-answerct4-answerct5-answerct6)/question) # 28.93%
print("average number of words per post ",numberofwords/total) #95.53
