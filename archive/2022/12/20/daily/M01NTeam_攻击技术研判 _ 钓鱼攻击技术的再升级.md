---
title: 攻击技术研判 | 钓鱼攻击技术的再升级
url: https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490335&idx=1&sn=c121efa85e964d8d5634e941dd494229&chksm=c187db0ef6f052185f9f7e31225bd267440662f3a42fbcc2579a7a69ead54448ff5084f572c1&scene=58&subscene=0#rd
source: M01NTeam
date: 2022-12-20
fetch_date: 2025-10-04T02:00:04.951536
---

# 攻击技术研判 | 钓鱼攻击技术的再升级

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwajyBoq4ftnia3wvfWIGicCLKkIqtS8oiaZPv1LiaBlibbCtnMhgowKS2bfcHlROeJ0Q5m0EI8hksp4TSQ/0?wx_fmt=jpeg)

# 攻击技术研判 | 钓鱼攻击技术的再升级

原创

天元实验室

M01N Team

![](https://mmbiz.qpic.cn/mmbiz_gif/TPGibEO8KBwajyBoq4ftnia3wvfWIGicCLKu5noCIJPV9QUGyzcEiaRoyFadictfXnpMyAw2DYTTkmubjcYmF9g526A/640?wx_fmt=gif)

**情报背景**

近期，Splunk 威胁研究团队对QakBot的攻击手法的演进进行了分析，在这之中不乏有各种技术的改进利用和创新。其中,QakBot在对钓鱼技术的改进更是细腻，本文将对文中的钓鱼技术改进进行剖析。

|  |  |
| --- | --- |
| **组织名称** | QakBot |
| **战术标签** | 初始访问 载荷投递 |
| **技术标签** | html smuggling iso lnk |
| **情报来源** | https://www.splunk.com/en\_us/blog/security/from-macros-to-no-macros-continuous-malware-improvements-by-qakbot.html |

**01** 攻击技术分析

攻击过程如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwajyBoq4ftnia3wvfWIGicCLKlpZq93ib2wB9YD2H1oiaCiaoZibVp9k9iakxUmrnRJic5dUoqD5u5WXGibUpQ/640?wx_fmt=png)

1.钓鱼网页中利用HTML smuggling将zip文件释放至目标主机

2.受害者点击恶意zip并输入密码，解压文件

3.解压后的文件中包含ISO文件，打开ISO后在受害者的视角中，只看到了一个伪造成文件夹的lnk文件，诱导受害者点击

4.受害者点击LNK文件后执行恶意脚本，攻击者实现上线，达到攻击目的

**亮点1 HTML smuggling的双层嵌套进行防御规避**

html smuggling自出现以来，备受钓鱼佬的青睐，各类安全产品也逐渐对此有所检测。而QakBot在攻击中采用了多个html钓鱼网站嵌套的方式，进行有效的防御规避。具体过程如下：

1.对使用了html smuggling技术的html2进行base64和字符反转实现混淆，嵌入在html1(受害者访问的钓鱼网页)中

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwajyBoq4ftnia3wvfWIGicCLKwpCnjOfpcUtPlfJKzzJ77OW1t5Gk322RBLeuOsm9NlVa7EjkApicnHw/640?wx_fmt=png)

图一 html1部分代码

2.嵌入方式采用的是html的 "embed" 标签，且setAttribute中参数设为1，即对该段代码的执行进行隐藏

3.执行html1中的reverse函数之后，将html2进行恢复并执行html smuggling实现下发zip恶意压缩包。html2具体代码如下：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwajyBoq4ftnia3wvfWIGicCLKEnBeObiadduDnBvM1kMDKGglxBnWG3Ukha1C8Ish642oibZRkbicKwaoQ/640?wx_fmt=png)

图二 html2部分代码

以往攻击者使用html smuggling的方式大多只是如html2一样，即一个html中包含html smuggling，打开后便下发文件至受害者本地。而该方式的改进，让原本释放文件的html文件更加隐蔽，html smuggling的代码执行也从原本的静态可见演变为动态执行，具有良好的防御规避效果。

**亮点2 lnk执行的改进**

攻击者使用的lnk的构造如下：

1.使用cmd.exe 执行.bat脚本，bat脚本执行另一个cmd脚本protracted.cmd，且protracted.cmd使用参数进行执行,bat脚本具体内容如下:

