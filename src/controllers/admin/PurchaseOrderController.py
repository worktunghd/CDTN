from src.controllers.BaseController import BaseController
import re
from src.models.PurchaseOrders import PurchaseOrders


class PurchaseOrderController(BaseController):

    def __init__(self):
        super().__init__(model=PurchaseOrders)

