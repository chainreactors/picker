---
title: wireshark的高级使用
url: https://mp.weixin.qq.com/s/kAm-_84dd1S1TJIaGnupUw
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:21:01.969228
---

# wireshark的高级使用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/njicUbJnVlIwn340vpxvTCzE0Md8gueG0x0yNyRyjV1Ae1jg1YvMWwKHPDxXTKsnyZvWkqAqnjs8EeMr6hhhtnW0pLbfiaJaicXFSwYVbYsYUI/0?wx_fmt=jpeg)

# wireshark的高级使用

原创

书中自有代码来
书中自有代码来

书中自有代码来

![]()

在小说阅读器中沉浸阅读

# 个性化配置

### 1. 数据流颜色标记

通过颜色快速识别异常流量或特定协议，提升视觉分析效率。

1. **操作路径**：`视图 (View)` → `着色规则 (Coloring Rules)` 。
2. **操作步骤**：

* **新建规则**

  ：点击 `+` 号，命名规则（如 "HTTP 5xx Error"）。
* **编写过滤器**

  ：输入逻辑表达式，例如 `http.response.code >= 500` 设为红底黑字，`tcp.flags.reset == 1` 设为黑底红字以警示连接重置。
* **优先级管理**

  ：列表越靠上的规则优先级越高。若多个规则匹配同一个包，仅显示最上方规则的颜色。利用上下箭头调整顺序。
* **作用域**

  ：可选择仅应用于当前配置文件或全局生效。

![](https://mmbiz.qpic.cn/mmbiz_png/njicUbJnVlIzc8CLic3EY4cX5Z0edayOyI57HAoV6EMWOhl7cFmyl9jnZiaDFwBBJXymoMj5OAhT3LibJSRypAuUL6onAficBZia7kwuJpMV8RMPQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/njicUbJnVlIwHib4mfhhYe6Vzuh6vxeo6U8ZN1T9iavdbuQ06ibkZ0iba5MW2gAQkUwPoHic60IUL8CCggyYSeppI7epHUtFduK2iaCwE7MkeIZrYU/640?wx_fmt=png&from=appmsg)

### 自定义界面布局

1. **视图模式切换**：`编辑(Edit)`→`首选项(Preference)` → `外观 (Appearance)` → `布局 (Layout)`：可选择垂直排列（详情在字节流上方）或水平排列（详情在字节流左侧）等，适应不同屏幕分辨率。
2. **列管理**：右键点击列标题栏，勾选所需字段（如 `Delta Time`, `Source Port`），或直接拖拽列标题调整顺序和宽度，可在`编辑(Edit)`→`首选项(Preference)` → `外观 (Appearance)` → `列`修改和增加。
3. **字体优化**：`编辑(Edit)`→`首选项(Preference)` → `外观 (Appearance)` → `字体和颜色` ，可调整字体大小和家族，便于在高分屏下清晰阅读。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/njicUbJnVlIyrhibV2DKfDibgqPk1a0H6seT5z9B4Yu1H2iaRoSbCEnp5zSNkM2kUptQYa9ErXlJaXGwS077OmYdD5loicGibENbibwQM6xAa78vqY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/njicUbJnVlIwe3ooEaC8VYDsp8Y8ugxMXLM5Znnib7FTCib3PKGtlKOKXhEiahibkC1F6Wibz02RV9ZpewxRtKlnVJqTy4zaV13ibdNBr9OiccsvFTw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/njicUbJnVlIwoZBBmLEzfNOWoTQh8OMT0KlEz2c7ccDl96mhfgYGkmj7WicwTqfibE9wljbl7jBTFxZfRHjyklWic88ibQFVH8evwrsHkxCYWcpY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/njicUbJnVlIxt9eVfa5Zb6hB5m8Totx0bqVdE0iby1JkQraQIwicPahtR3iaD14202AW7D6SC6cHbWAbnibIbobnlL2fUGFQjQn4sN7lDoQlastw/640?wx_fmt=png&from=appmsg)

