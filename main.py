from crud import get_all_transactions
from database.models import init_db
from utils.helpers import print_menu


def main():
    init_db()
    while True:
        print_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            print("Добавление транзакции")

        elif choice == "0":
            print("Выход")


        elif choice == "2":
            transactions = get_all_transactions()
            for row in transactions:
                print(f"{row[4]} | {row[2]}: {row[1]} руб. ({row[5]})")

if __name__ == "__main__":
    main()



