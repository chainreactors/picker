---
title: 攻击者网站目录问题 暴露其用 AI 把攻击做成了流水线
url: https://mp.weixin.qq.com/s/fJws6yg8dM-6Hs94u9iRuQ
source: Doonsec's feed
date: 2026-07-23
fetch_date: 2026-07-24T05:03:43.486237
---

# 攻击者网站目录问题 暴露其用 AI 把攻击做成了流水线

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDpXX83Zcz0iaYoCB2An09zHwf4LoQ5O6bsBJ1KJibncpwibiaqNTzRMcgdSoXceweWKwRqMzvYMU72ye0ETeMsLYMsS2WMZUTJsMYQ/0?wx_fmt=jpeg)

# 攻击者网站目录问题 暴露其用 AI 把攻击做成了流水线

白帽子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于黑鸟
，作者黑鸟

![](https://wx.qlogo.cn/mmhead/X4XEGYefSBSxrDYncLtKiacf7vZpHQnuLDMVc1rQjZsw9xYSM6kSCezibImssYuBjTibclnyop737M/0)

**黑鸟**
.

一介草民，深耕威胁情报领域多年，自封威胁分析师，APT狩猎者，战略忽悠分析师。 专注推送一切前沿高科技/人工智能、网络安全分析、敌我战略分析、数据挖掘、情报扩线、网络武器分析、社会工程学、一切开源情报、军事分析忽悠等。

最近Rapid7 的威胁研究团队从一条普通的MDR (托管检测与响应)告警出发，顺藤摸瓜挖出了一整套完全暴露的攻击者基础设施。这不是普通的恶意文件托管服务器，而是一个功能完整的恶意软件交付实验室，里面存放了超过1000 份攻击相关文件，完整记录了攻击者测试交付路径、制作社工诱饵、验证WebDAV 执行方法的全流程。

[rapid7.com/blog/post/tr-exposed-webdav-malware-delivery-lab-analysis/]

更值得关注的是，整个实验室的运作模式已经脱离了传统小作坊式的攻击开发，攻击者开始借助生成式AI 搭建标准化的研发流程，像正规软件产品团队一样快速迭代攻击手段，攻防对抗的节奏正在被彻底拉高。

一条告警牵出的完整攻击车间

最初的告警来自一次终端执行行为，有用户通过rundll32.exe 运行了从WebDAV 服务器拉取的文件，终端遥测显示WebClient 服务启动后，davclnt.dll向远程主机发起连接获取内容。

WebDAV 是一种网络文件共享协议，Windows原生支持，可以让用户像访问本地文件夹一样打开远程服务器上的文件。因为是系统原生支持的功能，很多安全检测会对这类流量放松警惕，所以成了近年攻击者投递恶意文件的热门通道。

研究人员顺着这个交付地址深入排查，意外发现服务器的目录是完全公开的，里面没有简单堆砌恶意payload (攻击载荷)，而是按功能划分了完整的工作区，既有存放最终载荷的目录，也有隔离测试不同投递方式的专区，甚至还有专门的QA 测试区用来验证诱饵在浏览器和资源管理器里的显示效果。

统计下来整个目录一共1048 个文件，覆盖了攻击交付的全链路环节。其中453 个是LNK 快捷方式诱饵，批量生成不同主题和执行路径的钓鱼快捷方式，搭配伪装文件名和虚假图标。236个是文件名伪装测试样本，用来验证Unicode 字符、双扩展名、空格填充等手段在不同环境下的欺骗效果。146个是 URL 和 LOLBins (系统自带合法工具)执行测试文件，尝试用各种 Windows 签名程序结合远程工作目录实现 WebDAV 场景下的代码执行。除此之外还有 89 个加密加载器、24 种另类执行容器、17个 WebDAV 适配脚本、9 个社工诱导网页，以及大量构建脚本和操作说明文档。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoGFILpulVRjEvcb05dEyzAwQW6B3zJI9ibSp9679EiaunhHqek1ddaaIqIK4R7SrZ4MDUfMufpD0wgWKwnux4gBzzMZ6Bfj1BO4/640?wx_fmt=png&from=appmsg)

像产品团队一样做测试的攻击者

整个暴露的目录最直观的感受，是攻击者已经形成了体系化的测试流程，完全按照产品迭代的逻辑打磨攻击手段。

他们重点测试了多个近年披露的高危漏洞，其中最完善的测试集针对CVE-2025-33053。这是一个Windows 互联网快捷方式漏洞，最早由Check Point 在分析Stealth Falcon APT 组织的活动时披露，核心原理是利用.url快捷文件启动系统自带的合法程序，同时将程序的工作目录设置为攻击者控制的WebDAV 共享。当合法程序调用子进程时，会优先从当前工作目录查找对应文件名的程序，这样攻击者放在共享里的同名恶意文件就会被执行，全程不会触发SmartScreen 或者Mark of the Web 安全警告。

