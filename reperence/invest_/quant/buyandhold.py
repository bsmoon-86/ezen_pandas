import pandas as pd
import numpy as np

## buyandhold 함수로 생성
## 매개변수를 3개
## 데이터프레임 , 구매한 날, 판매한 날
def bnh(_df, _start, _end):
    # index의 데이터를 시계열로 변경
    _df.index = pd.to_datetime(_df.index, format='%Y-%m-%d')
    # 결측치와 무한대의 값을 제외시키는 부분
    _df = _df.loc[ ~_df.isin([np.nan, np.inf, -np.inf]).any(axis=1) ]
    # 종가를 제외한 나머지 컬럼을 모두 삭제
    _df = _df[['Close']]
    # 일별 수익율 컬럼를 생성
    _df['daily_rtn'] = _df['Close'].pct_change()
    # 구매한 날짜와 판매한 날짜를 기준으로 데이터를 필퍼( 행의 조건으로 필터 )
    _df = _df.loc[_start : _end]
    # 누적 수익율 컬럼을 생성
    _df['st_rtn'] = (1 + _df['daily_rtn']).cumprod()

    return _df