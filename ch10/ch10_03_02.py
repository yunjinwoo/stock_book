import win32com.client
#10-3-2  과거 데이터 얻어 오기
#https://wikidocs.net/3684
#http://money2.creontrade.com/e5/mboard/ptype_basic/HTS_Plus_Helper/DW_Basic_Read_Page.aspx?boardseq=284&seq=102


instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

instStockChart.SetInputValue(0, "A003540")
instStockChart.SetInputValue(1, ord('2'))
instStockChart.SetInputValue(4, 10)
#instStockChart.SetInputValue(5, 5)
#0	종목 코드	요청할 종목의 종목 코드
#1	요청 구분	‘1’: 기간으로 요청, ‘2’: 갯수로 요청
#2	요청종료일	YYYYMMDD 형식
#3	요청시작일	YYYYMMDD 형식
#4	요청개수	요청할 데이터의 개수
#5	필드	0: 날짜, 1: 시간, 2: 시가, 3: 고가, 4: 저가, 5: 종가, 6: 전일대비, 8: 거래량, 9: 거래대금, 10: 누적체결매도수량
#6	차트구분	‘D’: 일, ‘W’: 주, ‘M’: 월, ‘m’: 분, ‘T’: 틱
#9	수정주가	‘0’: 무수정주가, ‘1’: 수정주가

instStockChart.SetInputValue(5, (0, 2, 3, 4, 5, 8))
instStockChart.SetInputValue(6, ord('D'))
instStockChart.SetInputValue(9, ord('1'))


# BlockRequest
instStockChart.BlockRequest()

# GetHeaderValue
numData = instStockChart.GetHeaderValue(3)
numField = instStockChart.GetHeaderValue(1)

# GetDataValue
for i in range(numData):
    for j in range(numField):
        print(instStockChart.GetDataValue(j, i), end=" ")
    print("")


print("--------------------")
instStockChart.SetInputValue(1, ord('1'))
instStockChart.SetInputValue(2, 20161031)
instStockChart.SetInputValue(3, 20161020)

# BlockRequest
instStockChart.BlockRequest()

# GetHeaderValue
numData = instStockChart.GetHeaderValue(3)
numField = instStockChart.GetHeaderValue(1)

# GetDataValue
for i in range(numData):
    for j in range(numField):
        print(instStockChart.GetDataValue(j, i), end=" ")
    print("")