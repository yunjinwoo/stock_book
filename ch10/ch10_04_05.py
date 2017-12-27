import win32com.client

# 모의투자 가입하기
# 2) 매수/매도하기
# https://wikidocs.net/3838
# 이게 구매 코드라는데... ㄷㄷㄷ;;;; 대체 어디냐....
instCpTdUtil = win32com.client.Dispatch("CpTrade.CpTdUtil")
instCpTd0311 = win32com.client.Dispatch("CpTrade.CpTd0311")

instCpTdUtil.TradeInit()

accountNumber = instCpTdUtil.AccountNumber[0]
instCpTd0311.SetInputValue(0, 2)
instCpTd0311.SetInputValue(1, accountNumber)


instCpTd0311.SetInputValue(3, 'A003540')
instCpTd0311.SetInputValue(4, 10)
instCpTd0311.SetInputValue(5, 13000)
instCpTd0311.BlockRequest()

