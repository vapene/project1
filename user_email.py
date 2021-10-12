import re

def email_validation_check(email):

    """


    :param email(str): email address
    :return: True or False

    """

    if re.findall(r"[\w.-]+@[\w.-]+.\w+",email)[0] != email:
        print('email 형식 체크')
        return False





    pass