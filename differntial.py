# value = input().split(' ')
'''
jisujisu- ax^n 함수가 아직 구현되지 않아 지수에 지수가 있을경우 지수의 미분값이 None이나오는 오류 생김 
-확인 x
입력값 지수를 ()로 묶었을 때 지수의 지수를 슬라이싱 할떄 오류가 생김
'''
def checksign(value):#일반 스펙 곱미분법 분류 함수
    pass


def mibun(value):
    pass

def multiplymibun(value):
    pass

def jisumibun(value): #value ex) 4^7x, log(1,x), 2x, e^4x+1 |ln은사용 x
    if '^' in value:
        # valuenum = value[:value.index('e'or'x')]
        jisu = value[value.index('^')+1:]#str
        minusbool  = False
        if jisu[0] == '-':#부호
            if value[0] == '-':
                minusbool = False
            else:
                minusbool = True
        if 'e' in value:
            valuenum = [int(aa) for aa in value[:value.index('e')].split() if aa.isdigit()]
            val = valuenum[0]
            if jisu.isdigit():#상수 확인
                return '0'
            elif '^' in jisu:#지수에 지수가 있을 때
                jisujisu = jisumibun(jisu)
                return f"{'-'if minusbool else ''}{jisujisu if jisujisu !='1'else ''}e{'^('+jisu+')'}"
            else:#지수가 1차일때 
                fjisu = jisu[:jisu.index('x')]
                sangsu = val*int(fjisu)
                return f"{'-'if minusbool else ''}{sangsu if sangsu != 1 else ''}e^{jisu}"
        
        else:#a^x일때
            valuenum = [int(aa) for aa in value[:value.index('x')].split() if aa.isdigit()]
            val = valuenum[0]
            if value.isdigit():
                return '0'
            # elif '^' in jisu:  #구현 조금 힘듦 4x^2x^2 = lnf(x) = 2x^2*ln4x
            #     jisujisu = jisumibun(jisu)
            #     return f"{'-'if minusbool else ''}{jisujisu if jisujisu != '1' else''}x^{jisu}"
            else:
                fjisu = value[value.index('^')+1:]
                sangsu = val*int(fjisu)
                return f"{'-'if minusbool else ''}{sangsu if sangsu != 1 else ''}x{'^' + int(jisu)-1 if int(jisu)-1 != 1 else ''}"

print(jisumibun('45e^7x^2'))

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


answer = []
# ans_str = '미분값: '
# for core in answer:
#     ans_str += core
# print(ans_str)
