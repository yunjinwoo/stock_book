import win32com.client

# 1) 거래량 분석을 통한 대박 주 포착
# https://wikidocs.net/3836

#http://money2.creontrade.com/e5/mboard/ptype_basic/HTS_Plus_Helper/DW_Basic_Read_Page.aspx?boardseq=284&seq=11&page=1&searchString=CpUtil.CpCodeMgr&p=8841&v=8643&m=9505

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
#001 종합주가지수
#002 대형(시가총액)
#003 중형(시가총액)
#004 소형(시가총액)
#005 음식료품
#006 섬유,의복
#007 종이,목재
#008 화학
#009 의약품

tarketCodeList = instCpCodeMgr.GetGroupCodeList(8) # 소형
print_i = 0

instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")
# Get PER
instMarketEye.SetInputValue(0, 67)
instMarketEye.SetInputValue(1, tarketCodeList)
# BlockRequest
instMarketEye.BlockRequest()
# GetHeaderValue
numStock = instMarketEye.GetHeaderValue(2)

sumPer = 0
i = 0
for code in tarketCodeList:
    print(code, instCpCodeMgr.CodeToName(code), instMarketEye.GetDataValue(0, i))

    sumPer += instMarketEye.GetDataValue(0, i)
    print_i = print_i + 1
    i = i + 1
    if print_i >= 40:
        break

print("Average PER: ", sumPer / numStock)
