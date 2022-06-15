from datetime import datetime

current_date = datetime.now()
Date_of_registration = current_date.strftime("%d/%m/%Y")

print(Date_of_registration)