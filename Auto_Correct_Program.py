# Name:          Farris Matar
# Date:          May 24, 2017
# Description:   Making an auto-correct program by reading
#                from a dictionary of words.

import pygame

# Opening the dictionary.
dictionaryFile = open("dict.txt","r")
editingDictionary = open("dict.txt","a")

# Making a list to hold all the words.
dictionary = []

# Making a variable to hold the words the user enters.
userWords = ""

# Making a loop to get all the words in the file and adding them to a list.
while True:
    text = dictionaryFile.readline()
    if text == "":
        break
    dictionary.append(text[:-1])

# Using a while loop to run the program until the user says to stop.
while True:
    # Resetting the variables.
    # List to hold the repeat words.
    repeatWords = []
    
    # List to hold the matching words and how many times they occur.
    matchingWords = []
    matchCount = []
    
    # Some variables to make sure some loops work.
    highestCount = 0
    highestWord = ""
    
    # Variables to choose which word to auto-correct to.
    choice1 = ""
    choice2 = ""
    choice3 = ""
    
    # Asking the user for the starting letters (using a loop to ensure they type something in).
    userText = input("Enter the first letter(s) of the word (or -1 to quit): ").lower()
    while userText == "":
        print("You didn't type anything in!")
        userText = input("Enter the first letter(s) of the word (or -1 to quit): ").lower()
    
    # Checking if the user wants to quit.
    if userText == "-1":
        break
    
    # Checking for the letters in any of the words of the dictionary.
    # Start by getting the length of the word.
    textLength = len(userText)
    
    # Making a loop to go through that many of the starting letters of all the words.
    for count in dictionary:
        # Checking if there is a match between starting letters and the word isn't repeated.
        if userText in count[:textLength] and count not in repeatWords:
            
            # Adding the word and how many times it occurs in the match list.
            matchingWords.append(count)
            matchCount.append(dictionary.count(count))
            # Adding it to the repeat list so it isn't repeated.
            repeatWords.append(count)
    
    # Finding the most used word (making sure not to run the code if no matches were found).
    if len(matchCount) > 0:
        for count in range(len(matchCount)):
            if matchCount[count] > highestCount:
                highestWord = matchingWords[count]
                highestCount = matchCount[count]
                
        # Printing the highest word and its number of occurences.
        print("Most Common Matches Found:")
        print(highestWord,"\t",highestCount)
        # Updating auto-correct choices.
        choice1 = highestWord
    
        # If there are more matches, finding the second highest word.
        if len(matchCount) > 1:
            matchCount.remove(highestCount)
            matchingWords.remove(highestWord)
            # Redoing the loop to find the second most used word.
            # Resetting the variables.
            highestWord = ""
            highestCount = 0
            for count in range(len(matchCount)):
                if matchCount[count] > highestCount:
                    highestWord = matchingWords[count]
                    highestCount = matchCount[count]
            print(highestWord,"\t",highestCount)
            # Updating auto-correct choices.
            choice2 = highestWord
                
        # If there are still more matches, finding the third highest word.
        if len(matchCount) > 1:
            matchCount.remove(highestCount)
            matchingWords.remove(highestWord)
            # Resetting the variables.
            highestWord = ""
            highestCount = 0
            # Redoing the loop to find the third most used word.
            for count in range(len(matchCount)):
                if matchCount[count] > highestCount:
                    highestWord = matchingWords[count]
                    highestCount = matchCount[count]
            print(highestWord,"\t",highestCount)
            # Updating auto-correct choices.
            choice3 = highestWord
            
        print()
        
        # Asking the user which word to auto-correct to.
        # Auto-correcting to the first word if no other matches were found.
        if choice2 == "" and choice3 == "":
            print("Auto-correcting",'"'+userText+'"',"to",choice1+".")
            print()
            dictionary.append(choice1)
            userWords += choice1 + " "
            # Adding the word to the dictionary text file.
            editingDictionary.write(choice1)
            editingDictionary.write("\n")
        
        # Deciding between two words if no other matches were found.
        elif choice3 == "":
            userChoice = input("Which word would you like to auto-correct to? (1 or 2, or c to cancel) ")
            print()
            # Using a loop to ensure proper input.
            while userChoice != "1" and userChoice != "2" and userChoice != "c":
                print("Invalid input.")
                userChoice = input("Which word would you like to auto-correct to? (1 or 2, or c to cancel) ")
            # Auto-correcting based on the user's choice.
            if userChoice == "1":
                print("Auto-correcting",'"'+userText+'"',"to",choice1+".")
                print()
                dictionary.append(choice1)
                userWords += choice1 + " "
                # Adding the word to the dictionary text file.
                editingDictionary.write(choice1)
                editingDictionary.write("\n")
                
            elif userChoice == "2":
                print("Auto-correcting",'"'+userText+'"',"to",choice2+".")
                print()
                dictionary.append(choice2)
                userWords += choice2 + " "
                # Adding the word to the dictionary text file.
                editingDictionary.write(choice2)
                editingDictionary.write("\n")                
        
        # Deciding between three words if three or more matches were found.        
        else:
            userChoice = input("Which word would you like to auto-correct to? (1, 2, or 3, or c to cancel) ")
            print()
            # Using a loop to ensure proper input.
            while userChoice != "1" and userChoice != "2" and userChoice != "3" and userChoice != "c":
                print("Invalid input.")
                userChoice = input("Which word would you like to auto-correct to? (1, 2, or 3, or c to cancel) ")
            # Auto-correcting based on the user's choice.
            if userChoice == "1":
                print("Auto-correcting",'"'+userText+'"',"to",choice1+".")
                print()
                dictionary.append(choice1)
                userWords += choice1 + " "
                # Adding the word to the dictionary text file.
                editingDictionary.write(choice1)
                editingDictionary.write("\n")
                
            elif userChoice == "2":
                print("Auto-correcting",'"'+userText+'"',"to",choice2+".")
                print()
                dictionary.append(choice2)
                userWords += choice2 + " "
                # Adding the word to the dictionary text file.
                editingDictionary.write(choice2)
                editingDictionary.write("\n")
                
            elif userChoice == "3":
                print("Auto-correcting",'"'+userText+'"',"to",choice3+".")
                print()
                dictionary.append(choice3)
                userWords += choice3 + " "
                # Adding the word to the dictionary text file.
                editingDictionary.write(choice3)
                editingDictionary.write("\n")
                
        
    # Explaining if no matches were found.
    else:
        print("No matches were found.")
        
        # Giving the option to add the unknown word to the dictionary.
        addToDictionary = input("Would you like to add this word to the dictionary? (y/n) ")
        # Using a loop to ensure proper input.
        while addToDictionary.lower() != "y" and addToDictionary.lower() != "n":
            print()
            print("Invalid input.")
            addToDictionary = input("Would you like to add this word to the dictionary? (y/n) ")
        
        if addToDictionary.lower() == "y":
            dictionary.append(userText.lower())
            print("The word",'"'+userText.lower()+'"',"has been added to the dictionary.")
            userWords += userText.lower() + " "
            # Adding the word to the dictionary text file.
            editingDictionary.write(userText.lower())
            editingDictionary.write("\n")
        print()

# Printing the user's words after they've quit.
print()
print("Your words:")
print(userWords[:-1]+".")

dictionaryFile.close()
editingDictionary.close()
