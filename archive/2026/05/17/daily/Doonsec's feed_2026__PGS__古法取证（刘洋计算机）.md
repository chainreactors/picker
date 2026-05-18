---
title: 2026\"PGS\"古法取证（刘洋计算机）
url: https://mp.weixin.qq.com/s/T8tw7TiG56MqPVr_r_cNqA
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:05:58.051147
---

# 2026\"PGS\"古法取证（刘洋计算机）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GOTHxR4ic5kiaLyNgzegFPicyryXwncZskLbGPkm70EMx46dKpHkC4liccyXJ7glnRUiaFIYFpicRubljS8wTMhSkbrp7Lx83YqnQqJoGFr7XXN2M/0?wx_fmt=jpeg)

# 2026"PGS"古法取证（刘洋计算机）

原创

zhoufish
zhoufish

ZhouFi网安分享

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前言

比赛时候着急，思路都乱的，没有做好，回来复现很多问题一想就通。

依旧古法复现，没有借助AI。但是比赛的时候还是得ai，因为动态分数，不用ai进不去决赛了。线上ai赋能，那以后线下呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icK836swLHcwv06xdgiciaePbs85RyQiceibNhgtGvGoRv2pOXX0wqtvNjPia8qANBibTzu2OjhFHprrgBPnzCicbP5HSBcwvhjlNicmabwqFTNa92NA/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/fticqTbZeagkEwWtWOzrNoz2MP5v1CEha9tLQehZS3EtOicnSQtoF7uN6XDAI4MNqK58yNReynK4yhyWArxS2vcmpMNWEy5ia8NSpxyICSS5GI/640?from=appmsg)

计算机取证

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icK836swLHcwv06xdgiciaePbs85RyQiceibNhgtGvGoRv2pOXX0wqtvNjPia8qANBibTzu2OjhFHprrgBPnzCicbP5HSBcwvhjlNicmabwqFTNa92NA/640?from=appmsg)

1、分析刘洋liuyang\_pc.E01检材，提取磁盘镜像SHA1值的前6位？

```
5bc418
```

是计算源盘的哈希值，不是镜像文件的。

