import random


my_hand = input("チョキ　グー　パー:")
hands = ["チョキ","グー","パー"]
enemy_hand = hands[random.randint(0, 2)]

if my_hand == "チョキ":
    if enemy_hand == "チョキ":
      print("あいこです。")
    elif enemy_hand == "グー":
         print("あなたの負けです。。。")  
    elif enemy_hand == "パー":
    　　　print("あなたの勝ちです！")     
elif my_hand == "グー":
　　　if enemy_hand == "チョキ":
　　　   print("あなたの勝ちです。")
　　　elif enemy_hand == "グー":
          print("あいこです。")
     elif enemy_hand == "パー":
     　　　print("あなたの負けです。。。")
elif my_hand == "パー":
    if enemy_hand == "チョキ":
       print("あなたの負けです。。。")
    elif enemy_hand == "グー":
         print("あなたの負けです") 
    elif enemy_hand == "パー":
    　　　print("あいこです。")  