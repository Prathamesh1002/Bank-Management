import datetime

# Initialize the transaction log file with a header
with open("transaction.txt", 'a') as e:
    e.write("AC_No,Amount,Operation,Date\n")

class User:
    def check_balance(self, AC_No):
        try:
            with open("data.txt", "r") as fp:
                for line in fp:
                    s = line.strip().split(',')
                    if s[0] == str(AC_No):
                        print(f"Account Details: {line}")
                        return
                print("Account not found.")
        except FileNotFoundError:
            print("Account information file not found.")

    def deposit_money(self, AC_No, amount):
        try:
            with open("data.txt", "r") as file:
                accounts = file.readlines()
            updated_accounts = []
            deposit_successful = False

            for account in accounts:
                account_data = account.strip().split(',')
                if account_data[0] == str(AC_No):
                    current_balance = int(account_data[2])
                    new_balance = current_balance + amount
                    account_data[2] = str(new_balance)
                    deposit_successful = True
                updated_accounts.append(','.join(account_data))

            with open("data.txt", "w") as file:
                file.writelines(updated_accounts)

            if deposit_successful:
                print(f"Deposited {amount} into Account No. {AC_No}")

                # Log the deposit in the transaction log
                transaction_info = f"{AC_No},{amount},Deposit,{datetime.datetime.now()}\n"
                with open("transaction.txt", "a") as log_file:
                    log_file.write(transaction_info)
            else:
                print(f"Account No. {AC_No} not found.")
        except FileNotFoundError:
            print("Account information file not found.")

    def withdraw_money(self, AC_No, amount):
        try:
            with open("data.txt", "r") as file:
                accounts = file.readlines()
            updated_accounts = []
            withdraw_successful = False

            for account in accounts:
                account_data = account.strip().split(',')
                if account_data[0] == str(AC_No):
                    current_balance = int(account_data[2])
                    if current_balance >= amount:
                        new_balance = current_balance - amount
                        account_data[2] = str(new_balance)
                        withdraw_successful = True
                    updated_accounts.append(','.join(account_data))
                else:
                    updated_accounts.append(account)

            with open("data.txt", "w") as file:
                file.writelines(updated_accounts)

            if withdraw_successful:
                print(f"Withdrew {amount} from Account No. {AC_No}")

                # Log the withdrawal in the transaction log
                transaction_info = f"{AC_No},{amount},Withdrawal,{datetime.datetime.now()}\n"
                with open("transaction.txt", "a") as log_file:
                    log_file.write(transaction_info)
            else:
                print(f"Account No. {AC_No} not found or insufficient balance.")
        except FileNotFoundError:
            print("Account information file not found.")

    def transfer_money(self, sender_AC_No, receiver_AC_No, amount):
        try:
            with open("data.txt", "r") as file:
                accounts = file.readlines()
            updated_accounts = []
            transfer_successful = False

            for account in accounts:
                account_data = account.strip().split(',')
                if account_data[0] == str(sender_AC_No):
                    sender_balance = int(account_data[2])
                    if sender_balance >= amount:
                        # Deduct the amount from the sender's account
                        sender_balance -= amount
                        account_data[2] = str(sender_balance)
                        updated_accounts.append(','.join(account_data))
                        transfer_successful = True
                    else:
                        print("Insufficient balance for transfer.")
                elif account_data[0] == str(receiver_AC_No):
                    receiver_balance = int(account_data[2])
                    # Add the amount to the receiver's account
                    receiver_balance += amount
                    account_data[2] = str(receiver_balance)
                    updated_accounts.append(','.join(account_data))
                else:
                    updated_accounts.append(account)

            with open("data.txt", "w") as file:
                file.writelines(updated_accounts)

            if transfer_successful:
                print(f"Transferred {amount} from Account No. {sender_AC_No} to Account No. {receiver_AC_No}")

                # Log the transfer in the transaction log
                transaction_info = f"{sender_AC_No},{amount},Transfer to {receiver_AC_No},{datetime.datetime.now()}\n"
                with open("transaction.txt", "a") as log_file:
                    log_file.write(transaction_info)
            else:
                print(f"Sender Account No. {sender_AC_No} not found or insufficient balance.")
        except FileNotFoundError:
            print("Account information file not found.")

