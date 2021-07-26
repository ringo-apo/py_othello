def hyoji(x,y):
    if board[x][y] == 'n':
        return '　'
    if board[x][y] == 'b':
        return '●'
    if board[x][y] == 'w':
        return '〇'

def serch_mannaka(arg1, arg2):
    if board[serch[0]][serch[1]] == 'b' or board[serch[0]][serch[1]] == 'w':
        return False
    return True

def serch_hidariue(arg1, arg2):
    x1 = arg1 - 1
    if x1<0:
        return False
    return True

def serch_ue(arg1, arg2):
    x1 = arg1 
    y1 = arg2 - 1

    if x1<0:
        return False

    if y1<0:
        return False

    return True

def serch_migiue(arg1, arg2):
    x1 = arg1 + 1
    y1 = arg1 - 1

    if x1<0:
        return False

    if y1<0:
        return False
    
    return True

def serch_hidari(arg1, arg2):
    x1 = arg1 - 1
    y1 = arg2

    if x1<0:
        return False

    if y1<0:
        return False

    return True

def serch_migi(arg1, arg2):
    x1 = arg1 + 1
    y1 = arg2

    if x1>7:
        return False

    if y1<0:
        return False

    if board[serch[0]][serch[1]] != 'w': 
        return False

    return True

def serch_hidarisita(arg1, arg2):
    x1 = arg1 - 1
    y1 = arg2 + 1

    if x1<0:
        return False

    if y1>7:
        return False

    return True

def serch_sita(arg1, arg2):
    x1 = arg1 
    y1 = arg2 + 1

    if y1>7:
        return False
    else:
        if board[x1][y1] == 'n':
            return False

    return True

def serch_migisita(arg1, arg2):
    x1 = arg1 + 1
    y1 = arg2 + 1

    if x1>7:
        return False

    if y1>7:
        return False

    if board[x1][y1] == 'n':
        return False

    return True


