from PIL import Image
class ImageToAscii:
    def __init__(self,im):
        self.im=Image.open(im)
    def Translator(self,r,g,b):
        strings='$$##@@**..  '#这里的字符从左到右为灰度最高到最低的，空格为白色
        gary = int(0.30 * r + 0.59 * g + 0.11 * b)#RGB转灰度计算公式
        unit=256/len(strings)
        return strings[int(gary/unit)]
    def output(self,weight=100,height=100):
        self.im=self.im.resize((weight, height))
        text=''
        for h in range(height):
            for w in range(weight):
                # getpixel()函数的作用是返回当前像素的rgb，因为图片不一定是RGB可能也会是RGBA所以要用分片处理
                text+=self.Translator(*self.im.getpixel((w, h))[:3])
            text+='\n'
        return text
x=ImageToAscii(input('Image name:'))
print(x.output())#可以自定输出字符画的长宽，默认为100*100


