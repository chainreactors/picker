---
title: 新型Keenadu安卓固件级后门揭开跨僵尸网络协同攻击链条
url: https://mp.weixin.qq.com/s/PMSRWccFOMEZ__pwbQwG5A
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:18:18.038385
---

# 新型Keenadu安卓固件级后门揭开跨僵尸网络协同攻击链条

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDoaWEZQKNnwzQqd2OGz8UFWpzgpXwXsibKsc6JeicfB9ORFmzB3Tpr0yias0XqEWcq8ugnfpXW3FAqFIDziaxRrETx9jX0NoD0dNO8/0?wx_fmt=jpeg)

# 新型Keenadu安卓固件级后门揭开跨僵尸网络协同攻击链条

白帽子

![]()

在小说阅读器中沉浸阅读

以下文章来源于黑鸟
，作者祝大家马上大吉的

![](http://wx.qlogo.cn/mmhead/X4XEGYefSBSxrDYncLtKiacf7vZpHQnuLDMVc1rQjZsw9xYSM6kSCezibImssYuBjTibclnyop737M/0)

**黑鸟**
.

一介草民，深耕威胁情报领域多年，自封威胁分析师，APT狩猎者，战略忽悠分析师。 专注推送一切前沿高科技/人工智能、网络安全分析、敌我战略分析、数据挖掘、情报扩线、网络武器分析、社会工程学、一切开源情报、军事分析忽悠等。

卡巴在本月完整披露了新型安卓固件级后门**Keenadu**的技术细节、攻击链路、传播方式与危害，同时证实了该后门与 Triada、BADBOX、Vo1d 三大主流安卓僵尸网络之间的深度关联，黑鸟总结的特点如下：

首先，需要明确的是 Keenadu是固件级后门，攻击发生在设备出厂前的固件生产环节，而非终端用户使用阶段，也是其能突破安卓核心安全机制的根本原因。

1. **攻击入侵环节**

   攻击者入侵了安卓设备厂商的固件供应链，在**固件源码编译阶段**，就将恶意静态库`libVndxUtils.a`植入到固件源码仓库中，存放路径为`vendor/mediatek/proprietary/external/libutils/arm[64]/`，并伪装成联发科官方的`vndx`专有组件（实际联发科产品中无此组件），以此规避开发人员的审计。
2. **技术植入细节**

   固件编译时，恶意静态库会与安卓核心系统库`libandroid_runtime.so`完成**静态链接**，同时篡改该库中安卓系统日志的核心原生方法`println_native`（对应`android.util.Log`类，所有安卓应用写系统日志都会调用该方法），在其实现逻辑中插入恶意函数`__log_check_tag_count`的调用。只要安卓系统运行、应用产生日志，该恶意函数就会被触发，实现开机自启、全生命周期运行。
3. **载荷激活与持久化**

   恶意函数被调用后，会通过 RC4 算法解密库体中内置的加密载荷，将其写入`/data/dalvik-cache/`目录，伪装成系统 jar 包规避检测，再通过`DexClassLoader`完成载荷加载。最终通过挂钩安卓所有应用的父进程**Zygote**，实现：设备上每一个应用启动时，都会被注入后门的 AKClient 客户端，彻底击穿安卓应用沙箱防护。
4. **签名绕过与 OTA 下发**

   由于恶意代码是在固件编译阶段植入，最终生成的固件镜像会携带设备厂商的**有效数字签名**，可通过安卓系统的签名校验，甚至能通过厂商的**官方 OTA 系统更新**直接下发给终端用户。典型案例为某系列平板，其 2023 年 8 月及之后的所有固件版本（包括厂商发布安全声明后的版本、Widevine L1 认证的型号固件）均被感染，并通过 OTA 推送给用户。

##

除了核心的固件供应链植入，Keenadu 及其恶意模块还通过 4 种方式实现更广泛的植入，即使设备固件本身干净，也可能被感染：

1. **系统应用预植入**

   攻击者将 Keenadu 加载器直接嵌入固件中的系统级应用（无法通过常规方式卸载），在应用的核心生命周期方法中植入触发逻辑。

   典型植入目标是人脸识别服务、系统桌面启动器、系统壁纸应用、OTA 更新组件、数字健康应用等；

   触发方式为在服务 / 应用的`onCreate`方法中注册广播接收器，监听屏幕亮灭、充电启动、网络连接等系统事件，自动调用初始化方法启动恶意加载器；

   特点是，无需篡改核心系统库，即可实现系统级权限的恶意行为，常规卸载手段无效。
2. **其他后门 / 僵尸网络的加载植入**

   利用已攻陷设备的其他固件级后门，直接部署 Keenadu 加载器，实现跨僵尸网络的协同扩散。

   BADBOX 后门（同为安卓固件级后门）已控制设备的`system_server`进程并拿到最高系统权限，其定义的 Binder 接口与 Keenadu 加载器完全适配，可直接在被攻陷设备上部署 Keenadu 的全量模块，无需重复进行固件级入侵；从而实现攻击能力复用，让已被其他僵尸网络控制的设备，成为 Keenadu 的新感染目标。
3. **热门应用篡改植入**

   攻击者篡改主流热门应用的安装包，嵌入 Keenadu 的 Nova（Phantom）点击器等恶意模块，通过非官方应用渠道、第三方应用仓库、论坛等渠道分发。用户下载安装篡改后的应用后，无需 root 权限、无需系统级修改，即可激活恶意模块，实现广告欺诈、隐私窃取等行为，是针对普通用户的轻量化植入方式。
4. **官方应用商店投毒植入**

   将嵌入了 Keenadu 恶意模块的应用，绕过安全检测后上传至 Google Play等官方应用商店，实现大规模合规化分发。

   Google Play 上多款智能相机类应用，嵌入了用于启动 Nova 点击器的恶意服务，累计下载量超 30 万次；

   ![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDok6rYynWpCVfk6iblaobZpZsToiag7RLhIHL9QyG3wPtic1saPAbaDQ2nibDPGkhAd3IUTKQK4ciaxdSEn9ic3Ddlhpv9af8vCmF8OI/640?wx_fmt=png&from=appmsg)

恶意代码采用**条件触发机制**，仅在特定包名、特定网络环境、特定地区的设备上才会激活恶意行为，常规静态扫描、沙箱检测难以识别。

下面是该后门的简单描述，关于技术细节、攻击链路、传播与处置。

## 一、核心感染原理

##

攻击者通过供应链攻击，在固件编译阶段将恶意静态库`libVndxUtils.a`与安卓核心系统库`libandroid_runtime.so`完成链接，通过篡改系统日志核心方法`println_native`插入恶意函数调用，实现恶意代码植入。该后门会挂钩安卓所有应用的父进程 Zygote，设备上每一个应用启动时，都会被注入后门副本，实现全应用的代码注入，彻底击穿安卓应用沙箱防护机制。

额外关键细节：

1. 该后门内置地域规避机制，若检测到设备系统语言为中文、且处于中国时区，会直接终止执行；若设备未安装 Google Play 商店及 Google Play 服务，也会保持静默不激活；
2. 入侵环节发生在固件编译阶段，而非单纯的 OTA 服务器被黑，被感染固件携带厂商有效数字签名，可通过官方 OTA 更新直接下发给终端用户，多个品牌平板的多款固件均被证实存在该问题，甚至含 Widevine L1 认证的设备固件也未能幸免；
3. 恶意代码通过 RC4 算法解密核心载荷，伪装成联发科官方`vndx`组件规避检测，在系统中无明显恶意特征。

完整感染链路图如下：

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoSnjMChMKvj7xK6SSSC2K9hd9YfQMibnvkLllicyVlDJhrRW5R4d57sL81l1Zt4ia5485g9VXrkXUf1MhBmcrmMibSZnQyzVfjLoI/640?wx_fmt=png&from=appmsg)

