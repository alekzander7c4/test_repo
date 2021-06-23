import pymysql


DB_HOST = ''
DB_NAME = ''
DB_PASS = ''
DB_USER = ''


class OpenSQL:

    def __init__(self, db_host, db_user, db_pass, db_name):
        self._db_host = db_host
        self._db_user = db_user
        self._db_pass = db_pass
        self._db_name = db_name

    def __enter__(self):
        self._connect = pymysql.connect(self._db_host,
                                        self._db_user,
                                        self._db_pass,
                                        self._db_name,
                                        cursorclass=pymysql.cursors.DictCursor)
        return self._connect

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connect.commit()
        self._connect.close()
        if exc_type:
            raise exc_type(exc_val)


class TestDB:

    def __init__(self):
        self._db_host = DB_HOST
        self._db_user = DB_USER
        self._db_pass = DB_PASS
        self._db_name = DB_NAME

    def get_test_data(self):
        # with OpenSQL(self._db_host, self._db_user, self._db_pass, self._db_name) as conn:
        #     cursor = conn.cursor()
        #     cursor.execute('SQL query;')
        #     return cursor.fetchone()
        pass
