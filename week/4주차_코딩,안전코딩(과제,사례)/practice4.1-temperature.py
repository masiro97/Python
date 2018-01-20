#입력
print('섭씨-화씨 온도변환기')
print('섭씨(C)를 화씨(F)로 변환하려면 1을')
print('화씨(F)를 섭씨(C)로 변환하려면 2를')
base = input('입력해주세요. ')
while not (base == '1' or base == '2'):
    base = input('입력해주세요. ')
if base == '1':
    print('섭씨(C)를 화씨(F)로 변환해드립니다.')
    tin = input('섭씨(C) 온도를 입력해주세요. ')
    while not (tin.isdigit() or tin[0] =='-' and tin[1:].isdigit()):
        tin = input('섭씨(C) 온도를 입력해주세요. ')
elif base == '2':
    print('화씨(F)를 섭씨(C)로 변환해드립니다.')
    tin = input('화씨((F) 온도를 입력해주세요. ')
    while not (tin.isdigit() or tin[0] =='-' and tin[1:].isdigit()):
        tin = input('화씨(F) 온도를 입력해주세요. ')

print()

#계산 및 출력
tin = int(tin)
if base =='1':
    tout = ((9.0/5.0) * tin) *32
    print('섭씨',tin,'도(C)는 화씨',round(tout), '도(C)입니다.')

elif base == '2':
    tout = ((5 * tin) - 160) / 9.0
    print('화씨',tin,'도(F)는 섭씨',round(tout),'도(F)입니다.')

print('감사합니다. 또 찾아주세요.')
    
