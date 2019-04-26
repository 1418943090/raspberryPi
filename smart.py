import time,os,pymysql
connecting=""
def mysql_con():
    global connecting
    connecting=pymysql.connect(
          host="localhost",
          user="root",
      password="huang110",
            db="lot",
       charset="utf8"
      )
    cur=connecting.cursor()
    return cur
#**************
fp=open("mqtt.txt",'a')
#******************************
while 1:
    cur=mysql_con()
    cur.execute("use lot")
    cur.execute("select * from smart")
    data=cur.fetchall()
    for row in data:
        if row[6]=='on':
            cur.execute("use lot")
            cur.execute("select * from now_data where name='%s'"%row[1])
            row1=cur.fetchall()
            if((row[2]=="less" and row1[0][2]<=row[3] )or(row[2]=="more" and row1[0][2]>row[3] )):
                equ_array=row[5].split(',')
                for equ in equ_array:
                    cur.execute("use lot")
                    cur.execute("select id,status from node_information where name='%s'"%equ)
                    equ=cur.fetchall()
                    if(row[4]!=equ[0][1]):
                      code=equ[0][0]+":"+row[4]
                      print(code)
                      fp.writelines("%s\n"%code)#将指令写入文档中
                      fp.flush()
                      cur.execute("update node_information set status='%s' where id='%s'"%(row[4],equ[0][0]))
                      connecting.commit()
            
    time.sleep(6)
fp.close()
cur.close()
connecting.close()
    
