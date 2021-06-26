# 아스키 코드
# String -> Char의 배열

text = "Hello World"
upper_cnt = 0
lower_cnt = 0

for t in text:
    print(ord(t))
    if(int(ord(t)) >= 65 and int(ord(t)) <= 90):
        upper_cnt += 1

    if int(int(ord(t)) >= 97 and int(ord(t)) <= 122):
        lower_cnt += 1


print(f"기준데이터는 [{text}] 입니다.")
print(f"대문자의 개수는 총 {upper_cnt} 입니다.")
print(f"소문자의 개수는 총 {lower_cnt}입니다.")
