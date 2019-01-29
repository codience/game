import sys
import random
hit = 0
your_life = 100
cp_life = 100
your_tension = 1
cp_tension = 1
y_at = 0
c_at = 0
y_df = 0
c_df = 0
teki = 0
your_level = 1
answer = 0
answer2 = 0

param = [your_level, your_life, cp_life, your_tension, cp_tension, hit, teki, y_at, y_df, c_at, c_df, answer, answer2]
def your_attack():
    if your_tension >= 4:
        y_at = input("攻撃は？上段、下段、クリティカル: ")
    else:
        y_at = input("攻撃は？上段、下段、テンションためる: ")
    return y_at

def your_defence():
    if cp_tension >= 4:
        y_df = input("防御は？ジャンプ、しゃがむ、クリティカル防御、テンションためる: ")
    else:
        y_df = input("防御は？ジャンプ、しゃがむ、テンションためる: ")
    return y_df

def cp_attack():
    if cp_tension >= 4:
        c_at = random.choice(("攻撃系","クリティカル"))
    else:
        c_at = random.choice(("上段","下段","テンションためる"))
    if c_at == "攻撃系":
        c_at = random.choice(("上段","下段"))
    return c_at

def cp_defence():
    if your_tension >= 4:
        c_df = random.choice(("防御系","クリティカル防御"))
    else:
        c_df = random.choice(("ジャンプ","しゃがむ","テンションためる"))
    if c_df == "防御系":
        c_df = random.choice(("ジャンプ","しゃがむ","テンションためる"))
    return c_df

def syutugen(param):
    param[4] = 0
    param[1] = param[0] * 10 + 100
    param[6] = random.choice(("ザコ","普通の敵","手強い敵","ボス"))
    if param[6] == "ザコ":
        cp_life = 50
    if param[6] == "普通の敵":
        cp_life = 100
    if param[6] == "手強い敵":
        cp_life = 150
    if param[6] == "ボス":
        param[2] = 200
    print(param[6] + "が現れたようだ・・・") 
    param[11] = input("この敵と戦いますか？ はい　or　いいえ：")
    if param[11] == "はい":
        while True:
                print("あなたの攻撃！")
                param[7] = your_attack()
                param[10] = cp_defence()
                if param[7] == "上段":
                    if param[10] == "ジャンプ" or param[10] == "テンションためる" or param[10] == "クリティカル防御":
                        param[5] = 20 * param[3] + 10 * param[0]
                        param[3] = param[3] - 1
                        if param[3] == 0:
                            param[3] = 1
                    else:
                        param[5] = 0
                elif param[7] == "下段":
                    if param[10] == "しゃがむ" or param[10] == "テンションためる" or param[10] == "クリティカル防御":
                        param[5] = 20 * param[3] + 10 * param[0]
                        param[3] = param[3] - 1
                        if param[3] == 0:
                            param[3] = 1
                    else:
                        param[5] = 0
                elif param[7] == "テンションためる":
                    param[5] = 0
                    param[3] = param[3] + 1
                elif param[7] == "クリティカル":
                    if param[10] == "クリティカル防御":
                        param[5] = 0
                        param[3] = 1
                    else:
                        param[5] = 999
                else:
                    param[5] = 0
                if param[10] == "テンションためる":
                    param[4] = param[4] + 1
                print("あなたの攻撃は　{}".format(param[7]))
                print("敵の防御は　{}".format(param[10]))
                param[2] = param[2] - param[5]
                if param[2] < 0:
                    param[2] = 0
                print("敵に　{} ダメージ！！".format(param[5]))
                print("あなたのテンションは {}（上限４）".format(param[3]))
                print("敵のテンションは {}（上限４）".format(param[4]))
                print("敵残りHP　　　{}".format(param[2]))
                if param[2] <= 0:
                    print("あなたの勝ち！")
                    param[0] = param[0] + 1
                    print("あなたのレベルは" + str(param[0]) + "になった！")
                    break
                
                print("敵の攻撃！")
                param[9] = cp_attack()
                param[8] = your_defence()
                if param[9] == "上段":
                    if param[8] == "ジャンプ" or param[8] == "テンションためる":
                        param[5] = 30 * param[4]
                        param[4] = param[4] - 1
                        if param[4] == 0:
                            param[4] = 1
                    else:
                        param[5] = 0
                elif param[9] == "下段":
                    if param[8] == "しゃがむ" or param[8] == "テンションためる":
                        param[5] = 30 * param[4]
                        param[4] = param[4] - 1
                        if param[4] == 0:
                            param[4] = 1
                    else:
                        param[5] = 0
                elif param[9] == "テンションためる":
                    param[5] = 0
                    param[4] = param[4] + 1
                elif param[9] == "クリティカル":
                    if param[8] == "クリティカル防御":
                        param[5] = 0
                        param[4] = 1
                    else:
                        param[5] = 999
                else:
                    param[5] = 0
                if param[8] == "テンションためる":
                    param[3] = param[3] + 1
                print("敵の攻撃は　{}".format(param[9]))
                print("あなたの防御は　{}".format(param[8]))
                param[1] = param[1] - param[5]
                if param[1] < 0:
                    param[1] = 0
                print("あなたに　{} ダメージ！！".format(param[5]))
                print("あなたのテンションは {}（上限４）".format(param[3]))
                print("敵のテンションは {}（上限４）".format(param[4]))
                print("あなたの残りHP   {}".format(param[1]))
                if param[1] <= 0:
                    print("あなたの負け・・・")
                    param[0] = param[0] - 1
                    if param[0] < 1:
                        param[0] = 1
                    print("あなたのレベルは" + param[0])
                    break
    else:
        print("あなたは逃げたため、レベルが１下がってしまった！")
    param[12] = input("ゲームを続けますか？ はい　or　いいえ：")
    if param[12] == "いいえ":
        print("お疲れ様でした。")
        sys.exit()
    else:
        syutugen(param)

syutugen(param)