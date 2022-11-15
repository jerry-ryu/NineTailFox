import os
from PIL import Image,ImageDraw,ImageFont


font_name = ['a피오피네모_0.ttf',
'a피오피네모OL.ttf',
'a피오피동글.ttf',
'a피오피동글OL.ttf',
'a피오피버블.ttf',
'a피오피버블OL.ttf',
'a피오피빙빙.ttf',
'a피오피빙빙MV.ttf',
'DXPOP-KSCpc-EUC-H.ttf',
'FB둥근붓POPL.ttf',
'fb둥근붓popm.TTF',
'fb매직popm.TTF',
'FB평붓POPM.ttf',
'THEDonguri.ttf'
]

font_path = '/opt/ml/NineTailFox/font/pop_font/'

save_path = '/opt/ml/NineTailFox/data'


# 이미지로 출력할 글자 및 폰트 지정 
text_kor = '가나다'
text_eng = 'abc'

font_list = [ImageFont.truetype(os.path.join(font_path, name), 40) for name in font_name]

# 이미지 사이즈 지정s
text_width = 100*3
text_height = 90

def create_font(font_list, font_name, text_width, text_height, save_path, text, country):
    
    for font, name in zip(font_list, font_name):
        # 이미지 객체 생성 (배경 검정)
        canvas = Image.new('RGB', (text_width, text_height), "white")
        
        # 가운데에 그리기 (폰트 색: 하양)
        draw = ImageDraw.Draw(canvas)
        w, h = font.getsize(text)
        draw.text(((text_width-w)/2.0,(text_height-h)/2.0), text, 'black', font)
        
        # png로 저장 및 출력해서 보기
        canvas.save(os.path.join(save_path ,name+"_"+ country+'.png'), "PNG")
        canvas.show()

create_font(font_list, font_name, text_width, text_height, save_path, text_kor, "kor")
create_font(font_list, font_name, text_width, text_height, save_path, text_eng, "en")