![testing-files-subfolders.png](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpDIoUJ5UeSTyZ4GZoetsAkNrLz1UckriaavCiafjqXIbSLmOCQ2WVXlMbIe5LT2XzHfS7u0BxsITIqRH4CWYysicMCHRTWgzKZG8/640?wx_fmt=png&from=appmsg)

攻击者留下的README 文档完整还原了这个漏洞的利用逻辑，甚至直接沿用了原分析报告里的示例路径。文档里明确标注了首选的利用程序是iediagcmd.exe 也就是IE 浏览器的诊断工具，还详细列出了不同Windows 版本的兼容性、补丁影响、以及备选的利用程序清单。除此之外他们还测试了CVE-2026-21513 这个MSHTML 框架安全绕过漏洞，以及CVE-2025-24054 这个NTLM 泄露漏洞，后者通常结合.library-ms文件利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqIMcaoplX2GHDSme5HibJIpA2volbzkh5o2qB1YwEvbmEc46Fxiaa7qsj7V7zonG0EQdew4vhdaS734Z1RA0qJALcuvUbyqicm14/640?wx_fmt=png&from=appmsg)

他们的测试维度覆盖了攻击落地的每一个细节。传输层同时测试了80 端口和443 端口加密的WebDAV 链路，路径格式对比了DavWWWRoot 和普通UNC 路径的差异。针对没有iediagcmd.exe 的主机，他们准备了CustomShellHost.exe、OfficeC2RClient.exe等多个备选 LOLBins。下载执行的载体测试了 bitsadmin、certutil、mshta等多种常见工具，快捷方式执行搭配了隐藏窗口、参数混淆等规避手段，甚至还测试了search-ms 查询、library-ms文件等可以直接在资源管理器里加载远程内容的投递容器。

所有测试内容都配有详细的说明文档，文档的结构化程度、表述方式和排版风格，都指向攻击者大量使用LLM (大语言模型)生成内容。比如其中一份测试套件直接把单个漏洞的利用扩展到了59 个不同Windows 二进制程序的批量测试，还按成功率划分了测试优先级，附带完整的原理说明和结果验证方法，整个文档的产出效率和规整度远高于传统手工编写的攻击手册。

批量生产的钓鱼诱饵，瞄准每一个日常场景

攻击者在诱饵制作上投入了大量精力，目标就是让恶意文件看起来和普通办公文档没有区别。

诱饵的主题全是企业用户日常高频接触的内容，包括发票、隐私政策、合同、签署文件、财务报告、工资单、医疗机构报告等等，目标就是降低用户的警惕性。大部分诱饵都伪装成PDF 或者Office 文档格式，通过伪造图标、隐藏扩展名、最小化启动窗口等手段，让用户双击的时候以为只是打开了一份普通文件。

除了文件类诱饵，他们还准备了大量ClickFix 格式的HTML 社工页面。这些页面伪装成Cloudflare 验证、Adobe文档错误、微软登录界面、Chrome 更新提示、Discord 通知等常见场景，诱导用户手动复制命令到终端执行。这类手法不需要用户下载可执行文件，靠社会工程学就能直接触发代码执行，绕过很多基于文件的安全检测。

所有诱饵的主题、文案、页面结构都呈现出批量生成的特征，同样有明显的LLM 辅助创作痕迹，攻击者可以快速产出适配不同场景、不同目标人群的钓鱼内容，大幅降低了社工诱饵的制作成本。

两条典型攻击链，藏着成熟的规避手段

研究人员重点分析了两个正在活跃的攻击活动，完整还原了从投递到最终载荷执行的全链路，两条链路最终投递的都是PureRAT 家族的恶意程序，但实现架构完全不同。

第一个是针对墨西哥地区的CURP 活动。攻击者搭建了钓鱼网站gobf [.] mx，仿冒墨西哥政府官方的CURP 人口登记查询服务，页面做得和官方网站高度相似，诱导用户输入身份信息查询记录。当用户点击下载查询结果按钮时，网站不会直接提供PDF 文件，而是通过前端JavaScript 调用search-ms 协议，直接在用户的Windows 资源管理器里打开攻击者的WebDAV 共享文件夹，并且自动过滤出.scr格式的可执行文件。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqnYNHVPs5Ysg47dsSsIz2xRg4AyIUZXiaqc5nKxvpzLT5iaV5rQJnrWcic1LAwZSgxMk1mJDEljjFAjJI23M1xz3csqdyQsD4A2I/640?wx_fmt=png&from=appmsg)

最具迷惑性的是，文件夹里的ReportFinal.rcs.pdf 看起来是标准PDF 文件，实际是用RTLO (右向左覆盖字符)伪装的.scr 可执行程序。用户双击之后，Inno Setup 安装包会解压释放 Fo-Binary.exe 加载器，接着通过process hollowing (进程镂空)技术，把恶意代码注入到有合法 EV 签名的奇虎 360 进程里执行，全程可以绕过大量安全检测。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoicAIR6gXcccCiauc46pAyYoXibiaWVSiaKmHYY77GqibyFCGImOtWYeuiaAnFoCMz5jnf07AIdRWgHgDVUHEom4EtibeQlAV4hgyAsNk/640?wx_fmt=png&from=appmsg)

