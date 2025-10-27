---
title: [SecData]-暗网流量公开数据集-1
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247490792&idx=1&sn=e5ff264f6b33a9af312953f95ff0edb4&chksm=fe2ee363c9596a75b27f680cd63b719285308c88cdc0e0ec803d8584a2c4245bd854520b3484&scene=58&subscene=0#rd
source: 安全学术圈
date: 2024-05-25
fetch_date: 2025-10-06T17:18:14.101916
---

# [SecData]-暗网流量公开数据集-1

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WEtk3TJf1kPf0yUibvpyatEIo7CXHwcgL7tXk2HolW7Xpco3lLiafBMuz6Sjawl0yicLWNxIzyRybvOw/0?wx_fmt=jpeg)

# [SecData]-暗网流量公开数据集-1

原创

zq@安全学术圈

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WFONa3Jbw26ePWfqhgEEjFnaAaTAEibib0bNeGvgPGmhGOsddcC9OiazI6RolOLNV4PRZJesMHdWicNZg/640?wx_fmt=jpeg&from=appmsg)

根据[专题笔记征稿](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247490782&idx=1&sn=dbb94ffe305ca2b3583882b5e589d946&chksm=fe2ee355c9596a43ad64a556b826ce82e593b5380e2e6ea5ddfb7b5bb8022f36be6f76641ffd&scene=21#wechat_redirect)，现将暗网已有的开源数据集梳理分享给大家：

### 1、CIC-Darknet2020

#### 1.1 数据介绍

CICDarknet2020数据集分为两层，在第一层生成普通流量和暗网流量，第二层为暗网流量，包括`音频流、视频流、Web浏览、即时通信、电子邮件、P2P、文件传输和VOIP`。该数据是`ISCXTor2016`和`ISCXVPN2016`数据集合并而来，结合了两者相应暗网类别中各自的VPN和Tor流量。第二层暗网流量的八种分类的流量源程序和详细信息如表1所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEtk3TJf1kPf0yUibvpyatEIbcpBcuKgAZtlvrH4HlXrXJCWANszYlJjZI2HibPnfdRzKEsF9GUomTw/640?wx_fmt=png&from=appmsg)

#### 1.2 数据下载

数据集链接：*https://www.unb.ca/cic/datasets/darknet2020.html*

基于上节的描述，图1展示了第一层数据集中正常流量和暗网流量的样本量对比情况，以及第二层数据集中各个类别样本量的占比情况。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEtk3TJf1kPf0yUibvpyatEIiax9DT4gkOwg4lUibfmb0wGpxHy0tRkY0y5ZG7wg8kE0ic459XQo5kV3g/640?wx_fmt=png&from=appmsg)

#### 1.3 论文及团队

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEtk3TJf1kPf0yUibvpyatEIbCl1NEOGxQ5vv5txZxohw67vTvbdoDkoNCnAeEk4bVGtngTDh4mh2Q/640?wx_fmt=png&from=appmsg)
> Arash Habibi Lashkari, Gurdip Kaur, and Abir Rahali, “DIDarknet: A Contemporary Approach to Detect and Characterize the Darknet Traffic using Deep Image Learning”, 10th International Conference on Communication and Network Security, Tokyo, Japan, November 2020.

`加拿大网络安全研究所(CIC)`位于弗雷德里克顿的新不伦瑞克大学，是一个综合性的多学科培训、研发和创业单位，吸收了社会科学、商业、计算机科学、工程、法律和科学领域的研究人员的专业知识。CIC关注的是安全数据的价值和意义，该研究所的网络安全科学项目侧重于为不断发展的数据密集型网络领域开发信息和网络安全解决方案，该计划的重点是开发和实施应对网络空间安全挑战的新方法，该研究解决了网络空间基础设施在恶意和不确定环境下确保其生存能力、可靠性和性能目标所面临的实际安全问题。

### 2、obfs4-mingan

#### 2.1 数据介绍

由9个子集组成：每个子集包含10000个实例，对应一个传输场景。对于每个子集，它包含两个部分：TCP数据和cell数据。TCP数据包含每个TCP报文的方向和时间信息，cell数据包含cell方向、时间戳和电路用途。

#### 2.2 数据下载

数据集链接：*https://pan.baidu.com/s/1kafKyemzmdEsyRnFlrV8NQ*，提取密码：*2rfw*

开源项目链接：*https://github.com/Meiqiw/obfs4-mingan/*

其中，clientdata是访问网站内容的流，cliententrp是访问隐藏服务内容的流，createfast是下载缓存文件的流。对于每个跟踪，在TCP文件夹中有一个记录TCP序列的txt文件，在日志文件夹中有一个同名的对应Tor日志文件。各个文件名的第一个数字是目标域的类型(0代表clientdata, 1代表clientp, 2代表createfast)。

```
dataset_Obfs4-MingAn
├── log
│   ├── client0_server0
│   ├── client0_server1
│   ├── client0_server2
│   ├── client1_server0
│   ├── client1_server1
│   ├── client1_server2
│   ├── client2_server0
│   ├── client2_server1
│   └── client2_server2
└── tcp
    ├── client0_server0
    ├── client0_server1
    ├── client0_server2
    ├── client1_server0
    ├── client1_server1
    ├── client1_server2
    ├── client2_server0
    ├── client2_server1
    └── client2_server2
```

#### 2.3 论文及团队

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEtk3TJf1kPf0yUibvpyatEIzPWSDTxhhRfh9cREF1Py1KqibQGa2lxpXJZE2biaTf2TrG9yVG8ymjHg/640?wx_fmt=png&from=appmsg)
> *Xuebin Wang, Zeyu Li, Wentao Huang, Meiqi Wang, Jinqiao Shi, Yanyan Yang. "Towards comprehensive analysis of tor hidden service access behavior identification under obfs4 scenario." Proceedings of the 2021 ACM International Conference on Intelligent Computing and its Emerging Applications. 2021.*

`北京邮电大学网络空间安全学院`网络安全与治理中心`时金桥教授团队`长期从事计算机网络与分布式系统、网络与信息安全相关项目科研工作，主要研究兴趣包括分布式网络系统、匿名通信与隐私保护、区块链网络、信息智能处理、大数据智能分析、网络测量技术等。

####

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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