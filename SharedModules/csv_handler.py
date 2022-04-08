import pandas as pd
from datetime import datetime,date
import csv

class csv_handler:

    def __init__(self):
        pass

    def save(records_to_save):
        with open(file_name,"a",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([x for x in records_to_save])

    def create(name):
        global file_name
        global file_name_skipped
        now = datetime.now()
        time_stamp = now.strftime("%H_%M")
        today = date.today()
        date_stamp = today.strftime("_%m_%d_%y")
        file_name_skipped = f"Output/Skipped/{name}Skipped{time_stamp}_{date_stamp}.csv"
        file_name = f"Output/Results/{name}{time_stamp}_{date_stamp}.csv"
        with open(file_name,"w",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(['Phone','Email','Status'])

    def read(input_file_name):
        records = []
        frame = pd.read_csv(f"Input/{input_file_name}.csv",dtype={"Phone": "string", "Email": "string"})
        dict_from_frame = frame.to_dict()
        lenn = len(dict_from_frame["Email"])
        for x in range(0,lenn):
            phone_number = dict_from_frame["Phone"][x]
            email = dict_from_frame["Email"][x]
            record = (phone_number,email)
            records.append(record)
        return records

    def skipped_create():
        with open(file_name_skipped,"w",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Phone","Email"])

    def skipped_save(records):
        with open(file_name_skipped,"a",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([x for x in records])

