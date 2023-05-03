flag = False

for hour in range(24):
    for minute in range(60):
        for second in range(60):
            print(f"{hour}:{minute:02d}:{second:02d}")
            
            if hour == 2:
                flag = True
                break
            
        if flag:
            break
        
    if flag:
        break