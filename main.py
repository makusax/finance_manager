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
            break

if __name__ == "__main__":
    main()



