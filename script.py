import random

# words=["ironman","thor","hawkeye","wanda","vision"] Can take a list 

# Can get words from a txt file.
f=open(r"C:\Users\catas\OneDrive\Desktop\VS Code Progs\Anagram Game\Dummy_words.txt")
a=f.readline()
words=a.split(",")
print(words)

word=random.choice(words)
# print(word)


jumble="".join(random.sample(word,len(word))) # Adding elements in empty string using sample from word to its length. 
# print(jumble)

chances=3

print("~"*30)
print("~~~Avengers Jumble Bumble~~~")
print("~"*30)

while chances !=0:
    print("The word is", jumble)
    print()

    guess=input("Enter your gussed word: ").lower()
    if guess == word:
        print("Correct Guess--You won!")
        print()
        break

    else:
        chances -=1
        print("Incorrect Guess.")
        print("Remaining chances are: ", chances)
        print()

else:
    print("All your chances are exhausted.")
    print("You lose.")
    print('The correct word is',word)









