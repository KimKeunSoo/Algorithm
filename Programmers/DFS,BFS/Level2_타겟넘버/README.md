# 타겟 넘버

- ###### 문제 설명

  n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

  ```
  -1+1+1+1+1 = 3
  +1-1+1+1+1 = 3
  +1+1-1+1+1 = 3
  +1+1+1-1+1 = 3
  +1+1+1+1-1 = 3
  ```

  사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

  ##### 제한사항

  - 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
  - 각 숫자는 1 이상 50 이하인 자연수입니다.
  - 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

  ##### 입출력 예

  | numbers         | target | return |
  | --------------- | ------ | ------ |
  | [1, 1, 1, 1, 1] | 3      | 5      |





# 코드

```python
def solution(numbers, target):
    n = len(numbers)
    cnt = 0
    def dfs(L, total):
        if L == n:
            if total == target:
                nonlocal cnt
                cnt +=1
        else:
            dfs(L+1, total+numbers[L])
            dfs(L+1, total-numbers[L])
            
    dfs(0,0)
    
    return cnt
```



**Idea : ** 각 numbers의 원소에 대해서 취할 수 있는 경우의 수는 더하거나, 빼거나 둘 중 하나임. 트리를 머릿속으로 그리면서 DFS 사용, Level을 나타내는 L이라는 변수(제일 위 root , 즉 1부터 시작해서 n까지 생각)와 합산 값인 total을 전달, L이 numbers의 길이와 같을 때, 즉 마지막 까지 도달했을때 total값과 target값이 같으면 cnt를 1 증가 시킴. 재귀적으로 구현해서 마무리.



## 남의 풀이 1

```python
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
```



완전 탐색, [1: ] == [2,3,4,5, . . .] 슬라이스 사용. 파이써닉하게 짰다고 볼수 있다.

if not 도 자유자재로 쓰도록 적응해야겠다. 



**참고** 

if not **x** 의 조건에 들어맞는 x는 다음과 같다.

- False
- 0
- **빈** 리스트 [] 
- **빈** 튜플 ()
- **빈** 딕셔너리 {}
- **문자길이 0**의 문자열 ""
- **None**
- 등등 ㅎㅎ



## 남의 풀이 2

```python
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    # l =  [(1, -1), (3, -3), (2, -2)...]
    s = list(map(sum, product(*l)))
    # 무작위로 하나씩 뽑아서 sum을 반복하여 완성한 것을 list로 반환
    return s.count(target)
```

상당히 python의 장점을 극대화시킨 코드.. 나도 이런거에 익숙해져야겠다..



**product 사용법**

곱집합이란, 여러 집합들 간에 하나씩 뽑아 조합을 만들 수 있는 모든 수를 뜻함

```python 
from itertools import product

a = [1,2,3]
b = ['a', 'b', 'c']
c = [[1,2,3], ['a', 'b', 'c']]
d = [[1,2,3], ['a', 'b', 'c'],['!', '@', '#']]

x = product(a, b)
print(list(x))

# [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]

y = product(*c)
print(list(y))
# [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]

z = product(*d)
print(list(z))
# [(1, 'a', '!'), (1, 'a', '@'), (1, 'a', '#'), (1, 'b', '!'), (1, 'b', '@'), (1, 'b', '#'), (1, 'c', '!'), (1, 'c', '@'), (1, 'c', '#'), (2, 'a', '!'), (2, 'a', '@'), (2, 'a', '#'), (2, 'b', '!'), (2, 'b', '@'), (2, 'b', '#'), (2, 'c', '!'), (2, 'c', '@'), (2, 'c', '#'), (3, 'a', '!'), (3, 'a', '@'), (3, 'a', '#'), (3, 'b', '!'), (3, 'b', '@'), (3, 'b', '#'), (3, 'c', '!'), (3, 'c', '@'), (3, 'c', '#')]

```



**map 사용법**

```python
list(map(lambda a: a*2, [1, 2, 3, 4]))
# [2, 4, 6, 8]

x = [(1,2), (3,4)]
print(list(map(sum, list(x))))
# 각 list의 합을 구하면 어떻게 될것인가
# [3, 7]
print(list(map(sum, product(*x))))
# 각 list에서 하나씩 차출해서서 더하면 어떻게 될 것인가
# [4, 5, 5, 6]
```



**count**

count는 s.count(target)으로 이렇게 s안에 target이 몇개 있는지 세는거