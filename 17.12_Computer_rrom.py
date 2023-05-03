month = input()
number_of_hours_spent = int(input())
people_of_group = int(input())
time_of_day = input()

if month == "march" or \
    month == "april" or \
     month == "may" or\
      time_of_day == "day":
       electricity_price = 10.50

elif  month == "march" or \
       month == "april" or \
        month == "may" or \
         time_of_day == "night":
           electricity_price = 8.40   

if month == "june" or \
      month == "july" or \
       month == "august" or \
        time_of_day == "day":
         electricity_price = 12.60

elif  month == "june" or \
       month == "july" or \
        month == "august" or \
         time_of_day == "night":
          electricity_price = 10.20

                    
if people_of_group >= 4 :
  electricity_price * 0.90
if number_of_hours_spent >= 5 :
  people_of_group / 2
    
total_price = (electricity_price * people_of_group) * number_of_hours_spent

print(f"Price per person for one hour: {electricity_price}")
print(f"Total cost of the visit: {total_price:.2f}")