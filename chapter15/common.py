import re

def email_validation_check(email):

    regex=r"[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}"


    find_result=re.findall(regex,email)

    if find_result[0] !=email:
        print('형식 맞지않음')
        return False

    print('서ㅓㅇ공')
    return True

