---
title: 【安全圈】字节跳动Coze CLI被吐槽像病毒
url: https://mp.weixin.qq.com/s/-e32vbzIy-mAAMkQO5VVOw
source: Doonsec's feed
date: 2026-08-11
fetch_date: 2026-08-12T03:59:52.414794
---

# 【安全圈】字节跳动Coze CLI被吐槽像病毒

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyH3qIhHuUCsnXhZdsic9A8EvF54jJLBSP3GhibCDNgvycDvq9x5iaGUKIaibLliavIOmkDzd9Vrc5LZVe9r1zosicNDmafTrBKX6tibWA/0?wx_fmt=jpeg)

# 【安全圈】字节跳动Coze CLI被吐槽像病毒

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

AI

B站网友 @HDAlex\_John 日前发布视频吐槽字节跳动旗下的AI智能体协作平台像是病毒。扣子命令行版Coze CLI会**静默安装附带技能**，而这些技能则会将用户安装的其他AI智能体工作流引导到Coze CLI中运行。

## ⚙️ 安装后自动执行技能同步

Coze CLI在配置文件中定义生命周期脚本，随后静默安装附带的技能。这个过程**不需要用户确认**，并且通过参数设置隐藏子进程输出。脚本仅在CI环境或开发源代码目录中跳过执行，因此普通用户使用npm或pnpm等包安装器执行安装时会直接触发静默技能安装。

Coze CLI的内部实现随后调用技能工具并将其自身携带的技能文件安装到系统全局AI智能体技能目录，安装过程使用全局参数和自动确认参数。

## 🎯 劫持了哪些工具？

Coze CLI依赖的技能工具会扫描本机是否存在不同的AI智能体配置目录，检测范围包括：

* **Claude Code**

  ：通过 ~/.claude 判断是否安装
* **Codex**

  ：通过 ~/.codex 或相关配置路径判断是否安装
* **其他工具**

  ：Cursor、Trae AI（同为字节产品）、Comate、Cline、Gemini CLI等

## 🔬 源代码审计发现

通过对Coze CLI源代码的审计，蓝点网发现其包含多种内置技能，每种技能设置的目标不同。例如 using-coze-cli/SKILL.md 的描述明确将**软件开发、媒体生成、文件上传和会话任务等场景导向Coze CLI**。

Coze CLI内置的技能会被复制到共享技能池，然后根据不同的AI智能体目录结构创建软链接或副本。这意味着用户即使只是安装Coze CLI，也可能在没有主动执行技能安装的情况下，将扣子提供的技能加入到其他AI编程工具的技能搜索范围。

不过需要说明的是，审计**未发现传统恶意软件行为**（如读取SSH私钥、浏览器密码、注入可执行文件等）。但从AI智能体工作流角度来说，这属于通过技能文件注入优先级规则和平台路由策略，影响智能体对用户请求的判断，具有明显的厂商导流和工作流锁定特征。

## 🧹 如何清理和卸载

如果你已经安装了Coze CLI，可以按以下步骤清理：

**1. 清理扣子注入的技能**

执行命令：COZE\_CLI\_NO\_SKILL\_NOTIFIER=1 coze self skill remove

**2. 卸载扣子CLI**

执行命令：npm uninstall -g @coze/cli 或 pnpm remove -g @coze/cli

**3. 检查并删除残留技能文件**

需要删除以下目录中的coze相关文件：

* ~/.agents/skills/coze-agent-collaboration
* ~/.agents/skills/using-coze-cli
* ~/.claude/skills/coze-agent-collaboration
* ~/.claude/skills/using-coze-cli
* ~/.codex/skills/coze-agent-collaboration
* ~/.codex/skills/using-coze-cli

> 特别提醒：不要删除 ~/.agents/skills 目录本身，否则会影响其他智能体安装的技能。只删除其中与coze相关的子目录即可。

***END***

阅读推荐

[【安全圈】OpenAI紧急暂停！新AI模型竟会自学"黑客技术"](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078224&idx=1&sn=cc5cca1ffdaf71baba9728066f84d777&scene=21#wechat_redirect)

[【安全圈】200万人身份告急！比利时电子身份证曝致命漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078224&idx=2&sn=cdb595c396ed85c7d7cbec78a2e74951&scene=21#wechat_redirect)

[【安全圈】开发者小心！VS Code扩展暗中窃取加密钱包](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078224&idx=3&sn=27ac74789ce072180bb82f5b25e79d15&scene=21#wechat_redirect)

[【安全圈】服装品牌李维斯遭黑客攻击，部分企业数据被窃取](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078212&idx=1&sn=82c69a11c8cde7ebde9dbae49bcc8da3&scene=21#wechat_redirect)

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