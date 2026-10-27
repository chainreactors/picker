---
title: 银狐木马再升级｜“镜昙” 团伙镜像投毒、定时失活攻击专项研判
url: https://mp.weixin.qq.com/s/8fDUDrMtxm4_J20OCW3_QQ
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T06:58:54.320099
---

# 银狐木马再升级｜“镜昙” 团伙镜像投毒、定时失活攻击专项研判

# 银狐木马再升级｜“镜昙” 团伙镜像投毒、定时失活攻击专项研判

信息安全研究

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于国家互联网应急中心CNCERT
，作者CNCERT

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM7x2UYGIAGwcwufoYr2R16synysQjwIEVJzwyjBcVT8Cg/0)

**国家互联网应急中心CNCERT**
.

国家计算机网络应急技术处理协调中心（简称“国家互联网应急中心”，英文简称CNCERT或CNCERT/CC），成立于2001年8月，为非政府非盈利的网络安全技术中心，是中国计算机网络应急处理体系中的牵头单位。

**点击蓝字 关注我们**

# 关于“银狐”木马“镜昙（G02）”团伙攻击态势深入分析报告

**一、事件概述**

在“银狐”木马专项工作中，CNCERT监测发现，银狐新团伙“镜昙”近期利用搜索引擎SEO/仿冒软件下载站/其他渠道传播银狐木马。该团伙依托镜像文件投毒，且恶意程序可按预设时间自动终止，攻击呈现“昙花一现”的特征。相比银狐历史分支，镜昙完成多维度技术升级：改用 IMG/ISO/VHD 镜像载体规避静态检测、采用三重混淆加密保护木马配置、重构配置存储加载架构，并新增可定制的攻击失活时间机制，隐蔽性与可控性显著增强。

专项工作组围绕该团伙的域名、下载链、样本、C2及通信行为开展关联分析，研判发现其具有载荷类型新、批量注册、模板复用、白加黑、持久化、反分析、攻击时间定制化等特征。2026年7月17日至10月20日累计被控设备5834台，单日上线被控客户端最高252台，C2日访问峰值为727802次。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRg18tcQKicqXKtdA1FdaJKcPmXwLeQAxcsd4DRTbGdZ83d2sLYgzLY0W6iauGFiblBVZTShh6VQZLbeCCOkGvQye6ruseUvfbzpXE/640?wx_fmt=png&from=appmsg#imgIndex=1)

图1 “镜昙”团伙攻击活动总体链路

**二、团伙画像与活动特征**

“镜昙” 银狐团伙是银狐攻击生态下独立运营的全新攻击分支，目标聚焦金融财务、银行、税务领域，攻击对象覆盖简体、繁体中文用户群体。该分支最早于2026年7月中下旬至8月开始活动，9月进入集中爆发阶段，活跃时间窗口显著晚于银狐历史分支。

团伙代号“镜昙”来源于两大攻击特征：一是以镜像类文件作为初始攻击载体；二是攻击时间支持定制，到达设定日期后停止执行恶意行为，呈现 “昙花一现” 的攻击特点。相较于银狐既往攻击分支，镜昙分支在载荷模式、加解密特征、配置存储加载机制、攻击时间可控能力等方面完成全面技术迭代升级，核心差异与技术更新如下：

1）恶意载荷投递方式全面革新：区别于银狐传统分支惯用的MSI安装包、NSIS/Inno Setup封装EXE可执行文件的投递形式，镜昙分支团伙采用IMG、ISO、VHD镜像文件作为核心恶意载荷载体。攻击者借助合法第三方对象存储桶或搭建钓鱼页面诱导用户下载仿冒软件，利用镜像文件的特殊属性规避主流静态检测手段，大幅丰富攻击投递链路，提升载荷落地成功率。

2）配置信息加密强度大幅提升：传统银狐木马仅对配置信息进行简单逆序处理后硬编码嵌入样本，对抗能力较弱。镜昙分支团伙对配置混淆机制完成全面升级，采用逆序→加密→逆序三重混淆处理逻辑，极大提升了配置信息的隐藏效果，显著增加安全分析人员提取、解密、解析木马配置信息的难度。

