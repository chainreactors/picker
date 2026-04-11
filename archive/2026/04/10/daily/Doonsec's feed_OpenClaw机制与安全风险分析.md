---
title: OpenClaw机制与安全风险分析
url: https://mp.weixin.qq.com/s/gbJy8T6XqFKWeN9M2igNEg
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:18:05.233364
---

# OpenClaw机制与安全风险分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0UKPAuBeu7lZePLrT0bMoNZs5iaQViapBXdILPpG3QzV4HFzVOIqv0ZYXHgYaRlqJfFp2Q6HudZMYBnOowkOYSWjMxZeKjYzlsNeB1yPy7Aqc/0?wx_fmt=jpeg)

# OpenClaw机制与安全风险分析

原创

r0
r0

联想全球安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**点击蓝字 关注我们**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7mPGUSdQNnraQhpYnc1LrNS8o4E41b9iamia3obafY8zfwIqzMB5XTaRJRAxayBWB9YAzdV8nKdqsSnLyDicDqs249Po02coN0OSw/640?wx_fmt=png)

**OpenClaw简介**

OpenClaw 是一个自托管的多渠道 AI 智能体网关(Gateway)，可以在任意操作系统上运行。它的核心定位是：让开发者和高级用户能够通过自己熟悉的聊天应用，随时随地与 AI 编程智能体进行交互，同时完全掌控自己的数据，无需依赖任何托管服务。OpenClaw还实现了一些有特色的功能，如通过在本地磁盘保存配置和用户对话交互数据，实现了跨会话的长久记忆和自适应行为；通过统一的接口，兼容了多个聊天应用的消息收发和应用内的特定操作。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7lx2u5n94lnTMnGvrTO51wHVvPwRzRtGmwoHBh8euMp0znIjNOVFSH4kjgbfSam4ErrXVuPVhO8qiaQgfgkh0DIW8NWibEFLlQLk/640?wx_fmt=png)

**OpenClaw核心组件与实现原理**

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7kd08BjvjmbnRic5asasH1pPV3Svf8dCK7Bk8iag5ETx1fuPdyGzxics1ztYypsbO7Wib93YiaEicPTyZ7pxfuWlzZiceaxPYupaPAlZA/640?wx_fmt=png)

本着一切不谈系统实现原理只凭空猜测风险都是耍流氓的原则，我们这里先从实现原理分析一些OpenClaw的核心组件。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7mg23VwFia4HncBYZ64D9ZibqrMicQKynK5Lqpic0Fy1dibejZs3B4wrfickH7HpiaCtAl8nz0nqyO5ruKqGK6E4yoGJHFIXJ6w06J1Dc/640?wx_fmt=png)

**登录认证**

OpenClaw的登录认证机制主要在Gateway组件中实现，进行登录认证时，核心认证入口函数authorizeGatewayConnect负责整个认证流程，根据通信协议分别使用WebSocket(authorizeWsControlUiGatewayConnect)或HTTP(authorizeHttpGatewayConnect)进行连接认证。登录认证过程可以总结为下图：

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7mLAprHq11DOjJ34LVIr7jUZd3nFo0MYEb47RCb0ak6NRkmicF9QSaCGkibM4UMZb9df96WpNF5icKiccZIMW7RxYzjcmO1Ls3D2DA/640?wx_fmt=png)

我们先从核心的认证模式分析，Gateway支持四种认证模式，系统会根据配置(config.gateway.auth.mode)和传入的凭证来决定使用哪种验证方式，由ResolvedGatewayAuthMode类型定义的四种认证模式：

**Token****：**OpenClaw默认使用Token进行认证，Gateway在启动时会随机生成或加载一个Token(通常在配置文件或环境变量 OPENCLAW\_GATEWAY\_TOKEN 中设置)。使用Token这种认证方式时，客户端在连接时必须提供Token，服务端使用防时序攻击的字符串比较safeEqualSecret来对比提供的Token和配置的Token是否一致。

**password：**类似于Token模式，使用用户自行设置的自定义字符串做验证，校验时同样使用safeEqualSecret做比较。

**none：**完全关闭认证。

**trusted-proxy：**从指定 HTTP 头(trustedProxy.userHeader)中提取用户身份，通过验证请求是否来自可信代理IP来判断认证是否通过。

