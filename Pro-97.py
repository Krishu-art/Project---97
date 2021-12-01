birthdate = int(input("Guess my birthdate from 11 to 19:"))

count = 1
while (count<=5):
 print(count)
 birthdate = int(input("Guess my birthdate from 11 to 19"))
 if (birthdate==10):
    print("Guess a bit higher")

 if (birthdate==11):
    print("Guess a bit higher")

 if (birthdate==12):
    print("close")

 if (birthdate==13):
    print("very close")   

 if (birthdate==14):
    print("U got it")
    break

 if (birthdate==15):
     print("Very close")

 if (birthdate==16):
    print("Close")

 if (birthdate==17):
    print("Guess a bit lower")

 if (birthdate==18):
    print("Cold")

 if (birthdate==19):
    print("Very cold")   
    count = count + 1
 
