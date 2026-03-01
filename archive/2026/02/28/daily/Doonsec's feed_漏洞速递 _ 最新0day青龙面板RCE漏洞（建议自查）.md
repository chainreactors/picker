---
title: 漏洞速递 | 最新0day青龙面板RCE漏洞（建议自查）
url: https://mp.weixin.qq.com/s/cCNxCrxNN9BY_xPYD9vwLg
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:21:58.840628
---

# 漏洞速递 | 最新0day青龙面板RCE漏洞（建议自查）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/7D2JPvxqDTGZHPMZiaGxWiaiaUV44FibFassLCcPrbpIOTx737LgyDkwvcBXns6Ixk1twmDlfbBLoLO6YeibDDndX4Q/0?wx_fmt=jpeg)

# 漏洞速递 | 最新0day青龙面板RCE漏洞（建议自查）

渗透Xiao白帽

![]()

在小说阅读器中沉浸阅读

***0x01 前言***

     青龙面板最新版本鉴权绕过导致远程代码执行漏洞，未经身份攻击者可通过该漏洞在服务器端任意执行代码，写入后门，获取服务器权限，进而控制整个 web 服务器。鉴于该漏洞影响范围较大，建议尽快做好自查及防护。

![](https://mmbiz.qpic.cn/mmbiz_png/7D2JPvxqDTEGws3l7BKRruibdXCDXh0DBwwyWuh8tcIHnG3L1krsicIs7Q3ib9HpvJHmiapJrNqg8UG4yPlMmqmSwA/640?wx_fmt=png)![]()

***0x02 漏洞等级***

```
高危
```

***0x03 漏洞影响***

```
icon_hash=="-254502902"
```

两万多条匹配结果~

![](https://mmbiz.qpic.cn/mmbiz_png/6XGOZPCymFcRS2Crgib3mPYaBR6TMHib2xicIRQ5r5HunTSuJjrFwG3Wx8VZG3Tt3mnVEhWvUknXulCZeLm3ibOFvKibjGsvgJlAQmFqc51yQyog/640?wx_fmt=png&from=appmsg)

***0x04 漏洞复现***

`PoC网上已公布建议尽快排查修复：`

![](https://mmbiz.qpic.cn/mmbiz_png/6XGOZPCymFfj6NhP8w12g6Z0XKFwUyAW6DCwFibmt5o1RQ8nnZia1IcT5qlIlR5BBibeXdyNBibJ3tkvBK7kVgibItcxxkmWZeT2UTcib5nwrZX0E/640?wx_fmt=png&from=appmsg)

***0x05 修复建议***

针对已安装青龙面板的用户，官方给出了明确的应急处置方案。第一步是自查风险，通过SSH方式登录NAS，检查路径/ql/data/db/下是否存在陌生的.fullgc恶意文件，同时使用top命令观察系统进程，排查是否有CPU、内存异常高占用的未知进程。这一步就像是给设备做一次全面的体检，及时发现潜在的问题。如果发现了恶意文件或异常进程，用户需要立即停止青龙容器及相关服务，并彻底删除恶意文件，避免其持续破坏设备。关闭公网映射也是非常重要的一步，若此前已将5700/15700端口映射到公网，务必立即关闭，杜绝不法分子通过漏洞远程攻击的可能。在开发者未发布官方安全修复版本并经厂商验证前，建议直接停用青龙面板，切勿抱有侥幸心理继续使用。

![图片](https://mmbiz.qpic.cn/mmbiz_png/7D2JPvxqDTER2M22xQ4L9ypTc8ycOSFz16CibJb5tZJAekLtXvhuAVPTwsIdyfGc6vViaCWib8HwdUeTs72DzN4ag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**网 安 考 证![图片](https://mmbiz.qpic.cn/mmbiz_png/7D2JPvxqDTER2M22xQ4L9ypTc8ycOSFz16CibJb5tZJAekLtXvhuAVPTwsIdyfGc6vViaCWib8HwdUeTs72DzN4ag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)**

需要考各类安全证书的可以扫码找我咨询，价格优惠、活动划算！

报名CISSP、CCSP、PTE、PTS、IRE、IRS、DSG、CCSK、CDSP、CZTP、ITIL4等符合活动标准的认证课程。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/7D2JPvxqDTHjHaNZEcAQxmACdS20uaT7YUP0TObLHLBicia6vKicVJ75AVOfN3RQxop70GQXFhFRm0ZkdKoydgfIg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1&random=0.06125543926007038&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/ib745vqibLBGIeAicnHiag9GCzTYjeicic5IWPqfyjLajDuwtJdNCAnCgcolqY8ROaE5CsEXR5zbjCU9aVl3WfkZpnDw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

往期推荐 · 有彩蛋

[【内网渗透】内网信息收集命令汇总](http://mp.weixin.qq.com/s?__biz=MzI1NTM4ODIxMw==&mid=2247485796&idx=1&sn=8e78cb0c7779307b1ae4bd1aac47c1f1&chksm=ea37f63edd407f2838e730cd958be213f995b7020ce1c5f96109216d52fa4c86780f3f34c194&scene=21#wechat_redirect)

[【内网渗透】域内信息收集命令汇总](http://mp.weixin.qq.com/s?__biz=MzI1NTM4ODIxMw==&mid=2247485855&idx=1&sn=3730e1a1e851b299537db7f49050d483&chksm=ea37f6c5dd407fd353d848cbc5da09beee11bc41fb3482cc01d22cbc0bec7032a5e493a6bed7&scene=21#wechat_redirect)

[【超详细 | Python】CS免杀-Shellcode Loader原理(python)](http://mp.weixin.qq.com/s?__biz=MzI1NTM4ODIxMw==&mid=2247486582&idx=1&sn=572fbe4a921366c009365c4a37f52836&chksm=ea37f32cdd407a3aea2d4c100fdc0a9941b78b3c5d6f46ba6f71e946f2c82b5118bf1829d2dc&scene=21#wechat_redirect)

[【超详细 | Python】CS免杀-分离+混淆免杀思路](http://mp.weixin.qq.com/s?__biz=MzI1NTM4ODIxMw==&mid=2247486638&idx=1&sn=99ce07c365acec41b6c8da07692ffca9&chksm=ea37f3f4dd407ae28611d23b31c39ff1c8bc79762bfe2535f12d1b9d7a6991777b178a89b308&scene=21#wechat_redirect)

[【超详细 | 钟馗之眼】ZoomEye-python命令行的使用](http://mp.weixin.qq.com/s?__biz=MzI1NTM4ODIxMw==&mid=2247488453&idx=1&sn=5828a0e1a2299d3ee0215f0ed4c30bf1&chksm=ea37ec9fdd406589124c67c45487be39ed1033d88c627092cf07f6d4f14ccdb9079b38dba74d&scene=21#wechat_redirect)

[【超详细 | 附EXP】Weblogic CVE-2021-2394 RCE漏洞复现](http://mp.weixin.qq.com/s?__biz=MzI1NTM4ODIxMw==&mid=2247488922&idx=1&sn=f43e3c243bbbfd2822867a3acaa8b85e&chksm=ea37eac0dd4063d63d98f935c73ce571cbfeb0e7272a6f171a28143bdb3e7134b09ea874969a&scene=21#wechat_redirect)

[【超详细】CVE-2020-14882 | Weblogic未授权命令执行漏洞复现](http://mp.weixin.qq.com/s?__biz=MzI1NTM4ODIxMw==&mid=2247485550&idx=1&sn=921b100fd0a7cc183e92a5d3dd07185e&chksm=ea37f734dd407e22cfee57538d53a2d3f2ebb00014c8027d0b7b80591bcf30bc5647bfaf42f8&scene=21#wechat_redirect)

[【超详细 | 附PoC】CVE-2021-2109 | Weblogic Server远程代码执行漏洞复现](http://mp.weixin.qq.com/s?__biz=MzI1NTM4ODIxMw==&mid=2247486517&idx=1&sn=34d494bd453a9472d2b2ebf42dc7e21b&chksm=ea37f36fdd407a7977b19d7fdd74acd44862517aac91dd51a28b8debe492d54f53b6bee07aa8&scene=21#wechat_redirect)

[【漏洞分析 | 附EXP】CVE-2021-21985 VMware vCenter Server 远程代码执行漏洞](http://mp.weixin.qq.com/s?__biz=MzI1NTM4ODIxMw==&mid=2247487906&idx=1&sn=e35998115108336f8b7c6679e16d1d0a&chksm=ea37eef8dd4067ee13470391ded0f1c8e269f01bcdee4273e9f57ca8924797447f72eb2656b2&scene=21#wechat_redirect)

[【CNVD-2021-30167 | 附PoC】用友NC BeanShell远程代码执行漏洞复现](http://mp.weixin.qq.com/s?__biz=MzI1NTM4ODIxMw==&mid=2247487897&idx=1&sn=6ab1eb2c83f164ff65084f8ba015ad60&chksm=ea37eec3dd4067d56adcb89a27478f7dbbb83b5077af14e108eca0c82168ae53ce4d1fbffabf&scene=21#wechat_redirect)

## [【奇淫巧技】如何成为一个合格的“FOFA”工程师](http://mp.weixin.qq.com/s?__biz=MzI1NTM4ODIxMw==&mid=2247485135&idx=1&sn=f872054b31429e244a6e56385698404a&chksm=ea37f995dd40708367700fc53cca4ce8cb490bc1fe23dd1f167d86c0d2014a0c03005af99b89&scene=21#wechat_redirect)

[【超详细】Microsoft Exchange 远程代码执行漏洞复现【CVE-2020-17144】](http://mp.weixin.qq.com/s?__biz=MzI1NTM4ODIxMw==&mid=2247485992&idx=1&sn=18741504243d11833aae7791f1acda25&chksm=ea37f572dd407c64894777bdf77e07bdfbb3ada0639ff3a19e9717e70f96b300ab437a8ed254&scene=21#wechat_redirect)

[【超详细】Fastjson1.2.24反序列化漏洞复现](http://mp.weixin.qq.com/s?__biz=MzI1NTM4ODIxMw==&mid=2247484991&idx=1&sn=1178e571dcb60adb67f00e3837da69a3&chksm=ea37f965dd4070732b9bbfa2fe51a5fe9030e116983a84cd10657aec7a310b01090512439079&scene=21#wechat_redirect)

[记一次HW实战笔记 | 艰难的提权爬坑](http://mp.weixin.qq.com/s?__biz=MzI1NTM4ODIxMw==&mid=2247484991&idx=2&sn=5368b636aed77ce455a1e095c63651e4&chksm=ea37f965dd407073edbf27256c022645fe2c0bf8b57b38a6000e5aeb75733e10815a4028eb03&scene=21#wechat_redirect)

**走过路过的大佬们留个关注再走呗![](https://mmbiz.qpic.cn/mmbiz_png/7D2JPvxqDTGYu9nrfsXsv7ZrsqXibnKn0eCPo3D8HzHfmHdiar1tickAm9gP0XpiakaQhyB0ib0OBrNyp0Kpz59Umow/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&random=0.2553642180635751)![]()**

**往期文章有彩蛋哦![](https://mmbiz.qpic.cn/mmbiz_png/7D2JPvxqDTGYu9nrfsXsv7ZrsqXibnKn06P5qlPDOibvAu5D68z2GBB98ATYhb2G1pMVA6iahuBuWOyicnUGQcWarg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&random=0.3569542558042562)![]()**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7D2JPvxqDTGqQ9LmPjPNrA06yLgQ76dFnZQ2rqRibzS3VLSZpH37jsJ1XMM9T3GqSp8EibvglJkEkSej8zjX9VRA/0?wx_fmt=png)

渗透Xiao白帽

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7D2JPvxqDTGqQ9LmPjPNrA06yLgQ76dFnZQ2rqRibzS3VLSZpH37jsJ1XMM9T3GqSp8EibvglJkEkSej8zjX9VRA/0?wx_fmt=png)

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