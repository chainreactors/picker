---
title: fscan 1.8.4 魔改&可视化&免杀定制版
url: https://mp.weixin.qq.com/s/myy58ap9BqBWrCVpHxK-Uw
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:54:05.827911
---

# fscan 1.8.4 魔改&可视化&免杀定制版

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rl85Sib8ZkaDbGy4EeVNc6vib5uOQaA3O7kQjMFHDDP5XLTOBwQwNcbmwEPFQQE0I6pBpT8utaiayfkCy2icATyYJQ/0?wx_fmt=jpeg)

# fscan 1.8.4 魔改&可视化&免杀定制版

原创

zyxa
zyxa

众亦信安

![]()

在小说阅读器中沉浸阅读

**声明：**文中涉及到的技术和工具，仅供学习使用，禁止从事任何非法活动，如因此造成的直接或间接损失，均由使用者自行承担责任。

**众亦信安，中意你啊！**

****温馨提示：当前公众号推送机制调整，仅常读及星标账号可展示大图推送。建议各位将众亦信安团队设为“星标“，以便及时接收我们的最新内容与技术分享。****

****![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaBrDvy8TKfP3pmENHPYQRvnyeL0ZcfqYJgXwahwgVIzqAslfCe4QPMCdyqwsVP4AE4VsMAkIkju7Q/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)****

      本文档详细介绍了基于 fscan 1.8.4 进行的深度定制与增强。本项目保留了原版强大的内网综合扫描能力，并在此基础上重点重构了 Web 漏洞验证体验、扩展了 POC 兼容性，并进行了工程化的体积与依赖优化。

我可以作为标题

一、 WebUI 界面交互重构

原版 WebUI 在进行漏洞验证时，操作流程较为单向且结果展示拥挤。本次更新对 WebUI 进行了完全重构，核心逻辑改为“结果导向，按需编辑”。

1.1 验证结果优先展示

* **改动点**：点击“验证”按钮后，不再直接显示编辑框，而是优先展示本次验证的 **完整 HTTP 请求包** 和 **响应包**。
* **优势**：

+ 渗透测试人员可以第一时间确认漏洞是否存在，无需被编辑框干扰。
+ 采用 `pre` 标签配合自动滚动条（`overflow: auto`），完美支持长报文（如超长 Payload 或大体积响应体）的查看，避免撑爆页面布局。

### 1.2 "编辑并重发" 模式

* **改动点**：在结果展示区下方新增 **“编辑并重发”** 按钮。点击后才会展开请求编辑区域。
* **逻辑优化**：

+ 编辑框默认自动填充上一次发送的原始请求包。
+ 用户可以在此基础上修改 Headers、Body 或参数，点击“发送”后，页面会刷新展示新的请求与响应结果。
+ 这种设计模仿了 Burp Suite Repeater 的工作流，更符合专业人员的使用习惯。

### 1.3 视觉与样式优化

* **主题**：统一为清爽的白色主题，提升长时间阅读的舒适度。
* **布局**：请求与响应区域通过明显的分割线与边框区分，层次分明。

![](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaDbGy4EeVNc6vib5uOQaA3O737tfwJknRIXFCu0Fqj8RF9KNgC1gbIibJ3fibh1iaSeeic3mqkoNZd3crQ/640?wx_fmt=png&from=appmsg)

二、 Nuclei POC 引擎支持

2.1 智能双格式支持

* **原理**：修改了 POC 加载器 (`WebScan/lib/client.go`)，在读取 YAML 文件时会自动识别格式。

+ 优先尝试按 fscan 原生格式解析。
+ 如果解析失败或特征不符，自动切换为 Nuclei 格式解析器。

* **用法**：用户无需增加额外参数，只需通过 `-pocpath` 指定 YAML 文件或目录即可。

  ```
  fscan.exe -pocpath ./nuclei-pocs/ -u http://example.com
  ```

### 2.2 核心字段映射

实现了将 Nuclei 的核心逻辑映射为 fscan 的 CEL 表达式：

* **Matchers 转换**：

+ `status` -> `response.status == code`
+ `word` -> `response.body.bcontains(b"keyword")`
+ `regex` -> 自动转换为 CEL 正则匹配函数