### 3. 名称解析增强 (Name Resolution)

将枯燥的 IP 地址、端口号和 MAC 地址转换为可读的主机名、服务名和厂商信息。

1. **操作路径**：`编辑` → `首选项` → `名称解析 (Name Resolution)`。
2. **相关设置**：

* **尝试反向解析网络地址**

  ：将 IP 解析为域名（注意：可能产生额外 DNS 流量或增加延迟，内网分析时可关闭）。
* **启用传输层名称解析**

  ：将端口号（如 443）自动显示为协议名（如 `https`）。
* **启用外部解析器**

  ：读取系统 `hosts` 文件或配置 DNS 服务器。
* **MAC 地址解析**

  ：解析前 24 位获取网卡厂商（OUI），若开启 NetBIOS/mDNS 支持，还可尝试解析主机名。

![](https://mmbiz.qpic.cn/mmbiz_png/njicUbJnVlIyaaiblCDT5GC2vqkQ8AWL8l5qIn5ULHH7f0xWECB9bT5xibxyIYR4tFBCzAMPMIlyS8Y4pOf6BiaSGoIbXMLLoicUfVSzjnWRlq6E/640?wx_fmt=png&from=appmsg)

### 4. 时间列显示格式

针对不同分析场景选择合适的时间基准。

1. **操作路径**：`视图` → `时间显示格式`。
2. **常用模式**：

* **自捕获开始起**

  ：默认模式，适合计算相对延迟和响应时间。
* **日期和时间**

  ：适合与系统日志、防火墙日志进行时间轴对齐。
* **UTC 时间**

  ：跨时区团队协作或分析全球分布系统时使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/njicUbJnVlIxibnuEwqpgmOMqL6tPT47XCXEsemCeDtjNdoHVYWFnicjbpQon9u8z2AHWj8ibpCxwYQwmGg01qTsu1PbdN2QLzd1KnHDyp5pMho/640?wx_fmt=png&from=appmsg)

# 包处理与抓包设置

## 图形界面抓包配置

### 接口管理与远程抓包

1. **进入设置**：`捕获 (Capture)` → `选项 (Options)`。
2. **接口筛选**：在列表中勾选常用物理接口，取消隐藏无关虚拟网卡（如 VMware/VirtualBox 适配器），保持界面整洁。
3. **远程抓包**：

* 需确保远程服务器已安装并运行 `rpcapd` 服务。
* 在本机接口名称栏输入格式：`rpcap://<远程IP>:<端口>/<接口名>`。
* **前提**：保证本机与远程服务器网络连通且防火墙放行相应端口（默认 2002）。

### 输出文件管理 (防止文件过大)

长时间抓包容易导致单文件过大，造成打开缓慢或内存溢出。

* **自动创建新文件**

  ：在 `输出 (Output)` 标签页中勾选。

+ **文件大小限制**

  ：建议设置为 `500 MB` 或 `1024 MB`。达到阈值后自动轮转生成新文件。
+ **文件名后缀**

  ：可配置自动添加时间戳或序列号。

* **环形缓冲区 (Ring Buffer)**

  ：

+ 勾选 `自动更新文件列表中的最新文件`。
+ 设置 `文件数上限`（例如 10 个）。
+ **效果**

  ：当文件数达到上限时，自动覆盖最旧的文件。确保持续监控时磁盘空间不被占满，且始终保留最近一段时间的抓包数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/njicUbJnVlIx9eUS4nZBsgbaRwa6EEiceH4vCq7pWVA3MibdxSWHM3P2A7FMgMufSWX6yJYcLNzcb071DdlXuGmV8wJ4YQicq3Av8YACV5icGluw/640?wx_fmt=png&from=appmsg)

## 命令行抓包工具：Dumpcap

*Dumpcap 是 Wireshark 的轻量级底层引擎，无图形界面，资源占用极低，非常适合部署在 Linux 服务器或嵌入式设备上。*

