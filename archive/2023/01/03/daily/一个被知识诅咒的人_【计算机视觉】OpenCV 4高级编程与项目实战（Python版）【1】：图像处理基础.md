---
title: 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【1】：图像处理基础
url: https://blog.csdn.net/nokiaguy/article/details/128525628
source: 一个被知识诅咒的人
date: 2023-01-03
fetch_date: 2025-10-04T02:54:37.586146
---

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【1】：图像处理基础

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【1】：图像处理基础

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2023-01-14 17:29:42 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量2.3k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

8

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
1

CC 4.0 BY-SA版权

分类专栏：
[OpenCV高级编程与项目实战（Python版）](https://blog.csdn.net/nokiaguy/category_12162950.html)
文章标签：
[计算机视觉](https://so.csdn.net/so/search/s.do?q=%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[opencv](https://so.csdn.net/so/search/s.do?q=opencv&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[图像处理](https://so.csdn.net/so/search/s.do?q=%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%86&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2023-01-02 22:09:18 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/128525628>

[![](https://i-blog.csdnimg.cn/blog_column_migrate/56256b7598fb005a8c32c420b606b60c.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

OpenCV高级编程与项目实战（Python版）
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12162950.html "OpenCV高级编程与项目实战（Python版）")

9 篇文章

订阅专栏

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)本文介绍了OpenCV4在Python中的应用，包括如何读取、显示和保存图像，以及获取图像属性。文章详细讲解了imread、imshow和imwrite函数的使用，并提到了处理png文件警告的方法和图像属性的获取。

视频课程：[《Python OpenCV 4高级编程与实战》](https://edu.csdn.net/course/detail/37684 "《Python OpenCV 4高级编程与实战》")

        本系列文章会深入讲解OpenCV 4（Python版）的核心技术，并提供了大量的实战案例。这是本系列文章的第1篇，主要讲解OpenCV处理图像的基本方法，主要包括读取图像、显示图像、保存图像和获取图像的属性。

**目录**

[1. OpenCV简介](#1.%20OpenCV%E7%AE%80%E4%BB%8B)

[2. OpenCV开发环境搭建](#2.%20OpenCV%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA%C2%A0)

[3. 读取图像](#3.%20%E8%AF%BB%E5%8F%96%E5%9B%BE%E5%83%8F)

[4. 读取png文件出现警告](#4.%20%E8%AF%BB%E5%8F%96png%E6%96%87%E4%BB%B6%E5%87%BA%E7%8E%B0%E8%AD%A6%E5%91%8A)

[5. 显示图像](#5.%20%E6%98%BE%E7%A4%BA%E5%9B%BE%E5%83%8F)

[6. 保存图像](#6.%20%E4%BF%9D%E5%AD%98%E5%9B%BE%E5%83%8F)

[7. 获取图像属性](#7.%20%E8%8E%B7%E5%8F%96%E5%9B%BE%E5%83%8F%E5%B1%9E%E6%80%A7)

---

### 1. OpenCV简介

        OpenCV是目前最流行的计算机视觉处理库之一，受到了计算机视觉领域众多研究人员的喜爱。计算机视觉是一门研究如何让机器“看”的科学，即用计算机来模拟人的视觉机理，用摄像头代替人眼对目标进行识别、跟踪和测量等，通过处理视觉信息获得更深层次的信息。例如，通过拍摄环绕建筑物一周的视频，利用三维重建技术重建建筑物三维模型；通过放置在车辆上方的摄像头拍摄前方场景，推断车辆能否顺利通过前方区域等决策信息。对于人类来说，通过视觉获取环境信息是一件非常容易的事情，因此有人会误认为实现计算机视觉是一件非常容易的事情。但事实不是这样的，因为计算机视觉是一个逆问题，通过观测到的信息恢复被观测物体或环境的信息，在这个过程中会缺失部分信息，造成信息不足，增加问题的复杂性。例如，当通过单个摄像头拍摄场景时，因为失去了距离信息，所以常会出现图像中“人比楼房高”的现象。因此，计算机视觉领域的研究还有很长的路要走。

        无论是图像处理还是计算机视觉，都需要在计算机中处理数据，因此研究人员不得不面对一个非常棘手的问题：将自己的研究成果通过代码输入计算机，进行仿真验证。而在这个过程中会重复编写基本的程序，这相当于为了制造一辆汽车，需要重新发明轮子。为了给所有研究人员提供“车轮”，英特尔(Intel)提出了开源计算机视觉库(Open Source Computer Vision Library，OpenCV)的概念，通过在计算机视觉库中包含图像处理与计算机视觉的通用算法，避免重复无用的工作。因此，OpenCV应运而生。OpenCV由一系列C语言函数和C++类构成，除支持使用C/C+语言进行开发之外，它还支持很多其他编程语言，如Java、Python、C#、Ruby等。OpenCV可以在Linux、Windows、macOS、Android、iOS等系统上运行。OpenCV的出现极大地方便了计算机视觉研究人员的算法验证，得到了众多研究者的喜爱。经过20多年的发展，OpenCV已经成为计算机视觉领域最重要的研究工具之一。图1是OpenCV的Logo。

![](https://i-blog.csdnimg.cn/blog_migrate/7e85d5835e8d105538ee69c8c6778d68.png)

图1

### 2. OpenCV开发环境搭建

本节会介绍如何搭建OpenCV-Python的开发环境。

OpenCV-Python目前最新版本是4.5.5.62。安装OpenCV-Python可以直接使用下面的命令安装：

```
pip install opencv-python
```

或者直接到下面的页面下载whl文件安装OpenCV-Python：

```
https://pypi.org/project/opencv-python/#files
```

下载页面如图2所示。

![](https://i-blog.csdnimg.cn/blog_migrate/d836d96b3d952121a214aabbab3601b8.png)

        在该页面包含了多个操作系统的OpenCV-Python版本，读者应该根据当前使用的操作系统下载相应的OpenCV-Python版本，假设读者使用的是Windows10，需要下载opencv\_python-4.5.5.62-cp36-abi3-win\_amd64.whl文件，然后使用下面的命令安装whl文件。

```
pip install opencv_python-4.5.5.62-cp36-abi3-win_amd64.whl
```

        安装完OpenCV-Python后，进入Python的REPL环境，执行import cv2，如果没有报错，说明OpenCV-Python已经安装成功，如图3所示。

![](https://i-blog.csdnimg.cn/blog_migrate/c36228cb05bcdc6a76556444b4ff6fa4.png)

图3

### 3. 读取图像

OpenCV提供了用于读取图像的imread函数，该函数的原型如下：

```
cv.imread( filename[,flags])->retval
```

参数说明：

* filename：待读取图像的文件名（绝对路径或相对路径）。
* flags：读取文件的类型，默认值是1，表示读取的是彩色图像（RGB格式），如果为0，表示灰度类型的图像。其中彩色图像也可以用cv2.IMREAD\_COLOR表示，灰度图像可以用cv2.IMREAD\_GRAYSCALE表示。
* retval：imread函数的返回值，一个由数字组成的矩阵，用于表示图像中的数据（颜色值），如果图像不存在或不可读，imread函数返回None。

注意：imread函数通过文件内容确定文件格式，而不是通过文件扩展名确定文件格式。例如，如果将png格式的图像文件book.png改名为book.jpg，imread函数仍然会按png格式读取book.jpg文件。

下面的例子使用imread函数读取了当前目录中的book.png文件，并输出返回结果。

```
import cv2
# 读取book.png文件
image = cv2.imread("images/book.png")
// 也可以使用下面的代码读取book.png文件
// image = cv2.imread("images/book.png", cv2.IMREAD_COLOR)
print(image) # 打印book.png中的数据（颜色值）
```

执行这段代码，会输出如图4所示的内容。

![](https://i-blog.csdnimg.cn/blog_migrate/110ef974ef0b80ee7bca4068b8ecdab4.png)

由于图像文件数据过大，所以只是输出了一部分数据，其余部分用省略号代替。

### 4. 读取png文件出现警告

在执行上一节代码时，尽管可以正常输出图像的数据，但还会输出如下的警告：

```
libpng warning: iCCP: known incorrect sRGB profile
```

         一般情况下，忽略这个警告并不影响OpenCV的正常工作，不过对于有强迫症的同学就太碍眼了，所以在这一节会将这个警告去掉。

       出现这个警告的原因是从libpng 1.6开始在检查ICC配置文件方面更为严格，所以可以删除png图像的iCCP块。下面先解释一下什么是ICC配置文件和iCCP块。

* **ICC****配置文件：**ICC是International Color Consortium（国际色彩联盟）的缩写。ICC配置文件是描述如何正确地将图像文件从一个颜色空间转换到另一个颜色空间的文件。ICC 配置文件有助于为图像获取正确的颜色。通过ICC配置文件，无论单个设备的色彩特性如何，都可以通过标准化的色彩空间正确显示色彩。
* **iCCP****块：**嵌入式ICC配置文件。在PLTE和IDAT之前。如果存在iCCP块，则不应该存在sRGB块。另外，PNG数据流最多应包含一个嵌入式配置文件。如果违反这些原则，在检测iCCP块时就可能会输出前面提到的警告。

        去除这个警告的方法也很简单，就是去除iCCP块即可，如果使用macOS、Linux或Unix非常简单，在终端直接使用convert命令即可：

```
convert book.png book1.png
```

        执行这行命令，可以去除book.png文件中的iCCP块，并生成新的book1.png文件，再使用上一节的代码读取book1.png文件，就不会输出这个警告了。

        如果使用的是Windows，可以通过第三方图像编辑工具去除iCCP块，如跨平台的ImageMagick（https://imagemagick.org），安装完ImageMagick后，在终端执行下面的命令即可：

```
magick convert book.png book1.png
```

### 5. 显示图像

        将图像以矩阵形式输出是给分析程序用的，如果要想给人展示图像，就应该将图像显示出来，而不是输出密密麻麻的数字。为此，OpenCV提供了imshow函数用来显示图像。imshow函数会弹出一个窗口，并在窗口中显示图像。

        如果只使用imshow函数显示窗口，那么这个窗口闪一下就退出了，所以还需要使用waitKey函数让阻止窗口提出。waitKey函数的作用是等待任意一个按键按下，如果有按键按下，waitKey函数就会执行完毕，继续执行下面的代码，否则waitKey函数将一直处于等待状态。

        尽管Python程序执行完后会释放所有资源，但一个好的习惯是在程序执行完后，主动释放资源，如果使用imshow函数打开一个窗口，那么这个窗口就是资源，所以在程序执行完毕后，需要使用destroyAllWindows方法释放通过imShow函数创建的窗口，当然，如果还有其他窗口，也会一起释放。

下面看一下这几个函数的原型：

(1) imshow函数

```
cv.imshow( winname, mat)-> None
```

参数说明：

* winname：显示图像的窗口名称。
* mat：要显示的图像的矩阵数据，也就是imread函数返回的值。

imshow函数的返回值是None。

(2) waitKey函数

```
cv.waitKey([delay])-> retval
```

参数说明：

* delay：可选参数，表示用户等待按下键盘上按键的时间，单位是毫秒（ms）。如果超过了这个时间，用户仍然未按下键盘上的任何键，那么waitKey函数将自动结束。如果不指定delay参数，默认值是0，表示无限等待，也就是说，只要用户不按下键盘上的键，waitKey函数将一直处于阻塞状态。
* retval：waitKey函数的返回值。如果用户按下键盘上的按键，那么waitKey函数返回按键对应的ASCII码，例如，用户按下了a键，那么waitKey函数的返回值是97。如果在等待delay毫秒后，用户仍然未按下任何按键，那么waitKey函数自动结束运行，并返回-1。

(3) destroyAllWindows函数

```
cv.destroyAllWindows()-> None
```

        destroyAllWindows函数没有参数，返回值是None。该函数用于销毁所有正在显示图像的窗口。

        下面的代码使用imread函数读取了当前目录中的book.png文件，并通过imshow函数显示book.png，最后通过waitKey函数输出用户按键的ASCII值。

```
import cv2
image = cv2.imread("images/book.png")  	# 读取book.png文件
cv2.imshow("book", image)  				# 在名为book的窗口中显示book.png
print(cv2.waitKey()) 		 			# 窗口将一直显示图像，按任意键关闭窗口，并输出按键值
cv2.destroyAllWindows()  				# 销毁所有窗口
```

执行这段代码，会弹出如图5所示的窗口。

![](https://i-blog.csdnimg.cn/blog_migrate/67ecd10d774873e52e0a812f647b3d59.png)

阅读这段代码应注意如下几点：

(1) 显示图像的窗口名称不能是中文，例如，将“book”改成“我写的书”，再运行程序，窗口左上角的标题就会呈现乱码，如图6所示。

(2) imshow函数的作用只是显示窗口，但如果整个Python程序都退出了，那么imshow函数显示的窗口也会自动关闭，所以要在imshow函数后面使用waitKey函数阻止Python程序退出。

![](https://i-blog.csdnimg.cn/blog_migrate/56cf988cae320bc70e5adf340b6056d9.png)

        如果想将彩色图像变成灰度图像，只需要将imread函数的...