* **Requests 转换**：

+ 自动解析 Nuclei 的 `Raw` 请求或 `Method/Path` 结构，转换为 fscan 的发包规则。
+ 支持 `{{BaseURL}}` 等标准变量替换。

![](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaDvbakzPN2tj7Y9QDPkyDhFGicwiaWBMoJoBazQeSpKB5Kzt3DTAeK0PA7rrJrOAjpibyY8wiaibUg8ZRg/640?wx_fmt=png&from=appmsg)

三、 ICMP 存活探测机制

本项目内置了高效的 ICMP 存活探测模块 (`Plugins/icmp.go`)，采用 **三级降级策略** 确保在各种权限与网络环境下均能工作。

1. **Level 1: Raw Socket 批量监听 (最快)**

* 当拥有 Root/Administrator 权限时，直接监听本地 ICMP 协议栈。
* 并发发送 ICMP Echo Request，单线程异步接收所有回包。
* 速度极快，适合大网段扫描。

2. **Level 2: 标准 ICMP Dial (非特权)**

* 如果 Raw Socket 监听失败，尝试使用 Go 标准库的 `net.Dial("ip4:icmp")`。
* 适用于部分受限环境。

3. **Level 3: 系统 Ping 命令 (兼容性)**

* 如果以上均失败（如极为严格的容器环境），自动降级调用系统 `ping` 命令（Windows/Linux/MacOS）。
* 解析系统命令输出判断存活，确保兜底可用。

四、 未授权访问扫描增强

集成了多种常见服务与中间件的未授权访问/弱口令检测插件，无需配置字典即可自动探测：

* **Docker API 未授权**：检查 `/version` 接口是否暴露。
* **Jenkins 未授权**：检查 `/manage` 面板是否允许匿名访问。
* **MQTT 未授权**：尝试建立匿名 MQTT 连接。
* **Redis 未授权**：尝试无密码连接 Redis 服务。
* **MongoDB 未授权**：尝试无认证列出数据库。
* **Memcached 未授权**：尝试执行 `stats` 命令。
* **Zookeeper 未授权**：尝试执行 `envi` 命令获取环境信息。
* **Elasticsearch 未授权**：检查 `/_cat` 或根路径信息。
* **FCGI (PHP-FPM) 未授权 RCE**：通过构造 FastCGI 协议包尝试执行命令。

![](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaDvbakzPN2tj7Y9QDPkyDhFKUshC3KMb2toTyL8o5FzFX1Na27OayIN8r2oN5H6CNNacJpS5dicmRw/640?wx_fmt=png&from=appmsg)

五、 工程化与体积优化

5.1 本地模块化 (Go Module)

* **去依赖**：移除了对 `github.com/shadow1ng/fscan` 远程库的依赖，`go.mod` 模块名更名为 `fscan`。
* **全本地引用**：所有 import 路径均指向本地源码 (`fscan/Plugins`, `fscan/common` 等)，彻底解决了二次开发时的包引用冲突问题，并支持离线编译。

### 5.2 体积瘦身

* **编译参数**：

+ 使用 `-trimpath` 移除二进制中的绝对路径信息。
+ 使用 `-ldflags "-s -w"` 去除符号表和 DWARF 调试信息。

* **成果**：

+ 可执行文件体积减少约 **20%** (从 ~52MB 降至 ~41MB)，且功能无损。

六、 快速开始

常用命令

```
在项目根目录执行编译go build -trimpath -ldflags "-s -w" -o fscan.exe
1. 默认扫描 (包含 ICMP 发现、端口扫描、漏洞探测)fscan.exe -h 192.168.1.0/24结果默认保存到本地result.txt
2. 指定 Nuclei POC 扫描fscan.exe -pocpath ./pocs/cve-2023-xxxx.yaml -u http://target.com
3. 启动 WebUI (端口 8787)fscan.exe -web -web-port 8787访问 http://127.0.0.1:8787 进行可视化漏洞验证
4. 指定文件 -web-loadff.exe -web -web-port 8080 -web-load 1.txt开启8080端口扫描本地1.txt文件
```

