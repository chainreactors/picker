---
title: 【工具分享】2026年应急响应取证工具下载，附Windows与Linux手把手教程
url: https://mp.weixin.qq.com/s/lWDutf33i2FadK_vPsI4Wg
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:17:41.600093
---

# 【工具分享】2026年应急响应取证工具下载，附Windows与Linux手把手教程

# 【工具分享】2026年应急响应取证工具下载，附Windows与Linux手把手教程

solarsec
solarsec

solar应急响应团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/DxUXemrrntp3gibjPSCHmSEpdPDqfBcXT5e151v5AJSbV5JtaALLzQe0I1Jibbet7rTia8icjmgo5r4hpY3IMpYPIw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

本文首发于**Solar应急响应团队「州弟学安全（徐龙州）」**，转载请务必注明出处。

Solar应急响应团队由思而听（山东）网络科技有限公司组建，长期专注勒索病毒应急响应、攻击溯源与数据恢复，为遭遇突发勒索事件的企业提供7×24小时突发危机干预通道。如企业正在遭受勒索攻击，可通过应急响应.cn（**https://solarsecurity.cn/****）**或应急响应.com（****https://www.solarert.com/**）**联系我们。

## 写在前面

此前，我们推送文章：[【全面更新】Solar应急响应官网全新发布，应急工具、解密器、勒索家族库全部免费开放（文末抽奖）](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247513744&idx=1&sn=af950dbebd068003528aaf1fea5eff16&scene=21#wechat_redirect)，并发布了取证工具，分别用于Windows和Linux系统。工具发布后，许多读者朋友关心的问题很直接：下载后先打开哪个程序，参数怎么填，采集出来的文件应该看什么，哪些结果只能说明存在线索，哪些结果可以支持进一步判断。

这篇教程按实际操作顺序展开。前半部分讲Windows采集和常见日志分析，后半部分讲Linux脚本与EFU工具。既能照着完成采集，也能理解每类取证结果在溯源中的作用。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQZeu3T2Xc0YrYeqVmRjQ52BZSBFjAIVSOOV0o3FNZvhhfMwXCFJ903cwviaiaysma2qcXAjia379ukeSe3L3W8AAajLImuC7dHsSI/640?wx_fmt=png&from=appmsg)

官网提供Windows和Linux取证工具下载，工具下载地址：应急响应.com/forensics

**使用环境：**所有操作都应在获得授权的设备或分析副本上进行。取证过程会读取文件、日志、注册表和程序运行痕迹，部分功能还会采集样本。操作前应评估业务影响，妥善保留原始证据。采集包可能包含用户名、IP地址、文件路径、浏览器记录等敏感信息，传输和共享时需要控制访问范围并做好脱敏。

**版本说明：**工具会持续更新，界面、文件名和输出目录可能随版本调整，请以实际下载版本及详情页说明为准。文中的文件数量、采集耗时、事件数量和日志内容均来自演示环境，不作为固定性能指标或现实事件结论。后续在线更新能力以官网实际上线情况为准。

### 相关实战案例

工具解决的是采集和初步整理问题，攻击入口、执行过程和持久化方式仍需结合现场证据分析。以下案例可与本教程配合阅读：

