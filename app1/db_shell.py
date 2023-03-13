# exec(open(r'F:\code_files_python\B8_Django\first_project\app1\db_shell.py').read())

from app1.models import *
from django.contrib.auth.models import User

# to get all data
# obj = Person.objects.all()
# print(list(obj))

# for person in obj:
    # print(person)
    # print(person.__dict__)

# to get first record
# first_rec = Person.objects.first()
# print(first_rec)

# to get record by id

# try:
#     obj = Person.objects.get(id=4)
#     print(obj)

# except Person.DoesNotExist:
#     print("Record does not exit")


# to get multiple record by passing a filename

# obj = Person.objects.filter(age=25)
# print(obj)
# print(obj.query)

# obj = Person.objects.filter(age=26, address="Nashik")    # , means and
# print(obj)
# print(obj.query)

# modify existing data

# p1 = Person.objects.get(id=5)
# print(p1.__dict__)
# p1.mobile_num = 9877777777
# print(p1.__dict__)
# p1.save()             # it is must to save in dbsqlite
# p1.delete()           


# Bulk create

# save- First Way

# p1 = Person(name= "AbC", age= 25, mobile_num = 5469871255, address= "Mumbai")
# p1.save()

# save- second Way

# Person.objects.create(name= "xyz", age= 30, mobile_num = 5469871245, address= "Nagpur")

# print(dir(Person.objects))

"""['__class__', '__class_getitem__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', 
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', 
 '__str__', '__subclasshook__', '__weakref__', '_constructor_args', '_db', '_get_queryset_methods', '_hints', 
 '_insert', '_queryset_class', '_set_creation_counter', '_update', 'aggregate', 'alias', 'all', 'annotate', 
 'auto_created', 'bulk_create', 'bulk_update', 'check', 'complex_filter', 'contribute_to_class', 'count', 
 'create', 'creation_counter', 'dates', 'datetimes', 'db', 'db_manager', 'deconstruct', 'defer', 'difference',
  'distinct', 'earliest', 'exclude', 'exists', 'explain', 'extra', 'filter', 'first', 'from_queryset', 'get', 
  'get_or_create', 'get_queryset', 'in_bulk', 'intersection', 'iterator', 'last', 'latest', 'model', 'name', 
  'none', 'only', 'order_by', 'prefetch_related', 'raw', 'reverse', 'select_for_update', 'select_related', 
  'union', 'update', 'update_or_create', 'use_in_migrations', 'using', 'values', 'values_list']"""


# Bulk create

# p1 = Person(name= "p", age= 21, mobile_num = 5469871031, address= "Nashik")
# p2 = Person(name= "q", age= 22, mobile_num = 5469871456, address= "Pune")
# p3 = Person(name= "r", age= 23, mobile_num = 5469871123, address= "Ahmadnagr")
# p4 = Person(name= "s", age= 24, mobile_num = 5469871789, address= "Nagpur")

# Person.objects.bulk_create([p1,p2,p3,p4])

# count

# print(Person.objects.count())      # record ke count dega

# to delete all records
# Person.objects.all().delete()

# to delete multiple record
# Person.objects.filter(age=24).delete()


# print(Person.objects.filter(name__startswith= "A"))   

# print(Person.objects.filter(name__endswith= "h"))

# print(Person.objects.exclude(name__startswith= "A"))

# print(Person.objects.filter(id= 1).exists()) #True and False o/p deta hai, aur filter ke sath hi hum exists()\
                                                #  lagate hai

# print(Person.objects.all().order_by("-id"))         # id ke hisab se record milenge, id ko - kiya to descending \
                                                   #order me o/p milega


# Person.objects.get(id=1).show_details()


# for per_obj in Person.objects.all():
#     per_obj.show_details()

# print(Person.get_data_above_age())

"---------------------------------------------------------------------------------------------------"

# exec(open(r'F:\code_files_python\B8_Django\first_project\app1\db_shell.py').read())

# from app1.models import Person

# obj = Person.objects.all()
# print(list(obj))

# obj = Person.objects.last()
# print(obj)

# obj = Person.objects.get(name= "Akash", id= 4)
# print(obj)

# obj = Person.objects.filter(id= 4)
# print(obj)


# print(Person.objects.filter(name__contains= "k")) # jis jis me k contain hoga wo sab o/p me milega

"-------------------------------------------------------------------------------------------------"

# data = Person.objects.all().values()          # we will get data in dict i.e list of dict, key: values 
# # print(data)
# for i in data:
#   print(i)


# data = Person.objects.all().values("id", "name","mobile_num")
# print(data)                    # values ke paranthesis me hum jo pass krenge wo o/p milenga


