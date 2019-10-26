import random

class Okane:
    def __init__(self, start=100, kakekin=20):
        self.money = start
        self.kake = kakekin
    def bet(self, kakekin, win):
        if win == True:
            self.money += kakekin 
        elif win == False:
            self.money -= kakekin

game = Okane()
print("インディアンポーカーへようこそ！")
print("あなたの所持金は", game.money,"$スタートです!")
for _ in range(3):
    
    enemy_number = random.randint(1 ,13)
    print("相手の数字は", enemy_number, "です！")

    my_number = random.randint(1, 13)
    kakekin = int(input("賭け金を入力して下さい"))

       
    select = input("high or low :")

    if select == "high":
        #「高い」を選択した時
       if my_number > enemy_number:
            print("あなたの勝ちです！") 
            print("おめでとう！賭け金Up！") 
            game.bet(kakekin, True)
       elif my_number < enemy_number:
           if select == "low":
        #「低い」を選択した時
                if my_number < enemy_number:
                    print("あなたの勝ちです！")
                    print("おめでとう！賭け金Up！")
                    game.bet(kakekin,True)
                elif my_number > enemy_number:
                    print("あなたの負けです。。。")
                    print("ザンネン！賭け金Down！")
                    game.bet(kakekin,False) 
    print("あなたの数字は", my_number, "でした！")
    print("あなたの所持金は、", game.money,"$です！")

