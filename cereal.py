import serial
import time
import smtplib
import os
import csv

#establishing the threshold for dryness; will later be used to send emails w/ logic
dry = 470

#we dont want spam
max_emails_perhour = 3
emails_sent = 0
hour_start = time.time()

#default state to avoid spam
email_sent = False

#logic for not sending more than 3 emails per hour 
def can_send_email(): 
        global emails_sent, hour_start
        current_time = time.time()
        if current_time - hour_start >= 3600:
                emails_sent = 0
                hour_start = current_time
        return emails_sent < max_emails_perhour
#defining proceduure/parameters/structure for email
def send_email(subject, body): 
        global emails_sent
        if can_send_email():
                email_body = f"Subject: {subject}\n\n{body}"
                os.system(f'echo "{email_body}" | msmtp asappooja@gmail.com')
                emails_sent += 1
                print("delivered aye aye")
        else:
                print("sorrys too many emails")

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)
#loop to read the arduinos cereal data, add it to the data csv using the writer
while True: 
        line = ser.readline().decode('utf-8').strip()
        value = int(line)
        from datetime import datetime
        with open('piplant_data.csv', mode='a') as file: 
                writer = csv.writer(file)
                writer.writerow([datetime.now(), value])
        if value > dry: #may need to fix this bc its not as intuitive; higher values = higher dryness. emails to water it 
                print("oh man piplant is sad")
                send_email("piplant dying of thirst", f"help please; {value} is the reading. \n yours truly, \n, the piplant :3")
                email_sent = True
        else:
                pass #doesnt do anything if the value is int he good range 
