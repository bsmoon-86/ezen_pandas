import requests
from bs4 import BeautifulSoup as bs
import pytesseract
import os
import shutil


# class 선언
class MacroOlive:
    # 생성자 함수 : 클래스가 생성이 될때 최초의 한번만 실행이 되는 함수
    # 초기화 함수라고 표현하기도 한다. 
    # 클래스에서 사용할 변수에 데이터를 삽입
    def __init__(self, _url):
        # self는 자기자신 : 클래스를 생성 하는 변수의 주소가 self를 뜻한다.
        self.url = _url
        self.src_list = []

    # self.url를 requests를 사용하여 요청을 보내고
    # 응답 값을 기준으로 BeatifulSoup을 이용하여 이미지의 주소값들만 받아온다. 
    def return_img(self):
        # 주소로 요청
        response = requests.get(self.url)
        # 데이터의 변환
        soup = bs(response.text, 'html.parser')
        # contEditor 태그를 서치
        div_data = soup.find_all('div', attrs={
            'class' : 'contEditor'
        })[1]
        # div_data에서 이미지 태그들을 모두 로드 
        img_list = div_data.find_all('img')
        # src 속성들만 따로 추출하여 리스트에 대입
        src_list = []
        for img in img_list:
            data = img['src']
            src_list.append(data)

        self.src_list = src_list

        return src_list

    # 이미지 파일을 저장 
    def image_save(self, _path):
        # 해당하는 폴더가 존재하는가?
        if os.path.isdir(_path):
            pass
        else:
            os.mkdir(_path)

        # _path에 마지막이 '/'가 아닌 경우 '/' 추가
        if _path[-1] != '/':
            self.path = _path+'/'
        else:
            self.path = _path
        i = 1
        
        while True:
            file_name = 'olive'+str(i)+'.jpg'
            # 해당하는 경로에 파일이 존재하는가?
            if os.path.isfile(self.path+file_name):
                i+=1
            else:
                break

        for src in self.src_list:
            html_data = requests.get(src)
            file_name = 'olive'+str(i)+'.jpg'
            imageFile = open(
                os.path.join(
                    _path, 
                    file_name
                ), 
                'wb'
            )
            chunk_size = 100000000
            for chunk in html_data.iter_content(chunk_size):
                imageFile.write(chunk)
                imageFile.close()
            i += 1
            print(f'{file_name} 저장 완료')
        return '이미지 저장 완료'
    
    # 이미지에서 텍스트 추출
    def get_imagetext(self, _tx):
        file_list = os.listdir(self.path)
        result = open(_tx, 'w', encoding='utf-8')

        pytesseract.pytesseract.tesseract_cmd = r'c:/Program Files/tesseract-OCR/tesseract'

        for file in file_list:
            text = pytesseract.image_to_string(
                self.path + file, 
                lang = 'kor+eng', 
                config = '-c preserve_interword_spaces=1 --psm 4'
            )
            result.write(text)
        result.close()
        shutil.rmtree(self.path)
        return '텍스트 추출 완료'


    