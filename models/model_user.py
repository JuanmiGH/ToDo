from entities.user import User

class ModelUser():

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.cursor()
            sql = "SELECT id, name, mail, password, img FROM usr WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            
            if row != None:
                return User(row[0], row[1], row[2], None, row[4])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)