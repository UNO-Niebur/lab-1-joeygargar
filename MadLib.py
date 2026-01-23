#MadLib.py
#Name: Mia Garcia
#Date: 1/22/26
#Assignment: Lab 1 

def main():
  print("Lets Do a Madlib!")
  #Ask user for words
  noun1 = input("Enter a noun: ")
  noun2 = input("Enter a noun: ")
  place1 = input("Enter a place: ")
  adjective1 = input("Enter a adjective: ")
  verb1 = input ("Enter a verb: ")
  adjective2 = input("Enter a adjective: ")
  #Print the story with the user supplied words.
  print("Everybody hold on to your", noun1, "the", noun2,
  "is about to take off. Please remain in your seats and keep your seat belts fastened as we make our way to", place1,
  ". This ride will be", adjective1,"so make sure your ready to", verb1,
  ". We apologize for the", adjective2,"smell and hope you enjoy the ride." )


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
