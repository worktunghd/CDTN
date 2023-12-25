from src.controllers.BaseController import BaseController
import re
from src.models.customers import Customer
from src.models.images import Image


class CustomerController(BaseController):

    def __init__(self):
        super().__init__(model=Customer)

    def delete_customer(self, customer_id):
        try:
            self.connection.connect()
            customer = self.connection.session.query(Customer).filter_by(id=customer_id).first()
            customer.orders.delete()
            print(customer.orders)
        except Exception as E:
            print(f"{E} - file CustomerController function delete_customer")
            return
        finally:
            self.connection.close()