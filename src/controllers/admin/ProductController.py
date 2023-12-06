from src.controllers.BaseController import BaseController
import re
from src.models.products import Product
from src.models.images import Image


class ProductController(BaseController):

    def __init__(self):
        super().__init__(model=Product, model_name="product")

