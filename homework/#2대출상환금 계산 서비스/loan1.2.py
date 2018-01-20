# 대출 상환금 계산 서비스
# 대출금 상환금액을 계산해주는 프로그램
#
# 입력: 원금(principal) - 백만이상 정수만 허용
#      상환기간(years) - 1이상 정수만 허용
#      연이자율(interest rate) - 0.1~9.9 범위의 정수 또는 부동소수점수 만 허용
# 출력: 연상환금, 월상환금, 상환금 총액
#
# 작성자: 로봇공학과 신혜영(2015041703)
# 작성날짜: 2015년 9월 17일 (version 1.0)

print("대출 상환금 계산 서비스에 오심을 환영합니다.")

# 입력

principal = input("대출원금이 얼마인가요? (백만이상) ")

while not principal.isdigit() or int(principal) < 1000000:
    principal = input("대출원금이 얼마인가요? (백만이상) ")

principal = int(principal)
                
years = input("상환기간은 몇년인가요? (1년이상 연단위) ")
while not years.isdigit() or int(years) < 1 :
    years = input("상환기간은 몇년인가요? (1년이상 연단위) ")

years = int(years)

interest_rate = input("이자율은 몇 %인가요? (0.0-9.9) ")
rate_tuple = interest_rate.partition('.')

while not (interest_rate.isdigit() and len(interest_rate) == 1 or rate_tuple[0].isdigit() and rate_tuple[2].isdigit() \
           and len(rate_tuple[0]) == len(rate_tuple[2]) == 1) or float(interest_rate) == 0 : 
    interest_rate = input("이자율은 몇 %인가요? (0.0-9.9) ")
    rate_tuple = interest_rate.partition('.')
    
interest_rate  = float(interest_rate)/100

print()

# 상환금 계산


d = (1+interest_rate)**years * principal * interest_rate/((1+interest_rate)**years -1)
round(d)


# 출력
print("대출 상환금 내역을 알려드리겠습니다.")
print("대출원금:",principal,"원")
print("연 이자율",interest_rate,"%로",years,"년동안 상환")
print("1년에 한번씩 상환하시면 매년",round(d),"원씩 지불하셔야 합니다.")
print("1달에 한번씩 상환하시면 매달",round(d/12),"원씩 지불하셔야 합니다.")
print("상환 완료시까지 총 상환금액은",round(d*years),"원 입니다.")
print("저희 서비스를 이용해주셔서 감사합니다.")
print("또 들려주세요.")
