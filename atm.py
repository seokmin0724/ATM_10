
# balance : 통장에 들어있는 기본 금액을 담는 변수
# 1.입금, 2.출금, 3.영수증 보기, 4.종료 => 글자를 입력 받을지(입금, 출금...) / 숫자를 입력받을지(1, 2, 3... )
# 숫자로 원하는 기능을 입력할 수 있게 만들어주세요 그리고 사용자가 입력한 기능은 num 변수에 담아주세요
# deposit_amount: 
# withdraw_amount:
# 영수증 기능에는 사용되는 데이터타입은 list => [["입금", 5000, 8000],["출금", 3000, 5000], ["출금", 2000, 3000]]

#영수증 기능 구현을 위한 빈 리스트 선언
receipts = []

#원금을 담는 변수
balance = 3000


while True:
    num = input("사용하실 기능의 번호를 입력해주세요(1.입금, 2.출금, 3.영수증 보기, 4.종료) ")

    if num == "1":
        deposit_amount = input("입금할 금액을 입력해주세요 : ") # "123123123".isdigit => True
        if deposit_amount.isdigit() and int(deposit_amount) > 0:  #첫번째 조건 문자가 입력된건 아닌지 확인 / 0 보다 큰 금액을 입력했는지 
            balance += int(deposit_amount) # balance = balance + int(deposit_amount)
            print(f"고객님이 입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.")

            #영수증에 데이터 넣기
            receipts.append(("입금",deposit_amount, balance))
        else:
            print("정신차리고, 제대로된 숫자형태로 입금액을 작성해줘!!!")
    if num == "2":
        withdraw_amount = input("출금할 금액을 입력해주세요 : ")
        if withdraw_amount.isdigit() and int(withdraw_amount) > 0:
            withdraw_amount = min(balance, int(withdraw_amount))
            balance -= withdraw_amount # balance = balance - withdraw_amount
            print(f"고객님이 출금한 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다.")

            #영수증에 데이터 넣기
            receipts.append(("출금",withdraw_amount, balance))
        else:
            print("정신차리고, 제대로된 숫자형태로 입금액을 작성해줘!!!")
    if num == "3":
        #리스트에 값이 있을때와 없을때 달랐으면 합니다.
        #값이 있을때 출력 결과가 출금 : 3000원 | 잔액 : 5000원과 같이 나왔으면 합니다.
        #    ""
        if receipts:
            print("====영수증====")
            for i in receipts:
                print(i)
                print(f"{i[0]} : {i[1]}원 | 잔액 {i[2]}원")
        else:
            print("허거덩거덩스 영수증에 아무내역도 없습니다.")
    if num == "4":
        print("서비스를 종료합니다.")
        break

