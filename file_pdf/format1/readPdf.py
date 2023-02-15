import PyPDF2
import json

import os

folder_path = "/home/dev/testing_pythonAnyWhere/file_pdf/format1"

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Filter the list of files to only include files with the desired format
desired_formats = [".pdf"]
desired_files = [file for file in files if any(file.endswith(format) for format in desired_formats)]
data_extrat = []
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


    text = text.replace("HTTP/1.0 200 OK Cache-Control: no-cache, private Date: Sun, 05 Dec 2021 18:45:46 GM", "")
    text = text.replace("ТЕСТУВАННЯ.УКР Бази тестів", "")
    text = text.replace("Завантажено з сайту - онлайн тестування КРОК", "")
    text = text.replace("Буклет українською мовою осінь перша зміна 2020 року", "")    
    


    list = text.split("\n")
    next_question = True

    count = 1
    question = ""
    answers = []
    n=1

    for text_item in list:
        
        if "" == text_item:
            next_question=True
            continue
        
        
        elif ("0%" in text_item or "100%" in text_item) and n<6 \
            and '10%.' not in text_item \
            and '10%,' not in text_item \
            and '90%.' not in text_item \
            and 'до 10%' not in text_item \
            and ' 30%.' not in text_item \
            and '-0%,' not in text_item \
            and '60% еритроцити' not in text_item \
            and '100% кисню' not in text_item \
            and '60%,' not in text_item:
            
            
            next_question = False
            answer = text_item.replace("100%","")
            answer = answer.replace("0%","")
            
            if "100%" in text_item:
                choise = True
            else:
                choise = False
                
            answers.append({                    
                    "sort": n,
                    "answer": answer,
                    "choise": choise
                })
            n=n+1

        elif next_question:
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
    

