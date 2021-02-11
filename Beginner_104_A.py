#入力をrへ入れる
r = int(input())

#rが1200未満ならABC、2800未満ならARC、それ以上ならAGCを出力
if r < 1200:
    print("ABC")
elif r < 2800:
    print("ARC")
else:
    print("AGC")