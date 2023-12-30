from src.controllers.BaseController import BaseController
import re
from src.models.Products import Products
from src.models.Images import Images


class ProductController(BaseController):

    def __init__(self):
        super().__init__(model=Products)

