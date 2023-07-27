# hw_8_4.py

# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}
    
    def get_user_info(self):
        while 1:
            try:
                self.user_data["name"] = input("이름을 입력하세요 :")
                if self.user_data["name"] == "끝":
                    break
                self.user_data["age"] = int(input("나이를 입력하세요 :"))
                if self.user_data["age"] == "끝":
                    break
                self.user_data["data"] = input("사용자 정보 : ")
                if self.user_data["data"] == "":
                    print("사용자 정보가 입력되지 않았습니다.")
                if self.user_data["data"] == "끝":
                    break
            except ValueError:
                print("나이는 숫자로 입력해야 합니다")

    def display_user_info(self):
        print(self.user_data)
        pass

user = UserInfo()
user.get_user_info()
user.display_user_info()
