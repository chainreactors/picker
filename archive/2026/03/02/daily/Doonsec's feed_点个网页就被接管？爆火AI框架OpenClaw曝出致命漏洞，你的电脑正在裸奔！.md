---
title: 点个网页就被接管？爆火AI框架OpenClaw曝出致命漏洞，你的电脑正在裸奔！
url: https://mp.weixin.qq.com/s/LHZPU7pujhzN_Ir-qcvCpw
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:07:22.128362
---

# 点个网页就被接管？爆火AI框架OpenClaw曝出致命漏洞，你的电脑正在裸奔！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicLZG4EN6QZ7jcQhekE0SYdE3pWSIhxBLzrWIOicZaQg7W62suKZDlTaDjMyzXv0gsSWFCvqbhvQzHKiaPojUvRVSB3A6W01iaRSyY/0?wx_fmt=jpeg)

# 点个网页就被接管？爆火AI框架OpenClaw曝出致命漏洞，你的电脑正在裸奔！

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器中沉浸阅读

最近，一款号称“本地AI操作系统”的开源框架OpenClaw，因为一个叫ClawJacked的高危漏洞，被推上了风口浪尖。

安全团队Oasis Security披露，黑客只要诱导你点进一个恶意网页，就能悄无声息地接管你本地运行的AI代理，甚至拿到你电脑的最高权限。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicIsXBhw5JvtDhyJIMjrNQllnr0LlxgMCnuKATZO2YibFlBg6SWVl6cWAMkbgdy1K5emhExXtPMmca5YPa1N9zo4OCrv8U6762eM/640?wx_fmt=jpeg)

这可不是普通的漏洞，而是一次彻头彻尾的架构级安全失败。

一、先搞清楚：OpenClaw到底是什么？

OpenClaw是今年初在开发者圈里火起来的一个开源AI智能体框架，核心卖点是“本地自托管”和“主动干活”。

和我们平时用的云端AI助手不一样，它直接跑在你自己的电脑上，能把大模型的“思考”和本地系统的“执行”能力打通。它不只是回答问题，还能直接操作文件、跑Shell命令、调用各种API，被很多人当成了自己的“数字管家”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicJ1RUTOp6Y2zPib7GMdToFbG25NBaV1ZiaWdPbXO9licRhia2nC3K0HiaHn7OcfOsWLtpHmQYDibrtiavzJjVIOU9lyVmJSKWYSCpWtJA/640?wx_fmt=jpeg)

正因为方便好用，短短几个月就有几十万用户用上了它，从个人开发者到互联网大厂的运维团队，都在用它提效。

二、ClawJacked漏洞：点个网页，你的AI就被“劫持”了

ClawJacked（CVE-2026-25253）是个CVSS评分8.8的高危漏洞，攻击方式简单到离谱，危害却大到吓人。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicIbQLY8icmxYsias5nSJCPrd5x5Z9iauy9V0JiciaoK5pErCTShGNSdyfX1zyUNp8dQcNBTLVQr55u8gvtoMzm0wx0AmspMZSZVPGYw/640?wx_fmt=jpeg)

1. 漏洞本质：信任本地，却引狼入室

问题出在OpenClaw的设计上：

 它的网关服务默认绑定在 localhost ，还开了个WebSocket接口。

 浏览器的同源策略本来会阻止跨域请求，但对 localhost 的WebSocket连接却“网开一面”。

这就给了黑客可乘之机：你在浏览器里访问一个恶意网站，网站里的JS代码就能在你完全没察觉的情况下，通过WebSocket连到你本地的OpenClaw网关。

2. 攻击过程：三步接管你的电脑

1. 诱导访问：黑客通过钓鱼邮件、社交平台或者恶意广告，骗你点进一个精心做的恶意网页。
2. 静默连接：恶意网页里的脚本自动连到 localhost 的OpenClaw服务，尝试破解或偷认证令牌。
3. 远程接管：一旦认证成功，黑客就能完全控制你的AI代理，接着执行任意Shell命令、读走你的API密钥和SSH私钥，甚至直接接管整台电脑。

整个过程不需要你点任何确认，也不会弹出安全警告，真正做到了“零点击”攻击。

三、影响有多大？数十万开发者的电脑正在裸奔

据安全机构统计，全球已经有超过3万个OpenClaw实例被攻陷。黑客用这些被劫持的AI代理，大规模偷API Key、加密货币钱包信息，还在分发恶意软件。

受影响的版本是2026年1月29日之前的所有OpenClaw版本。如果你还在用旧版本，又没及时升级，那你的电脑很可能已经成了黑客的“肉鸡”。

四、现在就做：你必须立刻采取的行动

如果你或你的团队在用OpenClaw，一定要在72小时内完成这些事：

