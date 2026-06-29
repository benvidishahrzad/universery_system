import random
import jdatetime
import colorama
import json
import os
class person():
    def __init__(self):
        self._name="......."
        self._fa="........"
        self.tavalod=None
        self.id='0000000000'
        self._phonenumber="09111111111"
        self._password=None
        self._user=None
        
        #----------------name---------------------
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self,value:str):
        if len(value)>=2 and value.isalpha():
            self._name= value
    #----------------family------------------
    @property
    def fa(self):
        return self._fa 
    @fa.setter
    def fa(self,value:str):
        if len(value)>=2 and value.isalpha():
            self._fa= value
    #-----------------tavalod---------------
    @property
    def tavalod(self):
        return self._tavalod 
    @tavalod.setter
    def tavalod(self, value):
        if value is None:
            pass
        else:
            try:
                year, month, day = map(int, value.split('/'))
                self._tavalod = jdatetime.datetime(year, month, day)
            except ValueError as e:
                print(f"Error: {e}. Please use yyyy/mm/dd.")
            except Exception as e:
                print(f"Unexpected error: {e}")
    #----------------id-------------------
    @property
    def id(self):
        return self._id 
    @id.setter
    def id(self,value:str):
        if len(value)==10 and value.isdigit():
            self._id= value
        if len(set(value)) == 1:
            return False
        check = int(value[9])
        s = sum(int(value[i]) * (10 - i) for i in range(9))
        r = s % 11
        if (r < 2 and check == r) or (r >= 2 and check == (11 - r)):
            self._id=value
        else: 
            print("not correct")
    #----------------phone-----------------
    @property
    def phonenumber(self):
        return self._phonenumber 
    @phonenumber.setter
    def phonenumber(self,value):
        if len(value)==11 and value.isdigit() and value[0:2]=='09':
            self._phonenumber= value
    #-----------------user----------------
    @property
    def user(self):
        return self._user 
    @user.setter
    def user(self):
        self._user= self.id
    
    #-----------------password----------------
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,value:str):
        if len(value)>=6 and len(value)<=12 and value.isdigit():
            self._password= value
                    
    def login(self,us,pas):
        pass
        
    def menu(self):
        pass
        
    
         

