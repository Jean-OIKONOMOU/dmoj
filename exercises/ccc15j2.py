str1 = input()
happyFaces = str1.count(":-)")
sadFaces = str1.count(":-(")

if (sadFaces + happyFaces) == 0:
    print("none")
elif sadFaces == happyFaces:
    print("unsure")
elif sadFaces > happyFaces:
    print("sad")
else:
    print("happy")
