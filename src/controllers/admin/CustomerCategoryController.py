from src.controllers.BaseController import BaseController
import re
from src.models.CustomerCategories import CustomerCategories
from src.models.Images import Images


class CustomerCategoryController(BaseController):

    def __init__(self):
        super().__init__(model=CustomerCategories)

    # Lấy ra thông tin rank dựa vào số tiền
    def getRankByPrice(self, price):
        try:
            self.connection.connect()
            return self.connection.session.query(CustomerCategories).filter(CustomerCategories.min_spending <= price).order_by(CustomerCategories.min_spending.desc()).first()
        except Exception as E:
            print(E)
            return

        finally:
            self.connection.close()


