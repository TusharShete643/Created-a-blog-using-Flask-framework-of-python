import pymysql as p

def connect():
    return p.connect(host='localhost',user='root',password='',database='userdt',port=3306)

def adduserdetails(t):
    con=connect()
    cur=con.cursor()
    sql='insert into user values(%s,%s,%s,%s)'
    cur.execute(sql,t)
    con.commit()
    con.close()

def checklgus(t):
    con=connect()
    cur=con.cursor()
    sql='select email,password from user where email=%s'
    cur.execute(sql,t[0])
    data=cur.fetchall()
    con.commit()
    con.close()
    return data