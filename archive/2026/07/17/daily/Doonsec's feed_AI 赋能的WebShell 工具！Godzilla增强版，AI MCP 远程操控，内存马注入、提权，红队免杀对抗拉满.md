---
title: AI 赋能的WebShell 工具！Godzilla增强版，AI MCP 远程操控，内存马注入、提权，红队免杀对抗拉满
url: https://mp.weixin.qq.com/s/WXrm0GkuiaRPk3AVQsigfA
source: Doonsec's feed
date: 2026-07-17
fetch_date: 2026-07-18T04:44:34.471762
---

# AI 赋能的WebShell 工具！Godzilla增强版，AI MCP 远程操控，内存马注入、提权，红队免杀对抗拉满

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibrevicNauKAUHbqCicazV2IK00yUCgohgquS6ERXon61KIXkzRMomfwRvZVhrInCJDbYUhMgibeaQBiaPWGMcicfT957uV6sxPtNo3OBcZXyYBtE/0?wx_fmt=jpeg)

# AI 赋能的WebShell 工具！Godzilla增强版，AI MCP 远程操控，内存马注入、提权，红队免杀对抗拉满

SelinuxJXM
SelinuxJXM

渗透安全HackTwo

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

0x01 工具介绍

**GodzillaSuper GSL5是基于哥斯拉深度二开的红队后渗透与WebShell管理平台，最新3.1.0版本重磅更新。工具适配多类型WebShell管理，新增NetCore全套载荷与专属插件，搭载AI驱动MCP服务，可对接Claude、Codex实现自动化操控。内置ASM字节码多态混淆、JNI原生执行等RASP绕过能力，支持多类型内存马注入。同时提供单机、内网共享、PG团队协作模式，自带全量操作审计日志，适配合规安全测试与红队实战演练。**

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAX0HClQc5pgJfic5oreXjGNsPu5CON14nslpicaUJyLEOa5NVFDvLuyKU9RQnVAaAR8GYdbLouYJMicrlduR5HonLkgWAh2QqjAlU/640?wx_fmt=png&from=appmsg)

注意：现在只对常读和星标的公众号才展示大图推送，建议大家把**渗透安全HackTwo**"**设为****星标****⭐️******"**否****则可能就看不到了啦！**

**下载地址在末尾 #渗透安全HackTwo**

0x02 功能介绍

✨核心特点

## 为什么我们需要 GSL5？

**GSL5（Godzilla Super Loader 5）** 的出现，正是为了填补这一空白。它基于 Godzilla 深度二次开发，在保留原版全部核心能力的基础上，引入了 **MCP 服务（AI 驱动）**、**团队协作（多数据源共享）**、**RASP 绕过 + 字节码多态混淆**、**内存马注入** 等前沿能力，并内置完整的操作审计体系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUyIn4ph9u1dGmQAc8rfueZa3xricPJPLe4GrUAzLAdW6FnPwqSovBkA2iaeIXWGEo6FqSoemLVusWA31HoSicb45Gb5m7DThIK1Y/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAU0XUv5sW7qk2BKRXeZsMJCudaZwdc6vG6B9e9QRJfmiaLrStz0QEqRTM07DucKvmmrqVnzJb0NGwoUe12nia4KlYkjvChWIGcfc/640?wx_fmt=png&from=appmsg)

## 六大升级，重新定义 WebShell 管理

GSL5 支持三种数据源模式，满足不同规模的团队协作需求：

* **单机模式**：本地 SQLite 数据库，适合个人使用
* **团队-远程 SQLite**：UNC 共享路径，小团队内网共享
* **团队-PostgreSQL**：远程 PG 数据库，多人共享 Shell 列表 + 操作审计

更贴心的是，GSL5 提供了一键迁移工具 `MigrateDb`，可以将单机 SQLite 无缝迁移到 PostgreSQL 团队库，零成本升级协作模式。

### 🛡️RASP 绕过 + 字节码多态混淆

这是 GSL5 最硬核的能力之一。面对日益普及的 RASP（Runtime Application Self-Protection）防护，GSL5 的 `RaspBypass` 插件提供了多层次的绕过方案：

**命令执行绕过：**

* `Unsafe.allocateInstance + forkAndExec` —— 绕构造函数监控
* **JNI 原生执行** —— 脱离 JVM 监控层
* **新线程 / GC finalize** —— 切割调用栈，破坏上下文检测
* **Tomcat-JNI / ProcessImpl 直调** —— 底层直接调用

**RASP 探测与禁用：**自动识别 OpenRASP、JRASP、Elkeid 等主流 RASP，支持禁用 Hook、修改配置、卸载 Agent。

