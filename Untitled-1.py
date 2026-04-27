# student = []
# for i in range (3):
#     name = input("enter student name : ")
#     markes = int(input("enter the marks :"))
#     student.append((name,markes))
# print(student)
# student = []
# for i in range (3):
#     name = input("enter the name : ")
#     marks = int(input("enter the marks : "))
#     data = {"name":name ,"marks":marks}
#     student.append(data)
# total = 0
# for j in student:
#     total += j["marks"]
# average = total /3
# if average >= 80:
#     grade = "A"
# elif average >=70:
#     grade = "B "
# elif average >=60:
#     grade = " C "
# else:
#     grade = "Fail"
# print(student)
# print("total",total)
# print("avarage",average)
# print("grade", grade)
# student = []
# for i in range (3):
#     name = input("enter your name : ")
#     number = int(input("enter your marks : "))
#     data= {"name":name,"marks":number}
#     student.append(data)
# total = 0
# for j in student :
#     total += j["markes"]
# average = total / 3
# if average >= 90:
#     grade= "A"
# elif average >= 80:
#     grade= " B "
# elif average >= 70:
#     grade = "C"
# else:
#     grade= "fail"
# print(student)
# print("totak",total)
# print("average",average)
# print("student:",student)
# student = [
#     {"name": "Ali",   "marks": 75},
#     {"name": "Sara",  "marks": 92}
# ]

# for j in student:
#     print(j)
# student = [
#     {"name": "Ali",  "marks": 75},
#     {"name": "Sara", "marks": 92}
# ]

# print(student)
# student = [
#     {"name":" MUdassar" , "marks ": 75},
#     {"name": "sara","marks ":92}
#     ]
# student.append("name")

# student = []
# for i in range (3):
#     name = input("enter the name  : ")
#     marks = int (input("enter the marks : "))
#     data = [{"name :",name ,"marks :",marks}]
#     student.append(data)
# print(student)
# student = []
# for i in range(3):
#     name = input("enter name: ")
#     marks = int(input("enter marks: "))
#     data = {"name": name, "marks": marks} 
#     student.append(data)                    
# print(student)
# total = 0
# for j in student:
#     total +=  j["marks"]
# average = total / 3
# if average >= 90:
#     grade = "A"
# elif average >= 80:
#     grade = "B"
# elif average >= 70:
#     grade = "C"
# else:
#      grade = "Fail"
# print("grade", grade)
# print("total",total)
# print("avarage",average)
# def countdown(n):
#     if n == 0:
#         print("Go!")
#         return
#     print(n)
#     countdown(n - 1)   # khud ko call kiya!

# countdown(10)
# def coutup(n):
#     if n == 10:
#         print("go!")
#         return 
#     print(n)
#     coutup(n+1)
# coutup(10)
# def countup(n):
#     if n == 40:
#         print(n)
#         print("!GO")
#         return 
#     print(n)
#     countup(n+1)
# countup(20)
# file = open("students.txt", "w")
# file.write("Ali - 75\n")
# file.write("Sara - 92\n")
# file.close()
# file = open("students.txt", "r")
# content = file.read()
# file.close()
# print(content)
# file = open("mian.txt", "w")
# file.write(" name :Mian mudassar\n")
# file.write("age  : 21 - 77\n ")
# file.write("phone: 335556666656\n")
# file.write("city : shahkot \n")
# file.write("degree:bscs\n")
# file.close()
# file = open("mian.txt","a")
# file.write("district : nankanasahib\n")
# file.write("city ; abc\n")
# file.close()    
# file = open("mian.txt","r")
# r= file.read()
# file.close()
# print(r)
# # Purana tarika — 3 lines
# file = open("mian.txt", "r")
# r = file.read()
# file.close()
 
# # Naya tarika — 2 lines — better!
# with open("mian.txt", "r") as file:
#     r = file.read()
 
# name = input("Enter name: ")
# age = int(input("Enter age: "))
# total = age + 5
# print(total)
# student = {"name": "Ali", "age": 20}
# student["age"] = 25
# student["city"] = "Lahore"
# del student["name"]
# print(student)
# def greet(name, city="Lahore"):
#     return f"Hello {name} from {city}"

