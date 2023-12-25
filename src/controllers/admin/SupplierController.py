from src.controllers.BaseController import BaseController
import re
from src.models.suppliers import Supplier


class SupplierController(BaseController):

    def __init__(self):
        super().__init__(model=Supplier)

