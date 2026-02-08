---
title: 最新二开 fscan 发布：免杀突破火绒 360，流量伪装再升级
url: https://mp.weixin.qq.com/s/HPzGdn9yuhpYzEGJH2khFg
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:28:23.215303
---

# 最新二开 fscan 发布：免杀突破火绒 360，流量伪装再升级

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2kmmuqK1icBIFl6SWLgyhfe5ibnFKhzhicxwINCgOHaUw42jNSibqiaVeyibu08Dm6WaCbb0TA41icopqOuw/0?wx_fmt=jpeg)

# 最新二开 fscan 发布：免杀突破火绒 360，流量伪装再升级

原创

星夜AI安全
星夜AI安全

星夜AI安全

![]()

在小说阅读器中沉浸阅读

📌各位可以将公众号设为星标⭐

📌这样就不会错过每期的推荐内容啦~

📌这对我真的很重要！

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kmmuqK1icBIFl6SWLgyhfe57xGuwEp15BTR4NNichFoqP3BQELMgFMhKKFI3nLJ8b07ujSM5CMhNpw/640?wx_fmt=png&from=appmsg)

📌1. 本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。

📌2. 所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。

📌3. 使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。 漏洞曝光！微软SharePoint再度遭高手攻破，Pwn2Own专项攻击成功突破！

---

## 1. 端口扫描与服务识别流量特征优化

* **扫描速率扰动**：

+ 端口扫描和服务识别的每次连接、探测包发送前后都会有10-100ms的随机sleep，避免流量过于规律。

* **探测包内容扰动**：

+ 服务识别时，探测包有10%概率被插入无害字节（如空格、换行），扰乱特征。

* **预留TCP参数伪装注释**：

+ 代码中已预留自定义Dialer位置，后续可进一步实现Window/TTL/Options等TCP参数伪装。

---

## 2. Web扫描流量优化

* **Referer 随机化**：每次HTTP请求自动随机设置Referer头（如百度、Google、Bing等）。
* **Cookie 随机化**：每次HTTP请求自动生成随机sessionid，模拟真实用户Cookie。
* **X-Forwarded-For 随机化**：每次HTTP请求自动生成随机IP，伪装真实来源。
* **请求速率扰动**：每次HTTP请求前可插入微小随机延迟。
* **基础头部伪装**：User-Agent、Accept、Accept-Language等已实现随机化。

---

## 3. 爆破与弱口令检测优化

* **用户名/密码顺序扰动**：爆破前会打乱用户名、密码和最终组合顺序，避免被WAF/IDS检测到固定顺序。
* **爆破速率扰动**：每次尝试前sleep 50-200ms，每次连接后sleep 10-50ms，模拟真实用户操作，降低被风控识别的概率。
* **连接行为模拟**：每次尝试和重试之间均有延迟，行为更接近真实用户。

---

## 4. 日志与结果输出优化

* **全局静默模式（Silent）**：只需设置`Common.Silent = true`即可完全静默运行，不输出任何日志。
* **进度条显示**：支持实时显示扫描进度，可通过`Common.ShowProgress`控制。
* **慢速日志输出**：通过`Common.SlowLogOutput`控制日志输出速度，模拟人工操作。
* **彩色输出控制**：通过`Common.NoColor`控制是否使用彩色输出。

---

## 5. 新增功能配置参数

### 5.1 CEL表达式评估引擎

#### 基础配置参数

* **POC并发数** (`-num`): 控制POC扫描的并发数量，默认20
* **完整扫描** (`-full`): 启用完整扫描模式，包含更多检测项
* **DNS日志验证** (`-dns`): 启用DNS日志验证功能
* **POC路径** (`-pocpath`): 指定自定义POC脚本路径
* **POC名称** (`-pocname`): 指定特定的POC脚本名称

#### 内置函数列表

**字符串处理函数：**

