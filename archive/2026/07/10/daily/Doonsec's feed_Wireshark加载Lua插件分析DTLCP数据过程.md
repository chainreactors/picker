---
title: Wireshark加载Lua插件分析DTLCP数据过程
url: https://mp.weixin.qq.com/s/qPwCybbI1HitJrgbXaEZJw
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T05:02:37.049380
---

# Wireshark加载Lua插件分析DTLCP数据过程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZaibroIiatwe0toEMlOYYqZdq828tqa8TDTomS6v67ZZMA66KyekoWs2Zgk4PDiaA0S1s4sZhaKFA4wqX2KUS03TEEiaKicsaIunepmWB44FYHR8/0?wx_fmt=jpeg)

# Wireshark加载Lua插件分析DTLCP数据过程

原创

利刃信安
利刃信安

利刃信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Wireshark加载Lua插件

分析DTLCP数据过程

Lua插件 · DTLCP协议解析 · UDP数据包分析 · Epoch/Sequence Number

01

PART

插件加载过程

PLUGIN LOADING PROCESS

1.1 启动扫描

Wireshark启动时，会自动扫描以下目录寻找Lua插件：

**Windows系统：**

%APPDATA%\Wireshark\plugins\ — 个人插件目录

C:\Program Files\Wireshark\plugins\ — 全局插件目录

**Linux/Mac系统：**

~/.wireshark/plugins/ — 个人插件目录

/usr/share/wireshark/plugins/ — 全局插件目录

1.2 初始化配置

Wireshark首先读取配置文件 init.lua ，检查关键配置：

...lua

disable\_lua = false -- 必须设置为false才启用Lua支持

run\_user\_scripts\_when\_superuser = false -- 安全控制

1.3 加载顺序

Wireshark 按以下顺序加载插件：

1 读取 init.lua 配置文件

2 检查Lua是否启用（ disable\_lua 值）

3 按字母顺序扫描插件目录中的所有 .lua 文件

4 逐个执行Lua插件脚本

5 插件注册协议和解析器到Wireshark系统

02

PART

DTLCP Lua插件注册过程

DTLCP LUA PLUGIN REGISTRATION

2.1 协议对象创建

插件首先创建DTLCP协议对象，定义协议的基本信息：

...lua

local dtlcp\_protocol = Proto("DTLCP", "DTLCP协议", "数据报传输层密码协议")

这告诉Wireshark：

协议名称： DTLCP

 显示名称： DTLCP协议

 协议描述： 数据报传输层密码协议

**DTLCP与TLCP的区别：**

| 特性 | TLCP | DTLCP |
| --- | --- | --- |
| 传输层 | **TCP** | **UDP** |
| 协议标准 | GB/T 38636-2020 | GM/T 0128-2023 |
| 数据包格式 | TLS Record格式 | DTLCP Record格式（含epoch/seq） |
| 连接特性 | 有连接、可靠 | 无连接、需重传机制 |

2.2 字段定义

接着定义DTLCP协议中包含的所有字段，相当于建立"数据字典"：

...lua

local fields = dtlcp\_protocol.fields

-- DTLCP特有的字段结构（基于UDP）

fields.epoch = ProtoField.uint16("dtlcp.epoch", "Epoch", base.HEX)

fields.sequence\_number = ProtoField.uint64("dtlcp.sequence\_number", "序列号", base.HEX)

fields.content\_type = ProtoField.uint8("dtlcp.content\_type", "内容类型", base.HEX)

fields.version = ProtoField.uint16("dtlcp.version", "协议版本", base.HEX)

fields.length = ProtoField.uint16("dtlcp.length", "长度", base.DEC)

fields.cipher\_suite = ProtoField.uint16("dtlcp.cipher\_suite", "密码套件", base.HEX)

fields.signature = ProtoField.bytes("dtlcp.signature", "签名数据")

**DTLCP Record格式：**

...record

DTLCP Record结构（共13字节头部）：

┌──────────────┬──────────────────┬──────────────┬──────────────┬──────────────┬───────────────┐

│ 偏移0-1字节 │ 偏移2-7字节 │ 偏移8字节 │ 偏移9-10字节 │ 偏移11-12字节│ 偏移13+字节 │

│ Epoch (2B) │Sequence Number(6B)│Content Type(1B)│ Version (2B) │ Length (2B) │Fragment/Payload│

└──────────────┴──────────────────┴──────────────┴──────────────┴──────────────┴───────────────┘

**DTLCP Content Type定义：**

...lua

-- DTLCP消息类型常量

local CONTENT\_TYPE = {

CHANGE\_CIPHER\_SPEC = 0x14, -- 密码切换

ALERT = 0x15, -- 告警

HANDSHAKE = 0x16, -- 握手

APPLICATION\_DATA = 0x17, -- 应用数据

}

