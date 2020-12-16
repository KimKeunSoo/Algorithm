def solution(answers):
    
    first_num = [1,2,3,4,5]
    second_num = [2,1,2,3,2,4,2,5]
    third_num = [3,3,1,1,2,2,4,4,5,5]
    c1,c2,c3 = 0,0,0
    
    for index in range(len(answers)):
        if first_num[index%len(first_num)] == answers[index]:
            c1+=1
        if second_num[index%len(second_num)] == answers[index]:
            c2+=1
        if third_num[index%len(third_num)] == answers[index]:
            c3+=1
    
    answer = []
    k = max(c1,c2,c3)
    if k == c1: 
        answer.append(1)
    if k == c2: 
        answer.append(2)
    if k == c3: 
        answer.append(3)
    
    return answer