class FDataBase:
       def __init__(self, db):
              self.__db = db
              self.__cur = db.cursor()

       def getMenu(self):
              sql = '''SELECT * FROM Models'''
              try:
                     self.__cur.execute(sql)
                     res = self.__cur.fetchall()
                     result = list(map(list, res))
                     if res:
                            return result
              except:
                     print("Ошибка чтения из БД")
              return []