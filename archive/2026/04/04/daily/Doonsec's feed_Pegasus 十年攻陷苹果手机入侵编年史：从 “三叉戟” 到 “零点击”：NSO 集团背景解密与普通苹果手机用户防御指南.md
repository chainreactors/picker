---
title: Pegasus 十年攻陷苹果手机入侵编年史：从 “三叉戟” 到 “零点击”：NSO 集团背景解密与普通苹果手机用户防御指南
url: https://mp.weixin.qq.com/s/YHiwJ4YRa2GUi6CA_s1p6w
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:37:15.341660
---

# Pegasus 十年攻陷苹果手机入侵编年史：从 “三叉戟” 到 “零点击”：NSO 集团背景解密与普通苹果手机用户防御指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zdwoicOrrJb0WFxoOr9dJ174hX3omtwpSP3IQfMicHNes5Wkl9l2YFCDRjKIrSzzuEIAiasm0ZUZHw45DDRX5m3g2IN7skm3SwKYxqdvHprtj8/0?wx_fmt=jpeg)

# Pegasus 十年攻陷苹果手机入侵编年史：从 “三叉戟” 到 “零点击”：NSO 集团背景解密与普通苹果手机用户防御指南

ZM
ZM

暗镜

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/zdwoicOrrJb0qyibHgpUZ1m1a5N60F6oJ1Bq5nL0vWgicjicpWvm6nB3NBLvQhv6xkCjmMvmZ9GZ7cicHCKKqbz3ku720JKVrf2JIYtGMwz5qBVU/640?wx_fmt=jpeg)

2026 年 4 月 2 日，一则网络犯罪论坛售卖帖引发全球苹果手机用户震动：威胁行为者 “xone9to1” 公开兜售代号Pegasus的零点击远程访问木马（RAT），宣称无需安装 APK/IPA 文件即可运行，完美兼容 iPhone 17（iOS 26.2）与安卓 5 至 16 系统，集实时监控、数据窃取、银行盗币、僵尸网络 DDoS 于一体。该软件针苹果iOS系统。威胁行为者称：其功能包括收集设备信息、网络和SIM卡详情、实时GPS定位及历史记录。高级功能包括设备控制（锁定、关机、铃声、亮度调节）、带DDoS攻击功能的僵尸网络控制、带加密功能的文件管理器、实时监控（前后摄像头、屏幕录制、麦克风访问）、键盘记录器，以及针对MetaMask、Trust、Binance、UPI、Apple Pay、Google Pay和PayPal等支付平台的银行/加密货币窃取模块。演示视频作为概念验证，这次事件也让这款统治移动攻防领域十年的 “武器级” 间谍软件再次站到聚光灯下。

从 2016 年击穿 iOS 安全防线，到 2026 年被暗网售卖，Pegasus 凭借持续迭代的零日漏洞与零点击攻击技术，成为针对 iPhone 最致命的威胁。本文将深度解密NSO Group公司背景、Pegasus 十年 iOS 攻击演进史、核心攻击技术，并整合完整防御方案，全面拆解这场移动安全领域的顶级攻防对抗。

# 一、Pegasus 幕后：以色列NSO Group 公司全解析

## 1. 公司基本概况

NSO Group Technologies（简称 NSO 集团）是全球最知名的网络情报与间谍软件开发商，NSO取自三位创始人名字首字母 ——Niv Karmi、Omri Lavie、Shalev Hulio。公司 2010 年正式成立，总部位于以色列赫兹利亚（Herzliya），全球雇员超 750 人，核心技术团队几乎全部是以色列前军事情报人员，多数曾服役于以色列军事情报总局 8200 部队（以军顶级网络战单位）。

作为以色列网络安全产业的标杆企业，NSO 集团长期以政府机构为唯一客户，核心业务是开发、销售高端监控技术，其产品被以色列官方列为 \*\*“武器级” 技术 \*\*，出口必须经以色列国防部严格审批。公司通过全球子公司隐蔽运营：在卢森堡使用 OSY Technologies，北美使用 Westbridge，欧洲通过 Q Cyber Technologies 开展业务，但随着技术泄露，其他领域的攻击事件也露出水面。

## 2. 发展历程与股权变迁

2010 年：Niv Karmi（前摩萨德成员）、Omri Lavie、Shalev Hulio 联合创立 NSO Group，获 Genesis Partners 风险投资 180 万美元（占股 30%）。

2011 年：首款 \*\*Pegasus（飞马）\*\* 间谍软件正式完成，定位高精度定向攻击工具。

2014 年：美国私募股权公司 Francisco Partners 以 1.3 亿美元收购 NSO 多数股权，公司进入快速扩张期。

2016 年：Pegasus 因攻击阿联酋人权活动人士 Ahmed Mansoor 首次曝光，全球舆论哗然。

2019 年：创始人 Shalev Hulio、Omri Lavie 联合欧洲私募股权基金 Novalpina Capital，以 10 亿美元估值从 Francisco Partners 回购 60% 股权。

