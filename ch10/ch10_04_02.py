import win32com.client

# 1) 거래량 분석을 통한 대박 주 포착
# https://wikidocs.net/3836

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
industryCodeList = instCpCodeMgr.GetIndustryList() # 전체 업종 가져오기
print_i = 0
for industryCode in industryCodeList:
    print_i = print_i + 1
    print(industryCode, instCpCodeMgr.GetIndustryName(industryCode))
    if print_i >= 15:
        break
#001 종합주가지수
#002 대형(시가총액)
#003 중형(시가총액)
#004 소형(시가총액)
#005 음식료품
#006 섬유,의복
#007 종이,목재
#008 화학
#009 의약품

tarketCodeList = instCpCodeMgr.GetGroupCodeList(5) # 음식료품
print_i = 0
for code in tarketCodeList:
    print_i = print_i + 1
    print(code, instCpCodeMgr.CodeToName(code))
    if print_i >= 40:
        break


tarketCodeList = instCpCodeMgr.GetGroupCodeList(5) # 음식료품
instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")
# Get PER
instMarketEye.SetInputValue(0, 67)
instMarketEye.SetInputValue(1, tarketCodeList)
# BlockRequest
instMarketEye.BlockRequest()
# GetHeaderValue
numStock = instMarketEye.GetHeaderValue(2)
# GetData
sumPer = 0
for i in range(numStock):
    sumPer += instMarketEye.GetDataValue(0, i)

print("Average PER: ", sumPer / numStock)