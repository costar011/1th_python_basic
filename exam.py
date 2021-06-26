# 01
# 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
s = "hello"
t = "python"
# 두 변수를 이용하여 아래와 같이 출력해보세요.
# 실행 예: hello! python

print(f"{s}! {t}")

# 02
# movie_rank 리스트에서 '럭키'를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

# 내가 푼 답
movie_rank[3]
print(movie_rank)

movie_rank.remove("럭키")
print(movie_rank)

# 03
# lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
# 실행 예: langs ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']

# 내가 푼 답
print(lang1 + lang2)

total_lang = lang1 + lang2
print(total_lang)

# 04
# 다음 리스트에 저장된 데이터의 개수를 화면에 구하라.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자",
        "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]

print(len(cook))

# 05
# 다음 리스트의 평균을 출력하라.
nums = [1, 2, 3, 4, 5]
# 실행 예 : 3.0

sum_nums = 0
for num in nums:
    sum_nums += num
print(sum_nums / len(nums))

# 06
# 다음 코드를 for문으로 작성하라.
# print("++++")
# print(10)
# print(20)
# print(30)

for i in range(4):
    result = i * 10

    if(result == 0):
        print("+++")
    else:
        print(result)

# 07
# 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.
for i in range(2002, 2051, 4):
    print(i)

# 08
# 1부터 30까지의 숫자 중 3의 배수를 출력하라.
for i in range(1, 31):
    if(i % 3 == 0):
        print(i)


# 09
# 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory 로 한다.

inventory = {
    "메로나": [300, 20],
    "비비빅": [400, 3],
    "죠스바": [250, 100]
}


# 10
# icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

result = sum(icecream.values())
print(result)
