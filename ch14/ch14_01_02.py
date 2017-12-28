from pandas import Series, DataFrame

#pandas 패키지 설치
#2) Series 기초
#https://wikidocs.net/4364
kakao = Series([92600, 92400, 92100, 94300, 92300])
print(kakao)

kakao2 = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19',
                                                            '2016-02-18',
                                                            '2016-02-17',
                                                            '2016-02-16',
                                                            '2016-02-15'])
print(kakao2)


# 와... 이건 개쩌네;;;;
mine   = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])
merge = mine + friend
print(merge)