* `bcontains(s, substr)`: 检查字符串是否包含子串（区分大小写）
* `bmatches(s, pattern)`: 正则表达式匹配（区分大小写）
* `icontains(s, substr)`: 检查字符串是否包含子串（不区分大小写）
* `imatches(s, pattern)`: 正则表达式匹配（不区分大小写）
* `startsWith(s, prefix)`: 检查字符串是否以指定前缀开头
* `endsWith(s, suffix)`: 检查字符串是否以指定后缀结尾
* `len(s)`: 获取字符串长度
* `substr(s, start, end)`: 提取子字符串
* `trim(s)`: 去除字符串首尾空白字符
* `split(s, delimiter)`: 按分隔符分割字符串
* `join(list, separator)`: 将列表元素用分隔符连接

**编码解码函数：**

* `base64(s)`: Base64编码
* `base64_decode(s)`: Base64解码
* `urlencode(s)`: URL编码
* `urldecode(s)`: URL解码
* `hexencode(s)`: 十六进制编码
* `hexdecode(s)`: 十六进制解码
* `md5(s)`: MD5哈希计算
* `sha1(s)`: SHA1哈希计算
* `sha256(s)`: SHA256哈希计算

**随机数生成函数：**

* `randomInt(min, max)`: 生成指定范围内的随机整数
* `randomString(length)`: 生成指定长度的随机字符串
* `randomLowercase(length)`: 生成指定长度的随机小写字母字符串
* `randomUppercase(length)`: 生成指定长度的随机大写字母字符串
* `randomLowercaseNumber(length)`: 生成指定长度的随机小写字母和数字字符串

**特殊功能函数：**

* `wait(seconds)`: 等待指定秒数
* `TDdate()`: 获取当前时间戳
* `shirokey()`: 生成Shiro框架密钥
* `concat(...args)`: 连接多个字符串
* `reverse(s)`: 反转字符串
* `repeat(s, count)`: 重复字符串指定次数

#### POC配置参数

* **请求方法**: GET、POST、PUT、DELETE等
* **请求路径**: 目标路径，支持变量替换
* **请求头**: 自定义HTTP请求头
* **请求体**: POST请求的数据体
* **表达式**: CEL表达式用于结果判断
* **规则匹配**: 响应内容匹配规则

### 5.2 Web扫描增强功能

#### HTTP请求处理优化

* **超时控制** (`-wt`): Web请求超时时间，默认5秒
* **代理支持**:

+ HTTP代理 (`-proxy`): 支持HTTP代理
+ SOCKS5代理 (`-socks5`): 支持SOCKS5代理

* **Cookie管理** (`-cookie`): 自定义Cookie信息

#### Web扫描控制参数

* **目标URL** (`-u`): 单个目标URL
* **URL文件** (`-uf`): 包含URL列表的文件
* **扫描模式**: 支持多种Web扫描模式

### 5.3 扫描模式与插件管理

#### 扫描模式配置

* **全扫描模式** (`-m all`): 执行所有可用插件
* **自定义模式** (`-m plugin1,plugin2`): 指定特定插件
* **本地模式** (`-local`): 仅执行本地信息收集

#### 插件分类说明

* **服务插件**: 网络服务扫描（SSH、FTP、数据库等）
* **Web插件**: Web应用扫描（标题、指纹、漏洞等）
* **本地插件**: 本地信息收集（系统信息、网络配置等）

#### 本地模式支持

* **系统信息收集**: 操作系统、版本、架构等
* **网络配置**: 网络接口、路由表、DNS配置等
* **用户信息**: 用户账户、权限、组信息等

### 5.4 输出与显示控制

#### 输出格式控制

* **文本格式** (`-f txt`): 纯文本输出
* **JSON格式** (`-f json`): JSON结构化输出
* **CSV格式** (`-f csv`): CSV表格输出（增强版）

#### 显示控制选项

* **静默模式** (`-silent`): 完全静默运行
* **无颜色输出** (`-nocolor`): 禁用彩色输出
* **日志级别** (`-log`): 控制日志输出级别
* **进度显示** (`-pg`): 显示扫描进度
* **扫描计划** (`-sp`): 显示详细扫描计划

