import pymysql as MYSQL
def Connectionpooling():
    db=MYSQL.connect(host='localhost',port=3306,user="root",passwd='Prince@123',db='videostream')
    cmd=db.cursor()
    return db,cmd