```
C:\Windows\System32\cmd.exe /c tools\protracted.cmd re gs v
```

2. "re gs v" 作为参数传入 protracted.cmd脚本，拼接脚本，实现脚本执行

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwajyBoq4ftnia3wvfWIGicCLKzpVWlRnIFRMUtOgnPKvYYzWhOqjOydxjOXFG0ibMl977bTh0LO2VqhA/640?wx_fmt=png)

3.脚本执行功能主要有：

* 将系统自带的regsvr32.exe复制为\appdata\local\temp\envelopingConcussion.com
* 使用envelopingConcussion.com执行bucketfuls.dat程序
* bucketfuls.dat是一个具有后门功能的dll，达到攻击目的

由此可见，与其他常见的lnk采取的方式不同的是，该bat脚本中执行cmd脚本程序时：

1.使用参数构造完整的cmd脚本，将敏感的程序名和路径的字符串，如"regsvr32.exe"，通过脚本进行拼接，减少敏感字符串暴露，达到静态防御规避效果

2.脚本中再执行脚本，而不是直接执行程序，拉长攻击链，同样达到防御规避效果

**02**总结

本文对QakBot在钓鱼中的技术的再改进进行了一定的分析，是值得参考的防御规避手法，可以借此举一反三，加强规避效果。同时，对于防守方而言，也是可参考的检测点。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwajyBoq4ftnia3wvfWIGicCLKNmQhXC47bFV719RjAvKqz5VtA8Yiczy0Wfr7yBXFb4RUpzvP2UPJjpA/640?wx_fmt=png)

**绿盟科技天元实验室**专注于新型实战化攻防对抗技术研究。

研究目标包括：漏洞利用技术、防御绕过技术、攻击隐匿技术、攻击持久化技术等蓝军技术，以及攻击技战术、攻击框架的研究。涵盖Web安全、终端安全、AD安全、云安全等多个技术领域的攻击技术研究，以及工业互联网、车联网等业务场景的攻击技术研究。通过研究攻击对抗技术，从攻击视角提供识别风险的方法和手段，为威胁对抗提供决策支撑。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwajyBoq4ftnia3wvfWIGicCLKVG4HZvsKl87DYyOiaWbkvlXuFWYVHE7keo2d3kOR4d4PZ0LWWAia6MvQ/640?wx_fmt=jpeg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwajyBoq4ftnia3wvfWIGicCLKp28dNAr2QY8d3lw4GHcIfcs75FDDYoLJ6KcazueiaibGQ2ib6HcezBlHg/640?wx_fmt=jpeg)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

**往期推荐**

[攻击技术研判｜Roshtyak中使用的内存防御规避策略](http://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490298&idx=1&sn=ed894219e04d36e454ead4f15420334d&chksm=c187daebf6f053fd20f6ca9ee6ed1e7f821c014b672ea86d44ca7e24c94c0de1f39d435a2dfb&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwajyBoq4ftnia3wvfWIGicCLKwAwTMElqX2icJe2VcrqjJGO1KddAo4sqnsl9sbCcV1oBk7SlU2QaBmw/640?wx_fmt=png)

[攻击技术研判｜利用.NET NativeAOT特性的新型攻击手法](http://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490235&idx=1&sn=9a6d99702b83320a16a362ae3c0fdfe3&chksm=c187daaaf6f053bc149ac8737fb840de53fe656f750ac99e633f1b627b7ded9e7df4d68c7daa&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwajyBoq4ftnia3wvfWIGicCLKwAwTMElqX2icJe2VcrqjJGO1KddAo4sqnsl9sbCcV1oBk7SlU2QaBmw/640?wx_fmt=png)

[攻击技术研判｜一种在行末隐藏有效载荷的新供应链攻击技术](http://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490196&idx=1&sn=a5d977f69b082c3a17804e263ffb0a46&chksm=c187da85f6f0539349a3e6bd0ce4c3f454bfa89e25d2352992f7766422e3f257b28f8abe5337&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwajyBoq4ftnia3wvfWIGicCLKwAwTMElqX2icJe2VcrqjJGO1KddAo4sqnsl9sbCcV1oBk7SlU2QaBmw/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

M01N Team

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

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