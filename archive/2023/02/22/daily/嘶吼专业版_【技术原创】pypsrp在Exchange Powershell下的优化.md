---
title: 【技术原创】pypsrp在Exchange Powershell下的优化
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247557838&idx=1&sn=2e92152a3cca7c3bbb112bafcd07ebe4&chksm=e91432f4de63bbe2afcdb2db164431b30147443ee78123a20ba9fa3987e6f269d15fada963d0&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-02-22
fetch_date: 2025-10-04T07:44:10.891889
---

# 【技术原创】pypsrp在Exchange Powershell下的优化

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknCNl6Nd0hQK6MzsLSWgGj7UXm4ETszX3Y42dNVqnsOz3Z1gXen86n7w/0?wx_fmt=jpeg)

# 【技术原创】pypsrp在Exchange Powershell下的优化

原创

3gstudent

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknmFCmQqWTXQqKdIX57iaibofB6O9NTUw9TOlav0ia1YkRhXH2qTQ2iaNQOA/640?wx_fmt=png)0x00 前言

pypsrp是用于PowerShell远程协议(PSRP)服务的Python客户端。我在研究过程中，发现在Exchange Powershell下存在一些输出的问题，本文将要介绍研究过程，给出解决方法。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknmFCmQqWTXQqKdIX57iaibofB6O9NTUw9TOlav0ia1YkRhXH2qTQ2iaNQOA/640?wx_fmt=png)0x01 简介

Exchange PowerShell Remoting

pypsrp的使用

pypsrp存在的输出问题

解决方法

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknmFCmQqWTXQqKdIX57iaibofB6O9NTUw9TOlav0ia1YkRhXH2qTQ2iaNQOA/640?wx_fmt=png)0x02 Exchange PowerShell Remoting

参考资料：

https://docs.microsoft.com/en-us/powershell/module/exchange/?view=exchange-ps

默认设置下，需要注意以下问题：

所有域用户都可以连接Exchange PowerShell

需要在域内主机上发起连接

连接地址需要使用FQDN，不支持IP

通过Powershell连接Exchange PowerShell的命令示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknd2icQQzFtUahXI4UxagDoFjdQTC5qdxjqNj4WSfGEIOd2XfSXfrpLrw/640?wx_fmt=png)

通过pypsrp连接Exchange PowerShell的命令示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknibJuINk9aKXNGTSDnqKLkeiaPRuwR3Xn0FEdrEcQagE8ONwxGRON1adw/640?wx_fmt=png)

如果想要加入调试信息，可以添加以下代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDkndLUmDgBZUs5QVtxwoNjtC0m3GV3dhBmqM2FmUUyZqZ2sTyfXP5pkxg/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknmFCmQqWTXQqKdIX57iaibofB6O9NTUw9TOlav0ia1YkRhXH2qTQ2iaNQOA/640?wx_fmt=png)

# 0x03 pypsrp存在的输出问题

我们在Exchange PowerShell下执行命令的完整返回结果如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDkn5dFg8yNSCLPic4ickicJsO76acvia4icicSy9zSAibmIgLyyKGbYnVeWEbkPg/640?wx_fmt=png)

但是通过pypsrp连接Exchange PowerShell执行命令时，输出结果不完整，无法获得命令的完整信息，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDkniaabHk5l1YEI7gaADGHBJWia5o0849ibnjr8NQXvt0aa3iaZFAZ3H5T2mQ/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknmFCmQqWTXQqKdIX57iaibofB6O9NTUw9TOlav0ia1YkRhXH2qTQ2iaNQOA/640?wx_fmt=png)

# 0x04 解决方法

1.定位问题

通过查看源码，定位到代码位置：https://github.com/jborean93/pypsrp/blob/704f6cc49c8334f71b12ce10673964f037656782/src/pypsrp/messages.py#L207

我们可以在这里添加输出message\_data的代码，代码示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknx1DwoOYrDdyoTicbr2lsdPHom1rfVR2lmxibF0icibVTibiaNyoz2WnNbMLA/640?wx_fmt=png)

返回结果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknW6Y0ajGXRvjK8L49djd1Ic6CqJqLnQsy929xuXEKNYy7GcLgxkBWEA/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknxkasGOlSLH3yNMQQsmLLvG387d6NsTuBPnIH1lribBtib3I6sYeJbvww/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknUeMnC3yQDN33qF3jCzleq1iagQdtWbdKghL7ic0CVg5LZgL7Bx7Kicvlg/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknT7uGC7qibuOsygvqgvgkibbw9mOKluYhLgwajQMVTUpBXeE92KtricJgA/640?wx_fmt=png)

在调用serializer.deserialize(message\_data)提取输出结果时，这里只提取到了一组数据，忽略了完整的结果

经过简单的分析，发现标签内包含完整的输出结果，所以这里可先通过字符串截取提取出标签内的数据，示例代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknrgSju49cBEjIgZa52fhbhKGb0sHkRn3U0CXib5enf2gVHXHyBmwY7dQ/640?wx_fmt=png)

进一步分析提取出来的数据，发现每个标签分别对应一项属性，为了提高效率，这里使用xml.dom.minidom解析成xml格式并提取元素，示例代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknd8tX5MdLxEibHn8meeK4MVI5OytPdWk0bl9N4I7SrXPOYt5z6tlfgicw/640?wx_fmt=png)

经测试，以上代码能够输出完整的结果

按照pypsrp的代码格式，得出优化pypsrp输出结果的代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknRS7cJh1yYtCqcuibVena5icRXe6c5LKV55fvgaibeHmSiaeRy0FXfMVibMA/640?wx_fmt=png)

使用修改过的pypsrp连接Exchange PowerShell执行命令时，能够返回完整的输出结果，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknEt0wRRwtN4FW23RySXr8auOUdIwyrWy0vbicKLibASULQgYCMgqGoqbg/640?wx_fmt=png)

经测试，在测试ProxyShell的过程中，使用修改过的pypsrp也能得到完整的输出结果

补充：

如果使用原始版本pypsrp测试ProxyShell，可通过解析代理的返回结果实现，其中需要注意的是在作Base64解密时，由于存在不可见字符，无法使用.decode('utf-8')解码，可以换用.decode('ISO-8859-1')，还需要考虑数据被分段的问题，实现的示例代码如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknbKC5rkZl4Ny0D9K1u5LNEYN3F2aJS6MR03t4tSsdVuc5MYBbHkMDiag/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknmFCmQqWTXQqKdIX57iaibofB6O9NTUw9TOlav0ia1YkRhXH2qTQ2iaNQOA/640?wx_fmt=png)0x05 小结

本文介绍了通过pypsrp连接Exchange PowerShell执行命令返回完整输出结果的解决方法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknXePQ2ia4fViaibt3ial7B4TBx2tLctq8oSPhfbyvbqicnpGrKdNhtln26AA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTBibRib5y9l81LmS5SQXDknPxA6htib7azL8hAMC78mAnsvl4wWzkT8AbvRvlZ2lQDccqUZPPqqzAw/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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