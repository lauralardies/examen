# Player 1 --> Plays with vowels

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

# Player 2 --> Plays with consonants

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

banana = list(input("Choose your string of the word banana: "))
pyramid(banana)
points(banana)