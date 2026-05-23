---
title: 做个\"脚本小子\"--AI攻防篇
url: https://mp.weixin.qq.com/s/qvNSC-LL5f_79RziqdTjDA
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:33:05.364213
---

# 做个\"脚本小子\"--AI攻防篇

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KvrEnQiahoiaDoia7RT5De8pGPeY2BCibicTZoxTUZYlnLoRCAqXayEMpKePsU4UjO7SvcDSPnKGUQV1ZbSUK7t4ZZpJ4uDwnsqCKOHhXzIBKgaE/0?wx_fmt=jpeg)

# 做个"脚本小子"--AI攻防篇

kingman
kingman

kingman安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

声明:

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者不为此承担任何责任。同时所有相关行为均已取得授权，未经作者同意禁止转载

# 前言

---

最近的AI渗透的火热程度很高

仿佛只要有了AI渗透 下一秒五角大楼都能被打穿

什么？！演示是DVWA？

那这和我挂一个扫描器有什么区别？？？

抱着这样的疑问，这篇文章就此诞生

搭建环境

---

windows物理机->vmware->kali虚拟机

```
https://www.kali.org/get-kali/#kali-virtual-machines
```

在官方站点上下载vmware镜像

![](https://mmbiz.qpic.cn/mmbiz_png/KvrEnQiahoiaAgOtqpe3Ddy64AvgvicPsQ5PyUGk8dFlQyrfeWIfQMk5KnJHgmeHakics4xADbMWE4rZC6mtKxM602c26DrjutAy3ibmuANKZWhQ/640?wx_fmt=png&from=appmsg)

将获取到镜像导入虚拟机

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaC5L2ibtsxCy7dPnxXfsy6h1LBoyUreoSicib9IDicmqDVlxgH33njyaxnUSN0CqoF1MogJ7EaOLdNw7VGFfwfyWbczDWlSK9Sdbmk/640?wx_fmt=png&from=appmsg)

Kali配置

---

* apt换源（直接影响安装ai的快慢）

```
使用 vim 编辑 sources.list 文件：vim /etc/apt/sources.list将官方源注释掉：# deb http://http.kali.org/kali kali-rolling main non-free contrib# deb-src http://http.kali.org/kali kali-rolling main non-free contrib添加国内镜像源选择一个国内镜像源并添加到文件中，例如中科大镜像源：# 中科大镜像源deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contribdeb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
```

* 安装Google浏览器以及Google浏览器对应版本的驱动（ai需求）

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.debgdebi google-chrome-stable_current_amd64.debgoogle-chrome --version随后根据获取的版本号下载对应的驱动wget https://storage.googleapis.com/chrome-for-testing-public/148.0.7778.167/linux64/chromedriver-linux64.zip解压后移动至/usr/local/bin/mv chromedriver-linux64/chromedriver /usr/local/bin/
```

* 安装ai渗透

```
apt install hexstrike-ai安装完成后使用find / -name hexstrike*进行查找
```

![](https://mmbiz.qpic.cn/mmbiz_png/KvrEnQiahoiaDib3icvaDLFWKpwFdUn9ibibacPzLSTZdnnNLad00RL6uLvf6ImmH7CWwn5UB5gLAJwR38bUCCaj4KDWZ0icdibeHwE0QNp5v5tdjHw/640?wx_fmt=png&from=appmsg)

```
我们需要修改hexstrike_server.py中的API_HOST = os.environ.get('HEXSTRIKE_HOST', '0.0.0.0')//从127.0.0.1修改成0.0.0.0此外需要将hexstrike-ai-mcp.json 和 hexstrike_mcp.py复制至windows备用运行hexstrike-server
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaDPAQtIiaphAUfFS394MV6qQDTA0ue9oqqIyN6iaFFg378rmeLGkLyH2dmLWjqPH4S3iaSmJgZ2o8tckErvlVE7l7ibw7VzibdTLWM4/640?wx_fmt=png&from=appmsg)

* 补齐所有渗透工具（可选）

```
最好网络环境很好 不然安装会持续1-3小时apt-get install kali-linux-everything
```

重点

---

其他文章中没讲过的问题 很坑！！！！！

成因：Hexstrike在mcp中写了150+的工具

