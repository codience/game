class Student:
    def __init__(self, user_name):
        self.type = "student"
        self.name = user_name
    
    def say_hello(self):
        print("おはようございます" + self.name +"です")

student1 = Student(user_name="田中")
student2 = Student(user_name="山下")

3

# def gozaru(name, gobi):
#     print(name + "でござる。" + gobi)

# gozaru("コウタ", "ニンニン！！！！")