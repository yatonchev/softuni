#Да се напише програма, която чете час и минути от 24-часово денонощие, въведени от потребителя и изчислява колко ще е часът след 15 минути. 
# Резултатът да се отпечата във формат часове:минути. Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59. 
# Часовете се изписват с една или две цифри. Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.

init_hour = int(input())
init_minutes = int(input())

total_time = (init_hour * 60) + init_minutes + 15

hours = total_time // 60
minutes = total_time % 60

if hours > 23:
    hours = 0
if minutes <10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")