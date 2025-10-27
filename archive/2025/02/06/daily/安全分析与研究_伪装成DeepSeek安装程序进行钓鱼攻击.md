---
title: 伪装成DeepSeek安装程序进行钓鱼攻击
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490331&idx=1&sn=9582d925f419463dc13cc39156388b69&chksm=902fb433a7583d25fbf20191ca96276f243d7e4b57117536101c1e8427c7f090cda1e3199256&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-06
fetch_date: 2025-10-06T20:36:02.547600
---

# 伪装成DeepSeek安装程序进行钓鱼攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmWMzdBmAlVkjgGhdOoAicia6cNE3b12fQy0csibbFIjbGAxH6HBgeuKe6gSicMM66u14mt0icibl8GAKUYQ/0?wx_fmt=jpeg)

# 伪装成DeepSeek安装程序进行钓鱼攻击

原创

pandazhengzheng

安全分析与研究

‍

**‍安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

最近一段时间DeepSeek很火，黑客总是会利用一些热点进行钓鱼攻击，此前ChatGPT很火的时候，黑客组织伪装成ChatGPT客户端安装程序传播恶意软件，近日又发现黑客组织伪装成DeepSeek客户端安装程序进行钓鱼攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWMzdBmAlVkjgGhdOoAicia6coJqJ9o8JMEDx7lh2ShNdicGmzUxtLrzZcbXhOAM3w9xwkYrULSiaECqQ/640?wx_fmt=png)

样本分析

1.伪装成DeepSeek客户端安装程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWMzdBmAlVkjgGhdOoAicia6ceYxKeJjqkicicsAGz7TZeLeNIsiboDySgkakwUzwkGHERYZwk14mDwG3w/640?wx_fmt=png)

2.解析MSI安装程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWMzdBmAlVkjgGhdOoAicia6cZHV1ibB0HgxHAR9BRibcTDbpKpFKjJ0gwKz9Xs4fVBHEXaesEPib0iaJQw/640?wx_fmt=png)

3.加载执行恶意模块，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWMzdBmAlVkjgGhdOoAicia6cyB1c56QSsoo5rTP0mD7uyP565DX3zvL9503to2wvzsYIj2D63IoX6Q/640?wx_fmt=png)

4.从MSI解压缩释放出来的恶意模块，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWMzdBmAlVkjgGhdOoAicia6cH32Rl2167ibKxkNnoqMiaCrYeu1ZW41pftuhuuEqfQVnZiaoUibhIialnicQ/640?wx_fmt=png)

5.恶意模块编译时间为2025年1月23日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWMzdBmAlVkjgGhdOoAicia6cnzshy2EHuUZ2kicK3ywb3bTlpuU7QKP9eMgRKDAMJXiaaSqO9vC84u5w/640?wx_fmt=png)

6.在内存中加载GdiPlus模块，执行恶意代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWMzdBmAlVkjgGhdOoAicia6cJEkrwdTMELcVFfFHUgqE1uzzOfyn5cdjEPBqC8iaeBrbzOR2ua6joBw/640?wx_fmt=png)

7.模块导出函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWMzdBmAlVkjgGhdOoAicia6czm0bhFw11KVXsJN2X6ntERbZ5l9QC0THzcOIhk8JFGTjVNXYSwXeJA/640?wx_fmt=png)

8.模块入口函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWMzdBmAlVkjgGhdOoAicia6cdlwaotAKD3ib96HaHWzGZicJ49l4XnmMWibFibP0cBr0XJESicxK1kP0OGw/640?wx_fmt=png)

9.主线程函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWMzdBmAlVkjgGhdOoAicia6cOCNMy1UzabfxIfUum9Vo0fKkTzV7gP8aL5BUXR8401Rg3C068DzRAg/640?wx_fmt=png)

从代码特征分析，与此前笔者分析的BumbleBee恶意软件家族代码特征基本一致，解析出来的配置信息：

{'BumbleBee': {'RC4 key': ['NEW\_BLACK'], 'Botid': ['9090'], 'Port': ['443'], 'DGA seed': [13073764856797028147], 'Number DGA domains': ['300'], 'Domain length': ['10'], 'TLD': ['.click']}}

对这款恶意软件感兴趣的朋友自行分析研究，有不懂的地方再交流。

总结结尾

黑客组织利用各种恶意软件进行的各种攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

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