---
title: APT狩猎工具
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490311&idx=2&sn=411e5b869e7b4425b9b6ce4d386e170a&chksm=902fb42fa7583d3998df7212df242d3ded6c932acd3b4b8a1fc90df1dcdea22ff764a30d9c03&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-04
fetch_date: 2025-10-06T20:38:56.012815
---

# APT狩猎工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmVD7DuzQ8bG31SV1Ma9ls0QZPg9nRrx4FSRgiaDgFrduXv8nzicCebG22vKpQarGUAcHic3pJqRwgyPw/0?wx_fmt=jpeg)

# APT狩猎工具

原创

pandazhengzheng

安全分析与研究

‍‍

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

APT狩猎过程中经常需要使用一些工具来帮助我们提高效率，笔者今天给大家介绍一款开源的APT狩猎工具，可以根据自己的需求进行修改，以及添加自己的APT规则以帮助我们快速的进行APT狩猎。

工具地址：

https://github.com/ahmedkhlief/APT-Hunter

APT-Hunter是针对Windows事件日志的威胁搜寻工具，由Purple Team Mind开发，用于检测隐藏在海量Windows事件日志中的 APT攻击活动，以减少发现可疑活动的时间，而无需使用复杂的解决方案来解析和检测Windows事件日志中的攻击行为，如SIEM解决方案和日志收集器。

工具分享

1.下载工具，运行之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVD7DuzQ8bG31SV1Ma9ls0Qwg1RK5JL3vMJiawwTI0icmMYxpFtqVhtOUH6AYib4htguautyX2D6Fukg/640?wx_fmt=png)

2.需要提供相关的Windows事件日志，可以使用项目中提供的现有工具对Windows事件日志进行收集，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVD7DuzQ8bG31SV1Ma9ls0Qprgc35bax4ia9osJ4UC16gTgSuM9na92Our0K9JE89gDxOLaAAXbKQw/640?wx_fmt=png)

3.使用APT-Hunter分析收集到的Windows事件日志，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVD7DuzQ8bG31SV1Ma9ls0QlhbIcibwQysuKGib88Lm7ILZT4JNYfhGE8OPvLNalufbS65DHnlyR1sQ/640?wx_fmt=png)

4.检测结果，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVD7DuzQ8bG31SV1Ma9ls0QUpdhDBml84XwOyObflJUHex632NvJ8MIZxd6vIms76zb365X8ssCTw/640?wx_fmt=png)

5.结果会保存到相关的目录下面，可以将这些结果上传到其他工具平台进行更一步的分析，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVD7DuzQ8bG31SV1Ma9ls0QfxbticpYJlNfGR3oveH2tY2yE9uNF4Qq5rzMOna0VOeVJNOqzvS5rTA/640?wx_fmt=png)

如果对这款工具感兴趣的可以自行下载研究，添加更多的自己提取的相关APT规则，包含的检测规则样例，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVD7DuzQ8bG31SV1Ma9ls0QVDwNpu1lpmqVoWsiaqp3vfV3HNibBq14UePxjzMTIdQZ1UAQ1DRbXwcw/640?wx_fmt=png)

**友情提示：工具仅仅只是工具，工具能辅助我们进行分析，提升一些狩猎效率，更加深度的APT狩猎分析，还得靠经验丰富的安全研究人员进行手动分析狩猎。**

总结结尾

APT是全球企业面临的最大的安全威胁之一，需要安全厂商密切关注，未来APT组织还会持续不断的发起网络攻击活动，同时也会持续更新自己的攻击武器，开发新的恶意软件变种，研究各种新的攻击技术，使用新的攻击手法，进行更复杂的攻击活动，这将会不断增加安全威胁分析和情报人员分析溯源与应急响应的难度，安全研究人员需要不断提升自己的安全分析能力，更好的应对未来各种威胁挑战，安全对抗会持续升级，这是一个长期的过程。

如果对恶意软件分析感兴趣的，可以加入笔者的全球安全分析与研究专业群，一起共同分析和研究全球流行恶意软件家族。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXDIda3D6VvFWhqojST24E2rTRBJMYDfYowK8WcvBScfWlJiaYZ5elMdlrREG1LDVODxFQ0Eoy0YLQ/640?wx_fmt=jpeg)

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmW8qYF2seSKglWFKoJdassltn5V5IPUn3OGXsdD4v2nRPg8ZzFAicpXlmlwVmd9KTm4XPkRcXtBEKw/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

‍‍

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