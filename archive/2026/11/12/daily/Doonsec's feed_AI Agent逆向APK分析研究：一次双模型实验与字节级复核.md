---
title: AI Agent逆向APK分析研究：一次双模型实验与字节级复核
url: https://mp.weixin.qq.com/s/QQk3gT62afShg6CoHS6cHA
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:04:33.082675
---

# AI Agent逆向APK分析研究：一次双模型实验与字节级复核

# AI Agent逆向APK分析研究：一次双模型实验与字节级复核

兰花豆说网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于Nagain
，作者小娜

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM4qKedOopJUe8l4B5Mzp7k54hHmK7OMocRyNvtC9TRNUw/0)

**Nagain**
.

专业的移动应用安全服务提供商

**点击蓝字**

**字节级复核验证证据真实性与目标绑定逻辑**

加固应用的逆向分析正在引入大模型 Agent 工作流：通过 MCP 协议调用 REA（Reverse Engineer Anything）工具集，自动完成样本识别、脱壳、反编译与报告生成。这类报告能否直接用于评估加固方案的防护强度，取决于一个前提：报告中的证据是否真实、结论是否绑定正确目标。本实验以一款真实加固 APK 为样本，由 GPT-6.1-Sol 与 DeepSeek-V4-Pro 分别执行静态、动态分析，形成四份报告，再由人工对全部关键结论做文件级、字节级、语义级复核。

    复核结果说明：证据的真实性不等于结论的正确性，这一风险应纳入企业验收 AI 逆向成果的标准，同时样本可能具有对抗性，如果样本确实包含诱饵负载，那么静态报告的错误可能部分由样本设计导致，而非模型能力不足。本报告无法区分“模型没有检查目标”与“样本刻意诱导模型不检查目标”，只能确认结果层面的目标错位。

