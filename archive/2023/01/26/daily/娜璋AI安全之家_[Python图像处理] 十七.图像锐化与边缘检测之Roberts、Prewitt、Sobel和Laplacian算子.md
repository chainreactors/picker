---
title: [Python图像处理] 十七.图像锐化与边缘检测之Roberts、Prewitt、Sobel和Laplacian算子
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247497675&idx=1&sn=ab016cdd6e925d57d77143feb3e4811f&chksm=cfcf4706f8b8ce103fb5b52464c3abdf0380cb08bb2a6a183f6b5243fce472ba718b695ee1a6&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2023-01-26
fetch_date: 2025-10-04T04:52:49.730805
---

# [Python图像处理] 十七.图像锐化与边缘检测之Roberts、Prewitt、Sobel和Laplacian算子

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRMOOt04ZibhxJWj1sbLViawiaBY7vUoRNAL7y9eVExRTBvibEa6iazlIOfic9GzJn71o37zd4p7GR1Japibg/0?wx_fmt=jpeg)

# [Python图像处理] 十七.图像锐化与边缘检测之Roberts、Prewitt、Sobel和Laplacian算子

原创

eastmount

娜璋AI安全之家

该系列文章是讲解Python OpenCV图像处理知识，前期主要讲解图像入门、OpenCV基础用法，中期讲解图像处理的各种算法，包括图像锐化算子、图像增强技术、图像分割等，后期结合深度学习研究图像识别、图像分类应用。希望文章对您有所帮助，如果有不足之处，还请海涵~

**由于收集图像数据的器件或传输数图像的通道的存在一些质量缺陷，文物图像时间久远，或者受一些其他外界因素、动态不稳定抓取图像的影响，使得图像存在模糊和有噪声的情况，从而影响到图像识别工作的开展。这时需要开展图像锐化和边缘检测处理，加强原图像的高频部分，锐化突出图像的边缘细节，改善图像的对比度，使模糊的图像变得更清晰。**

**图像锐化和边缘提取技术可以消除图像中的噪声，提取图像信息中用来表征图像的一些变量，为图像识别提供基础。通常使用灰度差分法对图像的边缘、轮廓进行处理，将其凸显。本文分别采用Laplacian算子、Robert算子、Prewitt算子和Sobel算子进行图像锐化边缘处理实验。本文主要讲解灰度线性变换，基础性知识希望对您有所帮助。**

* 一.Roberts算子
* 二.Prewitt算子
* 三.Sobel算子
* 四.Laplacian算子
* 五.总结代码

该系列在github所有源代码：

* https://github.com/eastmountyxz/
  ImageProcessing-Python

前文回顾（下面的超链接可以点击喔）：