2021 年：美国商务部将 NSO 列入实体清单，禁止美国企业向其供货；苹果、Meta 相继起诉 NSO，指控其利用 Pegasus 攻击 iPhone、WhatsApp 用户。

2023-2026 年：NSO 持续迭代 Pegasus，突破 iOS 15-17 系统；同时 Pegasus 技术泄露，黑产仿冒版开始在网络犯罪论坛流通。

## 3. 核心争议：从反恐工具到全球监控武器

NSO 集团始终宣称，Pegasus 仅用于打击恐怖主义与严重犯罪，客户均为合法政府机构。但过去十年，大量调查证实其被广泛滥用：

2018年，沙特政府利用 Pegasus 监控记者贾迈勒・卡舒吉，为其遇害提供情报支持。

2021年 “Pegasus 项目” 曝光：全球超 5 万人被列为监控目标，涉及墨西哥、印度、匈牙利等多国政治监控丑闻。

2026年Pegasus 流入黑产，威胁从定向高价值攻击扩散至普通用户，彻底打破 “政府专用” 的底线。

# 二、Pegasus 攻陷 iOS 十年：从点击链接到零点击无感知

正版 Pegasus 自诞生起，就将iOS 作为核心攻击目标，十年间完成四次技术跃迁，持续击穿苹果安全体系：

## 1. 2016 年：初代成名 ——“三叉戟” 漏洞，点击即沦陷

核心漏洞：Trident（三叉戟）三零日组合 ——WebKit 内存破坏漏洞、内核提权漏洞、沙箱逃逸漏洞。

攻击方式：通过短信发送恶意链接，用户点击后自动感染，无需额外授权。

影响范围：iOS 9.3.5 及以下系统，覆盖 iPhone 6/6s 全系列。

关键事件：阿联酋人权活动人士 Ahmed Mansoor 手机被植入，Citizen Lab 与 Lookout 联合曝光，苹果紧急推送 iOS 9.3.5 修复。

历史意义：首次证明 iOS 可被商业漏洞武器化攻破，Pegasus 一战成名。

## 2. 2019-2020 年：技术跃迁——WhatsApp 零点击，无需交互

核心突破：利用 WhatsApp 通话协议漏洞，拨打恶意通话即可触发代码执行，用户不接电话也会中招。

能力升级：实现无用户交互后台静默植入、静默提权，彻底绕过用户操作防御。

后续影响：Meta（原 Facebook）起诉 NSO，索赔 167 亿美元；苹果强化 iMessage、WhatsApp 等应用的系统隔离。

## 3. 2021 年：巅峰时刻——ForcedEntry 零点击，iMessage 成致命入口

核心漏洞：ForcedEntry（CoreGraphics 图像解析内存破坏漏洞）。

攻击方式：通过 iMessage 发送恶意 GIF 图片，无弹窗、无提示、无点击，系统后台自动解析触发漏洞。

覆盖范围：iOS 14.6 及更早版本，iPhone 11/12 全系列，实现完整设备接管。

曝光事件：Citizen Lab 证实巴林、沙特针对活动人士大规模攻击，苹果紧急发布补丁并推出 Lockdown 锁定模式。

时代标志：Pegasus 进入完全无感知攻击时代，用户行为无法防御。

## 4. 2022-2026 年：持续迭代—— 追打新版 iOS，黑产扩散

攻击转向：苹果封堵 iMessage 漏洞后，Pegasus 转向彩信、系统协议栈、底层服务漏洞。

系统穿透：持续突破 iOS 15-17 安全防护，2026 年仿冒版明确兼容iOS 26.2、iPhone 17。

威胁下沉：从军方情报、政府监控领域流入网络犯罪集团，集成加密货币窃取、DDoS僵尸网络等黑产功能。

# 三、核心技术解密：Pegasus 如何击穿 iOS 安全体系

iOS 凭借沙箱隔离、代码签名、ASLR地址随机化、DEP数据执行保护、内核安全构建纵深防御，但 Pegasus 通过一套完整攻击链路逐层瓦解：

## 1. 标准攻击链路：三步拿下iPhone

远程代码执行（RCE）

利用 iMessage、WebKit、图像解析、通话协议等零日漏洞，无需用户操作即可在设备上执行恶意代码；2021 年后以零点击为绝对主流，短信、彩信、iMessage 均为攻击入口。

沙箱逃逸

突破 iOS 应用隔离机制，获取访问系统目录、其他应用数据、密钥链的权限，脱离单一应用的安全限制。

内核提权

获取 iOS 最高权限（root），实现：

* 读取所有 App 数据（社交、邮件、支付、笔记）；
* 实时接管前后摄像头、麦克风、屏幕录制；
* 键盘记录、截取短信 OTP 验证码、窃取支付凭证；
* 隐藏进程、擦除日志、风险触发后自动自毁。

## 2. 2026 年版Pegasus 新增威胁

