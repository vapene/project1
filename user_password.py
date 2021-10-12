def password_validation_check(pwd):
    """ Checking password validation

    :param pwd(str): password string
    :return: True or False : the result of checking validation

    # """

    if len(pwd) <6 or len(pwd)>12:
        print("길이를 조절")
        return False

    for c in pwd:
        if not c.isnumeric() and not c.isalpha():
            print('문자와 숫자만')
            return False

    upper=False
    lower=False

    for c in pwd:
        if upper and lower:
            break

        if c.isalpha():
            if not upper:
                upper=c.isupper()
            if not lower:
                lower=c.islower()

    if not upper or not lower:
        print(pwd,"대소문자 필요")
        return False

    print(pwd,"는 적당합니다")
    return True

if __name__== '__main__':
    password_validation_check('ㄹㄴㅁㅇㄹㄴfs')
