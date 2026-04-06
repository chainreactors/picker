---
title: 流量分析实战——CTF真题练习
url: https://mp.weixin.qq.com/s/KJTBFcv9-1m_Dk3KIN_mcA
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:38:49.949341
---

# 流量分析实战——CTF真题练习

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/njicUbJnVlIy3lTh6yCHiaTNWXKQ2FxzOcNx2L3IgqvnfE02yvgmzDbPbhvxOJeU7icHbpBERARgtERcia0TOevMaznwHwn9o1x1iaFM0vojGZOc/0?wx_fmt=jpeg)

# 流量分析实战——CTF真题练习

原创

书中自有代码来
书中自有代码来

书中自有代码来

![]()

在小说阅读器中沉浸阅读

为了更好的理解和使用wireshark,让我们一起通过实际的题目来练习一下吧。

# 一、2019-工业信息安全技能大赛-山东站-简单流量分析

## 题目信息

不久前，运维人员在日常安全检查的时候发现现场某设备会不时向某不知名ip发出非正常的ICMP PING包。这引起了运维人员的注意，他在过滤出ICMP包分析并马上开始做应急处理很可能已被攻击的设备。运维人员到底发现了什么?flag形式为 flag{}

## 解题步骤

1. 下载附件，发现是一个压缩包，解压后是一个名为`fetus_pcap.pcap`的文件。
2. 我们使用wireshark打开文件进行分析，发现一共有230个分组，可以看到都是icmp包，是192.168.3.73和54.199.175.227之间的通信，可以猜测，运维人员管理的是192.168.3.73，而外网的设备是54.199.175.227。
3. 尝试搜索flag等关键词，搜索没有结果。
4. 发现题目时间不多了，于是上网搜索相关wp,找到一份：点击查看，居然是将icmp包的data长度转换为ascii码值拼接，这么奇特？
5. 参考wp编写python程序解码（当然也可以手动记录）：

```
#!/usr/bin/python
# -*- coding=utf -*-
import pyshark
import base64
L_flag = []
packets = pyshark.FileCapture('fetus_pcap.pcap')
for packet in packets:
    for pkt in packet:
        if pkt.layer_name == "icmp":
            ifint(pkt.type) != 0:
                L_flag.append(int(pkt.data_len))
c = len(L_flag)
for i inrange(0, c):
    L_flag[i] = chr(L_flag[i])
print(''.join(L_flag))
print(base64.b64decode(''.join(L_flag)))
```

> 注意使用老版本python运行，新版python可能出现错误，推荐3.6，使用pip安装pyshark库，使用apt安装tshark。

6. 结果如下：

```
Ojpcbm1vbmdvZGI6IToxNzg0MzowOjk5OTk5Ojc6OjpcbnVidW50dTokNiRMaEhSb21URSRNN0M0bjg0VWNGTEFHe3h4MmI4YV82bW02NGNfZnNvY2lldHl9Ojo=
b'::\\nmongodb:!:17843:0:99999:7:::\\nubuntu:$6$LhHRomTE$M7C4n84UcFLAG{xx2b8a_6mm64c_fsociety}::'
```

7. 得到flag,将flag按指定格式修改为`flag{xx2b8a_6mm64c_fsociety}`提交即可。

# 二、2020-之江杯-异常的流量分析

## 题目信息

工业网络中存在的异常，尝试通过分析PACP流量包，分析出流量数据中的异常点，并拿到FLAG，flag格式为 flag{}。

## 解题步骤

1. 下载附件，发现也是一个压缩包，解压得到`9.pcap`和一个`___MACOSX`的文件夹。
2. 使用wireshark打开文件，发现一共5799个分组，协议很杂，有arp、tcp等
3. 首先按长度排序，发现一个长度为37868的tcp数据流，打开发现是jpg的base64数据流。

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/njicUbJnVlIykDsp9GO0n8apoxYx4h5wANMFsgAkA11icPEal5Agouib4KgCTayHm9jhHhOYYvYcoKaUWHJ87kVrsM8RD7brcl8fWw6tg12oOY/640?wx_fmt=png&from=appmsg)

   解码看看：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/njicUbJnVlIyAgzw3yUyGicK4o7MQ1TcnblC8Xf8Cibl6oTYcm87puklLkiaoibXRLCEawrjeuRAjYQLaYkxScVicq8HTbl9XITibpFKiaCvxYuynh4/640?wx_fmt=jpeg&from=appmsg)

4. 输入flag即可，`flag{4eSyVERxvt70}`

# 三、2021-绿城杯-Misc-流量分析

## 题目信息

啥也没有

## 解题步骤

1. 依旧压缩包，解压后得到`1.pcapng`。
2. 使用wireshark打开发现有68607个分组，我的天！大部分协议是tcp和http,还有一些arp和dns。
3. 依旧搜索flag,不出所料没有，那按长度排吧，如此之多的包长度为1514,先看看吧。
4. 没什么头绪，是一些jsp文件，全部导出看看，是一个phpstudy搭建的服务器，运行的laravel，还有一个2345游戏中心？
5. 网上找wp,发现一篇：点击进入
6. 找到异常流量：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/njicUbJnVlIxwztfucSPV2ricxEEQfc5Z3aw4ykFXD2nbGP7q5T6VruSvAJsYmSQSk1rIfI5l3g995TCB5fAvWBmxldA4ibtdhwxLoxEes7wrs/640?wx_fmt=png&from=appmsg)

7. 按CVE -2021-3129的方法分析,得到flag。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/r57aCSG0dAvRdibKXBVSFWfFICJEzZvhogOeVscgwnjia8ZpicPMOOaE8t68cXrJE6oib5x8FjWNmd076icCj9nvWMw/0?wx_fmt=png)

书中自有代码来

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/r57aCSG0dAvRdibKXBVSFWfFICJEzZvhogOeVscgwnjia8ZpicPMOOaE8t68cXrJE6oib5x8FjWNmd076icCj9nvWMw/0?wx_fmt=png)

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