1. 马上升级到安全版本

 升级到 v2026.1.29 或更高版本，这是官方修复了ClawJacked的首个安全版。
 Docker用户可以直接跑：

bash
docker pull openclaw/openclaw:latest
docker-compose down && docker-compose up -d

2. 把安全配置拉满

 关掉无认证模式：新版本已经永久移除了无认证模式，一定要配置强密码或API Token认证。

 别把服务暴露到公网：确保网关只绑定 127.0.0.1 ，如果需要远程访问，用SSH隧道或VPN这种安全方式。

 封掉高危端口：在防火墙里全局封禁OpenClaw默认的 18789 端口，直接切断攻击入口。

3. 检查并重置所有敏感信息

 翻一遍本地配置文件，确认认证令牌有没有泄露。

 立刻重置所有相关的API密钥、SSH私钥和账号密码。
 扫描并删掉所有可疑的第三方技能和插件。

五、AI Agent时代，我们的安全底线在哪？

OpenClaw这次“爆雷”，给所有人敲了个警钟。当AI Agent从“云端给建议”变成“本地直接执行”，我们面对的安全挑战，是前所未有的。

 本地执行 = 本地风险：AI代理能直接操控系统，一旦被攻破，后果比普通信息泄露严重得多。

 开源 ≠ 安全：开源框架透明是优势，但漏洞也会被更快发现和利用。用得爽的同时，安全责任不能丢。

 架构设计才是安全的根：ClawJacked本质上是架构设计的失败，它提醒我们，做下一代AI系统，安全必须是首要考虑，而不是事后补救。

AI技术发展得太快了。

作为开发者，我们在拥抱新技术的时候，一定要保持警惕。赶紧检查一下OpenClaw部署，该升级升级，该加固加固，别让你的“数字管家”，变成黑客的“敲门砖”。

\*作者：hacking。编辑：黑白红。文章数据来自网络，经过大模型优化，内容或图片如果存有侵权，请留言联系我们，我们会第一时间进行处理。

**往期****相关****回顾**

[美以对伊朗战争中的“网络战”：22分钟掐断国家“喉舌”，18小时内斩首哈梅内伊](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247552148&idx=1&sn=8eccce92eae20393c407385599871db9&scene=21#wechat_redirect)

[网安寒冬！启明星辰2025亏6.1-5.4亿](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247550682&idx=2&sn=de7b180e7bb9ca00217fd568e326605d&scene=21#wechat_redirect)

[2026最值得去的大厂！ 排名超真实](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247550643&idx=1&sn=f220cc2ecdf5550834783541e733c536&scene=21#wechat_redirect)

[度假变噩梦！徐泽伟因美国网络入侵指控在意大利被扣，妻子：老人孩子还能等多久？](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247550585&idx=1&sn=d393ee66a57f3a9b6d2895a3e3b9ed9d&scene=21#wechat_redirect)

[被指控网络入侵：中国徐泽伟在意大利被扣押的210天、或被引渡美国](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247550577&idx=1&sn=34365a236610b5680df0781a39f0e3d7&scene=21#wechat_redirect)

[突发！35家中企业遭美国德州封杀（附名单）](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247550568&idx=1&sn=538294b059cbb618e6218f592a2fd3c2&scene=21#wechat_redirect)

[惊！2025网安公司亏损榜：奇安信巨亏超11亿，近八成企业陷亏损](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247550853&idx=1&sn=8cb2fcde8fb8bd15680ce14855375541&scene=21#wechat_redirect)

[字节海外中国籍员工集体破防](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247551103&idx=1&sn=7b3d78f68c8e49684ad2c0e2d5e86291&scene=21#wechat_redirect)

[年前裁员：某手S+功臣跨年被裁，大厂最真实的血色年终](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247551502&idx=1&sn=ad9bd0637ddba3b9a012b7e354f3d603&scene=21#wechat_redirect)

[2025字节跳动各部门年终奖汇总-网版](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247551512&idx=1&sn=a3fe7c595c04afe4548317576db326f6&scene=21#wechat_redirect)

[2025【腾讯】各部门年终奖汇总（已到账）](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247551574&idx=1&sn=80e8023a0ad7593623dd6b2286246ef1&scene=21#wechat_redirect)

[2025【京东】各部门年终奖汇总（已开奖）](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247551574&idx=2&sn=11d8db5792dc8214b2f1b6c448308d1b&scene=21#wechat_redirect)

[字节年薪40万，过年被父母劝回老家考公：大厂不如县城月薪3500](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247551656&idx=1&sn=864677aeaf4bdb8f647f48a9b096d643&scene=21#wechat_redirect)

预览时标签不可点

内容含AI生成图片

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

Hacking黑白红

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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