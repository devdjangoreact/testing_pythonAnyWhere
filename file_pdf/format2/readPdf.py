import PyPDF2
import json

import os, re

folder_path = "/home/dev/testing_pythonAnyWhere/file_pdf/format2"

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
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text = text + page.extractText().encode("utf-8").decode("utf-8")
        count = count + 1


    text = text.replace("Завантажено з сайту https://тестування.укр/  - онлайн тестування КРОК\n1\nБуклет весна 2019 року\nЦей \
        тест можна пройти в режимі онлайн тестування насайті https://тестування.укр/testkrok/studing/812\n/", "")
    text = text.replace("ТЕСТУВАННЯ.УКР Бази тестів", "")
    text = text.replace("Завантажено з сайту - онлайн тестування КРОК", "")
    text = text.replace("Буклет українською мовою осінь перша зміна 2020 року", "")    

    text = text.replace("Це офіційні тести з сайту Центру тестування https://www.testcentr.org.ua", "")
    text = text.replace("Цей тест можна пройти в режимі онлайн тестування на сайті https://тестування.укр/testkrok/studing/76", "")
 
    text = text.replace("Завантажено з сайту https://тестування.укр/  - онлайн тестування КРОК", "")
    text = text.replace("Буклет весна 2019 року","")
    text = text.replace("Цей тест можна пройти в режимі онлайн тестування на сайті https://тестування.укр/testkrok/studing/812/","")
    text = text.replace("30°","")
    text = text.replace("70o","")
    
    text = text.replace("Призначення ентеросорбентівD.","Призначення ентеросорбентівD.\nПризначення ентеросорбентівE.")
    text = text.replace("Гострий реактивний психозD.","Гострий реактивний психозD.\nГострий реактивний психозE.")

    text = text.replace("Дати вдихати пари аміачного спиртуB.","Дати вдихати пари аміачного спиртуB. \n  Дати вдихати пари аміачного спиртуE.")
    text = text.replace("ssssssss","")
    text = text.replace("ssssssss","")
    text = text.replace("ssssssss","")
    text = text.replace("ssssssss","")
    text = text.replace("ssssssss","")
    
    
    
    
    
    list = text.split("\n")
    next_question = True

    count = 1
    question = ""
    answers = []
    n=1


    for text_item in list:
        
        text_item = " ".join(text_item.split())
        
        if "" == text_item:
            next_question=True
            continue
        
        
        elif ("A." in text_item or "B." in text_item or "C." in text_item or "D." in text_item or "E." in text_item ) \
            and ( text_item.endswith('A.') or  text_item.endswith("B.") or  text_item.endswith("C.") \
            or  text_item.endswith("D.") or  text_item.endswith("E.")) \
            and 'A.,' not in text_item \
            and '°C.' not in text_item \
            and 'oC.' not in text_item \
            and 'A.,' not in text_item \
            and True:
            
            
            next_question = False
            answer = text_item.replace("100%","")
            answer = answer.replace("0%","")
            
            if "*" in text_item:
                choise = True
            else:
                choise = False
                
            answers.append({                    
                    "sort": n,
                    "answer": answer,
                    "choise": choise
                })
            n=n+1

        else:
            question = question + text_item

        if n==6:
        
            data.append({
                         "question": question, 
                         "nomber":count,
                         "answers":answers
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
    

