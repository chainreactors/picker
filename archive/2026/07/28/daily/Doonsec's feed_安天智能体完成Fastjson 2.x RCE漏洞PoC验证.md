---
title: 安天智能体完成Fastjson 2.x RCE漏洞PoC验证
url: https://mp.weixin.qq.com/s/WFL13fBelHczVdQk6u544g
source: Doonsec's feed
date: 2026-07-28
fetch_date: 2026-07-29T05:01:20.523149
---

# 安天智能体完成Fastjson 2.x RCE漏洞PoC验证

![cover_image](http://mmecoa.qpic.cn/mmecoa_jpg/Yicx1jVK2eOmk2sdKPoovibtvOxwzGPAeQ5hCPENBsf11kRVEM8Ftw440pMLHlq8C9fhgdtFEcuMNlxEdSTkz4FQ/0?wx_fmt=jpeg)

# 安天智能体完成Fastjson 2.x RCE漏洞PoC验证

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

安天CERT监测到互联网上披露了Fastjson 2.x远程代码执行漏洞。Fastjson2是阿里巴巴开源的Java JSON解析库重构升级版，凭借高性能和简洁的API在国内Java生态中占据主导地位，广泛应用于企业后端服务、微服务网关、数据接口层、政企平台等核心场景。

该漏洞的根因在于：Fastjson2在默认配置未启用SupportAutoType的情况下，部分通用对象解析流程仍会通过内置白名单哈希路径处理JSON中的@type字段。校验逻辑仅将输入类名的增量FNV-1a哈希与预设的白名单哈希值比对，命中后并不核对类名明文是否等于预期白名单类名，也不拦截":"、"!"等协议字符，攻击者可构造哈希碰撞的恶意类名绕过白名单校验，借助支持远程资源加载的上下文类加载器（ClassLoader）加载恶意类，最终实现远程代码执行（RCE）。

**该漏洞利用门槛低：**未经身份验证的攻击者仅需控制JSON请求体，无需目标系统存在任何已知危险类（如 Commons Collections 等常见 gadget 组件），不依赖特定JDK版本的内置类，在默认配置下即可触发，CVSS 3.1评分9.8分，属高危漏洞。漏洞成功利用后，攻击者可在服务器上执行任意代码，可能导致服务器被完全接管、敏感数据泄露、业务系统失陷或被作为内网渗透跳板。

目前漏洞细节已随官方修复提交（PR #7695）披露，PoC暂未公开，暂未发现在野利用行为。但漏洞原理已经公开，攻击者完全有能力在短时间内完成分析和武器化，防守方的修复窗口正在快速收窄。鉴于Fastjson2在国内Java业务中的普及度极高，请各用户单位高度重视，尽快开展资产自查，完成版本升级或临时缓解处置。

**0****2**

****风险描述****

## 2.1 **漏洞基本信息**

|  |  |
| --- | --- |
| **项目** | **内容** |
| **漏洞名称** | Fastjson2 远程代码执行漏洞 |
| **漏洞编号** | 暂无CVE编号 |
| **漏洞类型** | 远程代码执行（RCE）/ 反序列化 AutoType 绕过 |
| **风险等级** | 高危（CVSS 3.1 评分 9.8） |
| **影响版本** | Fastjson2 ≤ 2.0.62 |
| **利用条件** | 远程利用/ 无需认证 / 无需用户交互 / 默认配置即可触发 |
| **PoC状态** | 未公开 |
| **在野利用** | 暂未发现 |
| **修复方式** | 升级至官方修复版本/ 开启SafeMode / WAF加固 |

## 2.2 **漏洞原理分析**

Fastjson2的AutoType功能允许通过JSON中的@type字段指定反序列化的目标类。为防范Fastjson 1.x时期屡次出现的AutoType反序列化漏洞，Fastjson2默认关闭了AutoType，并引入白名单机制——即使AutoType处于禁用状态，解析器仍保留一小部分默认接受的安全类。

问题正出在白名单校验的实现方式上。当Fastjson2解析带有@type的JSON时，若AutoType处于禁用状态，代码会进入"已禁用"校验分支：该分支对输入类名字符串计算增量FNV-1a哈希，并与预设的白名单哈希值进行比对。其关键缺陷在于：命中哈希后，代码未二次验证实际类名明文是否与白名单类名完全一致，也未拦截":"、"!"等协议字符。

攻击者可通过FNV chosen-prefix碰撞技术，构造一个类名字符串，使其哈希值与某个白名单条目一致，但实际指向攻击者控制的恶意类，从而将完整类型名交给上下文ClassLoader的loadClass加载，最终触发远程代码执行。该利用方式不依赖任何第三方危险类（gadget-free），且全JDK版本通杀。

![](https://mmecoa.qpic.cn/mmecoa_png/frAs2k03Ypko0h9nxD3m6tfticyB3pIeawnSNq99ic71iaseHMRMNl0ntvyfuibjpmglFCRCibY3EpQhNTMItCh4FicWxEYZCMZckerCpe3MCY630/640?wx_fmt=png&from=appmsg)

**图1 Fastjson2 远程代码执行漏洞攻击链路示意图**

**0****3**

****受影响范围****

**Fastjson2 ≤ 2.0.62 受影响**

**Fastjson2 > 2.0.62（应用官方修复补丁）不受影响**

注：Fastjson官方在1.2.68及之后的版本中引入了SafeMode安全模式，开启后可完全禁用AutoType。仍使用Fastjson 1.x的用户，建议尽快迁移至Fastjson2修复版本，并同步开启SafeMode。

**0****4**

****AVL Code**完成了PoC的猜测和验证******

安天AVL Code 大模型完成该 Fastjson2 远程代码执行漏洞利用思路推演与 PoC 实操验证，成功加载恶意类触发 RCE，证实漏洞可稳定利用。

![](https://mmecoa.qpic.cn/mmecoa_png/frAs2k03YplGTTY9YF9Afoh5ugVKeRBqDqRWJGiah97Uj0qhLHNhpNpJ75MoL0qvz8XeJiazhD9HVWdGOGibD7DmMYDqpHRokgs8zUPbjdhQj0/640?wx_fmt=png&from=appmsg)

**图2****AVL Code****针对****Fastjson 2****分析验证**

![](https://mmecoa.qpic.cn/sz_mmecoa_png/frAs2k03YpmMBX469UfwMNiaVicEsIDludShhaPm0Nr3gDWJiacV9lt4FFdhvzxNvlwickybHZvic5LiaBFs3ezKOiaWBiciauWGBZ6eklZFticTtP17c/640?wx_fmt=png&from=appmsg)

**图3 安天 AVL Code生成 Fastjson 漏洞 PoC 并完成有效性验证**

**0****5**

**漏洞排查与检测**

## 5.1 **Fastjson版本自查**

Maven项目可检查pom.xml中的fastjson2依赖版本：

<dependency>

<groupId>com.alibaba.fastjson2</groupId>

<artifactId>fastjson2</artifactId>

<version>x.x.x</version>  <!-- 确认版本是否 ≤ 2.0.62 -->

</dependency>

也可在服务器上通过以下命令快速排查：

# 查找 fastjson2 JAR 包

find / -name "fastjson2-\*.jar" 2>/dev/null

# 查看运行中进程加载的 fastjson 组件

lsof | grep fastjson

# Gradle 项目

grep -r "fastjson2" build.gradle

若当前版本在受影响范围内（≤ 2.0.62），且未开启**安全模式（SafeMode）**，则存在安全风险。

## 5.2 **运行时排查**

# 列出 Java 进程

jps -l

# 检查指定进程是否加载了 fastjson2 相关类

jcmd <pid> VM.class\_hierarchy | grep -i fastjson2

## 5.3 **SafeMode 状态检查**

# 检查 JVM 启动参数中是否已启用 SafeMode

ps aux | grep java | grep "fastjson2.parser.safeMode"

# 若输出为空，说明 SafeMode 未启用，存在风险

**0****6**

**漏洞临时缓解处置方案**

## 6.1 **官方升级（推荐）**

目前官方已在GitHub发布修复补丁，建议受影响用户尽快升级至包含修复的最新版本。补丁详情：

https://github.com/alibaba/fastjson2/pull/7695/changes

## 6.2 **开启SafeMode 安全模式**

若暂时无法进行升级操作，可开启SafeMode安全模式作为临时缓解。开启SafeMode后，无论白名单还是黑名单均不支持AutoType，可从底层切断漏洞利用入口。开启方式如下：

**方式一：JVM启动参数（推荐）。**服务启动时追加全局安全模式开关参数：

-Dfastjson2.parser.safeMode=true

# 兼容旧属性名：-Dfastjson.parser.safeMode=true

**方式二：代码配置。**调用全局解析配置实例，主动开启安全模式：

ParserConfig.getGlobalInstance().setSafeMode(true);

**方式三：配置文件。**通过**类路径中的** fastjson2.properties 文件配置：

fastjson2.parser.safeMode=true

此外，也可直接使用fastjson2-noneautotype版本彻底禁用AutoType能力。若业务确实依赖AutoType反序列化，请评估能否改为显式指定目标类型，或仅对可信来源数据使用。

## 6.3 **部署WAF 访问控制拦截策略**

通过Web应用防火墙（WAF）或API网关新增匹配规则，拦截请求体中key包含@type标识字段的JSON请求载荷。@type字段为Fastjson AutoType特性的触发关键字，历史上绝大多数依托该组件实现的远程代码执行漏洞均需借助此字段完成恶意类加载。

配置规则时需兼顾两处数据检测范围：一是POST请求的请求体内容，二是URL拼接携带的参数内容；同时需兼容各类URL编码、特殊字符变形等常见绕过手段，避免恶意请求规避检测。

**0****7**

**安全建议**

**建立组件资产清单：**统计所有业务系统中使用的Fastjson/Fastjson2版本，纳入统一的组件资产管理，做到底数清晰；

**坚持最小权限运行：J**ava应用以低权限用户运行，限制Runtime.exec()等敏感操作，降低漏洞利用后的危害；

**部署纵深检测能力：**结合WAF、RASP、EDR对反序列化攻击特征（如@type字段、异常类加载行为）进行实时检测与告警；

**纳入常态化扫描：**将Fastjson2等关键开源组件纳入定期漏洞扫描与供应链安全管理范围；

**回溯历史日志：**检查历史访问日志中是否存在异常@type请求，排查是否已发生攻击尝试；

**完善应急预案：**提前制定**Fastjson 系列组件**高危漏洞的应急处置预案，做到发现即响应、响应即处置。

Fastjson族组件历史上多次曝出AutoType反序列化高危漏洞，且在国内Java业务中部署基数大、暴露面广。建议各单位以本次漏洞处置为契机，完成存量Fastjson 1.x业务向Fastjson2修复版本的迁移，并将SafeMode作为默认基线配置长期保持。

附录：参考资料

[1] Fastjson2 修复补丁（PR #7695）：

https://github.com/alibaba/fastjson2/pull/7695/changes

[2] Fastjson2 漏洞议题（Issue #7702）：

https://github.com/alibaba/fastjson2/issues/7702

[3] Fastjson2 官方仓库：

https://github.com/alibaba/fastjson2

[4] AVL Code官网

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