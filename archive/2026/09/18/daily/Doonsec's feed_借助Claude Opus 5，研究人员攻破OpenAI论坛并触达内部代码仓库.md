---
title: 借助Claude Opus 5，研究人员攻破OpenAI论坛并触达内部代码仓库
url: https://mp.weixin.qq.com/s/8sMVz_NU6hgpp7fuPxlhWQ
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:52:44.657320
---

# 借助Claude Opus 5，研究人员攻破OpenAI论坛并触达内部代码仓库

# 借助Claude Opus 5，研究人员攻破OpenAI论坛并触达内部代码仓库

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

近日安全研究团队Hacktron披露一安全测试事件：研究人员借助Anthropic的Claude Opus 5，针对图片解码器漏洞完成漏洞利用开发，成功入侵基于Discourse搭建的OpenAI官方社区论坛，并利用身份体系配置缺陷接管员工ChatGPT、Codex账号，最终访问到OpenAI内部源代码仓库。

本次安全测试发生在2026年7月25日，研究团队将Discourse图片处理组件的远程代码执行漏洞，与OpenAI单点登录机制缺陷结合，证实外围服务一旦被突破，可跨越身份信任边界，侵入高价值AI研发环境。

漏洞根源：HEIC图片解析引发堆缓冲区溢出

攻击入口是OpenAI社区论坛`community.openai.com`。该论坛采用Discourse程序，在处理用户上传图片时，常规图片校验库FastImage并不支持HEIC/HEIF格式文件。

当用户上传这类图片，系统会调用ImageMagick工具处理，底层依赖libheif解析库。

论坛容器使用Debian 12系统，内置libheif 1.19.7版本，该版本缺少上游安全补丁，存在堆缓冲区溢出漏洞。恶意构造的HEIC图片在解析过程中，可触发越界读写，为攻击者提供漏洞利用原语。

该漏洞编号CVE-2026-32882，Debian后续发布安全公告DSA-6417-1，警告畸形图片可造成内存信息泄露、拒绝服务，甚至执行任意代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1n1dHTp93O5Y6R2WtemLicrosSHLLibtL3piaFrrOpibBgvGfVKJ4xAkPbibnC25EM2WZAibJ0g0nGHwNdGXfMvIeu6QROPEIy2hz7s/640?wx_fmt=png&from=appmsg)

Claude Opus 5大幅降低漏洞利用开发门槛

研究团队最先使用Claude Opus 4.8开展审计与EXP编写。在关闭地址空间布局随机化（ASLR）环境下可以实现代码执行，但在Discourse默认开启ASLR的环境中，多次尝试都无法稳定利用。

Anthropic在7月24日发布Claude Opus 5之后，研究人员将同一任务交给新版大模型。仅用时3小时，Opus 5就生成可在Mac本地ARM64环境运行的EXP；随后研究人员将其适配移植到Discourse使用的x86-64+jemalloc运行环境。

7月25日UTC时间6点，团队验证图片上传路径可实现本地远程代码执行；在自建Discourse测试环境验证读取`/etc/hosts`成功后，将该EXP用于OpenAI社区论坛。

本次并非AI全自动黑客攻击。全程需要安全专家人工引导任务、验证结果、管控漏洞披露流程，但AI显著压缩漏洞利用开发周期，大幅降低这类高级攻击所需的专业人力成本。

跨服务连锁风险：论坛沦陷，直通内部研发资产

仅仅拿下论坛RCE，还无法直接访问OpenAI代码仓库。真正形成纵深突破的，是OpenAI身份体系配置不当：

被攻陷的论坛会话，可无交互接管在岗员工的ChatGPT与Codex账号。而Codex账号关联OpenAI私有GitHub组织，攻击者以此为跳板，尝试对私有代码仓库提交无害测试PR（编号1186742）完成权限验证。完成验证后研究人员立刻停止测试，通过Bugcrowd提交漏洞报告并通知OpenAI安全团队。

这类联合攻击案例敲响警钟：联邦身份信任体系必须纳入所有关联应用的攻击面评估。一旦账号失守，攻击者可顺着身份信任链访问GitHub、Slack、邮件等业务资产，攻击影响范围会远超最初被攻破的外围论坛。

事件时间线：

- UTC 7月25日 08:00–10:00：针对OpenAI论坛开展测试

- UTC 7月25日 22:49:45：OpenAI完成漏洞修复，间隔约14小时

Discourse侧漏洞也单独通过HackerOne上报，7月28日发布安全通告GHSA-vhm9-85gw-x335。OpenAI为该安全发现发放6500美元赏金，同时备注社区论坛本身不在其漏洞奖励计划测试范围内。

运维防护建议

1. 自建Discourse站点：不要仅在网页端更新，需要拉取最新代码并重建容器，网页更新无法替换底层存在漏洞的系统镜像；

2. 需要解析HEIF/HEIC/AVIF等不可信图片的企业：升级打好安全补丁的libheif、libde265组件；关闭不需要的解码器；图片转换操作放在隔离、一次性销毁的沙箱内执行；

3. ImageMagick环境：通过安全策略限制仅启用业务必需图片格式，例如GIF、JPEG、PNG，减少攻击面。

资讯来源：Hacktron博客、华尔街日报公开报道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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