import do_shiritori as ds

while True:
    print("しりとりするなら1, 終了なら0")
    flag = input()
    if(flag == '0'):
        break
    elif(flag == '1'):
        print("しりとりを始めます\n")
        ds.shiritori()
    else:
        print("0か1を入力してください\n")