class minuserror(Exception):
    def __init__(self, msg):
        
        self.msg = msg
        
    def __str__(self):    #init 에서 정의한 값을 출력하는 것
        return self.msg
        
try:
    a = int(input("양수 입력하세요: "))
    if a<0:
        raise minuserror("다시 양수 입력해주세요")
except minuserror as err:
    print(err)
finally :
    print("ㅅㄱ")