> **部署建议**：推荐将 `dumpcap` 所在目录加入系统环境变量 (`PATH`)，以便在任何路径下直接调用。服务器端通常只安装 dumpcap，抓包完成后将文件下载到本地用 Wireshark GUI 分析。

### 常用命令详解

1. **列出所有可用接口**

   ```
   dumpcap -D
   # 输出示例：1. eth0, 2. lo, 3. docker0 ...
   ```
2. **抓取指定接口的包（实时显示统计）**

   ```
   dumpcap -i 1
   # -i: 指定接口编号（也可使用接口名称，如 -i eth0）
   ```
3. **抓取并保存到指定路径**

   ```
   dumpcap -i 1 -w /var/log/capture.pcapng
   # -w: write，指定输出文件的完整路径
   ```
4. **高级限制：文件大小与数量轮转 (生产环境推荐)**

   ```
   dumpcap -i 1 -w /data/captures/capture.pcapng -b filesize:512000 -b files:10
   ```

* `-b filesize:512000`

  ：每个文件最大 512,000 KB (约 500MB)。
* `-b files:10`

  ：最多保留 10 个文件，存满后自动覆盖最旧的。
* *注：也可使用 `-b duration:60` 按时间切割文件。*

# 包分析核心技巧

## 过滤器：捕获过滤器 、显示过滤器

* **捕获过滤器 (Capture Filter)**

+ **时机**

  ：抓包**开始前**设置。
+ **语法**

  ：BPF 语法，如 `host 192.168.1.1`, `port 80`, `not arp`。
+ **作用**

  ：抓时丢弃不符合条件的包。**一旦开始无法修改**。用于节省磁盘空间和内存，适合高流量环境。

![](https://mmbiz.qpic.cn/mmbiz_png/njicUbJnVlIwpGfF9B39ho09j0N8QlyWIGIialFW9ia0k3zmJDTUFdmFCDMAiaelNnRw2NOh18xNX3o9iaTUbnCBVNbh3fpicaMCZOiahgHiaL2h5dA/640?wx_fmt=png&from=appmsg)

* **显示过滤器 (Display Filter)**

+ **时机**

  ：抓包**过程中**或**结束后**动态调整。
+ **语法**

  ：Wireshark 专有语法，如 `ip.addr == 192.168.1.1`, `http.request.method == "POST"`。
+ **作用**

  ：仅在前端显示时隐藏不匹配的包，原始数据仍保留在文件中。支持随时修改和撤销。

![](https://mmbiz.qpic.cn/mmbiz_png/njicUbJnVlIyOoPDNZELWqOy2B1fqJ9zCU8JCZ3c0DS0g31xpFalBevGgKwI5B5F6XqaC8PlDknos5JnXj52ozTkPRqicj2R4mbKKf36wMVuw/640?wx_fmt=png&from=appmsg)

## 显示过滤器的高级用法

### 1. 利用右键菜单减少错误

手动输入过滤器容易拼写错误，利用上下文菜单更高效：

* **作为过滤器应用**

  ：在数据包详情栏选中某字段（如 `Source IP`），右键 → `作为过滤器应用 (Apply as Filter)` → `选定 (Selected)`，自动生成 `ip.src == x.x.x.x`。
* **准备作为过滤器**

  ：选择 `准备作为过滤器 (Prepare as Filter)`，将条件添加到过滤栏但不立即执行，方便与其他条件组合（如 `and`, `or`）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/njicUbJnVlIx7tFEKWzyVxD2ic8bFuUwYwibCItTibGIAVyRPRS5sCib1cdqHiaQq79n9PF3KClcGrUPTKGoXRzBG4IiaNqFIjUPribWdw32zAtmibro/640?wx_fmt=png&from=appmsg)

### 2. 逻辑运算与排除

* **移除干扰包 (`not` / `!`)**

  ：

+ 例：`!arp and !dns and !llmnr` (排除常见的广播噪音，聚焦业务流量)。

* **组合条件 (`and` / `&&`, `or` / `||`)**

  ：

+ 例：`ip.src == 10.0.0.5 && tcp.port == 443` (只看特定源发的加密流量)。

### 3. 字符串匹配：`contains` vs `matches`

* **`contains` (包含)**

+ **特性**

  ：**区分大小写**。
+ **用途**

  ：精确查找子串。
+ 例：`frame contains "Password"` (只能匹配大写 P，小写 p 会被忽略)。

* **`matches` (正则匹配)**

+ **特性**

  ：支持正则表达式，通常**不区分大小写**（取决于具体正则写法，但 Wireshark 默认行为较灵活）。
+ **用途**

  ：模糊匹配、复杂模式查找。
+ 例：`frame matches "[Pp]assword"` (同时匹配大写和小写) 或 `http.host matches ".*\.api\.example\.com"`。

## 分类统计与会话分析 (Statistics)

当数据包数量巨大时，宏观统计比逐个查看更有效。

* **对话统计 (Conversations)**

+ 路径：`统计 (Statistics)` → `对话 (Conversations)`。
+ **功能**

  ：列出所有通信对（IP A ↔ IP B），显示包数、字节数。
+ **技巧**

  ：点击底部的 `追踪 (Follow)` 按钮，可直接生成该会话的显示过滤器，快速定位特定双方的交互。支持以太网、IP、TCP、UDP 等多层级。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/njicUbJnVlIwuXbLBh4t7bS9veicvoQNbia9JUsdFJJD6TJrme3Mjqicvk0fKUSDmXkWEvmkYrr9onu1uCJMiaUjDIL2lzeoRjwv6OiazB8ibahhUA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/njicUbJnVlIwZWtpAds3kibI0LDxwnG3ZKFKP8n8OpwKe10VBJYSQjDloicNNAunibuHkNFwTQ8cmMwUCfuLGqaKkI9rjIxibgHMSpPC9Bc16ia1s/640?wx_fmt=png&from=appmsg)

