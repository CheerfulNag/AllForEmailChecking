from datetime import datetime,date

class logs_handler:

    def __init__(self,path):
        self.path = path
        now = datetime.now()
        time_stamp = now.strftime("%H:%M")
        today = date.today()
        date_stamp = today.strftime("/%m/%d/%y")
        file = open(f"{self.path}Log.txt", "w") 
        file.write(f"PROGRAM STARTED: {time_stamp} {date_stamp}"+"\n")
        file.close() 

    def add_records_to_logs(self,record_text):
        now = datetime.now()
        time_stamp = now.strftime("%H_%M")
        file = open(f"{self.path}Log.txt", "a") 
        file.write(f'{time_stamp}: {record_text}\n') 
        file.close() 

    def black_box(self,record_text):
        now = datetime.now()
        time_stamp = now.strftime("%H_%M")
        file = open(f"{self.path}black_box.txt", "w")
        file.write(f'{time_stamp}: {record_text}\n') 
        file.close() 

