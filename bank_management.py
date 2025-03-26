import os
class bankmgmt:
    def addadmin(self,e):
        fp=open("data.txt",'a')
        fp.write(str(e))
        fp.close()
    def display(self):
        if(os.path.exists("data.txt")):  #file exists or not
            with open("data.txt", 'r') as fp:  #File open & close
                for e in fp:  #line by line read data
                    print(e)
        else:
            print("File does not exist")

    def search(self, AC_No):
        s = str(AC_No)
        if(len(s)!=3):
            print("Incorrect input ")
            return
        with open("data.txt", "r") as fp:
            # e: ek employee ka data 101,Anu, 10000
            # 102
            for e in fp:
                try:
                    e.index(str(AC_No),0,3)
                    print(e)
                    break
                except ValueError:
                    pass
            else:
                print("Record not found")
    def delete(self,AC_No):
       #read file & check if ac_no present
       found=False
       with open("data.txt",'r') as fp:
          details=[]
          for e in fp:
            #if ac_no match do nothing
            try:
                e.index(str(AC_No),0,3)
            
                
            except ValueError:
                details.append(e)
            else:
                found=True
                #record found
       #write data back to file
       if(found==True):
         with open("data.txt",'w') as fp:
           for x in details:
              fp.write(x) #if varible not found then this block not execute ,else part execute
       else:
          print("record not found")

    def update(self,AC_No):
        found=False
        with open("data.txt",'r') as fp:
            list1=[]
            for e in fp:
               try:
                  e.index(str(AC_No),0,3)
               except:
                  #record not found
                  list1.append(e)
               else:
                  ch=input("Do you want to update name: (y/n)")
                  if(ch=='y'):
                     name=input("Enter new name:")
                     splitted_data=e.split(',')
                     splitted_data[1]=name
                     e=','.join(splitted_data)
                     list1.append(e)
                  ch=input("Do you want to update balance: (y/n)")
                  if(ch=='y'):
                     balance=input("Enter new balance amount:")
                     splitted_data=e.split(',')
                     splitted_data[2]=str(balance)
                     e=','.join(splitted_data)
                     list1.append(e)
                  found=True
            if(found==True):
               with open("data.txt",'w') as fp:
                  for x in list1:
                     fp.write(x)
            else:
                print("data not found")  


    #def search(self, AC_No):
        
            
        #with open("data.txt", "r") as fp:
            # e: ek employee ka data 101,Anu, 10000
            # 102
            #for e in fp:
                #try:
                    #s=e.split(",")
                    #if (s[0]==str(AC_No)):
                    # print(e)
                     #break
                #except ValueError:
                    #pass
            #else:
                #print("Record not found") 
    
                   
        
