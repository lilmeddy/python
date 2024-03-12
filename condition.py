mede = int(input("Enter your score mede: "))
duro = int(input("Enter your score duro: "))
obafemi = int(input("Enter your score obafemi: "))
ibrahim = int(input("Enter your score ibrahim: "))
timi = int(input("Enter your score timi: "))
totalScore = mede + duro + obafemi + ibrahim + timi
meanScore = int(totalScore/5)
if (meanScore >= 70):
    print(f"The total score is {meanScore}. They all Passed cute hehe")
else:
    print(f"The total score is {meanScore}. They all failed sad lol")