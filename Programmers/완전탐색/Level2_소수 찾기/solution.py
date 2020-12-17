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