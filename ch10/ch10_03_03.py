#https://wikidocs.net/3685
# 3) PER, EPS 데이터 얻어 오기
#http://money2.creontrade.com/e5/mboard/ptype_basic/HTS_Plus_Helper/DW_Basic_Read_Page.aspx?boardseq=284&seq=131&page=1&searchString=CpSysDib.MarketEye&p=&v=&m=
import win32com.client

instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")
# SetInputValue
instMarketEye.SetInputValue(0, (4, 67, 70, 111))
instMarketEye.SetInputValue(1, 'A003540')

# BlockRequest
instMarketEye.BlockRequest()

# GetData
print("현재가: ", instMarketEye.GetDataValue(0, 0))
print("PER: ", instMarketEye.GetDataValue(1, 0))
print("EPS: ", instMarketEye.GetDataValue(2, 0))
print("최근분기년월: ", instMarketEye.GetDataValue(3, 0))