from src.controllers.BaseController import BaseController
import re
from src.models.order_details import OrderDetail
from src.models.images import Image


class OrderDetailController(BaseController):

    def __init__(self):
        super().__init__(model=OrderDetail)