class student(person):
    def __init__(self):
        super().__init__()
        self._dars=[]
        
    #-------------login-----------------------------------------------    
    def login(self,us,pas):
        try:
            with open('d:\\python\\fater\\sdata.json', 'r') as file:
                users = json.load(file) 
        except (FileNotFoundError, json.JSONDecodeError):
            users = []
        for user in users:
            #print(user)
            if user["user"] == us and pas != user["password"]:
                print("your password is NOT correct.")
                tast_pass=input("do you want tast it again? (y/n)")
                if tast_pass.lower()=='y':
                    i=1
                    while (i<=3) :
                        pas= input('password: ')
                        i=i+1
                        if user["user"] == us and pas == user["password"]:
                            print('welcome',us)
                            return True ##############################
                        print("your password is NOT correct.Try again")######################3
                print("Unfortunately, you cannot try again.")
                forget=input('do you forget it? (y/n)')
                if forget.lower()=='y':
                    print('Don worry.We will send your password to your email.')
                    return False
                else:
                    print('if you want we can help you to find your password...')
                    return False
            if user["user"] == us and pas == user["password"]:
                print('welcome', user["name"])
                return True
        
        print('username not found.')
        ans=input('continue? (y/n)')
        if ans.lower()=='n':
            print('end...')
            return False
        else:
            us=input("\t user:")
            pas=input("\t password:")  
    #-----------------------------menu----------------------------            
    def menu(self):
        print(colorama.Fore.LIGHTMAGENTA_EX)
        print('\t 1->change password')
        print('\t 2->select class')
        print('\t 3->request status')
        print('\t 4->make request ')
        print('\t 5->theses archive')
        print(colorama.Fore.RESET)
    
    #------------------regester---------------------
    def register(self , y):
        try:
            with open('d:\\python\\pro1\\sdata.json', 'r') as file:
                users = json.load(file) 
        except (FileNotFoundError, json.JSONDecodeError):
            users = []
        for user in users:
            if user['id'] == y:
                print("Username already exists.")
                return False
        return True
    
    #--------------edit-pass---------------------------    
    def edit_student(self,value):
        try:
            with open('d:\\python\\fater\\sdata.json', 'r') as file:
                data_list = json.load(file)
        except IOError as e:
            print("error", e)
        found = False
        for item in data_list:
            if item.get("user") == value[1]:
                if item["password"] ==value[2]:
                    found=True
                    item["password"]=value[0]
                    break
        if found==False:
            print("not found.")
            
        try:
            with open(('d:\\python\\fater\\sdata.json'), 'w') as file:
                json.dump(data_list, file, indent=9)
                print("edited.")
        except IOError as e:
            print("error", e) 
    #--------------------add-course-------------------
    def add_course(self, value):
        try:
            with open('d:\\python\\fater\\sdata.json', 'r') as file:
                data_list = json.load(file)
        except IOError as e:
            print("error", e)
        for i in data_list:
            if value[0]==i["user"]:
                for j in i["courses"]:
                    if value[1]==j:
                        print('It has already been selected once. ')
                        return False 
                print(f"Request for course {value[1]} sent.")
                return True 
    #------------------refresh-----------------------------------------
    def refresh(self,value):
        try:
            with open('d:\\python\\fater\\requestsdata.json', 'r') as file:
                data_list = json.load(file)
        except IOError as e:
            print("error", e)
        for item in data_list:
            if item.get("user") == value:
                if item["status"] =="accept":
                    found=True
                    break
        if found==False:
            print("not found.")    
            
        try:
            with open('d:\\python\\fater\\sdata.json', 'r') as file:
                data_list = json.load(file)
        except IOError as e:
            print("error", e)
        for i in data_list:
            if value[0]==i["user"]:
                i["courses"].append(value[1])
                self._dars.append(value[1])
                try:
                    with open(('d:\\python\\fater\\sdata.json'), 'w') as file:
                        json.dump(data_list, file, indent=11)
                        print(f"Course {value[1]} added for user {value[0]}.")
                except IOError as e:
                    print("error", e) 
        
class teacher(person):
    def __init__(self):
        super().__init__()
        
    def menu(self):
        print(colorama.Fore.LIGHTMAGENTA_EX)
        print('\t 1->edit request status')
        print('\t 2->thesis result')
        print('\t 3->theses archive')
        print('\t 4->change password')
        print(colorama.Fore.RESET)
        
    def login(self,us,pas):
        try:
            with open('d:\\python\\fater\\sdata.json', 'r') as file:
                users = json.load(file) 
        except (FileNotFoundError, json.JSONDecodeError):
            users = []
        for user in users:
            #print(user)
            if user["user"] == us and pas != user["password"]:
                print("your password is NOT correct.")
                tast_pass=input("do you want tast it again? (y/n)")
                if tast_pass.lower()=='y':
                    i=1
                    while (i<=3) :
                        pas= input('password: ')
                        i=i+1
                        if user["user"] == us and pas == user["password"]:
                            print('welcome',us)
                            return True ##############################
                        print("your password is NOT correct.Try again")######################3
                print("Unfortunately, you cannot try again.")
                forget=input('do you forget it? (y/n)')
                if forget.lower()=='y':
                    print('Don worry.We will send your password to your email.')
                    return False
                else:
                    print('if you want we can help you to find your password...')
                    return False
            if user["user"] == us and pas == user["password"]:
                print('welcome', user["name"])
                return True
        
        print('username not found.')
        ans=input('continue? (y/n)')
        if ans.lower()=='n':
            print('end...')
            return False
        else:
            us=input("\t user:")
            pas=input("\t password:") 
#-------------------edit_pass-----------------------------                
    def edit_teacher(self,value):
        try:
            with open('d:\\python\\fater\\tdata.json', 'r') as file:
                data_list = json.load(file)
        except IOError as e:
            print("error", e)
        found = False
        for item in data_list:
            if item.get("id") == value[1]:
                if item["password"] ==value[2]:
                    found=True
                    item["password"]=value[0]
                    break
        if found==False:
            print("not found.")
        try:
            with open(('d:\\python\\fater\\tdata.json'), 'w') as file:
                json.dump(data_list, file, indent=11)
                print("edited.")
        except IOError as e:
            print("error", e)
            