* 黑产版功能更贴合网络犯罪需求：
* 纯漏洞利用：宣称无需安装 APK/IPA 文件，完全依赖漏洞落地；
* 金融窃取强化：针对 MetaMask、Trust Wallet、Binance、Apple Pay、Google Pay、PayPal 等加密货币与支付平台定制窃取模块；
* 黑产工具集成：内置 DDoS 僵尸网络控制、加密文件管理器、远程设备控制（锁定、关机、调亮度）；
* 低门槛使用：提供演示视频 PoC，降低黑产团伙操作门槛。

# 四、苹果 vs Pegasus：十年攻防对抗复盘

| **对抗阶段** | **苹果防御动作** | **Pegasus 应对策略** |
| --- | --- | --- |
| 2016 年 | 紧急修复 Trident 漏洞，加强 WebKit 安全校验 | 转向通话、彩信等新攻击矢量 |
| 2021 年 | 封堵 ForcedEntry 漏洞，iMessage 隔离解析 | 挖掘内核、协议栈新零日漏洞 |
| 2022-2023 年 | 推出 Lockdown 锁定模式，限制 iMessage 等攻击面 | 针对性绕过 Lockdown 模式限制 |
| 2024-2026 年 | 强化内存安全、缩短漏洞响应周期、快速补丁 | 持续获取新版 iOS 零日，技术泄露致黑产仿制 |

# 五、Pegasus 级威胁防御：iPhone安全加固完整清单

## （一）、系统级必做设置（抵御零点击 / 系统漏洞）

立即升级至最新正式版 iOS

路径：设置 → 通用 → 软件更新

作用：封堵已公开 Pegasus 类漏洞（ForcedEntry、WebKit、iMessage漏洞）。

开启自动更新（关键）

设置 → 通用 → 软件更新 → 自动更新

开启：下载iOS更新、安装iOS更新、安全响应和系统文件。

高危人群开启 Lockdown 锁定模式

设置 → 隐私与安全性 → 锁定模式

适用：记者、律师、公职人员、高管、加密资产持有者

效果：大幅削弱 iMessage、链接预览、网页渲染等攻击面。

关闭不必要后台 App 刷新

设置 → 通用 → 后台 App 刷新 → 仅保留必要应用

减少恶意代码后台驻留与数据回传机会。

## （二）、iMessage / 信息安全（Pegasus核心入口）

开启未知发件人过滤

设置 → 信息 → 开启未知发件人过滤，关闭自动预览。

禁用 iMessage 链接预览

设置 → 信息 → 关闭链接预览，防止恶意 URL 自动加载。

极高风险人群可直接关闭 iMessage

设置 → 信息 → 关闭 iMessage，彻底切断经典零点击攻击通道。

## （三）、网页与链接安全（防止诱骗型攻击）

Safari 强化设置

设置 → Safari → 开启阻止跨网站跟踪、隐藏IP地址；

高级 → 敏感场景临时关闭JavaScript。

严格遵守 “三不原则”

* 不点击陌生链接、不扫码安装未知应用、不安装任何描述文件（.mobileconfig）。
* 仅从 App Store 安装应用
* 拒绝企业证书 App、TestFlight不明应用、第三方助手软件。

## （四）、权限与隐私防护（防止摄像头 / 麦克风窃取）

严控敏感权限

设置 → 隐私与安全性：相机、麦克风、定位、照片仅授予必要 App，且设为使用期间。

关闭后台定位

定位服务 → 所有非必要 App 设为永不。

## （五）、支付与加密资产安全（针对 2026 盗币模块）

钱包 App 双重加固

MetaMask、Trust Wallet 开启应用锁/面容锁，助记词离线保存。

支付 App 强验证

Apple Pay、PayPal 等开启二次验证，不自动填充 OTP 至可疑页面。

## （六）、反窃密检测与日常操作

每天至少重启一次 iPhone

多数 Pegasus 类木马无持久化，重启可清除内存驻留组件。

检查异常描述文件

设置 → 通用 → VPN 与设备管理，删除陌生描述文件。

关注耗电与流量异常

待机异常耗电、后台疯狂跑流量，可能是窃密软件回传数据。

绝不越狱

越狱直接摧毁 iOS 沙箱与内核防护，Pegasus可 100% 接管设备。

# 六、总结：间谍软件平民化下的移动安全警示

Pegasus 十年 iOS 攻击史，本质是高价值目标攻防的极致内卷：从需要用户点击，进化到零点击无感知；从境外军方情报专用，下沉到网络犯罪流通；从单一漏洞利用，到全体系安全穿透。2026 年版 Pegasus 的出现，标志着顶级间谍能力正式平民化，iOS 不再是绝对安全的 “堡垒”。

对普通用户而言，保持系统更新、开启基础防护、谨慎陌生链接，即可抵御绝大多数 Pegasus 类威胁；对记者、政要、加密资产持有者等高危人群，则需结合Lockdown 模式、物理隔离、操作规范形成完整防御体系。

这场对抗远未结束 —— 只要存在未公开的零日漏洞、足够高的攻击价值，Pegasus 及其仿制品就会持续进化。而移动安全的核心，始终是系统安全、用户习惯、防御意识的三重结合。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

暗镜

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

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