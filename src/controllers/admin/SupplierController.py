from src.controllers.BaseController import BaseController
import re
from src.models.Suppliers import Suppliers


class SupplierController(BaseController):

    def __init__(self):
        super().__init__(model=Suppliers)

