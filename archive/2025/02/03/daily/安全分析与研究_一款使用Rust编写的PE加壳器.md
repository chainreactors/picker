---
title: 一款使用Rust编写的PE加壳器
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490280&idx=1&sn=27a8a52ec1103e01e0110d3cd8177b5d&chksm=902fb5c0a7583cd6218d677628b2525d44e71fe4a1a277e33d09f2eb178e9d0f3d1b7f16868b&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-03
fetch_date: 2025-10-06T20:35:36.942911
---

# 一款使用Rust编写的PE加壳器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXDIda3D6VvFWhqojST24E2Q1XgRN1GcEMGrLxKeEURYicohM1cDxP0fCXzRgmhEBn9aeQgnP4suGg/0?wx_fmt=jpeg)

# 一款使用Rust编写的PE加壳器

原创

pandazhengzheng

安全分析与研究

‍

**‍安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

今天给大家分享一款最新的使用Rust编写的PE加壳器，适用于X86和X64系统进程，工具的整个加壳流程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXDIda3D6VvFWhqojST24E2mVqYYzWMVORkqIdZGiaX3zZTMaicXdpOGjalhymh76kLQKNF9boNeWUA/640?wx_fmt=png)

项目地址：

https://github.com/Azr43lKn1ght/Rusty-PE-Packer

加壳器分析

1.使用加壳器对程序进行加壳处理，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXDIda3D6VvFWhqojST24E2ZzmS9Ric5s2ujV3K5gSyLATylOicsGoswPAbOviayvLjUM5mWibm4Evg5Q/640?wx_fmt=png)

2.运行加壳之后的程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXDIda3D6VvFWhqojST24E20B5TKorNYw0FVicdTm4URJASpIyrFAKXcriaer8K3l1eqDoBicek1NadA/640?wx_fmt=png)

3.将程序添加到加载器的资源数据当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXDIda3D6VvFWhqojST24E2u73PDk8uJZ6xyjjVWNiawGmylvzCyHIIdskJvNaoswJAkcNmd95LJbw/640?wx_fmt=png)

4.使用RC4算法对程序进行加密处理，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXDIda3D6VvFWhqojST24E23FVwYKT2fWYXAJqKXSqynyib8KFribYTBxWtQWdCLVsU57oCD64dqiccA/640?wx_fmt=png)

5.加载器通过检测系统内存大小、进程数据、CPU信息等，反沙箱分析，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXDIda3D6VvFWhqojST24E23I4XoYT3I2dESSlngyBwqu6zU4BE3gxAVr5zHM1zwo3YaXKZ3qsSDg/640?wx_fmt=png)

6.通过反调试函数以及检测调试器进程名反调试对抗，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXDIda3D6VvFWhqojST24E2HIY40lZoDncZ3nvIYMs29qJStJ4Nj7rdfHVFiaMqfibHfBCPf93pTQSw/640?wx_fmt=png)

7.VEH滥用，利用睡眠函数中的PageGaurd访问异常来混淆执行流程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXDIda3D6VvFWhqojST24E2plRlLIUDqZibbaJ4A6O4tCv3MTCgibDHhMDVMQTLejlFEvXqr5eSkVvQ/640?wx_fmt=png)

8.搜索ntdll库中的ROP操纵RIP以执行解壳操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXDIda3D6VvFWhqojST24E2oYtFwu8EVRHVOMicyhXoF8QAibibXgPN4icicPqicIwiazzCfe4Fyz19iaVrvA/640?wx_fmt=png)

9.加载器解密资源中的数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXDIda3D6VvFWhqojST24E2EgZGImxmCyXtWzntvV5G625HCTKxJVAjllXdWYdNCUafRmrrsN9wLQ/640?wx_fmt=png)

10.解密算法与之前加密算法和密钥一致，都是使用RC4算法，密钥可自定义，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXDIda3D6VvFWhqojST24E22dxxJHTTV79q5bwlY34IQxdyvX0Qq7yHEP9ibwv15aleFEmfWYU9UYw/640?wx_fmt=png)

11.以explorer.exe进程做为进程执行载体，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXDIda3D6VvFWhqojST24E2JlNYuqOXXVRoAIgklKWW6EHQctGp6rawcsOlOq873noKRWfZGbhacQ/640?wx_fmt=png)

12.explorer.exe进程中加载执行程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXDIda3D6VvFWhqojST24E2phLfeYgWkHPjRibnr0Wg1CZmg7OSMCaxWjEu3oIEcbTIn9Wmib2AvEuQ/640?wx_fmt=png)

加载执行过程中会进行重定位表和基地址的相关处理，这款PE加壳器就分析完了，对加壳以及免杀有兴趣的可以自行分析研究一下。

**友情提示：该工具仅被用于笔者自己做分析和研究使用，提取相关的样本特征，用于攻防对抗技术研究，不使用该工具进行任何非法操作！**

总结结尾

如果对恶意软件分析感兴趣的，可以加入笔者的全球安全分析与研究专业群，一起共同分析和研究全球流行恶意软件家族。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXDIda3D6VvFWhqojST24E2rTRBJMYDfYowK8WcvBScfWlJiaYZ5elMdlrREG1LDVODxFQ0Eoy0YLQ/640?wx_fmt=jpeg)

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmW8qYF2seSKglWFKoJdassltn5V5IPUn3OGXsdD4v2nRPg8ZzFAicpXlmlwVmd9KTm4XPkRcXtBEKw/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

‍

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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