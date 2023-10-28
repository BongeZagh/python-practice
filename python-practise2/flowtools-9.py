#squares = []
#for values in range(2,21):
#    squares.append(values+13-12)
#
#print(squares)

#squares = [value**2 for value in range(1,11)]
#print(squares)
#for value in range(1,20):
#    print(value)


#value = list(range(1,999,231))
#print(value)
scores = {tom:85,alix:45,Nana:39,Yang:99}
    for name, score in scores.items():
        if score >= 90:
            grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)
