import re


def polynomial(formula:str) -> list:
    '''
    사용 용도:
        식이 다항식일때 분류해주는 함수
    매개 변수:
        ex) 3x + 1
    Todo:
        return 값 서술해두기
        어떻게 값을 나눌지 +, - 기준? -> 괄호 안에 있을때의 값은 제외하고 나눠야함
    '''
def division(formula:str)->list:
    '''
    사용 용도:
        괄호 판별 및 값 나누기
    '''
    results = []
    while '[' in formula or '(' in formula or '{' in formula:
        try:
            if '[' in formula:
                gual(formula, '[', ']')
            elif '{' in formula:
                gual(formula, '{', '}')
            elif '(' in formula:
                gual(formula, '(', ')')
            else:
                pass
        except:
            print('입력값이 잘못되었습니다')
    else:
        print('괄호 없을 떄')


    def gual(gual, back_gual):
        '''
        Todo:
            추출한 문자열을 formula 에서 제거해야함
        '''
        nonlocal results
        nonlocal formula
        try:
            # var_guals = ['[','{','(',']','}',')']
            gual_start = formula.find(gual)
            gual_end = formula.find(back_gual)
            sik_start = formula[:gual_start].rfind(' ')
            if sik_start == -1:
                sik = formula[:gual_end+1]
                results.append(sik)
                # formula.strip(sik)
                return 0
            sik = formula[sik_start:gual_end+1]
            results.append(sik)
            # formula.strip(sik)
            return 0
        except:
            raise Exception('gual 함수에서 오류')


    pass
if '__main__' == __name__:
    polynomial('ax[ax + 1] + 1')

def constant(num:str) -> str:
    '''
    사용 용도:
        상수항일때 사용
    '''
    return '0'


def fx_num(num:str) -> str: # 밑^[지수]  밑=mit 지수=jisu
    '''
    조건:
        밑에 x 가 존재해야한다.
    How to use:
        -밑^[지수]
    Raises:
        -mit의 슬라이스에서 앞부분을 전체 슬라이싱 했을 때
        앞부분에 예상치 못한 다항식일때 오류발생예정
    Todo:
        -지수갯수이상 지우기\n
        -다항식 처리연산하기
    '''
    if not '^' in num:
        mitnum = list(map(int, re.findall('\d+',num[:num.index('x')])))
        if len(mitnum) == 1:
            return mitnum[0]
    else:
        mit = num[num.index('^')-1:num.index('^')]
        mitnum = list(map(int, re.findall('\d+',num[:num.index('^')])))
        jisunum = list(map(int, re.findall('\d+',num[num.index('^['):])))

        if len(jisunum) != 1: #지수에 숫자값이 한개가 아닐때 -> 다항식지수? ex) 4x^[4x + 1]
            print('지수 이상')
        else:
            if len(mitnum) > 1: #띄어쓰기된 숫자 있다 판단 -> 다른 x값 있다.
                print('밑 갯수 이상') #나중에 다른함수로 연결예정
            elif len(mitnum) == 0: # 밑이 오직 x만 있을 때
                jisunum = jisunum[0]
                return (f"{jisunum}{'x' if jisunum != 1 else ''}{f'^[{jisunum-1}]' if jisunum-1>1 or jisunum-1<1 else ''}")
            else:#밑, 지수의 갯수가 일방적일때
                mitnum = mitnum[0]
                jisunum = jisunum[0]
                return (f"{mitnum*jisunum}{'x' if jisunum != 1 else ''}{f'^[{jisunum-1}]' if jisunum-1 > 1 or jisunum-1 < 1 else ''}")

# if '__main__' == __name__:
#     f = open('TestCaseLog.txt', 'a')
#     data = input()
#     print(fx_num(data))
#     f.write(f"fx_num('{data}') -> {fx_num(data)}\n")
#     f.close()


def e_fx(num:str)->str:
    '''
    Todo:
        -e감지 방법 생각해야함 다른 변수 안들어가게-> 띄어쓰기로 분할시키는게 어떤가 ex) a + 4x^[51]
    '''
    mitnum = list(map(int, re.findall('\d+',num[:num.index('^')])))
    jisunum = list(map(int, re.findall('\d+',num[num.index('^['):])))

# if '__main__' == __name__:
#     f = open('TestCaseLog.txt', 'a')
#     data = input()
#     print(e_fx(data))
#     f.write(f"e_fx('{data}') -> {e_fx(data)}\n")
#     f.close()
