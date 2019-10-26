import random

class Okane:
    def __init__(self, start=100):
        self.money = start

    def bet(self, kakekin, win):
        if win == True:
            self.money += kakekin 
        elif win == False:
            self.money -= kakekin

game = Okane(1000)
print("インディアンポーカーへようこそ！")
print("あなたの所持金は", game,"スタートです!")

for _ in range(3):
    
    enemy_number = random.randint(1 ,13)
    print("相手の数字は", enemy_number, "です！")

    my_number = random.randint(1, 13)
    select = input("high or low :")

    if select == "high":
        #「高い」を選択した時
    if my_number > enemy_number:
        print("あなたの勝ちです！") 
        print("おめでとう！賭け金Up！") 
        
    elif my_number < enemy_number:
        print("あなたの負けです。。。")      
    elif select == "low":
        #「低い」を選択した時
        if my_number < enemy_number:
        print("あなたの勝ちです！")
        elif my_number > enemy_number:
            print("あなたの負けです。。。") 
    print("あなたの数字は", my_number, "でした！")


