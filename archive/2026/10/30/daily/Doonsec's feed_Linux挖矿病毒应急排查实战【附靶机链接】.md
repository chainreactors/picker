---
title: Linux挖矿病毒应急排查实战【附靶机链接】
url: https://mp.weixin.qq.com/s/c1lB-AInRvMeEUS1b8KSEA
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:42:54.369238
---

# Linux挖矿病毒应急排查实战【附靶机链接】

# Linux挖矿病毒应急排查实战【附靶机链接】

原创

内存余响
内存余响

内存余响

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

场景：一台对外提供会员业务的服务器，CPU使用率长时间90%以上，页面卡顿。

靶机账号密码【root免密】：ir/Ir@2024

靶机地址：https://pan.baidu.com/s/1Tp2oPsiGFcn9HbXRFF5KkQ?pwd=ram6 提取码: ram6

本题共两个flag

通过查看CPU使用情况得知名为“kdevtmpfsi”的程序高度使用

查看CPU使用情况：

```
top -c
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib9ustSW9LxuIpFeg3VXUV4lSsb4xMibT3ASWOiaPPdzPEpiaA5RgmxhJTGWJ00FtRC4iaiadWvGvR3fY9bQVfSl3k0vyeQrUW6IYlh4/640?wx_fmt=png&from=appmsg)

看外联：

```
ss -antp | grep 972
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib8XfBNgVY59rF54CYoVq0JDzbmDu0t6M362ZJiaRB1ibzGJMEGlvHs5ETNT8gozkGzmHTyaTvQV1d7vpJdFVKN7ibgqtqBjcUR4iao/640?wx_fmt=png&from=appmsg)

查看目录额外发现同一时间存在另一个可疑文件，还是隐藏的：.sysconfig.json

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibib8Vt9IFA7nSxSUthK5MO48UmreyibUjumdORCPOVCC6anmA1sbNkPgicuo66l4pd0QlSHct1DqQh6c8ZKiaaITeZGJDycNXOeCCc/640?wx_fmt=png&from=appmsg)

查看隐藏的配置文件：

```
cat /tmp/.sysconfig.json
```

矿池地址、钱包、线程数，一应俱全。到这里，进程、文件、外联三件事已经串起来了，可以确认是一起挖矿事件。

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDib8ZnXYiaYtwu0wg1AbBv44JBUzU4IBhXCQIZX3WzOOCjazIEUR0MSC34hVkO6SapVkwU2nB3roiahq4zYdjr0Cn8vicYdRm05zhE0/640?wx_fmt=png&from=appmsg)

像这种挖矿的一般有复活程序，不过也可以试试能不能杀掉；

尝试下，杀掉后马上就起来了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibibHNjtiafQ7h5YkMZkpQeTj8Q1tNFtTRsQQvjgQ7kOQz0mQUaic6n0NzCzwslwPqwDfReo7eSXantyb8cYujX5QBELeHGbyrdEHU/640?wx_fmt=png&from=appmsg)

找出他的守护者，一般是两个方向：定时任务、系统服务。

定时任务有一个复活程序，在程序注释里得到一个flag

```
crontab -lcat /usr/lib/.cache/.upd
```

flag{cr0n\_k33ps\_th3\_m1n3r\_al1ve}

代码分析：

复活函数，一分钟检查一次挖矿程序、配置文件、python挖矿进程及二进制挖矿程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib97OIlcjP6hb9iaKtQ4PR6Ht8pg446NdzVsCMLWp9vnY6ibICIjIFWgF7pWB2qvAicexhea6audGDWSOduibFaxhA6Nd1LSJy373Rs/640?wx_fmt=png&from=appmsg)

检查下系统服务，发现可疑服务：network-helper.service

