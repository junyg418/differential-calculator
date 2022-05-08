import re

    # elements = num.split(' ')
    # print(elements)

def fx_num(num:str) -> str: # 밑^[지수]  밑=mit 지수=jisu
    '''
    조건:
        밑에 x 가 존재해야한다.
    How to use:
        -밑^[지수]
    Raises:
        -mit의 슬라이스에서 앞부분을 전체 슬라이싱 했을 때
        앞부분에 예상치 못한 다항식일때 오류발생예정\n
        -밑에 수가 존재 하지않으면 None 발생
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
            pass
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

if '__main__' == __name__:
    print(fx_num('x^[4]'))




def e_fx(num:str)->str:
    '''
    Todo:
        -e감지 방법 생각해야함 다른 변수 안들어가게-> 띄어쓰기로 분할시키는게 어떤가 ex) a + 4x^[51]
    '''
    mitnum = list(map(int, re.findall('\d+',num[:num.index('^')])))
    jisunum = list(map(int, re.findall('\d+',num[num.index('^['):])))
# print(x_num(input()))