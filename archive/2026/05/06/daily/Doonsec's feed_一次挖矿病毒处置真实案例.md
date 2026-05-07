---
title: 一次挖矿病毒处置真实案例
url: https://mp.weixin.qq.com/s/p2nH6aV8Ki-GJ3uhJcmOjg
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:26:20.804868
---

# 一次挖矿病毒处置真实案例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/wXKQNXqMicc9tVibmenylBn65IqXrUYB94u8ugibIYiaGaSOu3yEB3psftdkyA4ac9Qrl9p04zuV7ygxcCoecKKkOrRZMPdDUq0r0XEhjx4HnrE/0?wx_fmt=jpeg)

# 一次挖矿病毒处置真实案例

原创

安全攻防屋
安全攻防屋

安全攻防屋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

涉及到的敏感信息已打码

某能源企业运维人员在日常巡检中发现一台对外开放了6379端口的服务器CPU长时间占用率异常升高，影响正常业务，怀疑被感染了挖矿病毒。

发现Redis数据库攻击事件

步骤一：发现CPU高占用事件

进入创建的目标靶机中，执行【top】命令，发现内核CPU占比持续高达90%多，同时在进程列表中，并没有发现哪一个进程的CPU占比较高。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wXKQNXqMicc84LuOxY7uHSs7hVPRznOwjSHlugjFIUapqjlu9dLLFGPOMP08ERWaUNKc1cTGic60mguBSuQhxBsz3xnHrObc4ibgdPycLLYicE8/640?wx_fmt=png&from=appmsg)

#### 步骤二：发现ssh爆破攻击行为

查看审计登录日志【cat /var/log/auth.log】，发现在非常紧凑的时间内存在大量xx.xx.xx.xx该ip登录失败的记录，由此可知xx.xx.xx.xx是攻击者ip，并在3月3日这天对主机进行了ssh口令爆破。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wXKQNXqMicc8xEbhZnTXBOnvrvFCCdr9mHzzDc6SscVDeUCjaPCaibVQu8Dtd3L1TavibupXlQm7W4yK0DUNXEGDO1gtxYDvyvYKWYwrLMib8UM/640?wx_fmt=png&from=appmsg)

进一步追踪会发现攻击者并没有爆破成功，最后是在【09:18:29】该时间点通过私钥认证的方式进入的主机。

步骤三：发现数据库入侵事件

由该实验背景可知，主机对外开放了6379端口，对应redis服务，查看redis日志【cat /var/log/redis/redis-server.log | grep "xx.xx.xx.xx"】，发现攻击者在【03 Mar 08:18:38】该时间点第一次登录了redis数据库，排查会发现靶机的redis数据库存在未授权漏洞，无需密码即可登录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wXKQNXqMiccicRXkhkfQlkwU1DVKA0FzsAicvLlCtZucH0TgASUbtHdYDI0pwVyCxETlt1X2NKwIjVYmOTicYFmCOfcuZjib87wKdVCxPF94TOyw/640?wx_fmt=png&from=appmsg)

进一步分析redis日志， 会发现xx.xx.xx.xx:59054 与 Redis 实例建立了连接，执行了 SLAVE OF xx.xx.xx.xx:1234 命令，将当前服务器设置为 xx.xx.xx.xx:1234 的从服务器。

```
9463:S 03 Mar 08:41:33.448* SLAVE OF xx.xx.xx.xx:1234 enabled (user request from'id=6 addr=xx.xx.xx.xx:59054 fd=7 name=  age=0 idle=0 flags=N db=0 sub=0 psub=0 multi=-1 qbuf=0  qbuf-free=32768 obl=0 oll=0 omem=0 events=r cmd=slaveof')
```

成功连接后，Redis 启动主从同步过程，进行了全量同步，并从主服务器加载数据。

```
9463:S 03 Mar 08:41:35.923 * MASTER <-> SLAVE sync: receiving 44312 bytes from master
```

日志显示加载了名为 system 的 Redis 模块 ./exp.so

```
9463:S 03 Mar 08:41:37.924 * Module 'system' loaded from ./exp.so
```

完成复制并成功设置了新的主从复制 ID。

