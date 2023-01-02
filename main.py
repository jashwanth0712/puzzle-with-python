import mysql.connector as mys
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'chiru',
  'raise_on_warnings': True
}
cnx = mys.connect(**config)
#-----------------------creating game data -----------------------
mycursor = cnx.cursor()
def create_table():
  mycursor.execute('create table game(one varchar(2),two varchar(2),three varchar(2),four varchar(2),five varchar(2),six varchar(2),seven varchar(2),eight varchar(2),nine varchar(2),ten varchar(2),eleven varchar(2),twelve varchar(2))')
  #filling all the answers
def drop_table():
  mycursor.execute('DROP TABLE game')
def insert_game_data():  
  horizontal ={'2,5':'ACTUAL', '3,7':'APPEND','5,1':'INSERT','6,4':'PACKET','8,4':'DELETE'}
  # horizontal ={'2,five':'ACTUAL', '3,seven':'APPEND','5,one':'INSERT','6,four':'PACKET','8,four':'DELETE'}
  vertical={'1,8':'TUPLE','3,12':'DROP','2,5':'AVERAGE','3,2':'BANDWIDTH',}

  sql = "INSERT INTO game (one ,two ,three ,four ,five ,six ,seven ,eight ,nine ,ten ,eleven ,twelve ) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s)"
  val=[]
  #code to add horizontal elements 
  for i in range(11):
    l=[' ']*12
    val.append(l)
  for i in horizontal:
    k=i.split(',')
    init=int(k[1])
    for j in horizontal[i]:
      print(int(k[0]),init)
      val[int(k[0])-1][init-1]=j
      init+=1
  #code to add vertical elements 
  for i in vertical:
      k=i.split(',')
      init = int(k[0])
      for j in vertical[i]:
          print(init,int(k[1]))
          val[init-1][int(k[1])-1]=j
          init+=1
  # code to print the puzzle  answer  
  def print_ans():
      for i in val:
          for j in i:
              print(j,end=" ")
          print()

  mycursor.executemany(sql, val)
  print("created table")
  cnx.commit()
# create_table()
# insert_game_data()
drop_table()
print("1.The parameters which we use in the function call or the parameters which we use to send the values/data during the function call")
print('2.the function used to find the mean value')
print('3.function used to add new record in a table')
print('4.datatype which is immutable and is similar to lists')
print('5._________ switching is the transfer of small pieces of data of fixed sizes across various networks')
print('6._________ mode is used to write data in a file without deleting previous data')
print('7.________ function is used to delete a table from a database')
print('8.the difference between the highest frequency and the lowest frequency in which the data is being shared is called')
print('9.________ is a function which deletes paricular record according to the condition in sql')

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


print('****GAME OVER****')

cnx.close()
