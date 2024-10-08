#Remove duplicate numbers from array and create a new one without duplicates
# "use" is allowed, "in" is not

numbers: list[int] = [13, 10, 22, 18, 32, 39, 21, 5, 33, 15, 18, 2, 9, 31, 15, 7, 28, 18]

clean_array: list[int]= []

clean_array = list(set(numbers))


print("La lista", numbers, "tiene", len(numbers), "elementos")
print("La lista", clean_array, "tiene", len(clean_array), "elementos")


"""
I can't use this 🤡
It is good tho

for number in numbers:
    if number not in clean_array:
        clean_array.append(number)

"""