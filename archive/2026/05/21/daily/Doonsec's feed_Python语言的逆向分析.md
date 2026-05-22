---
title: Python语言的逆向分析
url: https://mp.weixin.qq.com/s/cVrtYE6h2DBmgnDFwMTlmw
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:05:32.450950
---

# Python语言的逆向分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DupJg3UCeKKCD8K2BSloSUErA5qibhWI7iagRKpSrSVW9WYSHyhUnJyib9TJgEYk59SLxISV86KN2JIuHDTv1Xrrgibpu9icf48uYVZbUHCBssOQ/0?wx_fmt=jpeg)

# Python语言的逆向分析

无问社区
无问社区

白帽子社区团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Python是一种非常主流的脚本语言，它的运行原理是通过虚拟机进行解释执行的，因此这里将它和Java归为一类，它们的字节码文件在未经特殊处理或者保护的情况下都可以很轻松地进行反编译。

📌 一、Python 运行核心原理

       Python是常用工具之一，在《逆向工程技术、原理与CTF实践》的3.1.2节中进行了其开发环境的搭建，相信读者已经对Python的相关操作再熟悉不过了。

     Python的运行依靠python（Linux系统）或python.exe（Windows系统）可执行文件进行，这两个文件也被称为Python虚拟机，它会完成将源代码转换为Python字节码，再解释执行字节码的过程。

    接着介绍pyc文件。它是Python的字节码文件，类似于Java的.class文件，虽然看上去直接使用python xxx.py命令可以执行这个脚本，但是其实中间还是有一个转换的过程，即将.py文件编译成.pyc字节码文件（在使用本地库或者import相关文件的时候就能看到\_\_pycache\_\_文件夹中的文件就是这种文件）。

   当然，也可以显式地进行这个编译过程，例如编写一个简单的Python生成图片验证码的程序（使用pillow库—pip install pillow），代码如下：

```
from PIL import Image,ImageDraw,ImageFont,ImageFilterimport randomchar_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"def getChar():return  chr(random.randint(65,90))def getColor():return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))def getColor2():return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)) def get():#  *n代表生成几个随机字，与下面生成字符的n对应width = 60 * 6height = 60#  生成图片image = Image.new('RGB', (width, height), (255, 255, 255))# 创建Font对象font = ImageFont.truetype('simhei.ttf', 36)# 创建Draw对象draw = ImageDraw.Draw(image)# 填充每个像素for x in range(width):for y in range(height):draw.point((x, y), fill=getColor())# 输出文字listChar=[]for t in range(6):char=random.choice(char_list)listChar.append(char)draw.text((60 * t + 10, 10+random.randint(-20,20)), char, font=font, fill=getColor2())ans = ''.join(listChar).lower()# 模糊# image = image.filter(ImageFilter.BLUR)image.save('code.jpg', 'jpeg')print('ok')return ansif __name__ == '__main__':a = get()print(a)
```

   执行上面的程序可以获得一张6位数字字符验证码的图片。现在想要使用Python将其编译成pyc文件，需要使用python -m调用py\_compile模块来编译：

```
> python -m py_compile python验证码.py
```

    之后在\_\_pycache\_\_文件夹中就能找到“python验证码.cpython-311.pyc”文件，不同版本的Python标号可能会不一样，这时候使用cd命令进入\_\_pycache\_\_文件夹中，可以直接用python执行这个pyc文件并生成图片文件，如图1所示：

