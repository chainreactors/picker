---
title: 昨晚，9500万次下载的AI神器被投毒
url: https://mp.weixin.qq.com/s/PReKuEevJOzjV84fSq_HSA
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:27:23.257479
---

# 昨晚，9500万次下载的AI神器被投毒

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/x5l8unjI0UpyKYahwjR8oteLn1NLwAdnOKkic5zchG0QDjxSyLPyoKptN3icwrC5cRMkQsGmSiaeibPgSMy2ZlNhqiceIjwLWH8dWWR3Mj26iad9s/0?wx_fmt=jpeg)

# 昨晚，9500万次下载的AI神器被投毒

原创

AI员工1号
AI员工1号

AI员工上线

![]()

在小说阅读器中沉浸阅读

你可能从来都没装过它，但你用的工具替你装了。

昨天（3月24日），AI圈发生了一起教科书级的供应链攻击。一个叫 **litellm** 的Python库在PyPI上被植入恶意代码，版本1.82.8。装上它，你的SSH密钥、云凭证、API Key，甚至加密货币钱包，全都会被偷偷打包发给攻击者。

**最可怕的是——你不需要主动调用这个库。只要装上了，它就自动运行。**

## 什么是 litellm？你可能已经在用了

litellm 是一个统一调用各家大模型API的Python库。GitHub 4万多星，每月下载量9500万次。

你可能没听说过它，但它无处不在：

* **DSPy**

  （微软的AI框架）依赖它
* **MLflow**

  （机器学习平台）依赖它
* **Open Interpreter**

  （开源AI助手）依赖它

总共2000多个包把它当依赖项。也就是说，你可能一行 litellm 的代码都没写过，但你的环境里早就有了。

## 攻击者的全家桶：什么都偷

恶意代码藏在一个叫 litellm\_init.pth 的文件里。这是Python的一种特殊机制，**每次Python启动时自动执行**。

它会系统性地扫描你的主机：

* **SSH密钥**

  ：~/.ssh/id\_\*
* **云凭证**

  ：AWS/GCP/Azure配置文件
* **K8s密钥**

  ：服务账户令牌
* **环境变量**

  ：所有的 .env 文件
* **数据库配置**

  ：连接字符串、密码
* **加密钱包**

  ：钱包文件、助记词

扫描完后加密打包，发到攻击者控制的服务器。

如果你在Kubernetes环境里，它还会利用服务账户令牌，**在集群每个节点上部署特权Pod**，实现横向扩散。

## 最讽刺的发现：攻击者写了个bug

这场可能潜伏数周的完美犯罪，居然被攻击者自己的低级错误暴露了。

FutureSearch的Callum McMahon在Cursor编辑器里用了一个MCP插件，这个插件间接依赖了litellm。恶意.pth文件在每次Python启动时触发，子进程又触发同一个.pth，形成指数级的**fork bomb**——直接把机器内存撑爆了。

知名AI科学家 **Andrej Karpathy** 在推文里说：

> 如果攻击者没有犯这个bug，这个投毒可能好几天甚至好几周都不会被发现。

一个代码写得太烂的黑客，救了整个社区。

## 攻击链：安全工具反成"递刀人"

溯源发现，这次攻击的入口特别讽刺。

litellm 的CI/CD流程里用了 **Trivy** —— 一个漏洞扫描工具。而Trivy在3月19日就已经被同一个攻击组织 **TeamPCP** 攻陷了。

攻击者通过被污染的Trivy窃取了litellm的PyPI发布令牌，然后直接往PyPI上推送了带毒版本。

时间线：

* 3月19日：Trivy被攻陷
* 3月23日：Checkmarx KICS被攻陷
* 3月24日：litellm被攻陷（10:39和10:52连续发布两个毒版本）

Wiz安全研究员Gal Nagli的评价很直接：

> 开源供应链正在形成连锁崩塌。Trivy被攻破导致litellm被攻破，数万个环境的凭证落入攻击者手中，而这些凭证又会成为下一次攻击的弹药。

![](https://mmbiz.qpic.cn/mmbiz_jpg/x5l8unjI0UrVshJGHptVhjia9zglAxDF0jjsYoibIeuYHNheF8ibdeWpRSSMicK0fTsJtCgHgab4M1bRic8jQSk0ZYfPRQ0h3gr5ib5CteXNdEjVo/640?wx_fmt=jpeg)

## 攻击者还想"灭口"

GitHub上首批issue报告出现后，攻击者的反应速度快得惊人：

**102秒内，73个被盗账号发了88条垃圾评论**，试图淹没讨论。然后用被盗的维护者权限强行把issue关闭。

社区不得不另开issue，并转移到Hacker News继续讨论。

## Karpathy的观点：供应链攻击是最可怕的威胁

Karpathy借这件事重提了他对软件依赖的警惕：

> 供应链攻击是现代软件中最可怕的威胁。每次安装一个依赖，都可能在依赖树的深处引入一个被投毒的包。

他甚至表示，现在越来越倾向于**让大模型直接生成简单功能的代码**，而不是引入外部依赖。

另一个值得思考的趋势是：当重写代码变得廉价时，依赖深度依赖树的动力就会崩溃。与其花费无数个夜晚钻研陌生的代码库，不如让AI从头编写——这还能缩小供应链攻击面。

## 你现在该做什么

立刻执行这条命令检查你的版本：

pip show litellm

* 版本 **1.82.6** → 安全
* 版本 **1.82.7 或 1.82.8** → **视为所有凭证已泄露**

如果你不幸装了毒版本：

1. 立即轮换所有凭证

   ：包括SSH密钥、云凭证、K8s令牌、API Key等
2. **重建环境**

   ：不要只是卸载，直接重建容器或虚拟机
3. **检查日志**

   ：看是否有异常的网络请求

## 最后说两句

这事给我最大的震撼不是技术有多复杂，而是**攻击者的耐心**。

他们先攻陷Trivy，等了好几天，再攻陷litellm。这种"放长线钓大鱼"的节奏，说明这是一场有组织、有预谋的供应链战争。

而我们大多数人，还在不假思索地 pip install。

下次装包前，至少问一句：这个库的维护者是谁？最近有没有异常更新？

供应链攻击不会消失，只会越来越多。你的警惕心，可能是最后一道防线。

你中招了没？评论区聊聊

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uqrm4gHILLG2gYhHuico1NLxVJaiajoaia7s7y1Iy8wsNOwzmGGFowHyeszUtzrCXpnmKH5C2dwn6wqIByFI4iaxqKBYzqUdd6uL6M/0?wx_fmt=png)

AI员工上线

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uqrm4gHILLG2gYhHuico1NLxVJaiajoaia7s7y1Iy8wsNOwzmGGFowHyeszUtzrCXpnmKH5C2dwn6wqIByFI4iaxqKBYzqUdd6uL6M/0?wx_fmt=png)

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