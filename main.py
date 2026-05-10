from database import create_database
from redundancy import add_employee, show_all_employees

def main():
    # 1. Create Database
    create_database()
    
    print("\n🚀 REDUNDANCY REMOVAL SYSTEM — CodeAlpha\n")
    
    # 2. Add test data
    print("--- Adding initial data ---")
    add_employee("Hiba Bendimerad", "hiba@gmail.com", "Telecommunications")
    add_employee("Sara Amrani",     "sara@gmail.com",  "computer science")
    add_employee("Karim Belhadj",   "karim@gmail.com", "network")
    
    # 3. show database 
    show_all_employees()
    
    # 4. test duplicates
    print("--- Test with duplicates ---")
    add_employee("Hiba Duplicate",  "hiba@gmail.com",  "Autre")   # ← duplicates !
    add_employee("Sara 2",          "sara@gmail.com",  "Autre")   # ← duplicates !
    add_employee("Nassim Hadj",     "nassim@gmail.com","Security") # ← unique ✅
    
    # 5. show final database
    show_all_employees()

if __name__ == "__main__":
    main()