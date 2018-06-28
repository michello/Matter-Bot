import pymysql.cursors

class MyDB:

  def __init__(self):
    self.conn = pymysql.connect(
      host='localhost',
      port=8080,
      user='root',
      password='',
      db='wms_request_pipeline',
      charset='utf8mb4',
      cursorclass=pymysql.cursors.DictCursor)

    self.conn_cur = self.conn.cursor()

  def query(self, query, params):
    return self.conn_cur.execute(query, (params))

  def delete(self):
    self.conn.close()
