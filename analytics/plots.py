import matplotlib.pyplot as plt
from database.crud import get_all_transactions

def show_spending_pie():
    transactions = get_all_transactions()
    # ... логика группировки по категориям
    plt.pie(category_totals, labels=labels, autopct='%1.1f%%')
    plt.title("Расходы по категориям")
    plt.show()