# print(greet("Ali"))
# print(greet("Sara", "Karachi"))
# student_name = []
# student_marks = []
# for i in range(3):
#     name= input("enter name: ")
#     marks= int(input("enter marks: "))
#     student_name.append(name)
#     student_marks.append(marks)
# print(student_name,student_marks)
# with open("rana.txt","w") as file:
#     for i in range(3):
#         file.write(student_name[i]+ " - " + str(student_marks[i])+"\n")
# with open("rana.txt", "r") as file:
#     content = file.read()
# print(content)
# student_marks = []
# student_name = []
# for i in range(3):
#     name = input("enter the name of student : ")
#     marks = int(input("enter the marks of student : "))
#     student_name.append(name)
#     student_marks.append(marks)
# total = 0
# for j in student_marks:
#     total += j
# average = total / 3
# if average >=90:
#     grade = "A"
# elif average >=80:
#     grade = "B"
# elif average >= 70:
#     grade=" C "
# elif average >=60:
#     grade = " D "
# else:
#     garde= " fail"
# max_marks = max(student_marks)
# min_marks = min(student_marks)
# max_index = student_marks.index(max_marks)
# min_index = student_marks.index(min_marks)
# print("names : ",student_name)
# print("marks ",student_marks)
# print("total ",total)
# print("average ",average)
# print("Highest:", student_name[max_index], max_marks)
# print("Lowest:", student_name[min_index], min_marks)

# contact = [ ]
# data = {"name ":"ali" ,"phone":3041830117, "city ":"shahkot"}
# contact.append(data)
# print(contact)
# contact= []
# for i in range (3):
#     name = input("enter your name : ")
#     phone = int(input("enter your phone number: "))
#     city = input("enter your city : ")
#     data= {"name":name,"phone":phone ,"city":city}
#     contact.append(data)
# for c in contact:
#     print(c["name"])
#     print(c["phone"])
#     print(c["city"])
# search_name = input("search: ")
# for c in contact:
#     if c["name"]==search_name:
#         print(c["name"], c["phone"], c["city"])
# contact = [ ]
# for i in range(3):
#     name = input("enter name : ")
#     phone= int (input("enter name : "))
#     city = input("enter city : ")
#     data={"name":name,"phone":phone,"city":city}
#     contact.append(data)
# for c in contact:
#     print(c["name"])
#     print(c["phone"])
#     print(c["city"])
# search_name = input("search : ")
# if c["name"]==search_name:
#     print(c["name"],c["phone"],c["city"])
   


# contact= []
# for i in range (3):
#     name = input("enter your name : ")
#     phone = int(input("enter your phone number: "))
#     city = input("enter your city : ")
#     data= {"name  ":name,"phone ":phone ,"city ":city}
#     contact.append(data)
#     print(contact)
# a = "123"
# a = a+a
# print(a)
# b = 123
# b = b+ b
# print(b)
# name = "Mudassar"
# print(len(name))
# print(name[0])
# print(name[-1])
# print(name[0:4])
# print(name.upper())
# print(name.lower())
# print(name.replace("Mudassar","ali"))
# print(name.split("a"))
# print("mian"+ " " " Mudassar")
# print(name.count("s"))
# print(name.find("d"))
# print(name.startswith("M"))
# print(name.endswith("r"))
# print("  hello  ".strip())
# print(name.isalpha())
# print("123".isnumeric())
# print(name * 2)
# print(f"my name is {name}")
# print(name.title())
# print(name.title())
# print(name.reverse())
# print(name.reverse())
# print(name[::-1])
# def mian(ali):
#     return ali
# def add(a, b):
#     return a + b
# print(add(3,3))
# add = lambda a,b :a + b
# print(add(5,3))
# add = lambda a,b :  a if a> b else b
# print(add(4 , 99))
# name = " Mudassar "
# def show():
#     print (name)
# show()
# # def miana():
#     city = "shahkot"
# print(city)
# name = " MUDASSAR "
# def change():
#     global name
#     name = "ALI"
# change()
# print(name)
# name = " MIAN "
# def show():
#     name = "ali"
# show()
# print(name)
# name = "HAMZA"
# def ss():
#     global name
#     name = " subhan"
# ss()
# print(name)
# import random
# print(random.randint(1,10))
# import random
# print (random.randint(1,10))
# print(random.choice(["apple","banana","mango"]))
# items= [1,2,3,4,5]
# random.shuffle(items)
# print (items )
# import random
# print(random.randint(1,10))
# print(random.choice(["apple","banana"," orange"]))
# item = [1,2,3,4,5,6]
# random.shuffle(item)
# print(item)
import random
words = ["python","java","html","css","php"]
selected_words= random.choice(words)
hidden = []
for letter in selected_words:
    hidden.append("-")
print(hidden)
guess = input("Guess a letter : ")
if guess in selected_words:
    print("correct")
else:
    print("wrong!")
for i in range(len(selected_words)):
    if selected_words[i] == guess:
        hidden[i] = guess
print(hidden)
    


# import random
# words = ["python","java","html","css","php"]

# selected_word = random.choice(words)

# print("Stored word:", selected_word)
# print("New call:", random.choice(words))
# print("New call:", random.choice(words))