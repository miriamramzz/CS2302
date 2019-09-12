#########################################################################
#                          Lab 1 - Recursion                            #
#########################################################################

#Function that creates the anagrams given the word and the index
def makeAnagram(word, index):
    if index > (len(word)-1):
        return word
    else: #index has not reached the end
        #initialize the new word to the the first given character
        new_word = word[index]
        #execute permutations until index of the first letter is equal to max index
        if index != (len(word) - 1):
            new_word.join(word[index + 1])
        return makeAnagram(word, index+1)
                
        
#Use this method to find the word inputted by the user and search for the word
# in faster time than if done linearly with a for loop
def search4Word(L, key):
    middle = 0
    low = 0;
    high = len(L)-1
    while(high >= low):
        middle = int((high + low)/2)
        if(L[middle] < key): #search the right subtree
            low = middle + 1
            #print("Current: ", L[low])
        elif(L[middle] > key): #search the left subtree
            high = middle - 1
        else:
            print("Word Found"); #middle is found
            return makeAnagram(key, 0);
    print("Not found")  #key not in list

def main():
    #Ask for the word that the user would like to get the anagram of
    userInput = input("Enter a word: ")
    
    #variable wordFile will save the address of the file name given?
    #wordFile = open('words_alpha.txt')
    
    #create an empty set to store the words
    wordList = []

    #for loop will add the contents of the file one line at a time into list
    with open('words_alpha.txt', 'r') as wordFile:
        for word in wordFile:
            wordList.append(word.split())
            #word_Set.add(words) #add function adds each word into the set            
    #print(wordList)
    #print(wordList[3]) #test           
           
    #search4Word(wordList, userInput)
    print(len(wordList))

main()

#TESTING METHODS
#new_W = makeAnagram("meow",0)
#print(new_W)