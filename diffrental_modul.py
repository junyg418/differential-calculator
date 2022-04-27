import re


def x_num(num:str) -> str: # 밑^[지수]  밑=mit 지수=jisu
    mit = num[:num.index('^')]
    mitnum = list(map(int, re.findall('\d+',num[:num.index('^')])))
    jisunum = list(map(int, re.findall('\d+',num[num.index('^['):])))

    if len(jisunum) != 1: #지수에 숫자값이 한개가 아닐때 -> 비정상
        pass
    else:
        if len(mitnum) != 1: #띄어쓰기된 숫자 있다 판단 -> 다른 x값 있다.
            print('지수 갯수 이상') #나중에 다른함수로 연결예정
        else:#밑, 지수의 갯수가 일방적일때
            mitnum = mitnum[0]
            jisunum = jisunum[0]
            return (f"{mitnum*jisunum}{'x' if jisunum >= 1 else ''}{f'^[{jisunum-1}]' if jisunum > 1 or jisunum < 1 else ''}")



x_num(input())