from django.contrib import admin
from django.db.models import Sum
# Register your models here.
from .models import*

admin.site.register(Receipe)
admin.site.register(StudentID)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Subject)

class subject_marks_admin(admin.ModelAdmin):
    list_display=['student','subject','marks']

admin.site.register(SubjectMarks,subject_marks_admin )

class ReportCardAdmin(admin.ModelAdmin):
    list_display=['student','student_rank','total_marks']
    def total_marks(self,obj):
        subject_marks=SubjectMarks.objects.filter(student=obj.student)
        return 0
    
admin.site.register(ReportCard,ReportCardAdmin)