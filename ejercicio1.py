banana = list("Banana")
banana1 = []
banana2 = []

def sepVowelConsonant(banana, banana1, banana2):
    banana1 = []
    banana2 = []
    for i in range(len(banana)):
        if banana[i] == "a" or banana[i] == "e" or banana[i] == "i" or banana[i] == "o" or banana[i] == "u":
            banana[i] = "Vowel"
        else:
            banana[i] = "Consonant"

    for i in range(len(banana)):
        if banana[i] == "Vowel":
            banana1.append(banana[i])
        if banana[i] == "Consonant":
            banana2.append(banana[i])

# Player 1 --> Plays with vowels (banana1)

def pyramid(banana):
    for i in range(len(banana) + 1):
        line = " "*(len(banana) - i) + printPyramid(banana[0:i])
        print(line)
    return line

def printPyramid(banana):
    solution = ""
    for i in range(len(banana)):
        solution = solution + banana[i] + " "
    return solution

# Player 2 --> Plays with consonants (banana2)

def pyramid2(banana):
    for i in range(len(banana) + 1):
        line = " "*(len(banana) - i) + printPyramid2(banana[0:i])
        print(line)

def printPyramid2(banana):
    solution = ""
    for i in range(len(banana)):
        solution = solution + banana[i] + " "
    return solution

def points(banana):
    stuart_points = 0
    kevin_points = 0
    vocal = 'aeiouAEIOU'
    for i in range (len(banana)):
        if banana[i] not in vocal:
            stuart_points += (len(banana))
        else: 
            kevin_points += (len(banana))
    print ("Stuart has " + str(stuart_points) + " points, and Kevin has " + str(kevin_points) + ".")
    if stuart_points > kevin_points:
        print ("Winner, Stuart")
    elif stuart_points < kevin_points:
        print ("Winner, Kevin")
    else:
        print ("Draw")

pyramid(banana)
pyramid2(banana)
points(banana)