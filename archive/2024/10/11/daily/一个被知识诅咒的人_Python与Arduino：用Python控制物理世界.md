---
title: Python与Arduino：用Python控制物理世界
url: https://blog.csdn.net/nokiaguy/article/details/142708120
source: 一个被知识诅咒的人
date: 2024-10-11
fetch_date: 2025-10-06T18:46:20.102802
---

# Python与Arduino：用Python控制物理世界

# Python与Arduino：用Python控制物理世界

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
于 2024-10-10 10:00:00 发布
·
1.7k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

19

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

23
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#arduino](https://so.csdn.net/so/search/s.do?q=arduino&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

### 前言

在如今的物联网时代，硬件与软件的融合变得越来越重要。Arduino作为一种简单且功能强大的微控制器平台，常常用于快速原型设计和学习电子开发。而Python作为一门通用、简洁且功能丰富的编程语言，因其简单易用和丰富的库支持，受到许多开发者的喜爱。将这两者结合起来，我们就能通过Python控制Arduino来与物理世界进行交互。

本文将详细介绍如何使用Python与Arduino通信，重点讨论如何通过`pySerial`库控制Arduino上的硬件设备，比如LED灯、传感器等。我们会从环境设置、基本通信原理到具体项目实现，全方位展示Python与Arduino结合的强大潜力。

### 目录

1. 安装和配置开发环境
2. Arduino与Python通信的原理
3. 使用pySerial库与Arduino通信
4. 实战项目1：控制LED灯
5. 实战项目2：读取温度传感器数据
6. 实战项目3：通过Python实时控制Arduino上的电机
7. 扩展：Python与多设备通信
8. 总结与展望

---

### 1. 安装和配置开发环境

在开始编写代码之前，我们首先需要配置好开发环境。要实现Python与Arduino的通信，主要需要以下工具：

#### 1.1 必备工具

* **Arduino开发板**（如Arduino Uno）
* **Arduino IDE**：用于编写和上传Arduino代码
* **Python**：建议安装最新的Python 3.x版本
* **pySerial库**：Python用于串口通信的库
* **USB数据线**：用于连接Arduino与电脑

#### 1.2 Arduino IDE安装

Arduino IDE是用于编写、编译和上传Arduino代码的工具。可以通过以下步骤安装：

1. 访问[Arduino官网](https://www.arduino.cc/en/software)下载适用于你操作系统的Arduino IDE。
2. 安装完成后，使用USB数据线将Arduino开发板与电脑连接。
3. 打开Arduino IDE，选择`工具 > 板`并选择你使用的开发板（例如`Arduino Uno`）。
4. 在`工具 > 端口`中选择Arduino连接的串口。通常会显示为`COMX`（Windows）或`/dev/ttyACMX`（Linux和macOS）。

#### 1.3 安装Python与pySerial库

接下来，确保系统上安装了Python，可以通过命令行检查：

```
python --version
```

若未安装Python，请访问[Python官网](https://www.python.org/)进行安装。

安装完Python后，使用`pip`安装`pySerial`库：

```
pip install pyserial
```

`pySerial`库是Python与硬件设备通过串口通信的桥梁。它能让我们通过Python脚本轻松与Arduino设备进行数据传输和控制。

---

### 2. Arduino与Python通信的原理

Arduino和Python的通信主要依靠串口（Serial）通信实现。Arduino内置了串口通信的支持，开发者可以通过`Serial`库发送和接收数据。而在Python端，我们使用`pySerial`库来打开串口、发送数据和读取Arduino返回的信息。

串口通信是一种非常常见的通信协议，它允许通过一根线（即串口）在两个设备之间进行点对点通信。串口通信通常有以下几个重要参数：

* **波特率（Baud Rate）**：指定通信的速率，通常为9600或115200。发送端和接收端必须使用相同的波特率。
* **数据位（Data bits）**：每次发送的数据位数，一般为8位。
* **停止位（Stop bits）**：每次通信结束时的标志位。
* **奇偶校验（Parity）**：用于检测数据传输中的错误，一般不使用。

在本次项目中，我们使用9600的波特率进行通信，保持默认的数据位、停止位和无校验。

#### 通信框架

以下是Arduino与Python通信的基本框架：

1. **Arduino端**：

   * Arduino接收Python发送的指令，通过`Serial.read()`或`Serial.readString()`读取串口数据。
   * 根据接收到的指令，Arduino执行对应的操作（如点亮LED、读取传感器数据等）。
   * Arduino将执行结果通过串口返回给Python。
2. **Python端**：

   * Python打开串口，并通过`write()`函数发送控制指令。
   * Python通过`read()`或`readline()`函数读取Arduino返回的数据，并处理这些数据。

### 3. 使用pySerial库与Arduino通信

`pySerial`是一个用于串口通信的Python库。下面我们将通过具体代码展示如何使用`pySerial`与Arduino进行通信。

#### 3.1 打开串口

首先，使用`pySerial`打开与Arduino的串口通信。在Python中，我们需要指定串口号和波特率：

```
import serial
import time

# 打开串口，指定串口号和波特率
ser = serial.Serial('COM3', 9600, timeout=1)  # 根据实际端口号修改COM3
time.sleep(2)  # 等待Arduino初始化
```

在上面的代码中，我们通过`serial.Serial()`打开了指定的串口（如Windows上的`COM3`，macOS/Linux上的`/dev/ttyACM0`），并设置波特率为9600。`timeout=1`表示读取数据时的超时时间为1秒。

#### 3.2 发送和接收数据

接下来，使用`write()`发送数据，使用`readline()`读取Arduino返回的响应：

```
# 发送指令
ser.write(b'1')  # 发送字符'1'给Arduino

# 读取Arduino的响应
response = ser.readline().decode('utf-8'
```

![](https://csdnimg.cn/release/blogv2/dist/pc/img/lock.png)最低0.47元/天 解锁文章

200万优质内容无限畅学

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)

确定要放弃本次机会？

福利倒计时

*:*

*:*

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png)
立减 ¥

普通VIP年卡可用

[立即使用](https://mall.csdn.net/vip)

[![](https://profile-avatar.csdnimg.cn/2ccacbf1fc8347338ede60bde7fb2eec_nokiaguy.jpg!1)

蒙娜丽宁](https://unitymarvel.blog.csdn.net)

关注
关注

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like.png)

  19

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  23

  收藏

  觉得还不错?
  一键收藏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseWhite.png)
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/guideRedReward01.png)
  知道了

  [![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment.png)

  0](#commentBox)

  评论
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/share.png)
  分享

  复制链接

  分享到 QQ

  分享到新浪微博

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/share/icon-wechat.png)扫一扫
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/more.png)

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

