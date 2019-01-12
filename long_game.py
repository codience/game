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


print("敵が現れた！")
while True: 
    print("あなたの攻撃！")
    y_at = your_attack()
    c_df = cp_defence()
    if y_at == "上段":
        if c_df == "ジャンプ" or c_df == "テンションためる" or c_df == "クリティカル防御":
            hit = 30 * your_tension
            your_tension = your_tension - 1
            if your_tension == 0:
                your_tension = 1
        else:
            hit = 0
    elif y_at == "下段":
        if c_df == "しゃがむ" or c_df == "テンションためる" or c_df == "クリティカル防御":
            hit = 30 * your_tension
            your_tension = your_tension - 1
            if your_tension == 0:
                your_tension = 1
        else:
            hit = 0
    elif y_at == "テンションためる":
        hit = 0
        your_tension = your_tension + 1
    elif y_at == "クリティカル":
        if c_df == "クリティカル防御":
            hit = 0
            your_tension = 1
        else:
            hit = 999
    else:
        hit = 0
    if c_df == "テンションためる":
        cp_tension = cp_tension + 1
    print("あなたの攻撃は　{}".format(y_at))
    print("敵の防御は　{}".format(c_df))
    cp_life = cp_life - hit
    if cp_life < 0:
        cp_life = 0
    print("敵に　{} ダメージ！！".format(hit))
    print("あなたのテンションは {}（上限４）".format(your_tension))
    print("敵のテンションは {}（上限４）".format(cp_tension))
    print("敵残りHP　　　{}".format(cp_life))
    if cp_life <= 0:
        print("あなたの勝ち！")
        break
    
    print("敵の攻撃！")
    c_at = cp_attack()
    y_df = your_defence()
    if c_at == "上段":
        if y_df == "ジャンプ" or y_df == "テンションためる":
            hit = 30 * cp_tension
            cp_tension = cp_tension - 1
            if cp_tension == 0:
                cp_tension = 1
        else:
            hit = 0
    elif c_at == "下段":
        if y_df == "しゃがむ" or y_df == "テンションためる":
            hit = 30 * cp_tension
            cp_tension = cp_tension - 1
            if cp_tension == 0:
                cp_tension = 1
        else:
            hit = 0
    elif c_at == "テンションためる":
        hit = 0
        cp_tension = cp_tension + 1
    elif c_at == "クリティカル":
        if y_df == "クリティカル防御":
            hit = 0
            cp_tension = 1
        else:
            hit = 999
    else:
        hit = 0
    if y_df == "テンションためる":
        your_tension = your_tension + 1
    print("敵の攻撃は　{}".format(c_at))
    print("あなたの防御は　{}".format(y_df))
    your_life = your_life - hit
    if your_life < 0:
        your_life = 0
    print("あなたに　{} ダメージ！！".format(hit))
    print("あなたのテンションは {}（上限４）".format(your_tension))
    print("敵のテンションは {}（上限４）".format(cp_tension))
    print("あなたの残りHP   {}".format(your_life))
    if your_life <= 0:
        print("あなたの負け・・・")
        break

    

