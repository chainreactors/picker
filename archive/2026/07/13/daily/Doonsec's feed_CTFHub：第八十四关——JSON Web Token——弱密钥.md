---
title: CTFHub：第八十四关——JSON Web Token——弱密钥
url: https://mp.weixin.qq.com/s/aNjo_zzT0XBWM8sbxSfMEQ
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:43:44.638136
---

# CTFHub：第八十四关——JSON Web Token——弱密钥

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TkbqemjbpIqxxnMJBFEJOhTp1hibZQuVjBD4ibb6lZ61q1z5l5sTavemtH3xicTATVm6JHBSNcsAVuBSgA22g76GictGGcLtNafxYtOIPB7L6vY/0?wx_fmt=jpeg)

# CTFHub：第八十四关——JSON Web Token——弱密钥

原创

君陌社区
君陌社区

君陌社区渗透安全笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

CTFHub网址:【https://www.ctfhub.com/#/index】

登录账号
点击技能树

选择“web进阶- JSON Web Token-弱密钥”开启题目

题目描述: 如果JWT采用对称加密算法，并且密钥的强度较弱的话，攻击者可以直接通过蛮力攻击方式来破解密钥。尝试获取flag

漏洞原理:服务器使用弱密钥对JWT进行HMAC签名，攻击者可通过暴力破解获取该密钥，从而随意篡改令牌载荷并重新签名，实现身份伪造与权限绕过。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIqb6R9L9kjmI0SKg4bToD5r2GtYxRicdhMiaIDgnLjeEfthSV3qxrx91ZXOBWUEKf1X9tQyb1zPVicyjp9LzDUXLCVyfYgPsD2h14/640?wx_fmt=png)

单击打开链接进入靶场实战练习环境，在登录页面输入用户名admin和随机密码

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIrO7cZyrmpc5Y0YemAhhwpA1RnwJlz5gcVKZuAdPafficd1l3Y15loKLUOnJnsutEbZIlEBh9jJ47zGECtQ7vFyTyhz1ibn85UnQ/640?wx_fmt=png)

登陆后页面出现的文字，表示只有管理员才能获得flag数据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIpGmbROOvQfPRjyZEj4u3VJaxHuPWgk7IcKdjUtlCFWribKlYuuy6E5IygMZrM05a8F5YjJd9I5ne7bzAXqbjj4TwaXkkpqmFPw/640?wx_fmt=png)

打开Yakit工具截获数据包复制其中的token字段内容

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIpcxzhApyrEpHZpBlXBicC9QhHEibVI1VXazqPNhnpBPjrSYib25eKhpNgG5d4GGadBYQHbM6159biaTIQx2VJGhROiaYvSAiaErTAic4/640?wx_fmt=png)

打开kali系统，输入

```
./jwtcrack <你复制的JWT令牌>
```

运行后工具已经帮我们爆破出了弱密钥为etjx

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIpFJwoiabsgoHNdJrzpsHZThXGaVwC0Tm7INg58BjPlmia5UUoic9ENbaPXHYIONEKIeSQg0r6W7RZ5ccTE70Feiah2Q18pMt9jItk/640?wx_fmt=png)

访问JWT官网 https://jwt.io

粘贴JWT令牌到Encoded Token输入框

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIqazzyGTuriceB1XI6B6Qa0bFZquBY7fYibHkVPcfL1otAVZdo7ic7WDmRkCvyjYdnCS3wFDFlw5ica5qqgxIZqQYKk9USrmiaHoTMk/640?wx_fmt=png)

选择JWT Encoder进入JWT编码器

找到role字段，将其值修改为admin

在页面底部的“JWT Signature Verification”部分，输入爆破出的弱密钥

生成了一个新的JWT令牌

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIpDd0Sx2ovhiaqNDhicsMuMPIyGdPYE7HtXzat73B4kauYtktIGRWxNBjPJjKQHYA4tkRuHMfVHcY3jicU0BkeTYDz5P2dI42amNs/640?wx_fmt=png)

将新的JWT令牌输入数据包中的token字段，构建成一个新的而数据包发送，从返回的数据中找到flag数据

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIrWAAPgxuuItem7QnQ6t3STdKI38wvKfibibf3kO3GmAMNoOyAyQrG6TpNtEBPS4oTM1xJG85XiakajoRV3z9y6AibST8XQ2EoxkAU/640?wx_fmt=png)

提交flag数据完成靶场实战练习

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIr9swfVUXnQYZqRRCacvjBa2WXxXoWiaTIuU2pBdUcZEWXFvkSu6O0KSKaZQOdibwO5HMM9N70ssdibjObf4WEYKJrfo6eCkMGNqs/640?wx_fmt=png)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/csuE9m26HkI8taS28gIOWsc8KaibxmZ9HDovmlvGsicEnJuSw0Ricdq3KibbTUnRicEO0NohDyczWdgJBOe3RWF1tQw/0?wx_fmt=png)

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