专栏目录

参与评论
您还未登录，请先
登录
后发表或查看评论

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[AIGC撕裂劳动力市场：技术狂潮下，人类将走向乌托邦还是深渊？](https://unitymarvel.blog.csdn.net/article/details/145234235)

01-18
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2558

[随着人工智能（AI）技术的迅猛发展，尤其是生成式AI（AIGC），劳动力市场正经历前所未有的变革。从内容创作到自动化生产线，几乎每个行业都在经历一场技术的洗礼。然而，这场革命并不是全然的光明，它带来了深刻的社会变动，也引发了广泛的担忧和不安。我们不得不面对一个核心问题：AIGC将如何影响未来的工作？会让人类的大多数工作消失，还是会创造出全新的职业机会？](https://unitymarvel.blog.csdn.net/article/details/145234235)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【Python图形图像】《Python OpenCV从菜鸟到高手》——零基础进阶，开启图像处理与计算机视觉的大门！](https://unitymarvel.blog.csdn.net/article/details/143574491)

11-07
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2251

[《Python OpenCV从菜鸟到高手》是一本深入探讨Python与OpenCV技术的图像处理教程。从Python的基础知识到OpenCV的强大功能，这本书带领读者逐步掌握计算机视觉的核心技术。Python因其简洁和强大的库生态被广泛应用于数据分析、人工智能等领域，而OpenCV则是图像处理与计算机视觉的利器。本书通过循序渐进的方式，让读者从零基础到掌握高级图像处理技能，帮助你实现从初学者到高手的跃升。](https://unitymarvel.blog.csdn.net/article/details/143574491)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【奇妙的Python】解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

09-04
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3140

[《奇妙的Python——神奇代码漫游之旅》是一本面向实际应用的Python编程指南，涵盖文件操作、GUI设计、多媒体处理、自动化办公、加密解密等多个领域。由华为HDE专家李宁编写，通过丰富的实战案例，帮助读者在工作和项目中高效应用Python，提升编程技能。无论是新手还是有经验的开发者，这本书都将带你深入探索Python的无限可能，开启一段充满创意与实用性的编程之旅。](https://unitymarvel.blog.csdn.net/article/details/141889588)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[2025机器人产业大洗牌：新兴初创企业的技术革命与崛起之路](https://unitymarvel.blog.csdn.net/article/details/151067555)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1049

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创企业通过创新算法和低成本方案挑战传统巨头。本文剖析产业洗牌动因，包括AI融合、融资热潮和应用场景扩展，重点解析人形机器人等关键技术。通过ROS控制、A\*路径规划和PyTorch视觉识别等代码示例（附中文注释），展示初创企业的技术优势。文章预测Figure AI、Unitree等公司将引领消费级机器人市场，推动社会进入智能协作新时代。（150字）](https://unitymarvel.blog.csdn.net/article/details/151067555)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[Java应用容器化革命：Docker部署从入门到精通](https://unitymarvel.blog.csdn.net/article/details/151067543)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/...