如果你直接按照官方的Readme.txt将hexstrike-ai-mcp.json

直接作为配置导入到mcp服务器中

那你将面临的问题不是

导入工具不全就是模型卡死

底层逻辑：

由于mcp配置中存在大量函数和文字说明

1个工具用的token会在30-80之间

不算提示词、以及要真实执行的内容

最少已经消耗掉7,500Token

更别提之后多轮对话的上下文等等

有人吐槽：钱而已我多的是！可当我掏出上下文限制，阁下又该怎么应对？

解决方式：

通过MCP代理工具例如Mcpcp

进行代理 MCP加载的时候->搜索一次->调用->返回

对于模型来说，需要做的相较于全加载上下文断供 只需要做一个搜索即可

大幅度减少Token的消耗

安装方式放入windows配置小节中

Windows配置

---

```
我们可以下载cherry studio这种直接桌面端聊天也可以下载编程相关的Visual Studio Code、cursor之类的作为交互媒介如下以Visual Studio Code的Roo插件为例在拓展商店处找到Roo Code
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaD8yQCicsdPt5yUcqLDTnU7vEia4XfoCC0r8Iap0wCyeqhiazTE6GFO1QrQNKNPMUV1rtt7iaE6iaZVWLOR0VQe7yHUjUNn6JQtEphU/640?wx_fmt=png&from=appmsg)

```
安装python3安装nodejshttps://nodejs.org/en/download/环境变量等配置完成之后在cmd中运行npm install -g mcmcp创建一个存放配置文件的目录创建文件mcpcp.json内容如下{  "upstreams": [    {      "id": "hexstrike",      "label": "HexStrike AI",      "transport": "stdio",      "command": "python",      "args": [        "path\to\hexstrike_mcp.py",//从kali中复制出来的文件        "--server",        "http://kali的ip:8888"      ]    }  ]}此处还是以Visual Studio Code举例
```

![](https://mmbiz.qpic.cn/mmbiz_png/KvrEnQiahoiaD97pN4FbKlUwZmArRgRXXnpIbys0iahzC2Z7qc39TUeuOia7WZZvDkXNIuoqlicZ0J0GVHM4icSSkDicIYibOZGqe4ZlyTVuXw2t7yM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaByNDVe8wB22iaLVJDHVj42MaaiblPOGnC2pQHibohp7JEiczXzhtEYP3BJmAlqLXhGBWID7y9DFFs14HViayjQDticTVLohGcsmnqXs/640?wx_fmt=png&from=appmsg)

```
填写的内容如下{    "mcpServers": {        "toolmux": {            "command": "mcmcp",            "args": [                "path\to\mcpcp.json"            ],            "alwaysAllow": [                "search"            ]        }    }}当配置成功时
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaBNb9zv23icTJrb3iaGibicZbFm8EqM6vtdYZdhib6m1fR8mgkgPCJL2WX9KPAnKSA0cH1dWSO9iafliciauNunpSRQ45EnyyqaU4QyCBc/640?wx_fmt=png&from=appmsg)

至此MCP服务器配置成功（相当于让ai拥有调用kali的能力）

关于大模型我们分两种情况讨论

---

情况一：

使用联网大模型优点在于响应速度快、智力水平高

缺点在于离线不可用、需要付费（高智慧模型）

当然 渗透别人的中转站拿token那你当我没说就行

```
以Visual Studio Code举例填入对应的API密钥以及厂商即可
```

