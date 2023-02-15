import json
from .source.models import Category, Test, HashTag, SetTest, TestList, SetTestList




f = open('/home/dev/start-project/server/testing/check.json')
data_json = json.load(f)

for item in data_json: 
    for key, value in item.items():
        test = Test.objects.create({'description':text_item.question, 
                                'category':1})
        SetTest.objects.create({'title': text_item.answer_a,
                                    'test':test, 
                                    'description':"test", 
                                    'choise':  False})
        SetTest.objects.create({'title': text_item.answer_b,
                                    'test':test, 
                                    'description':"test", 
                                    'choise':  False})
        SetTest.objects.create({'title': text_item.answer_c,
                                    'test':test, 
                                    'description':"test", 
                                    'choise':  False})
        SetTest.objects.create({'title': text_item.answer_d,
                                    'test':test, 
                                    'description':"test", 
                                    'choise':  False})
        SetTest.objects.create({'title': text_item.answer_e,
                                    'test':test, 
                                    'description':"test", 
                                    'choise':  False})
        SetTest.objects.create({'title': text_item.answer_true,
                                    'test':test, 
                                    'description':"test", 
                                    'choise':  True})
            
        break