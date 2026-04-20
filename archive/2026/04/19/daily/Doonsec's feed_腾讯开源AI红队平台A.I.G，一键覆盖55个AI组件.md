---
title: 腾讯开源AI红队平台A.I.G，一键覆盖55个AI组件
url: https://mp.weixin.qq.com/s/7En46JHCj8BsHfrdMK17og
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:52:21.876860
---

# 腾讯开源AI红队平台A.I.G，一键覆盖55个AI组件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicK3gdGRD4dheJkdtmPnKoep9OS6yTJ2YD9EQkV4CCoBj7Ll1Hb59q11oW56Rj93mdicpnccMteye1e8XwNbhVOCXibj1Q3evIBmw/0?wx_fmt=jpeg)

# 腾讯开源AI红队平台A.I.G，一键覆盖55个AI组件

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年4月19日，腾讯朱雀实验室正式更新旗下AI-Infra-Guard（A.I.G） 项目。

这款定位为AI红队平台的工具完成重大升级，从AI基础设施安全扫描，全面扩展至整个Agent生态安全评估，已在GitHub斩获3.5k Star，下载量突破9.2k。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicKy2awZRe7DmYFEIV13o6UoU5aPYbMeP10QyloTqZwvuibheNXMYib1wyPxKibChjibSnLlk3jPWzxeXsJY9FWszgb0IYOuEDTecgw/640?wx_fmt=jpeg)

五大核心模块，覆盖AI安全全场景

A.I.G构建五大检测模块，实现从AI底层组件到上层应用的全链路安全体检，精准对标行业安全标准：

1. ClawScan（OpenClaw安全扫描）

一键检测OpenClaw不安全配置、Skill风险、CVE漏洞与隐私泄露，安全引擎由朱雀实验室自研，Skill情报数据与科恩实验室联合共建。

2. Agent Scan（Agent智能扫描）

基于LLM多阶段推理完成Agent工作流安全评估，覆盖信息收集、漏洞检测、分级研判全流程，支持Dify、Coze及自定义HTTP接口，漏洞分类严格对齐OWASP Top 10 for Agentic Applications（ASI 2026）。

3. MCP Server & Agent Skills扫描

覆盖14大类安全风险，支持源代码、GitHub URL、远程MCP服务三种扫描方式，可检测工具投毒、Rug Pull骗局、语义劫持、幽灵指令等新型Agent安全威胁，全面覆盖MCP生态已知风险。

4. AI基础设施漏洞扫描

精准识别55个主流AI框架组件，涵盖1000+已知CVE漏洞，支持Ollama、ComfyUI、vLLM、n8n、Triton等常用组件，输入目标地址即可自动指纹识别+漏洞匹配。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicJkaxNbYCVjMdm3Tu1ZQgoAnSVIQnn2ndwOGvHMBQcZCdsgLfKyK0XN8cPRBfVBk2PuSR8g6ZsUv6PWd5zQ6xBOVo61hlibLOkM/640?wx_fmt=jpeg)

5. 越狱评估

依托高质量数据集检测Prompt安全风险，支持多攻击方法验证与跨模型对比，快速诊断大模型越狱漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicJ5eb7Dia1WxZFIt8ibY89R3DC9KRBK00ycRlZvx2ia7wpNNZQsVPOApqYp0EwPF774NWVZRpzeTJWSTEWJC5uLQpgGEVP8AXenzA/640?wx_fmt=jpeg)

核心亮点：直击AI生态安全痛点

 精准预警供应链风险：可检测LiteLLM等主流LLM代理库供应链攻击，第一时间更新高危威胁规则。

企业&学术双认可：

服务腾讯、DeepSeek、蚂蚁国际、工行、B站、vivo、OPPO等头部企业，清华、北大、浙大等高校广泛使用，获17篇学术论文引用，入选Black Hat Europe 2025 Arsenal。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicKWGSrw3fvnOYNhqNx3W410j6L58z0CFdjt5s7Kg2e7NicNmEGLysrtibHyAxQibT5edtOX1iaYicAlNjIeJCibUNiaiaJZ6sQqBoQ5Xjc/640?wx_fmt=jpeg)

- 工程化落地能力：支持嵌入CI/CD流水线作为发布前安全门禁，可通过Webhook在PR事件自动扫描，插件化架构支持YAML/JSON自定义扩展规则。

- 一键快速部署：通过Docker Compose即可快速启动，提供完整API与Swagger文档，便捷集成到现有安全体系。

工具局限与使用提示

- 暂无认证机制，不建议公网部署；

- Agent Scan当前主要支持Dify、Coze平台；

- Pro版需邀请码，功能差异未公开。

A.I.G的核心价值不仅是安全扫描工具，更重新定义了AI红队的检测边界，覆盖基础设施、Agent工作流、MCP Server、Skill供应链全层级，为AI规模化落地提供标准化安全检测框架。

快速部署

plaintext

git clone https://github.com/Tencent/AI-Infra-Guard.git

cd AI-Infra-Guard

docker-compose -f docker-compose.images.yml up -d

访问地址：http://localhost:8088

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicJshhM6KfGAtYicUmicUQ0TibHm5qJibFApEV1iaaWHrMliaOQibjW2JAodsTiaK72sul8BsGJXBOph1haMHmxMmds9Mks6MU0Q4icEyXjA/640?wx_fmt=jpeg)

项目地址：github.com/Tencent/AI-Infra-Guard

作者：hacking。前北漂程序员，现在做安全。

文章数据来自网络，大模型优化，侵权删。

**往期****相关****回顾**

[度假变噩梦！徐泽伟因美国网络入侵指控在意大利被扣，妻子：老人孩子还能等多久？](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247550585&idx=1&sn=d393ee66a57f3a9b6d2895a3e3b9ed9d&scene=21#wechat_redirect)

[被指控网络入侵：中国徐泽伟在意大利被扣押的210天、或被引渡美国](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247550577&idx=1&sn=34365a236610b5680df0781a39f0e3d7&scene=21#wechat_redirect)

[徐泽伟引渡美国！意大利上诉被驳回，被美国指控黑客入侵](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247554243&idx=1&sn=5b97552ba5b90774714b65b7e239ebce&scene=21#wechat_redirect)

[朝鲜黑客封神！潜伏6个月盗走2.85亿，DeFi史上最精密猎杀案曝光](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247553894&idx=1&sn=102a2765f53d5763674c655e99a438c0&scene=21#wechat_redirect)

[拼多多暴力抗法夹断执法人员手指！网友：“砍一刀”不是白叫的，15亿罚轻了](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247554322&idx=1&sn=7a58f4966877fd25b453b69723b99c25&scene=21#wechat_redirect)

预览时标签不可点

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