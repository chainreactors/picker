---
title: “龙虾”卸载指南，来了！
url: https://mp.weixin.qq.com/s/NMNOiq_GJmlENCh7cl1vaw
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:24:51.854759
---

# “龙虾”卸载指南，来了！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/lYWDmickZ2mxAR18r5jZ1heHOA9VOPv3cKC6grvNaLIvlp8dPF9vus4Iicq2BKHVtcLgHHQKotdEfU6hNsqhY0eOQxj7gOMpVaK1sBbnAILAE/0?wx_fmt=jpeg)

# “龙虾”卸载指南，来了！

数世咨询

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/pLQo55EgAVVtWaico4vsuPdOibLTiavlgoqU5SGxwU9V8XnvTIfg6PzHSibTzxgPhOqiaEeEMa0MlBqLiarfpkSTFia8w/640?wx_fmt=jpeg#imgIndex=0)

近期，开源AI智能体OpenClaw（俗称“龙虾”）火了，AI“养龙虾”成为全网热点，[多地宣布下场“养龙虾”](https://mp.weixin.qq.com/s?__biz=MTI0MDU3NDYwMQ==&mid=2657899086&idx=1&sn=c865e7b26a701173d1b72b653ccdc518&scene=21#wechat_redirect)。

“龙虾”通过整合调用通信软件和大语言模型，在用户电脑上自主执行文件管理、邮件收发、数据处理等复杂任务。然而，“养龙虾”背后，隐患和风险也很大。有网友反馈，“养龙虾”过程中，出现了乱删内容、隐私泄露、乱花钱等问题——

* 近日，Meta超级智能实验室AI对齐与安全总监Summer Yue遭遇OpenClaw失控事件，个人邮箱中200多封邮件被删除；
* 有人称，在网店购买了OpenClaw远程安装服务，刚装上5分钟后，就接到反诈中心电话，吓出了一身冷汗；
* 深圳一名程序员分享在安装OpenClaw的第三天，因API（调用外部服务应用程序编程接口）密钥被盗，在凌晨收到了高达1.2万元的Token（即通常所说的词元，它是处理文本的最小数据单元）账单。

官方发布风险提示

近日，工信部、国家互联网应急中心先后发布风险提示，围绕OpenClaw可能存在的一系列安全风险，提醒用户审慎使用。（[审慎使用“龙虾”等智能体！这六项提醒务必知悉](https://mp.weixin.qq.com/s?__biz=MTI0MDU3NDYwMQ==&mid=2657898981&idx=1&sn=6523b5580f0cc785611246043c371d10&scene=21#wechat_redirect)）

目前，OpenClaw智能体通过更新到官方最新版本，确实能修复已知安全漏洞，但并不意味着完全消除安全风险。因为将实例暴露于互联网、使用管理员权限、明文存储密钥等配置问题，即使升级到最新版本，如果不采取针对性的防范措施，依然存在被攻击风险。

无需懂代码

“龙虾”官方卸载指南

目前，有些已经安装OpenClaw的人，打算将其卸载，网上也出现不少卸载教程。

3月10日，某交易平台上已出现代卸载OpenClaw的服务。一名IP地址显示在上海的商家报价，上门卸载OpenClaw收费299元（仅限在上海），远程卸载OpenClaw收费199元，并称“安全彻底，无残留”。

如果你已经安装了OpenClaw，体验过后发现驾驭不了，想要卸载，可参考OpenClaw官方自带的卸载教程操作，不需要懂代码，只需要一步步跟着照做即可。

**官方推荐的卸载教程**

打开终端（Terminal）

* Windows用户：按键盘上的Win+R键，在弹出的框中输入cmd，然后按回车；或者直接在开始菜单里搜索“命令提示符“或“PowerShell”。
* Mac用户：按键盘上的Command+Space（空格键），在搜索框输入Terminal或终端，然后按回车。

输入下面这行命令并回车

代码块：openclaw uninstall --all --yes，其中：

* uninstall：告诉程序我要卸载。
* --all：彻底删除，包括网关服务、本地数据库、配置文件等所有数据。
* --yes：全程自动确认，不需要你手动按 Y 确认。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JPu5lvAD1XE3icibqfpvRibd0TszqwiciaDHbesASvRGEN8pkkqt7r0lJPnlQ1wV1WQMd2Ljd94ibb75HlAXXF9o7wfblYOBOuZHcVytRkqKyYnXo/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=1)

删除命令行工具

以上指令跑完后，电脑里就只剩下OpenClaw的外壳（CLI工具）了。如果想把它彻底清除，再执行一行——代码块：npm uninstall -g openclaw。至此，电脑就彻底干净了。

注意事项

执行完上述操作后，建议重启一次电脑，确保所有后台进程彻底关闭。如果曾在OpenClaw里绑定过API Key（如OpenAI、Claude的密钥），建议去对应的官网废弃旧密钥，生成新密钥，以防万一。

来源：央视新闻

责任编辑：清栀

      【2026-03-23期】

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

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