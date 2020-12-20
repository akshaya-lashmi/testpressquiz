from django.contrib import admin

from quiz.models import User, Quiz, Question, Test


class UserTable(admin.ModelAdmin):
    pass


admin.site.register(User, UserTable)


class QuizTable(admin.ModelAdmin):
    pass


admin.site.register(Quiz, QuizTable)


class QuestionTable(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionTable)


class TestTable(admin.ModelAdmin):
    pass


admin.site.register(Test, TestTable)
