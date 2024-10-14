from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import sqlite3
import requests
import xlrd
from xlrd import open_workbook
import xlwt
from xlwt import Workbook 

co='0'
cou='0'
filename=''
class Application(Frame):

        def __init__(self,master):
                super().__init__(master)
                self.grid()
                self.create_widgets()
                self.bytes = 0
                self.maxbytes = 0
                
                

        def create_widgets(self):
                self.lbl=Label(self,height=5,width=110,text="Offline Module",bd=2,bg="black",fg="white")
                self.lbl.grid(padx=(0,0),pady=(0,0),row=0, column=0)

                #self.bttn=Button(self, height=5,width=100,text="Django Offline Module")
                #self.bttn.grid(padx=(0,0), pady=(0,0), row=0, column=0)

                self.bttn1 = Button(self,command=self.choose, height=3,width=22,text="Choose File") #write this : ,command=self.choose,
                self.bttn1.grid(padx=(0,10), pady=(50,10), row=1, column=0)
              
                self.fnameLabel = Label(self, text="File Name")
                self.fnameLabel.grid(padx=(0,10), pady=(10,10),row=2,column=0)
                
                self.bttn2 = Button(self,command=self.alloc, height=3,width=22)  #write this: command=self.alloc
                self.bttn2.grid(padx=(0,10), pady=(10,10),row=3,column=0)
                self.bttn2.configure(text = "Allocate")
                
                self.bttn3 = Button(self,command=self.exc, height=3,width=22) #write this:,command=self.exc
                self.bttn3.grid(padx=(0,10), pady=(10,10),row=4,column=0)
                self.bttn3['text']= 'Get Excel Sheets'
                
                self.x = Label(self, text="Waiting")
                self.x.grid(padx=(0,10), pady=(20,10),row=5,column=0)     

                self.progress=ttk.Progressbar(self,orient="horizontal",length=200,mode="determinate")
                self.progress.grid(padx=(0,10), pady=(10,10),row=6,column=0)

                self.bttn4 = Button(self,command=self.upload, height=3,width=22, text="Upload") #write this : ,command=self.upload
                self.bttn4.grid(padx=(0,10), pady=(40,10),row=7,column=0)



        def choose(self):
               Tk().withdraw()
               global filename
               filename = askopenfilename()
               self.fnameLabel.configure(text=filename)
               global co
               if(filename!=''):
                       co='1'



        def alloc(self):
                global co
                global cou
                global filename
                limit=5
                if(co!='1'):
                        self.x.configure(text='Please Select File')
                else:               
                        self.x.configure(text='Processing')
                        self.sortt()
                        con = sqlite3.connect("Alloc.db")
                        cur = con.cursor()
                        cur.execute('''CREATE TABLE IF NOT EXISTS studs(Name TEXT, sub text) ''')
                        cur.execute("delete from studs")
                        book = open_workbook(filename)
                        sheet = book.sheets()[0]
                        data = [sheet.row_values(i) for i in range(sheet.nrows)]

                        for idx_r, row in enumerate(data[1:]):
                                selec=row[2]
                                if (selec!=''):
                                        cur.execute("select count(*) from studs where sub=(?)",(selec,))
                                        num=cur.fetchone()
                                        if(num[0]<limit):
                                                cur.execute('''INSERT INTO studs(Name, sub) values(?,?)''',(row[0],selec))
                                        else:
                                                print('first priority missed for',row[0])
                                                selec=row[3]
                                                if (selec!=''):
                                                        cur.execute("select count(*) from studs where sub=(?)",(selec,))
                                                        num=cur.fetchone()
                                                        if(num[0]<limit):
                                                                cur.execute('''INSERT INTO studs(Name, sub) values(?,?)''',(row[0],selec))
                                                        else:
                                                                print('second priority missed for',row[0])
                                                                selec=row[4]
                                                                if (selec!=''):
                                                                        cur.execute("select count(*) from studs where sub=(?)",(selec,))
                                                                        num=cur.fetchone()
                                                                        if(num[0]<limit):
                                                                                cur.execute('''INSERT INTO studs(Name, sub) values(?,?)''',(row[0],selec))
                                                                        else:
                                                                                print('third priority missed for',row[0])
                                                                                selec=row[5]
                                                                                if (selec!=''):
                                                                                        cur.execute("select count(*) from studs where sub=(?)",(selec,))
                                                                                        num=cur.fetchone()
                                                                                        if(num[0]<limit):
                                                                                                cur.execute('''INSERT INTO studs(Name, sub) values(?,?)''',(row[0],selec))
                                                                                        else:
                                                                                                print('fourth priority missed for',row[0])
                                                                                                selec=row[6]
                                                                                                if (selec!=''):
                                                                                                        cur.execute("select count(*) from studs where sub=(?)",(selec,))
                                                                                                        num=cur.fetchone()
                                                                                                        if(num[0]<limit):
                                                                                                                cur.execute('''INSERT INTO studs(Name, sub) values(?,?)''',(row[0],selec))
                                                                                                        else:
                                                                                                                print('fifth priority missed for',row[0])
                                                                                                                cur.execute('''INSERT INTO studs(Name, sub) values(?,?)''',(row[0],'Not Alloc'))
                                                                                                else:
                                                                                                        cur.execute('''INSERT INTO studs(Name, sub) values(?,?)''',(row[0],'Not Alloc'))
                                                                                else:
                                                                                        cur.execute('''INSERT INTO studs(Name, sub) values(?,?)''',(row[0],'Not Alloc'))
                                                                else:
                                                                        cur.execute('''INSERT INTO studs(Name, sub) values(?,?)''',(row[0],'Not Alloc'))
                                                else:
                                                        cur.execute('''INSERT INTO studs(Name, sub) values(?,?)''',(row[0],'Not Alloc'))
                                else:
                                        cur.execute('''INSERT INTO studs(Name, sub) values(?,?)''',(row[0],'Not Alloc'))
                


                        con.commit()
                        self.x.configure(text='Allocated')
                        cou='1'

        def exc(self):
                global co
                global cou
                if(co!='1' or cou!='1'):
                        self.x.configure(text='Please Allocate First')
                else:
                        self.x.configure(text='Processing')
                        con = sqlite3.connect("Alloc.db")
                        cur = con.cursor()
                        cur.execute("select distinct(sub) from studs")
                        lis=cur.fetchall()
                        con.close()
                        wb = Workbook()
                        i=0
                        for s in lis:
                                i=i+1
                                j=1
                                name='Sheet'+str(i)
                                sheet = wb.add_sheet(name)
                                sheet.write(0,0,'Name')
                                sheet.write(0,1,'Subject')
                                con = sqlite3.connect("Alloc.db")
                                cur = con.cursor()
                                cur.execute("select * from studs where sub=(?)",(s[0],))
                                results = cur.fetchall()
                                con.close()
                                for row in results:
                                        sheet.write(j,0,row[0])
                                        sheet.write(j,1,row[1])
                                        j=j+1
                                

                        wb.save('Final.xls')
                        self.x.configure(text='Excel Sheets Generated')
                        con.close()


                        
        def upload(self):
                global co
                global cou
                if(co!='1' or cou!='1'):
                        self.x.configure(text='Please Select File')
                else:
                        try:
                                self.start()
                                self.progress["value"]=0
                                self.progress.update()
                                self.x.configure(text='Processing')
                                con = sqlite3.connect("Alloc.db")
                                cur = con.cursor()
                                cur.execute("select * from studs")
                                results = cur.fetchall()
                                for row in results:
                                        payload={'name': row[0], 'sub': row[1]}
                                        r = requests.post("http://127.0.0.1:8000/upload/", data={'name': row[0], 'sub': row[1]})
                                        self.x.configure(text='Processing')
                                        print(r.url)
                                        self.bytes += 10
                                        self.progress["value"] = self.bytes
                                        self.progress.update()
                                self.progress["value"]=100
                                self.progress.update()
                                self.x.configure(text='Uploaded to Database')
                                con.close()
                        except:
                                self.x.configure(text='Not connected to the Internet')

        def start(self):
                self.progress["value"] = 0
                self.maxbytes = 100
                self.progress["maximum"] = 100
                
        


        def sortt(self):
                global filename
                target_column = 1
                book = open_workbook(filename)
                sheet = book.sheets()[0]
                data = [sheet.row_values(i) for i in range(sheet.nrows)]
                labels = data[0]
                data = data[1:]
                data.sort(key=lambda x: x[target_column])
                bk = xlwt.Workbook()
                sheet = bk.add_sheet(sheet.name)

                for idx, label in enumerate(labels):
                     sheet.write(0, idx, label)

                for idx_r, row in enumerate(data):
                    for idx_c, value in enumerate(row):
                        sheet.write(idx_r+1, idx_c, value)

                bk.save('result.xls')
                filename='result.xls'



                
root = Tk()
root.title("Offline Module")
root.geometry("870x650")
app = Application(root)
root.mainloop()
