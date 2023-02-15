import PyPDF2
import json


def remove_values_from_list(the_list, val):
       return [value for value in the_list if value != val]

pdfFileObj = open('data.pdf', 'rb')
  
pdf_reader = PyPDF2.PdfFileReader(pdfFileObj)

data = []

count = 0
text = ""
for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    text = text + page.extractText().encode("utf-8").decode("utf-8")
    count = count + 1
    # if count == 5:
    #     break

# text = str(text)

text = text.replace("Інформаційна сторінка/Мої курси/ КРОК / KROK/ Крок 3 / Krok 3/ Крок 3 Загальна лікарська підготовка 2022", "")
text = text.replace("Розпочатовівторок 1 листопад 2022 7:14", "")
text = text.replace("СтанЗавершено", "")
text = text.replace("Завершеновівторок 1 листопад 2022 7:17", "")
text = text.replace("Витрачено часу2 хв 39 сек", "")


text = text.replace("Неправильно\Балів 0 з 1", "")
text = text.replace("Балів 0 з 1", "")
text = text.replace("Балів0/150", "")
text = text.replace("Балів0/150", "")
text = text.replace("Балів0/150", "")
text = text.replace("Балів0/150", "")


text = text.replace("Оцінка0 з можливих 10 (0%)", "")
text = text.replace("Макс. оцінка до 1", "")
text = text.replace("Відповіді не було", "")
text = text.replace("https://testcentr .net/mod/quiz/review .php?attempt=58824&cmid=72&showall=1", "")
text = text.replace("02.11.22, 22:51 Крок 3 Заг альна лік арськ а підг отовка 2022: Attempt review", "")
n=0
while not n == 300:
    n=n+1
    text = text.replace(" " +str(n)+"/69", "")
    text = text.replace("Питання " +str(n), "")

list = text.split("\n")
next_question = False

count = 1
question = ""
for text_item in list:
    if "" == text_item:
        continue
    
    elif "a." in text_item:
        answer_a = text_item
    elif "b." in text_item:
        answer_b = text_item
    elif "c." in text_item:
        answer_c = text_item
    elif "d." in text_item:
        answer_d = text_item
    elif "e." in text_item:
        answer_e = text_item
        
    elif "Правильна відповідь: " in text_item:
        next_question = True
        answer_true = text_item
    else:
        question = question + " " + text_item
        
    if next_question:    
        data.append({"question":str(count) +"." + question, 
                    "answer_a":answer_a,
                    "answer_b":answer_b,
                    "answer_c":answer_c,
                    "answer_d":answer_d,
                    "answer_e":answer_e,
                    "answer_true":answer_true
                    })
        count = count + 1
        next_question =False
        question = ""


    
with open('data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False)  
  
pdfFileObj.close()