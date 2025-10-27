---
title: Water Hydra APT组织最新攻击链攻击样本详细分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489036&idx=1&sn=62b9023cc59d7e12aaeaa52b35df216c&chksm=902fb924a7583032918cb468c2547efbbe92e3b1dfa529c5f8d6ec304f6c0f991b7fd5bb554e&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-10-13
fetch_date: 2025-10-06T18:50:39.662647
---

# Water Hydra APT组织最新攻击链攻击样本详细分析

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74WkyMDl62MznUSWIwWNK39tq9tLaT1nyRZjyJt1ubnRMmJWJrd48dAw/0?wx_fmt=jpeg)

# Water Hydra APT组织最新攻击链攻击样本详细分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/14711

先知社区 作者：熊猫正正

Water Hydra APT组织于2021年首次被公开曝光，它主要针对金融行业进行攻击活动，对全球的银行、加密货币平台、外汇和股票交易平台、赌博网站和赌场发起攻击，笔者针对该APT组织的最新的攻击链样本进行了详细分析，供大家参考学习。

详细分析

1.初始样本为一个URL链接，点击URL链接之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR749cboFmq8Id2uKA3GUDkiaBkWoUaLvAYM0HAv35BouVhrqlkO0YaicmMg/640?wx_fmt=png)

2.查看网页内容，从远程服务器上下载相关的恶意文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74M3bQItEib2LAa5tH2U0Vac2Rng4bq4ze2W4joxW9NwrF7NmjqicJ6I3w/640?wx_fmt=png)

3.下载的恶意文件为一个PDF图标的LNK文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74ibnp2NurTuRcxEzSbwHQSP5XsCayqmFiagbvEMqws6OHicKeIZJaTUoWw/640?wx_fmt=png)

4.该LNK文件包含的CMD命令，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74o2hOab41RThph2KdRa8pTyfmaDvYGKpn72icMOIvqWekQZ2desKgJsg/640?wx_fmt=png)

5.执行远程服务器上的BAT脚本，从远程服务器下载MSI恶意安装程序到临时目录，并启动MSI恶意安装程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74hvNJSgFAr0whuS1xN0DzRVDOiciciaBEnt4wLviclJhsFB3vUwddv2yoHQ/640?wx_fmt=png)

6.从远程服务器下载JPEP图片，然后显示图片，图片内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74MFhiaFBOCJIBRRWn8Lb1qia3NOkhDcqRtiaZwoZCr0R0biaialSC8ldiceWw/640?wx_fmt=png)

7.MSI安装程序相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74O7y537KCq7YIs5sIaZB0Wt2EcajRP91DJ70SW7GjHnlQsVYf8YwTWQ/640?wx_fmt=png)

8.枚举MSI文件的表和流信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74uVTDTPNtDTuMCMn3KkyxFt6fVNuOE0Ppnlrco5NiaicshWMTLvicRNHFw/640?wx_fmt=png)

9.解压缩MSI安装程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74288Hj7jB1pAeetbN6Rp36SEkjYtOYiaor41dNrscwR7QwDF27AeUJ8A/640?wx_fmt=png)

10.查看CustomAction.idt文件内容，执行自定义安装脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74jmkrs4qBsLm2zA2gtLlNV41GtFN0ppJQTAlLBLwGR23hiaeB4tGhz9g/640?wx_fmt=png)

11.解压出自定义操作DLL模块和包安装CAB文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74KGibtUtazz9xM7hGqNvc8oibib8yxvibN4wSTAwj5Pic8sVagQuIYWmtPQA/640?wx_fmt=png)

12.自定义操作DLL解析安装包安装CAB文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74FGTrq70CnHqUVtNkmjVor1so9n6HA0k17FRTpRgHDPRkFkpJJP8ecw/640?wx_fmt=png)

13.包安装文件配置信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR7468nneXMFCnib82kqic5Fpg49JFyv5t7lkL6nOoEtXKZaD97IVVFD3Mbw/640?wx_fmt=png)

14.包安装文件在Temp目录下解压缩之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74IpIyJzPcoykeXbSuiceNmET7aichlcpxtxMIg1ogN8HxUrdhbybRopzg/640?wx_fmt=png)

15.设置系统自启动项注册表值，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74VwjHqiaBUVbjUCbicJbQYKtb9kyF83jVKeSicmgu1Bxz2unQOyMUeSv3w/640?wx_fmt=png)

