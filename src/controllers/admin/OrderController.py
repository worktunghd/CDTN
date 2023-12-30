from src.controllers.BaseController import BaseController
import re
from src.models.Orders import Orders
from src.models.Images import Images


class OrderController(BaseController):

    def __init__(self):
        super().__init__(model=Orders)