---

## 6. 增强CSV输出功能

### 6.1 新增CSV格式特性

当选择CSV输出格式时，系统会自动生成包含22个详细列的增强CSV文件，提供更全面和美观的扫描结果展示。

#### CSV列头说明

| 列名 | 说明 | 示例 |
| --- | --- | --- |
| 发现时间 | 扫描结果发现的时间戳 | 2024-01-15 14:30:25 |
| 结果类型 | 扫描结果的类型分类 | HOST/PORT/SERVICE/VULN |
| IP地址 | 目标主机的IP地址 | 192.168.1.100 |
| 网段 | 目标IP所属的网段 | 192.168.1.0/24 |
| 端口 | 开放的端口号 | 80,443,22 |
| URL | 完整的URL地址 | http://192.168.1.100:8080 |
| 网站标题 | Web页面的标题 | Apache2 Ubuntu Default Page |
| 服务名称 | 识别出的服务名称 | http,ssh,mysql |
| 版本 | 服务版本信息 | 2.4.41,8.0.26 |
| 主机名 | 目标主机的主机名 | web-server-01 |
| 操作系统 | 目标主机的操作系统 | Windows 10,Ubuntu 20.04 |
| 设备类型 | 自动推断的设备类型 | Web服务器,数据库服务器,个人主机 |
| 漏洞情况 | 发现的漏洞或风险等级 | 发现漏洞,高风险服务,正常 |
| 状态 | 扫描结果状态 | alive,open,identified,vulnerable |
| 服务横幅 | 服务返回的横幅信息 | SSH-2.0-OpenSSH\_8.2p1 |
| 产品信息 | 产品名称和厂商信息 | Apache/2.4.41,MySQL/8.0.26 |
| 域名 | 相关的域名信息 | example.com |
| 协议 | 使用的协议类型 | HTTP,HTTPS,SSH |
| HTTP状态码 | Web响应的状态码 | 200,404,500 |
| 内容长度 | Web响应的内容长度 | 1234 |
| 指纹信息 | 识别出的技术指纹 | Apache,Ubuntu,PHP |
| 详细信息 | 其他详细信息 | 格式：key=value; key2=value2 |

### 6.2 设备类型自动分类

系统会根据扫描结果自动推断设备类型，包括：

* **数据库服务器**: MySQL、MSSQL、Oracle、PostgreSQL、Redis、MongoDB等
* **Web服务器**: Apache、Nginx、IIS、Tomcat等
* **文件服务器**: FTP、SMB、NFS、Rsync等
* **远程访问服务器**: SSH、Telnet、RDP、VNC等
* **邮件服务器**: SMTP、POP3、IMAP等
* **网络设备**: 路由器、交换机等
* **打印机**: 网络打印机、IPP服务等
* **工业控制系统**: Modbus、S7、Ethernet/IP等
* **个人主机**: Windows、Linux、Mac等个人计算机
* **未知设备**: 无法分类的设备

### 6.3 漏洞情况评估

系统会自动评估扫描结果的风险等级：

* **发现漏洞**: 明确发现的安全漏洞
* **高风险服务**: Telnet、FTP、Redis等高风险服务
* **中风险服务**: SSH、RDP、VNC等需要认证的服务
* **正常**: 未发现明显风险的服务

### 6.4 使用示例

#### 基本使用

```
扫描目标并输出CSV格式结果
./fscan -h 192.168.1.0/24 -f csv -o scan_results.csv

扫描Web服务并输出详细CSV
./fscan -u http://example.com -f csv -o web_scan.csv

全扫描模式输出CSV
./fscan -h 192.168.1.0/24 -m all -f csv -o full_scan.csv
```

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kmmuqK1icBIFl6SWLgyhfe5Tlxv6XVicjFE5Z2oRxGziajfKzVzGnVGy7FqM2zWWvbt0KVrFByn75BA/640?wx_fmt=png&from=appmsg)

