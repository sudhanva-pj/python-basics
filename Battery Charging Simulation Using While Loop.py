battery =15
min=0
while battery < 100  :
    min=min+1
    battery = battery+2

    if battery > 100:
        battery = 100

    print(f"In {min} minute Battery: {battery} %.")
print("Battery is fully charged in ", min, " minute.")