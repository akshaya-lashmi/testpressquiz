from django.urls import path, include

from rest_framework.routers import DefaultRouter

from quiz.views import UserViewset,QuestionViewset,TestViewset,QuizViewset

router = DefaultRouter()

router.register(r'users', UserViewset)

router.register(r'question', QuestionViewset)

router.register(r'test', TestViewset)

router.register(r'quiz', QuizViewset)