![](https://mmbiz.qpic.cn/mmbiz_jpg/dSuLL4Phb2QsKOqLz0Dg3SjZSzjIWSNxp9WicmYtMsqVD9CZTiabibHic7GJa5eAKibDvkv1mNeP2cfb5YlicIISJib17oRGlLy0v4oaAXSxHR8JqE/640?wx_fmt=jpeg&from=appmsg#imgIndex=0)

本文要点

模型：DeepSeekV4pro、GPT6.1-SOL;

MCP：Reverse Engineer Anything

本地工具：IDA9.4Headless、 IDA 8.0 + Hex-Rays 、JADX、unpack.jar、adb

运行沙箱：AIO\_3399ProC，Android API 28

静态报告宣称“100% 脱壳、还原全部业务代码”。字节级复核证实其解密过程真实可复现，但产物指向包内诱导DEX，运行时主业务一个类都未覆盖；

动态阶段两份报告在产物哈希、类结构、边界结论上高度收敛，并明确记录 VMP未证实、Java2C 业务方法还原 0/19——记录未还原项的报告反而符合事实；

同一份样本，静态与动态结果指向两个不同的代码层。复核的重点不是“报告是否自洽”，而是“输出物是否绑定正确目标”。

一、实验设计

样本为一款加固 APK，加固特征包括 DEX 加密、VMP 载体（libdexVmp103.so）、Java2C 编译（libnllvm.so）、壳加载器（libxloader.so）与风控 SDK（com.rc.\*）。四组实验配置为 2 个模型 × 2 种模式：静态分析不运行应用，直接分析文件；动态分析在用户授权设备（Android API 28）上运行 unpack.jar 完成脱壳。

![](https://mmbiz.qpic.cn/mmbiz_png/dSuLL4Phb2TXMO3yibuqwXf8MB0PRJcSAhia0WvLdKIibaZcAgPaXgkD2Ql0Woicv3dUlHG8oNT5c4lmB8oVGgEHk6MSbocK4FY4WA64jW4dPLo/640?wx_fmt=png&from=appmsg#imgIndex=1 "undefined")

复核分三级：文件级，对样本与四份报告计算 SHA-256；字节级，按报告偏移对 libdexData.so 执行 XOR 0x66 并校验 DEX 魔数，计算静态六 DEX 与动态三 DEX 的哈希；语义级，扫描 DEX 中的类描述符与字符串，与运行时加载结果对照，并对 RC 配置做独立解密复算。

    表 1 同时暴露一个数据完整性问题：两份静态报告哈希完全相同（09d6d93e…），说明它们不是两次独立落盘的产物。静态阶段因此只能视为一次共享基线，不用于模型间差异归因。这一发现本身也是结论的一部分：不做哈希校验时，重复文件容易被当成独立复现，从而高估结论的稳健性。

二、静态阶段：字节正确，目标错位

静态报告的核心结论是：壳的 DEX 加密层已被完全破解，六个 DEX 100% 静态还原，共 2,386 个类、3,843 个 Java 文件，业务为 com.wanxiao.enterprise.dexProtect 演示应用。

    字节级复核按报告给出的偏移执行 XOR 0x66，结果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/dSuLL4Phb2SH8zJjn9a8EvxkqjtbAicyLicEFwmvEhKcyHEHrdJrKb3ibqfqKgyHqLSoFR5KjtJCADeaB3zmC1L42frHG3t6dict2b5iaQeW7I1A/640?wx_fmt=png&from=appmsg#imgIndex=2 "undefined")

六个密文块均还原出合法 DEX，说明报告在密文定位、密钥识别、字节变换层面可信，没有编造字节。问题出在这六个 DEX 的归属。语义级扫描结果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dSuLL4Phb2RCExBvPQcib77aia3IefacodLcNbiasvvoZONMd9wwaiaYREqm7OvqDME7fiavQvXcia0EIibrbib5FZ8d65icticaLemicdO20iaRyo5SfMk/640?wx_fmt=png&from=appmsg#imgIndex=3)

静态主DEX以com/wanxiao/enterprise/dexProtect 的 MainActivity、DexFileEncryptor、DexRuntimeLoader 为主，是包内随附的演示载荷；运行时主业务为 com.demo + com.rc.\* 风控 SDK，在静态六 DEX 中没有对应物。静态 dex6.dex 与动态 classes\_1.dex 哈希相同（63f2313f…），说明静态分析只捕获到 com.xxx.\* 反检测这一层，与主业务无关。

结论：静态报告的六个 DEX 真实、合法、可复现，但目标是演示载荷而非运行时业务。“100% 脱壳”是把“对某一DEX的完整提取”等同于“对目标应用的完整还原”。本报告将这类错误定义为“证据一致型幻觉”：证据链内部完全自洽，每个字节都是真的，结论却指向错误对象。它比凭空编造更难识别——按“哈希对不对、DEX 能不能打开”复核，会全部通过，后续风险评估将建立在错误的代码层上。

三、动态阶段：确定性产物与收敛事实

动态阶段在真机上执行 unpack.jar 的 -onlyUnpack 完成脱壳，产物为三个 DEX：

![](https://mmbiz.qpic.cn/mmbiz_png/dSuLL4Phb2Sx6dV1Wia3VJX1KEOL8HhmZGT626KA7TATm0ickwBYyFIzyXQ7GM1agQFnNsFG6nQIiblaUr16QQAvUiayaV75oC4Ed6Xt9Amkov0/640?wx_fmt=png&from=appmsg#imgIndex=4)

三份 DEX 合计 1,683 个类定义（class\_defs），JADX 顶层类 968 个，smali 类 1,622 个——三种计数口径不同，不能直接比较，这是阅读 AI 报告时常见的口径陷阱。classes\_2.dex 的 SHA-256 为 d58f360c…，在两份报告目录与一次补充运行的三处独立落盘目录中完全一致，说明脱壳结果是确定性的，两份动态报告建立在同一原料上。

两份报告在以下事实上收敛

· 主业务为 com.demo + com.rc.\* 风控 SDK（RC SDK v3.5.1.4），覆盖 RcAPI、Library、RcHelper、MyWindowCallback 等类；

· DEX 声明 155 个 native 方法，其中 90 个属于 RC 类（Library 27、RcHelper 38、MyWindowCallback 19、HE 6），其余 65 个为 Android API 相关声明，不计入 Java2C 保护方法；

· VMP 未证实：libdexVmp103.so 可见函数仅返回 0x10006，.data 段为 11,288,576 字节封装载荷，未获得 RegisterNatives 表与真实字节码映射；

· Java2C 未还原：libnllvm.so 保留 19 个 MyWindowCallback 的 JNI 名称，但无可复核的静态引用，业务方法体还原 0/19；

· Native 入口定位：libxloader.so、libnllvm.so 的 JNI\_OnLoad@0x4cf70 与 librc.so 的 JNI\_OnLoad@0x4c6b8。

   另外，unpack.jar 的完成事件 id=100、退出码 100（非 0），日志无 error；报告如实标注“退出码 100 异常”，既不把非零退出码解释为成功，也不因退出码否定已核验的产物。

    与静态阶段对照：静态报告宣称“100% 还原”，被语义复核证伪；动态报告记录“0/19 未还原”“VMP 未证实”，反而与事实一致。对加固样本，任何不含未解决项的报告都应优先怀疑；明确记录未还原项，是可信信号而非失败标志。

四、两模型的差异与结构化评分

动态产物相同，两份报告的差异可归因于分析选择与证据组织。

GPT-6.1-Sol 侧重证据闭合：为分析副本建立独立 fixture，保存 APK 全部 563 个文件条目、13 个大小写冲突资源单独归档，产出 137 KB rea-evidence.json 与 2.28 MB analysis.json。其关键产出是 RC 配置解密：从 AESUtils 调用链定位固定口令，按 key = SHA256(口令) 前 16 字节（8b85bcae…）、iv = 后 16 字节（55695a2e…）派生，经 AES/CBC/NoPadding、Base64、gzip 解出明文 JSON（projectname=MobileCRM、channel=debug、server\_address=http://106.75.x.x:8080、appid=c36da5d5…c851；地址与 appid 已做脱敏处理）。本实验独立复算：gzip 头与 JSON 主体一致，但流在 144 字节处截断，解压器报流结束标记缺失。因此“配置字段级恢复”成立，“完整 gzip 流校验通过”不成立。报告同时保留“未访问该服务器”“不能认定该地址为实际使用地址”两条边界。

    DeepSeek-V4-Pro 侧重边界保守：按 Java/Native/加密/局限分层，未证实项集中列入 unknowns。对 DesUtils 的判定有代表性：类名虽为 DES，实际是 str.charAt(i) ^ key.charAt(i % 26) 的循环异或，以小写 hex 输出——这类“名不副实”的算法识别是 Java 层逆向的高价值发现。因 REA idalib provider 为 attached 模式、缺少函数工具且未切换引擎，其 Native 深度分析未开展，配置解密被归入“不可解”。

工具链不一致是必须记录的变量：静态报告记录本机 IDA Pro 9.4，GPT 动态降级为本机 IDA 8.0 + Hex-Rays，DeepSeek 未做 Native；REA Ghidra 在 Windows 下不支持 ARM64 ELF。同一实验出现三种 Native 策略，覆盖深度差异不能全部归因于模型。

![](https://mmbiz.qpic.cn/mmbiz_png/dSuLL4Phb2TPYibXseEibdjIiaPNSE1M1zRfjKzWA2SMTe2KWf6uro3G75cLcOxicgU33Mkm9GPkKfH5bZAX7qmq05zfds6onC0w3BVrCpAibibSE/640?wx_fmt=png&from=appmsg#imgIndex=5)

评分仅用于本次结构化比较：样本量为 1、每阶段一次运行、ground truth 有限，不构成模型能力排名。静态基线“目标一致性”仅 1 分，因为六 DEX 指向演示载荷；“不确定性校准”仅 1 分，因为“100%”“全部业务代码”等全称判断超出证据范围。

五、对加固评估与安全分析的启示

对采购加固方案或引入 AI 逆向能力的企业，本实验给出四个可操作的验收问题：

1. 产物可复现：报告中的文件、哈希、偏移能否独立重算？只有叙述、没有产物的结论不具备验收价值。

2. 目标可绑定：产物的包名、类名与运行时加载的代码是否一致？静态分析容易提取到“真实但无关”的载荷层，必须与动态结果及 manifest 对齐。

3. 来源可追溯：每个结论能否回到具体文件、偏移、函数地址或日志？工具版本、设备、降级策略是否如实记录？

4. 不确定性可校准：已证实与未证实是否分层？是否存在“100%”式的全称判断？

四点中任何一点不满足，该结论都不能进入“还原成功”。对加固样本，第 2 点尤其关键。

    对工作方式的三条建议：其一，对加固样本，静态优先是高风险策略，静态分析适合线索发现与加固版本识别，不能单独支撑“业务已还原”的结论；其二，Agent 的价值在编排、假设生成与证据整理，脱壳、反编译与最终复核仍需工程串联与人工配合完成；其三，将“未还原项清单”纳入报告必选项——缺少该清单的报告不应被采信。

六、结论与边界

本实验的结论：证据真实不等于结论正确。

Agent 可以准确解出字节、完整记录证据，同时把输出物绑定到错误目标。对抗这一风险，依赖更可核查的输出物、更明确的来源、更严格的目标绑定，以及明确标注未还原项的边界意识。

END

防AI逆向分析破解APP加固交流测试请联系：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ribStUdgfRibRzY53qlXuaicfdytWSAiaAgEicz0bOoQXUVDD4DdicwqEC3Sibfo9IkzvDqrgzbnJq0UKr3yr9fqG73nezyCiaibN9EqmYrmC5KE3vo4/640?wx_fmt=png&from=appmsg)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1Y7uRicSTtCequUrbj3R6CelD6j6kTdgeaBdywoCOdImg0P7WnB8zQTYveOJzTzHtSely8qFvufmiaA/0?wx_fmt=png)

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