3）配置信息存储与加载模式重构优化：该分支团伙彻底摒弃银狐传统的硬编码配置存储方式，重构了配置存储与加载架构。攻击者将木马配置信息与shellcode代码合并后整体加密，独立存放于专属文件中，后续通过独立解密模块完成解密、执行shellcode，再将有效配置参数传递至winos木马主体，以规避常规特征检测与静态IOC提取手段，提升攻击隐蔽性。

4）新增攻击时间定制化可控机制：银狐既往分支的木马样本均无失活时间等限制条件，攻击生命周期不可控。而分支团伙新增精细化时间对抗机制，在木马配置模块中内置专属失活时间，可自主控制恶意程序的有效存活与攻击周期，既提升了攻击者对整体攻击活动的可控性，也进一步规避长期驻留带来的溯源与检测风险，强化整体对抗能力。

（一）团伙概况

|  |  |
| --- | --- |
| **项目** | **内容** |
| 团伙名称 | “镜昙”团伙 |
| 最早可追溯时间 | 2026年7月下旬（2026.7.22日） |
| 主要攻击目标 | 中文背景用户（简体/繁体并存）；行业聚焦金融财务/银行/税务方向 |
| 主要传播渠道 | 搜索引擎检索引流+仿冒软件下载站、第三方对象存储桶资源直链下发镜像 （仿冒企业办公软件/税务/银行对账等） |
| 主要恶意功能 | 远控与信息窃取 |
| 当前活跃情况 | 持续活跃中：截至分析时间（2026.10.14）部分钓鱼页面仍可访问下载，最新下载样本远控配置CC持续有效； |

（二）传播资源与基础设施特征

|  |  |  |
| --- | --- | --- |
| 观察维度 | 统计结果 | 主要特征 |
| 域名与注册 | 自有C2／中转域名池28 个（19 个.club + 9 个.cc） | 后缀集中于.club、.cc；该批域名呈字母+数字 或纯字母 规律命名（acms555、taku788、moik77a、qzqy688 fshsjlk 、hscdmnz、Hdfnxzn、hxnxcan），疑批量注册。注册商均为为22net, Inc. 是一家位于中国的 ICANN 认证域名注册商，总部在杭州 |
| 解析与托管 | 钓鱼侧承载IP 64.81.30.137 单点承载16 个域；C2 侧非标端口直连IP | 钓鱼侧域名多为“tax”前缀，仿冒税务相关软件/文档（tax-documentsXX、company-tool）；网站通过“企业软件安全下载中心”标题仿冒企业安全软件 |
| 下载基础设施 | 阿里云OSS 6 bucket（东京／雅加达／香港）+ 腾讯云 COS 6 bucket（新加坡／香港／雅加达）+ AWS S3（yingxiang.s3.ap-northeast-1.amazonaws.com） | 三家云厂商分池托管；载荷名setup.exe、<随机>.exe、DMRootCA.zip、202609013823.img |

**三、典型攻击活动分析**

（一）传播入口

攻击者通过发送钓鱼链接或钓鱼跳转诱导用户访问钓鱼网站下载恶意文件。攻击者注册钓鱼域名，搭建名为“星河科技软件下载中心”的银狐仿冒网站，提供伪装的“企业官方软件安装包”下载功能。攻击者实施SEO污染与钓鱼投递，以此确保必应搜索“星河科技软件下载中心”，搜索页面排名靠前的搜索结果大多为银狐组织仿冒网站，搜索结果如下图所示。推测其可能在发送信息中使用跳转页面、下载提示或话术中使用“星河科技软件下载中心”等字样，以促使部分用户查找、访问钓鱼网站。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/aoXpXT1UJRjqBmr1psuFhfuleia4Wia5BnPuo9B2RicUPotGLrDGRcVVa91fHpAwTEreibMnAcIdCdV4zWVFjegkfa2Sq4Z7Lh2mIjpqQwT0o8U/640?wx_fmt=jpeg&from=appmsg#imgIndex=2)

图2 传播入口或仿冒页面

打开后页面如下图所示，页面以“安全、稳定、快速的软件分发中心”为话术，落地页标题统一为“星河科技软件下载中心”。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRhEvsnr4L8Xk05zCdsjnhMOTcjFFf3moRBOnrHnAwp9EUibHsKMjEmk4PUDoXOicb8Scl8urQnvBlsW5vpl3qxnmA5djAvTZ5icgA/640?wx_fmt=png&from=appmsg#imgIndex=3)