然后我们分别分析WebSocket连接认证和HTTP连接认证。

OpenClaw的主要通信通过WebSocket进行，WebSocket的握手和认证流程可以大致分为如下过程：

**1.连接请求:**

客户端发起WebSocket连接。服务端发送connect.challenge事件，包含一个随机的nonce(一次性随机数)，用于后续的签名验证。

**2.握手请求:**

客户端发送第一条消息，必须包含connect方法的请求参数(ConnectParams)，ConnectParams包含客户端信息(ID,版本)、请求的角色(如operator、node)、请求的权限范围以及认证信息。

**3.登录认证:**

服务端调用resolveConnectAuthState进行登录认证。首先检查是否提供了全局Token或Password，若提供则使用。检查握手请求的ConnectParams是否包含设备信息(deviceId，publicKey)，如果包含则进行设备认证；设备认证过程主要进行了签名验证，具体为验证设备使用私钥对nonce的签名，确保请求未被篡改且来自持有私钥的设备；设备认证通过配对成功后会获得DeviceToken。

**4.设备配对：**

如果客户端提供了设备公钥但尚未配对或令牌无效，且未通过共享认证，服务端会触发requestDevicePairing设备配对。进行设备配对时，服务端会向管理员(已连接的Control UI或CLI)广播配对请求；管理员批准后，设备获得授权，并获取DeviceToken。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7mg23VwFia4HncBYZ64D9ZibqrMicQKynK5Lqpic0Fy1dibejZs3B4wrfickH7HpiaCtAl8nz0nqyO5ruKqGK6E4yoGJHFIXJ6w06J1Dc/640?wx_fmt=png)

**Channels**

OpenClaw实现的一个非常有特色的功能就是用统一的接口，把常用的聊天应用的消息格式统一转化为了Agent能够理解的标准事件，这个功能官方文档抽象称为channels。由于通过channels可以直接给AI Agent下发指令，指令执行是Agent防御的核心，OpenClaw在实现channels时构建了一套安全体系：

**1.私聊与群组**

OpenClaw将聊天应用里的对话场景严格区分为**私聊**(Direct Message，DM)和**群组**(Group)，针对这两个场景分别有不同的安全策略。

**DM策略：**

1. **pairing**：DM默认使用pairing策略。在这种策略下，未在白名单中的用户发来消息时，系统不会直接执行指令，而是会回复一个“配对码”。用户必须在Gateway的控制台输入该配对码，完成设备绑定后，才可以成为受信任的发件人并在AI Agent中执行指令。这种配置策略可以有效防止陌生人攻击。
2. **allowlist**：只允许配置文件中allowFrom列表里的用户与AI Agent交互。
3. **open：**任何知道OpenClaw聊天应用账号的人都可以与它交互，这种配置策略是非常危险的。
4. **disabled****：**禁用DM。

**Group策略：**

1. **open：**任何在群组中的人都可以和OpenClaw聊天应用账号交互，这种配置策略同样是非常危险的。
2. **allowlist：**只允许配置文件中channels列表中显式声明的群组才可以与AI Agent交互，且Group的allowlist名单和DM的allowlist名单是分开管理的。
3. **disabled：**禁用群组聊天。

**2.白名单**

OpenClaw的白名单系统(allowFrom)不仅仅是简单的字符串相等比较，它实现了一套比较复杂的解析引擎：

**多维度匹配：**支持根据 Sender ID、Username 甚至手机号进行匹配。

**正则匹配**：支持正则匹配和通配符，如配置为"\*"则等同于open配置策略；白名单在比较前会统一转换为小写，以防止大小写绕过。

**3.指令网关**

OpenClaw实现了“使用权”和“管理权”的分离，消息中的普通对话和控制命令(如/reset，/system.run)会被严格区分。具体实现为，resolveControlCommandGate函数会检查当前发件人是否具备执行高级命令的权限，这样即使用户在allowFrom列表中具有向AI Agent发送消息的权限，但如果没有useAccessGroups的权限，他依然无法在AI Agent执行特权命令。

**4.Webhook签名**

