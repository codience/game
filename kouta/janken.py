import random

class okane:
     def __init__(self, start=100):
        self.money = start
     def bet(self, start, win):
         if win == True:
             self.money  *= 2
         elif win == False:
             self.money = 0
     


print("じゃんけんへようこそ！")
start = int(input("スタート金額を入力してください"))
game = okane(start=start)
battle = int(input("試合回数を入力してください"))
print("あなたの所持金は", game.money, "＄スタートです！")

for _ in range(battle):

     hands = ["チョキ","グー","パー"]
     enemy_hand = hands[random.randint(0, 2)]
     my_hand = input("チョキ　グー　パー:")
     if my_hand == "チョキ":
          if enemy_hand == "チョキ":
               print("あいこです。")
               print("引き分け！賭け金なし！")
          elif enemy_hand == "グー":
               print("あなたの負けです。。。") 
               print("ザンネン！賭け金DOWN！")
               game.bet(start,False)
          elif enemy_hand == "パー":
               print("あなたの勝ちです！") 
               print("おめでとう！賭け金UP！") 
               game.bet(start,True) 
     elif my_hand == "グー":
          if enemy_hand == "チョキ":
                    print("あなたの勝ちです。")
                    print("おめでとう！賭け金UP！")
                    game.bet(start,True)
          elif enemy_hand == "グー":
                    print("あいこです。")
                    print("引き分け！賭け金なし！")
          elif enemy_hand == "パー":
                    print("あなたの負けです。。。")
                    print("ザンネン！賭け金DOWN！")
                    game.bet(start,False)
     elif my_hand == "パー":
          if enemy_hand == "チョキ":
                    print("あなたの負けです。。。")
                    print("ザンネン！賭け金DOWN！")
                    game.bet(start,False)
          elif enemy_hand == "グー":
                    print("あなたの勝ちです！")
                    print("おめでとう！賭け金UP！")
                    game.bet(start,True)
          elif enemy_hand == "パー":
                    print("あいこです。")
                    print("引き分け！賭け金なし！")
     print("相手の数字は", enemy_hand,"でした！")
     print("あなたの所持金は", game.money,"$です！")