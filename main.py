import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

#Database connection function
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="emp"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error",str(err))

#hi pavan
def clear_fields():
    emp_id_entry.delete(0,tk.END)
    first_entry.delete(0, tk.END)
    last_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)
    country_entry.delete(0, tk.END)
    gender_var.set("")
    btech_var.set(0)
    mtech_var.set(0)
    degree_var.set(0)
    diploma_var.set(0)



#Function to insert data into database
def register_employee():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()

        #Read data
        emp_id = emp_id_entry.get()
        first = first_entry.get()
        last = last_entry.get()
        email = email_entry.get()
        password = pass_entry.get()
        address = address_entry.get()
        phone = phone_entry.get()
        salary = salary_entry.get()
        country = country_entry.get()

        gender = gender_var.get()

        #Education_list
        education_list = []
        if btech_var.get(): education_list.append("B.tech")
        if mtech_var.get(): education_list.append("M.tech")
        if degree_var.get(): education_list.append("Degree")
        if diploma_var.get(): education_list.append("Diploma")
        education = ",".join(education_list)

        query = """
        INSERT INTO employee
        (emp_id, first_name, last_name,email, password,
        address, phone, salary,country, gender, education)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        try:
            cursor.execute(query,(emp_id,first,last, email, password, address,
                                  phone, salary, country, gender, education))
            conn.commit()
            messagebox.showinfo("Success","Employee registered successfully")
            clear_fields()


        except mysql.connector.Error as err:
            messagebox.showerror("Registration Error",str(err))
        finally:
            cursor.close()
            conn.close()


    #GUI_Setup
root = tk.Tk()
root.title("Employee Registration")
root.geometry("1300x900")

#Employee_ID
tk.Label(root,text="Employee ID:").grid(row=0, column=0, padx=5, pady=5)
emp_id_entry = tk.Entry(root)
emp_id_entry.grid(row=0, column=1, padx=5, pady=5)

#First Name
tk.Label(root, text="First Name:").grid(row=1, column=0, padx=5, pady=5)
first_entry = tk.Entry(root)
first_entry.grid(row=1, column=1, padx=5, pady=5)

#Last Name
tk.Label(root,text="Last Name:").grid(row=2, column=0, padx=5, pady=5)
last_entry = tk.Entry(root)
last_entry.grid(row=2, column=1, padx=5, pady=5)

#Email
tk.Label(root,text="Email:").grid(row=3, column=0, padx=5, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=3, column=1, padx=5, pady=5)

#Password
tk.Label(root,text="Password:").grid(row=4, column=0, padx=5, pady=5)
pass_entry = tk.Entry(root,show="*")
pass_entry.grid(row=4, column=1, padx=5, pady=5)

#Address
tk.Label(root,text="Address:").grid(row=5, column=0, padx=5, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=5, column=1, padx=5, pady=5)

#Phone
tk.Label(root,text="Phone:").grid(row=6, column=0, padx=5, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=6, column=1, padx=5, pady=5)

#Salary
tk.Label(root, text="Salary:").grid(row=7, column=0, padx=5, pady=5)
salary_entry = tk.Entry(root)
salary_entry.grid(row=7, column=1, padx=5, pady=5)

#Country
tk.Label(root, text="Country:").grid(row=8, column=0, padx=5, pady=5)
country_entry = tk.Entry(root)
country_entry.grid(row=8, column=1, padx=5, pady=5)

#Gender
tk.Label(root, text="Gender:").grid(row=9, column=0, padx=5, pady=5)
gender_var = tk.StringVar(root)

tk.Radiobutton(root, text="Male", variable = gender_var, value="Male").grid(row=9, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=9, column=1, padx=80, sticky="w")
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").grid(row=9, column=1, padx=160, sticky="w")

#Education(Checkboxes)
tk.Label(root, text="Education:").grid(row=10, column=0, padx=5, pady=5)

btech_var = tk.IntVar()
mtech_var = tk.IntVar()
degree_var = tk.IntVar()
diploma_var = tk.IntVar()

tk.Checkbutton(root, text="B.tech", variable=btech_var).grid(row=10, column=1, sticky="w")
tk.Checkbutton(root, text="M.tech", variable=mtech_var).grid(row=10, column=1, padx=80, sticky="w")
tk.Checkbutton(root, text="Degree", variable=degree_var).grid(row=10, column=1, padx=160, sticky="w")
tk.Checkbutton(root, text="Diploma", variable=diploma_var).grid(row=10, column=1, padx=240, sticky="w")


#Register Button
tk.Button(root, text="Register", command=register_employee, bg="green",padx=40, pady=20).grid(row=11, column=0, columnspan=2, pady=15)


root.mainloop()











