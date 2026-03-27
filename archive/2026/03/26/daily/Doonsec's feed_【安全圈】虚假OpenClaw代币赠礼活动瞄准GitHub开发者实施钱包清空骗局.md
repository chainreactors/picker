---
title: 【安全圈】虚假OpenClaw代币赠礼活动瞄准GitHub开发者实施钱包清空骗局
url: https://mp.weixin.qq.com/s/705rRHgsAmE1G0wzCkcApQ
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:29:43.127269
---

# 【安全圈】虚假OpenClaw代币赠礼活动瞄准GitHub开发者实施钱包清空骗局

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyHiaiaNPT5gxneJpIZzN4OuCUN9G25oCkYkibPecCXAp7RPb3K6J0bjtO8CQguAAzjvmI4iccD7BUv31icicEs7cWribueMe6GL7ZJKIE/0?wx_fmt=jpeg)

# 【安全圈】虚假OpenClaw代币赠礼活动瞄准GitHub开发者实施钱包清空骗局

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

AI钓鱼

参与OpenClaw项目的软件开发人员正成为一场旨在清空其数字钱包的危险钓鱼活动的最新目标。安全研究公司OX Security最新发现，攻击者利用GitHub自身通知系统，将毫无戒心的用户诱导至欺诈网站。

## **5000美元诱饵**

骗局始于GitHub平台，攻击者创建虚假账户开启新讨论帖。为扩大传播范围，他们在帖子中标记数十名真实开发者。这种标记机制会直接向受害者发送邮件或推送通知，使信息看起来像是日常工作中的正常内容。

在这些讨论帖中，诈骗者宣称特定开发者因贡献突出，被选中获得价值5000美元的$CLAW代币奖励。攻击者使用的典型话术包括："感谢您在GitHub的贡献。我们通过分析档案，选定您获得OpenClaw代币分配"。

根据OX Security团队向Hackread.com提供的研究报告，帖子中的链接（通常使用Google LinkShare短地址）会跳转至`token-claw.xyz`域名。该网站几乎完全克隆了官方OpenClaw页面。

![GitHub开发者遭遇5000美元OpenClaw加密货币赠礼骗局](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyFOFcWo6RtguCYhvibH2mRNbcEfVBic5cdtVH8FyXBQaAbribo6NMpYTUCaUORrNrwMSGA66tKD523wo5XibGweltpRpDVE2mYNicU0/640?wx_fmt=jpeg&from=appmsg)
钓鱼诱饵与恶意网站主页（图片来源：OX Security）

唯一显著区别是页面上的"连接钱包"按钮。研究人员发现该网站支持MetaMask、Trust Wallet、OKX和Bybit等主流钱包服务。一旦用户连接钱包试图领取奖励，攻击者就能清空其中所有资产。

![GitHub开发者遭遇5000美元OpenClaw加密货币赠礼骗局](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyFVOMm5RrILZ3menDTXAdNgw9V4PY8iaCddbdmmmVLTaicyib9ZAmW3ZMjKeYxqZy5Nso1Qc069OJ7tGYS7eI9dYKN9ib861xKP8Mc/640?wx_fmt=jpeg&from=appmsg)
钓鱼页面支持多种加密货币钱包（图片来源：OX Security）

## **隐匿行踪**

研究人员发现攻击者使用名为`eleven.js`的JavaScript文件承载恶意指令，其中包含专门设计的"核弹"函数——该功能会清除用户浏览器存储中的所有盗窃证据，阻碍后续犯罪追踪。这表明网络罪犯仍采用复杂手段掩盖行踪。

据分析，攻击者很可能通过筛查GitHub上关注或参与OpenClaw相关项目的用户来锁定目标。这种精准筛选使得标记行为更具迷惑性。

## **防护建议**

虽然目前尚未确认受害者，但攻击者上周已创建多个专用账户实施传播。值得注意的是，这些账户在活动启动数小时后即被删除以规避检测。研究人员还定位到用于接收赃款的特定钱包地址（`0x6981E9EA7023a8407E4B08ad97f186A5CBDaFCf5`）。

OX Security专家建议，任何可能接触过该网站的开发者应立即撤销钱包授权并屏蔽`token-claw.xyz`域名。常规安全原则是：对GitHub上任何宣称意外获奖的议题都应保持高度警惕。

***END***

阅读推荐

[【安全圈】上海警方深入推进“涉企网络谣言”打击整治：处置 270 余个违规账号，AI 洗稿编造车企销量下滑等行为被严惩](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075069&idx=1&sn=13b358d9c7991bf709ee2d720e484439&scene=21#wechat_redirect)

[【安全圈】AI 圈地震：月安装量约 9500 万次的 API 网关 LiteLLM 遭投毒](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075069&idx=2&sn=7ea915e24da062e25443aebe478f6c60&scene=21#wechat_redirect)

[【安全圈】HackerOne 披露员工数据泄露事件：第三方服务商 Navia 遭入侵](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075069&idx=3&sn=81030c6344d3eb99b31a0593ace75849&scene=21#wechat_redirect)

[【安全圈】马自达通报安全事件：员工和合作伙伴数据遭泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075041&idx=1&sn=ae9e793a53a8639e64c1a2ab362f1677&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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