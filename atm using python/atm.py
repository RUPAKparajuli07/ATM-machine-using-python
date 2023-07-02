import tkinter as tk
from tkinter import font


class ATM:
    def __init__(self):
        self.balance = 1000

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. Current balance is {self.balance}."
        else:
            raise ValueError("Invalid input.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return f"Withdrew {amount}. Current balance is {self.balance}."
        elif amount <= 0:
            raise ValueError("Invalid input.")
        else:
            return "Insufficient funds."


def check_balance_label():
    balance = atm.check_balance()
    result_label.config(text=f"Your current balance is: {balance}")


def deposit_button():
    try:
        amount = float(deposit_entry.get())
        result = atm.deposit(amount)
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Invalid input.")


def withdraw_button():
    try:
        amount = float(withdraw_entry.get())
        result = atm.withdraw(amount)
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Invalid input.")


def enter_key(event):
    # Determine the widget where the Enter key was pressed
    widget = event.widget
    if widget == deposit_entry:
        deposit_button()
    elif widget == withdraw_entry:
        withdraw_button()


atm = ATM()

window = tk.Tk()
window.title("ATM Machine")
window.geometry("1200x800")

# Increase font size by 30 times
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=12 * 30)

check_balance_button = tk.Button(window, text="Check Balance", command=check_balance_label)
check_balance_button.configure(font=("Times New Roman", 30), fg="darkred", bg="black")
check_balance_button.pack(pady=10)

deposit_label = tk.Label(window, text="Deposit Amount:")
deposit_label.configure(font=("Times New Roman", 30), fg="darkred", bg="black")
deposit_label.pack()
deposit_entry = tk.Entry(window, font=("Times New Roman", 30))
deposit_entry.configure(fg="darkred", bg="black")
deposit_entry.pack()
deposit_entry.bind("<Return>", enter_key)  # Bind Enter key event

deposit_button = tk.Button(window, text="Deposit", command=deposit_button)
deposit_button.configure(font=("Times New Roman", 30), fg="darkred", bg="black")
deposit_button.pack(pady=10)

withdraw_label = tk.Label(window, text="Withdraw Amount:")
withdraw_label.configure(font=("Times New Roman", 30), fg="darkred", bg="black")
withdraw_label.pack()
withdraw_entry = tk.Entry(window, font=("Times New Roman", 30))
withdraw_entry.configure(fg="darkred", bg="black")
withdraw_entry.pack()
withdraw_entry.bind("<Return>", enter_key)  # Bind Enter key event

withdraw_button = tk.Button(window, text="Withdraw", command=withdraw_button)
withdraw_button.configure(font=("Times New Roman", 30), fg="darkred", bg="black")
withdraw_button.pack(pady=10)

# Set "Save Money" text alignment to the left and center the output screen text
save_money_text = tk.Label(window, text="\n Spend wisely today, save generously for tomorrow.\n")
save_money_text.configure(font=("Georgia", 30), fg="orange", bg="black", anchor="w")
save_money_text.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.configure(font=("Times New Roman", 50), fg="darkred", bg="black")
result_label.pack(pady=10)

window.configure(bg="black")
window.mainloop()
