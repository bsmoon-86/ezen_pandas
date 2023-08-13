import pandas as pd
import os

# 위에서 작업한 특정 경로에서 파일을 로드하여 결합하는 함수를 생성 
# 매개변수로 사용할 부분 : 파일의 경로, 확장자
def list_data(_path, _end):
    # _path의 마지막 문자열이 '/'가 아니라면?
    if (_path[-1] != '/'):
        # 문자열 마지막에 '/' 추가해준다. 
        _path = _path+'/'

    # _end가 처음 문자가 '.'이 아니라면 '.'을 추가 
    if not(_end.startswith(".")):
        _end = "."+_end

    # 매개변수로 받아온 경로를 이용하여 해당 위치의 파일 리스트를 로드 
    file_list = os.listdir(_path)
    # print(file_list)

    # _end와 같은 파일명만 새로운 리스트로 생성
    end_list = []

    for i in file_list:
        if i.endswith(_end):
            end_list.append(i)

    # 비어있는 데이터프레임을 생성 
    result = pd.DataFrame()

    for i in end_list:
        if (_end == ".csv"):
            df = pd.read_csv(_path + i)
        elif (_end == ".json"):
            df = pd.read_json(_path + i)
        elif (_end == ".xlsx") | (_end == '.xls'):
            df = pd.read_excel(_path + i)
        result = pd.concat([result, df], axis=0, ignore_index=True)

    return result

print('list start')