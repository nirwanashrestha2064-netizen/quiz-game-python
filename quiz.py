print("🎯 Welcome to Quiz Game!")

question=("What is the capital of Nepal?")
answer=input(question+" ")
print("Your answer is :",answer)

score=0

correct_answer="Kathmandu" 
if answer==correct_answer:
    print("It is absolutely correct!")
    score+=1
else:
    print("Sorry, this is wrong!")


question = "Which planet is known as the Red Planet?"
answer = input(question + " ")

correct_answer = "Mars"

if answer == correct_answer:
    print("It is absolutely correct!")
    score+=1
else:
    print("Sorry, this is wrong!")

print("Your score: ",score)