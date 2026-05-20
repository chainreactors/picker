---
title: 最新公开 | 利用RPC添加计划任务Bypass核晶（有时效性）
url: https://mp.weixin.qq.com/s/NX5gDMqR_XMLdMjajsoJWQ
source: Doonsec's feed
date: 2026-05-19
fetch_date: 2026-05-20T06:01:21.241657
---

# 最新公开 | 利用RPC添加计划任务Bypass核晶（有时效性）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6XGOZPCymFcTFzo0cKXwUqFjZzIQ7byo52ib4qiaoPgbhpbOIRq8P3ibBTMcyQdrzLFrYJwg3tnyOTKn0WA2VVibic9C5Q1eV1mGZfnlrM9lGH4g/0?wx_fmt=jpeg)

# 最新公开 | 利用RPC添加计划任务Bypass核晶（有时效性）

原创

鬼屋女鬼
鬼屋女鬼

渗透Xiao白帽

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### 前言

事件的起因是有某学员通过飞书的权限控制不严格，偷取我个人笔记的里面记录，拿去某vx群倒卖，倒卖价格让人乍舌，500RMB/650RMB 就卖，所以决定公开这种方法。

![](https://mmbiz.qpic.cn/mmbiz_png/6XGOZPCymFcPVAaYE4LluV2ibtCW7YfZTITIg9Vvd1JN12jviaTNBtlkrtVCOyH3SiaG3BuX79rwJgjmCia69HL4DgocexbWX1jzbrb7MrKgFhI/640?wx_fmt=png&from=appmsg)

## 利用RPC添加计划任务

方法存在时效性，肯定会被安全厂商添加规则进行拦截，后续不会再发布任何关于核晶维权的绕过手法

要吃瓜的各位，请移步：

```
http://archive.today/2026.05.16-155204/https://mp.weixin.qq.com/s/zOMxAEtOLXT3zwUf_jx2gw
```

利用RPC接口添加计划任务，源项目被360核晶拦截，将localhost修改为0或者NULL，即可绕过核晶拦截

```
RpcStringBindingComposeW(RPC_UUID, (RPC_WSTR)L"ncacn_np", (RPC_WSTR)NULL, InterfaceAddress, NULL, &StringBinding);
```

### 项目地址

https://github.com/FemaleGhost/RPCAdd\_ScheduleTask

吃瓜内容已被恶意投诉无法查看，问题不大有pdf备份的瓜![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Watermelon.png)

⬇️⬇️详细文章在这里查看⬇️⬇️

[揭露某个偷资料的小偷](https://mp.weixin.qq.com/s?__biz=MzAxNzkyOTgxMw==&mid=2247495429&idx=1&sn=c7e2d78b7ea140e373f856d7b620e044&scene=21#wechat_redirect)

目前此人已经更换wx号和头像，望各位周知

此人估计还会继续举报，文章已经做了备份

https://archive.md/LFZN6

![](https://mmbiz.qpic.cn/mmbiz_png/6XGOZPCymFeGzDh5pElVb3ZE16hZPxDPxnzlDf48t9BYjJpyBpclic5I1O6zOkYkeOJ6n0gZjYIm45czQwflBKy3g3m17fDjgVmqwJuiabPDA/640?wx_fmt=png&from=appmsg)

吃瓜+工具项目地址可后台回复【RPC2026】自行获取

![图片](https://mmbiz.qpic.cn/mmbiz_png/7D2JPvxqDTER2M22xQ4L9ypTc8ycOSFz16CibJb5tZJAekLtXvhuAVPTwsIdyfGc6vViaCWib8HwdUeTs72DzN4ag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=4)

**网 安 考 证![图片](https://mmbiz.qpic.cn/mmbiz_png/7D2JPvxqDTER2M22xQ4L9ypTc8ycOSFz16CibJb5tZJAekLtXvhuAVPTwsIdyfGc6vViaCWib8HwdUeTs72DzN4ag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=6)**

需要考各类安全证书的可以扫码找我咨询，价格优惠、活动划算！

报名CISSP、CCSP、PTE、PTS、IRE、IRS、DSG、CCSK、CDSP、CZTP、ITIL4等符合活动标准的认证课程。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/6XGOZPCymFdPQq4TrtEjHHW85PMTtLbRGjib1es3srEX2MfHTfSWwUZmIjFB50SuTkacy9VjHzxL6nWnJ8z94gbXFLlo7d2CowhVP7WYbn1M/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1&random=0.06125543926007038&watermark=1&tp=webp#imgIndex=8)

![图片](https://mmbiz.qpic.cn/mmbiz_png/ib745vqibLBGIeAicnHiag9GCzTYjeicic5IWPqfyjLajDuwtJdNCAnCgcolqY8ROaE5CsEXR5zbjCU9aVl3WfkZpnDw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=9)

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

**走过路过的大佬们留个关注再走呗![图片](https://mmbiz.qpic.cn/mmbiz_png/7D2JPvxqDTGYu9nrfsXsv7ZrsqXibnKn0eCPo3D8HzHfmHdiar1tickAm9gP0XpiakaQhyB0ib0OBrNyp0Kpz59Umow/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&random=0.2553642180635751&tp=webp#imgIndex=10)**

**往期文章有彩蛋哦![图片](https://mmbiz.qpic.cn/mmbiz_png/7D2JPvxqDTGYu9nrfsXsv7ZrsqXibnKn06P5qlPDOibvAu5D68z2GBB98ATYhb2G1pMVA6iahuBuWOyicnUGQcWarg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&random=0.3569542558042562&tp=webp#imgIndex=12)**

预览时标签不可点

阅读原文

修改于

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