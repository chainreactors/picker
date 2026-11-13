---
title: 第180篇：蓝队分析取证工具箱 V5.11，新增自动化解密、流程图展示等功能
url: https://mp.weixin.qq.com/s/LJkh00zABp0saB-1vRUqLg
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:57:48.500759
---

# 第180篇：蓝队分析取证工具箱 V5.11，新增自动化解密、流程图展示等功能

# 第180篇：蓝队分析取证工具箱 V5.11，新增自动化解密、流程图展示等功能

取证与溯源

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于希潭实验室
，作者abc123info

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM6fmEcY2bcaelEq3UFVKWcPYSM5dibWwP6KNJRapia8tbPQ/0)

**希潭实验室**
.

ABC\_123，2008年入行网络安全，希潭实验室创始人，某工业大学客座教授，某部委授课讲师、省级专家裁判，省评标专家。专注于安全咨询、网络安全培训、APT技战法分析、代码审计、渗透测试。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9Lbc0INLwTJTZT1GaNutZrfDn6csvjBoS2ox0efLUEexXqPEcVbYfbLo8w/640?wx_fmt=png)

 Part1 前言

大家好，我是ABC\_123。最近抽时间，结合网友们的反馈，对蓝队工具箱的各个功能进行了大幅度的升级。加入了自动化解密Webshell流量的功能、大幅度提升pcap包分析功能、加入可视化流程图功能、jwt token分析功能等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2Zc77PyLkuDupKmynbgOEwUUWTzUVjztJ8lNBUiaU9icoEOBhMD2DdLFiazribOgicGo0O9910qnCUP5NsLGWiabqBwOm1v6GShlmRj0/640?wx_fmt=png&from=appmsg)

 Part2 技术研究过程

* 更新内存马反编译分析功能

可以对不同加密类型的内存马进行反编译分析，此次更新添加了"查看代码流程图功能"，新增python bytes、Base64+zip.Inflater编码的内存马反编译功能。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2ZR7ozFWDYJRPBKug03oHHyOqtddAXDibBnE8zqZTb2fPwdE2d6m5dvmyl66UIyQABhgOpeV8lavqtdAppJkUzIicgthZsFkhiaJ4/640?wx_fmt=png&from=appmsg)

* ### 更新Java反序列化分析功能

添加"查看代码流程图"功能，新增python bytes、Base64+zip.Inflater编码的反序列化数据包分析功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2bNF4E8jsPSI2qvPA4rt5dX2Q3QjZuhLOic1cibuPAKoWa2RsbwwS83TG7hmYIibeeetaa4Tb46mFkLcgyibNFMFUlNoPfhrJbwlMU/640?wx_fmt=png&from=appmsg)

* ### 漏洞分析添加流程图展示功能

新增"对象关系图"展示功能。新增宝兰德bes中间件、帆软、浪潮GS、Hessian等反序列化数据包的分析功能，方便溯源分析攻击者的攻击行为。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2atQQat2FqrHdcBLlJG8IicbwfiamQ95qCnkwhMlyCpniae6feD8p9l8n3VdYdnyiatibdoqWhwtAhQZ1d8ccasFb5qsDwFVS1Dcibiak/640?wx_fmt=png&from=appmsg)

点击开始"解密按钮"，会自动化生成流程图，也可以导出PNG格式的流程图，放到溯源分析报告中。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2YZou883zFxVhEne8MG52w9o0Dpd1KC7fEPwqU3xjBADClIEh6XvdGl5Miczu9RdJJicKVaia500uv8FoL2dqWr8b085oDtkia7f2s/640?wx_fmt=png&from=appmsg)

###

* ### 全自动解密功能

点击"全量自动解密"按钮，可以对粘贴的数据包，自动识别出主流的Webshell的流量并解析；也可以"使用密码字典自动化解密加密流量"按钮进行爆破猜解key，然后还原出明文数据包。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2aS2dIwqKF3feQnSX6t0q1TmxP9WChggaH2OrzkP6UkRHZ1jN0sVuZKagIPBzMQhSUtj7SyyE9GyZpTYZbXUwjrQs7RiaAOCjyU/640?wx_fmt=png&from=appmsg)

###

* ### Webshell自动解密，添加UI展示功能

点击"自动解密"按钮，可以对主流的Webshell的数据包进行解密，无需手工选择数据包；新增魔蝎1.5版本、GTWebShell、旧版彼岸花等Webshell的加密流量解密功能。新增webshell流量返回数据包的"UI界面展示"功能。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2ZdGd6VE1VicqJC5re36vicNRAwlib6QrlIpnluGadpss9UqWaI2TappTzutVNwAiancS94yCAmAIu3JYjsKObjxkiblITHcArwGqnc/640?wx_fmt=png&from=appmsg)

