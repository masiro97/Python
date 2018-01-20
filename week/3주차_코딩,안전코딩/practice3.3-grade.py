score = input("점수를 입력하세요. ")
score = int(score)
if 90 <= score <= 100:
    print("A")

elif 80 <= score < 90:
    print("B")

elif 70 <= score < 80:
    print("C")

elif 60 <= score < 70:
    print("D")

else:
    print("환산할 수 없는 점수입니다.")
