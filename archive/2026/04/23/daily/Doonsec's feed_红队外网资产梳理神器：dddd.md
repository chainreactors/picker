---
title: 红队外网资产梳理神器：dddd
url: https://mp.weixin.qq.com/s/BjoaSdY3iE6JyWchc4jvmw
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:48:53.127620
---

# 红队外网资产梳理神器：dddd

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODzxac3bEPhs7pXSM9eH2mwfMDrWEiarkWVEEHCUREDN2pgIXbk0bqusJg8x6Yiaibyz3r6UmNm1hlZoomtq5Qera08QFEHe7h7cZk/0?wx_fmt=jpeg)

# 红队外网资产梳理神器：dddd

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 红队外网资产梳理神器

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

  dddd 是一款**批量信息收集与供应链漏洞探测工具**，支持 *自动识别输入类型*（IP/网段/域名/URL），内置**主动/被动指纹识别**与指纹漏洞映射数据库，集成 **Nuclei v3**、*子域名枚举*、空间测绘（Hunter/Fofa/Quake），面向**红队**与**安服人员**，优化信息收集工作流。

## 🚀 一句话优势

**自动识别目标类型**，指纹-POC 联动避免无效发包，**低依赖开箱即用**。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 自动类型识别 | IP/网段/域名/URL 无需手动分类 |
| 指纹识别 | 主动/被动识别，支持复杂逻辑运算 |
| 漏洞探测 | Nuclei v3 集成，指纹映射减少误报 |
| 子域名枚举 | 高效爆破，精准泛解析过滤 |
| 空间测绘 | Hunter/Fofa/Quake 批量拉取 |
| 审计日志 | 敏感环境行为追溯 |

## 📸 主要运行功能截图

| 功能模块 |  |
| --- | --- |
| 漏洞探测 | ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxF3BHhdTjGnicSOb19gFZZhzbia4uyU3gWJ0QPUyyZ8ic5CovhCppVmJmC01RSunOhPvau3X5BFWgvkg9Sdr8Ybq47e5HkAPyKqc/640?wx_fmt=png&from=appmsg) |
| 指纹 | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODy9Zdvu82FApJibbxV9wqyVFxBe19rTJ9FDfAcGibficicT4DrJms5qVpkf6FEVh4PiahCRiakM8dZlzq9n9QoehVy0l1U7RLoOica1Bg/640?wx_fmt=png&from=appmsg) |
| Poc | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwluR6pkKvp56LZ0GHAs8jdc2vQyf2of13EiaxIdmRZT9OsV6MC7ok5wc75ViaFuS6B1UfAvNeM9l5AknJnHjmoT0HR7XiaR4ia1Qg/640?wx_fmt=png&from=appmsg) |
| 工作流(workflow) | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxMYhKDCfShZfToRW3Ae5Eibice4qW7rsLq28SK3qCNf9cIsHic2TRiblFhejibQNeSOSX5lZJYI7I12Vz5qPwaI5TDls23It3EKUZ0/640?wx_fmt=png&from=appmsg) |
| 漏洞报表 | ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyPUgvRhiaSdGQRVjFNYPTFibYcJDGA1HaKj46nzPUUh1SPUficRpexfGpSmmrjWPyO01v0ia5ibHa3GqydwTLtxsP36QriaB5pehzCE/640?wx_fmt=png&from=appmsg)  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxAQib4SdcQblSCuOpfCCCP8GTd7NNI7zOiaQU0hPQzxEy76bI1aZl1baReExu4ics5v0SN4Ria8xDzZKBBMibNa73o0JUxc6URI5x4/640?wx_fmt=png&from=appmsg) |

## ✨ 核心亮点

### 1. 智能输入识别与复杂指纹逻辑

  无需手动区分目标类型，系统**自动识别**输入是 *IP 地址*、CIDR 网段、**域名**还是 *URL*，自动匹配对应的扫描策略。指纹识别引擎支持 **与/或/非/括号** 组合的复杂逻辑运算，规则编写**，可精准描述****多条件组合**的识别场景（如"Apache + Tomcat + 非 Windows"），大幅降低*误识别*与漏识别。

### 2. 指纹-漏洞映射减少无效发包

  建立**指纹与 POC 的映射数据库**，扫描时先执行**指纹识别**，仅对匹配到的组件调用关联 **Nuclei v3** POC 进行检测。相比全量 POC 扫描，这种方式**发包量减少 80% 以上**，既降低**目标告警概率**，又提升*扫描速度*。Hunter 低感知模式进一步减少空间测绘时的**风控触发**，适合大规模外网资产梳理。

