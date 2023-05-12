import time
import pandas as pd

# Requests: HTTP 요청을 보낼 수 있도록 기능을 제공하는 라이브러리
import requests 
# BeautifulSoup: 웹 페이지의 정보를 쉽게 스크랩할 수 있도록 기능을 제공하는 라이브러리
from bs4 import BeautifulSoup 

# 데이터를 정리할 DataFrame 생성
df = pd.DataFrame(columns=['인적사고','process','발생일시','사고원인','피해상황'])

iStart = 20544


for i in range(iStart,1,-1):
    try:
        url = 'https://www.csi.go.kr/acd/acdCaseView.do?case_no=%s' %i
        print(url)
        data=requests.get(url)
        soup = BeautifulSoup(data.text, 'html.parser')
        # tr 을 찾기
        trs = soup.find_all('tr')
        
        # 인적사고 td만 찾기
        td = trs[7].find_all('td')
        incident = tds[1].text.strip()
        # 프로세스
        td = trs[11].find_all('td')        
        proce = tds[1].text.strip()
        #발생원인
        td = trs[15].find_all('td')
        reason = tds[1].text.strip()
        #발생일시
        td = trs[4].find_all('td')
        desc = tds[1].text.strip()
        #피해상황
        tds = trs[17].find_all('td')        
        die = tds[2].text.strip()
        
        # 발생일시에 대한 값이 2019 이하인 경우, continue
        if int(desc.split('-')[0]) < 2019:
            continue
        
        # incident, desc Dataframe에 할당
        df.loc[iStart-i,'인적사고'] = incident
        df.loc[iStart-i,'process'] = proce
        df.loc[iStart-i,'발생일시'] = desc
        df.loc[iStart-i,'사고원인'] = reason
        df.loc[iStart-i,'피해상황'] = die
    except:
        continue
    time.sleep(1)

df.to_csv('c:/data/accident/설사고수집.csv',index=False)




# 데이터 전처리

import pandas as pd 
data = pd.read_csv("c:/data/accident/건설사고수집.csv")


data['사고원인']

data.dropna(how='all', inplace=True)

data['사고원인'] = data['사고원인'].str.replace(':', '')
data['사고원인'] = data['사고원인'].str.replace('주원인', '')
data['사고원인'] = data['사고원인'].str.replace('*', '')

data['사고원인'] = data['사고원인'].str.replace('\t|\t|\r', '', regex=True)

data.info()

import re
#정규식으로 보조원인 제거 
data['사고원인'] = data['사고원인'].str.replace('보조원인.*$','', regex=True)
data['사고원인'] = data['사고원인'].str.replace('\n','', regex=True)


data = data.dropna()

data['사고원인'].unique()

data['사고원인'].value_counts()

data['사고원인'] = data['사고원인'].apply(lambda x: str(x).strip()) 


#발생일시컬럼을 이용해서 시간, 날짜 나누기 
data['date'] = data['발생일시'].apply(lambda x: x.split(' ')[0].strip())
data['time'] = data['발생일시'].apply(lambda x: x.split(' ')[1].strip())

data = data.drop(["발생일시"],axis = 1)


data.to_csv('c:/data/accident/건설사고.csv',index=False)

data = pd.read_csv("c:/data/accident/건설사고.csv")



df = pd.DataFrame(columns=['process','발생일시','사망'])

사망자 수 확인 
iStart = 20544



for i in range(iStart,1,-1):
    try:
        url = 'https://www.csi.go.kr/acd/acdCaseView.do?case_no=%s' %i
        print(url)
        data=requests.get(url)
        soup = BeautifulSoup(data.text, 'html.parser')
        # tr 을 찾기
        trs = soup.find_all('tr')
        
        # 사망자 수 
        tds = trs[17].find_all('td')        
        die = tds[2].text.strip()
        
        # 프로세스
        tds = trs[11].find_all('td')        
        proce = tds[1].text.strip()
        
        #발생일시
        tds = trs[4].find_all('td')
        desc = tds[1].text.strip()
        
        
        # 발생일시에 대한 값이 2019 이하인 경우, continue
        if int(desc.split('-')[0]) < 2019:
            continue
        
        # incident, desc Dataframe에 할당
        df.loc[iStart-i,'사망'] = die
        df.loc[iStart-i,'process'] = proce
        df.loc[iStart-i,'발생일시'] = desc
    except:
        continue
    time.sleep(1)