---
title: 深度复盘单一企业SRC全维度挖洞过程（中）
url: https://mp.weixin.qq.com/s/1t4mI16YmbXMukP0TQL5fw
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:38:28.659378
---

# 深度复盘单一企业SRC全维度挖洞过程（中）

# 深度复盘单一企业SRC全维度挖洞过程（中）

youki
youki

C4安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

从点到面的挖掘过程

起初登录界面无法暴力破解，注册流程也需要人工审核。

翻阅帮助手册摸清账号命名规则，账号为机构简称搭配学号，默认密码和账号一致。**登录需要携带凭证，密码经过Base64 编码。**

```
先后搭建学生、教师两套字典爆破，学生账号无果，爆破教师账号时多次出现 500 报错，最终成功跑出两个高权限教师账号。平台按学校做好隔离，不同院校数据互不互通。
```

**获取多个测试账号**
登录界面如下，如图是无法进行爆破密码的

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9COic3Bsx6q96obsicrOTr03Ob7XDcUfaUI2ugYcTmhnjiah8jK92SXFv4gMA7hqwlpeV7ASYReZQus2Q3OcYfoJfEiaibf939lGsvsI/640?wx_fmt=png&from=appmsg)
正常注册也是需要审核
![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CNJEnibzjlrBnicZmOfCZFZezaTsC5gajCPTYeGne1yETn5FI5V8smWX90sPxvPwojH0eVXdmrKgrkfBgo06pfD7j8Ln5ckddjL8/640?wx_fmt=png&from=appmsg)
好在还有一个帮助页面，有个使用手册
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CMcKLdvePsljYwNpHRVh5UhiaCrkLyickVQyy275UHN0l5Nhey8xGR2Wod6rLfVLibRJDBYfbeLKPW4UDlwJGwPkVGABDAm5nkUdc/640?wx_fmt=png&from=appmsg)
手册就有几个非常关键的信息，给出了演示环境的账号格式，真实的账号格式为**简称＋学号**，简称可以直接登录页面查询，默认密码即为账号，学号的格式基本也是固定的，很容易就找到
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CNC62aVxJCwKUZsa90xeftyEicgia5OmbGxZw0YAiaOgJUJkt2kAMseQW5cP8Ihocs2L3bGQRfjBKlcQaSPD7Nbr2OFSibdvCjb6Ag/640?wx_fmt=png&from=appmsg)回到登录页面看下流程，这里有个获取类似于凭证的请求包
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CMjtdPemNzbTEs2k5Hbj68fsg4icgVv4XLpGeuIG9icdvibWKpRTWqbNWgUcN69EicJxCqwXs8WeRfW8B3MExVKTMWebcrT0BA23c4/640?wx_fmt=png&from=appmsg)
最后一个数据包则带着这个凭证还有账号密码去请求，密码一眼就能看出来是**base64编码**，这就可以尝试爆破测试账号

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9COYqiazx5sLBFGFBQknQbn8XWRmlMvXZdExZrhDpC1uynWFYQ7CNJC5TDEAQBuXO06sqiaRFMlvSr5neFFS2aLotiaQDl5VFicEjA8/640?wx_fmt=png&from=appmsg)
这里爆破了400个账号是没有爆破成功，在刚刚学生使用手册的地方还有一个教师手册

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9COxwVUVlcS2soicD1Kewgic1L8o9Xr3Z8mvObia80icvtOcd32qQVk89Co9Ofuh3hgU3LEhibJTSN9ASVGMNRa5rLpnI20xnvFzPyO8/640?wx_fmt=png&from=appmsg)
继续构造字典爆破一波，这里爆破到200多之后都是500服务器错误了，不过好在成功爆出来两

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPEyVPo7FibicTkYJmupLzaBqfdM6Ef8IEmgiabJjGGy0cfE4A1w151j33j9rhgUJiaWmjOz5GEL3BcdtibSvibCr0VHmvqhVf4jdiaNc/640?wx_fmt=png&from=appmsg)
接下来就是**开盲盒时间**，使用上面账号登录直接就是金色传说，权限很高的教师账号
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CN5MsicHtyUibdrPsFG6ibf4uSZSqF8vUWO6uVNJEjvvPUicy94Akrggx8mSMmaM2UFWGBNrbarlTFULyxKCV1ZSQwVnH9iclhr2mpQ/640?wx_fmt=png&from=appmsg)
这里教师账号管理功能只有两个账号，估计往上还有个**超管的权限**

学生账号就比较多了，一共**1w多个**，均为测试大学下的**测试账号**，这里是看不到其他真实学校的账号的，估计学校和学校之间做了很明确的隔离限制

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CO7d7OsyzNdUuH4IlnN2znFud7kVKEmFqBkIKpzbX1D6OpnLKh03SrUibWvJAs01MjaGibg4xcPiajt6l9zDPRVXvuAt7uzFQWMys/640?wx_fmt=png&from=appmsg)

任意账号接管