整体流程如下：

固件编译阶段植入恶意代码到libandroid\_runtime.so

设备启动，Zygote进程加载被感染的系统库，后门随系统启动激活

system\_server进程中启动AKServer恶意服务，建立C2通信、获取核心权限

Zygote fork创建所有应用进程时，同步注入AKClient客户端

AKClient与AKServer通过Binder完成通信，按C2指令向目标应用加载定制化恶意载荷

最终执行：广告欺诈/搜索引擎劫持/安装量作弊/隐私窃取/账号盗号等恶意行为

**全链路攻击分支补充**：

1. 主链路：

   固件供应链感染 → libandroid\_runtime.so → BADBOX/AKServer/AKClient → 全应用注入 → 恶意模块执行
2. 旁路链路 1：

   系统应用预植入（人脸识别服务 / 桌面启动器 / 壁纸应用等） → Keenadu 加载器启动 → 恶意载荷下载执行
3. 旁路链路 2：

   BADBOX 等已入侵后门 → 直接部署 Keenadu 加载器 → 设备二次感染
4. 旁路链路 3：

   篡改应用 / 官方商店恶意应用 → 安装后激活 Nova 等恶意模块 → 本地执行恶意行为

## 三、架构与权限能力

采用客户端 - 服务端（AKClient/AKServer）核心架构，深度复刻安卓系统原生 Binder IPC 通信机制，实现高隐匿、高权限的恶意控制，核心能力如下：