# data = Person.objects.all().values()

# list_name = []
# for i in data:
#   list_name.append(i["name"])


# print(list_name)



# data = Person.objects.all().values()

# age_list = list(map(lambda x: x["age"], list(data)))

# print(age_list)
# print(sum(age_list)//len(age_list))     # average age of all persons

# Person.get_avg_age()   # models.py humne class method define kr di hai

"----------------------------------------------------------------------------------"

# data = Person.objects.all().values_list()   # list of tuples, menas tuples me data milega, values only
# print(data)

"----------------------------------------------------------------------------------------------"

# DATABASE change to mysql

# exec(open(r'F:\code_files_python\B8_Django\first_project\app1\db_shell.py').read())

# User.objects.create_user(username="Hemant", password="Python@123")  # always use create_user

# print(Person.objects.all())

# p1 = Person.objects.get(id = 4)
# p1.is_active = False
# p1.save()

# data = Person.objects.filter(id__in = [3, 5])
# print(data)

# for i in data:
#   i.is_active = False
#   i.save()

# data = Person.objects.filter(id__in = [3,5]).update(is_active=False)
# print(data)

# print(Person.objects.filter(is_active= True))
# print(Person.objects.filter(is_active= False))


# print(Person.get_active_data())

# print(Person.get_inactive_data())

# print(Person.isactivep.all())
# print(Person.isinactivep.all())
# print(Person.isactivep.all())
# print(Person.objects.all())

"------------------------------------------------------------------------------------------------"

# exec(open(r'F:\code_files_python\B8_Django\first_project\app1\db_shell.py').read())

# clgs = College.objects.all()
# prnc = Principal.objects.all()
# depts = Department.objects.all()
# stds = Student.objects.all()
# subjs = Subject.objects.all()

# print(clgs[0])

# for dept in depts:
#   print(dept.__dict__)


# for stud in stds:
#   print(stud.__dict__)


# for subj in subjs:
#   print(subj.__dict__)

# clg = clgs[0]            # K.K. Wagh College Nashik
# print(clg)
# print(clg.principal)
# print(clg.principal.__dict__)


# nandurkar_obj = Principal.objects.first()   
# print(nandurkar_obj)
# print(clg.department_set.all())    # take class name in lowercase      # one to many


# dept = Department.objects.first()

# print(dept.college)   

# print(dept.student_set.all())


# dept = Department.objects.get(id=1)
# print(dept.student_set.all())

# get all student deptwise

# all_depts = Department.objects.all()
# d = {}
# for dept in all_depts:
  # print(f"Department Name:- {dept}, students:- {list(dept.student_set.all())}")
  # d[dept.name] = list(dept.student_set.all())

# print(d)



# s1 = Student.objects.get(id = 10)
# print(s1.dept)

# get department from student

# studs = Student.objects.all()
# print(studs)
# stud_dept_dict = {}
# it_stud_list = []
# mech_stud_list = []
# civil_stud_list = []
# EE_stud_list = []
# for stud in studs:
#   stud_dept_dict[stud.name] = stud.dept.name
#   if stud.dept.name == "IT":
#       it_stud_list.append(stud.name)

#   elif stud.dept.name == "Mechanical": 
#       mech_stud_list.append(stud.name)

  # elif stud.dept.name == "Civil":
  #     civil_stud_list.append(stud.name)

#   elif stud.dept.name == "EE":
#       EE_stud_list.append(stud.name)


# print(stud_dept_dict,"\n")
# print(it_stud_list,"\n")
# print(mech_stud_list,"\n")
# print(civil_stud_list,"\n")
# print(EE_stud_list)



# exec(open(r'F:\code_files_python\B8_Django\first_project\app1\db_shell.py').read())

# clg = College.objects.get(id=1)
# print(clg.princi)             # related_name = "princi" given so we can fetch by princi    

    
# depts = Department.objects.all()

# for dept in depts:
#     print(dept.subjs.all())


# print([list(dept.subjs.all()) for dept in Department.objects.all()])


# clg = College.objects.get(id=1)
# print(clg.depts.all()[0].studs.all())
# student_list = []
# for dept in clg.depts.all():
#     student_list.extend(dept.studs.all())


# print(student_list)
   

# s1 = Student.objects.get(id=1)

# print(s1.dept.college.name)

"-------------------------------------------------------------------------------------------"

# Data Adddition

# College.objects.create(name= "Bhujbal Knowledge City", adr= "Nashik")  # clg add ho jayega
# c1 =College.objects.get(id=3)
# p1 = Principal(name= "ABC", exp_total = 10, qual = "Phd", college = c1)  # object pass krke data insert krna
# p1.save()

