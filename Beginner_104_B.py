#sを入力値として読み込む
s = input()

#問題文の通り順番にif文で読み込む。1度に一気でも良かった。
if s[0] == "A":
    s = s[1:]
    if "C" in s[1:-1] and s.count("C") == 1:
        s = s.replace("C","")
        if s.islower():
            print("AC")
        else:
            print("WA")
    else:
        print("WA")
else:
    print("WA")