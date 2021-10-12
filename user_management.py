import user_email as ue
import user_password_re as upr

class User:
    """


    """

    def __init__(self,email,password):
        self.email=email
        self.password=password
        self.check_validation()

    def check_validation(self):
        ue.email_validation_check(self.email)
        upr.password_validation_check(self.password)

if __name__=="__main__":
    user1=User('isi.cho@gmail.com','3jskMF4EM')
    print("==========================")
    user2=User('sdk*df@gmail.com','wr8idFSd')