**关键字段说明：**

**Epoch** ：会话周期标识（握手成功后epoch递增）

 **Sequence Number** ：48位序列号（防重放攻击）

 **Content Type** ：消息类型（Handshake/AppData/Alert等）

2.3 解析器注册

DTLCP基于UDP，需要注册到UDP端口：

...lua

-- 注册到UDP端口（DTLCP通常使用自定义UDP端口）

local udp\_table = DissectorTable.get("udp.port")

udp\_table:add(443, dtlcp\_protocol) -- 监听UDP 443端口

udp\_table:add(9000, dtlcp\_protocol) -- 监听UDP 9000端口（示例）

**DTLCP端口监听策略：**

DTLCP通常使用自定义UDP端口（非标准443）

 可以监听多个UDP端口（测试环境可能使用不同端口）

 支持动态端口配置（通过Preference设置）

03

PART

DTLCP数据包解析过程

DTLCP PACKET PARSING PROCESS

3.1 数据包到达触发

当Wireshark捕获到符合条件的UDP数据包时，会自动调用已注册的DTLCP插件解析器。

**触发条件：**

...trigger

UDP端口匹配 → 协议识别 → 触发DTLCP解析器

例：UDP端口443或9000 → 数据包到达 → 调用dtlcp\_protocol.dissector

3.2 解析器接收参数

DTLCP解析器函数接收三个关键参数：

...lua

function dtlcp\_protocol.dissector(buffer, pinfo, tree)

-- buffer: DTLCP Record数据字节流（从DTLCP头部开始，不包含UDP/IP/Ethernet头部）

-- pinfo: 包信息（序号、时间、源/目标UDP端口等）

-- tree: 协议树（用于添加DTLCP解析结果）

end

**参数说明：**

pinfo.src\_port 和 pinfo.dst\_port — UDP源端口和目标端口

 buffer:len() — DTLCP Record数据总长度（从Epoch开始到数据包结束）

 buffer参数指向DTLCP Record起始位置，不包括UDP/IP/Ethernet头部

3.3 DTLCP数据读取与解析

DTLCP解析器按GM/T 0128-2023标准逐字节读取数据：

**安全检查（必须）：**

...lua

function dtlcp\_protocol.dissector(buffer, pinfo, tree)

-- 安全检查：buffer必须至少有13字节（DTLCP头部）

if buffer:len() < 13 then

return

end

-- 然后再读取字段

local epoch = buffer(0, 2):uint()

-- ...

end

**完整解析步骤：**

...parsing

第1步：读取DTLCP Record头部（固定13字节）

├─ Epoch (0-1字节) → buffer(0, 2):uint()

├─ Sequence Number (2-7字节) → buffer(2, 6):uint64() -- 读取6字节，按uint64解析

├─ Content Type (8字节) → buffer(8, 1):uint()

├─ Version (9-10字节) → buffer(9, 2):uint()

└─ Length (11-12字节) → buffer(11, 2):uint()

第2步：根据Content Type判断消息类型

├─ 0x14 (ChangeCipherSpec) → 解析密码切换

├─ 0x15 (Alert) → 解析告警消息

├─ 0x16 (Handshake) → 解析握手消息

└─ 0x17 (Application Data) → 解析应用数据

第3步：解析Fragment/Payload（变长，根据Length字段）

├─ 读取Length指定的字节数 → buffer(13, length)

├─ 如果是加密数据，解析加密结构

└─ 如果是握手消息，解析握手子消息

第4步：特殊字段处理

├─ 加密Record：解析IV + 密文 + MAC/AuthTag

├─ 握手Record：解析Handshake Header + 消息内容

└─ 分片处理：DTLCP支持消息分片传输

3.4 DTLCP特有的解析逻辑

**Epoch和Sequence Number处理：**

...lua

-- Epoch标识会话周期

local epoch = buffer(0, 2):uint()

if epoch == 0 then

-- Epoch 0：握手阶段，明文传输

subtree:add(fields.epoch, buffer(0, 2)):append\_text(" (握手阶段)")

else

-- Epoch > 0：加密传输阶段

subtree:add(fields.epoch, buffer(0, 2)):append\_text(" (加密阶段)")

end

-- Sequence Number防重放

local seq\_num = buffer(2, 6):uint64() -- 读取6字节序列号，按uint64解析

subtree:add(fields.sequence\_number, buffer(2, 6))

-- 验证序列号是否递增（防重放攻击）

**UDP分片处理：**

DTLCP基于UDP，可能需要处理消息分片：

...lua

-- DTLCP消息分片处理（示例）

local function handle\_fragment(subtree, buffer, offset, length)

local fragment\_tree = subtree:add(buffer(offset, length), "Fragment")

fragment\_tree:append\_text(" (可能包含分片信息)")

