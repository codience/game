import random

class okane:
    def __init__(self, start=100, kakekin=20):
        self.money = start
        self.kake = kakekin
    def bet(self, kakekin, win):
        if win == True:
            self.money += kakekin
        elif win == False:
            self.money -= kakekin
game = okane()
print("じゃんけんへようこそ！")
print("あなたの所持金は", game.money, "＄スタートです！")

for _ in range(3):
     hands = ["チョキ","グー","パー"]
     enemy_hand = hands[random.randint(0, 2)]
     my_hand = input("チョキ　グー　パー:")
     if my_hand == "チョキ":
          if enemy_hand == "チョキ":
               print("あいこです。")
               print("引き分け！賭け金なし！"))
          elif enemy_hand == "グー":
               print("あなたの負けです。。。") 
               print("ザンネン！賭け金DOWN！")
               game.bet(kakekin,False)
          elif enemy_hand == "パー":
               print("あなたの勝ちです！") 
               print("おめでとう！賭け金UP！") 
               game.bet(kakekin,True) 
     elif my_hand == "グー":
          if enemy_hand == "チョキ":
                    print("あなたの勝ちです。")
                    print("おめでとう！賭け金UP！")
                    game.bet(kakekin,True)
          elif enemy_hand == "グー":
                    print("あいこです。")
                    print("引き分け！賭け金なし！")
          elif enemy_hand == "パー":
                    print("あなたの負けです。。。")
                    print("ザンネン！賭け金DOWN！")
                    game.bet(kakekin,False)
     elif my_hand == "パー":
          if enemy_hand == "チョキ":
                    print("あなたの負けです。。。")
                    print("ザンネン！賭け金DOWN！")
                    game.bet(kakekin,False)
          elif enemy_hand == "グー":
                    print("あなたの勝ちです！")
                    print("おめでとう！賭け金UP！")
                    game.bet(kakekin,True)
          elif enemy_hand == "パー":
                    print("あいこです。")
                    print("引き分け！賭け金なし！)) 
     print("相手の数字は", enemy_hand,"でした！")
     print("あなたの所持金は", game.money,"$です！")