```
systemctl list-unit-files --type=service --state=enabled
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibibwYyeTorUPsuUmGgJvXZBTZuO3w3D6rLYvWUFqxXSROmIOr5NQSANP7kbEPXS4cVddmj0PDo4aLVOqW6bE6nkia2bNvm9ZyJ2w/640?wx_fmt=png&from=appmsg)

查看服务详情，这个文件路径跟上面定时任务的一样，程序也是一分钟检查一次

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibic28HojBqrIBekQ7pHEibFhLFvicFS7roicKvOsuqATlicN71plR8WQ3uic3ewVZPXBbT9Ykkicjfh4yJ88IJKbicbQKaU0BjMsPj2uLU/640?wx_fmt=png&from=appmsg)

排查web日志发现是文件上传漏洞造成的，这里拿到第二个flag

flag{w3bsh3ll\_1s\_th3\_d00r}

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibicmvRIK6qLuQqy9IDLfPg3qCbharyUAIkqklt7fWCBUK7QdoRzJCOyeSkFXehedgqa4W5YU1FiaUiayX6hMGwNRGqJgRCYKm2WcM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibic0WLLzWqcJa7pq1GGibqLrnRuT4SA4L56pnlKUqic1jDVe5JYsFOvLu1ciahkNjnPHrMsBREic0BtaG05bL8oNpibYXnwQcnBqeZGA/640?wx_fmt=png&from=appmsg)

处置环节：

1、关掉服务

```
systemctl disable --now network-helper.servicerm -f /etc/systemd/system/network-helper.servicesystemctl daemon-reload
```

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibibvv3TRpP0t53UXutfhujDQ6F9UyLplxTTDexvTmQtj9LPmVFnUPW0juaBsFvVs7ibw9SL1kqkzodpPtkvxibn0Pbm3sYlAzh87M/640?wx_fmt=png&from=appmsg)

2、清理定时任务

```
crontab -r -u root
```

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibic5lzcamSUMd6KQWXAX2hevU7JhoLVzdJsjREOCQfibagUk6BBnyoxAEOrb3QLxGOYPibkV7uCtKLsSuUaO8JiaicKw9YKtsftug90/640?wx_fmt=png&from=appmsg)

3、删脚本与备份

```
rm -f /usr/lib/.cache/.upd /usr/lib/.cache/.kdev.bakrm -f /usr/lib/.cache/pool.py
```

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDib9J2JZib6MktBxfMPuqhuicz5bFrmGtcHmp2ASHOKnXeDNgkazJ3bo9HzIianP90Ja2GmXWOwhibBW478zf4icUeT1xZEuKfKeRUs1Y/640?wx_fmt=png&from=appmsg)

4、杀进程及删除落地文件；另外需要修复漏洞，因为是应急响应练习，所以不做这一步了，实际工作中一般由开发完成。

```
pkill -9 -x kdevtmpfsipkill -9 -f 'cache/pool.py'rm -f /tmp/kdevtmpfsi /tmp/.sysconfig.json
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib9dpglIexR6jS5KXr3y5RkGzfXofibQAibxutlZialslyh9s7rzb2weWcG2uwBmbEkUYgyrztOezs8km1vU4Ku2v5YGlRU44ic7QicE/640?wx_fmt=png&from=appmsg)

5、观察两分钟，看看还会不会再复活

```
sleep 120; pgrep -x kdevtmpfsi || echo clean
```

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibicaedymEDxr68ksTYkIpxKgia0AT7zIPsPoPL6j9OFicsJslXDdw4PeyjmnOkhNdibpqGqDyAgqkvZyJqK3A7tYFAO8yia8QWXB4ibY/640?wx_fmt=png&from=appmsg)

还原攻击链：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibicOTibDurYfpHAy9h3gA4SybRMKj3iasPlDDDkSWycGNujcgU6OLD9kWv0JPVr02kamibDtGQM023hkmgHdheNUiaGpY5TPSkHMGug/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibic4YfldibtqMVhOo0ez7bhNzzvcKGfFIlhFKFvlSN3VmFvNUVyibvMYJP3SR60w6t9GFkzGY4yrGNrvk2DZYQ5lbJQppuHpG1VfI/0?wx_fmt=png)

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