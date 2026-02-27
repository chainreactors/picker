---
title: AI-Reverse-Engineering：ai逆向工具实战和CTF适用
url: https://mp.weixin.qq.com/s/lz63rG9CSMOaavnubo5uYA
source: Doonsec's feed
date: 2026-02-26
fetch_date: 2026-02-27T04:06:23.426485
---

# AI-Reverse-Engineering：ai逆向工具实战和CTF适用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicLC2R32I14iaW01boz2RsDNKOUmsmib68bFltuSpJQgCLGKvqVJmk5wHDEeG4ktiaAgKF1J0JKST7Se7pr34zDuV9gefkO8eQ7w7U/0?wx_fmt=jpeg)

# AI-Reverse-Engineering：ai逆向工具实战和CTF适用

sec0nd安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于网安武器库
，作者网安武器库

![](http://wx.qlogo.cn/mmhead/wprMnqDUJH750rSoju0Ydj8oy8ZcvD3Q02RbUUUWUCUrOVR0ezfokNuxFv2svB1ibhJPFe7hEQAw/0)

**网安武器库**
.

分享各种实用的黑客工具和CTF工具

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[Venom：全面的渗透测试利器](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486518&idx=1&sn=08481bf21ca0caa11e1a60abc67f8e55&scene=21#wechat_redirect)

·[猫头鹰 XSS 平台：一个针对XSS漏洞的测试平台](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486503&idx=1&sn=b0abad58a1cdbebb8c1aec9e2e405dbd&scene=21#wechat_redirect)

·[Donut+SGN 利用微软签名进行静态特征混淆与终端检测规避](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486480&idx=1&sn=91080cabf64e334fb3151852df260b99&scene=21#wechat_redirect)

·[FnOS GUI Exploit Tool:针对 FnOS 系统的综合漏洞利用工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486470&idx=1&sn=be6ac8da8d54423b050f7ab7e596659b&scene=21#wechat_redirect)

·[ManSpider：一款黑客内网快速敏感信息搜集工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486462&idx=1&sn=13d367de0d7867608564ca9827a012b9&scene=21#wechat_redirect)

·[Web-Check：一款全面的web网站信息和漏洞扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486451&idx=1&sn=1e91aeea9f174b4331a580e28e5c273f&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJgbLJw5OLia4slP9WBYUSraMkpDaSz9lOEDE08ibOuepibbySHXrDgjUiawVnPrZia3NJ5Tut2KgZwiaNt9CCMbOHnZfnUicNDBVgG7Q/640?wx_fmt=png&from=appmsg)

      逆向工程往往需要研究人员逐行分析二进制文件、解读汇编指令，耗时且门槛高。而由 biniamf 开发的 `AI-Reverse-Engineering` 工具，将 AI 能力与经典逆向分析工具 Ghidra 深度融合，通过自然语言交互驱动 Ghidra 自动完成逆向分析流程，让安全研究者无需手动操作 Ghidra 界面，仅通过提问就能获取二进制文件的函数分析、反编译伪代码、交叉引用等核心信息，大幅降低逆向工程的操作成本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**中国记者节**

克隆项目仓库

```
git clone https://github.com/biniamf/ai-reverse-engineering.gitcd ai-reverse-engineering
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJoSkwyDTIS4YXpLiaGdhWkO8AGajAd0nrumBMLlzg3mZxvAzHTbs1aL6LpvzUlP8RZ5m8SQ8FER9cB6LqoibndgXI7iagS2ib8WrI/640?wx_fmt=png&from=appmsg)

启动 Ghidra 无界面服务（Docker 方式）

通过 Docker 快速启动 Ghidra REST API 服务，无需手动安装 Ghidra：

```
docker run --rm -p 9090:9090 -v $(pwd)/data:/data/ghidra_projects biniamfd/ghidra-headless-rest:latest
```

该命令会映射 9090 端口用于 Ghidra 服务通信，并将分析数据存储在本地 data 文件夹

配置 LLM 服务

新建 .env 文件，填写 LLM 相关配置（以 OpenAI 为例）：

```
OPENAI_API_BASE=https://api.openai.com/v1OPENAI_API_KEY=你的API密钥OPENAI_MODEL=gpt-3.5-turbo
```

若使用本地 LLM（如 Ollama），替换为以下配置：

```
LLM_TYPE=localLOCAL_LLM_URL=http://localhost:11434/v1LOCAL_LLM_MODEL=llama2
```

启动 WebUI 服务

安装依赖并启动 Web 界面：

```
pip install -r requirements.txtpython webui/app.py
```

启动成功后，访问 http://localhost:5000 即可进入工具界面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**使用演示**

访问 http://localhost:5000 即可进入工具界面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJgABYlzkI5e1koKfcQmxltbicfHBAj8d8dZYYrghBEYLT33NqwdMmlffwzpEcT1DiaWXwiaHVuGcHicibASdEDnNpKlJIc3vPp4CKw/640?wx_fmt=png&from=appmsg)

选择待分析文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicL00iaUq3xFRo5qZErM6TS3R1TPupmDibiaiaYHTIQtEsvibe4Q300AMfiaIaF7zOnMzThjTcM8FaD9BO7hE0f5WHiaSyR8VAoS8VTeicU/640?wx_fmt=png&from=appmsg)

分析

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJ3QicOFCu73cGxdJGmVTfnPtBSLDdZ6NPU2pr6D4Coc1TyP9Zksl8Lqz2670IJPXK0nP25UNnys796On9n0pqsGuu4KicBQjwko/640?wx_fmt=png&from=appmsg)

出现下图样式就是分析完毕了

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKicZAdPKGLHkCt9nR0hJ9ribN76aP4GIDxYFzib2V7LovnpjlSuhCpxtibTjW72VHoH4yvxLlGN0vD6nHdKDYqVcZiax1pTfedicE2g/640?wx_fmt=png&from=appmsg)

点开后询问你的问题即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIuibNnC55gupS3R6Rc8hvB4C8USb7XAoGbNJoa71HVwSsJvmpZ5wzdMPMzT4KdZtT6IppngM2WmxkzDEEAJITprFr8046Lc2EE/640?wx_fmt=png&from=appmsg)

以下是完整演示视频

github地址

```
https://github.com/biniamf/ai-reverse-engineering
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

sec0nd安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

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