图3 仿冒钓鱼页面

（二）跳转与下载链接

钓鱼页面包含多个下载链接，分别对应恶意文件的不同版本（如链接格式为 https://taxationjfwk.com/download/tax-documentsXX，XX 为数字后缀）；攻击者只需修改该数字后缀，即可实现恶意文件的版本更新。点击即可下载诱饵文件，这些诱饵文件采用税务文件、对账单据、采购订单、逾期账户对账单等财税业务主题构建或直接以时间命名，如“tax-documents1.zip”、“Reconcile an account.zip”、“Statement of Outstanding Account.zip”、“Bank Statement.zip”等。下载的ZIP文件解压即得到恶意IMG/ISO/VHD文件，以此规避杀毒软件对EXE等常用格式文件的静态检测。

|  |  |  |  |
| --- | --- | --- | --- |
| 环节 | URL/域名 | 作用 | 核验时间 |
| 入口 | taxationjfwk.com（解析ip:64.81.30.137） | 仿冒网站 | 2026.9.12 |
| 跳转 | https://taxationjfwk.com/download/tax-documentsXX | 下载链接（XX为数字，支持通过数字进行更新及多个版本链接下载) | 2026.9.12 |
| 下载 | https://taxationjfwk.com/download/tax-documents42 | 当前分析文件下载链接 | 2026.9.12 |
| 最新链接 | https://taxationjfwkjfkk.com/download/tax-documents9 | 同ip解析的域名对应的最新链接；持续更新生成不同批次的仿冒链接。 | 2026.9.23 |

（三）样本落地与执行

以样本

1886e9fb95c4b1a62ae192e688f583f9d4c444f02082a7768041603517f52f52为例，该样本为IMG文件，其中包含名为“AMD.0903002123.EXE”的合法程序和名为“xwEB\_eLF.dLl”的恶意DLL文件，用户执行“AMD.0903002123.exe”时，以白加黑方式启动“xwEB\_eLF.dLl”。该恶意DLL首先解密配置信息，检测当前的系统时间是否晚于有效期限。如果已超期，则弹出提示框并退出进程；否则执行后续恶意功能。在“%public%”下创建名为“NVTELEMETRY”的文件夹及随机名称的子文件夹，并将上述合法程序复制为“NvTelemetryBridge64.exe”，复制恶意DLL文件，然后创建新进程，执行该合法程序。

新进程启动后，以白加黑方式启动恶意模块“xwEB\_eLF.dLl”，执行恶意行为。

