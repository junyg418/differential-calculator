# value = input().split(' ')

def checksign(value):#일반 스펙 곱미분법 분류 함수
    pass


def mibun(value):
    pass

def multiplymibun(value):
    pass

def jisumibun(value): #value ex) 4^7x, log(1,x), 2x, e^4x+1 |ln은사용 x
    if '^' in value:
        # valuenum = value[:value.index('e'or'x')]
        jisu = value[value.index('^')+1:]
        minusbool  = False
        if jisu[0] == '-':#부호
            if value[0] == '-':
                minusbool = False
            else:
                minusbool = True
        if 'e' in value:
            valuenum = [int(aa) for aa in value[:value.index('e')].split() if aa.isdigit()]
            print(valuenum)
            if jisu.isdigit():#상수 확인
                return '0'
            elif '^' in jisu:#지수에 지수가 있을 때
                jisujisu = jisumibun(jisu)
                return f"{'-'if minusbool else ''}{jisujisu if jisujisu !='1'else ''}e^{jisu}"
            else:#지수가 1차일때 
                fjisu = jisu[:jisu.index('x')]
                return f"{'-'if minusbool else ''}{valuenum*int(fjisu)}e^{jisu}"
        
        else:#a^x일때
            pass

print(jisumibun('44e^7x'))

def triFunc(value):
    useValue = value.lower()
    if useValue in 'cos': #value에 cos 값이 있을떄
        changeVal = f'-{mibun}sin{useValue[3:]}'
    if useValue in 'sin': #value에 sin 값이 있을떄
        pass
    if useValue in 'tan': #value에 tan 값이 있을떄
        pass


def plusMinChange(value):
    for facVal,index in enumerate(value, 1):
        if index % 2: #부호x 게산식일때
            if facVal[0] == '-':
                if answer[index-1] == '+': #뒷자리 -일때 앞 부호 -변환
                    answer[index-1] = '-' 


# answer = []
# ans_str = '미분값: '
# for core in answer:
#     ans_str += core
# print(ans_str)
