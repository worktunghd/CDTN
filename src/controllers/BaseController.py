from src.database.ConnectDatabase import ConnectMySQL
from mysql import connector
from src.enums.enums import *
from dataclasses import dataclass, asdict
from sqlalchemy.orm.util import class_mapper
from sqlalchemy.exc import SQLAlchemyError
from src.views.common.Common import warningMessagebox

class BaseController:

    def __init__(self, model):
        self.connection = ConnectMySQL()
        self.model = model

    def getDataByModel(self):
        return self.connection.getDataByModel(self.model)

    def insertDataMultipleWithModel(self, data):
        return self.connection.insertDataMultipleWithModel(data)

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

    def insertDataWithModelRelation(self, data, other_data=None):
        try:
            with self.connection.session.begin_nested():
                self.connection.session.add(data)
                # xử lý cập nhât, thêm mới cho các bản ghi khác
                for other in other_data:
                    action = other.get('action', None)
                    data = other.get('data', [])
                    data_dict = []
                    other_model = None
                    if isinstance(data, dict):
                        data = list(data.values())
                    for item in data:
                        other_model = item.__class__
                        item_dict = vars(item)
                        item_dict.pop('_sa_instance_state', None)
                        data_dict.append(item_dict)
                    if action == FormMode.ADD.value and other_model:
                        print(1)
                    elif action == FormMode.EDIT.value and other_model:
                        # update data
                        self.connection.session.bulk_update_mappings(other_model, data_dict)

                self.connection.session.commit()
                return True

        except SQLAlchemyError as e:
            print(e)
            self.connection.session.rollback()
            raise e

    def updateDataTest(self, item_data, relations_data):
        try:
            with self.connection.session.begin_nested():
                model_data = vars(item_data)
                # Loại bỏ trường '_sa_instance_state' nếu tồn tại
                model_data.pop('_sa_instance_state', None)
                query = self.connection.session.query(self.model).filter(self.model.id == model_data.get('id', ''))
                query.update(model_data)
                data = query.first()
                for relation_name in relations_data:
                    relationship_instance = getattr(data, relation_name, None)


                self.connection.session.commit()
                return True

        except SQLAlchemyError as e:
            print(e)
            self.connection.session.rollback()
            raise e


    def updateDataWithModelRelation(self, item_data, relations_data, other_data=None):
        try:
            with self.connection.session.begin_nested():
                model_data = vars(item_data)
                # Loại bỏ trường '_sa_instance_state' nếu tồn tại
                model_data.pop('_sa_instance_state', None)
                query = self.connection.session.query(self.model).filter(self.model.id == model_data.get('id', ''))
                query.update(model_data)
                data = query.first()
                for relation in relations_data:
                    if getattr(self.model, relation, None):
                        self.process_relation_with_request(class_mapper(self.model).get_property(relation).mapper.class_, relations_data.get(relation, {}), getattr(data, relation, []))
                    else:
                        warningMessagebox("Đã xảy ra lỗi")
                        return

                # xử lý cập nhât, thêm mới cho các bản ghi khác
                for other in other_data:
                    action = other.get('action', None)
                    data = other.get('data', [])
                    data_dict = []
                    other_model = None
                    if isinstance(data, dict):
                        data = list(data.values())
                    for item in data:
                        other_model = item.__class__
                        item_dict = vars(item)
                        item_dict.pop('_sa_instance_state', None)
                        data_dict.append(item_dict)
                    if action == FormMode.ADD.value and other_model:
                        print(1)
                    elif action == FormMode.EDIT.value and other_model:
                        # update data
                        self.connection.session.bulk_update_mappings(other_model, data_dict)

                self.connection.session.commit()
                return True

        except SQLAlchemyError as e:
            print(e)
            self.connection.session.rollback()
            raise e

    # xử lý cập nhật, sửa, xóa cho relation
    def process_relation_with_request(self, relation_model, data, data_old):
        # Tạo một từ điển để lưu trữ các bản ghi trong mối quan hệ theo uuid
        try:
            data_old = {model.id: model for model in data_old}
            update = []
            insert = []
            # Duyệt qua danh sách items và cập nhật hoặc thêm mới các bản ghi vào mối quan hệ
            for item in data:
                # kiểm tra nếu có id (đã tồn tại trong db) thì cập nhật
                item_id = item.get('id', None)
                if item_id in data_old:
                    data_old.pop(item_id)
                    update.append(item)
                else:
                    insert.append(item)
            # update data
            self.connection.session.bulk_update_mappings(relation_model, update)
            # delete data
            self.connection.session.query(relation_model).filter(relation_model.id.in_((list(data_old.keys())))).delete()
            # insert data
            self.connection.session.bulk_insert_mappings(relation_model, insert)
        except Exception as E:
            print(f"{E} - file BaseController function process_relation_with_request")
            return


    def getDataByIdWithModel(self, model_id):
        return self.connection.getDataByIdWithModel(self.model, model_id)

    def getDataByModelIdWithRelation(self, model_id):
        return self.connection.getDataByModelIdWithRelation(self.model, model_id)

    def deleteDataMutipleWithModel(self, ids):
        return self.connection.deleteDataMutipleWithModel(self.model, ids)

    def updateOrInsert(self, data):
        self.connection.updateOrInsert(data)

    def deleteDataWithModel(self, model_id):
        return self.connection.deleteDataWithModel(self.model, model_id)

    # kiểm tra data đã tồn tại khi insert
    def checkExitsDataWithModel(self, column, data):
        return self.connection.findFirstWithColumnByModel(self.model, column, data)

    # kiểm tra data đã tồn tại khi update
    def checkExitsDataUpdateWithModel(self, column, data, model_id):
        return self.connection.findFisrtWithColumnWithoutIdByModel(self.model, column, data, model_id)

    def searchData(self, search_column, search_text, order_columns=['created_at']):
        return self.connection.searchData(self.model, search_column, search_text, order_columns)