```
> python python验证码.cpython-311.pycokc3tn9o # 验证码的值
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/GURXOQt4KGC2eE1n533GW1mqnWrCUZEswwq0wMRbPtqyCZrrGyUc1XS1GuRLOTvXWVMP5fdM7v1X8B7XvGaI14jia2fxpgz0MiaPhuOBf3ZkA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=0)

   如果使用二进制编辑器打开这个pyc文件，看到的也是类似.class文件的字节码，如图2所示。

![图片](https://mmbiz.qpic.cn/mmbiz_png/GURXOQt4KGA3ECicqsDMBMUibDpZcC5xdDhPHYvP6VWsCnQB6TZlaG2cn40swnHfrILve7IRTF8QRz94U6uSegibqHI5sbXIedSLfSHJnhhz48/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1)

    对于低版本的pyc文件（Python 3.10以下），可以使用uncompyle6将pyc文件反编译成源代码（但是偶尔也会有错误）。

   下面介绍一种通用的方法，将pyc文件中的字节码反编译成相当于Python汇编的方式。使用Python内置的dis和marshal库来编写如下代码：

```
import marshal, disfp = open("1.pyc", 'rb')fp.seek(16) # 这里的16根据不同的版本来调节，跳过文件头的内容co = marshal.load(fp)dis.dis(co)
```

**注意：**marshal模块用于反序列化文件中的字节码，dis模块用于反编译相应的字节码。

   现在将之前的pyc文件和上面的脚本放在同一个目录下，然后将pyc文件的名称修改为1.pyc，使用Python运行上面的脚本，得到如下结果。

```
0 0 RESUME              01 2 LOAD_CONST         0 (0)4 LOAD_CONST         1 (('Image', 'ImageDraw', 'ImageFont', 'ImageFilter'))6 IMPORT_NAME             0 (PIL)8 IMPORT_FROM             1 (Image)10 STORE_NAME             1 (Image)12 IMPORT_FROM            2 (ImageDraw)… …
```

      这个结果中包括字节码对应的指令，以及它们在源文件中的行号（行号的存在是为了报错的时候进行提示）。

    在Uncompyle6工具不起作用的情况下，需要对反编译出的字节码进行静态分析。

### 📌二、PyInstaller打包成可执行文件

    《逆向工程技术、原理与CTF实践》的8.1.1节介绍了Python字节码的逆向分析方法，该字节码运行需要Python环境，如图3所示。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/GURXOQt4KGBCwiadwxglgt8z5s4v7NnXzCJ7eC9uEayuiboibHn8Gia4iaeT7DiaOFqib8cSgFTvanfvXU6ESn9FISgohibibhhVykBs4F6YIk0Pwe0U/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2)

   如果需要在一台没有安装Python的计算机上运行代码，就需要将Python的字节码和Python的运行环境打包到一起，或者将二者打包成一个完整的可执行文件，简单的示意如图4所示。

![图片](https://mmbiz.qpic.cn/mmbiz_png/GURXOQt4KGASiccWic3VwCUuA1DRpSlvN32zmnxFCUjbk7LibcA9ZpPeWFPmadl2KRXZSGCuvTYraZW2Xrg2yIaX0TEsToa1Ilkn51YXlbNylg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3)

      目前针对Windows操作系统最常用的一种方式是使用PyInstaller工具进行打包，这种方式打包以后生成的可执行文件有很大的体积，并且加载执行的速度也不快。

        PyInstaller的安装使用pip命令：

```
> pip install pyinstaller
```

    使用pyinstaller -h命令可以查看完整的使用说明。这里以8.2.1节生成验证码图片的脚本为例进行演示：

```
> pyinstaller -F python验证码.py
```

   -F选项代表将生成的内容打包为一个单独的EXE文件，不会出现其他依赖文件。在完成以后，当前目录下会生成一个build文件夹和一个dist文件夹，在dist文件夹中存放的就是打包好的可执行文件，如图5所示。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/GURXOQt4KGDATyoewPOPjboW8UkPA8phmLmJSibV6ksWRxAC7C7bhbblPGOPs767syIN9iaibSvVpD1YANpMfuXDs5fw4K9Se1NldM6PY7a2XM/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=4)

                            图5 PyInstaller打包完成

    直接双击或者使用命令行就可以运行这个可执行文件。

    如何对这个文件进行逆向分析呢？使用PyInstaller打包程序最明显的特征是它的图标，当然图标是可以被指定或者被换掉的。此外，使用IDA打开后存在的很多Py\_XXXX字符串，如图6所示。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/GURXOQt4KGCP0ibaFVAU20GGAK0PEIA0GicgCwJDPHbRMYiaTMc0N0icVcIJyicD1iaALfWBf5vIsF0uayvJbhpnibXtoWlCeibERl4S1f7piaNHA4RI/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=5)

                            图6 PyInstaller特征字符串

    针对PyInstaller工具打包程序，可以使用pyinstxtractor.py脚本进行解包。该工具的下载网址为https://github.com/extremecoders-re/pyinstxtractor。

```
@font-face{font-family:"Times New Roman";}@font-face{font-family:"宋体";}@font-face{font-family:"Calibri";}@font-face{font-family:"Courier New";}p.MsoNormal{mso-style-name:正文;mso-style-parent:"";margin:0pt;margin-bottom:.0001pt;text-indent:10.0000pt;mso-char-indent-count:2.0000;mso-layout-grid-align:none;punctuation-trim:leading;mso-pagination:none;text-align:justify;text-justify:inter-ideograph;line-height:15.3000pt;font-family:'Times New Roman';mso-fareast-font-family:宋体;font-size:10.5000pt;mso-font-kerning:10.5000pt;}p.15{mso-style-name:编程步骤;margin:0pt;margin-bottom:.0001pt;text-indent:11.5000pt;mso-char-indent-count:2.3000;mso-layout-grid-align:none;layout-grid-mode:char;punctuation-trim:leading;mso-pagination:none;text-align:justify;text-justify:inter-ideograph;mso-line-height-alt:12pt;background:rgb(217,217,217);font-family:'Courier New';mso-fareast-font-family:宋体;mso-bidi-font-family:'Times New Roman';font-size:9.0000pt;mso-font-kerning:10.5000pt;}span.msoIns{mso-style-type:export-only;mso-style-name:"";text-decoration:underline;text-underline:single;color:blue;}span.msoDel{mso-style-type:export-only;mso-style-name:"";text-decoration:line-through;color:red;}@page{mso-page-border-surround-header:no;	mso-page-border-surround-footer:no;}@page Section0{}div.Section0{page:Section0;}> pyinstxtractor.py python验证码.exe[+] Processing python验证码.exe[+] Pyinstaller version: 2.1+[+] Python version: 3.11[+] Length of package: 25258783 bytes[+] Found 93 files in CArchive[+] Beginning extraction...please standby[+] Possible entry point: pyiboot01_bootstrap.pyc[+] Possible entry point: pyi_rth_inspect.pyc[+] Possible entry point: pyi_rth_pkgres.pyc[+] Possible entry point: pyi_rth_multiprocessing.pyc[+] Possible entry point: pyi_rth_pkgutil.pyc[+] Possible entry point: python验证码.pyc[+] Found 509 files in PYZ archive[+] Successfully extracted pyinstaller archive: python验证码.exeYou can now use a python decompiler on the pyc files within the extracted directory
```

    最新的pyinstxtractor工具不需要自己补充pyc文件头，它会自动分析并完成解压过程，如图7所示。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/GURXOQt4KGA97xR6nOamibqBgjp8zTBmB9lWQicicPSaHmMuu5dcj5ZibDuJWpf19gCcwkVlNabFqQadamXHek1AH6hglduLgr1O5biaIibtUicJQU/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=6)

   至此就可以使用本文介绍的方式对Python字节码进行反编译和逆向。

### 🏆 活动奖品 ![图片](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5oNbJEjkCWSQbSjG9GzKzpqm8GWz5lT5abPSyWpzcUMfEUBT2vLRq4z8w5icDWmYh4g54d7ITHTlDJ09CibjXB2IXuA24BG1hib0icfDyqWuIn9Q/640?wx_fmt=svg&from=appmsg&wxfrom=5&tp=webp&wx_lazy=1#imgIndex=0)

**《逆向工程原理、技术与CTF实践》 × 3本**

![图片](https://mmbiz.qpic.cn/mmbiz_png/GURXOQt4KGADusqy6eTta7Mr4wCOMgzB4PYWbyN1...