OpenClaw支持两种主要的入站通信模式，Webhook和WebSocket。WebSocket主要用于Gateway连接各种内部客户端、外部平台，一般会采取前文登录认证部分的安全机制来保障安全性；Webhook会在公网暴露web接口，仅仅使用Bearer Token来进行认证是不够的，OpenClaw还在src/plugin-sdk/webhook-request-guards.ts采取了一些其他策略来进一步保证安全性：

**请求方法限制**：只允许POST请求，对扫描器常用的GET探测进行拦截。

**请求载荷限制：**preAuth限制最大请求为64KB，超时5秒；postAuth限制最大请求为1MB，超时30秒。限制请求载荷大小的原因是防止读取、处理无限大的HTTP body导致资源耗尽。

**并发请求限制：**使用createWebhookInFlightLimiter限制同一来源的并发请求数，默认单Key最大8个并发。

OpenClaw的channels安全体系建立在DM Pairing、Allowlist之上;

Channels是OpenClaw的亮点功能，但同时也需要我们正确配置才能最大发挥OpenClaw的作用。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7mg23VwFia4HncBYZ64D9ZibqrMicQKynK5Lqpic0Fy1dibejZs3B4wrfickH7HpiaCtAl8nz0nqyO5ruKqGK6E4yoGJHFIXJ6w06J1Dc/640?wx_fmt=png)

**文件系统隔离**

OpenClaw 的文件系统安全分为多个层次，从底层路径验证到沙箱容器隔离，形成了比较完整的防御体系。

1. **容器隔离**

OpenClaw通常默认启用沙箱模式，默认情况下会尝试在Docker容器中执行系统命令。OpenClaw的每个Agent或Session都运行在独立的Docker容器中，这天然的将Agent的文件系统操作限制在容器内部，使其无法直接访问宿主机的根文件系统；同时，在Docker启动时可以配置--read-only，使得容器的根文件系统变为只读，进一步防止恶意软件持久化或篡改系统文件。OpenClaw还会在Docker容器启动时过滤掉敏感的环境变量，防止宿主机的敏感信息(如API Key)泄露到沙箱环境中。

2. **路径防护**

即使在Docker容器内部，OpenClaw也未将其视为完全受信的环境，在宿主机和Docker容器交互以及Agent执行文件操作时，实施了严格的应用层检查。

3. **根目录锁定**

Docker容器内所有文件操作必须限制在配置的rootDir内，且校验解析后的绝对路径是否依然位于rootDir下，防止通过../进行路径穿越攻击。

4. **符号链接防护**

OpenClaw会调用openVerifiedLocalFile和resolvePinnedWriteTargetWithinRoot显式检查路径中的每一级是否包含符号链接，如果检测到符号链接指向了rootDir之外，操作会立刻被阻断。这样的机制有效防御了Symlink Race攻击，即在文件检查和文件写入的时间间隔内替换符号链接以指向敏感文件。

5. **硬链接防护**

OpenClaw会检查文件的硬链接数，如果文件有多个硬链接，操作会被拒绝。这样的机制防御通过创建指向敏感文件的硬链接来绕过权限检查的攻击。

原子写入与校验

文件写入操作采用“写入临时文件->重命名”的原子操作模式，写入完成后，会再次校验目标文件的身份，确保写入的文件是预期的文件且未被替换。

6. **沙箱文件系统桥接**

OpenClaw实现了一个桥接层用于在Agent和Docker容器之间安全地进行文件传输、文件操作，桥接层设计了一些安全机制来进一步保障Docker容器的安全性：

在执行任何Shell命令前，预先解析和校验路径的安全性，确保操作的目标路径是合法的、可写的、不会逃逸rootDir；所有的文件操作都会被构建为一组经过校验的Shell命令计划(SandboxFsCommandPlan)，而非直接拼接字符串执行，这样进一步减少了命令注入的风险。

OpenClaw 的文件系统隔离采用了"容器隔离+应用层校验"的双重保险机制。容器提供了操作系统级别的强隔离，应用层的文件操作在代码逻辑层面防御了比较复杂的路径穿越和条件竞争攻击，确保了Agent在拥有执行Shell命令的同时也无法突破文件系统的边界。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7lx2u5n94lnTMnGvrTO51wHVvPwRzRtGmwoHBh8euMp0znIjNOVFSH4kjgbfSam4ErrXVuPVhO8qiaQgfgkh0DIW8NWibEFLlQLk/640?wx_fmt=png)