```
9463:M 03 Mar 08:41:37.925 * MASTER MODE enabled
```

由此推知攻击者通过redis未授权漏洞，利用主从复制方式拿到服务器权限。

![](https://mmbiz.qpic.cn/mmbiz_png/wXKQNXqMicc9Z2lE3uIL4LByQpDY2hULQR0Jbia0gbnonjhUaanbgOXwyU1E4t6Xb3SBqwtRkG5V73wHLfVm9EhYrrtCckI53LabEQAmZ1xdA/640?wx_fmt=png&from=appmsg)

任务二：分析CPU高占用事件

步骤一：排查动态劫持攻击

根据前面排查得到的信息，执行【top】命令时发现内核CPU占比持续高达90%多，但在进程列表中，并没有发现哪一个进程的CPU占比较高。

![](https://mmbiz.qpic.cn/mmbiz_png/wXKQNXqMicc9Pf3nkpwkM8cec8gTiaO4PIJiar62bDUicLdj0PueXfZJEaaibBg0aHo9ics0K8ayvpkiaUCacib9BC19k5p0WUcblWVHOQKk3BnsicME/640?wx_fmt=png&from=appmsg)

怀疑攻击者对恶意进程进行隐藏，排查是否存在动态劫持事件，检查【cat /etc/ld.so.preload】，发现其加载了【libuClibc\_cola.so】库文件。

![](https://mmbiz.qpic.cn/mmbiz_png/wXKQNXqMiccicC9OmBl2a18zblb3Nh80dAg5DhMAiaobrqK19A5wkjqUMPMICzxON8SfOiaZuYPzGcyxNq2uKduXIPbcaCZUCsKqmic1Soic8l6pw/640?wx_fmt=png&from=appmsg)

进一步查看该文件详细信息【stat /usr/local/lib/libuClibc\_cola.so】，发现其被修改时间和被攻击事件非常相近。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wXKQNXqMiccicfQcl72pyjbicJ1svAjMYflMJ9c4fNFI7le5qIJq1LkgNHc0YEqzN5feMkaVZvEdkByuibrLnwZvxDHWX9rjONrAQ9EDCp2px5I/640?wx_fmt=png&from=appmsg)

将libuClibc\_cola.so下载下来，放到在线云沙箱上分析，发现其为恶意文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wXKQNXqMicc92OAw6vfMiabhicDys6nDMm8FzPCKZnAbxESKZUbyOuzS5kZsE0hicXqlRSSz9MbfvX4ZhxYziad43ibZlAm4t2ObybiaAXJMY2h260/640?wx_fmt=png&from=appmsg)

步骤二：排查命令篡改攻击

注释或删除掉【/etc/ld.so.preload】文件中的内容，再次使用top命令查看进程情况，发现依然没有发现可疑进程，怀疑top命令有被修改过，【stat /usr/bin/top】查看命令的详细信息，发现该命令在被攻击附近的时间被修改过内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wXKQNXqMicc8vlcSVqT4GWLUrJJCPpsvL4U9oQm5IPPDYw6DMcjn5aaH5pKpGwqQKwMqm5f6xoNttu6zt4YwnZUqFiaAax4FTWmiaiaMribgum4A/640?wx_fmt=png&from=appmsg)

使用【file /usr/bin/top】查看发现是个文本文件。

