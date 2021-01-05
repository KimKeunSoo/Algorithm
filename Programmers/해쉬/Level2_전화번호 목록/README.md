# 전화번호 목록

- darklight

- sublimevimemacs

- Python3 

###### 문제 설명

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

- 구조대 : 119
- 박준영 : 97 674 223
- 지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

##### 제한 사항

- phone_book의 길이는 1 이상 1,000,000 이하입니다.
- 각 전화번호의 길이는 1 이상 20 이하입니다.

##### 입출력 예제

| phone_book                  | return |
| --------------------------- | ------ |
| [119, 97674223, 1195524421] | false  |
| [123,456,789]               | true   |
| [12,123,1235,567,88]        | false  |

##### 입출력 예 설명

입출력 예 #1
앞에서 설명한 예와 같습니다.

입출력 예 #2
한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

입출력 예 #3
첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.



# 코드

```python
def solution(phone_book):

    for index1, num in enumerate(phone_book):
        for index2, num_punk in enumerate(phone_book):
            if index1 == index2:
                continue
            else:
                if num_punk.startswith(num):
                    return False
    return True
```



**Idea : 그냥 모든 완전 탐색으로 중복값 찾아내기**



해쉬로 풀지 않았다. O(n^2^)의 복잡도로 풀었는데 처음 startswith를 find로 써서 했다가 30분날렸다. (find, startswith 정리함)

근데 심지어 누구는 zip(zip 정리함)이란걸 써서 더 간단하게 해뒀더라. 아래 첨부한다.

```python
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
```



하지만 해쉬 문제의 취지에 맞게 해쉬로 짠 코드도 첨부한다.

```python
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
```





