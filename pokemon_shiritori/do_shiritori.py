import random
import json
import time
import copy

#jsonファイルを開く
json_open = open('./pokemon_data.json', 'r', encoding="utf-8")
pokemon_list = json.load(json_open)
pokemon_name = []
for i in range(len(pokemon_list)):
    pokemon_name.append(pokemon_list[i]['name'])

#ランダムなポケモンの名前を返す
def search_random(pokemon_list, word_unused):
    while True:
        num = random.choice(word_unused)
        word = pokemon_list[num]['name']
        if(word[len(word)-1] != 'ン'):
            break
    word_unused.remove(num)
    return word

#頭文字がinitialのポケモンの名前を返す
def search_word(pokemon_list, word_final, word_unused):
    tmp = copy.copy(word_unused)
    while True:
        num = random.choice(tmp)
        tmp.remove(num)
        word = pokemon_list[num]['name']
        if(word[0] == word_final and word[len(word)-1] != 'ン'):
            break

        if(len(tmp) == 0):
            return '00000'
    word_unused.remove(num)
    return word

#wordの最後の文字を返す
def search_final(word):
    i=len(word)-1
    while i > 0:
        word_final = word[i]
        if(word_final == 'ー'):
            i=i-1
        else:
            break
    return word_final

#不正な文字をカタカナ大文字に変換
def trans(word_final):
    if word_final in 'ァィゥェォッャュョヮヵヶ2XYZ♂♀' :
        word_final = word_final.replace('ァ','ア')
        word_final = word_final.replace('ィ','イ')
        word_final = word_final.replace('ゥ','ウ')
        word_final = word_final.replace('ェ','エ')
        word_final = word_final.replace('ォ','オ')
        word_final = word_final.replace('ッ','ツ')
        word_final = word_final.replace('ャ','ヤ')
        word_final = word_final.replace('ュ','ユ')
        word_final = word_final.replace('ョ','ヨ')
        word_final = word_final.replace('ヮ','ワ')
        word_final = word_final.replace('ヵ','カ')
        word_final = word_final.replace('ヶ','ケ')
        word_final = word_final.replace('2','ツ')
        word_final = word_final.replace('X','ス')
        word_final = word_final.replace('Y','イ')
        word_final = word_final.replace('Z','ト')
        word_final = word_final.replace('♂','ス')
        word_final = word_final.replace('♀','ス')
    return word_final

#wordがしりとりルール違反をしていないか確認
def judge(pokemon_name, word_unused, word_final, word):
    for i in range(0, len(pokemon_name)):
        if(pokemon_name[i] == word):
            poke_num = i
            break

    if(word not in pokemon_name):
        print("{} はポケモンの名前ではありません".format(word))
        return 0
    elif(poke_num not in word_unused):
        print("{} はすでに使用しました".format(word))
        return 0
    elif(word[0] != word_final):
        print("しりとりが成立していません")
        return 0
    elif(word[len(word)-1] == 'ン'):
        return -1
    else:
        word_unused.remove(poke_num)
        return 1

#しりとりを行う
def shiritori():
    #手番を決める
    print("あなたが...先攻:0 後攻:1 どちらでも:2")
    turn = input()
    if(turn == '2'):
        turn = random.randint(0, 1)

    if(turn == '0'):
        print("あなたが先攻です\n")

    else:
        print("あなたが後攻です\n")

    word_unused = list(range(0, len(pokemon_list)-1, 1))
    word = search_random(pokemon_list, word_unused)
    print("最初のポケモンは {} です\n".format(word))
    word_initial = word[0]
    word_final = jaconv.h2z(search_final(word), kana=True)
    word_final = trans(search_final(word))

    winner = 'non'

    #しりとり動作
    while True:
        if(turn == '0'):
            print("\nあなたの番です")
            print("「{}」から始まるポケモンを入力してください".format(word_final))
            while True:
                word = input()
                is_ok = judge(pokemon_name, word_unused, word_final, word)
                if(is_ok == 1):
                    break
                elif(is_ok == 0):
                    print("「{}」から始まるポケモンを入力してください".format(word_final))
                elif(is_ok == -1):
                    print("「ん」で終わりました")
                    winner = 'you lose'
                    break
            turn = '1'
        else:
            print("\n敵の番です")
            word = search_word(pokemon_list, word_final, word_unused)
            if(word != '00000'):
                print(word)
            else:
                winner = 'you win'
            turn = '0'

        word_final = trans(search_final(word))

        if(winner == 'you lose'):
            print("敵の勝ちです")
            break
        elif(winner == 'you win'):
            print("あなたの勝ちです")
            break