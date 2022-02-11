# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


f = open("demo.txt", "r")
current_x = 1
current_y = 2
newline = ""
p = ""
turn = 5
fav_food = ""
def convert():
    L = [[""]*9 for n in range(3)]
    line = f.readline()
    print(L)

    # for i in range(len(L)):
    #     print(line[i])

    for i in range(3):
        for j in range(0,9):
            L[i][j] = (line[j])
            print(line[j])
        line = f.readline()
    print(L)
    # print(L[1][2])









def move():
    dir = input("next step?")
    if(dir == "n"):
        newline = f.readline()
        # print(newline[currentindex])


def move2():
    if(turn == 0):
        print("a")

    if("b"):
        turn-1
        print("you hate waking up 9 am in the morning cuz your first class DHUM 1300 is 9:30, so you decided to take a 15min snap"
              " before escaping")

    if("c"):
        print(f"there is a dagger, a rope, a Justin Bieber's platinum CD and {fav_food} ")

    if("w"):
        print("On your back is a floor-to-celing window, it seems you could jump out of it ")
    if("&"):
        print("you tie the rope on the frame of the window and jump off. However, Justin Bieber's platinum CD is so heavy"
              "that the rope cannot hold you. You dead")
        turn-5;



def print_hi(name):

    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    convert()



# The framed and signed photo of Justin Bieber, Dagger, { }
# starting point: back: bed    forward : chest  left: window  right: dark staircase

# staricase: only forward and backward
# turn in total?
# half way: left way is a mysterious door (cleaning supplied )
# s
#