![](https://mmbiz.qpic.cn/mmbiz_png/KvrEnQiahoiaCbyOXbZ8U196rjUibt2X9ayc3nlTM6eAhu6GY6VYPsDIg2rDmaGvHGQUQKMaIEIMOfmC4ficd1arWLk1j3amnOm9yUmUBmzMpCY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaBFr0oHBI4vplhz8jSVeibM14Xl3ibqabFeL0icPnFP1fujGX3GibvwibTHFhGmJHuLNDNqptBibNfMJJT6QJrPXKQogsKuowP1G441Y/640?wx_fmt=png&from=appmsg)

情况二：

使用本地量化模型优点在于免费、隐私、不需要联网

缺点在于智力一般般、和你能运行的模型参数有关

主要压力的是显卡硬件-》消费级显卡能力有限

当然你是计算卡或者SLI大法弄了几张5090那也当我没说

```
如果你的显卡显存很好 那么此时我们可以考虑本地量化模型此处推荐使用ollamahttps://ollama.com/安装完成后直接 pull自己想要的模型即可
```

pull模型有两个点值得注意

* 模型参数消费级单卡顶到天35B（数字越小智力越低）
* 此外还需要支持调用工具！否则MCP无法使用

![](https://mmbiz.qpic.cn/mmbiz_png/KvrEnQiahoiaCaXV0jicb3veicL5wbdIy7CR9SQbuIeiciboDfEVjicfFjhsrK80AHTWHRdJOfwbc9cv0KQlo9vvT8Ur79mVRReic9jr8lUFqbyVYDc/640?wx_fmt=png&from=appmsg)

```
挑选适合的模型后即可在cmd中使用pull对应的名字拉取如ollama pull qwen3.5:9b拉取完成后使用ollama serve此时ollama将运行在http://127.0.0.1:11434随后进入visual studio code填入配置即可
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaAbkfrI9xIyJPgUibltzu00iaLvXiavO6OoLRs26K6p1ibLV18EzPBj3oktEvA3kNPGPjBwzHE3J2ccAo9qsmWzpYVyqVvu0sl41vs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/KvrEnQiahoiaDQlWkicAia2SBUYWMno9LxedWvz0YaPIyheFumTa9ia4y8ibvxXibx6zRWHDsoaubVvzgw74iad7o8axgMIxTQpLzgowSzryGwtFqicI/640?wx_fmt=png&from=appmsg)

总结

---

## 一、渗透测试的底层逻辑从未改变

##

不考虑"七分运气三分技术"的玄学成分**投入量与产出比，始终正相关。**

| 方案 | 优势 | 局限 |
| --- | --- | --- |
| 买Token（GPT/Claude等） | 速度快、覆盖面广 | 上下文有限、Token消耗大 |
| 自建集群（本地LLM） | 隐私可控、无限次调用 | 硬件成本高、模型能力天花板 |
| 人工渗透工程师 | 逻辑链条强、经验驱动 | 贵、慢、不可复制 |

---

## 二、AI的统治区：广度碾压

##

在**通常型漏洞挖掘**场景下——SQL注入、XSS、SSRF、基础信息泄露……

这些攻击路径**标准化、模板化、无需复杂推理链**。

> AI比人更全面、更稳定、更不容易遗漏。

这不是AI变强了，是这类活本来就该被自动化取代。

---

## 三、AI的死亡区：逻辑链才是真正的战场

##

真正的渗透从来不是单个漏洞堆叠，而是一条**环环相扣的攻击链例如**：

```
```
注册普通用户
    ↓
越权调用API（身份篡改）
    ↓
添加管理员账户（权限提升）
    ↓
上传WebShell（最终落地）
```
```

每一步都是一个**逻辑陷阱**，AI极易在任意环节断裂。

###

### 举个真实案例：

###

笔者曾遇到一个越权注册管理员的场景——

| 步骤 | 人类能做的 | AI大概率卡住的 |
| --- | --- | --- |
| ① 发现注册接口可调用管理API | ✅ 关联分析 | ✅ 基本能识别 |
| ② 密码需特殊加密格式 | **逆向/抓包分析** | ⚠️ 大概率尝试明文或常用hash |
| ③ 登录流程被改为注册流程（需篡改手机验证码API） | ✅ **理解业务逻辑后主动绕过** | ❌ **无法理解"登录≠注册"的语义差** |

> 这不是AI不够聪明，是**它不懂业务，不懂意图，不懂"人为什么要这么设计"**。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk33j31ajLZ0yloe8cj2zYIaKaL9mGiaX3eEzZ0Y6HH1J15GyY5F0hLZ5GMlILlw81dcxNLoK3hq5cQ/0?wx_fmt=png)

kingman安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk33j31ajLZ0yloe8cj2zYIaKaL9mGiaX3eEzZ0Y6HH1J15GyY5F0hLZ5GMlILlw81dcxNLoK3hq5cQ/0?wx_fmt=png)

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