import pymongo
import datetime
import smtplib
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = client.get_database("nad_repo")
collection = db.get_collection("upload_file_info")

res = collection.find_one( {}, { "upload_csv_status"})
val = res['upload_csv_status']
print(val)
can = collection.find({"process_start_ts":{"$gte":datetime.datetime(2020,4,1,0,0,0), "$lt":datetime.datetime(2021,4,1,0,0,0)}}).count()
print(can)


s =smtplib.SMTP('ssd7mahi@gmail.com',25)
s.starttls()
s.login("ssd7mahi@gmail.com", "SWAYAM1234567890")
message = f"A total of {can+1} universities registered with a upload csv status of {val}"
s.sendmail("ssd7mahi@gmail.com", "s3091990@gmail.com", message)
s.quit()