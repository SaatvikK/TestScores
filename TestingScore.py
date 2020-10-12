Names = []
Test1 = []
Test2 = []
Test3 = []
Total = []
Ave = []
#Test 1: /20
#Test 2: /25
#Test 3: /35

#Input Students names and scores:
NumStudents = int(input("How many students are there? "))
while(len(Names) != NumStudents):
  NameInput = input("Input Name:")
  Names.append(NameInput)
  while(True):
    Test1Score = int(input("Test 1 Score: ")) 
    if(Test1Score <= 20):
      Test1.append(Test1Score)
      break
    elif(Test1Score > 20):
      print("Mark inputted is too high (out of 20), try again.")
    else:
      print("An unexpected error has occurred.")
  while(True):
    Test2Score = int(input("Test 2 Score: "))
    if(Test2Score <= 25):
      Test2.append(Test2Score)
      break
    elif(Test2Score > 25):
      print("Mark inputted is too high (out of 25), try again.")
    else:
      print("An unexpected error has occurred.")
  while(True):
    Test3Score = int(input("Test 3 Score: "))
    if(Test3Score <= 35):
      Test3.append(Test3Score)
      break
    elif(Test3Score > 35):
      print("Mark inputted is too high (out of 30), try again.")
    else:
      print("An unexpected error has occurred.")
del NumStudents
#Total Scores for each Student:
for i in range(len(Names)):
  total = 0
  total = total + Test1[i] + Test2[i] + Test3[i]
  Total.append(total)


#CALCULATIONS
#Var for Total for each student is "Total"
#Ave = Total/3
for i in range(len(Total)):
  Ave.append(Total[i]/3)

for i in range(len(Names)):
  print("Name: ", Names[i], "\n Total Score: ", Total[i], "\n Average: ", Ave)