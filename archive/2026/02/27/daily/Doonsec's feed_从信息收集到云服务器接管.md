---
title: 从信息收集到云服务器接管
url: https://mp.weixin.qq.com/s/Yl5zrM26v3-tOU3E7qrSHA
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:50:37.919417
---

# 从信息收集到云服务器接管

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/16lHuWzRRduMsp5PMTdqzUIh1102f48E1iaaRho7uFdRMF3FLVARsuP9keibYEibsUeFrtOb0Rgw4rVc3p1DNPeg9R7yVgfCobKicamgStjAVtQ/0?wx_fmt=jpeg)

# 从信息收集到云服务器接管

原创

private null
private null

轩公子谈技术

![]()

在小说阅读器中沉浸阅读

开工大吉！新年第一天上班，手气就爆棚——直接拿了个 shell！这哪是普通的反弹，分明是新年运气的强势反弹啊！

看来今年的红队之路注定是畅通无阻，渗透测试一测一个准，漏洞一挖一个稳。

希望接下来的每一天，都能像今天一样顺利拿下目标，root 权限到手，项目满分过！

祝各位同行也开工大吉，脚本跑得快，权限拿得稳，新年一起冲鸭！

首先，映入眼前的，是一号目标，登录页面，登录页面的测试思路，可还记否？

比如扫目录，敏感文件，查看接口，隐藏参数，上传点，未授权点，oss密钥，

未失效 token，加密 key，测试账号，用户名枚举，密码爆破，验证码识别，

默认密码，万能密码（注入），xss，log4j2，jndi，fastjson，401 to 200

，jwt 爆破，注册覆盖，密码找回，sso/oauth等等

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdv9Ry0ynNuk75E8XP4kj62E91VmHAibUAKH9PiaY945ticia8uNWKfUy2y6iaqJ9XuJPMyKDM8Im6ZZwOZameblxAk8HibmaMcPd2ND0/640?wx_fmt=png)

群友眼睛过于毒辣，之前的马虎，都被扒个精光，所以这个页面码死，站点是 tp 框架，顾名思义，掏出一件 rce 工具扫扫看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdsThOoNWTp9ow90vhjJXcOCN8XzibwyjFKMyQIewdVnDiaqALae5ib7OQuHI97TiaibqMeD5oLEaRYWojnR6ibBfEoibkNghXnHA5mT28/640?wx_fmt=png)

那包不可能有的

hunter 搜一下子域

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRds5ty9F1xaVxMia60LibDLMbqTscXOnplMjMFNjERMLPkp6ZR9yTjq7I0Iyc5a09XWI4Gv2c1xlRkFzRR5GJRvaULF8KxZfcCLOE/640?wx_fmt=png)

又发现一个后台，但是这个没验证码，就可以进行爆破了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdtkWoS2laqItMS3ghNleHg2uKibqROVTLv4mOvny2TBTvYgq4iaFWUsYH0icPCa2gkVXYbdlEialiczP3cjlLLrBzgwAEt5qy8ANY58/640?wx_fmt=png)

也算运气不错，弱口令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdvbhyDic9ejVnFcUb6mNjqnrWOxm8cYGMFlNlMGcpuO3pnOaFnicLFMzKSJR0VcJlu32UiadbfDR6NiavMKF6vvZ9dzLy6wtgm0hYU/640?wx_fmt=png)

翻吧翻吧发现了阿里云 oss

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdsHSeyicianxWI8oibfZZwYlbjXSfIPzsibv0iaeKa9uCJnRymHsjJ5iaibMkSXibTeOAV2kEb4xhLKkiabpUhVB76MChswGWquB7JLfYb8/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdsvF3Vg5zSJLrxhkpGNquia4glgCrjGBoROOld6RsJ6s1pLKpFcrWKnbz7bx02xTJ8uGiaVrxSlku43TuGL9VzhXmX86VNzvWiavM/640?wx_fmt=png)

转用 cf，扩大危害程度

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRduNfU5kiaESFf8ZmrOFXSiaZRutA0g6rX4t0o97MDDyOKt8j7hvYdwUNSSISpSBhrqoia26xel4Fzm3SQaKmRLjOuEyyOfvc7QU7c/640?wx_fmt=png)

公网IP 和 Hunter 对应的 ip 一模一样，也就是说 直接拿下了 18 个网站

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdvDOlNzf9oRSDf3gaXBPCfibqJSolpSUcw5zywNO5OOFCicQAuGHtOQJUbicBOMNmBqVSibiabsoJDMaWfkMRVEJ18tecvDorlTC0JY/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdsklniaYw3HmkyHUuzt6LU8dr8HTN0W0CC6iaicz74SZtdTtNtibwXJ9A9YvlibQI0T5NXcA0VIVG2s1XIp1icXfPfJEYCLEGTtJkt8g/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BAby4Fk1HQZCDnChGupgZyfRK8Bs8twy3rbw6gic8GAoiaqoIIVarKvqMgQ1vj4t0UyMNdvaIHmTE2XgzeSFn32Q/0?wx_fmt=png)

轩公子谈技术

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BAby4Fk1HQZCDnChGupgZyfRK8Bs8twy3rbw6gic8GAoiaqoIIVarKvqMgQ1vj4t0UyMNdvaIHmTE2XgzeSFn32Q/0?wx_fmt=png)

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