**OpenClaw风险分析**

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7kd08BjvjmbnRic5asasH1pPV3Svf8dCK7Bk8iag5ETx1fuPdyGzxics1ztYypsbO7Wib93YiaEicPTyZ7pxfuWlzZiceaxPYupaPAlZA/640?wx_fmt=png)

通过对OpenClaw核心组件的实现原理分析发现，尽管其实现时考虑了诸多的安全缓解措施，但这些安全措施并不成熟、这些安全措施实现时逻辑存在漏洞，这样一个庞大、复杂的AI Agent网关依旧存在安全风险，可以总结分为以下几类：

1. **认证绕过**

OpenClaw的权限控制基于token验证、allowlist、api接口鉴权等等，但是由于OpenClaw支持多用户、多channels接入，权限模型非常复杂，在实现一些很细致的权限校验时容易出现逻辑漏洞。攻击者利用这些逻辑漏洞通常可以进行权限提升，比如访问自己原本没有权限访问的api接口、提升token权限等等，认证绕过是非常高危的漏洞，甚至可能导致OpenClaw网关直接被攻陷。

2. **路径穿越**

AI Agent在工作时需要读取OpenClaw网关本地文件进行上下文理解、文件操作等，如果这些文件隔离不当、文件路径处理不当，攻击者就能读取或覆盖OpenClaw网关本地关键文件。路径穿越类漏洞一般出现在zip解压缩、符号链接、条件竞争攻击等攻击场景中，OpenClaw虽然在实现时考虑了类似的攻击场景并进行了防御性编码，但从历史漏洞数据来看，在一些细粒度的攻击场景下依然存在路径穿越的逻辑漏洞。

3. **命令执行**

命令执行是AI Agent面临的最直接的威胁，因为OpenClaw的Agent被赋予了执行Shell命令的能力，一旦Agent执行了恶意的Shell命令，就可能造成数据丢失、数据泄露或OpenClaw网关直接被接管。我们或许无法假设AI永远不会曲解人类的意图，让AI能在拥有执行Shell命令进行自动化工作的同时保证AI不执行恶意Shell命令，这应该是AI模型和AI Agent亟待解决的问题。我们很高兴可以看到OpenClaw针对Agent的命令执行做了诸多安全防护，但是从历史漏洞分析在细微攻击场景的处理上OpenClaw依然犯了很多错误，比如命令允许列表可以通过命令拼接绕过，一些看似无害命令的特定搭配也会存在风险比如env -S可以用来执行任意拼接的命令，攻击者甚至可以通过URL编码绕过OpenClaw的前端正则、前缀检查。

4. **容器隔离**

OpenClaw为了降低命令执行漏洞的风险，默认启用了Docker容器隔离即在Docker中执行Shell命令，但是OpenClaw的Docker隔离由于配置历史上也出现过漏洞。容器隔离模块出现的漏洞不会像命令执行、认证绕过一样直接造成非常严重的后果，但会对安全隔离体系造成破坏，如逃逸Docker在OpenClaw网关宿主机执行命令。虽然容器隔离会出现安全漏洞导致隔离失效，但容器隔离机制本身减小了别的模块出现安全漏洞时对网管宿主机本身的危害、降低了安全影响，无疑是非常优秀的安全机制和安全设计。

5. **channels**

OpenClaw的channels使用了统一的接口把常用的聊天应用的消息格式统一转化为了Agent能够理解的标准事件，channels是最直接暴露给攻击者的攻击面，攻击者利用channels模块的漏洞与OpenClaw聊天应用账号交互可以越权访问api接口、泄露OpenClaw网关数据、甚至直接接管OpenClaw网关。由于OpenClaw接入了诸多常用聊天应用，这套体系需要非常细化的身份验证、权限控制，针对特定应用的验证处理逻辑还需要安全研究人员和开发人员进一步深入检查。

6. **供应链安全**

OpenClaw的AI Agent支持MCP、skills等工具调用，这些工具通过给AI提供描述和api接口，使得AI可以根据需求和工具描述调用工具获取所需的信息。MCP、skills本质就是桥接AI和外部工具...