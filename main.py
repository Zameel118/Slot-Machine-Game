MAX_LINES = 3

def deposit():
    while True:
        amount = input("How much would you like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a valid amount")

    return amount

def num_of_lines():
    while True:
        lines = input("Enter how many Lines (1-" + str(MAX_LINES) + "): ")


def main():
    balance = deposit()

main()