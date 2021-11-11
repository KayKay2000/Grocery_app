

def percentage_plus(bill_amount, tip):
    return (float(bill_amount) * float(tip)/100 + float(bill_amount)) 

def tip_calculator_split():
    bill_amount= input("What is your bill amount? ")
    tip= input("What percentage is your tip? ")
    people= input("How many people are in your party? ")
    total_bill= percentage_plus(bill_amount,tip)
    per_person= float(total_bill)/float(people)
    print(f"What is the total bill? {bill_amount} \nWhat percentage would you like to tip? {tip} \nTotal bill is ${total_bill} \nEach person will pay ${per_person}")

tip_calculator_split()