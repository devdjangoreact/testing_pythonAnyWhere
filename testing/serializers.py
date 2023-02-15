from rest_framework import serializers

from .models import Category, Test, HashTag, SetTest, TestList, SetTestList


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = (
            "id",
        )

class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = "__all__"
        read_only_fields = (
            "id",
        )

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = "__all__"
        read_only_fields = (
            "id",
        )


class SetTestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SetTest
        fields = "__all__"
        read_only_fields = (
            "id",
        )

class TestWithSetSerializer(serializers.ModelSerializer):
    choise = SetTestSerializer(many=True)
    
    class Meta:
        model = Test
        fields = "__all__"
        read_only_fields = (
            "id",
        )


class SetTestListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = SetTestList
        fields = "__all__"
        read_only_fields = (
            "id", 
            "updated_date",
        )



class TestListSerializer(serializers.ModelSerializer):
    choised = SetTestListSerializer(many=True)
        
    class Meta:
        model = TestList
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_date",
            "updated_date",
        )
        