---
title: 🧿 捡洞神器-AI版越权检测burp插件AutorizePro
url: https://mp.weixin.qq.com/s?__biz=MzU0MzkzOTYzOQ==&mid=2247489510&idx=1&sn=f5acc656368d5ae0c1a5386739e3036e&chksm=fb029abecc7513a8a1b83a23b1f11de6364ba3fa3bdf0bc56aec025e1a3eab701f9c296634cd&scene=58&subscene=0#rd
source: 黑伞安全
date: 2024-10-20
fetch_date: 2025-10-06T18:50:49.656954
---

# 🧿 捡洞神器-AI版越权检测burp插件AutorizePro

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/apmYTPAKhlXGalzutoEhxfcuHbicXyCpCa5ficosuzV5r5ibY7zLGvoNK1liaUGCAVDlSvBFwOQibom4gyTLhTlTy2g/0?wx_fmt=jpeg)

# 🧿 捡洞神器-AI版越权检测burp插件AutorizePro

sule01u

黑伞安全

# 🧿 AutorizePro (AI版上线啦 ❤️‍🔥):

### 工具仓库地址: https://github.com/sule01u/AutorizePro

### AutorizePro 是一款专注于越权检测的 Burp 插件，基于Autorize插件进行二次开发，方便安装易于使用

### 工具背景

* • **越权漏洞在黑盒测试、SRC挖掘中几乎是必测的一项，但手工逐个测试越权漏洞往往会耗费大量时间，而自动化工具又存在大量误报, 基于此产生了AutorizePro**

### 工具亮点

* • **优化检测逻辑 && 增加 AI 分析模块，将原始工具误报率从 99% 降低至 5% ，从海量误报中解脱出来**
* • **对于需要人工确认的告警可通过展示页面并排查看 原始请求、越权请求 以及 未授权请求 的数据包方便对比差异**

### 适用人群

* • 白帽子：释放更多的生产力用于测试强依赖手工测试的接口或功能点上，避免消耗大量精力浪费在手工越权测试 或 迷失在误报之中
* • SDLC工程师: 拥有更全面的接口信息优势之上进一步提升黑盒测试时发现越权这类逻辑漏洞的效率
* • 产品测试：在进行功能测试时可通过结合本插件更早发现此类安全漏洞，让产品基础安全性在产研团队就得以提升

## 🔧 安装AutorizePro

### 1️⃣ 下载 Burp Suite 和 Jython

```
1. 下载 Burp Suite：https://portswigger.net/burp/releases
2. 下载 Jython standalone JAR 文件：https://www.jython.org/download.html
```

### 2️⃣ 配置 Burp Suite 的 Python 环境

```
1. 打开BurpSuite
2.导航到Extender->Options
3.在PythonEnvironment部分，点击SelectFile
4.选择你刚刚下载的Jython standalone JAR 文件
```

### 3️⃣ 安装 AutorizePro 插件

```
1. 下载插件到本地
2.打开BurpSuite，导航到Extender->Extensions->Add
3.在ExtensionType选择框中，选择python
4.在Extension file 选择框中，选择代码仓库中AutorizePro.py 文件路径
```

### AutorizePro 插件安装完成界面 🎉

![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXGalzutoEhxfcuHbicXyCpCJMXnxxLIprN35NibIib5Q4AYtv32ht5BVib3N6eZMKRDrsW4B21FbBZFw/640?wx_fmt=png&from=appmsg)

## 🔫 使用 AutorizePro 插件

