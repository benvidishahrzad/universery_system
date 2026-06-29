import colorama
import jdatetime
from oop import person, student, teacher,course,requests,thesis

print('hi')
# print('-'*50)
# print(colorama.Fore.YELLOW , datetime.datetime.now())
#print('-'*50)
print(colorama.Fore.YELLOW , jdatetime.datetime.today())
#----------------logORsing-----------------
print('-'*50)
print("\t student->s")
print("\t professor->p")
print(colorama.Fore.WHITE)
try:
    who=input("who are you: ")
except Exception as x:
    print(x)
print('-'*50)
user=input("\t user:")
password=input("\t password:")
#-------------------------student------------------------------
if who.lower()=='s':
    stu1=student()
    re1=requests()
    stu1.refresh(user)
    if stu1.login(user, password)==False:
        exit()
    stu1.menu()
    work=input('your choice:')
    if work=='1':
        print("value must be digit and has 6 to 12 number.")
        value=input("enter new value: ")
        check_password=input("please enter your password:")
        stu1.edit_student((value,user,check_password))
    elif work=='2':
        co=course()
        co.show()
        while(True):
            course_id=input("\t course id:")
            if co.check_capacity(course_id) is False:
                print("no capacity.")
                if input('do you want to choose another course? y/n')=='n': exit()
                else: continue
            else:
                break
        if stu1.add_course((user,course_id))==True:
            re1.user=user
            re1.dars=course_id
            re1.name=str(user)
            re1.teacher=str(course_id)
            try:
                re1.add_to_dict()
                print("added.")
            except:
                print ("try again later...")
                exit()    
    elif work=='3':
        re1.show_requests_students(user)
    elif work=='4':
        th1=thesis()
        if re1.check_three_mounth(user) is True:
            th1.stu_code=user
            th1.writer = user
            course_id=input("course id: ")
            th1.course_id = course_id
            th1.title=input("title: ")
            th1.year=int(input("year: "))
            th1.trimester=int(input("trimester: "))
            th1.teacher=input("teacher: ")
            th1.abstract=input("abstract address")
            k_num= int(input("how many keywords do you have?"))
            for i in range(k_num):
                k=input("keywords: ")
                th1.keywords.append(k)
            th1.pdf_path= input("pdf address")
            th1.first_page_image= input("first page image: ")
            th1.last_page_image=input("last page address: ")
            try:
                th1.add_to_dict()
                print("added.")
                re1.user=user
                re1.dars="define"
                re1.name=str(user)
                re1.teacher=str(course_id)
                re1.add_to_dict()
            except:
                print ("try again later...")
                exit()
            
    elif work=='5':
        while(True):
            print('\t 1->title')
            print('\t 2->teacher')
            print('\t 3->keywords')
            print('\t 4->judges')
            print('\t 5->year')
            print('\t 6->writer')
            find=input("your choice:")
            th=thesis()
            th.find(find)
            end=input("do you want to search with another category? (y/n)")
            if end=='y':continue
            else: break
        
        
#-------------teacher---------------------------------------
elif who.lower()=='t':
    tea1=teacher()
    tea1.login(user,password)
    re1=requests()
    teacher_name=tea1.find_name(user)
    re1.show_requests_teacher(teacher_name)
    tea1.menu()
    work=input('your choice:')
    if work=='1':
        user_student=input("enter the student user: ")
        print(colorama.Fore.LIGHTMAGENTA_EX)
        print('\t 1->accept')
        print('\t 2->reject')
        print(colorama.Fore.RESET)
        which=input("answer: ")
        if which=="1":
            status="accept"
        if which =="2":
            status="reject"
        else:
            print("not available!")
            exit()
        re1.change_status((status,teacher_name,user_student,))
    elif work=='2':
        th1=thesis()
        user_student=input("enter the student user: ")
        status="accept"
        mark=input("please enter score: ")
        re1.change_status((status,teacher_name,user_student,))
        th1.edit()
    elif work=='3':
        while(True):
            print('\t 1->title')
            print('\t 2->teacher')
            print('\t 3->keywords')
            print('\t 4->judges')
            print('\t 5->year')
            print('\t 6->writer')
            find=input("your choice:")
            th=thesis()
            th.find(find)
            end=input("do you want to search with another category? (y/n)")
            if end=='y':continue
            else: break
    elif work=='4':
        print("value must be digit and has 6 to 12 number.")
        value=input("enter new value: ")
        check_id=input("please enter your user:")
        check_password=input("please enter your password:")
        tea1.edit_teacher((value,check_id,check_password))
        

            