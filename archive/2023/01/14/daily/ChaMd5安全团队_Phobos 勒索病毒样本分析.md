---
title: Phobos 勒索病毒样本分析
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247508165&idx=1&sn=6f22edb20bea46c4f390de872b44a05c&chksm=e89d881ddfea010bd04a2757f1c97141e6173b5234e4d8cac3c69764d79da414101c7caed8f9&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2023-01-14
fetch_date: 2025-10-04T03:53:32.545166
---

# Phobos 勒索病毒样本分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PUubqXlrzBQ9l6Wp4PHLLjFCEgkrEGyhOib4hVEiazSyVPZtib5Mdl9War1tzR3J5g5qBZ4ooPMqM1c9CpL7Wt8oA/0?wx_fmt=jpeg)

# Phobos 勒索病毒样本分析

原创

萌奇奇

ChaMd5安全团队

> > 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱
> >
> > admin@chamd5.org(带上简历和想加入的小组)

Phobos勒索病毒在近年来的热度不断上升，感染率不断提升，该病毒执行后会加密各种文件，并以zip.id[number].[hudsonL@cock.li].Devos命名。

下面对该家族样本进行分析，主要分析该病毒特征和行为。

勒索信：

```
!!!All of your files are encrypted!!!
To decrypt them send e-mail to this address: hudsonL@cock.li.
If you have not received a response within 24 hours, write to us at Jabber: helprecovery@gnu.gr
```

勒索图片：

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQ9l6Wp4PHLLjFCEgkrEGyh3gic7TZfn0BWN4rHlXzbfJdSiaYMkzibjtdA7m1TVb0X6N4yRvuHwRS4w/640?wx_fmt=png)

勒索图片

### 一、CRC32进行校验

该样本开局使用CRC32算法检测样本完整性，该算法在病毒中多次使用。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQ9l6Wp4PHLLjFCEgkrEGyhJu9tHDFS2YoTSGsoQa6kqNiaP8JEPBd9b6Dica19jHoIGicSz1UDw1uUQ/640?wx_fmt=png)

1.png

### 二、对样本进行提权操作

判断样本权限，若没有权限，则进行提权操作。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQ9l6Wp4PHLLjFCEgkrEGyhnrhmEUb5I0bwJa3A1dngq01U0euEMe9fuhKhibR79dOI18DR8ic0mUSw/640?wx_fmt=png)

提权

### 三、使用AES进行消息解密

使用AES对密钥进行解密后，根据节表进行读取。

节表一区间为0xC，依次为索引、偏移、长度。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQ9l6Wp4PHLLjFCEgkrEGyhAsrrN1Igdq1vS2g6wQWXlAzcmibgxHxd6BkSHTZ3baym2LZBS5FhdKw/640?wx_fmt=png)

aes1

资源解密密钥如下：

```
00AAF128  87 8F 65 5E 1B 30 7D E2 97 4B 8C 35 E4 46 B5 01  ..e^.0}â.K.5äFµ.
00AAF138  00 00 00 00 38 F1 F2 75 00 28 E3 00 18 F6 0F 01  ....8ñòu.(ã..ö..
```

资源解密向量如下：

```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

解密成功后部分：

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQ9l6Wp4PHLLjFCEgkrEGyhhJib0HTzDzicbbSarnYCehB3cnNotic7svvMzypvGpKGyboZ4rE4VVXcg/640?wx_fmt=png)

Untitled

### 四、网络通信

由于该样本未配置IP，故未产生网络连接

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQ9l6Wp4PHLLjFCEgkrEGyhZrzqiaI35ej5ngyaJBWRZJrrLHVqEMpkvqRicPmkdwZrQRob1W8UiaDMQ/640?wx_fmt=png)

网络.png

### 五、持久化驻留

在下列目录中对勒索病毒进行拷贝留存

C:\Users\86173\AppData\Local

C:\Users\86173\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup;

C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup

注册表中设置开机自启动项

Software\Microsoft\Windows\CurrentVersion\Run

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQ9l6Wp4PHLLjFCEgkrEGyhsdXusEU3GpmicUKQ3qnU5a5RJ8gNKvYNJZDplRkAHr1WHPuBu38TyVg/640?wx_fmt=png)

持久化驻留

### 六、创建线程终止占据文件的进程

拍摄进程快照，依次判断进程是否有文件占用。

尝试终止进程，尽可能加密更多文件。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQ9l6Wp4PHLLjFCEgkrEGyhM7w3Cic4UOVsXricKa7q7hyskbVIGpGKjrWIgiaiaE7xriccLLQl7Dm4Rhg/640?wx_fmt=png)

terminal

### 七、对文件进行勒索加密

1、通过随机数生成密钥，包括获取进程pid、tid、获取运行时间，获取本地时间等

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQ9l6Wp4PHLLjFCEgkrEGyhLeER9iafP78th6wPV3GuCGQ2mU7yzJrZNKs6gCxd9rUuDku9JStQHBQ/640?wx_fmt=png)

随机生成密钥

2、判断文件是否为空，若不为空，设置文件属性，根据文件大小加密文件。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQ9l6Wp4PHLLjFCEgkrEGyhxJNwHLq2nPegINJK9M8GIqW2jwqAlruhWESI3qBrnXz3BIUXyrLHYg/640?wx_fmt=png)

加密

总结：

样本通过采用CRC32校验+AES加解密进行制作勒索样本。

1. 进行CRC32校验
2. 判断是否提权，若未提权则进行提权的相关操作
3. AES解密相关消息，后面根据节表信息进行内容读取
4. 建立网络通信，发送连接请求
5. 持久化驻留，拷贝留存相关信息
6. 创建线程终止占据文件的进程
7. 随机创建加密密钥，对文件进行加密

由于使用作者公钥进行加密，故无私钥的情况下，AES暂时无法解密。

防范建议：

可以使用安装杀毒软件的方法进行防范。

该样本并未做太多对抗行为，特征明显，可以被传统杀软有效拦截。

C2：

33d32078ebe0c9429e405fdeb347dfb1ba5543e61d1179d13edffc7943b57640

招新小广告

ChaMd5 Venom 招收大佬入圈

新成立组IOT+工控+样本分析 长期招新

欢迎联系admin@chamd5.org

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBR8nk7RR7HefBINILy4PClwoEMzGCJovye9KIsEjCKwxlqcSFsGJSv3OtYIjmKpXzVyfzlqSicWwxQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRyftF8Oqhh2V8ib6wEgOiaCMdKBLfkLlHAvKibMgjerLzeXXxRmyI9VpjX7e37vjeW2scODia9KHGoqQ/0?wx_fmt=png)

ChaMd5安全团队

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRyftF8Oqhh2V8ib6wEgOiaCMdKBLfkLlHAvKibMgjerLzeXXxRmyI9VpjX7e37vjeW2scODia9KHGoqQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过