```
1. 打开配置选项卡：点击AutorizePro->Configuration。

2.通过fetch cookie header按钮获取最新请求的验证头或手动复制低权限用户的验证头（通常是Cookie或Authorization），并将其复制到标有“Insert injected header here”的文本框中。注意：如果请求中已经包含了该头部，插件会替换现有的头部，否则会添加新头部。

3.如果不需要进行未授权的测试（即不带任何 cookie 的请求，用于检查接口是否存在身份验证，而不仅仅是低权限用户的越权检测），可以取消勾选Check unauthenticated (默认开启)。

4.勾选Intercept requests fromRepeater，通过Repeater发送的请求也会被进行插件处理。

5.点击AutorizeProis off 按钮启用插件，让AutorizePro开始拦截流量，并进行授权检测。

6.打开浏览器，并配置代理设置，使流量能够通过Burp代理。

7.使用高权限用户访问你想测试的应用程序，测试修改类资源时可使用Match/Replace配置越权测试时需要修改的资源信息。

8.在AutorizePro插件的左侧结果展示界面中，你将看到请求的 URL 和对应的权限检查状态。

9.目前仅支持阿里云通义千问 api key(sk开头);如何获取API-KEY: https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key)。

10.当启用 API-Key时，符合AI分析触发条件的请求会交由 AI 进一步分析，结果将展示在 AI.Analyzer列。

11.点击左侧展示页面的某个 URL，可以查看它的原始请求、修改后的请求以及未经身份验证的请求/响应，方便你分辨差异。
```

### 🌠 使用效果示例

> 🌟 大幅降低误报: 从下图中可以看出，启用AI分析后，你只需要去分析一个请求是否真正越权，人工投入的分析精力节约95%以上。

![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXGalzutoEhxfcuHbicXyCpCob1KJpHnLuicl3CR2vAjH0qofYH6XJBtWYR0wEyXia1E5ribP72ibbfqibA/640?wx_fmt=png&from=appmsg)

> 查看AI判定越权的具体请求，可同时展示越权请求、原始请求、未授权请求，方便对比差异

![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXGalzutoEhxfcuHbicXyCpChJibgibyVMD99enKdRYJzxibzfibxLN7GzdgWCfmibdN4NJCicTG1icRAFAgw/640?wx_fmt=png&from=appmsg)

### ❓检测状态说明

* • **Bypassed! (红色) : 判定越权**
* • **Enforced! (绿色) : 判定不存在越权**
* • **Is enforced??? (please configure enforcement detector): 无法判断，可以在 enforcement detector 进一步配置越权特征协助判断**

```
🌟 Tips:

Is enforced???状态表示插件无法确定接口是否做了权限控制，可通过 enforcement detector 进一步配置权限校验特征来辅助判断。

eg:
如果某个接口对于越权访问请求会返回"无权限"这个指纹特征，
你就可以将这个指纹特征添加到EnforcementDetector 过滤器中，这样插件判断时就会查找这个指纹特征，区分出实际已鉴权的接口，减少误报。
```

### 🚰 过滤器配置：在 Interception Filters 配置拦截规则

* • **拦截过滤器位可以配置插件需要拦截哪些域名 或 拦截带有什么特征的请求。**
* • **你可以通过黑名单、白名单、正则表达式或 Burp 的范围内的项目来确定拦截的范围，以避免不必要的域名被 AutorizePro 拦截，减少对不关注的请求的拦截分析。**
* • **🌟 默认配置会避免拦截脚本和图片，你也可以新增更多静态资源类型的忽略规则。**

## 💰 AI分析功能需要花多少钱？

• 为最大程度减少AI分析带来的经费消耗,目前仅检测响应为json格式 && 长度小于3000 的数据包;若不符合条件，AI分析功能将不会生效。

• ⚠️ 注意：当启用AI分析功能时，您应该尽量在 Interception Filters 中配置拦截的 域名 / 规则 以免检测非目标站点带来的经费消耗。

• AI分析功能需要先开通模型调用服务，在 阿里云百炼首页顶部提示 进行开通：

* ![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXGalzutoEhxfcuHbicXyCpCNfHTDalaWGITsickPCr6uUldB2h4pYw15dpqK9UG37jvzqamMibtC1Ew/640?wx_fmt=png&from=appmsg)
* • 阿里云通义千问API计费说明 ( 个人测试消耗示例：在插件开发调试期间全天较高频率测试且没有限制域名，全天消耗总费用**0.38元** )。
* ![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXGalzutoEhxfcuHbicXyCpCnxLoXSYQ7PVNTLhzrAGgq12mecV6YWNIfs6hjAhQVSkPmS7keHcp3w/640?wx_fmt=png&from=appmsg)

* **扫码关注不懂安全获取更多安全分享**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

黑伞安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

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