测试免杀时效截止2026.1.23

360

![](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaDvbakzPN2tj7Y9QDPkyDhFQxoPWrdCgbQhh9r7tuKlvLeBX9WBbHtss9fu7iaWmht3KJtAun9GicUg/640?wx_fmt=png&from=appmsg)

火绒

![](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaDvbakzPN2tj7Y9QDPkyDhFH3C1BAcrUseMwOYx09g7QMEYJNTLTtLkbDic8Ys39QnBXlz8Fia90vPw/640?wx_fmt=png&from=appmsg)

windf

![](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaDvbakzPN2tj7Y9QDPkyDhFEaHzibdEc2E6dd862V0Vib6ic8lj6KGYFZ2Vl0K4MLwzNsseick1eOiaM4g/640?wx_fmt=png&from=appmsg)

后续功能持续迭代中.....

tips：

圈子专注于渗透测试、漏洞挖掘、免杀对抗、逆向分析四大核心方向，同时提供各类实战工具、0day 情报与长期更新的技术资源。目前已更新包括 suo5 二开（含流量修改及客户端工具）、哥斯拉特战版二开（持续维护）、以及 0day 披露等内容。

未来还将陆续上线自研 webshell 管理工具、CS 远控定制版本、内网漏洞批量检测工具（fscan 二开 web 界面）、src 与 edu 高赏金积分报告（脱敏）、以及历年 hw 实战案例复盘等深度内容，致力于打造一个真正能提升技术、辅助实战的高质量交流圈。

目前定价 129 / 年，前 30 名入圈师傅可享 85 折优惠，欢迎各位热爱技术的师傅加入，一起交流、一起进步。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/rl85Sib8ZkaBrDvy8TKfP3pmENHPYQRvnoUJruepz5RIakgWW15WoZlx0GwZl7t32HZLbGzw6Es3o0LNVcicrUdA/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

盒子

![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzYAmqmVyLA140bY25X4CBspqHHIdchuvl5bTtXqjEZWH6oEdricIUiaNw/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzrJoCPp65LU8vOvfiaZ9azEZaiacT4HWN9BjAQibgve4Jwhp2S6H91vYbw/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzIc7ibNTL1yqTC9icFDaMaHUtRiccsy6Arnq9KZwBJVhHtIpoibz12VEvgA/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uz4VYVzN5xicYdBt62M6vo2icO8NjQlCaKibkMu15obIz9EnXe0alwSkm1A/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

携程

![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzQm262GVX0fMUqBQP3hZ3kFNO3EnrRdlYU6ODSQhfsac4fXu0DggE7w/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

小红书总榜第二第三

![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzyynyEXxX43C2Dn95nqZVLt0ElQb0eb9jqT1HRO8W3VQiaibpXkzNlI7w/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uz6sT5VB2NhebTS27LRTg6rqcJcPCV35ictQMWD5qqxEKvG4BK6UXoNrw/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

攻防

![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzR87BIcxwa5feaKA3IWcibefB5pkNUGy4q8HKTucczg1MAk1CFdpyBKg/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzMbWx5FD5Sia3vMfoCBDC4gs3avOaeKP7xUkwNcOUMiardqEm7roQsMxg/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzpAONs33icjw7rDANxt444wAfEZNQLVia0Qs7Fxpmb0ExFOMQfsKIbrZQ/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzudOB49nibPxwwcInGibS06Dd24s3PGLWYZ51jaicDYxBXfvUrM9kxX6bQ/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaBrDvy8TKfP3pmENHPYQRvnxX6pJGD61jba1mLFcdJ16Lg0AW9WmsEBAnFgaTAWeytqPKQXiaLX2Kw/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaBrDvy8TKfP3pmENHPYQRvn4BF5iap2jTibQeibicg5Spuhze3QZtVwNrKvriaJqz9l677mRGwVluW2tBg/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17)

![](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaDUh1duUKheR8XDZMPUr38fXNqibjA1IcBUbPhPLib8NK7KGl9Y3vdZ9CAMcibvH5XwUYrGV7KmY66kQ/640?wx_fmt=png&from=appmsg)
...