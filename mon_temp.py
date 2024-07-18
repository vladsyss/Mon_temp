import csv
import smtplib
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def sendmsg(Subject, Body):
    # Создание объекта сообщения
    msg = MIMEMultipart()
 
    # Настройка параметров сообщения
    msg["From"] = "sysuev.va@gidroagregat.ru"
    msg["To"] = "sysuev.va@gidroagregat.ru"
    msg["Subject"] = Subject
 
    # Добавление текста в сообщение
    text = Body
    msg.attach(MIMEText(text, "plain"))
 
    # Отправка письма
    s = smtplib.SMTP("mail.gidroagregat.ru", '587')
    #print (type(s))
    s.starttls()
    s.send_message(msg)
 
    # Закрытие соединения
    s.quit()

incl_col = [0, 12, 13 , 14, 15, 16, 17, 18, 19, 20, 21, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]                          # индексы нужных столбцов
tmax = '45'
curr_date_0 = ''

while True:

    with open(r"\\SRV-11\C$\Portable\OpenHardwareMonitor\OpenHardwareMonitorLog-2024-07-18.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            col = list(row[i] for i in incl_col)
        print(col)                            # вывод нужных столбцов
        #print(col[0])
 
        curr_date = col[0]
        print (curr_date)
        if curr_date == curr_date_0:
            Subject, Body = "Мониторинг температуры в серверной прекращён!", "Мониторинг температуры в серверной прекращён!"
            print ("Мониторинг температуры в серверной прекращён!")
            sendmsg(Subject, Body)
            sys.exit()
        else:
            curr_date_0 = curr_date


        #Удаление элемента из списка по индексу в Python
        #https://sky.pro/media/udalenie-elementa-iz-spiska-po-indeksu-v-python/
        deleted_element = col.pop(0)
        #print(col)
    
        #Перебор элементов списка
        #https://stepik.org/lesson/444552/step/1
        for x in col:
            #print (x)
            if int(x) >= 45:
                #print (x)
                Subject, Body = "Возможно повышение температуры в серверной!", "Возможно повышение температуры в серверной!"
                print ("Возможно повышение температуры в серверной!")
                sendmsg(Subject, Body)
                sys.exit()
    time.sleep(60)