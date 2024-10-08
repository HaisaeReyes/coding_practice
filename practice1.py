# string array, verify if the word given is part of the array and return the position index
# do not use "in"

data: list[str] = ["boy", "baloon", "horn", "guitar", "flower", "house", "horse"]

word: str = str(input("Insert a word to verify: "))
i = 0

while i < 7:

    if word == data[i]:
        print("The index for", word,"is", i )
    
    elif (data != i) and (i == 6):
        print("The word given is not on the array")

    i = i + 1