1. **AKServer 服务端**

   运行在系统最高权限的`system_server`进程，本质是一个恶意系统服务，是后门的核心控制中枢。可实现：任意应用权限的静默授予 / 撤销、设备实时地理位置窃取、全量设备信息（IMEI/MAC/ 型号 / 系统版本等）外发、C2 服务器通信与载荷管理、全设备 DEX 文件注入与代码执行；内置 AES-128 CFB 加密通信机制，同时设置 2.5 个月的休眠规避期，对抗安全厂商的样本分析与检测。
2. **AKClient 客户端**

   被注入设备上所有启动的应用进程，通过受保护广播`com.action.SystemOptimizeService`获取服务端通信接口，借助 Binder 向 AKServer 发送交互事务，可根据目标应用的包名、进程名，加载定制化的恶意 DEX 载荷，让攻击者可针对不同应用实现精准的恶意行为控制，最终获得设备的完全远程控制权。

该架构彻底突破了安卓两大核心安全原则：一是让应用沙箱完全失效，后门可访问所有应用的隐私数据；二是突破安卓权限管控体系，可无视系统规则为任意应用分配敏感权限。

## 后门架构图：

```
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqnlu7Dua9HnDt3JtSkTGV0zstf9ianwR0fqLIHFg0HicDwibluPlPUCssoyqiaZfKPfX1MdFMjaI8F4FQyicicW8U4GjicFnaUWrsp30/640?wx_fmt=png&from=appmsg)
```

## 五、恶意功能模块

Keenadu 采用模块化设计，可根据 C2 指令动态下载、加载、卸载不同恶意模块，核心模块及恶意行为如下：

1. **Keenadu 加载器**

   核心基础模块，目标为亚马逊、SHEIN、Temu 等主流电商应用，可收集设备全量元数据与应用信息，静默下载执行其他恶意模块、安装未知 APK，已被证实可在用户不知情的情况下向电商购物车自动添加商品，通过推荐码实现欺诈变现。
2. **点击器加载器**

   注入壁纸、YouTube、Facebook、数字健康、系统桌面等应用，通过 GeoIP 获取设备精准位置与 IP 信息，动态下载广告点击类载荷，针对游戏、食谱、新闻等网站的广告元素实现静默交互点击。
3. **Google Chrome 模块**

   定向攻击 Chrome 浏览器，可监控用户地址栏的所有输入内容，窃取搜索关键词，同时实现搜索引擎劫持 —— 无论用户手动输入搜索词，还是选择自动补全建议，都会被重定向到攻击者指定的搜索引擎，实现流量劫持与广告变现。
4. **Nova（Phantom）广告点击器**

   核心欺诈模块，采用机器学习 + WebRTC 技术实现自动化广告点击，可伪装成用户正常交互规避检测；同时可作为加载器，下载间谍模块、Gegu SDK 多阶段点击器，实现更复杂的恶意行为。
5. **安装变现模块**

   嵌入系统桌面启动器，监控设备上所有应用安装会话，通过伪造广告点击流量、注入推广跟踪链接，欺骗广告平台，让平台认为应用安装来自合法的广告点击，实现应用安装量作弊与变现。
6. **Google Play 模块**

   定向获取谷歌广告 ID，将其作为受害设备的唯一标识存储，供其他所有恶意模块调用，支撑广告欺诈、设备追踪、用户画像构建等行为。

所有模块均采用 DSA 签名校验 + AES 加密机制，仅攻击者持有私钥可生成有效载荷，同时支持远程静默卸载，规避安全检测与溯源。

## 六、多渠道传播

除核心的固件供应链攻击外，该后门及相关模块已形成多维度、全场景的传播体系，具体如下：

