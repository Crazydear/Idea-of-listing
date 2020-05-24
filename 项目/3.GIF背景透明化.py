from PIL import Image
import os


class Gif_transparent:
    def __init__(self,gifFile):
        self.gifFileName = gifFile
        self.im = Image.open(self.gifFileName)    #使用Image模块的open()方法打开gif动态图像时，默认是第一帧
        self.imgs = []
        self.pngDir = self.gifFileName[:-4]
        if (not os.path.exists(self.pngDir)):
            os.mkdir(self.pngDir)  #创建存放每帧图片的文件夹

    def transparent_back(self,img):
        # 以第一个像素为准，相同色改为透明
        img = img.convert('RGBA')
        L, H = img.size
        for i in [0,L-1]:
            for j in [0,H-1]:
                color_0 = img.getpixel((i,j))
                for h in range(H):
                    for l in range(L):
                        dot = (l,h)
                        color_1 = img.getpixel(dot)
                        if abs(color_0[0]-color_1[0])<25 and \
                                abs(color_0[1]-color_1[1])<25 and \
                                abs(color_0[2]-color_1[2])<25:
                            color_1 = color_1[:-1] + (0,)
                            img.putpixel(dot,color_1)
        return img

    def con(self,path):
        img = Image.open(path)
        img = self.fangda(img)
        img = self.transparent_back(img)
        #img = self.suoxiao(img)
        img.save(path)

    def fangda(self,img):
        new_x, new_y = img.size
        new_x, new_y = new_x * 4 , new_y *4
        resized = img.resize((new_x, new_y), resample=Image.LANCZOS)
        # 修改原始数据
        img.thumbnail((new_x, new_y), resample=Image.LANCZOS)
        return resized
    def suoxiao(self,img):
        new_x, new_y = img.size
        new_x, new_y = int(new_x / 4), int(new_y / 4)
        img.resize((new_x, new_y), Image.ANTIALIAS)
        img.thumbnail((new_x, new_y), resample=Image.LANCZOS)
        return img
    def chuli(self):
        try:
            while True:
                #保存当前帧图片
                current = self.im.tell()
                print(current)
                # im = transparent_back(im)
                self.im.save(self.pngDir+'\\'+str(current)+'.png')
                self.con(self.pngDir+'\\'+str(current)+'.png')
                temp = Image.open(self.pngDir+'\\'+str(current)+'.png')
                self.imgs.append(temp)
                #获取下一帧图片
                self.im.seek(current+1)
        except EOFError:
            pass
        self.imgs[0].save('save_name.gif', save_all=True, append_images=self.imgs[1:],duration=40,transparency=0,loop=0,disposal=2)

gif = Gif_transparent("logo.gif")
gif.chuli()
