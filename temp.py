val=[]
horizontal ={'2,5,1':'ACTUAL', '3,7,6':'APPEND','5,1,3':'INSERT','6,4,5':'PACKET','8,4,9':'DELETE'}
vertical={'1,8,4':'TUPLE','3,12,7':'DROP','2,5,2':'AVERAGE','3,2,8':'BANDWIDTH',}

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

#to show empty
total=horizontal
total.update(vertical)
for i in val:
    for j in i:
        if(j==' '):
            print('   ',end="")
        else:
            flag=-1
            for g in total:
                k=g.split(",")
                if(int(k[0])==j and int(k[1])==i):
                    flag=int(k[2])
                    break
            if(flag>0):
                print('|',flag,'|',end='')
            else:
                print('|_|',end='')
    print()