16.将解压后相关恶意文件拷贝到%appdata%\WMProjectFiles目录下，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74Y93yiaVg1A1RexpibqMUeeqwgjND5D46qibclhdvibzsp1jCIpQoewJUtA/640?wx_fmt=png)

17.%appdata%\WMProjectFiles目录下生成恶意文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74rbgUYjvHgpfXkTxMYRlJntG5jPE1f2RHUtwTmYYZfZpLTlZXGibcpDw/640?wx_fmt=png)

18.调用MAFWIKFNMUI9430.ocx模块导出函数RunDllEntryPointW，该模块是一个VB编写的加载程序，编译时间为2024年5月20日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74FSTLLwBZBCKx2PuPoKu6BBicgzicsywG1ibCibteRBv7icLqe07kNbMicZjw/640?wx_fmt=png)

19.设置相关的注册表项，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74icwM9Dnj9l3ETAbjxJHzO0icVZ2cicaO87Lnwxfxp4Au7RPEIKI6a8X4w/640?wx_fmt=png)

20.info.txt注册表项内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74YvDfvZUYlE4ibKUiaxFVSiaBOfcia35fbQBBodd29nsnnBib6x8Q86UibThQ/640?wx_fmt=png)

21.设置完成之后的注册表项，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74eMHibUhGw82Ihmrkr9JQjia6WXErSiaX10lYVYL16S4kWsWTZQia9pDic3A/640?wx_fmt=png)

22.调用soundtrack.ocx恶意模块，该模块也是一个VB编写的加载程序，编译时间为2024年5月20日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74Xmw1UVpxH9QX52x3QpObVHyvLhQYcegDPzqVlrtrwh3GIH42PmsgZg/640?wx_fmt=png)

23.恶意模块读取同目录下的WMFile01.tmp文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74lJnOic407veJwlIGEIZamKPdjlmklEdRj9iaReFlK65tibPrj7lYNoGdQ/640?wx_fmt=png)

24.在指定的目录下解密生成WMFile01.dll模块，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74OteiaHfEyFszKQ2ymQwJfvyakz8xBHibEwsAVL3uIfeatTvkLEyic9ysw/640?wx_fmt=png)

25.调用WMFile01.dll模块，启动%appdata%\ProductConfigurations目录下的WINDBVERS程序，并将恶意代码注入到WINDBVERS.EXE进程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74IJA7lxiaWD6ticiclhrAIL61y4UsVg2ZqSryUdRaTyvnIsSv3dg5qSLog/640?wx_fmt=png)

26.相关的函数API列表，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74mSloAUnnT8GnGd3b2Ua2KZKib0Aibpiajsy0EtxVibia0iaiay5aPXLBsyOaQ/640?wx_fmt=png)

27.从内存中DUMP恶意代码，最后的Payload仍然是一个使用VB编译的程序，编译时间为2024年5月11日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74EYAyZfTx3AmNMPXwTtwPXvjUeO5SxMQ69gXFDqibhFtJtAQTZrJlGAA/640?wx_fmt=png)

28.通过分析可以确定最终的Payload为DarkMe RAT恶意程序，里面也使用了大量的混淆代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74qAJhh1JUI9vspiaal6cOHsaJDOHBCxia1ibGT7tibJ2ic2LFG8ef3EzZNmw/640?wx_fmt=png)

29.创建隐藏窗口，传输套接字数据，与服务器端通信，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74lyjLuqPoib3soJEEk8ZLkibWmREU9cSzdkHparlgTuDYlK4bh0a6D3QA/640?wx_fmt=png)

30.解密出远程服务器域名unfawjelesst322.com，与远程服务器通信，相关的流程信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74OmTnPKictGSKUfcMQ09HGia11QpO1iclpBjALNHoFVbPuibTiahDW4riaAkA/640?wx_fmt=png)

该RAT恶意软件，支持多种不同的指令操作，包含文件目录操作、注册表操作、获取主机相关信息、截取屏幕信息、执行Shell、上传下载文件等。

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74QM2IjhVwhz7YKAQ21KicIwmVzCL5GuDLvNB5MEgYLo3NibfvmR79DZkQ/640?wx_fmt=png)

总结结尾

黑客组织利用各种恶意软件进行的攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，而且非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

安全分析与研究，专注于全球恶意软件的分析与研究，深度分析追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmV8xT8dcYW78f9dA31kBR74ZAicnWqt2ycGWVXXCicWbbdlUdVniacjMoEd75hHic2VhLZibGTVolzMaxg/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

预览时标签不可点

阅读原文

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