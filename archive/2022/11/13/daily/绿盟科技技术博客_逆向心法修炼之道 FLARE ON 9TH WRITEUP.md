---
title: 逆向心法修炼之道 FLARE ON 9TH WRITEUP
url: http://blog.nsfocus.net/flare-on-9th-writeup/
source: 绿盟科技技术博客
date: 2022-11-13
fetch_date: 2025-10-03T22:38:06.035872
---

# 逆向心法修炼之道 FLARE ON 9TH WRITEUP

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 逆向心法修炼之道 FLARE ON 9TH WRITEUP

### 逆向心法修炼之道 FLARE ON 9TH WRITEUP

[2022-11-12](https://blog.nsfocus.net/flare-on-9th-writeup/ "逆向心法修炼之道 FLARE ON 9TH WRITEUP")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")

阅读： 1,809

**背景：**Mandiant 公司的 FLARE 团队会在每年九十月份举办一场侧重于 Windows 平台的逆向挑战赛 FlareOn CTF，旨在考验参赛选手在逆向分析领域上的技能水平。从 2014 年至今 FLARE 团队已经连续举办了 8 届比赛，而今年第 9 届 FlareOn Challenge 也是 Mandiant 被 Google 收购后所举办的第一场 FlareOn 挑战赛。尽管相比往年，本届比赛的开赛时间略微晚了一个月，但比赛时长和题目质量却并没有缩水。比赛时长仍旧是横跨 6 周，自北京时间 2022.10.01 08:00 开始到 2022.11.12 09:00 结束。比赛题目所涉及的内容与往年大同小异，基本涵盖了 C/C++、JavaScript、.Net、密码学、勒索、后门、网络流量等主题方向，另外还新增加了一个针对 68K Macintosh 架构的挑战题目。
对于大陆地区的小伙伴们来说，正好可以趁国庆假期在家刷刷题练练手，最后再在收到双十一快递包裹的喜悦中结束比赛。

## 一、Flaredle

### ![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image6-1-300x215.png)

第一题对输入内容的校验逻辑相对直白，通过与word.js中内置的一组硬编码值进行比对，若相符即验证通过：

## ![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image7-300x241.png)

## 二、Pixel Poker

### ![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image8-300x181.png)2.1 writeup

![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image9-300x248.png)

根据计算逻辑，只要保证像素点的x，y坐标满足以下条件即可触发flag显示：

* X == 0x52414C46 % 0x2E5
* Y == 0x6E4F2D45 % 0x281

选取坐标(x,y )=(95,313），点击即可得到flag：

![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image10-300x187.jpeg)

## 三、Magic 8 Ball

### ![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image11-300x155.png)3.1 writeup

解题步骤（前2步可调换顺序）：

1. Star typing your question处输入gimme flag pls?
2. 以L L U R U L D U L（即：左左上右上左下上左）顺序依次敲击键盘上的方向键
3. 回车确认

经分析，程序关键的校验逻辑存在于函数0x4024E0中，其主要完成以下校验操作：

1. 检查是否有用户输入，且输入内容是否与0x4021A1处硬编码字符串gimme flag pls?相同；

![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image12-300x110.png)

2. 用户是否按指定序列依次敲击了方向键；

![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image13-300x248.png)

若满足以上两个条件，程序随即进入flag解密分支：

![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image14-300x236.png)

## 四、darn\_mice

![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image15-300x155.png)

### 4.1 writeup

程序需提供1个命令行参数，该命令行参数将被用作以下用途：

1. 参与生成待执行的1字节shellcode（多组）
2. 参与解密计算

由于代码中会执行v2(v2)操作，而此地址上填充的是str[i]+v5[i]的内容，即只有1字节。为了保证函数正常执行，那么大概率这1字节是一个ret指令，对应十六进制0xC3：

![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image16-300x50.png)

按此逻辑编写脚本反推输入内容：

![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image17-300x49.png)

将see three, C3 C3 C3 C3 C3 C3 C3! XD作为命令行参数，再次运行程序即可得到flag内容：

![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image18-300x54.png)

## 五、T8

### ![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image19-300x211.png)5.1 writeup

入口处（0x4046E0）通过月相计算函数判断当前日期的月相值，经分析，程序只有在满月的日期运行时才能避免陷入长时间的休眠等待：

![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image20-300x117.png)

这里可通过修改系统日期来绕过sleep休眠。

接下来t8.exe作为网络请求客户端，向flare-on.com发起2次POS请求，其网络请求参数的构造方式如下：

|  |
| --- |
| srand(milliseconds since current hour) randnum = rand()  key = wchar(  md5sum.hexdigest(  wchar(“FO9″+randnumOfDecimal)))    POST1 => wchar(  b64\_encode(  rc4(key, wchar(“ahoy”))))    RESP1 => rc4(key, b64\_decode(resp))  .split(wchar(“,”))  .forEach(calcMoonPhase).map(phase => {  alphabet[phase]  })  .join()    POST2 => rc4(md5sum(flag), “sce”) |

而服务器则会将flag信息加密后放在第一次的响应应答中。根据该报文的构造方式，若要解密flag信息则需要知晓参与RC4加密的key参数。由于POST1和RESP1共用同一对rc4 key，且我们有双方的数据包流量，则可以通过枚举方式找出程序当时参与运算所使用的rc4 key。

根据分析结果，rc4 key的构造依赖于运行时的时间戳：

![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image21-300x94.png)

|  |
| --- |
| password = “FO9” + 自本小时开始所经过的毫秒数 key = md5sum(password) |

报文中的时间戳信息可以将时间范围缩小到16:14:36前后，即srand函数的seed范围介于1000\*(14\*60+36)~ 1000\*(14\*60+36)+0xFFFF之间：

![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image22.png)

因此可构造最多65535组key，对应的password形如：

|  |
| --- |
| FO99870 FO99873  FO99876  FO99879  FO99883  …snip… |

因为POST1的内容已知，即：y.d.N.8.B.X.q.1.6.R.E.=，则只需要逐个遍历找到正确的password即可。

编写测试脚本进行测试，当password为FO911950时，rc4(key, “ahoy”)的结果正好为ydN8BXq16RE=。

需注意，key的hexstream形式为：a5c6993299429aa7b900211d4a279848，而由于程序内部均使用wchar\_t类型来存储字符串等内容，故真正参与计算的key实际是：61003500630036003900390033003200390039003400320039006100610037006200390030003000320031003100640034006100320037003900380034003800。

使用该key，对RESP1内容进行解密，即可得到解密后的内容：

|  |
| --- |
| rc4(array(“61003500630036003900390033003200390039003400320039006100610037006200390030003000320031003100640034006100320037003900380034003800”), b64decode(“F1KFlZbNGuKQxrTD/ORwudM8S8kKiL5F906YlR8TKd8XrKPeDYZ0HouiBamyQf9/Ns7u3C2UEMLoCA0B8EuZp1FpwnedVjPSdZFjkieYqWzKA7up+LYe9B4dmAUM2lYkmBSqPJYT6nEg27n3X656MMOxNIHt0HsOD0d+”)) |

得到的内容再经wchar(“,”)分割（0x40426A）后生成14组\_SYSTEMTIME结构类型的存储数据（CyberChef [recipe](#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)RC4(%7B'option':'Hex','string':'61003500630036003900390033003200390039003400320039006100610037006200390030003000320031003100640034006100320037003900380034003800'%7D,'Latin1','Latin1')Fork('%5C%5Cx2c%5C%5Cx00','%5C%5Cn',false)To_Hex('Space',0)&input=VGRRZEJSYTFueEdVMDZkYkIyN0U3U1E3VEoyK2NkN3pzdExYUlFjTGJtaDJuVHZEbTFwNUlmVC9DdTBKeFNoazZ0SFFCUld3UGxvOXpBMWRJU2ZzbGtMZ0dEczQxV0sxMmliV0lmbHFMRTRZcTNPWUlFbkxOandWSHJqTDJVNEx1M21zK0hRYzRuZk1XWFBnY09IYjRmaG9razkzL0FKZDVHVHVDNXorNFlzbWdSaDFaOTB5aW5MQktCK2ZtR1V5YWdUNmdvbi9LSG1KZHZBT1E4bkFubDhLLzBYRys4ellRYlpSd2dZNnRIdnZwZnluOU9YQ3l1Y3Q1L2NPaThLV2dBTHZWSFFXYWZycDhxQi9KdFQrdDV6bW5lelFscDN6UEw0c2oyQ0pmY1VUSzVjb3BiWkN5SGV4VkQ0akpOK0xlekpFdHJEWFAxREpOZz09)）：

|  |
| --- |
| e5 07 09 00 03 00 0f 00 0d 00 25 00 03 00 62 02 dc 07 0a 00 06 00 0d 00 0d 00 25 00 09 00 2a 03  e1 07 0c 00 04 00 07 00 0d 00 25 00 24 00 e5 00  e0 07 05 00 05 00 06 00 0d 00 25 00 0b 00 26 00  e2 07 0a 00 01 00 08 00 0d 00 25 00 1f 00 45 03  e6 07 03 00 02 00 01 00 0d 00 25 00 32 00 da 00  de 07 07 00 02 00 16 00 0d 00 25 00 36 00 d1 02  de 07 05 00 03 00 0e 00 0d 00 25 00 01 00 e8 00  da 07 04 00 01 00 05 00 0d 00 25 00 3a 00 0b 00  dd 07 0a 00 04 00 03 00 0d 00 25 00 16 00 16 03  de 07 01 00 02 00 0e 00 0d 00 25 00 10 00 c9 00  dc 07 0c 00 01 00 0a 00 0d 00 25 00 30 00 0c 02  e6 07 02 00 01 00 1c 00 0d 00 25 00 22 00 4b 01  e6 07 09 00 05 00 09 00 0d 00 25 00 21 00 6d 01 |

分别计算这14组日期参数对应的月相值，以月相值为下标索引，从内置的一个字符串编码表中取相应的字符进行拼接：

![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image23-300x298.png)

即可得到flag前缀：i\_\*\*。

在使用正确key的情况下，t8在拿到第二次响应RESP2后最终会生成一个提示窗：

![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image24.png)

## 六、àla mode

### ![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image25-300x183.png)6.1 writeup

使用capa v4.0有注意到该文件具备mixed mode特征：

![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image26-300x39.png)

使用flass-floss v1.7.0发现存在xor解密后的\\.\pipe\FlareOn字符串：

|  |
| --- |
| floss.v1.7.0.exe -x -g –no-static-strings –no-stack-strings -q HowDoesThisWork.dll |

![](https://blog.nsfocus.net/wp-content/uploads/2022/11/image27-278x300.png)

其中一些函数操作及管道名称等跟dnSpy中看到的代码逻辑基本...