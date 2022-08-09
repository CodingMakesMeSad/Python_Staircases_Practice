#testing functions, global varibles
# x = input("Enter a number, 1-9: ")
# int_x = int(x)



# Staircase
def Staircase():
    c = int_x
    for i in range(c+1):
        for z in range(i):
            print(i, end=" ")
        print(" ")

# Inverted Staircase
def Inverted_Staircase():
    b = 0
    for i in range(int_x, 0 ,-1):
        b += 1
        for z in range(1, i + 1):
            print(b, end=" ")
        print(" ")

# Staircase (but with same digit)
def Same_Digit_Staircase():
    c = int_x
    b = 0
    for i in range(c):
        for z in range(i +1):
            print(c, end=" ")
            b += 1
        print(" ")

# Inverted Staircase (but with same digit)
def Same_Digit_Inverted_Staircase():
    c = int_x
    for i in range(c, 0, -1):
        for z in range(1, i + 1):
            print(c, end=" ")
        print(" ")

#Staircase_Inverted_Number
def Staircase_Inverted_Number():
    c = int_x
    for i in range(c +1):
        for z in range(i +1):
            print(z, end=" ")
        print(" ")


#Inverted_Staircase_Inverted_Number
def Inverted_Staircase_Inverted_Number():
    c = int_x
    for i in range(c, 0, -1):
        for z in range(0, i +1):
            print(z, end=" ")
        print(" ")
    print("0")

#Alternating_Odd_Staircase
def Alternating_Odd_Staircase():
    c = int_x
    i = 1
    while i <= c:
        z = 1
        while z <= i:
            print((i * 2 - 1), end=" ")
            z = z +1
        i = i + 1
        print(" ")
# Dislike how it runs bUt ItS pRoPeR

# Alternating_Even_Staircase
def Alternating_Even_Staircase():
    c = int_x
    i = 1
    while i <= c:
        z = 1
        while z <= i:
            print((i * 2), end=" ")
            z = z +1
        i = i + 1
        print(" ")

try:
    print("Staircase, type 1")
    print("Inverted_Staircase, type 2 ")
    print("Same_Digit_Staircase, type 3")
    print("Same_Digit_Inverted_Staircase, type 4")
    print("Staircase_Inverted_Number, type 5")
    print("Inverted_Staircase_Inverted_Number, type 6")
    print("Alternating_Odd_Staircase, type 7")
    print("Alternating_Even_Staircase, type 8")
    type = input("Enter what kind of staircase you want: ")
    int_type = int(type)

    x = input("Enter a number, 1-9: ")
    int_x = int(x)

    commands = {
      1: Staircase,
      2: Inverted_Staircase,
      3: Same_Digit_Staircase,
      4: Same_Digit_Inverted_Staircase,
      5: Staircase_Inverted_Number,
      6: Inverted_Staircase_Inverted_Number,
      7: Alternating_Odd_Staircase,
      8: Alternating_Even_Staircase,
    }
    commands[int_type]()
except:
    print("Are you sure you entered a valid number(s)?")
#Add that it loops until 0 is written
#Remove _ from prompt menu

input("Press ENTER to exit")

#Testing functions, don't forget to un/comment top of page
# Staircase()
# Inverted_Staircase()
# Same_Digit_Staircase()
# Same_Digit_Inverted_Staircase()
# Staircase_Inverted_Number()
# Inverted_Staircase_Inverted_Number()
# Alternating_Odd_Staircase()
# Alternating_Even_Staircase()