print ("Hello")
print ("  　Ａ　Ｂ　Ｃ　Ｄ　Ｅ　Ｆ　Ｇ　Ｈ")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("１＊　＊　＊　＊　＊　＊　＊　＊　＊")
print ("  ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("２＊　＊　＊　＊　＊　＊　＊　＊　＊")
print ("  ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("３＊　＊　＊　＊　＊　＊　＊　＊　＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("４＊　＊　＊　＊●＊〇＊　＊　＊　＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("５＊　＊　＊　＊〇＊●＊　＊　＊　＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("６＊　＊　＊　＊　＊　＊　＊　＊　＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("７＊　＊　＊　＊　＊　＊　＊　＊　＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("８＊　＊　＊　＊　＊　＊　＊　＊　＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")

board = [
          ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
          ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
          ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
          ['n', 'n', 'n', 'b', 'w', 'n', 'n', 'n'],
          ['n', 'n', 'n', 'w', 'b', 'n', 'n', 'n'],
          ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
          ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
          ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
]
print (board)

print ("  　Ａ　Ｂ　Ｃ　Ｄ　Ｅ　Ｆ　Ｇ　Ｈ")
print ("  ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("１＊" + hyoji(0, 0) + "＊" + hyoji(0, 1) + "＊" + hyoji(0, 2) + "＊" + hyoji(0, 3) + "＊" + hyoji(0, 4) + "＊" + hyoji(0, 5) + "＊" + hyoji(0, 6) + "＊" + hyoji(0, 7)+ "＊")
print ("  ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("２＊" + hyoji(1, 0) + "＊" + hyoji(1, 1) + "＊" + hyoji(1, 2) + "＊" + hyoji(1, 3) + "＊" + hyoji(1, 4) + "＊" + hyoji(1, 5) + "＊" + hyoji(1, 6) + "＊" + hyoji(1, 7) + "＊")
print ("  ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("３＊" + hyoji(2, 0) + "＊" + hyoji(2, 1) + "＊" + hyoji(2, 2) + "＊" + hyoji(2, 3) + "＊" + hyoji(2, 4) + "＊" + hyoji(2, 5) + "＊" + hyoji(2, 6) + "＊" + hyoji(2, 7) + "＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("４＊" + hyoji(3, 0) + "＊" + hyoji(3, 1) + "＊" + hyoji(3, 2) + "＊" + hyoji(3, 3) + "＊" + hyoji(3, 4) + "＊" + hyoji(3, 5) + "＊" + hyoji(3, 6) + "＊" + hyoji(3, 7) + "＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("５＊" + hyoji(4, 0) + "＊" + hyoji(4, 1) + "＊" + hyoji(4, 2) + "＊" + hyoji(4, 3) + "＊" + hyoji(4, 4) + "＊" + hyoji(4, 5) + "＊" + hyoji(4, 6) + "＊" + hyoji(4, 7) + "＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("６＊" + hyoji(5, 0) + "＊" + hyoji(5, 1) + "＊" + hyoji(5, 2) + "＊" + hyoji(5, 3) + "＊" + hyoji(5, 4) + "＊" + hyoji(5, 5) + "＊" + hyoji(5, 6) + "＊" + hyoji(5, 7) + "＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("７＊" + hyoji(6, 0) + "＊" + hyoji(6, 1) + "＊" + hyoji(6, 2) + "＊" + hyoji(6, 3) + "＊" + hyoji(6, 4) + "＊" + hyoji(6, 5) + "＊" + hyoji(6, 6) + "＊" + hyoji(6, 7) + "＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("８＊" + hyoji(7, 0) + "＊" + hyoji(7, 1) + "＊" + hyoji(7, 2) + "＊" + hyoji(7, 3) + "＊" + hyoji(7, 4) + "＊" + hyoji(7, 5) + "＊" + hyoji(7, 6) + "＊" + hyoji(7, 7) + "＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")

print("黒番")
print("A1")

serch = (0, 0)
print (serch)

# 真ん中
kekka_mannaka = serch_mannaka(*serch)
print (kekka_mannaka)

if kekka_mannaka == True:

    # 左上
    kekka_hidariue = serch_hidariue(*serch)
    print (kekka_hidariue)

    kekka_ue = serch_ue(*serch)
    print (kekka_ue)

    kekka_migiue = serch_migiue(*serch)
    print (kekka_migiue)

    kekka_hidari = serch_hidari(*serch)
    print (kekka_hidari)

    kekka_migi = serch_migi(*serch)
    print (kekka_migi)

    kekka_hidarisita = serch_hidarisita(*serch)
    print (kekka_hidarisita)

    kekka_sita = serch_sita(*serch)
    print (kekka_sita)

    kekka_migisita = serch_migisita(*serch)
    print (kekka_migisita)

board2 = board

board2[x][y] = 'a'
print (board2)


print ("  　Ａ　Ｂ　Ｃ　Ｄ　Ｅ　Ｆ　Ｇ　Ｈ")
print ("  ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("１＊" + hyoji(0, 0) + "＊" + hyoji(0, 1) + "＊" + hyoji(0, 2) + "＊" + hyoji(0, 3) + "＊" + hyoji(0, 4) + "＊" + hyoji(0, 5) + "＊" + hyoji(0, 6) + "＊" + hyoji(0, 7)+ "＊")
print ("  ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("２＊" + hyoji(1, 0) + "＊" + hyoji(1, 1) + "＊" + hyoji(1, 2) + "＊" + hyoji(1, 3) + "＊" + hyoji(1, 4) + "＊" + hyoji(1, 5) + "＊" + hyoji(1, 6) + "＊" + hyoji(1, 7) + "＊")
print ("  ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("３＊" + hyoji(2, 0) + "＊" + hyoji(2, 1) + "＊" + hyoji(2, 2) + "＊" + hyoji(2, 3) + "＊" + hyoji(2, 4) + "＊" + hyoji(2, 5) + "＊" + hyoji(2, 6) + "＊" + hyoji(2, 7) + "＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("４＊" + hyoji(3, 0) + "＊" + hyoji(3, 1) + "＊" + hyoji(3, 2) + "＊" + hyoji(3, 3) + "＊" + hyoji(3, 4) + "＊" + hyoji(3, 5) + "＊" + hyoji(3, 6) + "＊" + hyoji(3, 7) + "＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("５＊" + hyoji(4, 0) + "＊" + hyoji(4, 1) + "＊" + hyoji(4, 2) + "＊" + hyoji(4, 3) + "＊" + hyoji(4, 4) + "＊" + hyoji(4, 5) + "＊" + hyoji(4, 6) + "＊" + hyoji(4, 7) + "＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("６＊" + hyoji(5, 0) + "＊" + hyoji(5, 1) + "＊" + hyoji(5, 2) + "＊" + hyoji(5, 3) + "＊" + hyoji(5, 4) + "＊" + hyoji(5, 5) + "＊" + hyoji(5, 6) + "＊" + hyoji(5, 7) + "＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("７＊" + hyoji(6, 0) + "＊" + hyoji(6, 1) + "＊" + hyoji(6, 2) + "＊" + hyoji(6, 3) + "＊" + hyoji(6, 4) + "＊" + hyoji(6, 5) + "＊" + hyoji(6, 6) + "＊" + hyoji(6, 7) + "＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
print ("８＊" + hyoji(7, 0) + "＊" + hyoji(7, 1) + "＊" + hyoji(7, 2) + "＊" + hyoji(7, 3) + "＊" + hyoji(7, 4) + "＊" + hyoji(7, 5) + "＊" + hyoji(7, 6) + "＊" + hyoji(7, 7) + "＊")
print ("　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")

