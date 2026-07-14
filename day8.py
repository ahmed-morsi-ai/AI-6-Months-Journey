import os
from datetime import datetime

file_name = "sales_log.txt"

if os.path.exists(file_name):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"تم الدخول بنجاح - {current_time}\n")