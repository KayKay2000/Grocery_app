

def percentage_plus(bill, tip):
    return (float(bill) * float(tip)/100 + float(bill))  


def tip_calculator():
    bill = input("What is the bill total? ")
    tip = input("What percentage is the tip? ")
    total_bill= percentage_plus(bill,tip)
    print(f"What is the total bill? {bill} \nWhat percentage would you like to tip? {tip} \nTotal bill is {total_bill}")


tip_calculator()