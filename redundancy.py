import sqlite3

def is_duplicate(email):
    """Verify if email already exist in the database"""
    conn = sqlite3.connect("cloud_data.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM employees WHERE email = ?", (email,))
    result = cursor.fetchone()
    
    conn.close()
    return result is not None  #True = duplicate, False = unique

def add_employee(name, email, department):
    """Adds an employee only if not duplicated"""
    if is_duplicate(email):
        print(f"❌ DUPLICATE DETECTED : '{email}' already exists → Not added")
        return False
    
    conn = sqlite3.connect("cloud_data.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO employees (name, email, department)
        VALUES (?, ?, ?)
    """, (name, email, department))
    
    conn.commit()
    conn.close()
    print(f"✅ '{name}' successfully added !")
    return True

def show_all_employees():
    """Shows all employees in the database"""
    conn = sqlite3.connect("cloud_data.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    
    conn.close()
    
    print("\n📋 --- CURRENT DATABASE ---")
    if not employees:
        print("   (empty)")
    for emp in employees:
        print(f"   ID:{emp[0]} | {emp[1]} | {emp[2]} | {emp[3]} | {emp[4]}")
    print("----------------------------------\n")