#-------------------------find-name-------------------
    def find_name(self,value):
        try:
            with open('d:\\python\\fater\\tdata.json', 'r') as file:
                data_list = json.load(file)
        except IOError as e:
            print("error", e)
        for item in data_list:
            if item.get("user") == value:
                return item["name"]
        
        
                     
        
        

        
class course():
    def __init__(self):
        self._id=''
        self.title=''
        self._teacher=''
        self._year=jdatetime.datetime.now().year
        self._trimester=0
        self._capacity=0
        self._session=0
        self.source=''
        self._vahed=0
        
    #------------id------------------------    
    @property
    def id(self):
        return self._id 
    @id.setter
    def id(self,value:str):
        if len(value)==5 and value.isdigit():
            self._id= value
            
    #----------------teacher------------------
    @property
    def teacher(self):
        return self._teacher 
    @teacher.setter
    def teacher(self,value:str):
        try:
            with open('d:\\python\\fater\\tdata.json', 'r') as file:
                teachers = json.load(file) 
        except (FileNotFoundError, json.JSONDecodeError):
            teachers = []
        for user in teachers:
            if user["name"] == value:
                self._teacher=value
                
    #------------------trimester-------------------------
    @property
    def trimester(self):
        return self._trimester 
    @trimester.setter
    def trimester(self,value):
        if value==1 or value==2:
            self._trimester = value
        else:
            print("trimester out of range.")
    #------------------capacity-------------------------
    @property
    def capacity(self):
        return self._capacity 
    @capacity.setter
    def capacity(self,value):
        if int(value)>1:
            self._capacity = value
        else:
            print("capacity out of range.")
    #---------------session------------------------------
    @property
    def session(self):
        return self._session
    @session.setter
    def session(self,value):
        if int(value)>0:
            self._session = value
        else:
            print("session out of range.")
    #-------------------------vahed------------------------
    @property
    def vahed(self):
        return self._vahed
    @vahed.setter
    def vahed(self, value):
        if  1 <= int(value) <= 5:
            self._vahed = value
        else:
            print("vahed out of range.")
            
    #---------------show---------------------------------
    def show(self):
        with open(('d:\\python\\fater\\courses.json'), 'r') as file:
            data = json.load(file)
        print(colorama.Fore.BLUE)
        for item in data:
            print(item)
        print(colorama.Fore.RESET)
        
    #--------------check_capacity----------------------
    def check_capacity(self,value):
        with open(('d:\\python\\fater\\courses.json'), 'r') as file:
            data_list= json.load(file)
        #print( data_list)
        for i in data_list:
            if value==i["id"]:
                #print(i)
                if i["capacity"]>0:
                    return True
                else:
                    return False

    
