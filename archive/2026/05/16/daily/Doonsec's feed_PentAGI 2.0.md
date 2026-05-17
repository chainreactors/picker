---
title: PentAGI 2.0
url: https://mp.weixin.qq.com/s/Um55TgUe6ZLf5yvaihcF4w
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:45:33.637110
---

# PentAGI 2.0

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquMXib5YeQGhldEiarReHT7pmcZues1zOXGVG1Zl37anBQz3eAEcxZQzaNNpPImljIk2vWwAytBiaeU5iczm8fKbCpXpfiasCkfaBIFU/0?wx_fmt=jpeg)

# PentAGI 2.0

原创

Eclat.
Eclat.

船山信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

PentAGI 2.0的正式开源。它不再是Nessus那种简单的扫描器pro，也不是几个命令行工具串起来跑流程，它是一套真正的多Agent自主安全平台，能够实现推演攻击路径的效果。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquMu8vhJyjCDQtmLiaqcPiauanT8xEp8ANWVmmfb7WKUZOIRibmNo3wIo4bzedJGaxTadicAQQ3M0MzXjtywRkoZUyb8FRuoJr4RYZo/640?wx_fmt=jpeg&from=appmsg)

**PentAGI 2.0内部**

查看其相关的文档可以发现PentAGI 2.0内部跑的是一套模拟真实红队的分工体系，从上到下。其中分为下面的几个分支协同发展

Primary Agent拆解任务、统筹协调；Pentester Agent执行具体渗透操作；Coder Agent专门写Exploit和Payload；Reflector Agent验证结果、挑毛病；Mentor Agent盯着整个过程，一旦发现某个Agent陷入死循环，立刻拉回来。

分工之后，每个Agent负责自己相关的那一个模块，而Mentor是在外统领全局的一个作用。

**国产模型API**

对国内安全团队而言，用境外云端大模型处理渗透测试的敏感数据，合规风险一直都是不可忽略的问题。针对这个问题PentAGI 2.0带来的是直接内置了DeepSeek、GLM、Kimi和Qwen的支持，只需要配个API\_KEY就能跑。还预置了Ollama Cloud等，更容易调用国产的大模型，也能让低成本的中小型业务运行起来。

**安装命令**

Docker Compose一键启动，三条命令搞定基础环境：

```
git clone https://github.com/vxcontrol/pentagi.gitcd pentagicp .env.example .envdocker-compose up -d
```

访问 http://localhost:3000 就能看到界面。接国内模型的话，在项目根目录建一个custom.provider.yml，把对应的base\_url和api\_key\_env填进去，挂载到容器里重启就好。

#### 手动安装步骤：

```
# 同样克隆并复制配置git clone https://github.com/vxcontrol/pentagi.gitcd pentagicp .env.example .env
# 创建自定义provider配置cat > custom.provider.yml << 'EOF'providers:  - name: deepseek    type: openai    api_base: https://api.deepseek.com/v1    api_key_env: DEEPSEEK_API_KEY    models:      default: deepseek-chat      embedding: deepseek-embedEOF
# 在.env中添加DeepSeek API密钥echo "DEEPSEEK_API_KEY=your_key_here" >> .env
# 挂载自定义配置并启动docker compose run -v $(pwd)/custom.provider.yml:/app/custom.provider.yml pentagi
```

**OOB攻击支持**

由于在进行SSRF探测、XXE外带、RCE回显等测试时，这些都需要进行反向连接的操作。因此PentAGI 2.0优化了Docker Host Network模式，使得容器可以直接绑定主机网络接口，再进行配合Agent提示词里强制分配OOB端口的机制，使得反向Shell监听场景可以正常跑通。这一个过程的解决，是区分能演示的工具和能实战的工具最直接的标准。

**调用限制**

开发者并没有无限开发它的ai自主服务，是因为他们设置了Agent调用工具不超过100次，限定Agent不超过20次；执行前强制生成3到7步计划；连续相同调用超过阈值会触发Mentor介入等一系列当ai陷入无限开发场景下的应急处置措施。但如今这套机制还是Beta状态。

安全建议：仅在授权隔离环境中部署，严禁对未授权目标使用。

来源：github.com/vxcontrol/pentagi

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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