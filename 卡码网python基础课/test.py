while True:
    try:
        s = list(input().split())
        total = 0
        n = len(s)
        valid_grades = True
        
        for grade in s:
            if grade == "A":
                total += 4
            elif grade == "B":
                total += 3
            elif grade == "C":
                total += 2
            elif grade == "D":
                total += 1
            elif grade == "F":
                total += 0
            else:
                print("Unknown")
                valid_grades = False
                break
        
        if valid_grades:
            average = total / n
            print(f"{average:.2f}")
    except:
        break

        