![](https://mmbiz.qpic.cn/mmbiz_png/wXKQNXqMiccibm5Qtxy9qehlEYnLyox5zYfQjZrAIm8EXxKhxEQNHuct2rs7qdOkib1A56M2hiao8kPUnRXtEECtDRiaia5GZ16b43VNFj2ic9bRiaI/640?wx_fmt=png&from=appmsg)

查看其内容【cat  /usr/bin/top】，能够看到攻击者只是简单的将命令进行替换，将原始的top命令改成了【.top】，接着重新创建了top命令，运行原始的【.top】并将结果过滤dnsmasq关键词，达到隐藏恶意进程的目的。

```
#!/bin/bash/usr/bin/.top | grep -v "dnsmasq"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wXKQNXqMicc9T9V0hr657HxW3px25DUsJsAAarANibibSqDibdLPJg5e9tw2NOdVlwqGFgLjwPPL9VpZnOtiblKtK9qCJc9cUibKIJ81icwlibg2swA/640?wx_fmt=png&from=appmsg)

删除该top文件【rm /usr/bin/top】，并将.top改回成top【mv /usr/bin/.top /usr/bin/top】，再次执行top命令，发现恶意进程【dnsmasq】。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wXKQNXqMicc9yJuaJgxsBKHxoWGWuvDV1WEkdLwmCv0iaA5UGLfuDkxy59bJrtf7IrzYHyf8NGoGt5p7qSmnK96g2cuTBseTNHPLyrReNFkOw/640?wx_fmt=png&from=appmsg)

使用kill命令结束该恶意进程【kill -9 PID】，再次使用top命令，发现CPU恢复正常。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wXKQNXqMiccibWmJ9VDCHolKxNIKVsdYVyzA5us7BQnjcEXicK8Qb2cFhCRrzLFjbTbELYgot0ZB3mkVwXvIg6osHeTQDfsb7DT2OIHlvxnaCc/640?wx_fmt=png&from=appmsg)

步骤三：发现矿池IP

在使用kill命令结束掉恶意进程之后，重启服务器会发现依然存在CPU高占用现象，怀疑存在开启自启服务，排查在被攻击时间段是否有创建过恶意服务【find /etc/systemd/system/ /lib/systemd/system/ -type f -newermt "2025-03-03 00:00:00" ! -newermt "2025-03-05 00:00:00"】，【syscola.service】服务在被攻击时间段被创建。

![](https://mmbiz.qpic.cn/mmbiz_png/wXKQNXqMiccibZSUVrlwUggd3OoXg8xrmGAKEmhicfiaKgaoRAs5yHfEJj3All0W2NeGw2BLYcH3b4Mv1bXicFBWgouCTBYOcXfMeBicsfhlicwIeE/640?wx_fmt=png&from=appmsg)

进一步查看该服务内容，其执行的是【/usr/bin/xxx.sh】脚本。

![](https://mmbiz.qpic.cn/mmbiz_png/wXKQNXqMicc8Tn0LCbO6hchYZtCdDaN5AbrXl2KribPTV9XcSmDvzqLAIjcfa3XrNK8FbpfjaNkFKbh0atOuhVnOZ1JXoU9966R9kJTSCZWG8/640?wx_fmt=png&from=appmsg)

查看xxx.sh脚本内容【cat /usr/bin/xxx.sh】，在该脚本中发现了对前面排查到的恶意动态劫持文件的写入操作，已经脚本中执行恶意进程dnsmasq。

![](https://mmbiz.qpic.cn/mmbiz_png/wXKQNXqMicc8zyraoC8vPb6ibnKRD7IfgK33PMjjj9rMyHNFLS7ibqZfaq7ibCocnW5adZh33c6qNk5FcSEnBULHJaF8GNo4cS6zeJvq2Asq01o/640?wx_fmt=png&from=appmsg)

对脚本中的ip【80.211.206.105】进行分析，在线云沙箱【https://s.threatbook.com】中查询该ip，得到结论该ip为矿池ip，由此推知dnsmasq是攻击者上传的恶意挖矿程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wXKQNXqMiccicALWiaUMbl7gIbYpibSMpUtdU4XUaZqo7VxIhHiamae4chQNTgXv3AubTHhibs6jLr5kfFuoHzHUGvBWQww3t3N3bQXfdTywrxiaibI/640?wx_fmt=png&from=appmsg)

停止并删除该恶意服务，并删除恶意脚本。

####

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/b6UzoibqnYFGTf9IOyaKE1W4aWbrXDvYN14IOFPkoPiaiaWx9N5GCFOnAIyRUjEloN3YrksmjEOZJqzjCNyzYajXg/0?wx_fmt=png)

安全攻防屋

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/b6UzoibqnYFGTf9IOyaKE1W4aWbrXDvYN14IOFPkoPiaiaWx9N5GCFOnAIyRUjEloN3YrksmjEOZJqzjCNyzYajXg/0?wx_fmt=png)

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