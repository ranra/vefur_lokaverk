import pymysql
from app.routes import *




conn = pymysql.connect(host='tsuts.tskoli.is', user='2209922929', passwd='mypassword',db='2209922929_vefur')
cur = conn.cursor()

def get_img():
    img_list=[]
    cur.execute("SELECT * FROM images")
    for row in cur:
        img_list.append(row[2])
    return img_list




def create( username, name, email, password):
    cur.execute(
        "Insert into users values('{}','{}','{}','{}')".format(username, name, email, password))
    conn.commit()
    cur.execute("SELECT * FROM users")




def check():
    cur.execute("SELECT * FROM users")
    for row in cur:
       print(row)





def img_insert():
    try:
        with conn.cursor() as cursor:
            for i in range(len(image_names)):
                sql = "INSERT INTO `images` (`img_id`,`img_name`, `img_link`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (str(i), "mynd", image_names[i]))
        conn.commit()
    finally:
        print("done")
        conn.close()