### 3. 低依赖开箱即用与审计日志

  Release 提供各系统**预编译二进制文件**，下载即可运行，无需安装 *Python/Go* 等环境。支持 **txt/html/json** 多格式输出，HTML 报表包含**漏洞请求/响应详情**，便于**复现与报告撰写**。*-a* 参数开启**审计日志**，记录完整扫描行为，满足敏感环境的**合规审计**与*事后追溯*需求。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| 自动类型识别 | 正则+启发式判断 | 零配置，减少操作失误 |
| 复杂指纹逻辑 | 与/或/非/括号运算 | 规则表达力强，精准匹配 |
| Nuclei v3 集成 | 业界标准 POC 引擎 | POC 生态丰富，更新及时 |
| 泛解析过滤 | 智能去噪算法 | 子域名爆破结果更干净 |
| 低依赖二进制 | 静态编译发布 | 跨平台开箱即用 |
| Hunter 低感知 | 请求频率控制 | 降低 API 风控触发 |

## 📖 使用指南

① **准备工作**：从 Release 下载对应系统的**二进制文件**与 *config.zip*，解压后放置于同目录。v2.0 起可独立于 config 运行，但建议保留以获取完整指纹库。

② **核心操作**：执行 dddd -t 192.168.0.1/24 扫描内网网段，dddd -t http://test.com 进行 Web 扫描。外网资产梳理使用 dddd -t 'icp.name="xxxx有限公司"' -hunter -fofa -oip 从 Hunter 拉取并补充 Fofa 端口。子域名枚举执行 *dddd -t xxx.com -sd*，仅指纹识别添加 -npoc 参数跳过 POC 检测。

③ **结果查看**：默认输出至 **result.txt**，HTML 漏洞报表为 *当前时间戳.html*，可通过 *-o* 与 -ho 自定义路径。开启 *-a* 后**审计日志**保存至 audit.log。扫描可随时 **Ctrl+C 终止**，已识别结果实时落盘不丢失。

## 📖 项目地址

```
https://github.com/SleepingBag945/dddd
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

| ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzDcbialtDJB2iauRibULjWbzQk2oeHEyuNcGjibhWw6SpJia0RYGY3D7UhMASYr1QPAicb1LaSL1XlDrVowaibjeB41IKYSBHE8z9sN8/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwMu4dL9ZhibwZKibzwdD01Btq6ia2183uH0ibzaGibkr1aribDe1jicrtW0px8pd6Rz1kT7QpTtzfdmicibiaFZHSqI40srWZhLQ9HpR1JY/640?wx_fmt=png&from=appmsg) |
| --- | --- |

### 推荐阅读

✦ ✦ ✦

| [渗透测试人员必备武器库：子域名爆破、漏洞扫描、内网渗透、工控安全工具全收录](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485592&idx=1&sn=818004a6d625c4c4112ce73b83433854&scene=21#wechat_redirect) |
| --- |
| [AI驱动的自动化红队编排框架(AutoRedTeam-Orchestrator)跨平台支持，集成 130+ 安全工具与 2000+ Payload](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485309&idx=1&sn=292afbe37fb95c64f33470f915b0c54e&scene=21#wechat_redirect) |
| [JS逆向必备：这款插件能Bypass Debugger、Hook CryptoJS、抓取路由](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247486181&idx=1&sn=3ace47da643c72cec0d615aeccb955ac&scene=21#wechat_redirect) |
| [上传代码即审计：AI 驱动的自动化漏洞挖掘与 POC 验证平台](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485488&idx=1&sn=a37acb031febe69db608de53ddee5732&scene=21#wechat_redirect) |
| [AI 原生安全测试平台(CyberStrikeAI)](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485208&idx=1&sn=b5181181c1e0800124e3e099706ef2ef&scene=21#wechat_redirect) |
| [多Agent智能协作+40+工具调用：基于大模型的端到端自动化漏洞挖掘与验证系统](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485805&idx=1&sn=8f374a239135f6a753d5cce887f8318b&scene=21#wechat_redirect) |
| [基于DeepSeek的代码审计工具 (Ai-SAST-tool.xjar)](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485314&idx=1&sn=56082cd314311ffc15cc0bcf03a395e2&scene=21#wechat_redirect) |
| [基于AI的自主渗透测试平台](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485127&idx=1&sn=b5eb3fdc1cc23976011e2bca396c1bc7&scene=21#wechat_redirect) |

✦ ✦ ✦

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg)

**点在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxEb9kj2s0xfj49wycWpJlJYYzMflMiarFrZv4k6FxVzwtic65opL9vO55NibibVYyicXOeerVCRrxPicpxGm4dyAyPbmaciaaia0RFgms/0?wx_fmt=png)

0x八月

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxEb9kj2s0xfj49wycWpJlJYYzMflMiarFrZv4k6FxVzwtic65opL9vO55NibibVYyicXOeerVCRrxPicpxGm4dyAyPbmaciaaia0RFgms/0?wx_fmt=png)

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