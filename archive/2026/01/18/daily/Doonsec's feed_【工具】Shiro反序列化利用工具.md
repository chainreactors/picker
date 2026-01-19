---
title: 【工具】Shiro反序列化利用工具
url: https://mp.weixin.qq.com/s/XpaK0jTBaHVjz4PBz79NSw
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:37:14.914722
---

# 【工具】Shiro反序列化利用工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YxCBEqEyrw0A1MyNyQeapqOWy20UtricWFyK3zg6O86ticXJO3rWeOmxFLjhOy2FrcVAUL1iaia4qOn55cQmL4Viayg/0?wx_fmt=jpeg)

# 【工具】Shiro反序列化利用工具

原创

track
track

泷羽Sec-track

![]()

在小说阅读器中沉浸阅读

> 声明！本文章所有的工具分享仅仅只是供大家学习交流为主，切勿用于非法用途，如有任何触犯法律的行为，均与本人及团队无关！！！

**往期推荐：**

**[【工具】Sqlmap中文汉化版](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489242&idx=1&sn=67c1cac7a017a4f1c57e97fc415ef6fd&scene=21#wechat_redirect)**

**[若依(RuoYi)框架漏洞战争手册](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489224&idx=1&sn=a59ca4e14728e9a03b38223b57f39447&scene=21#wechat_redirect)**

**[【工具】多平台GUI图形化资产测绘工具，支持一键导出](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489051&idx=1&sn=c1dcbe17078b6ed0bd16e7d061bae691&scene=21#wechat_redirect)**

**[【SRC】金融场景挖掘技巧](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247488878&idx=1&sn=2bffe97dce5fc3ceedafee8e9b9bbe31&scene=21#wechat_redirect)**

**[一款功能强大的红蓝对抗工具Potato Tool-具备免杀,提权,漏扫,内存马生成,ai分析,溯源等高效的网络安全综合工具](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247485262&idx=1&sn=18ac6ffb1e0bd3a02f80116938ec03e4&scene=21#wechat_redirect)**

## 工具介绍

shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马）

Apache Shiro 550 反序列化漏洞（CVE 相关）源于其对 rememberMe Cookie 的不安全处理，该 Cookie 采用 AES 加密但存在默认密钥，攻击者可利用已知密钥构造恶意序列化数据，通过反序列化执行任意代码，ShiroAttack2 工具则针对该漏洞提供了密钥爆破、利用链构造等快速检测与利用能力，可验证目标是否存在该漏洞并实现漏洞利用

## 工具获取

github

```
https://github.com/SummerSec/ShiroAttack2
```

或在公众号后台回复**26118**即可获取

## 工具特点

如下

* javafx
* 处理没有第三方依赖的情况
* 支持多版本CommonsBeanutils的gadget
* 支持内存马
* 采用直接回显执行命令
* 添加了更多的CommonsBeanutils版本gadget
* 支持修改rememberMe关键词
* 支持直接爆破利用gadget和key
* 支持代理
* 添加修改shirokey功能（使用内存马的方式）**可能导致业务异常**
* 支持内存马小马
* 添加DFS算法回显（AllECHO）
* 支持自定义请求头，格式：abc:123&&&test:123

## 使用演示

检测key

![image-20260118174753090](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0A1MyNyQeapqOWy20UtricWP98giclmriawYCjJzykx5JicR1PjIdRFWr6J4QfrEoK1FbmShqvJFVD5w/640?wx_fmt=png&from=appmsg)

image-20260118174753090

爆破利用链

![image-20260118174831868](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0A1MyNyQeapqOWy20UtricWJiaCkf6o4zvCFXx4jVMNyaJJIOofnutSHN17oUlzFH1dNrllLIyW4fA/640?wx_fmt=png&from=appmsg)

image-20260118174831868

找到key和利用链，之后就可以命令执行了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0A1MyNyQeapqOWy20UtricWeXEyYHLbVrvPuRMzGZhVg0HCPZW1OHdKltezl4VSiatoALZbocfSzmw/640?wx_fmt=png&from=appmsg)

## 知识星球

**可以加入我们的知识星球，包含cs二开，甲壳虫，渗透工具，SRC案例分享，POC工具等，还有很多src挖掘资料包**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0A1MyNyQeapqOWy20UtricWickIkkgL1dp6qcCBRWCdWSwEgHjhpDJPtNUWEOHqMJhJXDs5dAPZRRQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw0A1MyNyQeapqOWy20UtricWDokPKvTLANVJMZd4muw3FfWfJh5URxImOmNXv39RtCEAOqagD3ubXw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YxCBEqEyrw0A1MyNyQeapqOWy20UtricWYs3TzIWg4njJQ1hiafeN3iazOLYqM5wr4m5mUEwYOFAwmichMLP38YZFw/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2ob06EicM7DDKBlMjOVw0mmNOVKLafx8sRvQbcCQ91ACGG0DWnFb85TOIUSQBgWWmibMSa9KiaEfQXA/0?wx_fmt=png)

泷羽Sec-track

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2ob06EicM7DDKBlMjOVw0mmNOVKLafx8sRvQbcCQ91ACGG0DWnFb85TOIUSQBgWWmibMSa9KiaEfQXA/0?wx_fmt=png)

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