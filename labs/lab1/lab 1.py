"""
Name: <Jonathan Helfgott>
<lab1>.py
"""


def test():
    print("The time has come, the Walrus said, To talk of many thing")

def calc_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
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