#### CSV输出示例

发现时间,结果类型,IP地址,网段,端口,URL,网站标题,服务名称,版本,主机名,操作系统,设备类型,漏洞情况,状态,服务横幅,产品信息,域名,协议,HTTP状态码,内容长度,指纹信息,详细信息等等

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kmmuqK1icBIFl6SWLgyhfe5iaI3tF0OIKftt8yBZVmA7odrff1TzeBZicXTHVNaO80dDU0AjEiaqSqSw/640?wx_fmt=png&from=appmsg)

### 6.5 优势特性

1. **信息完整性**: 包含扫描过程中的所有关键信息
2. **自动分类**: 智能推断设备类型和风险等级
3. **结构化展示**: 清晰的列头和数据组织
4. **易于分析**: 支持Excel等工具进行数据分析
5. **中文友好**: 使用中文列头，便于理解
6. **扩展性强**: 可根据需要添加新的列和分类

### 6.6 注意事项

* CSV文件使用UTF-8编码，确保中文正确显示
* 某些字段可能为空，这是正常现象
* 建议使用Excel或WPS等工具打开CSV文件以获得最佳显示效果
* 大文件建议分批处理以提高性能

#### 免杀效果

火绒

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kmmuqK1icBIFl6SWLgyhfe5whby5KC7DU7kny2NRvcWxwNF4apqv3eKexib9qZ2TMAe4O7P3l23PlA/640?wx_fmt=png&from=appmsg)

360

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kmmuqK1icBIFl6SWLgyhfe5C7V3g1lFAl54EJ3KB6cGdHq44icQeIwpwyKfVBqIYRwq9dO3UbPalkw/640?wx_fmt=png&from=appmsg)

关注微信公众号后台回复**入群** 即可加入星夜AI安全交流群

## 圈子介绍

现任职于某头部网络安全企业攻防研究部，核心红队成员。2021-2023年间累计参与40+场国家级、行业级攻防实战演练，精通漏洞挖掘、红蓝对抗策略制定、恶意代码分析、内网横向渗透及应急响应等技术领域。在多次大型演练中，主导突破多个高防护目标网络，曾获“最佳攻击手”“突出贡献个人”等荣誉。

已产出的安全工具及成果包括：

* 多款主流杀软通杀工具（覆盖卡巴斯基、诺顿、瑞星等）
* Metasploit定制化模块（含漏洞利用payload免杀版本）
* 全自动信息收集平台（集成资产测绘、端口扫描、指纹识别）
* 内网穿透套件（支持多层网络环境下的流量转发）
* 权限维持工具集（含注册表、服务、进程隐藏等多种持久化方式）
* 哥斯拉/冰蝎定制化马生成器（可绕过主流终端防护与EDR）
* 日志清理工具（针对Windows/Linux系统关键日志的无痕删除）
* 浏览器凭证窃取工具（支持Chrome/Edge/Firefox等主流浏览器）
* 企业VPN漏洞利用工具（适配多款商用VPN设备）
* 工控系统专用扫描器（针对SCADA、PLC等设备的安全检测）
* 邮件钓鱼平台（含模板生成、追踪统计功能）
* 社工信息聚合工具（整合多平台公开信息检索）

后续将不断更新到内部圈子中 欢迎加入圈子

![](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2kmmuqK1icBIFl6SWLgyhfe5M0C8S3PDcSJjS8sGKAW9bBeDxnqe0emRL2CARSkDXCZRibAAOQ2LKDg/640?wx_fmt=jpeg&from=appmsg)

```
只要全力以赴，就无所谓失败
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2kmmuqK1icBIFl6SWLgyhfe58lFVicJia1PYk5DTicXkwtBOqshob5CBHaSaYaBxa4YF2iaia1Q6BPS5wRA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kDRUZoVyoQSFNmAaYwluEFTjXAgQILjvqxkG8dwdfCP3ia9vzvl09Te62lH6VjoGcL2txz...