**ASM 多态混淆：**上传 `RaspBypassModule` 前，通过 ObjectWeb ASM 注入随机字段名 + 随机 NOP 指令，每次字节码特征都不同，彻底规避哈希/静态签名检测。

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAWoicOzPnwPeFgu57AwlUCCh65ofjnrNiaPb7TOxQ3l9SeSNCIv9lxUphI97tZkGLBxepuLXqUQKXqhcAiat8I9OILe32UibtmYN0o/640?wx_fmt=png&from=appmsg)

### 💉 内存马注入：无文件落地的终极隐蔽

GSL5 支持多种内存马注入方式，覆盖主流 Java Web 容器和框架：

| 注入类型 | 目标平台 |
| --- | --- |
| Filter 内存马 | Tomcat |
| Servlet 内存马 | Tomcat |
| Listener 内存马 | Tomcat |
| Controller 内存马 | Spring |
| VM Anonymous Class | JVM 层面（隐蔽性最高） |

### 🔌丰富的插件生态

GSL5 内置了覆盖多平台、多场景的插件集：

| 插件 | 平台 | 功能 |
| --- | --- | --- |
| **TH\_TOOLS** | Java / C# | Potato 系列提权（EfsPotato / BadPotato / GodPotato / SweetPotato）、Shellcode 注入 |
| **Mimikatz** | 通用 | 凭据抓取 |
| **Useradd** | 多平台 | 添加系统账号 |
| **OaTools** | Java / C# | 金蝶、致远、泛微、用友、Weblogic、vCenter 等专项代理 |
| **ShellAvscan** | 通用 | 目标安全软件探测 |
| **NetCore 插件组** | .NET Core | RealCmd、PortScan、Zip、HttpProxy、EasySocks、EvalCode、ShellcodeLoader |

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAW03358ZXgWOSEarpDKGH8s5WfcJeVez9gyUI3ZoHDe9e5xxzP4Wic6g1HiacQET0LNwAaKW0VibG5ic7m8xCUb45emFDZstR82EicQ/640?wx_fmt=png&from=appmsg)

### 📊 现代化 UI + 全量操作审计

* **FlatLaf 主题**：现代化界面，支持壁纸管理器、透明度调节
* **OperationAuditLog**：全量操作审计，记录"谁、何时、做了什么"
* 团队模式下，所有操作日志可经 `oplog_query` 查询，实现责任可追溯

###

0x03 更新介绍

```
NetCore 载荷：NetCoreDynamicPayload + NETCORE_AES_BASE64（ASP.NET Core Middleware）NetCore 插件：RealCmd / PortScan / Zip / HttpProxy / EasySocks / EvalCode / ExecuteAssembly / ShellcodeLoaderMCP 应用级入口：配置菜单；Claude / Codex 一键写配置MCP 绑定：默认 0.0.0.0:9123，支持 port / bindHost / host:portEncoding 自检：shell_detect_encoding / encoding=auto
```

0x04 使用介绍

📦安装与使用指南

### 环境要求

* **Java**：JDK / JRE 8 或以上（已验证 1.8.0\_431）
* **授权文件**：`license.lic` 必须存在于运行目录

### 生成授权

```
javac KeyGen.java && java KeyGen
```

生成的 `license.lic` 放到运行目录。授权格式为 `GSL1:<AES-CBC 密文>`，支持设置有效期、绑定目录 SHA256 + HMAC-SHA256 签名。

### 启动 GUI

```
java -jar gsl5.jar
```

启动后选择数据源（单机 SQLite / 远程 SQLite / PostgreSQL），进入主界面。

### 添加 Shell

主界面左侧为 Shell 分组树，右侧为操作区。菜单 → 右键分组 → 添加 Shell，配置关键字段：

| 字段 | 说明 |
| --- | --- |
| URL | WebShell 地址 |
| 密码 / 密钥 | 通信密钥 |
| Payload | JavaDynamicPayload / CSharpPayload / PhpPayload / NetCoreDynamicPayload |
| 加密 | JAVA\_AES\_BASE64 / JAVA\_C2 / PHP\_XOR / CSHARP\_AES\_BASE64 / NETCORE\_AES\_BASE64 |
| 编码 | 目标控制台编码（Windows 多为 GBK，Linux 多为 UTF-8） |

保存后双击或右键连接，支持测试连接、批量测试、搜索、克隆、导入导出。

### 启动 MCP 无头模式（可选）

```
java -jar gsl5.jar mcp
```

然后在 Claude / Codex 配置中添加：

```
{  "mcpServers": {    "gsl5": {      "type": "sse",      "url": "http://127.0.0.1:9123/sse"    }  }}
```

GSL5 提供一键写入配置功能，支持 Claude Code、Claude Desktop、Codex 三种客户端。

## NetCore 载荷：面向未来的 .NET Core 支持

