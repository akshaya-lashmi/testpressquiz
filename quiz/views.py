from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer

from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from quiz.models import User, Question, Test, Quiz
from quiz.serializer import UserSerializer, TestSerializer, QuestionSerializer, QuizSerializer


class UserViewset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user.html'

    def list(self, request, *args, **kwargs):
        queryset = User.objects.all()
        return Response({'users': queryset})


class QuestionViewset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'questionlist.html'

    def list(self, request, *args, **kwargs):
        queryset = Question.objects.all()
        return Response({'questions': queryset})


class QuizViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                  GenericViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'quiz.html'

    @action(detail=False)
    def showquiz(self, request):
        id = request.GET.get("id")
        queryset = Test.objects.filter(quiz__id=id)
        # print(queryset.question.query)
        return Response({'quiz': queryset})


class TestViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                  GenericViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
