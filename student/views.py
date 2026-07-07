from django.shortcuts import render , get_object_or_404 , redirect
from .models import StudentData1
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden , HttpResponseRedirect
from django import forms
from django.urls import reverse


# Create your views here.
def home(request):
    searchEnroll=request.GET.get("searchEnroll")
    if searchEnroll:
        student=StudentData1.objects.filter(enroll__icontains=searchEnroll)
    else:
        student = StudentData1.objects.all()
    return render(request,'home.html',{'student':student}) 


@login_required
def detail(request , student_id):
    student = get_object_or_404(StudentData1 , pk = student_id)

    if request.user.groups.filter(name = "Faculty").exists():
        return render(request , "detail.html" , {"data" : student , "is_faculty" : True})
    
    if hasattr(request.user , "student_profile") and student.user == request.user :
        return render(request , "detail.html" , {"data" : student , "is_faculty" : False})

    return render(request , "detail.html" , {"data" : student , "error" : "You dont have permission to access this page."})



class MarksForm(forms.ModelForm):
    class Meta:
        model = StudentData1
        fields = ["python" , "fsd" , "coa"]



@login_required
def edit_marks(request , student_id):
    if not request.user.groups.filter(name = "Faculty").exists():
        return HttpResponseForbidden("You do not have access to edit marks.")
    
    else:
        student = get_object_or_404(StudentData1 , pk = student_id)

        if request.method == "POST":
            form = MarksForm(request.POST , instance = student)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('detail', args=[student_id]))
            
            # else:
            #     form = MarksForm(instance = student)
            # return render(request , "edit_marks.html" , {"form" : form , "data" : student})
        else:
            form = MarksForm(instance = student)
            return render(request , "edit_marks.html" , {"form" : form , "data" : student})
        

@login_required
def delete_student(request , student_id):
    if not request.user.groups.filter(name = "Faculty").exists() :
        return HttpResponseForbidden("You do not have access to delete student.")
    
    student = get_object_or_404(StudentData1 , pk = student_id)

    if request.method == "POST":
        student.delete()
        return redirect("home")
    
    return render(request , "delete_student.html" , {"data" : student})