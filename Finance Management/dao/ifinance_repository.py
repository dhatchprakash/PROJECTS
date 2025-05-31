import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from abc import ABC, abstractmethod
from entity.expense import Expense
from entity.user import User

class IFinanceRepository(ABC):
    @abstractmethod
    def create_user(self, user: User) -> bool:
        pass

    @abstractmethod
    def create_expense(self, expense: Expense) -> bool:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def delete_expense(self, expense_id: int) -> bool:
        pass

    @abstractmethod
    def get_all_expenses(self, user_id: int) -> list:
        pass

    @abstractmethod
    def update_expense(self, user_id: int, expense: Expense) -> bool:
        pass



if __name__ == "__main__":
    print("Imports are working! Interface file is running.")
