score = int(input("Enter your score: "))
score1 = int(input("Enter your score1: "))
score2 = int(input("Enter your score2: "))
score3 = int(input("Enter your score3: "))
score4 = int(input("Enter your score4: "))
totalScore = score + score1 + score2 + score3 + score4
meanScore = totalScore/5
if (meanScore >= 70):
    print(f"The total sore is {meanScore}. You Passed")
else:
    print(f"The total score is {meanScore}. You failed lol")