end

3.5 结果添加到协议树

DTLCP解析出的每个字段都添加到Wireshark的协议树中显示：

...lua

-- 创建DTLCP协议树

local subtree = tree:add(dtlcp\_protocol, buffer())

-- 添加DTLCP Record头部

subtree:add(fields.epoch, buffer(0, 2))

subtree:add(fields.sequence\_number, buffer(2, 6))

subtree:add(fields.content\_type, buffer(8, 1))

subtree:add(fields.version, buffer(9, 2))

subtree:add(fields.length, buffer(11, 2))

-- 添加Payload/Fragment

if length > 0 then

local payload\_tree = subtree:add(buffer(13, length), "Payload")

-- 根据Content Type继续解析...

end

**Wireshark界面显示DTLCP解析结果：**

...display

DTLCP Protocol (UDP Port 443)

├─ Epoch: 0x0001 (加密阶段)

├─ Sequence Number: 0x000000000001 (防重放)

├─ Content Type: 0x17 (Application Data)

├─ Version: 0x0101 (DTLCP 1.1)

├─ Length: 64 bytes

└─ Payload:

├─ IV: 16 bytes (SM4-CBC加密)

├─ Encrypted Data: 48 bytes

└─ MAC/AuthTag: 16 bytes (HMAC-SM3或SM4-GCM AuthTag)

04

PART

完整工作流程总结

COMPLETE WORKFLOW SUMMARY

4.1 DTLCP解析流程图

...flow

Wireshark启动

↓

读取init.lua配置

↓

扫描插件目录

↓

加载dtlcp\_analyzer.lua

↓

创建DTLCP协议对象

↓

定义DTLCP字段（epoch/seq/content\_type等）

↓

注册UDP端口解析器

↓

监听UDP网络端口

↓

捕获UDP数据包

↓

触发DTLCP解析器函数

↓

读取Epoch和Sequence Number

↓

判断Epoch阶段（握手/加密）

↓

读取Content Type

↓

根据类型解析Payload

↓

处理加密/分片逻辑

↓

添加到协议树显示

↓

用户查看DTLCP解析结果

4.2 关键环节说明（DTLCP特有）

| 环节 | TLCP（TCP） | DTLCP（UDP） | 关键差异 |
| --- | --- | --- | --- |
| 传输层监听 | TCP端口 | UDP端口 | UDP无连接，需监听多个端口 |
| 协议识别 | TLS Record Header | DTLCP Record Header | DTLCP含epoch/sequence\_number |
| 数据结构 | ContentType+Version+Length | Epoch+Seq+Type+Version+Length | DTLCP头部多5字节（epoch+seq） |
| 防重放机制 | TCP序列号 | DTLCP序列号（48位） | UDP需显式序列号防重放 |
| 加密阶段标识 | 无显式标识 | Epoch字段 | Epoch标识握手完成与否 |
| 分片处理 | TCP自动分片 | DTLCP需手动处理分片 | UDP需应用层分片重组 |

4.3 DTLCP数据包解析循环

对于每个捕获的UDP数据包，DTLCP解析器都会执行：

...loop

UDP包到达 → 解析器调用 → 读取epoch+seq → 判断阶段

→ 读取Content Type → 解析Payload → 处理分片/加密 → 显示结果

**关键差异：**

**TLCP（TCP）** ：可靠传输，自动分片重组，无显式序列号

 **DTLCP（UDP）** ：无连接，需epoch/seq防重放，应用层分片处理

05

PART

实际应用示例：DTLCP协议解析

PRACTICAL APPLICATION EXAMPLE

5.1 DTLCP握手阶段解析

**第一阶段：插件加载**

...loading

Wireshark启动 → 读取init.lua → 扫描plugins目录

→ 发现dtlcp\_analyzer.lua → 执行脚本

→ 创建DTLCP Proto对象 → 定义epoch/seq等字段

→ 注册解析器到UDP端口（443/9000）

**第二阶段：Epoch 0握手数据捕获**

...handshake

UDP端口监听 → 捕获UDP数据包（epoch=0x0000）

→ 识别为DTLCP握手阶段 → 触发dtlcp\_analyzer解析器

→ 解析Epoch=0 → 明文传输阶段

→ 解析Content Type=0x16 (Handshake)

→ 解析握手消息（ClientHello/ServerHello等）

**第三阶段：Epoch 1加密数据解析**

...encrypted

握手完成 → Epoch递增为1 → 捕获UDP加密数据包

→ 解析Epoch=0x0001 → 加密传输阶段

→ 解析Sequence Number → 验证防重放

→ 解析Content Type=0x17 (AppData)

→ 解析加密Payload → SM4-CBC/SM4-GCM解密

→ 解析AuthTag/HMAC → 完整性校验

→ 所有字...