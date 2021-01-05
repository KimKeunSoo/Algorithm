def solution(phone_book):

    for index1, num in enumerate(phone_book):
        for index2, num_punk in enumerate(phone_book):
            if index1 == index2:
                continue
            else:
                if num_punk.startswith(num):
                    return False
    return True