[【成功案例】成功挫败 888 勒索家族历时半年的百万赎金勒索，应急处置全流程高效修复，避免千万损失并获客户赠送锦旗](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247504605&idx=1&sn=fb942b0711ddbfab24897adad2ae2f4f&scene=21#wechat_redirect)

[【全网首发】Weax与Sorry勒索病毒席卷全国中小企业，深度还原全链路攻击，疑似黑客利用AI挖掘管家婆0day漏洞](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247510579&idx=1&sn=c8ddda3466a9fc0b75f1121ad96b24c4&scene=21#wechat_redirect)

[【勒索预警】某ERP曝0day漏洞致Weax勒索病毒在国内爆发，波及资产近4万台（合并修订版）](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247511937&idx=1&sn=0b2a89e4a0ab893a71eea71c15d14305&scene=21#wechat_redirect)

[【勒索预警】警惕！Weax勒索病毒改用国内IP发起0day攻击，某地产ERP遭加密，完整溯源复盘（附IOC）](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247512969&idx=1&sn=bc8ace54cffcaf17252e7c8da0ecb05d&scene=21#wechat_redirect)

[【勒索预警】快转发！某财务ERP曝最新0day，Weax勒索病毒携杭州代理IP再次爆发，全网同类资产超十万，完整溯源复盘（附IOC）](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247513584&idx=1&sn=fa69a8b7da95745e00e2eab6b51e3372&scene=21#wechat_redirect)

[【勒索预警】万字溯源分析，weax勒索病毒利用国内代理IP对某ERP使用通杀0day攻击勒索，影响资产近4万（附IOC）](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247514230&idx=1&sn=3840a5b7d9b816623db17acb8a609894&scene=21#wechat_redirect)

[【勒索预警】首发，weax勒索病毒针对用友畅捷通T+应用0day攻击溯源全流程（附IOC）](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247514452&idx=1&sn=d867ab55ab867712051db21537d641ef&scene=21#wechat_redirect)

[【案例分享】你的密码出现在暗网，问题可能出在自己的电脑上](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247514850&idx=1&sn=e4a13ef23a55d0f8977d740296522261&scene=21#wechat_redirect)

## 实际操作

### Windows版本

#### 1.下载与解压

打开**应急响应.com/forensics**，选择Windows版本，进入**查看详情**查看功能说明，再下载压缩包。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYDtkwTf5toMicN2m48iaK5lRb22hkxLUVKtNL3ofeKIe7VFPjd0E3lQRKcDdVzpVPOmvXM96yDt94NADqNTibicibXy23z0sFNkLr8/640?wx_fmt=png&from=appmsg)

Windows和Linux工具均可从对应卡片进入详情页

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQYZkx0aA1SCF8Hy0bLDEZfYy3ia5r2xdPyho9HRkuR3e3Yg1OQer40ft6xtXMglwILUXYJPh2kOHIpJRSichTgtmE452mPZCMhQM/640?wx_fmt=png&from=appmsg)

Windows详情页列出主要采集功能和操作说明

下载后得到一个以日期和时间命名的ZIP压缩包，先完整解压，再运行其中的程序。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYnDia2E4uibv9CXIeC31yAt99XYGW4Iu8Z8CiaAdbh5QZIFicpgAtOgG52HX3sK2GrM7ErRRibEjOuoo75TNkx0PbeibJILzEOuB2Mc/640?wx_fmt=png&from=appmsg)

下载包以日期和时间命名

解压后的目录包含四个文件：

| 文件 | 用途 |
| --- | --- |
| Everything-x64.exe | 建立文件索引，提供文件检索和文件清单相关能力 |
| Solar取证.exe | 主要采集程序，负责执行各项取证任务 |
| Hash.exe | 计算指定文件的哈希值，由主程序按需调用 |
| es.exe | Everything配套命令行组件，一般不需要单独操作 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQZV1Udn8MjXXgkgaHXP7AziaBpB9960uNVxYNBRgiaKKE7iccAibmicyF4ENNicNfqP6KurUOchAZBaQp02J6y9nVheeKjib1NzL7oYng/640?wx_fmt=png&from=appmsg)

Windows版本解压后包含主程序和三个配套组件

**这几个文件需要保留在同一目录。**只复制`Solar取证.exe`到其他位置运行，可能导致依赖组件无法调用。

#### 2.启动程序

第一步，右键`Everything-x64.exe`，选择“以管理员身份运行”。首次启动后等待文件索引建立，并保持程序运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQYeJxciaU8bd5lKsC72Fm8jibjaeD7mN62GZicrJ5ibbicSFtfyYD53n2CtjYdKffSsuoy7T9jNt56z1eib16hcePInsCQV6hWU762lw/640?wx_fmt=png&from=appmsg)

Everything按演示方式以管理员身份运行

第二步，右键`Solar取证.exe`，同样选择“以管理员身份运行”。部分系统日志、注册表和受保护目录需要较高权限才能读取，权限不足可能造成采集不完整。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQZr3nUOfDjfuTre3qgYboClkfO24Zppg5FwWxqaoUHSC8NJWkNPWddspibMDP2nd7sgKTZeYfzbhx6lkEI2bWjYC1ibbxtaloAe4/640?wx_fmt=png&from=appmsg)

Solar取证主程序按演示方式以管理员身份运行

#### 3.配置采集任务

主界面主要包含输出目录、哈希文件、文件后缀、勒索信名称和取证项目五部分。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQZRQV6fxbicrMR95bKyw3ia0Nm7lzLdpWS7UISs7SGHg10RazjfYjiaywKnxb4NchiclZGFaricxAtTXMok5UuTFfzF7zH4vNyJ3WFY/640?wx_fmt=png&from=appmsg)

采集前检查输出位置、检索条件和取证项目

各项配置如下：

| 配置项 | 填写方法与用途 |
| --- | --- |
| 输出目录 | 默认输出到当前目录，也可点击“浏览”修改。选择剩余空间充足、便于后续打包保存的位置 |
| 哈希文件 | 默认为空。需要核对某个文件时，选择该文件，主程序会调用同目录下的Hash.exe计算哈希 |
| 后缀 | 遍历指定扩展名的文件。勒索事件中可填写加密文件后缀，用于定位样本和统计分布 |
| 勒索信名称 | 遍历指定名称的勒索信，例如README.txt，实际填写时以现场发现的完整文件名称为准 |
| 取证项目 | 默认全部勾选。首次采集可保留默认配置，现场已有明确范围时再按需调整 |

**当前官网详情页提示，后缀填写时不加小数点，例如**`weax`**。截图用于说明字段位置，不建议照搬其中的示例值，实操以当前版本详情页提示为准。**

“获取样本”可能涉及恶意文件。采集后的样本应隔离保存，避免在办公终端直接双击、解压执行或与无关人员共享。

配置完成后，点击“开始取证”。

#### 4.检查执行结果

采集期间，执行日志会显示当前任务和返回信息。出现“执行完成”提示后，先检查日志中是否存在文件不存在、权限不足、解析失败或其他错误，再查看输出目录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQbCnUZBibl8zwcSn87Url3RSMfospsj16Ta0W8ewGE3eG1rmKQMJtM0icjicjIZ4mb3UKcibudRND56iad49rtymLOkiapwNepxnBoko/640?wx_fmt=png&from=appmsg)

