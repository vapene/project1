import re


def password_validation_check(pwd):
    """ Checking password validation

    :param pwd(str): password string
    :return: True or False : the result of checking validation

    # """

    if len(pwd) <6 or len(pwd)>12:
        print("길이를 조절")
        return False


    if re.findall('[a-zA-z0-9]+',pwd)[0] !=pwd:
        return False

    if len(re.findall("[a-z]",pwd))==0 or len(re.findall("[A-Z]+",pwd))==0:
        return False


    print(pwd,"는 적당합니다")
    return True

if __name__== '__main__':
    password_validation_check('ㄹㄴㅁㅇㄹㄴfs')
