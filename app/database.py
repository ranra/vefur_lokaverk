import pymysql
conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2209922929', passwd='mypassword', db='2209922929_vefur')
cur = conn.cursor()


class Database():
    def __init__(self):
        pass

    def create(self, username, name, password, email):
        cur.execute(
            "Insert into users values('{}','{}','{}','{}')".format(username, name, email, password))
        conn.commit()
        cur.execute("SELECT * FROM users")

    def check(self, username, password):
        cur.execute("SELECT * FROM users")
        for row,col in cur:
            if username in row:
                if password in col:
                    print("loggedin")
