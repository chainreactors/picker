---
title: 【安全圈】假 AI 助手暗藏木马：恶意“ClawdBot”插件潜伏 VS Code
url: https://mp.weixin.qq.com/s/pmhDywCsrmwiSnwWo4RU1g
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:19:14.369970
---

# 【安全圈】假 AI 助手暗藏木马：恶意“ClawdBot”插件潜伏 VS Code

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyFhGG5jrQCsMOjZwAMC7FibGg3BaDneeic6x5pHZ1rd3blrO2GBnGH01B3rO0GrTiaLp7DlEVShUvCJnO4w7LsD3eUCXwOqibSG2gE/0?wx_fmt=jpeg)

# 【安全圈】假 AI 助手暗藏木马：恶意“ClawdBot”插件潜伏 VS Code

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

ClawdBot

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyGuicuLicPqt6ONP7JliarxDHLafaCf9o5HzIialKfAsxMJ7M1dibBThIMp9t8L4HSTxVNF1ZfhgtW8ciasqeHiajic2Q87oEKbNhkBhlw/640?wx_fmt=png&from=appmsg)

AI 编程助手正在成为开发者的“标配工具”，但攻击者显然也盯上了这波热度。

2026 年 1 月 27 日，Aikido Security 安全研究员 Charlie Eriksen 披露，一款名为 **“ClawdBot Agent”** 的 Visual Studio Code 插件伪装成热门 AI 编程助手“ClawdBot”，实际上却在开发者电脑中**悄悄投放木马程序**。

这起事件虽然最终影响范围有限，但它揭示了一个值得警惕的新趋势：**攻击者开始系统性利用 AI 工具热潮作为供应链攻击入口。**

---

## 伪装得“太像真的”，反而更危险

很多恶意插件粗制滥造，功能不全，很容易露出破绽。但这次不同。

这款假 ClawdBot 插件：

* 拥有专业图标与完整 UI
* 支持多家主流 AI 接口（OpenAI、Anthropic、Google 等）
* 实际功能可以正常调用 API 进行代码辅助

也就是说，它**确实是一款能正常使用的 AI 编程助手**。

正因为“能用”，才更具欺骗性。用户在正常使用过程中逐渐建立信任，而恶意行为则在后台悄然执行。

安全报告指出，这本质上是一款**完整功能型木马（Functional Trojan）**——前台是生产力工具，后台是恶意投递器。

---

## 恶意行为：启动即投放

当 VS Code 启动时，该插件会自动下载并执行恶意载荷。

攻击链中使用了多个伪装文件名，例如：

* Lightshot.exe（常见截图软件名）
* Code.exe（Electron 伪装包）

这些名称只是“外壳”。分析发现，实际下载的是一个具备投递能力的恶意程序（dropper），可进一步部署后续载荷。

更值得注意的是，攻击者在代码中保留了多个硬编码回退路径，说明其载荷版本可能经过多次演化，具备持续升级能力。

---

## 基础设施：具备冗余与隐藏机制

调查显示，该木马的 C2（命令与控制）通信指向域名：

darkgptprivate.com

该域名注册时间距攻击发生仅数周，托管于塞舌尔的 Omegatech LTD。

攻击者还采用多层隐藏机制：

* 通过 Cloudflare 隐藏真实服务器
* 主 C2 域名 clawdbot.getintwopc.site
* 设置备用通信通道
* Node.js 失败则回退至 PowerShell 执行

这并非“玩票式”恶意插件，而是明显经过规划设计的攻击行动。

---

## 为什么开发者成为目标？

AI 编程工具具有几个典型特征，使其成为高价值攻击入口：

1. **高权限运行** —— 插件通常拥有文件读写权限
2. **直接接触源码** —— 可读取本地代码、凭证、密钥
3. **默认信任开发者环境** —— 企业安全策略往往较为宽松

一旦开发者机器被植入后门，攻击者可能：

* 窃取 API Key、云凭证
* 访问私有仓库
* 注入恶意代码
* 横向渗透企业网络

开发环境，正在成为新的供应链攻击前沿。

---

## 幸运的是：发现及时，影响有限

研究人员第一时间向 Microsoft 报告，插件很快被下架。

在移除前，该插件仅记录到 21 次安装，影响范围相对有限。

但需要注意的是：**真正的 ClawdBot 团队从未发布过官方 VS Code 插件。**

攻击者只是抢先注册了名称。

---

## 给开发者的现实提醒

在 AI 工具“淘金热”之下，风险正在同步上升。

建议开发者在安装插件前重点关注：

* 发布者是否为官方认证账号
* 是否有真实官网与开源仓库
* 是否存在社区讨论与历史版本记录
* 插件权限是否超出合理范围

尤其是新出现、借热点快速蹿升的工具，更应保持警惕。

---

这起事件释放出一个明确信号：**AI 不只是生产力工具，也正在成为攻击载体。**

当工具越智能、越流行，攻击者就越有动力去模仿它。

对开发者来说，真正的安全意识，不是拒绝 AI，而是在使用 AI 时保持基本的验证与审慎。

***END***

阅读推荐

[【安全圈】广东中山查获一起无人机黑飞案：破解限高飞至 8000 米、距离客机仅 800 米](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074091&idx=1&sn=258503d60276bfaba296f6bd06f49950&scene=21#wechat_redirect)

[【安全圈】伊利诺伊州男子承认入侵数百个 Snapchat 账户以窃取裸照](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074091&idx=2&sn=2f09e042ed9df8d43ab6088739b94dcd&scene=21#wechat_redirect)

[【安全圈】黑客团伙滥用 Hugging Face 平台传播数千款安卓恶意软件变种](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074091&idx=3&sn=b6761e3685ab7431a90b333dd1dd0638&scene=21#wechat_redirect)

[【安全圈】快手被罚 1 个亿，该来的还是来了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074077&idx=1&sn=69d08f4127037e10cba5cfd2b44b657c&scene=21#wechat_redirect)

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