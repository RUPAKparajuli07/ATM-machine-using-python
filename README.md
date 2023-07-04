
<body>
  <h1>ATM Machine Documentation</h1>

  <h2>Introduction</h2>
  <p>
    This is a simple ATM (Automated Teller Machine) machine program implemented using the Tkinter library in Python. The program allows users to perform basic banking operations such as checking the account balance, making deposits, and withdrawing funds.
  </p>

  <h2>Classes</h2>
  <h3>ATM</h3>
  <pre>
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
  </pre>

  <h2>Functions</h2>
  <pre>
def check_balance_label():
    # Retrieves the current account balance and updates the result label

def deposit_button():
    # Retrieves the deposit amount, calls the deposit method, and updates the result label

def withdraw_button():
    # Retrieves the withdrawal amount, calls the withdraw method, and updates the result label

def enter_key(event):
    # Determines the widget where the Enter key was pressed and calls the corresponding button function

  </pre>

  <h2>GUI Elements</h2>
  <p>
    The program creates a graphical user interface (GUI) using the Tkinter library. The main GUI window contains several elements:
  </p>

  <pre>
check_balance_button: Button - "Check Balance"
deposit_label: Label - "Deposit Amount:"
deposit_entry: Entry - Input field for deposit amount
deposit_button: Button - "Deposit"
withdraw_label: Label - "Withdraw Amount:"
withdraw_entry: Entry - Input field for withdrawal amount
withdraw_button: Button - "Withdraw"
save_money_text: Label - Text encouraging wise spending and saving
result_label: Label - Displays the result of deposit or withdrawal operations
  </pre>

  <h2>Running the Program</h2>
  <p>
    To run the program, execute the Python script. A GUI window titled "ATM Machine" will open, allowing users to interact with the ATM interface. They can check their account balance, make deposits, and withdraw funds. The result of each operation is displayed in the result label area.
  </p>

  <h2>Dependencies</h2>
  <p>
    The program requires the Tkinter and font modules from the Tkinter library, which are imported at the beginning of the code. These modules are typically included with standard Python installations, so no additional installation should be necessary.
  </p>

  <p>
    Please note that this documentation assumes a basic understanding of Python programming and the Tkinter library.
  </p>
</body>
</html>
