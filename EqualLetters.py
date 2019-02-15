'''
    Returns the user input word.
'''
def get_user_input():
    return input("\nInsert the word that will be validated: \n")

'''
    Returns a char dictionary with the frequency of each char.
        {Char:Number of appearences}
'''
def fill_char_dictionary(word):
    charDictionary = {}
    for i in word:
        if i in charDictionary:
            charDictionary[i] = charDictionary[i] + 1
        else:
            charDictionary[i] = 1

    return charDictionary

'''
    Returns the index of the different char inside the word
'''
def find_different_char(word, charDictionary):
    differentChar = ""
    for i in charDictionary:
        if charDictionary[i] == 1:
            differentChar = i

    for j in range(0, len(word)):
        if word[j] == differentChar:
            return j

'''
    Checks if there is only one different char in the word.
        True: There is only one different char.
        False: There is more than one different char.
'''
def only_one_different(charDictionary): #bbaab
    charNumber = 0
    for i in charDictionary:
        if charDictionary[i] > 1:
            charNumber += 1
    
    if charNumber == 2:
        return False
    else:
        return True

def main():
    tryAgain = True
    while tryAgain:
        word = get_user_input()

        #Checks if word length is right according to requirements
        if len(word) >= 3 and len(word) <= 9:
            charCounter = fill_char_dictionary(word)
            if len(charCounter) == 2 and only_one_different(charCounter):
                differentCharIndex = find_different_char(word, charCounter)
                print("INDEX " + str(differentCharIndex))
            else:
                print("INVALID INPUT (incorrect content)")
    
        else:
            print("INVALID INPUT (incorrect length)")

        tryAgainAnswer = input("\nDo you want to try another word?(y/n):\n").lower()

        if tryAgainAnswer == "y":
            tryAgain = True
        else:
            tryAgain = False

main()            