from src.controllers.BaseController import BaseController
import re
from src.models.OrderDetails import OrderDetails


class OrderDetailController(BaseController):

    def __init__(self):
        super().__init__(model=OrderDetails)