# p1 = Principal(name= "ABC", exp_total = 10, qual = "Phd", college_id = 3)   # pass Clg id
# p1.save()

# Principal.objects.create(name= "Abc", exp_total = 10,qual = "PHD", college_id=3)

# Department.objects.create(name= "Production",dept_strength = 60, college_id = 3)

# Student.objects.create(name = "A", marks = 89)
# Student.objects.create(name = "B", marks = 92)
# Student.objects.create(name = "C", marks = 95)

# s1, s2, s3 = Student.objects.filter(id__gt = 12)
# print(s1,s2,s3, sep="\n")

# prod_dept = Department.objects.get(id= 5)
# print(dir(prod_dept.studs))
# prod_dept.studs.add(s1)
# prod_dept.studs.add(s2, s3)    # one to many-- add students in department



# select_related

# studs = Student.objects.all()[0:5]
# print(studs)

  

# studs = Student.objects.select_related("dept")
# print(studs)
# for stud in studs:
#     print(stud.dept)


# exec(open(r'F:\code_files_python\B8_Django\first_project\app1\db_shell.py').read())


# c180 = CarModel.objects.create(name= "C180")
# c200 = CarModel.objects.create(name= "c200")
# CarModel.objects.all()
# print(CarModel.objects.all())

# gas = FuelType.objects.create(name= "gas")
# diesel = FuelType.objects.create(name= "diesel")
# hybrid = FuelType.objects.create(name= "hybrid")
# print(FuelType.objects.all())

# c180 = CarModel.objects.get(name= "C180")
# c200 = CarModel.objects.get(name= "C200")

# gas = FuelType.objects.get(name= "gas")
# diesel = FuelType.objects.get(name= "diesel")
# hybrid = FuelType.objects.get(name= "hybrid")
# bio_diesel = FuelType.objects.get(name= "Bio-Diesel")

# c200.fueltype.add(gas,diesel,hybrid)
# print(c200.fueltype.all())

# c200.fueltype.create(name="Bio-Diesel")
# print(bio_diesel.carmodel_set.all())

# print(bio_diesel.carmodels.all())    # related name given as carmodels
# print(c180.fueltype.all())


# print(CarModel.objects.filter(fueltype__name__startswith= "B"))

# print(FuelType.objects.filter(carmodels__name__startswith= "c"))

"-------------------------------------------------------------------------------------"


# exec(open(r'F:\code_files_python\B8_Django\first_project\app1\db_shell.py').read())

# from django.db import connection
#Raw sql queries

# first way

# cursor = connection.cursor()
# cursor.execute("select * from student")  # raw sql
# data = cursor.fetchall()
# print(data)
# # data = cursor.fetchmany(5)    # first 5 data aayega, firse fetchmany 5 kiya to uske aageke 5 record aayenge
# print(data)

# data = cursor.fetchmany(5)    
# print(data)

# second way

# data = Student.objects.raw("select * from student")

# for stud in data:
#     print(stud)

"-----------------------------------------------------------------------------------------------"

# Multiple database
# Mysql, sqlite
# Mysql, postgresql


# SECOND_DATABASE = "second_db"
# data = Student.objects.using(SECOND_DATABASE).all()  # using another database
# print(data)

# c1= College.objects.using(SECOND_DATABASE).create(name = "COEP",adr = "Pune")
# d1= Department.objects.using(SECOND_DATABASE).create(name= "ENTC",dept_strength= 60, college= c1)
# s1 = Student.objects.using(SECOND_DATABASE).create(name= "PQR", marks = 95, dept = d1)
# s2 = Student.objects.using(SECOND_DATABASE).create(name= "EFG", marks = 94, dept = d1)
# subj1 = Subject.objects.using(SECOND_DATABASE).create(name= "Data Signal", is_practical = True, dept= d1)

# exec(open(r'F:\code_files_python\B8_Django\first_project\app1\db_shell.py').read())

# THIRD_DATABASE = "third_db"
# data = Student.objects.using(THIRD_DATABASE).all()  # using another database
# print(data)

# c1= College.objects.using(THIRD_DATABASE).create(name = "COEP",adr = "Pune")
# d1= Department.objects.using(THIRD_DATABASE).create(name= "ENTC",dept_strength= 60, college= c1)
# s1 = Student.objects.using(THIRD_DATABASE).create(name= "PQR", marks = 95, dept = d1)
# s2 = Student.objects.using(THIRD_DATABASE).create(name= "EFG", marks = 94, dept = d1)
# subj1 = Subject.objects.using(THIRD_DATABASE).create(name= "Data Signal", is_practical = True, dept= d1)


"------------------------------------------------------------------------------------------------------------"


