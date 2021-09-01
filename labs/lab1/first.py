"""
Name: <Jonathan Helfgott>
<lab1>.py
"""


def test():
    print("The time has come, the Walrus said, To talk of many thing")
def calc_area():
    length = 20
    width = 5/Users/jonathanhelfgott/PycharmProjects/220/venv/bin/python /Users/jonathanhelfgott/PycharmProjects/220/labs/lab1/first.py
Area = 100
Enter the length:
Enter the width: 5
Enter the height:
Volume = 125
Enter the length: 1
Enter the width: 1
Enter the height: 1
Volume = 1
Enter the number of shots: 3
Enter the shots made2
shooting_percentage= 0.6666666666666666
enter number of pounds3
total cost of shipping= : 60.09dollars and cents

Process finished with exit code 0

    area = length * width
    print("Area =", area)



def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)



def calc_rec_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    Height= eval(input("Enter the height: "))
    volume=length * width * Height
    print("Volume =", volume)



def shooting_percentage():
    total_shots=eval(input("Enter the number of shots: "))
    shots_made=eval(input("Enter the shots made"))
    shots_percentage=shots_made/total_shots
    print("shooting_percentage=",shots_percentage)



def coffee():
    coffee_per_pound=eval(input("enter number of pounds"))*10.5
    shipping=coffee_per_pound*.86
    overhead=1.50
    total_cost= coffee_per_pound+shipping+overhead

    print("total cost of shipping= :",str(total_cost) + "dollars and cents")



def main():
    calc_area()
    calc_rec_volume()
    calc_rec_volume()
    shooting_percentage()
    coffee()
main()