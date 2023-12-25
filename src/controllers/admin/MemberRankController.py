from src.controllers.BaseController import BaseController
import re
from src.models.member_ranks import MemberRank
from src.models.images import Image


class MemberRankController(BaseController):

    def __init__(self):
        super().__init__(model=MemberRank)

    # Lấy ra thông tin rank dựa vào số tiền
    def getRankByPrice(self, price):
        try:
            self.connection.connect()
            return self.connection.session.query(MemberRank).filter(MemberRank.spending <= price).order_by(MemberRank.spending.desc()).first()
        except Exception as E:
            print(E)
            return

        finally:
            self.connection.close()


