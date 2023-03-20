from rest_framework.response import Response
from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
import json, random, string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction

from .models import Category, HashTag, Test, SetTest, TestList, SetTestList
from .serializers import CategorySerializer, HashTagSerializer, TestSerializer, TestWithSetSerializer
from .serializers  import  SetTestSerializer, TestListSerializer, SetTestListSerializer


# Category
class CategoryList(APIView):
    # permission_classes = [AllowAny,]

    def upload_test_pdf(self, file):
        
        
        f = open(file)
        data_json = json.load(f)
        try:
            category = Category.objects.get(pk=1)
        except:
            category = Category.objects.create(title="title")
        for text_item in data_json:       
            test = Test.objects.create(category=category, description=text_item['question'] )
            SetTest.objects.create(title= text_item['answer_a'],
                                        test=test, 
                                        description="test", 
                                        choise=False,
                                        sort='a')
            SetTest.objects.create(title= text_item['answer_b'],
                                        test=test, 
                                        description="test", 
                                        choise=False,
                                        sort='b')
            SetTest.objects.create(title= text_item['answer_c'],
                                        test=test, 
                                        description="test", 
                                        choise=False,
                                        sort='c')
            SetTest.objects.create(title= text_item['answer_d'],
                                        test=test, 
                                        description="test", 
                                        choise=False,
                                        sort='d')
            SetTest.objects.create(title= text_item['answer_e'],
                                        test=test, 
                                        description="test", 
                                        choise=False,
                                        sort='e')
            SetTest.objects.create(title= text_item['answer_true'],
                                       test=test, 
                                        description="test", 
                                        choise=True)
        

    def upload_testing_ukr(self, file):
        
        f = open(file)
        data_json_full = json.load(f)
        
        for data_json in data_json_full: 

   
            try:
                hashTag = HashTag.objects.get(title=data_json['title'])
            except:
                hashTag = HashTag.objects.create(title= data_json['title'])
                                                    
            category = Category.objects.get(pk=1)

            for text_item in data_json['questions']:       
                test = Test.objects.create(
                    category=category, 
                    description=text_item['question'],
                    nomber=text_item['nomber'])
                
                test.hashtag.add(hashTag)
                
                for text_item_answer in text_item['answers']:  
                    SetTest.objects.create(title= str(text_item_answer['answer']),
                                                test=test, 
                                                description="test", 
                                                choise=text_item_answer['choise'],
                                                sort=text_item_answer['sort'])
                


    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        
        # self.upload_test_pdf("/home/dev/testing_pythonAnyWhere/testing/source/data.json")
        # self.upload_testing_ukr('/home/dev/testing_pythonAnyWhere/testing/source/тестування.json')
        # self.upload_testing_ukr('/home/dev/testing_pythonAnyWhere/testing/source/format2.json')
        # self.upload_testing_ukr('/home/dev/testing_pythonAnyWhere/testing/source/format4.json')
        self.upload_testing_ukr('/home/dev/projects/testing_pythonAnyWhere/testing/source/format5.json')
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
    
    @transaction.atomic
    def post(self, request, pk, format=None):
        objhashtag = HashTag.objects.get(pk=pk)
        # create test list
        tests = Test.objects.filter(hashtag=objhashtag)  

        objectTestList = TestList.objects.create(
            title = objhashtag.title,
            description = objhashtag.title + " опис",
            quantity=tests.count()
        )
        # create set test list
        for test in tests:
            setTestLists = SetTestList.objects.create(
                test_list=objectTestList,
                test=test
            )

        return Response("created", status=status.HTTP_201_CREATED)


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
class TestListView(APIView):
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


class TestWithSetView(APIView):
    # permission_classes = [AllowAny,]

    def get(self, request, format=None):
        
        query = request.query_params.get('keyword')
        quantity = request.query_params.get('quantity')
        
        if query == None:
            query = ''
        
        test = Test.objects.filter(description__icontains=query).order_by('id')
        
        paginator = Paginator(test, 1000)
        page = request.query_params.get('page')
        
        try:
            tests = paginator.page(page)
        except PageNotAnInteger:
            tests = paginator.page(1)
        except EmptyPage:
            tests = paginator.page(paginator.num_pages)
        
        if page == None:
            page = 1
        
        serializer = TestWithSetSerializer(tests, many=True)
        return Response({'tests': serializer.data, 'page': page, 'pages': paginator.num_pages})
    
    # def get(self, request, pk, format=None):
    #     test = Test.objects.filter()
    #     serializer = TestWithSetSerializer(test)
    #     return Response(serializer.data)
    
    
# SetTest settest SetTestSerializer
class SetTestListView(APIView):
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
        serializer = TestListSerializer(testlist, many=True)
        all = request.GET.get('all')
     
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
        testlist_nom = serializer.data
        for test_nom in testlist_nom['choised']:
            test = Test.objects.filter(pk=test_nom["test"])
            test_nom["test"] = TestWithSetSerializer(test,many=True).data
        return Response([serializer.data])

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
        
    
        query = request.query_params.get('settest')
        
        settest = SetTest.objects.get(pk=int(query))
        
        test_list = TestList.objects.get(pk=1)
        
  
        
        
        serializer = SetTestListSerializer(data={
            'test_list':test_list.id,
            'set_test':settest.id,
            'test': settest.test.id,
            'mark':False,
            
        })
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

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "test_list": openapi.Schema(type=openapi.TYPE_STRING),
                "test": openapi.Schema(type=openapi.TYPE_STRING),
                "set_test": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def put(self, request, pk, format=None):
        settestlist = self.get_object(pk)
        # serializer = SetTestListSerializer(settestlist, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        set_test = SetTest.objects.get(id=request.data['params']['id'])
        settestlist.set_test = set_test
        settestlist.save()
        return Response("updated", status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        settestlist = self.get_object(pk)
        settestlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