1. **系统应用预植入**

   将 Keenadu 加载器直接嵌入固件中的系统应用，包括人脸识别服务、桌面启动器、系统壁纸应用、OTA 更新组件、数字健康应用等，其中人脸识别服务为首次发现的植入目标，可随系统启动直接激活，无法通过常规方式卸载。
2. **其他后门加载分发**

   BADBOX 等已实现系统级入侵的后门，可直接在被攻陷设备上部署 Keenadu 加载器，利用已获取的 system\_server 权限完成二次感染，实现僵尸网络之间的协同扩散。
3. **热门应用篡改**

   通过篡改主流热门应用，在非官方应用渠道、第三方应用仓库分发，植入 Nova 等恶意模块，用户安装篡改应用后即被感染。
4. **官方应用商店投放**

   恶意模块已成功渗透 Google Play、小米 GetApps 等官方应用商店，其中 Google Play 上多款带恶意代码的智能相机应用，累计下载量已超 30 万次；恶意代码采用条件触发机制，仅在特定包名、特定环境下激活，规避应用商店的安全检测。

## 七、僵尸网络关联

本次报告首次完整梳理了四大主流安卓僵尸网络的关联关系，证实了其背后的协同攻击链路，形成了覆盖安卓全生态的攻击矩阵：

1. **Keenadu 与 BADBOX 的直接关联**

   二者在载荷代码、核心架构上存在高度相似性，BADBOX 可直接下载、分发 Keenadu 加载器，Keenadu 开发者大概率参考了 BADBOX 的源代码，二者为独立但深度协作的僵尸网络，其中 Keenadu 主要以安卓平板为核心攻击目标。
2. **四大僵尸网络的关联闭环**

* Triada 与 Vo1d：共享 C2 服务器域名，存在明确的基础设施关联；
* Triada 与 BADBOX：曾联合发起恶意 WhatsApp 修改版攻击，从同一入口点启动两款木马，实现联合入侵；
* BADBOX 与 Vo1d：已被行业研究证实存在代码与基础设施的深度关联；
* BADBOX 与 Keenadu：存在直接的载荷分发与代码同源性，是本次报告的核心新发现。

3. 攻击能力互补：四大僵尸网络形成了从固件级预植入、系统应用篡改、普通应用投毒的全链条攻击覆盖，可实现安卓设备从出厂到用户使用全生命周期的入侵，是目前安卓生态中规模最大、技术能力最强的恶意软件联盟。

   ![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrNean4GDWoI63RHJxfOyEYnCShKoNib1WEL1Ov1u4rWPtnEO5ZyKa8uZiav7ibJvuvdMsgZmmRtkVIb6SFCE18HFicPopLIicYwhdo/640?wx_fmt=png&from=appmsg)

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqEMic4t9IBwRnNFhTjq8r8D8N8ccbl8eHVtlWaU4fTPBrFxAbVfgfXnO5iam1sS6sLwGKATjkSpemABKibypdbn2rUQbkPfKOYKU/640?wx_fmt=png&from=appmsg)

其中关于BADBOX的八卦信息，可以自行搜索上个月外网的某篇文章，在此不进行复述。

## 八、受害与处置

根据卡巴斯基遥测数据，全球累计 13715 名用户遭遇 Keenadu 或其相关模块的攻击，受攻击用户数量最多的国家 / 地区依次为：俄罗斯、日本、德国、巴西、荷兰，受感染设备以安卓平板为主。

### 分场景处置建议

1. **若 libandroid\_runtime.so 系统库被感染**

   优先检查厂商官方固件更新，确认是否已发布干净的固件版本，更新后通过安全软件验证威胁是否清除；

   若无官方干净固件，可尝试手动刷入第三方纯净固件，需注意手动刷机存在设备变砖的风险；

   固件修复完成前，建议停止使用该被感染设备，避免隐私泄露与财产损失。
2. **若系统应用被感染**

   为被感染应用寻找可替代的干净应用，例如桌面启动器、壁纸应用等，同时尽可能停用被感染的系统功能（如被入侵的人脸识别服务）；

   通过 ADB 工具执行命令

`adb shell pm disable --user 0 应用包名`，禁用被感染的系统应用，阻止其恶意行为。

3. 若普通应用被感染，直接通过系统设置或安全软件，卸载被感染的应用即可完成威胁清除。

原文完整技术披露链接：

https://securelist.com/keenadu-android-backdoor/118913/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

白帽子

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/...