最终的载荷是PureRAT4.4.3，一款基于.NET开发的信息窃取木马，全程无文件运行在内存中。它会窃取受害者设备上的加密货币钱包数据、浏览器保存的账号密码和Cookie、Telegram会话数据、Foxmail 邮件内容，同时截取桌面屏幕。木马自带反调试和反沙箱检测，一旦发现处于分析环境就会立刻终止运行，窃取到的所有数据会通过加密通道发送到远程C2 (命令与控制)服务器。

第二个是名为DlrtyGames 的攻击链，采用了完全不同的DLL sideloading (DLL 侧加载)投递架构。攻击入口是 7-Zip 制作的自解压包 DlrtyGames.exe，解压后会释放两个文件，一个是合法签名的育碧程序Volt\_Droid.exe，另一个是恶意的discord-rpc.x64.dll。当用户运行合法程序时，会优先加载同目录下的恶意DLL 文件，完成初始执行。

后续的载荷被加密藏在一张PNG 图片的IDAT 数据块里，属于隐写术的一种，能绕过很多针对文件格式的检测。恶意DLL 会解密图片里的载荷，等待45 秒规避沙箱检测后，通过dllhost.exe 完成权限提升，最终同样用进程镂空技术把木马注入到合法签名的进程中运行。

这个链路的最终载荷是模块化的RAT (远程访问木马)，具备键盘记录、屏幕截图、窗口监控、远程命令执行等功能。键盘记录模块会针对支付、银行、加密货币相关的关键词触发数据窃取，覆盖了绝大多数主流金融和加密平台的关键词，针对性非常强。

AI 加持下，攻击研发正在工业化

这次事件最核心的警示，不是攻击者用AI 写了恶意代码，而是他们用LLM 重构了整个攻击研发流程，把原本零散的攻击手段变成了标准化的产品流水线。

从遗留的文件能清晰看到整个运作模式。攻击者用LLM 批量生成测试文档、漏洞利用说明、诱饵制作指南，把单个漏洞快速扩展成覆盖几十种场景的测试矩阵。他们开发了名为Simba Service 的WebDAV 交付管理面板，自带访问统计、访客画像、风险拦截、链接生成等完整功能，面板的文档和界面同样有大量LLM 生成的痕迹。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqapcoYurhTkH10LsXcNErIoqb82mOOmhicY5txJuntWI3MiaChtcxyJmVDIHO5gYiaR1LhJQyLP2fqPxsMHtcxybKtV3MsRPqmU4/640?wx_fmt=png&from=appmsg)

整个项目的工程化程度很高，管理面板基于Python 开发，搭配SQLite 数据库和Tailwind 前端，部署在Ubuntu 服务器上，支持实时监控文件访问、统计不同诱饵的转化率、自动识别并拦截扫描器IP。5.5天的运行日志里，这套系统一共处理了77098 次请求，来自101 个国家的3892 个独立IP，累计传输了45.9GB 数据，其中97% 的执行请求都来自CURP 活动的诱饵，攻击流量高度集中在墨西哥地区，峰值正好对应墨西哥的工作时段，完全是一套成熟可量化的攻击交付系统。

更有戏剧性的是，攻击者的OPSEC (操作安全)意识严重不足，不仅把整个测试目录公开在服务器上，连管理面板都保留了默认的账号密码，所有内部架构、接口文档、部署配置全部暴露在外，相当于把自己的整个研发车间直接展示给了防守方。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqHY87e4UW9yR8gOkQV3m5gHUyMiahI0Yd3d970Nrh6TPvQPTYqiaQnibmCf7lmYVDibibeicvdS8Ske9xeibG2HYXfDOrPXRJMPKTc78/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoKGgtNoJqMcHJmwcAw34Nh6T3b5LibOJeQ71R3HUKGMHgNxPRAr7xlzMI5PL56PD6ic6KIWwdgJXXwpapau4UpfJUIicg6Ef8c64/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqnP8myv7wdpQbtCFQR4Accbdqd5O3HECJPsOV7a3ktcHHv0rxQUDPYIiaa8ZZXyKIOXUnj6MvHrdanKmRo1ibAUKPGSfNz30IB8/640?wx_fmt=png&from=appmsg)

从攻击技术覆盖来看，整套链路覆盖了MITRE ATT&CK 框架里的用户执行、文件伪装、DLL劫持、进程注入、凭据窃取、加密C2 等三十余项技术点，同时还涉及多个和LLM 辅助攻击相关的AML 框架技术项，完整呈现了AI 时代攻击活动的新形态。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqh2pkMzMljBDgY19zQ3gy0x21AaOxeh4r9t3ApkOb0cXSZUFmj3Un6Re09ibvQVd945NicMxhxbBn6g2kyVvFkYZdiaGLjzmSIF4/640?wx_fmt=png&from=appmsg)

帮你节省噪音信息筛查时间⬇️

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

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