执行日志用于确认各模块是否完成以及是否出现错误

**“执行完成”只表示采集流程结束，不等于每个模块都成功，更不等于系统没有异常。**某个模块报错时，应保留错误信息，结合系统版本、组件状态和运行权限判断原因。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYxklVpPrOw7mhu271Xk6GCIS1SwAdMbSDUJTNGsYex6iaEFJN5icBbBvVYO7icibYRia6ILjDKtw5z1YJnQZmSzfXjWopqbYTwNRwI/640?wx_fmt=png&from=appmsg)

采集结果按主机和时间等信息生成独立目录

不同系统环境和工具版本的输出会有差异，常见内容可按下表理解：

| 输出内容 | 主要用途 |
| --- | --- |
| iisLogs | IIS Web访问日志，用于分析请求来源、访问路径和响应状态 |
| jumplist | 应用程序跳转列表，用于还原用户与文件、目录的交互线索 |
| Logs | Windows事件日志，包括安全、系统、PowerShell等日志 |
| Recent | 各用户最近访问项目及快捷方式等线索 |
| reg | 导出的注册表文件，用于排查启动项、服务和用户操作痕迹 |
| SRUM | 应用资源使用、网络连接和流量等记录及解析结果 |
| Amcache、AppCompatCache相关文件 | 程序文件和兼容性缓存线索，需结合其他证据判断 |
| prefetch、prefetch.csv | Prefetch原始文件及解析结果，用于辅助分析程序执行痕迹 |
| 计划任务.csv、系统启动项.csv | 持久化入口排查 |
| ProcessTree.csv、ProcessModules、网络连接.csv | 采集时点的进程、模块和网络连接快照 |
| 1.efu | 文件清单，可配合Everything继续检索文件名和路径 |
| Sample | 按采集条件获取的样本，需在隔离环境中分析 |
| hosts、DnsCache、certutil相关输出 | hosts配置、DNS缓存和证书工具缓存等辅助线索 |

进程、网络连接和本地用户等结果反映的是采集时点状态。攻击程序已经退出或连接已经断开时，快照中可能看不到历史行为，需要继续检查日志和其他痕迹。

### 溯源视角分析日志文件

采集完成后，分析工作可以围绕四个问题展开：攻击从哪里进入，执行了什么，如何保持访问，是否有数据外传。单条日志通常只能回答其中一小部分，需要按时间和对象交叉验证。

#### 1.IIS Web访问日志

如果业务系统运行了IIS Web应用，且怀疑攻击从Web入口进入，可以优先查看`iisLogs`目录。文件名通常包含站点和日期信息，文件大小可作为安排排查顺序的参考。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQZYPMDAbRKhjYWHicQoTicDea79Ozyic6x0LiaH63YZXBR3mP3NZjebPEHnicyBE2JGrrc5lS13hic1k6vIUvdTxB6L2uWmtnI7TCVug/640?wx_fmt=png&from=appmsg)

演示环境中的`u_ex261113.log`为546 KB，明显大于其他文件，可优先检查

**文件变大不等于遭到扫描。**业务量增长、日志拆分策略变化、异常请求增多都可能改变文件大小，它只能帮助决定先看哪个文件。

打开日志后，重点看请求时间、来源IP、请求路径、User-Agent和HTTP状态码。演示日志中，同一来源在短时间内请求了大量无规律路径，并出现密集的404状态码，这类特征支持目录或文件扫描判断。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQYJH5LDcHbzE8kxFVQpW7Bg90WibtwChkiajX6EUp1IHJU4dvKS2YB7jm50BOFDHbWwawYk0IiaklU7OSYHvUxEIssibWuwuBuzazg/640?wx_fmt=png&from=appmsg)

短时间内出现大量无规律路径请求，并伴随密集404状态码

404表示服务器未找到请求资源。它能说明扫描和探测行为存在，但不能证明漏洞利用成功。即使出现200状态码，也只能说明请求得到成功响应，仍需检查可疑接口的请求内容、后续文件落地、进程执行、数据库操作和其他日志。

IIS W3C日志通常按UTC记录时间。与Windows本地事件、文件时间或其他设备日志互证时，应先核对日志格式和时区，再换算到同一时间基准，避免把攻击链顺序排错。

#### 2.Jump List跳转列表

Jump List可理解为应用程序的跳转列表痕迹，常见于任务栏或开始菜单的最近项目、固定项目等功能。它可能保留应用程序、目标路径、目标时间和文件系统记录等信息，用于辅助还原用户访问过哪些文件或目录。

原始文件通常位于`jumplist`目录，常见扩展名包括：

* `.automaticDestinations-ms`
* `.customDestinations-...