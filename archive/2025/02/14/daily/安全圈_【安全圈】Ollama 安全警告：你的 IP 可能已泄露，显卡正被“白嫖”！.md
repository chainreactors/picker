---
title: 【安全圈】Ollama 安全警告：你的 IP 可能已泄露，显卡正被“白嫖”！
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067800&idx=1&sn=09bc41e2d4710c7c7588a6fd8940884e&chksm=f36e7b98c419f28e917c9f93fe48b1fe4ebeda2d0e351b2d1fbf8048a9bded4dd1127f05fcc3&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-14
fetch_date: 2025-10-06T20:36:29.405367
---

# 【安全圈】Ollama 安全警告：你的 IP 可能已泄露，显卡正被“白嫖”！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylian7dYBcH4FqP33t54OpgM0LqhoAzYgXyibOBtI20mr1jRrGzOceNd0CeQ5K95OjAEwRBK1brcU0JQ/0?wx_fmt=jpeg)

# 【安全圈】Ollama 安全警告：你的 IP 可能已泄露，显卡正被“白嫖”！

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络安全

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylian7dYBcH4FqP33t54OpgM0oF2yiaibToBMunqIicxpBI33fGP3mLM4djHSrD3ARhWglwfCqaaLk4Etg/640?wx_fmt=png&from=appmsg)

最近，一项令人震惊的“硬核”技术浮出水面：通过简单的方法，任何人都能直接调用全球范围内默认开放 Ollama API 的计算机资源。无论这些设备位于美国、中国、德国还是英国，只要拥有 IP 地址，就可能被用作高性能 AI 计算服务器，而设备主人却浑然不觉。

#### 实测场景：

抱着试试看的心态，我随机挑选了一个 IP 地址进行测试，结果令人难以置信——直接成功连接！这台设备竟是一台配备了 32B 模型 DeepSeek R1 的高性能机器，显卡配置至少是 RTX 3090 或 RTX 4090 级别。这样的设备居然能被随意调用，实在令人后背发凉！

#### 问题根源：

#### Ollama 默认暴露 API！

#### Ollama 的默认设置：

1. 默认启动 API：安装并启动 Ollama 后，它会自动启动一个 API 服务。
2. 无访问限制：默认情况下，任何人都可以通过 IP 地址直接访问该 API，无需任何授权。
3. 全球 IP 扫描威胁：更有甚者，有人开发了全球 IP 扫描工具，专门搜寻开放 Ollama API 的设备，并将这些 IP 地址整理成公开搜索引擎。只需输入关键词，就能轻松找到并使用这些设备。

#### 潜在危害：

如果未做任何防护，你的 GPU 资源可能正在为陌生人提供 AI 计算服务：

* 资源耗尽：你的显卡可能被大量占用，导致设备性能下降，甚至无法正常使用。
* 安全风险：开放 API 可能被滥用，甚至成为攻击的跳板。
* 经济损失：如果你使用的是云服务器（如 AWS、阿里云等），GPU 资源被占用将直接增加你的成本。

#### 防护措施：如何保护你的设备？

为了避免设备被“白嫖”，可以采取以下措施：

1. 限制 API 访问范围
   修改 Ollama 启动命令，让 API 仅监听本地回环地址（127.0.0.1），防止外部访问：

```
```
<BASH>
ollama serve --host 127.0.0.1
```
```

2. 使用防火墙屏蔽端口
   通过防火墙封锁 Ollama 的默认端口（11434），确保 API 只能在本地或局域网内访问：

* Windows：

```
```
<POWERSHELL>
New-NetFirewallRule -DisplayName "Block Ollama External Access" -Direction Inbound -LocalPort 11434 -Protocol TCP -Action Block
```
```

* Linux（iptables）：

```
```
<BASH>
sudo iptables -A INPUT -p tcp --dport 11434 -j DROP
```
```

* Linux（UFW）：

```
```
<BASH>
sudo ufw deny 11434
```
```

3. 检查公网 IP 是否暴露
   如果你的 Ollama 运行在云服务器或具有公网 IP 的设备上，建议立即检查公网 IP 是否可访问。如果发现异常，请关闭 Ollama 或限制 API 访问权限。
4. 停止非法调用
   如果发现你的设备已被他人调用，建议立即更换 IP 地址或停止 Ollama 运行，避免进一步资源损失。

#### 总结：

Ollama 默认设置的开放性虽方便了本地使用，但也带来了巨大的安全隐患。你的显卡是用真金白银购买的，绝不应该为陌生人“免费打工”。

* 立即行动：检查你的 Ollama 配置，确保 API 不被外部访问。
* 提高警惕：定期监控设备资源使用情况，发现异常及时处理。
* 安全至上：将防护措施落实到位，避免成为下一个被“白嫖”的对象。

你的设备，你的资源，必须由你来掌控！

***END***

阅读推荐

[【安全圈】网络攻击扰乱了Lee报纸在美国各地的运营](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067786&idx=1&sn=6b219161a3c6923cd9dffc601b4abff2&scene=21#wechat_redirect)

[【安全圈】OpenSSL 修补了高严重性漏洞 CVE-2024-12797](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067786&idx=2&sn=c497b609a80250b639e05ac4c19e5d69&scene=21#wechat_redirect)

[【安全圈】OmniGPT AI 聊天机器人涉嫌入侵：黑客泄露用户数据和 3400 万条消息](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067786&idx=3&sn=2f7e62e02af6dbbc8efc5add1acf93e2&scene=21#wechat_redirect)

[【安全圈】Microsoft补丁积极利用零时缺陷-CVE-2025-21418 & CVE-2025-21391](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067786&idx=4&sn=290289ab17f0f8e7dea5feaad426fb1b&scene=21#wechat_redirect)

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