如果返回数据包显示攻击者尝试翻查目录，可以直接树形框显示出目录、文件的属性结构等，看起来更加直观。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2ZWPvpMx0RvC5NJEmm2rOoUHww3Zd2ibVSvXOQSN9R3pjfv1dZ9GUc7FBWiakm658qjFkdfLX3FpkxgmUbKLeRFaT6icKHJXibnrSU/640?wx_fmt=png&from=appmsg)

* ### 更新流量包分析功能，速度大幅提升

花费很大精力，解决流量包分析功能的性能问题，分析10几个G的Pcap包也没有问题。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2Zibv0qbTXvuPZ7gsEelPTXnsQfqnR3m0q2iaqDkCdicDibmlwj9QrAI9lBKpHibqIibUe2rLEtgicQeowhCAjQYcRiaxHDe2lInpuibqIM/640?wx_fmt=png&from=appmsg)

加入了大量的pcap流量包的统计分析展示能力，包括IP分析展示、XXF的ip地址统计、会话分析、主机活动时间线、攻击行为分析、TCP标志位统计、流量画像、HTTP画像等等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2boy2pUOCriadfxANXT4Tjb8LYiaMCgibZ85kyjE9l2P4zolaojUMHkyOy8bIJhdtdWLuclwvqXicNPyAL8Q6bMUcyeicKlmgUyEqNQ/640?wx_fmt=png&from=appmsg)

* ### 更新溯源反制功能

针对NPS代理反制功能，针对3种情况都进行分析反制。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2bicuxkuayrEZLDFKZX640FdqCoRWOzASXqmzwpCJOMStiaH5ib6fNeCZ1ic2I9AFJQvRVjqZXuLic9lqvHPMAyibFwMnZ7OIEuiaQVko/640?wx_fmt=png&from=appmsg)

* ### 新增编码/解码功能

### 大幅度优化"JWT Token编码/解码"功能、红队常用的编码功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2a2vHqAsAPw4cZysSKPict2yoeFf8p3aICbyb4XTxBSILO7AZjk9VKolXqCx8SiaBibZxKub0ib8w4e8n8zgXxD3y0TtkbAnliaViaoY/640?wx_fmt=png&from=appmsg)

大幅度融合各个"XSS编码/解码"功能，不再使用调用本地html页面的方式，改用java代码全部仿照重写。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2bCu8R1wDczrOflpiatxXnboOchjOJekXO2N6zxQ5pOLDEZbFLsJiaULrCLZRnicdKiaUPM4HV0VJgibZfZic2icK475LZ3THL8VMGKKQ/640?wx_fmt=png&from=appmsg)

* 更新机器学习识别DGA域名功能

### 用本机显卡重新跑的4个机器学习模型，提升DGA域名识别的准确度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2ar4poA5KB926jibpypoQM6dCKqwkBMU41xBFtjXEr3NgtTSwWxIcD52ia9ymyujETVs9nibCkXnn5gNibs0lic6VC0XqOsrSQXMS7I/640?wx_fmt=png&from=appmsg)

 Part3 总结

1.  蓝队分析取证工具箱后续会继续添加新的分析功能，敬请期待。

2.  关注公众号"希潭实验室"，回复"蓝队"，即可得到此工具的下载地址。

3.  欢迎大家扫码加入知识星球希水涵@信安知识库，进入星球内部交流群，一起学习进步！

![](https://mmbiz.qpic.cn/mmbiz_jpg/uPOMOKjLe2YU6YdILmbv6CbQQjPzT5fTMH918e5lLTyuBcJxypX32Ihkyu2ab3ibjhnq7gTk7dvnJ4HibQpSziaOoDwpQj83t9OMtJicPErfKbo/640?wx_fmt=jpeg&from=appmsg)

为了便于技术交流，现已建立微信群"希水涵-信安技术交流群"，欢迎您的加入。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CCZ6JZb61crQSz8mzsGic5UDic2FzIQahiavs8MTicHrF8Q9ZpqBgb19eg9e2kQruCaiaiciaG5G74VSHjw/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450A5qqg2iaK6KIYYR8y6pF5Rh3JHDibOKOop204nXz618iawdRb8dABicMPtHb2PkJE8x6koJO5HyuwZJQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=18)

**公众号专注于网络安全技术分享，包括APT事件分析、红队攻防、蓝队分析、渗透测试、代码审计等，每周一篇，99%原创，敬请关注。**

**Contact me: 0day123abc#gmail.com**

**OR 2332887682#qq.com**

**(replace # with @)**

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/dwTW4pyxLTnvdjZrQ9sYsrHVWx683lYSM0wnbVtfAs1Xp1cAbFBQ0lyAp87Z5BciaLQj54X8hCx7qbyJy6lOLXw/0?wx_fmt=png)

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