from src.controllers.BaseController import BaseController
import re
from src.models.Customers import Customers
from src.models.Images import Images


class CustomerController(BaseController):

    def __init__(self):
        super().__init__(model=Customers)

    def delete_customer(self, customer_id):
        try:
            self.connection.connect()
            customer = self.connection.session.query(Customers).filter_by(id=customer_id).first()
            customer.orders.delete()
            print(customer.orders)
        except Exception as E:
            print(f"{E} - file CustomerController function delete_customer")
            return
        finally:
            self.connection.close()