**平台个人中心支持微信绑定登录，刷新页面的数据包依靠用户 ID 生成微信绑定链接。**

```
ID 无法直接遍历，但考试、作业等功能接口会泄露各类账号 ID。

拿到目标 ID 替换请求参数，即可生成他人的微信绑定地址。

扫码完成绑定后清理缓存，就能用微信登录接管账号。

学生端接口可轻易拿到教师 ID，低权限账号也能拿下高权限账户，风险覆盖面广。
```

右上角个人设置功能，有个绑定微信的功能

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9COibxcPiakA7b1VQv72zJwEK127YlPSAy91xWfF8FrvWBffKawIlu01YwQRb1t2sP4nyyc7UMBDP3kg77ALGfgX0W8fvAZicvY5K4/640?wx_fmt=png&from=appmsg)
这里**F5刷新**一下，会加载如下数据包，会根据id值返回一个绑定微信到此账号的链接，因为是可以使用微信直接登录此平台的，只要获取到目标账号id值就可以**把我的微信尝试绑定到目标账号**上，虽然是不可遍历的，但是有很多途径可以获取到这个id值
![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPhQtIMEoltMRib0HAX6CHThggP9C9kFfTSicTlUSogItKm69zJX56yTkEy1Wj9GGN4AickIbpQI27padJKq5wQZvYqQjkIKUpABk/640?wx_fmt=png&from=appmsg)
在一个考试的系统中，有个新建题库功能
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CM1WMfAC0XKniaHpehHPgicbS1ESLxQxj8VCQ3LvzBBY1nxU1pD44Yn46yE7tQLYSPgIFF3zvNX6Wfvduf1dHsEPOAzJ7nJKHSCE/640?wx_fmt=png&from=appmsg)
过程中可以选择显示全部教学负责人
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CMH9OJADHOhINe2QWiaLcFl55UDk4SWAXialq3mPfr3iadgXGyicmdIZwXeUZPbF12hptiaS6HcgrwuYnlAj9iceh9QNA2hOdyUU73ps/640?wx_fmt=png&from=appmsg)
开启抓包，返回了目标id
![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9COFYuAfCxySgskUMXnB3sEcEcFz23g2ibDogwS62oZRVDLwP5kqjpiajiaJ9FXQ0hWkz3LYq9kEHmxoO2cLo76MpELHVkB5lWKFyY/640?wx_fmt=png&from=appmsg)
在一开始数据包直接替换这个id即可
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CNW1h9LbSunUL4onPBJ7OOCLVz7W8kiaqpjzcMzkICGHkOf50QRAs9XYzP7ibm5Db78AzeyYqB38QTO7j12H8MHC1dbb313zNngo/640?wx_fmt=png&from=appmsg)
打开访问，然后拿自己微信扫一扫提示微信号绑定成功
![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CMSicyktAZGAqbASboh6gbcQkqzKZbHbDtseAeyiaHsf0ftib2FUvEyyVFSqnic5a21fgSicibP7icArwuzcz4pLycEZUxqyG2vDoRmiaA/640?wx_fmt=png&from=appmsg)
这里需要先清除下浏览器缓存，然后拿这个微信扫码登录，成功接管了其他账号
![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CMInhmrcZSXYY4Xib40BdTWqVm9T3VgDLp3B25ibm5XHicEXWVzKfaL58B2IZO6PmHUH7d8yzJFZxr0tDHn8Zdp567CeCR2APGztU/640?wx_fmt=png&from=appmsg)

---

内部社区已有770+师傅加入

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CMSHBvYMO76JqnXwWAE7uS87f4MXPBia5BXSKiapQevic1Yt2cTYxiaRMUOnicCoerjrwf5aGFYosuicQy6OsX2VS5nu5kib5qPWh0e1M/640?wx_fmt=png&from=appmsg)
加入价格已涨价至**79.9**，后续人数增加还会上涨价格！先到先得！

**最新漏洞挖掘工具、AI工具第一时间分享！**
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CN5PDQib1SoicbAFDHz6cosm1A2zSQb7iavgzq13zgX1L3vPpoQHHib2licIjxovdaiaQ4EWebOAc1v0l5oKqpnkuknEO6ytXThbZLQ8/640?wx_fmt=png&from=appmsg)

**漏洞挖掘快人一步！**

内容框架（持续新增中）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPwGujPBmYz9ibfgs7wRQ5S7Ik5qNukbibPa4uxhB9ksVnCia3m2fYM8J5IibY9IyfeKLmgYiadaHbIp5bJGdvdr7rKk2JPebcaSNUo/640?wx_fmt=png&from=appmsg)

**欢迎各位小伙伴加入了圈子，有意向的师傅们可以扫码加入我们，共同进步。**

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9COibhcJn5j6w0hR19oBv9Jichwlf4FdITiaU9YxWwyFVptQH1TzTeJ1ZE2JbleXmbtBa0zVHkF0IDr54U6Y8I7vj6YhUHRoibReobY/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过