* **端点统计 (Endpoints)**

+ 查看单个主机的总流量排名，快速定位网络中的“噪嘴”主机或攻击源。

* **协议分层统计 (Protocol Hierarchy)**

+ 以树状图展示各类协议占比，快速判断网络主要承载的业务类型。

## 提取传输的文件

从流量中还原用户传输的实际文件（图片、文档、脚本等）。

* **单文件提取**

  ：

1. 找到文件传输完成的数据包（如 HTTP `200 OK` 或 SMB `Write AndX`）。
2. 右键 → `追踪流 (Follow)` → `TCP/HTTP Stream`。
3. 在弹出的窗口中，若为二进制文件会显示乱码，点击 `保存原始数据 (Save as)` 即可导出。

* **批量导出**

  ：

+ 路径：`文件` → `导出对象 (Export Objects)` → 选择协议 (如 `HTTP`, `SMB`, `IMF`)。
+ 列表会显示所有检测到的文件及其大小，可全选并一键保存到本地文件夹。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/njicUbJnVlIzswIdHeYzgibljh0iazYsbT3lNtkjd6uviciaykLaBgrpCOJ77jXw1oKxlHjdR9TiabhhwCor0vKevKpibkFTghxYutM0ZLBcLnk3HA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/njicUbJnVlIwGw2G6FTGYtRVKdU2ibFynhdpMU6XDu4sogXhtDrjKBTa8WjQcwlHRFvryiciaMTNezib04XwduKlOXsRWuobSedrziaks6icBE0c1Q/640?wx_fmt=png&from=appmsg)

# 注意事项与最佳实践

## 1. 权限与驱动差异

* **管理员权限**

  ：抓包需要访问底层网卡驱动，**必须**拥有管理员权限。

+ *Windows*

  : 右键“以管理员身份运行”。
+ *Linux*

  : 推荐将用户加入 `wireshark` 组 (`sudo usermod -aG wireshark $USER`)，避免...