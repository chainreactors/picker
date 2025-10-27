---
title: WECHAT二维码闪退分析
url: https://www.secpulse.com/archives/199777.html
source: 安全脉搏
date: 2023-05-05
fetch_date: 2025-10-04T11:37:54.817335
---

# WECHAT二维码闪退分析

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# WECHAT二维码闪退分析

[代码审计](https://www.secpulse.com/archives/category/articles/code-audit)

[洞源实验室](https://www.secpulse.com/newpage/author?author_id=49765)

2023-05-04

31,018

##

**作者：hu1y40（洞源实验室，安全工程师）**

##

# 一、 **事件背景**

腾讯旗下的微信是一款社交通讯应用程序，由中国互联网巨头腾讯公司开发和运营。作为一款领先的社交应用，微信在全球范围内拥有大量的注册用户，且用户的活跃度极高。在微信中，用户可以通过扫描二维码来进行好友添加、进入公众号页面、加入群聊、进入小程序等。

2023年4月23日，用户在扫描或浏览某些畸形二维码时，会导致微信出现闪退等异常情况。

据了解，这种异常情况主要是由于畸形二维码造成的越界读取产生。

# 二、 **事件过程**

![图片1.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/图片1-1024x418.png "图片1-1024x418.png")

2023年4月23日晚上，部分微信用户反馈点开二维码图片会造成闪退。

![图片2.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/图片2-1024x718.png "图片2-1024x718.png")

2023年4月24日凌晨三点，GZTime发出了制造畸形二维码的python代码。

![图片3.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/图片3-1024x581.png "图片3-1024x581.png")

2023年4月24日下午两点，Konano发现微信开源的二维码识别引擎中的问题代码。

![图片4.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/图片4-1024x925.png "图片4-1024x925.png")

至文章编写的2023年4月26日为止，iOS端微信尚未更新修复此bug。

## 三、 **技术分析**

## 1. **二维码基础**

这里会介绍二维码创建的部分步骤，以用来分析后续的畸形二维码。

### 1.1 数据分析

QR码将一串文本编码成二进制位（1和0）。QR标准有四种文本编码模式：数字、字母数字混合、字节和汉字。每种模式将文本转换为不同的二进制位字符串，但每种编码方法都使用不同的方法将数据编码为最短的二进制位字符串。

### 1.2 数据编码

#### 1.2.1 纠错级别

二维码的四个纠错级别是：L、M、Q、H。

L表示最低纠错级别，能够修复约7%的数据码字错误；

M表示中等纠错级别，能够修复约15%的数据码字错误；

Q表示较高纠错级别，能够修复约25%的数据码字错误；

H表示最高纠错级别，能够修复约30%的数据码字错误。

#### 1.2.2 版本

二维码的版本指的是二维码矩阵中每一行和每一列的模块数，例如版本1的二维码矩阵大小是21x21（包括两个空白区域），版本2的大小是25x25，以此类推。版本越高，可以存储的信息也就越多。每个版本都有一个版本信息指示符来标识它的版本。（最多四十个版本）

![图片5.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/图片5-1024x310.png "图片5-1024x310.png")

#### 1.2.3 使用所选模式编码

• [Numeric Mode Encoding](https://www.thonky.com/qr-code-tutorial/numeric-mode-encoding)

• [Alphanumeric Mode Encoding](https://www.thonky.com/qr-code-tutorial/alphanumeric-mode-encoding)

• [Byte Mode Encoding](https://www.thonky.com/qr-code-tutorial/byte-mode-encoding)

• [Kanji Mode Encoding](https://www.thonky.com/qr-code-tutorial/kanji-mode-encoding)

####

#### 1.2.4 添加模式指示器

|  |  |
| --- | --- |
| Mode Name | Mode Indicator |
| Numeric Mode | 0001 |
| Alphanumeric Mode | 0010 |
| Byte Mode | 0100 |
| Kanji Mode | 1000 |
| ECI Mode | 0111 |

####

#### 1.2.5 添加字符计数指示器

后续字符有多少个，根据版本不同，这个指示器所占的位数不同。

![图片6.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/图片6-1024x757.png "图片6-1024x757.png")

####

#### 1.2.6 确定QR码需要的位数

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Version and EC Level | Total Number of Data Codewords for this Version and EC Level | EC Codewords Per Block | Number of Blocks in Group 1 | Number of Data Codewords in Each of Group 1's Blocks | Number of Blocks in Group 2 | Number of Data Codewords in Each of Group 2's Blocks | Total Data Codewords |
| 1-L | 19 | 7 | 1 | 19 |  |  | (19\*1) = 19 |
| 1-M | 16 | 10 | 1 | 16 |  |  | (16\*1) = 16 |
| 1-Q | 13 | 13 | 1 | 13 |  |  | (13\*1) = 13 |
| 1-H | 9 | 17 | 1 | 9 |  |  | (9\*1) = 9 |
| 2-L | 34 | 10 | 1 | 34 |  |  | (34\*1) = 34 |
| 2-M | 28 | 16 | 1 | 28 |  |  | (28\*1) = 28 |
| 2-Q | 22 | 22 | 1 | 22 |  |  | (22\*1) = 22 |
| 2-H | 16 | 28 | 1 | 16 |  |  | (16\*1) = 16 |
| ... | ... | ... | ... | ... | ... | ... | ... |

####

#### 1.2.7 添加终止符

添加1~4个0（bit）使得达到所要求的位数；添加了终止符后如果bit数不是8的倍数则继续添加0使得为8的倍数；如果最终的bit串仍然太短，则添加填充字符11101100 00010001。

##

## 2. **二维码生成**

### 2.1 代码

**import** qrcode
**from** qrcode.util **import** \*

**def** hack\_put(self, num, len):
 **if** num == 0:
     num = 2*# faker length of hack\_data*
 **for** i **in** range(len):
     self.put\_bit(((num >> (len - i - 1)) & 1) == 1)
qrcode.util.BitBuffer.put = hack\_put
qr = qrcode.QRCode(2, qrcode.constants.ERROR\_CORRECT\_Q, mask\_pattern=0)
data = "tested by InsBug".encode("utf-8")
data += b' ' \* (22-len(data)-3)
*# 22为2-Q的Total Number of Data Codewords for this Version and EC Level，-3是由于模式和长度指示器共占了24位，正好为3Byte。*
user\_data=QRData(data, MODE\_8BIT\_BYTE)
hack\_data=QRData(b'', MODE\_8BIT\_BYTE)
qr.add\_data(user\_data)
qr.add\_data(hack\_data)

img = qr.make\_image()
img.save("<filename>.png")

###

### 2.2 生成结果及扫描结果

![图片7.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/图片7.png "图片7.png")

该二维码通过上述代码生成。

![图片buchong.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/图片buchong-1024x709.png "图片buchong-1024x709.png")

QRazyBox的解析结果，发现hack\_data被解释成了一个Byte Mode指示器，并且长度为代码中设置的faker length，这时候如果再往后续读取数据便开始越界解析。

####

### 2.3 CRASH演示

![图片buchong2.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/图片buchong2.png "图片buchong2.png")

大部分用户反馈的微信点开二维码图片闪退的问题，在企业微信41.03.6008版本中同样存在。

###

## 3. **CRASH****分析**

### 3.1 源码分析

由于根源问题是wechat\_qrcode这个开源二维码识别引擎出现的问题。

 int nBytes = count;
 BitSource& bits(\*bits\_);
*// Don't crash trying to read more bits than we have available.*
 int available = bits.available();
*// try to repair count data if count data is invalid*
 **if** (count \* 8 > available) {
     count = (available + 7 / 8);
 }

 ArrayRef<char> bytes\_(count);
 char\* readBytes = &(\*bytes\_)[0];

以上为导致出现问题的解析代码。

（[代码文件链接](https://github.com/opencv/opencv_contrib/blob/960b3f685f39c0602b8a0dd35973a82ee72b7e3c/modules/wechat_qrcode/src/zxing/qrcode/decoder/decoded_bit_stream_parser.cpp#L202-L203)https://github.com/opencv/opencv\_contrib/blob/960b3f685f39c0602b8a0dd35973a82ee72b7e3c/modules/wechat\_qrcode/src/zxing/qrcode/decoder/decoded\_bit\_stream\_parser.cpp#L202-L203）

最终在填入一个有长度的空比特的时候，nByte不为0，available为0，执行到199行count被更新为0。

在执行到203行的时候，由于count为0，声明的是一个空数组，后续对其访问则是非法访问。其也对应了最后出错的EXCEPTION\_ACCESS\_VIOLATION。由于这一份引擎在腾讯系软件中广泛使用，所以除了微信，在企业微信、QQ中也同样会因为该二维码造成闪退。

####

### 3.2 逆向分析

![图片8.png](https://secpulseo...