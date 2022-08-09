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
#Added alternative, Alternating_Odd_Staircase_Cut_Off and Even_Cut_off

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

def Alternating_Odd_Staircase_Cut_Off():
        c = int_x
        i = 1
        if int_x == 1 or int_x == 2 or int_x == 3 or int_x == 4:
            Alternating_Odd_Staircase()
        else:
            four = 4
            while i <= four:
                z = 1
                while z <= i:
                    print((i * 2 - 1), end=" ")
                    z = z +1
                i = i + 1
                print(" ")
            print("Number too big, limit is 4.")

def Alternating_Even_Staircase_Cut_Off():
    c = int_x
    i = 1
    if int_x == 1 or int_x == 2 or int_x == 3 or int_x == 4:
        Alternating_Even_Staircase()
    else:
        four = 4
        while i <= four:
            z = 1
            while z <= i:
                print((i * 2), end=" ")
                z = z +1
            i = i + 1
            print(" ")
        print("Number too big, limit is 4")

try:
    print("Staircase, type 1")
    print("Inverted Staircase, type 2 ")
    print("Same Digit Staircase, type 3")
    print("Same Digit Inverted Staircase, type 4")
    print("Staircase Inverted Number, type 5")
    print("Inverted Staircase Inverted Number, type 6")
    print("Alternating Odd Staircase, type 7")
    print("Alternating Even Staircase, type 8")
    print("Alternating Odd Staircase Cut Off, type 9")
    print("Alternating Even Staircase Cut Off, type 10")
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
      9: Alternating_Odd_Staircase_Cut_Off,
      10: Alternating_Even_Staircase_Cut_Off,
    }
    commands[int_type]()
except:
    print("Are you sure you entered a valid number(s)?")


repeat = input("Do you want to continue? Y/N: ")

while repeat.lower().startswith('y'):
    try:
        print("Staircase, type 1")
        print("Inverted Staircase, type 2 ")
        print("Same Digit Staircase, type 3")
        print("Same Digit Inverted Staircase, type 4")
        print("Staircase Inverted Number, type 5")
        print("Inverted Staircase Inverted Number, type 6")
        print("Alternating Odd Staircase, type 7")
        print("Alternating Even Staircase, type 8")
        print("Alternating Odd Staircase Cut Off, type 9")
        print("Alternating Even Staircase Cut Off, type 10")
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
          9: Alternating_Odd_Staircase_Cut_Off,
          10: Alternating_Even_Staircase_Cut_Off,
        }
        commands[int_type]()
    except:
        print("Are you sure you entered a valid number(s)?")
    repeat = input("Do you want to continue? Y/N: ")

else:
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
