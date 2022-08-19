# Q1) Create a list of 10 random players in football team.
# perform following operations on list and discuss on each output
# Display list, Sorts the list, use remove to Remove the first item with the specified value

# footballPlayers = ["Lionel Messi", "Cristiano Ronaldo", "Neymar", "Robert Lewandowski",
#                    "Kylian Mbappé", "Kevin De Bruyne", "Virgil van Dijk", "Sadio Mané", "Riyad Mahrez", "Erling Haaland"]
# print("Football Players: " + str(footballPlayers))
# footballPlayers.sort()
# print("\nSorted Football Players List: \n" + str(footballPlayers))
# footballPlayers.remove("Virgil van Dijk")
# print("\nAfter removing Virgil van Dijk:\n"+str(footballPlayers))

# Q2) Write a program to randomly select 10 integer elements from range 100 to 200 and find the smallest among all.

# import random

# list1 = []
# for i in range(10):
#     list1.append(random.randint(100, 200))
# tup1 = tuple(list1)
# print("Random Numbers between 100-200 are: " + str(tup1))
# print("The smallest element is: " + str(sorted(tup1)[0]))

# Q 3) Create a dictionary of 5 countries with their currency details and display them.

countries = {
    "India": "Indian Rupee INR",
    "Australia": "Australian dollar AUD",
    "Switzerland": "Swiss franc CHF",
    "United States": "United States dollar USD",
    "United Kingdom": "British pound GBP"
}
print(countries)
