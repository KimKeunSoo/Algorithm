# 소수 찾기

- 문제 설명

한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

##### 제한사항

- numbers는 길이 1 이상 7 이하인 문자열입니다.
- numbers는 0~9까지 숫자만으로 이루어져 있습니다.
- 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

##### 입출력 예

| numbers | return |
| ------- | ------ |
| 17      | 3      |
| 011     | 2      |

##### 입출력 예 설명

예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

- 11과 011은 같은 숫자로 취급합니다.



# 코드

```python
from itertools import permutations

def solution(numbers):
    answer = 0
    new_list = []
    all_list = []
    tmp = []
    tmp2 = []
    new_list = list(numbers)
    
    for i in range(len(new_list)):
        tmp.extend(list(map(''.join, permutations(new_list, i+1))))         
    
    for i in tmp:
        tmp2.append(int(i))
        
    all_list = list(set(tmp2))        

    for num in all_list:
        if is_prime(num):
            answer+=1
            
    return answer


def is_prime(chr):
    num = int(chr)
    if num <= 1:
        
        return False 
    for i in range(2, num):
        if num % i == 0:
            return False 
    print(num)
    return True
```



a = "12345" 일때 b = list(a) 하면 ['1', '2', '3', '4', '5'] 가 된다!



더 좋은 코드

```python
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
```

ㅅㅂ 존나 간단히 썼네 