* [[Python图像处理] 一.图像处理基础知识及OpenCV入门函数](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247484670&idx=1&sn=c31b15b73f27a7ce44ae1350e7f708a2&chksm=cfccb433f8bb3d25c25f044caac29d358fe686602011d8e4cbdc504e3a587e756215ce051819&scene=21#wechat_redirect)
* [Python图像处理] 二.OpenCV+Numpy库读取与修改像素
* [[Python图像处理] 三.获取图像属性、兴趣ROI区域及通道处理](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247487743&idx=2&sn=5c0baea7ecabffa609fc4bbfc3824c40&chksm=cfcca032f8bb2924e729647d7a00602d639eeb1d9686641460c0752f9858947311b6309b2634&scene=21#wechat_redirect)
* [[Python图像处理] 四.图像平滑之均值滤波、方框滤波、高斯滤波、中值滤波及双边滤波](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247488101&idx=1&sn=f7529e05195e98cd5992e7b8c10a369c&chksm=cfcca2a8f8bb2bbee28a7aa11a6a34a72b539398fa61b6df54d829f058008f15efd4b84d5757&scene=21#wechat_redirect)
* [[Python图像处理] 五.图像融合、加法运算及图像类型转换](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247488186&idx=1&sn=a529c96d6fdd0e5d372265a0287609de&chksm=cfcca277f8bb2b619eeb43b61e762ee7579f4f60647c4dad8ef5f92a19596cf553e51c1666c2&scene=21#wechat_redirect)
* [[Python图像处理] 六.图像缩放、图像旋转、图像翻转与图像平移](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247489178&idx=1&sn=9476b932ce22f9039266cf14eb9d348b&chksm=cfcca657f8bb2f417b9eda13f58619cbde74eb679b3736b3567d9e588a4a1baa2816c2d6595b&scene=21#wechat_redirect)
* [[Python图像处理] 七.图像阈值化处理及民族服饰实验对比](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247489212&idx=1&sn=cbe30c912ef9eeb2da252b2c68beed04&chksm=cfcca671f8bb2f67923b82dbbaaf2fc4c1fe6d6b5146931d659f4ede2a91f42bc592ca17415e&scene=21#wechat_redirect)
* [[Python图像处理] 八.图像腐蚀与图像膨胀](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247491023&idx=1&sn=fb6e82528df9bfd4d024c3ffc658153f&chksm=cfccad02f8bb2414a3dfb14dfe92bccc2b76a9bfd81ea6a5750de5fe7dcf3cf8fab49562419a&scene=21#wechat_redirect)
* [[Python图像处理] 九.形态学之图像开运算、闭运算、梯度运算](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247491051&idx=1&sn=7769199b36d076552563c4a29e0fd26f&chksm=cfccad26f8bb243083d26b74120bfdef6d13cf14d08679d4bd311aa2d1717bec672bda8fe123&scene=21#wechat_redirect)
* [[Python图像处理] 十.形态学之图像顶帽运算和黑帽运算](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247491575&idx=1&sn=4d0345abcc85b6539ce8b3e86e011681&chksm=cfccaf3af8bb262c04cedf7b4764852d3874e83fe66050159969811fe43dc0fce237be9d6ae5&scene=21#wechat_redirect)
* [[Python图像处理] 十一.灰度直方图概念及OpenCV绘制直方图](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247496096&idx=1&sn=c40336e179a9fad5cb3b4d64c93f856e&chksm=cfcf416df8b8c87b2476bd157324958513a251c306d8a64686a889d5f493c7676662fc9d1b95&scene=21#wechat_redirect)
* [[Python图像处理] 十二.图像几何变换之图像仿射变换、图像透视变换和图像校正](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247496551&idx=1&sn=3c9006f26a1459ebc3b91eed29c45106&chksm=cfcf43aaf8b8cabcaf9e60791da6adfd31aa41c609cf3abc7009f093e6fbbdf9bb08f8bed79f&scene=21#wechat_redirect)
* [[Python图像处理] 十三.基于灰度三维图的图像顶帽运算和黑帽运算](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247496726&idx=1&sn=1e4fcfa9ca0cd26ae68dbbacf9473bbc&chksm=cfcf44dbf8b8cdcd3d4a2fef5b50363cc651e7e42e82ff258006166d798e5518d092d4062e90&scene=21#wechat_redirect)
* [[Python图像处理] 十四.基于OpenCV和像素处理的图像灰度化处理](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247497076&idx=1&sn=73cd0c587448cb77693cee5450df2363&chksm=cfcf45b9f8b8ccafe0ca77dcce6bf9eaee608eb9ccfc91f0480d980b440f002fcbe7cd34a9b3&scene=21#wechat_redirect)
* [[Python图像处理] 十五.图像的灰度线性变换](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247497363&idx=1&sn=a4a08b33f4f87e366e2a62543a3eec4a&chksm=cfcf465ef8b8cf484de7012042c58b4df0b312b8fdea656a58d6881a22fbc330711af9a71985&scene=21#wechat_redirect)
* [[Python图像处理] 十六.图像的灰度非线性变换之对数变换、伽马变换](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247497466&idx=1&sn=2cd697c35d8509297ddd6e412f59166a&chksm=cfcf4637f8b8cf219d948a16c70fcba47f336af4143416f86f43c3816c8e231642ed547f4d3f&scene=21#wechat_redirect)
* [Python图像处理] 十七.图像锐化与边缘检测之Roberts、Prewitt、Sobel和Laplacian算子

> 学Python近十年，认识了很多大佬和朋友，感恩。深知自己很菜，得拼命努力前行，编程也没有什么捷径，干就对了。希望未来能更透彻学习和撰写文章，同时非常感谢参考文献中的大佬们的文章和分享，共勉。
>
> - https://blog.csdn.net/eastmount

---

# 一.Roberts算子

Roberts算子又称为交叉微分算法，它是基于交叉差分的梯度算法，通过局部差分计算检测边缘线条。常用来处理具有陡峭的低噪声图像，当图像边缘接近于正45度或负45度时，该算法处理效果更理想。其缺点是对边缘的定位不太准确，提取的边缘线条较粗。

Roberts算子的模板分为水平方向和垂直方向，如公式（11.7）所示，从其模板可以看出，Roberts算子能较好的增强正负45度的图像边缘。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMOOt04ZibhxJWj1sbLViawiaBicwYYmt9Sx5YEgPdJKpzLbTVg5zsBL9f4fHJAhnlJGxTvJmdVHlicvaQ/640?wx_fmt=png)

详细计算公式如下所示：（PS-下图参考自己的书和论文）

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMOOt04ZibhxJWj1sbLViawiaBgkoLxVVSIDgg5REke0tP6jKE6e4esHwKjmMCgibn3iaUkia6Byt9qibricw/640?wx_fmt=png)

在Python中，Roberts算子主要通过Numpy定义模板，再调用OpenCV的filter2D()函数实现边缘提取。该函数主要是利用内核实现对图像的卷积运算，其函数原型如下所示：

dst = filter2D(src, ddepth, kernel[,
          dst[, anchor[, delta[, borderType]]]])

* src表示输入图像
* dst表示输出的边缘图，其大小和通道数与输入图像相同
* ddepth表示目标图像所需的深度
* kernel表示卷积核，一个单通道浮点型矩阵
* anchor表示内核的基准点，其默认值为（-1，-1），位于中心位置
* delta表示在储存目标图像前可选的添加到像素的值，默认值为0
* borderType表示边框模式

Python实现代码如下所示：

```
# -*- coding: utf-8 -*-import cv2  import numpy as np  import matplotlib.pyplot as plt #读取图像img = cv2.imread('lena.png')lenna_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#灰度化处理图像grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Roberts算子kernelx = np.array([[-1,0],[0,1]], dtype=int)kernely = np.array([[0,-1],[1,0]], dtype=int)x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)#转uint8 absX = cv2.convertScaleAbs(x)      absY = cv2.convertScaleAbs(y)    Roberts = cv2.addWeighted(absX,0.5,absY,0.5,0)
#用来正常显示中文标签plt.rcParams['font.sans-serif']=['SimHei']
#显示图形titles = [u'原始图像', u'Roberts算子']  images = [lenna_img, Roberts]  for i in xrange(2):     plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')     plt.title(titles[i])     plt.xticks([]),plt.yticks([])  plt.show()
```

运行结果如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMOOt04ZibhxJWj1sbLViawiaBODX7WOuzkcgmTFEppArfaic4rqZTkqmXo9uWC7rTTGetrtZffIWMcCQ/640?wx_fmt=png)

---

# 二.Prewitt算子

Prewitt是一种图像边缘检测的微分算子，其原理是利用特定区域内像素灰度值产生的差分实现边缘检测。由于Prewitt算子采用3*3模板对区域内的像素值进行计算，而Robert算子的模板为2*2，故Prewitt算子的边缘检测结果在水平方向和垂直方向均比Robert算子更加明显。Prewitt算子适合用来识别噪声较多、灰度渐变的图像，其计算公式如下所示。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMOOt04ZibhxJWj1sbLViawiaB3FSZUmZPQ4NPtj6gGwdkTLL9xRbsOgfDTicLSjNJxp6rlVo1nUUDgGg/640?wx_fmt=png)

在Python中，Prewitt算子的实现过程与Roberts算子比较相似。通过Numpy定义模板，再调用OpenCV的filter2D()函数实现对图像的卷积运算，最终通过convertScaleAbs()和addWeighted()函数实现边缘提取，代码如下所示：

```
# -*- coding: utf-8 -*-import cv2  import numpy as np  import matplotlib.pyplot as plt #读取图像img = cv2.imread('lena.png')lenna_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#灰度化处理图像grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Prewitt算子kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]],dtype=int)kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]],dtype=int)x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)#转uint8absX = cv2.convertScaleAbs(x)       absY = cv2.convertScaleAbs(y)    Prewitt = cv2.addWeighted(absX,0.5,absY,0.5,0)
#用来正常显示中文标签plt.rcParams['font.sans-serif']=['SimHei']
#显示图形titles = [u'原始图像', u'Prewitt算子']  images = [lenna_img, Prewitt]  for i in x...