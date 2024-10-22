from datetime import datetime


current_time = datetime.now()

#Display current date and time
print(current_time)

#Display the format  [YYYY-MM-DD HH:MM:SS]
format_1 = current_time.strftime("%Y-%m-%d %I:%M:%S")
print(format_1)

#Display the format  [MM/DD/YYYY]
format_2 = current_time.strftime("%m/%d/%Y")
print(format_2)

#Display the format  [Day, Month DD, YYYY]
format_3 = current_time.strftime("%a, %B %d, %Y")
print(format_3)

#Display the format  [Day, Month DD, YYYY HH:MM:SS AM/PM]
format_4 = current_time.strftime("%A, %B %d, %Y %I:%M:%S")
print(format_4)

#Format the date and time like "Thu-Jul-11 10:26:23 IST 2024"
format_5 = current_time.strftime("%a-%b-%d, %Y %I:%M:%S IST %Y")
print(format_5)

#Display Date only
print(current_time.strftime("%d"))

#Display Time only
print(current_time.strftime("%I:%M"))

#Display month only
print(current_time.strftime("%m"))

#Display Year only
print(current_time.strftime("%Y"))

#Display format- 8 [ISO format:]
iso_format = current_time.isoformat()
print(iso_format)