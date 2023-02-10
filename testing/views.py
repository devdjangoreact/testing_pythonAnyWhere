from rest_framework.response import Response
from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView

from .models import Category, HashTag, Test, SetTest, TestList, SetTestList
from .serializers import CategorySerializer, HashTagSerializer, TestSerializer
from .serializers  import  SetTestSerializer, TestListSerializer, SetTestListSerializer


# Category
class CategoryList(APIView):
    # permission_classes = [AllowAny,]

    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING),
                "slug": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
    # permission_classes = [AllowAny,]
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING),
                "slug": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# HashTag hashtag HashTagSerializer
class HashTagList(APIView):
    # permission_classes = [AllowAny,]

    def get(self, request, format=None):
        hashtag = HashTag.objects.all()
        serializer = HashTagSerializer(hashtag, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def post(self, request, format=None):
        serializer = HashTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HashTagDetail(APIView):
    # permission_classes = [AllowAny,]
    def get_object(self, pk):
        try:
            return HashTag.objects.get(pk=pk)
        except HashTag.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        hashtag = self.get_object(pk)
        serializer = HashTagSerializer(hashtag)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def put(self, request, pk, format=None):
        hashtag = self.get_object(pk)
        serializer = HashTagSerializer(hashtag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hashtag = self.get_object(pk)
        hashtag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Test test TestSerializer
class TestList(APIView):
    # permission_classes = [AllowAny,]

    def get(self, request, format=None):
        test = Test.objects.all()
        serializer = TestSerializer(test, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "description": openapi.Schema(type=openapi.TYPE_STRING),
                "category": openapi.Schema(type=openapi.TYPE_STRING),
                "hashtag": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def post(self, request, format=None):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestDetail(APIView):
    # permission_classes = [AllowAny,]
    def get_object(self, pk):
        try:
            return Test.objects.get(pk=pk)
        except Test.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        test = self.get_object(pk)
        serializer = TestSerializer(test)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "description": openapi.Schema(type=openapi.TYPE_STRING),
                "category": openapi.Schema(type=openapi.TYPE_STRING),
                "hashtag": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def put(self, request, pk, format=None):
        test = self.get_object(pk)
        serializer = TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        test = self.get_object(pk)
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# SetTest settest SetTestSerializer
class SetTestList(APIView):
    # permission_classes = [AllowAny,]

    def get(self, request, format=None):
        settest = SetTest.objects.all()
        serializer = SetTestSerializer(settest, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING),
                "test": openapi.Schema(type=openapi.TYPE_STRING),
                "choise": openapi.Schema(type=openapi.TYPE_STRING),
                "description": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def post(self, request, format=None):
        serializer = SetTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SetTestDetail(APIView):
    # permission_classes = [AllowAny,]
    def get_object(self, pk):
        try:
            return SetTest.objects.get(pk=pk)
        except SetTest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        settest = self.get_object(pk)
        serializer = SetTestSerializer(settest)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING),
                "test": openapi.Schema(type=openapi.TYPE_STRING),
                "choise": openapi.Schema(type=openapi.TYPE_STRING),
                "description": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def put(self, request, pk, format=None):
        settest = self.get_object(pk)
        serializer = SetTestSerializer(settest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        settest = self.get_object(pk)
        settest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# TestList testlist TestListSerializer
class TestListList(APIView):
    # permission_classes = [AllowAny,]

    def get(self, request, format=None):
        testlist = TestList.objects.all()
        serializer = CategorySerializer(testlist, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING),
                "quantity": openapi.Schema(type=openapi.TYPE_STRING),
                "description": openapi.Schema(type=openapi.TYPE_STRING),
                "created_date": openapi.Schema(type=openapi.TYPE_STRING),
                "updated_date": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def post(self, request, format=None):
        serializer = TestListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestListDetail(APIView):
    # permission_classes = [AllowAny,]
    def get_object(self, pk):
        try:
            return TestList.objects.get(pk=pk)
        except TestList.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        testlist = self.get_object(pk)
        serializer = TestListSerializer(testlist)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING),
                "quantity": openapi.Schema(type=openapi.TYPE_STRING),
                "description": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def put(self, request, pk, format=None):
        testlist = self.get_object(pk)
        serializer = TestListSerializer(testlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        testlist = self.get_object(pk)
        testlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# SetTestList settestlist SetTestListSerializer
class SetTestListList(APIView):
    # permission_classes = [AllowAny,]

    def get(self, request, format=None):
        settestlist = SetTestList.objects.all()
        serializer = SetTestListSerializer(settestlist, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "test_list": openapi.Schema(type=openapi.TYPE_STRING),
                "set_test": openapi.Schema(type=openapi.TYPE_STRING),
                "mark": openapi.Schema(type=openapi.TYPE_BOOLEAN),
            },
        )
    )
    def post(self, request, format=None):
        serializer = SetTestListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SetTestListDetail(APIView):
    # permission_classes = [AllowAny,]
    def get_object(self, pk):
        try:
            return SetTestList.objects.get(pk=pk)
        except SetTestList.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        settestlist = self.get_object(pk)
        serializer = SetTestListSerializer(settestlist)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        settestlist = self.get_object(pk)
        serializer = SetTestListSerializer(settestlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        settestlist = self.get_object(pk)
        settestlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

