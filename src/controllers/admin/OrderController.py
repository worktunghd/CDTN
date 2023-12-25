from src.controllers.BaseController import BaseController
import re
from src.models.orders import Order
from src.models.images import Image


class OrderController(BaseController):

    def __init__(self):
        super().__init__(model=Order)

    def insertOrder(self, order, other_data):
        [
            {
                'action': FormMode.EDIT.value,
                'data': self.product_update,
            },
            {
                'action': FormMode.EDIT.value,
                'data': customer,
            },
        ]