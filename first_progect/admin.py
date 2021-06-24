from django.contrib import admin
from first_progect.models import Student, Course
# Register your models here.

class StudentInline(admin.StackedInline):
    model = Student
    fields = 'name age'.split()
    extra = 10

class CourseAdmin(admin.ModelAdmin):
    Inlines = [StudentInline]

class StudentAdmin(admin.ModelAdmin):
    list_display = "id name age birthday course".split()
    search_fields = 'name'.split()
    list_filter = 'birthday course'.split()
    list_editable = 'age birthday course'.split()

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)