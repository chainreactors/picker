---
title: 安天智能体完成Fastjson2.x SeeAlso链RCE漏洞PoC验证
url: https://mp.weixin.qq.com/s/0W1AAi1mQlsl7ubWqS7T5w
source: Doonsec's feed
date: 2026-08-01
fetch_date: 2026-08-02T05:09:22.151649
---

# 安天智能体完成Fastjson2.x SeeAlso链RCE漏洞PoC验证

![cover_image](http://mmecoa.qpic.cn/mmecoa_jpg/Yicx1jVK2eOmk2sdKPoovibtvOxwzGPAeQ5hCPENBsf11kRVEM8Ftw440pMLHlq8C9fhgdtFEcuMNlxEdSTkz4FQ/0?wx_fmt=jpeg)

# 安天智能体完成Fastjson2.x SeeAlso链RCE漏洞PoC验证

安天CERT
安天CERT

安天垂直响应平台

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方"蓝字"

关注我们吧！

**0****1**

**概述**

安天CERT监测到互联网上公开了针对 Fastjson2 远程代码执行漏洞的 SeeAlso 利用链及配套 PoC（概念验证代码）。Fastjson2 是阿里巴巴开源的高性能 Java JSON 解析库，凭借其出色的解析性能和简洁的 API 设计在国内 Java 生态中占据主导地位，广泛应用于企业级后端服务、微服务网关、数据接口层、政企平台等核心生产场景。

与前期披露的信息相比，本次公开的SeeAlso 链出现了重要变化。早期分析普遍认为该漏洞的利用前提是构造 FNV-1a 哈希碰撞以命中 AutoType 内置白名单；而 SeeAlso 链表明：在存在多态反序列化场景（如目标类标注 @JSONType(seeAlso=...)）的应用中，解析器创建的 ObjectReaderSeeAlso 会在构造时强制开启 SupportAutoType，使 AutoType 校验直接进入"已开启"分支。攻击者无需构造任何哈希碰撞，即可让恶意类名绕过白名单校验直达类加载器，借助支持远程资源加载的上下文类加载器（ClassLoader）从远端拉取并执行恶意类，最终实现远程代码执行（RCE）。

目前该漏洞的SeeAlso 利用链技术细节与完整 PoC 均已公开，攻击者可直接复现并完成武器化，防守方的修复窗口正在快速收窄。鉴于 Fastjson2 在国内 Java 业务中的普及度极高，请高度重视，立即开展资产自查，尽快完成版本升级或临时缓解处置。

**0****2**

****风险描述****

## 2.1 **漏洞基本信息**

|  |  |
| --- | --- |
| **漏洞名称** | **Fastjson2 远程代码执行漏洞（SeeAlso 利用链）** |
| **漏洞编号** | 暂无CVE |
| **漏洞类型** | 远程代码执行（RCE）/ 反序列化 AutoType 白名单绕过 |
| **风险等级** | 高危（CVSS 3.1 评分 9.8） |
| **影响版本** | Fastjson2 ≤ 2.0.62 |
| **修复版本** | Fastjson2 2.0.63（官方修复补丁 PR #7695） |
| **利用条件** | 远程利用/ 无需认证 / 无需用户交互 / 默认配置即可触发；需存在多态反序列化场景 |
| **PoC 状态** | 已公开（含完整利用代码与一键复现脚本） |
| **在野利用** | 暂未发现大规模在野利用 |
| **修复方式** | 升级至2.0.63 及以上 / 开启 SafeMode / 出向管控 / WAF 加固 |

##

**0****3**

****受影响范围****

Fastjson2 ≤ 2.0.62 受影响；Fastjson2 ≥ 2.0.63（合入官方修复补丁 PR #7695）不受影响。

从利用条件看，未开启安全模式（SafeMode）、且代码中存在多态反序列化场景（@JSONType(seeAlso=...)、Jackson @JsonSubTypes/@JsonTypeInfo、sealed types 等）的应用风险最高。公开 PoC 已在 JDK 8 与 JDK 21 上完成完整 RCE 实测，JDK 11/17 未经实测但预期同样可利用。

注：Fastjson 1.x 用户另需关注同期披露的 fastjson 1.2.68–1.2.83 远程代码执行漏洞（CVE-2026-16723），官方修复版本为 1.2.84。仍使用 Fastjson 1.x 的用户，建议尽快升级修复版本或迁移至 Fastjson2 修复版本，并同步开启 SafeMode。

**0****4**

****公开PoC情况与武器化风险****

本次随SeeAlso 链公开的 PoC 仓库包含了端到端的完整利用代码，主要包括：基于 Spring Boot 的漏洞靶场（提供多态反序列化接口 /parseAnimal）、基于 ASM 字节码技术的恶意 JAR 生成器（自动生成继承多态基类的 Evil 类）、用于托管恶意字节码并接收回显的 HTTP 回调服务器，以及一键构建复现脚本。攻击者执行数条命令即可完成从环境搭建到远程代码执行的全流程验证。

PoC 与技术细节的完整公开，意味着攻击者无需自行分析漏洞原理即可直接复现、改造并武器化，此前"PoC 未公开"所留下的缓冲窗口已经消失。考虑到 Fastjson2 的互联网暴露面达百万级，各单位应将该漏洞的处置优先级提升至最高，按"随时可能出现在野利用"的假设开展排查与加固，并对历史访问日志进行回溯，检查是否已发生攻击尝试。

**0****5**

**AVL Code完成了PoC的分析和验证**

安天AVL Code 大模型完成该 Fastjson2 远程代码执行漏洞利用思路推演与 PoC 实操验证，成功加载恶意类触发 RCE，证实漏洞可稳定利用。

![](https://mmecoa.qpic.cn/mmecoa_png/frAs2k03Ypm0helfNVNME84smusVO1jn2uD0klXUAcUMrzzgNZzwEEVKk3UduOic7r1YJMsLE2aFzvW2sAPACakyBl1ywVB5dpGtY60PUib6w/640?wx_fmt=png&from=appmsg)

**图2 AVL Code针对Fastjson2分析验证**

![](https://mmecoa.qpic.cn/sz_mmecoa_png/frAs2k03YplOkN7zliaGohKXZ0xmicaZ27bAQWs7p3fveKxvCcibj0nIeJIhZjXB9fMAHfhWeibpK4A1h1Vq2YBXVRwzic5EZ8NKQdV8xU7T7ibtw/640?wx_fmt=png&from=appmsg)

**图3 安天 AVL Code生成 Fastjson2 漏洞PoC 并完成有效性验证**

**0****6**

**漏洞排查与检测**

## 6.1 **组件版本自查**

Maven 项目可检查 pom.xml 中的 fastjson2 依赖版本：

|  |
| --- |
| <dependency>      <groupId>com.alibaba.fastjson2</groupId>      <artifactId>fastjson2</artifactId>      <version>x.x.x</version>  <!-- 确认版本是否 <= 2.0.62-->  </dependency> |

也可在服务器上通过以下命令快速排查：

|  |
| --- |
| # 查找 fastjson2 JAR 包  find / -name "fastjson2-\*.jar" 2>/dev/null     # 查看运行中进程加载的 fastjson 组件  lsof | grep fastjson     # Gradle 项目  grep -r "fastjson2" build.gradle |

若当前版本在受影响范围内（≤ 2.0.62），且未开启安全模式（SafeMode），则存在安全风险。

## 6.2 **多态反序列化特征排查**

针对SeeAlso 链的触发条件，建议在源代码与依赖中排查多态反序列化用法，重点检索以下特征：

|  |
| --- |
| # 排查 fastjson2 seeAlso 多态注解  grep -rn "seeAlso" --include="\*.java" .     # 排查 Jackson 多态注解（fastjson2 默认兼容）  grep -rn "@JsonSubTypes\|@JsonTypeInfo" --include="\*.java" . |

存在上述用法且对应接口会解析外部不可信JSON 数据的系统，应视为高风险资产优先处置。

## 6.3 **SafeMode状态检查**

|  |
| --- |
| # 检查 JVM 启动参数中是否已启用 SafeMode  ps aux | grep java | grep "fastjson2.parser.safeMode"     # 若输出为空，说明 SafeMode 未启用，存在风险 |

## 6.4 **流量与日志检测**

结合WAF、网关与主机日志，重点检测以下特征：请求体或 URL 参数中出现 @type 字段，尤其是取值包含 jar:、http:、!: 等协议字符或 ":.." 点号变形特征的 JSON 载荷；应用服务器向外发起的非常规 HTTP 请求，特别是目标资源以 .class、.jar 结尾的出向连接（远程类加载的必要环节）；以及 JVM 进程中异常加载的外部类。

**0****7**

**漏洞处置方案**

## 7.1 **官方升级（推荐）**

官方已发布修复版本Fastjson2.0.63（修复补丁随 PR #7695 合入），建议受影响用户尽快升级。补丁详情：

https://github.com/alibaba/fastjson2/pull/7695/changes

该修复的核心要点包括：白名单哈希命中后增加类名明文文本回验；直接拒绝包含":"、"!" 等 URL 协议字符的类型名；阻断 ClassLoader、JDBC 相关危险基类的加载路径，从多个环节切断本漏洞的利用链。

## 7.2 **开启SafeMode 安全模式**

若暂时无法升级，可开启SafeMode 安全模式作为临时缓解。开启后无论白名单还是黑名单均不支持 AutoType，可从底层切断漏洞利用入口。开启方式如下：

方式一：JVM 启动参数（推荐）。服务启动时追加全局安全模式开关参数：

|  |
| --- |
| -Dfastjson2.parser.safeMode=true  # 兼容旧属性名：-Dfastjson.parser.safeMode=true |

方式二：代码配置。调用全局解析配置实例，主动开启安全模式：

|  |
| --- |
| ParserConfig.getGlobalInstance().setSafeMode(true); |

方式三：配置文件。通过类路径中的fastjson2.properties 文件配置：

|  |
| --- |
| fastjson2.parser.safeMode=true |

此外，也可直接使用fastjson2-noneautotype 版本彻底禁用 AutoType 能力。注意：开启 SafeMode 后 @type 字段将被完全拒绝，若业务确实依赖多态反序列化（包括 seeAlso 用法），请评估改为显式指定目标类型，或仅对可信来源数据使用。

## 7.3 **网络出向管控**

SeeAlso 链完成 RCE 的必要环节是目标服务器向攻击者控制的地址发起 HTTP 请求拉取远程类字节码。建议在主机防火墙、安全组或出口网关上收敛业务服务器的出向访问策略，仅放行必要的域名与端口，阻断非必要出网连接，从网络层面抬高远程类加载的实施门槛。

## 7.4 **部署W****AF****拦截策略**

通过Web 应用防火墙（WAF）或 API 网关新增匹配规则，拦截请求体中 key 包含 @type 标识字段的 JSON 请求载荷。@type 字段为 Fastjson AutoType 特性的触发关键字，历史上绝大多数依托该组件实现的远程代码执行漏洞均需借助此字段完成恶意类加载。

配置规则时需兼顾两处数据检测范围：一是POST 请求的请求体内容，二是 URL 拼接携带的参数内容；同时需兼容各类 URL 编码、特殊字符变形（如本漏洞的 ":.." 点号变形）等常见绕过手段，避免恶意请求规避检测。

**0****8**

**安全建议**

**建立组件资产清单：**统计所有业务系统中使用的Fastjson/Fastjson2 版本与多态反序列化用法，纳入统一的组件资产管理，做到底数清晰；

**治理多态反序列化用法：**梳理seeAlso、@JsonSubTypes 等多态建模场景，能改为显式类型解析的尽量改造，避免对不可信数据启用多态反序列化；

**坚持最小权限运行：**Java 应用以低权限用户运行，限制 Runtime.exec() 等敏感操作，降低漏洞利用后的危害；

**部署纵深检测能力：**结合WAF、RASP、EDR 对反序列化攻击特征（如 @type 字段、jar:http 变形类名、异常类加载与出向连接行为）进行实时检测与告警；

**纳入常态化扫描：**将Fastjson2 等关键开源组件纳入定期漏洞扫描与供应链安全管理范围；

**回溯历史日志：**检查历史访问日志中是否存在异常@type 请求与可疑出向连接，排查是否已发生攻击尝试；

**完善应急预案：**提前制定Fastjson 系列组件高危漏洞的应急处置预案，做到发现即响应、响应即处置。

Fastjson 族组件历史上多次曝出 AutoType 反序列化高危漏洞，且在国内 Java 业务中部署基数大、暴露面广。建议以本次漏洞处置为契机，完成存量 Fastjson 1.x 业务向 Fastjson2 修复版本的迁移，并将 SafeMode 作为默认基线配置长期保持。

附录：参考资料

[1] Fastjson2 修复补丁（PR #7695）

https://github.com/alibaba/fastjson2/pull/7695/changes

[2] Fastjson2 官方仓库

https://github.com/alibaba/fastjson2

[3] fastjson 1.x 安全公告（CVE-2026-16723）

https://github.com/alibaba/fastjson2/wiki/Security-Advisory:-Remote-Code-Execution-in-fastjson-1.2.68%E2%80%931.2.83

[4] [安天智能体完成Fastjson 2.x RCE漏洞PoC验证](https://mp.weixin.qq.com/s?__biz=Mzg5MTU3NTM0Nw==&mid=2247486163&idx=1&sn=831d763bef668188c67d40ad6f7a42b9&scene=21#wechat_redirect)

[https://mp.weixin.qq.com/s/WFL13fBelHczVdQk6u544g](https://mp.weixin.qq.com/s?__biz=Mzg5MTU3NTM0Nw==&mid=2247486163&idx=1&sn=831d763bef668188c67d40ad6f7a42b9&scene=21#wechat_redirect)

[5] AVL Code官网

<https://www.avlcode.cn>

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Yicx1jVK2eOnMpQiaccCDTrrxNFUNEkjj9HOFJY9d1a1PkIWPTeH4uXSslP7nKTo0qUORjCREJq8BISLcgCepGgw/0?wx_fmt=png)

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