class requests():
    def __init__(self):
        self._status="under review"
        self._tarikh=jdatetime.datetime.today()
        self._name=''
        self._teacher=''
        self.user='00000'
        self.dars=''
        
    #-----------teacher--------------------
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self,value:str):
        try:
            with open('d:\\python\\fater\\sdata.json', 'r') as file:
                students = json.load(file) 
        except (FileNotFoundError, json.JSONDecodeError):
            students = []
        for user in students:
            if user["user"] == value:
                self._name= user["family"]    
    #-----------teacher--------------------
    @property
    def teacher(self):
        return self._teacher 
    @teacher.setter
    def teacher(self,value):
        try:
            with open('d:\\python\\fater\\courses.json', 'r') as file:
                teachers = json.load(file) 
        except (FileNotFoundError, json.JSONDecodeError):
            teachers = []
        for user in teachers:
            if user["id"] == value:
                self._teacher= user["teacher"]
                return
            print("Teacher ID not found.")
    #-----------------show-teacher--------------------------------
    def show_requests_teacher(self,value):
        with open(('d:\\python\\fater\\requestsdata.json'), 'r') as file:
            data = json.load(file)
        print(colorama.Fore.GREEN)
        for item in data:
            if item.get("teacher") == value:
                print(item)
        print(colorama.Fore.RESET)
        
    #-----------------show-student--------------------------------
    def show_requests_students(self,value):
        with open(('d:\\python\\fater\\requestsdata.json'), 'r') as file:
            data = json.load(file)
        print(colorama.Fore.GREEN)
        for item in data:
            if item.get("user") == value:
                print(item)
        print(colorama.Fore.RESET)
    #------change------------------------------------------
    def change_status(self,value): #value =id-student
        try:
            with open('d:\\python\\fater\\requestsdata.json', 'r') as file:
                data_list = json.load(file)
        except IOError as e:
            print("error", e)
        found = False
        for item in data_list:
            if item.get("teacher") == value[1]:
                if item["id"] ==value[2]:
                    found=True
                    item["status"]=value[0]
                    break
        if found==False:
            print("not found.")
            
        try:
            with open(('d:\\python\\fater\\requestsdata.json'), 'w') as file:
                json.dump(data_list, file, indent=6)
                print("edited.")
        except IOError as e:
            print("error", e) 
    
    #--------add-dict----------------------
    def add_to_dict(self):
        newRequest={
            "user":self.user,
            "id dars":self.dars,
            "name student":self.name,
            "teacher":self.teacher,
            "date":str(self._tarikh),
            "status":self._status
        }
        try:
            with open('d:\\python\\fater\\requestsdata.json', 'r') as file:
                data_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data_list = []
        data_list.append(newRequest)
        
        with open(('d:\\python\\fater\\requestsdata.json'), 'w') as file:
            json.dump(data_list, file, indent=7)
    
    #-------------------check_three_mounth-----------------------------
    def check_three_mounth(self,value):
        with open(('d:\\python\\fater\\requestsdata.json'), 'r') as file:
            data = json.load(file)
        print(colorama.Fore.GREEN)
        found=False
        for item in data:
            if item.get("user") == value:
                request_date=item.get("date")
                request_date = request_date.split()[0]
                request_date = jdatetime.datetime.strptime(request_date, "%Y-%m-%d")
                now = jdatetime.datetime.now()
                three_months_later = request_date + jdatetime.timedelta(days=90)
                print(item)
                print("you can request to define.")
                print("\t 1-> yes")
                print("\t 2->no ")
                answer=input('answer: ')
                if answer=="1":
                    found=True
                    return True
                else:
                    pass
                return found
        print(colorama.Fore.RESET)
        
    

