import PyPDF2
import json

import os

folder_path = "/home/dev/testing_pythonAnyWhere/file_pdf/format4"

data_extrat = []

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Filter the list of files to only include files with the desired format
desired_formats = [".pdf"]
desired_files = [file for file in files if any(file.endswith(format) for format in desired_formats)]

# Process each file
for file in desired_files:
    file_path = os.path.join(folder_path, file)

    pdfFileObj = open(file_path, 'rb')
      
    pdf_reader = PyPDF2.PdfFileReader(pdfFileObj)   

    data = []

    count = 0
    text = ""
    start = True
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        if start:
            start =False
            continue
        text = text + page.extractText().encode("utf-8").decode("utf-8")
        count = count + 1

    text = text.replace("Інформаційна сторінка/Мої курси/ КРОК / KROK/ Крок 3 / Krok 3/ Крок 3 Загальна лікарська підготовка 2022", "")
    text = text.replace("Розпочатовівторок 1 листопад 2022 7:14", "")
    text = text.replace("СтанЗавершено", "")
    text = text.replace("Завершеновівторок 1 листопад 2022 7:17", "")
    text = text.replace("Витрачено часу2 хв 39 сек", "")


    text = text.replace("'Це офіційні тести з сайту Центру тестування https://www.testcentr.org.ua/'", "")
    text = text.replace("Балів 0 з 1", "")
    text = text.replace("Балів0/150", "")
    text = text.replace("Макс. оцінка до 1,00", "")
    text = text.replace("Відповіді не було", "")
    text = text.replace("Відмітити питання", "")


    text = text.replace("Відмітити питання", "")
    text = text.replace("Текст питання", "")
    text = text.replace("'Завантажено з сайту https://тестування.укр/  - онлайн тестування КРОК'", "")
    text = text.replace("'1ТЕСТУВАННЯ.УКР Бази тестів'", "")
    text = text.replace("'Буклет весна 2019 року'", "")
    text = text.replace("'Цей тест можна пройти в режимі онлайн тестування на сайті https://тестування.укр/testkrok/studing/812'", "")


    text = text.replace("Оцінка0 з можливих 10 (0%)", "")
    text = text.replace("Макс. оцінка до 1", "")
    text = text.replace("Відповіді не було", "")
    text = text.replace("https://testcentr .net/mod/quiz/review .php?attempt=58824&cmid=72&showall=1", "")
    text = text.replace("02.11.22, 22:51 Крок 3 Заг альна лік арськ а підг отовка 2022: Attempt review", "")
    
    
    text = text.replace("c. Свiжозаморожена плазм а  d. Крiопреципiта т", "c. Свiжозаморожена плазм а\n  d. Крiопреципiта т")
    text = text.replace("a. Гострий пiєлонефри т  b. Гострий гломерулонефри т ", "a. Гострий пiєлонефри т \n b. Гострий гломерулонефри т ")    
    text = text.replace("Виберіть одну відповідь:  ", "") 
    text = text.replace("Правиль на", "Правильна") 
    text = text.replace("відповід ь", "відповідь") 
    text = text.replace("d. Фiбриляцiя шлуночкi в ", "d. Фiбриляцiя шлуночкi в \n d. Фiбриляцiя шлуночкi в ") 
    text = text.replace("відпов ідь", "відповідь") 
    text = text.replace("d. УЗ Д органiв черевної порожнин и ", "d. УЗ Д органiв черевної порожнин и \n d. УЗ Д органiв черевної порожнин и ") 
    text = text.replace("Відмітити питанн я", "") 
    
    text = text.replace("Коментар", "") 
    text = text.replace("відпов ідь", "відповідь") 
    text = text.replace("відпов ідь", "відповідь") 
    text = text.replace("відпов ідь", "відповідь") 
    text = text.replace("відпов ідь", "відповідь") 
    text = text.replace("відпов ідь", "відповідь") 
    text = text.replace("відпов ідь", "відповідь") 
    text = text.replace("відпов ідь", "відповідь") 
    text = text.replace("відпов ідь", "відповідь") 
    text = text.replace("відпов ідь", "відповідь") 
    text = text.replace("відпов ідь", "відповідь") 
    text = text.replace("відпов ідь", "відповідь") 

    
    
    
    
    n=0
    while not n == 300:
        n=n+1
        text = text.replace(" " +str(n)+"/69", "")
        text = text.replace("Питання " +str(n), "")


    # text = " ".join(text.split())
    list = text.split("\n")
    next_question =True

    count = 1
    question = ""
    

    answers = []
    n=1
    for text_item in list:
        
        text_item = " ".join(text_item.split())
        
        if "" == text_item:
            next_question=True
            continue
        
        if "Завершити перегляд" in text_item:
            break
        
        elif ("a." in text_item or "b." in text_item or "c." in text_item or "d." in text_item or "e." in text_item ) \
            or "Правильна відповідь" in text_item \
            and ( text_item.startswith('a.') or  text_item.startswith("b.") or  text_item.startswith("c.") \
            or  text_item.startswith("d.") or  text_item.startswith("e.") or  "Правильна відповідь" in text_item ) \
             \
            and 'a.,' not in text_item \
            and '°C.' not in text_item \
            and 'oC.' not in text_item \
            and 'a.,' not in text_item \
            and True:
            
            spl_text2 = False
            
            if "a." in text_item and "b." in text_item:
                spl_text = text_item.split("b.")
                spl_text2 = True
                text_item = 'b. '+spl_text[1]
            elif  "b." in text_item and "c." in text_item:
                spl_text = text_item.split("c.")
                spl_text2 = True
                text_item = 'c. '+spl_text[1]
            elif  "c." in text_item and "d." in text_item:
                spl_text = text_item.split("d.")
                spl_text2 = True
                text_item = 'd. '+spl_text[1]
            elif  "d." in text_item and "e." in text_item:
                spl_text = text_item.split("e.")
                spl_text2 = True
                text_item = 'e. '+spl_text[1]  
                              
            if spl_text2:
                answers.append({                    
                    "sort": n,
                    "answer": spl_text[0],
                    "choise": False
                })
                n=n+1
                
            
            next_question = False
            answer = text_item.replace("100%","")
            answer = answer.replace("0%","")
            
            if "Правильна відповідь" in text_item:
                # if not len(answers) == 5:
                #     print(len(answers))
                #     answers.append({                    
                #     "sort": "n",
                #     "answer": "answer",
                #     "choise": "choise"
                # })
                
                choise = True
            else:
                choise = False
                
            answers.append({                    
                    "sort": n,
                    "answer": answer,
                    "choise": choise
                })
            n=n+1
            
        else :
            question = question + text_item
            continue
        # else:
        #     print(text_item)
        if n==7: 
            
            data.append({"question":question, 
                        "nomber":count,
                        "answers":answers,

                        })
            count = count + 1
            next_question =True
            question = ""
            answers=[]
            n=1
            
    pdfFileObj.close()

    data_extrat.append({"title":file[0:-4], "questions":data})

    
with open(file[0:-4]+'.json', 'w') as f:
    json.dump(data_extrat, f, ensure_ascii=False)  
  