![图片](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRhu0FOslP0iadLFRonqtxSeZ4WtkQdyYVpicibn4a7w6hdibTeYQXoRB9iaSvMcZQV5cSsk89qzYsN0wSsELbRxTZzRzUbIKToOKgmI/640?wx_fmt=png&from=appmsg#imgIndex=4)

图4 样本执行链

（四）远程控制与恶意功能

恶意DLL模块启动后，解密出配置信息并解析各个字段，向C2（acms555.club）发起连接，下载执行具有后门功能的“登录模块”。该后门具备文件管理、键盘记录、插件动态加载、系统重启/关机等多种控制能力。

![图片](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRhnicJjRK31Eyicgic1bCugPQ0Bov7bEtctJB1goIUWWpLbJ9KsT67mzda8EO6PjJpPhgZHkHo4Ze44CH577WtVsNV9hYS8j12hRU/640?wx_fmt=png&from=appmsg#imgIndex=5)

图5 通信或恶意功能证据

**四、典型恶意样本分析**

如下为该团伙使用恶意样本的分析结果，该样本详细信息如下表所示。

|  |  |
| --- | --- |
| **样本标签** | **内容** |
| SHA-256 | 1886e9fb95c4b1a62ae192e688f583f9d4c444f02082a7768041603517f52f52 |
| 文件名称 | AMD.0903002123.img |
| 文件大小 | 9.98 MB (10469376 bytes) |
| 文件类型 | IMG镜像文件 |
| 数字签名 | 无 |
| 编译/时间特征 | 2026.09.03 |
| 投递来源 | 钓鱼网站 |
| 主要功能 | 银狐木马的上线模块（即下载器） |

（一）初始载荷与解密加载

前置攻击载荷通过钓鱼网站诱骗用户下载相关仿冒软件类的恶意文件。下载关键词多与税务、财务、企业办公相关。

|  |  |
| --- | --- |
| **关键词** | **攻击指向** |
| tax-documents | 税务 |
| Reconcile an account、Statement of Outstanding Account、Bank Statement | 银行对账/财务 |
| Purchase Order | 企业采购 |
| company-XX、软件下载 | 企业/办公软件 |

本次分析中下载的母体压缩包文件名为 “tax-documentsXX” (XX为数字)，内嵌文件为主体分析文件：“AMD.0903002123.img”

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRjoRhY3KKzt7pJzkznUx7dP9ialE7y8f9NULiaZYSgibTic4RrAfgN9ics2f7cN9PgIZltibs79NuOFGiaB3PKxX1picuW9vAicLsN0dtCY/640?wx_fmt=png&from=appmsg#imgIndex=6)

图6 初始载荷

该IMG文件中包含白文件“AMD.0903002123.exe”和恶意文件“xwEB\_eLF.dLl”，通过白加黑方式启动该恶意文件。如下图所示：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRh5mNYicTIb12bjyewnjwiaYPHY9rJFniagQRuLp9H95jslEnBRDmGWXVZHJ6m1BlAgO0wibndSVroG0Nun9ZJTO8JuaTIWJ3l5VKY/640?wx_fmt=png&from=appmsg#imgIndex=7)

图7 内嵌文件载荷

恶意文件“xwEB\_eLF.dLl”中硬编码了经过加密的配置信息，如下图所示：

![图片](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRhH8tTkdDtWzceHVlpc2qtpbF1otqr8zxkfV581hwglxibUJ1G6uaJwfDfaOwK5z6BJtkyH07EWhPBF7qOibw75dNvpYjUw4FXmc/640?wx_fmt=png&from=appmsg#imgIndex=8)

图8 加密的配置信息

该DLL启动后，首先将该配置信息进行逆序+rc4解密+逆序处理，以得到明文。如下图所示：

![图片](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRgUzCibpeJ8I3dicy3MOiavjrMBXICGyzR60WHdIOG74pS5Snmr2auSITFiaJSicuaOghaSr7tscDDPRFozEhoOVkBaeVkzyhPqfqwU/640?wx_fmt=png&from=appmsg#imgIndex=9)

图9 配置信息解密过程

从明文配置信息可知，C2为“acms555.club”，该恶意程序的制作时间为2026.09.03，失效时间为2026.09.06。

判断当前系统时间是否晚于失效时间，如果是，则弹出提示框并退出当前进程。如下图所示：

![图片](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRjpyhJoSgs7S3FcCIm6kFZRtVzd9mfskkIQj8zvByfxyNBK6NWVzh0r7J8fgliaqn5r457tKcKp4iaEEAT3yux5oPTMKsEZQESgQ/640?wx_fmt=png&from=appmsg#imgIndex=10)

图10 检测是否在有效期内

弹出的超期提示框如下图所示，如果在有效时间内，继续执行后续恶意功能。

![图片](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRgQibhWHkWjIYkTQAVDIMvuaiafmibbdZz4ctDklDAUDy0M8mY0bEktNuRwwXicG0RS5YcJ0sZibNSfex0BqcjXsO4zuQWMre17yaf4/640?wx_fmt=png&from=appmsg#imgIndex=11)

图11 超期提示框

按照各字段解析配置信息，如下图所示：

![图片](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRjt2rn9ktYuhrfFGIYwZFKUWCAdb1iaYNiadF0snXJ5r8Rc8k0Rm1icY4LAhbJhibdpBsHFX4yTTndHhvayeNTlLibh2WOMgwRBeBfc/640?wx_fmt=png&from=appmsg#imgIndex=12)

图12 解析配置各字段

如果当前进程文件路径不包含“%public%\NVTELEMETRY”，在“%public%”下创建名为“NVTELEMETRY”的文件夹，在该文件夹中创建一个“【32个随机数字】.【3个随机字母】”命名的子文件夹，将“AMD.0903002123.EXE”复制为该子文件夹下的“NvTelemetryBridge64.exe”，将“xwEB\_eLF.dLl”复制为“xwEB\_eLF.dLL”，如下图所示：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRjkVmX36u8HddLRjMfD5vkYT8kp3ib03HZqozqmr5ib6seY5Yn...