from src.controllers.BaseController import BaseController
import re
from src.models.imports import Import


class ImportController(BaseController):

    def __init__(self):
        super().__init__(model=Import)

