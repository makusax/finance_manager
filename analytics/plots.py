import matplotlib.pyplot as plt
from database.crud import get_all_transactions


def show_spending_pie():
    transactions = get_all_transactions()
    expenses = [t for t in transactions if t[5] == 'expense']

    categories = {}
    for _, amount, category, _, _, _ in expenses:
        categories[category] = categories.get(category, 0) + amount

    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
    plt.title("Распределение расходов")
    plt.show()