![](https://mmbiz.qpic.cn/mmbiz_png/BPr6ErxsUmxp8ZSibAVTOmsLJoDVBWVWEKyhYnyt7bP239OKZwrrMiaMiaKmLCzsBYXLZnicIIvxrZFDiaqHXGFqvhTB2nucyHlqjT2GLdeFqHDY/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GOTHxR4ic5kjOmqSsNdJezMjYt1RbVvhibPuy0nQIE4rZ0ib6ib7ico8cmAhIg7GZUiaFj7SxBOPYwjrp4icOGL54240hR7g4Jrvia4BRib5QDf06zeA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kQhHzrOA0bsLhttiadLzbbtSteLLR5EL9zdPicZnULIJmoYNrwtQibMRAk8OExb1pibdYdqrP4uMnAxJUqllgqOsIpv578EExSd8KtBXiaCDU8LM/640?from=appmsg)

2、分析刘洋liuyang\_pc.E01检材，计算机系统Build版本为？

```
26100
```

取证工具直接看。

![](https://mmbiz.qpic.cn/mmbiz_png/BPr6ErxsUmxp8ZSibAVTOmsLJoDVBWVWEKyhYnyt7bP239OKZwrrMiaMiaKmLCzsBYXLZnicIIvxrZFDiaqHXGFqvhTB2nucyHlqjT2GLdeFqHDY/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOTHxR4ic5kgqnibPmW12ia7OAnib4GCct7zziaUvaTTTqJ8VoTNA9CoOV659zLyic1UkV5evC3eTQAoiaRPastAIEmCulscJ9fzC7an7NWjItSeU0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kQhHzrOA0bsLhttiadLzbbtSteLLR5EL9zdPicZnULIJmoYNrwtQibMRAk8OExb1pibdYdqrP4uMnAxJUqllgqOsIpv578EExSd8KtBXiaCDU8LM/640?from=appmsg)

3、分析刘洋liuyang\_pc.E01检材，计算机最后一次正常关机的时间为？UTC +0

```
2026-04-20 16:25:35
```

时间减去8小时。

![](https://mmbiz.qpic.cn/mmbiz_png/BPr6ErxsUmxp8ZSibAVTOmsLJoDVBWVWEKyhYnyt7bP239OKZwrrMiaMiaKmLCzsBYXLZnicIIvxrZFDiaqHXGFqvhTB2nucyHlqjT2GLdeFqHDY/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GOTHxR4ic5kiaMXE3hNwYcsr9vcGiaQQatA7fX332kyyibnJMfMEcWW2jpAs6IxCich0LAVNXYlR6sV6Snxib31YQdnRpib6qwR7ic5nQpGjMJC5OWM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kQhHzrOA0bsLhttiadLzbbtSteLLR5EL9zdPicZnULIJmoYNrwtQibMRAk8OExb1pibdYdqrP4uMnAxJUqllgqOsIpv578EExSd8KtBXiaCDU8LM/640?from=appmsg)

4、分析刘洋liuyang\_pc.E01检材，计算机网卡的MAC地址为？

```
00-50-56-30-26-1C
```

工具直接得到。

![](https://mmbiz.qpic.cn/mmbiz_png/BPr6ErxsUmxp8ZSibAVTOmsLJoDVBWVWEKyhYnyt7bP239OKZwrrMiaMiaKmLCzsBYXLZnicIIvxrZFDiaqHXGFqvhTB2nucyHlqjT2GLdeFqHDY/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GOTHxR4ic5kgt810t0hw7Wove1np2yjVFOIibA4zib06ibKBgGCxZn1EawzCNczicJkYst1j3D8Ty28l32u4ng4lzyqfB14p7Z9HP1xdMR7u8ldg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kQhHzrOA0bsLhttiadLzbbtSteLLR5EL9zdPicZnULIJmoYNrwtQibMRAk8OExb1pibdYdqrP4uMnAxJUqllgqOsIpv578EExSd8KtBXiaCDU8LM/640?from=appmsg)

5、分析刘洋liuyang\_pc.E01检材，分析机主是从哪里下载的typora？

```
蓝奏云
```

浏览器历史记录搜索，这是蓝奏云的网址。

![](https://mmbiz.qpic.cn/mmbiz_png/BPr6ErxsUmxp8ZSibAVTOmsLJoDVBWVWEKyhYnyt7bP239OKZwrrMiaMiaKmLCzsBYXLZnicIIvxrZFDiaqHXGFqvhTB2nucyHlqjT2GLdeFqHDY/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GOTHxR4ic5khRJJd7uwIZqmwHlFoeI0rWvTGQxMnfOqqj48Bfu0BZJu9ibVib8q8eoUEuRmVRic6ZAeRLfN8b3gVyhFufRW06uwqoevaMCGp4TI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kQhHzrOA0bsLhttiadLzbbtSteLLR5EL9zdPicZnULIJmoYNrwtQibMRAk8OExb1pibdYdqrP4uMnAxJUqllgqOsIpv578EExSd8KtBXiaCDU8LM/640?from=appmsg)

6、分析刘洋liuyang\_pc.E01检材，刘洋在2026-04-19 13:46:01（UTC +0）曾访问过百度云盘，请给云盘的打开密码？

```
48gy
```

时间在浏览器历史记录中加8就是：13+8=21。

搜索时间为：2026-04-19 21:46:01。

![](https://mmbiz.qpic.cn/mmbiz_png/BPr6ErxsUmxp8ZSibAVTOmsLJoDVBWVWEKyhYnyt7bP239OKZwrrMiaMiaKmLCzsBYXLZnicIIvxrZFDiaqHXGFqvhTB2nucyHlqjT2GLdeFqHDY/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOTHxR4ic5kjBnWl4F805Rj8xbvOnGcFAjTCACE5DT7Z54CtpBiclgbFAgicaCa387iaoiccsU57XY3nM5vOrgganatd2LRLxMb1ke19DKstSFlA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kQhHzrOA0bsLhttiadLzbbtSteLLR5EL9zdPicZnULIJmoYNrwtQibMRAk8OExb1pibdYdqrP4uMnAxJUqllgqOsIpv578EExSd8KtBXiaCDU8LM/640?from=appmsg)

7、分析刘洋liuyang\_pc.E01检材，请给出刘洋管理pve集群所用的端口号？

```
8006
```

浏览器历史记录中就有记录，或者是仿真上去查看服务。

![](https://mmbiz.qpic.cn/mmbiz_png/BPr6ErxsUmxp8ZSibAVTOmsLJoDVBWVWEKyhYnyt7bP239OKZwrrMiaMiaKmLCzsBYXLZnicIIvxrZFDiaqHXGFqvhTB2nucyHlqjT2GLdeFqHDY/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GOTHxR4ic5kh94BzL0nhmSBnGUTTwTQjT4oRiaNpNPibm6MNxFzkmD1dGHgdoOLtZO34Uj1ustA2zeic91ViaE8JDr6W4Pj03yjzVR3Gz8m7gqLY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kQhHzrOA0bsLhttiadLzbbtSteLLR5EL9zdPicZnULIJmoYNrwtQibMRAk8OExb1pibdYdqrP4uMnAxJUqllgqOsIpv578EExSd8KtBXiaCDU8LM/640?from=appmsg)

8、分析刘洋liuyang\_pc.E01检材，请给出刘洋登录理财网站所使用的密码？

```
admin123
```

浏览器中的保存密码，后面也可以去1Password中看到。

![](https://mmbiz.qpic.cn/mmbiz_png/BPr6ErxsUmxp8ZSibAVTOmsLJoDVBWVWEKyhYnyt7bP239OKZwrrMiaMiaKmLCzsBYXLZnicIIvxrZFDiaqHXGFqvhTB2nucyHlqjT2GLdeFqHDY/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOTHxR4ic5kiakPCOpou4WeK140WbibCJYdqiaicKwXTeq3vVEfhulr3yTsElovMhF7uibbYKnmibhvib1hCu24Bhqon0icsWINRFtgFzbXC67yzZibmI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kQhHzrOA0bsLhttiadLzbbtSteLLR5EL9zdPicZnULIJmoYNrwtQibMRAk8OExb1pibdYdqrP4uMnAxJUqllgqOsIpv578EExSd8KtBXiaCDU8LM/640?from=appmsg)

9、分析刘洋liuyang\_pc.E01检材，请给出理财网站的IP地址？

```
192.168.0.70
```

仿真打开记事本软件notepad++在host文件中可以查看到。

![](https://mmbiz.qpic.cn/mmbiz_png/BPr6ErxsUmxp8ZSibAVTOmsLJoDVBWVWEKyhYnyt7bP239OKZwrrMiaMiaKmLCzsBYXLZnicIIvxrZFDiaqHXGFqvhTB2nucyHlqjT2GLdeFqHDY/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOTHxR4ic5khDFsGBkXoSAPfF4rElzFuf67sZrYWOp6jqG2ZnZGIWUMEBOicrq75onp1ypYCgj3ZiajrgfrBPbbWnadFCb8Sk8FcL4hEYmZz4I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kQhHzrOA0bsLhttiadLzbbtSteLLR5EL9zdPicZnULIJmoYNrwtQibMRAk8OExb1pibdYdqrP4uMnAxJUqllgqOsIpv578EExSd8KtBXiaCDU8LM/640?from=appmsg)

10、分析刘洋liuyang\_pc.E01检材，请给出计算机内Bitlocker加密分区恢复密钥的前6位？

```
560615
```

使用工具，用内存密钥去解密Bitlocker。

> Elcomsoft Forensic Disk Decryptor

![](https://mmbiz.qpic.cn/mmbiz_png/BPr6ErxsUmxp8ZSibAVTOmsLJoDVBWVWEKyhYnyt7bP239OKZwrrMiaMiaKmLCzsBYXLZnicIIvxrZFDiaqHXGFqvhTB2nucyHlqjT2GLdeFqHDY/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GOTHxR4ic5kjknffMSicqVFAaia0HZRAgcFnnbibnHjN3H7pg6lgXdATeQHBAYHq7kKFyuG0mltQ4hf6Z5zAHmGETcjm01iasudWqYNJFMwNNQEM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kQhHzrOA0bsLhttiadLzbbtSteLLR5EL9zdPicZnULIJmoYNrwtQibMRAk8OExb1pibdYdqrP4uMnAxJUqllgqOsIpv578EExSd8KtBXiaCDU8LM/640?from=appmsg)

第二步

![](https://mmbiz.qpic.cn/mmbiz_png/BPr6ErxsUmxp8ZSibAVTOmsLJoDVBWVWEKyhYnyt7bP239OKZwrrMiaMiaKmLCzsBYXLZnicIIvxrZFDiaqHXGFqvhTB2nucyHlqjT2GLdeFqHDY/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GOTHxR4ic5kh3RLnkA6ZkMUjRky4NOMTlAicdmvqoicjh9F9q3JBpcl5GXiaLJaVS36LGZVWs5UzcfRyicdibtyWiaErWYEhrOticCpQpn3GE57zl5E/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kQhHzrOA0bsLhttiadLzbbtSteLLR5EL9zdPicZnULIJmoYNrwtQibMRAk8OExb1pibdYdqrP4uMnAxJUqllgqOsIpv578EExSd8KtBXiaCDU8LM/640?from=appmsg)

第三步

![](https://mmbiz.qpic.cn/mmbiz_png/BPr6ErxsUmxp8ZSibAVTOmsLJoDVBWVWEKyhYnyt7bP239OKZwrrMiaMiaKmLCzsBYXLZnicIIvxrZFDiaqHXGFqvhTB2nucyHlqjT2GLdeFqHDY/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GOTHxR4ic5kjRkESgtB5kFYQodHMic3OibOicPquTQ3hkckdVnNn2uolYhPAhXIWlwXUrp2Be6UhddAX3W4KWforodILOOviczzRcI5RnXXmSKRY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kQhHzrOA0bsLhttiadLzbbtSteLLR5EL9zdPicZnULIJmoYNrwtQibMRAk8OExb1pibdYdqrP4uMnAxJUqllgqOsIpv578EExSd8KtBXiaCDU8LM/640?...