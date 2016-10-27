from xml.dom import minidom


xmldoc = minidom.parse("../Data_set/Posts.xml")
posts = xmldoc.getElementsByTagName("posts")[0]
rows = posts.getElementsByTagName("row")
question = 0
answer = 0
answerctone =0
answercttwo =0
answerctmore =0
numberofwords=0

for row in rows:
    postTypeId = int(row.attributes["PostTypeId"].value)
    if(postTypeId==1):
        question= question +1
        answercount = int(row.attributes["AnswerCount"].value)
        if(answercount == 1): answerctone = answerctone+1
        elif (answercount == 2): answercttwo = answercttwo +1
        elif( answercount >2): answerctmore = answerctmore +1
    else: answer= answer +1
    body= row.attributes["Body"].value
    numberofwords= len(body.split()) + numberofwords
 
total= question + answer
print("question count ",question) #38321
print("answer count ",answer)  #47532
print("one answer count ",answerctone) #16914
print("two answer count ",answercttwo) #6155
print("more than two answer count ",answerctmore) #4165
print("no answer ", question-answerctone-answercttwo-answerctmore) #11087
print("one answer percentage ",answerctone/question) #44.14%
print("two answer percentage ",answercttwo/question) #16.06%
print("more than two answer percentage ",answerctmore/question) #10.87%
print("no answer ", (question-answerctone-answercttwo-answerctmore)/question) # 28.93%
print("average number of words per post ",numberofwords/total) #95.53
