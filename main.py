"""
╔════════════════════════════════════════════╗
║   MY FIRST PYTHON PROJECT ✨               ║
║   Expense Tracker Application              ║
║   Started: 2026                            ║
║   This is where my coding journey began!   ║
╚════════════════════════════════════════════╝
"""

expenses = [] # list of expenses in form of dicts. #local data structure

print("Welcome to the Expense Tracker!")

while True:
    print("===M-E-N-U===")
    print("""
          1. Add expenese
          2. view all expense
          3. View total expense
          4. delete expense
          0. exit
          """)
    choice  = int(input("Enter your choice : "))
    
    if (choice == 1):
        date = input("Enter date as dd-mm-yyyy: ")
        category = input("Category like (travel , food ,books?): ")
        amount = float(input("Enter your expenese: "))
        description = input("Any special note: ")
        
        expense= {
            "date": date,
            "category": category,
            "amount" : amount,
            "description" : description
        }
        
        expenses.append(expense)
        
        print("\n Sucessfully Expense added")
    elif(choice == 2 ):
        if(len(expenses) == 0):
            print("No Expenses Found")
        else:
            count=1
            for x in expenses:
                print(f"\n{count}. expense: \nDate: {x['date']},\nAmount: {x['amount']},\nCategory: {x['category']},\nNote: {x['description']}")
                count += 1
                
    elif (choice == 3):
        totalAmt=0
        for x in expenses:
            totalAmt += x["amount"]
        
        print(f"\nTotal Expense: {totalAmt}")
        
    elif (choice == 4):
        if(len(expenses) == 0):
            print("No Expenses Found")
        else:
            count=1
            for x in expenses:
                print(f"\n{count}. expense: \nDate: {x['date']},\nAmount: {x['amount']},\nCategory: {x['category']},\nNote: {x['description']}")
                count += 1
            
            delIndex = int(input("\nEnter the number of the expense you want to delete: "))
            
            if delIndex < 1 or delIndex > len(expenses):
                print("Invalid index!!!")
            else:
                rm = expenses.pop(delIndex - 1)
                print(f"Expense deleted successfully !!!\nDeleted Expense Details: {rm}")
    
    
    elif(choice == 0):
        print("Bye...")   
        print("Hope you use your money wisely")
        break
    
    else:
        print("invaild input!!!")   
        
    
