from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=64)
    link = models.CharField(max_length=1024, blank=False, null=True)
    slug = models.CharField(max_length=64, unique=True)
    def __str__(self):
        return self.title 
    
class HashTag(models.Model):
    title = models.CharField(max_length=64, unique=True)
    def __str__(self):
        return self.title    
    
class Test(models.Model):
    description = models.CharField(max_length=2096)
    nomber = models.IntegerField(default=0, blank=False, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    hashtag = models.ManyToManyField(HashTag)
    def __str__(self):
        return f"{self.description}"
    
class SetTest(models.Model):
    title = models.CharField(max_length=256)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, blank=False, related_name='choise')
    choise = models.BooleanField(default=False,blank=True)
    description = models.CharField(max_length=256, unique=False)
    sort = models.CharField(max_length=16, default='') 
    def __str__(self):
        return f"{self.title}"
        
class TestList(models.Model):
    title = models.CharField(max_length=2096)
    quantity = models.IntegerField(default=0)
    description = models.CharField(max_length=256, unique=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title}"
    
class SetTestList(models.Model):
    test_list = models.ForeignKey(TestList, on_delete=models.DO_NOTHING, blank=False,  related_name='choised' )
    test = models.ForeignKey(Test, on_delete=models.DO_NOTHING, blank=False, null=True)
    set_test = models.ForeignKey(SetTest, on_delete=models.DO_NOTHING, blank=False, null=True)
    updated_date = models.DateTimeField(auto_now=True)
    mark = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.set_test}"
