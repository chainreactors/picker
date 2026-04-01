---
title: 从模板到提交到管理POC：VSCode 插件简化 POC 全流程
url: https://mp.weixin.qq.com/s/euKnHxD0p2cX9fpmmQWxPw
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:42:12.972013
---

# 从模板到提交到管理POC：VSCode 插件简化 POC 全流程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODxsKr3FGXzf9rZubTmWb5UzKEoaGSvTzPicCN20Uzuz3nzLjLn8sEFicB0Op2EEvR7u6Py2utvNufKMB5cO0ibvA9XHMSuXicDEhx0/0?wx_fmt=jpeg)

# 从模板到提交到管理POC：VSCode 插件简化 POC 全流程

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器中沉浸阅读

# 从模板到提交到管理POC：VSCode 插件简化 POC 全流程

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

  vscode-plugin-poc 是一款基于 **pocsuite3 框架**的 VSCode 插件，提供 *POC 模板生成*、漏洞平台一键提交、代码片段补全等功能，帮助**安全研究人员**快速完成漏洞验证代码的开发与管理，提升 POC 编写标准化程度。

## 🚀 一句话优势

**右键即生成 POC 模板**，一键提交漏洞平台，告别重复性代码编写。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 新建 POC | 右键生成 pocsuite3 标准模板 |
| 提交 POC | 一键提交到漏洞管理平台 |
| 代码片段 | 常用 POC 代码快速补全 |
| 本地扫描 | 快速创建本地扫描任务 |

## 📸 运行截图

| 功能模块 | 截图 |
| --- | --- |
| 右键新建 POC 菜单 | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODz8h6q2V6ibiaZxU0yiaq9EEbDWR0k1RWF05KS7QIu507icpcHZ2Vu3mksF4sHLLcJlibgiayc7hZ0PBYoD13caEFpAntqgjffbdv06E/640?wx_fmt=png&from=appmsg) |
| POC 模板生成效果 | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyaFxcsYd79KuI4qpxggN6RFcLofBRuyEMvqNXf4DK2FDOiaLjPv3gFKko1cDvJAHQQvdproibPHHAicucKHyia6h1pKCGa3O4cEPE/640?wx_fmt=png&from=appmsg) |

## ✨ 核心亮点

### 1. pocsuite3 标准化模板生成

  右键资源管理器任意文件夹，选择\*\*"新建POC"\*\*即可自动生成基于 *pocsuite3* 框架的标准化 POC 结构，包含 **vulID**、name、*author*、type、level、cve 等元数据字段，以及 **\_verify**、\_attack、*check* 三个核心方法模板。支持 **SQL注入**、命令执行、*文件读取* 等常见漏洞类型选择，自动填充对应检测逻辑框架，减少 80% 的重复代码编写工作。

### 2. 漏洞管理平台无缝集成

  插件深度集成漏洞管理平台，在 POC 文件编辑器中右键选择\*\*"提交POC"**，自动解析文件中的元数据（如漏洞名称、危害等级、CVE 编号等），智能判断漏洞记录是否存在：已存在则**自动更新\*\*，不存在则创建新记录。支持 *HTTP/HTTPS* 协议，配置简单（仅需设置平台地址、用户名、密码），实现**开发-提交-管理**闭环。

### 3. 代码片段智能补全

  内置多个实用代码片段，输入 **poc** 前缀按 Tab 键即可插入完整 POC 模板，输入 *get\_files\_info* 或 read\_file 快速插入文件操作相关代码。覆盖 POC 开发中的高频代码模式，配合 VSCode 的 IntelliSense 功能，大幅降低**记忆成本**和*输入错误*。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| VSCode Extension API | 原生插件架构 | 与 IDE 深度集成，体验流畅 |
| pocsuite3 框架 | 知道创宇开源 POC 框架 | 行业标准，兼容性强 |
| Node.js 18+ | 异步事件驱动 | 性能优异，生态丰富 |
| Webpack 打包 | 模块化构建 | 体积优化，加载快速 |
| 配置验证机制 | 启动时检查登录配置 | 错误前置，减少排查成本 |

## 📖 使用指南

① **准备工作**：克隆仓库后执行 npm install 安装依赖，运行 npm i --save-dev webpack webpack-cli 和 npm install -g vsce 安装打包工具。在 VSCode 设置中搜索 *login*，配置 **login.url**、login.username 和 *login.password*。

② **核心操作**：在资源管理器右键目标文件夹，选择 **"新建POC"**，选择漏洞类型（如 *SQL注入*）后自动生成模板。编辑完成后，在编辑器中右键选择 "提交POC"，系统自动解析元数据并推送至平台。

③ **结果查看**：提交成功后，登录漏洞管理平台查看已创建的漏洞记录。使用快捷键 **Ctrl + Shift + L** 可快速创建本地扫描任务（开发中），生成的 POC 文件可直接在 pocsuite3 环境中运行验证。

## 📖 项目地址

```
https://github.com/u1hine/vscode-plugin-poc
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

| ![img](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODwHdUbwzDLq3nh7hplKZNDBERhMYooic5cPGwPHEJRonMYCoupeaa6fPuwOKehMek9HTEvnLaG0uuiaScGxWWmibtK9XNFHF4PJD0/640?wx_fmt=jpeg&from=appmsg) | ![img](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwTIuKGmnGNWdp04KFRDHLuy2sn430a7pFSLwaOhaAb2sddKZ3uDapQ5II45nXqiaUicl8IXcdcpazmOVgV0o1v63mbpXicFlZYibQ/640?wx_fmt=png&from=appmsg) |
| --- | --- |
| ![img](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxHicicgIE0gTVhia5o7wNZiaPBibHFSAbvchW91fT05Nhp3rnNNDmoiauT4jK4JBicGHSBwFvcABEjrMB9fhnQc7xGkVx2t52CKzLW4k/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODzCtog7ElLXnrLg7t9j99DftdLLjjVKFwP6unsUPX1EquflicE51wMFjB3zIBWLf6W3qFHA5modicNn3XbwJE8roDq7njXZRfjuo/640?wx_fmt=jpeg&from=appmsg) |

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