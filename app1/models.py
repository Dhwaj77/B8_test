from django.db import models

# Create your models here.

#ORM --- object relational mapper

class ActivePersons(models.Manager):    # Custom Model Manager
    def get_queryset(self):
        return super().get_queryset().filter(is_active= True)

class InActivePersons(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active= False)


class Person(models.Model):          #Table
    # Django bydefalult id provide krta hai
    name = models.CharField(max_length = 200)
    age = models.IntegerField()
    mobile_num = models.IntegerField()
    address = models.CharField(max_length= 400)
    email = models.EmailField(null= True)
    date_joined = models.DateTimeField(auto_now= True, null= True)
    date_updated = models.DateTimeField(auto_now_add=True, null= True)
    is_active = models.BooleanField(default= True)
    isactivep = ActivePersons()
    isinactivep = InActivePersons()
    objects = models.Manager()

    

    class Meta:
        db_table = "person"

    def __str__(self):
        return f"{self.name}--{self.address}"

    def show_details(self):
        print(f"""--------------------------------
Person name:- {self.name}
Person age:- {self.age}
Person Mobile:- {self.mobile_num}
Person Address:- {self.address}""")

    @classmethod
    def get_data_above_age(cls):
        return cls.objects.filter(age__gte= 25)

    @classmethod
    def get_avg_age(cls):
        '''Average age of all persons'''
        data = Person.objects.all().values()
        age_list = list(map(lambda x:x["age"], list(data)))
        print(sum(age_list)//len(age_list))

    @classmethod
    def get_active_data(cls):
        return cls.objects.filter(is_active=True)

    @classmethod
    def get_inactive_data(cls):
        return cls.objects.filter(is_active= False)

"---------------------------------------------------------------------------------------"

class CommanClass(models.Model):
    name = models.CharField(max_length= 200)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True                       # due to this, it will not create table


class College(CommanClass):
    adr = models.CharField(max_length=500)
    est_date = models.DateField(auto_now= True)
    
    class Meta:
        db_table = "college"

class Principal(CommanClass):
    exp_total = models.FloatField()
    qual = models.CharField(max_length= 200)
    college = models.OneToOneField(College, on_delete=models.CASCADE, related_name= "princi")
    class Meta:
        db_table = "principal"


class Department(CommanClass):
   dept_strength = models.IntegerField()
   college = models.ForeignKey(College, on_delete= models.CASCADE, related_name= "depts")

   class Meta:
        db_table = "dept"
        unique_together = (("name","college"))  # same dept create nhi hoga same college ke liye


class Student(CommanClass):
    marks = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete= models.CASCADE, related_name= "studs", null=True)
    class Meta:
        db_table = "student"

class Subject(CommanClass):
    is_practical = models.BooleanField(default=False)
    student = models.ManyToManyField(Student)
    dept = models.ForeignKey(Department, on_delete= models.CASCADE, related_name= "subjs")
    class Meta:
        db_table = "subject"





"---------------------------------------------------------------------------------------------"


class FuelType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    name= models.CharField(max_length=255)
    fueltype = models.ManyToManyField(FuelType, related_name="carmodels")

    def __str__(self):
        return self.name        