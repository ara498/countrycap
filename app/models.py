from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_id=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=10)
    dept_loc=models.CharField(max_length=20)
  
    def __str__(self):
        return self.dept_name+str(self.dept_id)

class Employee(models.Model):
    emp_name=models.CharField(max_length=10,primary_key=True)
    emp_no=models.IntegerField()
    designation=models.CharField(max_length=20)
    sal=models.DecimalField(max_digits=40,decimal_places=2)
    cmm=models.DecimalField(max_digits=20,decimal_places=2,null=True,blank=True)
    Hire_date=models.DateField(auto_now_add=True)
    dept_id=models.ForeignKey(Dept,on_delete=models.CASCADE)
    MGR=models.ForeignKey('self',on_delete=models.SET_NULL,blank=True,null=True)
    
    
    def __str__(self):
        return self.emp_name+str(self.emp_no)

class SalGrade(models.Model):
        GRADE=models.IntegerField(primary_key=True)
        LowSAL=models.DecimalField(max_digits=20,decimal_places=3)
        HISAL=models.DecimalField(max_digits=20,decimal_places=3)
            

