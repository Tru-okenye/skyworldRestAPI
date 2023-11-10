# views.py
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import QuestionSerializer, ResponseSerializer
from .models import Question, Response
from rest_framework.pagination import PageNumberPagination

class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  # You can adjust the page size as needed
    page_size_query_param = 'page_size'
    max_page_size = 100

class ResponseView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.ListModelMixin):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    pagination_class = CustomPageNumberPagination

    def perform_update(self, serializer):
        question_id = self.request.data.get('question')
        question = Question.objects.get(pk=question_id)
        serializer.save(question=question)
        

    @action(detail=False, methods=['get'])
    def filter_by_email(self, request):
        email_address = request.query_params.get('email_address', '')
        responses = Response.objects.filter(email_address=email_address)
        serializer = ResponseSerializer(responses, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def certificates(self, request, pk=None):
        response = get_object_or_404(Response, pk=pk)
        file_path = response.file_upload.path
        return FileResponse(open(file_path, 'rb'))
