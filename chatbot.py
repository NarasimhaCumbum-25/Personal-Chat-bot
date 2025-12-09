import datetime
import time


name=input("welcome,enter your name:")
presenthour=datetime.datetime.now().hour
if 5 <= presenthour <= 11:
    print(f"Good morning,{name}")
elif  11 <= presenthour <= 17:
    print(f"Good afternoon,{name}")
elif  17 <= presenthour <= 20:
    print(f"Good evening,{name}")
else:
    print(f"Good night,{name}")            
    



print("hello, Welcome to your chatbot")
print("Ask your basic questions, Type 'bye' to exit from conversation")

# create the dictionary for the resonses and match questions

responses={
    "hello":"Hi , I am there to answer you",
    "how are you":"I am fine, what about you",
    "I am also fine":" Then what new",
    "who are you":" I am your smart chatbot",
    "python":"This is a high demanding programming language "
}
# logic (Function)
def getresponseof(userquery):
    userquery=userquery.lower()
    for eachkey in responses:
        if eachkey in userquery:
            return responses[eachkey]            
    return "Im in learning mode , not able to answer"
#user input
while True:
    userinput=input("Enter your question:")
    reply=getresponseof(userinput)
    print("Bot",reply)
    time.sleep(2)
    if "bye" in userinput.lower():
        break
