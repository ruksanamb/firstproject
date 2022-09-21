from django.shortcuts import redirect, render
from studentapp.models import StudentDetails



# Create your views here.
def add_student(request):
    return render(request,'addstudent.html')

def add_student_details(request) :
    if request.method=='POST':
        sname=request.POST.get('name')
        sage=request.POST.get('age')
        sdate=request.POST.get('joining_date')
        saddress =request.POST.get('address')
        semail=request.POST.get('email')
        squalify=request.POST.get('qualification')
        sgender=request.POST.get('gender')

        student=StudentDetails(name=sname,
                            age=sage,
                            joining_date=sdate,
                            address=saddress,
                            email=semail,
                            qualification=squalify,
                            gender=sgender)
    student.save()              
    return redirect('show_page')          
def show_page(request):
    students=StudentDetails.objects.all()
    return render(request,'showlist.html',{'student':students})


def editpage(request,pk):
    students=StudentDetails.objects.get(id=pk) 
    return render(request,'editpage.html',{'students':students})


def edit_student_details(request,pk):
    if request=='POST':
        students=StudentDetails.objects.get(id=pk) 
        students.name=request.POST.get('name')
        students.age=request.POST.get('age')
        students.address=request.POST.get('address')
        students.email=request.POST.get('email')
        students.qualification=request.POST.get('qualification')
        students.gender=request.POST.get('gender')
        students.save()
        return redirect('show_page')
    return render(request,'editpage.html',)  

def delete_student(request,pk):
      students=StudentDetails.objects.get(id=pk) 
      students.delete()
      return redirect('show_page')

    
     




  