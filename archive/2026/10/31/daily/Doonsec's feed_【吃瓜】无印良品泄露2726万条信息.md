---
title: 【吃瓜】无印良品泄露2726万条信息
url: https://mp.weixin.qq.com/s/yVsKKOt_bS7ZrLskS6-fLQ
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:18:09.329936
---

# 【吃瓜】无印良品泄露2726万条信息

# 【吃瓜】无印良品泄露2726万条信息

原创

泼猴
泼猴

表哥带我

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/UA4ABKCY6OyOoXBWReemeibD75IIothmT0iaUGdL3fvTcpS9l8YAryDTJsz9YHxOH9OgJIXa71GBliamUaSERxsicvoPBuHp7btbL3PGJ47UOj8/640?wx_fmt=webp&animated=1&from=appmsg)

**10 月 30 日，运营无印良品的良品计划对外发布通报，旗下日本区 MUJI APP 被非法访问，预估最多 2726万 条客户资料存在外泄**

MUJI 中国随后单独说明，国内版本 APP 和会员数据是独立服务器部署，不和日本这边互通，国内用户不受这次事件影响。泄露字段集中在邮箱、生日、性别，没有信用卡、住址、手机号这类高敏感内容，但已经足够支撑钓鱼定向投递。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UA4ABKCY6OwppU0ZL21Eh1j8A4wx3G7UScpDGvc9AdJUbvm15OY327OkGzqrvFXicqhEJhol2RkGwGAGwGtrLqXwyicVicJqib7hQr7Irwiau89c/640?wx_fmt=webp&from=appmsg)

# 受害者范围

受害对象为日本 MUJI APP 注册用户，就算是已经注销账号、取消订阅的用户信息也在风险池内。数据本身不算顶级敏感，但攻击者拿到邮箱 + 生日组合后，很容易针对性制作高仿钓鱼邮件，冒充 MUJI 官方发兑换券、订单通知、账号核验链接，诱导用户输入账号密码，再横向撞库其他平台账号。

# 攻击链

攻击者逆向 APP 接口，拿到后端 API 路径 → 找到鉴权或者数据查询接口漏洞，绕过身份校验批量拉取用户数据表 → 导出用户基础资料，用于后续钓鱼营销或者打包在黑市流通；厂商发现异常访问后，关停风险接口、修复漏洞，分批通知涉事用户。目前官方暂未披露具体是什么漏洞。

# 处置方案

1. 区分版本：国内 MUJI APP 用户不用恐慌，本次事件和国内会员库隔离；如果你同时注册过日版 MUJI 账号，重点盯好注册邮箱；
2. 收到 MUJI 标题的邮件、短信，凡是带链接让你登录、填验证码、解绑卡的，一律不要点，直接走 APP 内原生入口核对通知；
3. 该邮箱如果在别的平台复用了密码，尽快修改，开启二次验证，防止撞库；
4. 后续收到良品计划官方通知，按指引操作，不要相信主动找上门、自称 MUJI 客服的私聊消息。

```
# 检测该邮箱是否已经在公开泄露库中被标记（仅用于自己邮箱自查）
# 提示：不要把隐私邮箱提交到不知名第三方查询站点
# 推荐使用haveibeenpwned官方渠道自助核验
```

---

对此`你怎么看`在评论区发表你的意见吧

推荐阅读

[【吃瓜】冰箱也能被黑](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488197&idx=1&sn=4049fbf054b477a035f58eb50cd7803e&scene=21#wechat_redirect)

[【吃瓜】朝鲜黑客盗走交易所60亿美元](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488197&idx=2&sn=7213e22ab5b2ccd819fbb725858fdb64&scene=21#wechat_redirect)

[群晖NAS遭遇大规模勒索攻击](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488119&idx=1&sn=c2d86b543b1b4149e6fb734f15af6d8f&scene=21#wechat_redirect)

[PingCAP泄露10.6T数据](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488070&idx=2&sn=a20a3f36e61bd6f903e35773c30cdf0c&scene=21#wechat_redirect)

[【吃瓜】耐克盒马等账号发淫秽事件梳理](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247488016&idx=1&sn=c1af2be1807753b41b47919cb6ae56ae&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/pxKqYxJWy7PW1JR7KU1wRqvaNyp3ESh9m1FzIau0Uqvh7DDnryFJCzq3u7sc2J8wAtOffybvhBgkQW1CfJs9sg/0?wx_fmt=png)

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