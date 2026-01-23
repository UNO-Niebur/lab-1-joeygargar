#FirstProgram.py
#Name: Mia Garcia
#Date: 01/22/26
#Assignment: Lab 1 

def main():
  print("First Program")
  #Say hello
  print("hello")
  #Ask for the user's name
  username = input("what is your name?")
  #Use the user's name in the program.
  print("nice to meet you", username)
  #Ask the user for their age.
  userage = int(input("how old are you?"))
  #Tell the user what year they were born in.
  #Assume that they have not had their birthday yet this year.
  birthyear = 2026 - userage 
  print("you were born in", birthyear) 

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
