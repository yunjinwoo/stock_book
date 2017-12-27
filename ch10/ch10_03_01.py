import win32com.client

# 연결방법
# http://money2.creontrade.com/e5/mboard/ptype_basic/plusPDS/DW_Basic_Read.aspx?boardseq=299&seq=35&page=1&searchString=&prd=&lang=8&p=8833&v=8639&m=9505
# https://wikidocs.net/2880
instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
print(instCpStockCode.GetCount())
for i in range(0, 10):
    print(instCpStockCode.GetData(0, i) , "-", instCpStockCode.GetData(1, i))

# A035420 - NAVER

# A000020 - 동화약품
# A000030 - 우리은행
# A000040 - KR모터스
# A000050 - 경방
# A000060 - 메리츠화재
# A000070 - 삼양홀딩스
# A000075 - 삼양홀딩스우
# A000080 - 하이트진로
# A000087 - 하이트진로2우B
# A000100 - 유한양행