def solution(numbers):

    new_list = sorted(list(map(''.join, map(str, numbers))), key=lambda x: x*3, reverse = True )
    return str(int(''.join(new_list)))