GSL5 不仅是 Java/PHP/ASP 的天下，还完整支持 **ASP.NET Core Middleware** 动态载荷：

1. 生成时选择 `NetCoreDynamicPayload` + `NETCORE_AES_BASE64`
2. 将生成的 Middleware `.cs` 文件放入 ASP.NET Core 项目：`app.UseMiddleware<GslCoreShellMiddleware>();`
3. 添加 Shell，密码密钥一致后连接
4. 插件页可见 NetCore 专属功能：RealCmd、SuperTerminal、PortScan、Zip、HttpProxy 等

> ⚠️ 注意：NetCore 载荷不是传统 aspx，不能直接当文件上传使用，必须作为 Middleware 接入管道。

###

**0x05 内部VIP星球介绍-V1.5（福利）**

如果你想学习更多**渗透测试技术/应急溯源/免杀工具/挖洞SRC赚取漏洞赏金/红队打点等**欢迎加入我们**内部星球**可获得内部工具字典和享受内部资源和内部交流群，****每天更新1day/0day漏洞刷分上分******([2026POC更新至10922+](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247497496&idx=2&sn=05fc9eb156cce34fff4a02b7d72092ae&scene=21#wechat_redirect))****，**包含全网一些**付费扫描****工具及内部原创的Burp自动化漏****洞探测插件/漏扫工具等，AI代审工具，最新挖洞技巧等**。shadon/Hunter/0zone/Zoomeye/Quake/Fofa高级会员/AI账号/CTFShow等各种账号会员共享。详情点击下方链接了解，觉得价格高的师傅后台回复" **星球** "有优惠券名额有限先到先得**❗️**啥都有**❗️**全网资源最新最丰富**❗️****（🤙截止目前已有2900+多位师傅选择加入❗️早加入早享受）**

最新漏洞情报分享：https://t.zsxq.com/DSAvv

**👉****[点击了解加入-->>内部VIP知识星球福利介绍V1.5版本-1day/0day漏洞库及内部资源更新](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247497496&idx=2&sn=05fc9eb156cce34fff4a02b7d72092ae&scene=21#wechat_redirect)**

结尾

# 免责声明

# 获取方法

**公众号回复**20260717**获取下载、回复 加群 获取交流群**

# 最后必看-免责声明

文章中的案例或工具仅面向合法授权的企业安全建设行为，如您需要测试内容的可用性，请自行搭建靶机环境，勿用于非法行为。如用于其他用途，由使用者承担全部法律及连带责任，与作者和本公众号无关。本项目所有收录的poc均为漏洞的理论判断，不存在漏洞利用过程，不会对目标发起真实攻击和漏洞利用。文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用。如您在使用本工具或阅读文章的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。本工具或文章或来源于网络，若有侵权请联系作者删除，请在24小时内删除，请勿用于商业行为，自行查验是否具有后门，切勿相信软件内的广告！

---

# 往期推荐

**1.[内部VIP知识星球福利介绍V1.5（AI自动化）](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247497496&idx=2&sn=05fc9eb156cce34fff4a02b7d72092ae&scene=21#wechat_redirect)**

**2.[CS4.8-CobaltStrike4.8汉化+插件版](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247483949&idx=1&sn=cae68096be06be4f0ea746ee5908dc79&scene=21#wechat_redirect)**

**3.[全新升级BurpSuite2026.4专业(稳定版)](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247498687&idx=1&sn=61c2f88f87221eb2b9316bdedf6c0b33&scene=21#wechat_redirect)**

**4.[最新xray1.9.11高级版下载Windows/Linux](http://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247483882&idx=1&sn=e1bf597eb73ee7881ae132cc99ac0c8e&chksm=cf16a75af8612e4c73eda9f52218ccfc6de72725eb37aff59e181435de095b71e653b446c521&scene=21#wechat_redirect)**

**5.[最新HCL AppScan Standard](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247497507&idx=1&sn=5b6961225d8adb6ba8d5e43d4943ef9e&scene=21#wechat_redirect)**

渗透安全HackTwo

微信号：关注公众号获取

后台回复星球加入：知识星球

扫码关注 了解更多

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qFFAxdkV2tgPPqL76yNTw38UJ9vr5QJQE48ff1I4Gichw7adAcHQx8ePBPmwvouAhs4ArJFVdKkw/640?wx_fmt=png "二维码")

上一篇文章：[Nacos配置文件攻防思路总结|揭秘Nacos被低估的攻击面](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247492839&idx=1&sn=b6f091114fbd8e8922153a996c8f4f1c&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RjOvISzUFq7Xn8hrO8IErNMnOukYmCdtMhJibzK67Lzz9AJA3XPKvDxfPc8KEgT42O89Dh0UScq9g2GsjbF6Enw/0?wx_fmt=png)

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