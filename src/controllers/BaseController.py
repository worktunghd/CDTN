from src.database.ConnectDatabase import ConnectMySQL
from mysql import connector

class BaseController:

    def __init__(self, model, model_name):
        self.connection = ConnectMySQL()
        self.model = model
        self.model_name = model_name

    def getDataByModel(self):
        return self.connection.getDataByModel(self.model)

    def getDataByQuery(self, query):
        return self.connection.getDataByQuery(query=query)

    def findFirstByQuery(self, query):
        return self.connection.findFirstByQuery(query=query)

    def insertData(self, data):
        return self.connection.insertData(data)

    def updateDataWithModel(self, data, model_id):
        return self.connection.updateDataWithModel(data, self.model, model_id)

    def updateDataWithQuery(self, data, query):
        return

    def getDataByIdWithModel(self, model_id):
        return self.connection.getDataByIdWithModel(self.model, model_id)


    def deleteDataWithModel(self, model, model_id):
        return self.connection.deleteDataWithModel(model, model_id)

    # kiểm tra data đã tồn tại khi insert
    def checkExitsDataWithModel(self, column, data):
        return self.connection.findFirstWithColumnByModel(self.model, column, data)

    # kiểm tra data đã tồn tại khi update
    def checkExitsDataUpdateWithModel(self, column, data, model_id):
        return self.connection.findFisrtWithColumnWithoutIdByModel(self.model, column, data, model_id)

    def searchData(self, search_column, search_text, order_columns=['created_at']):
        return self.connection.searchData(self.model, search_column, search_text, order_columns)