class thesis:
    def __init__(self):
        self.status="waiting"
        self._mark=0
        self._stu_code=''
        self._writer=''
        self._course_id =''
        self.title =''
        self.year=0
        self._trimester=0
        self._teacher=''
        self._judges=[]
        self.abstract =''
        self.keywords =[]
        self.pdf_path =''
        self.first_page_image =''
        self.last_page_image =''
    #-----------stu-code--------------------
    @property
    def stu_code(self):
        return self._stu_code 
    @stu_code.setter
    def stu_code(self,value):
        try:
            with open('d:\\python\\fater\\sdata.json', 'r') as file:
                students= json.load(file) 
        except (FileNotFoundError, json.JSONDecodeError):
            students = []
        for user in students:
            if user["user"] == value:
                self._stu_code= value 
     #-----------writer--------------------
    @property
    def writer(self):
        return self._writer 
    @writer.setter
    def writer(self,value):
        try:
            with open('d:\\python\\fater\\sdata.json', 'r') as file:
                students= json.load(file) 
        except (FileNotFoundError, json.JSONDecodeError):
            students = []
        for user in students:
            if user["user"] == value:
                self._writer= user["family"]
    #-----------teacher--------------------
    @property
    def course_id(self):
        return self._course_id 
    @course_id.setter
    def course_id(self,value):
        try:
            with open('d:\\python\\fater\\courses.json', 'r') as file:
                c = json.load(file) 
        except (FileNotFoundError, json.JSONDecodeError):
            c = []
        for user in c:
            if user["id"] == value:
                self._course_id=value  
    #-----------teacher--------------------
    @property
    def teacher(self):
        return self._teacher 
    @teacher.setter
    def teacher(self,value):
        try:
            with open('d:\\python\\fater\\tdata.json', 'r') as file:
                teachers = json.load(file) 
        except (FileNotFoundError, json.JSONDecodeError):
            teachers = []
        for user in teachers:
            if user["id"] == value:
                self._teacher= user["teacher"] 
    #-----------judges--------------------
    @property
    def judges(self):
        return self._judges 
    @judges.setter
    def judges(self,value):
        try:
            with open('d:\\python\\fater\\tdata.json', 'r') as file:
                teachers = json.load(file) 
        except (FileNotFoundError, json.JSONDecodeError):
            teachers = []
        for user in teachers:
            if user["id"] == value:
                self._judges.append(user["teacher"])
    #----------------trimester------------------
    @property
    def trimester(self):
        return self._trimester 
    @trimester.setter
    def trimester(self,value):
        if value==1 or value==2:
            self._trimester = value
        else:
            print("trimester out of range.")
            
            
     #-----------------mark----------------
    @property
    def mark(self):
        return self._mark
    @mark.setter
    def mark(self,value):
        if int(value)>=0 and int(value)<=20 and value.isdigit():
            self._mark= value
    #---------------show---------------------------------
    def show(self):
        with open(('d:\\python\\fater\\theisis.json'), 'r') as file:
            data = json.load(file)
        print(colorama.Fore.BLUE)
        for item in data:
            if item["status"]=="accept":
                print(item)
        print(colorama.Fore.RESET)
        
        #----------- save to JSON --------------------
    def add_to_dict(self):
        new_thesis = {
            "status":self.status,
            "student_code": self._stu_code,
            "writer": self._writer,
            "course_id": self._course_id,
            "title": self.title,
            "year": self.year,
            "trimester": self._trimester,
            "teacher": self._teacher,
            "judges": self._judges,
            "abstract": self.abstract,
            "keywords": self.keywords,
            "pdf_path": self.pdf_path,
            "first_page_image": self.first_page_image,
            "last_page_image": self.last_page_image
        }

        try:
            with open('d:\\python\\fater\\theisis.json', 'r') as file:
                data_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data_list = []
        data_list.append(new_thesis)
        
        with open(('d:\\python\\fater\\theisis.json'), 'w') as file:
            json.dump(data_list, file, indent=14)
    #-----------------find----------------------
    def find(self,value):
        try:
            with open('d:\\python\\fater\\theisis.json', 'r') as file:
                data_list = json.load(file)
        except IOError as e:
            print("error", e)
        for item in data_list:
                if value=='1':
                    f=input(colorama.Fore.MAGENTA ,"title: ")
                    if item.get("title") == f:
                        print(item)
                    break
                elif value=='2':
                    f=input(colorama.Fore.MAGENTA ,"teacher: ")
                    if item.get("teacher") == f:
                        print(item)
                    break
                elif value=='3':
                    f=input(colorama.Fore.MAGENTA ,"keywords: ")#//////////////////////////////////
                    if item.get("keywords") ==f:
                        print(item)
                    break
                elif value=='4':
                    f=input(colorama.Fore.MAGENTA ,"judges: ")#///////////////////////////////////////
                    if item.get("judges") == f:
                        print(item)
                    break
                elif value=='5':
                    f=input(colorama.Fore.MAGENTA ,"year: ")
                    if item.get("year") == f:
                        print(item)
                    break
                elif value=='6':
                    f=input(colorama.Fore.MAGENTA ,"writer: ")
                    if item.get("writer") == f:
                        print(item)
                    break 
                print(colorama.Fore.RESET)
    #------change------------------------------------------
    def change_status(self,value): #value =id-student
        try:
            with open('d:\\python\\fater\\theisis.json', 'r') as file:
                data_list = json.load(file)
        except IOError as e:
            print("error", e)
        found = False
        for item in data_list:
            if item.get("teacher") == value[1]:
                if item["id"] ==value[2]:
                    found=True
                    item["status"]=value[0]
                    break
        if found==False:
            print("not found.")
            
        try:
            with open(('d:\\python\\fater\\theisis.json'), 'w') as file:
                json.dump(data_list, file, indent=6)
                print("edited.")
        except IOError as e:
            print("error", e)
            
     
            