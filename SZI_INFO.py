# class FDataBase:
#        def __init__(self, db):
#               self.__db = db
#               self.__cur = db.cursor()

#        def getMenu(self):
#               sql = f'''SELECT * FROM Models'''
#               try:
#                      self.__cur.execute(sql)
#                      res = self.__cur.fetchall()
#                      result = list(map(list, res))
#                      if res:
#                             return result
#               except:
#                      print("Ошибка чтения из БД")
#               return []


SZI_models = [
    ['Sobol', '62000', 'Несанкционированный доступ', '0.8'],
    ['SecretDisk', '45000', 'Подтверждение авторства', '0.9']
]