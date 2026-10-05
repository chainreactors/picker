---
title: 关于网传AcFan SystemService投毒事件的分析
url: https://mp.weixin.qq.com/s/JF97y0u-RGCYhHorbf6IqA
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:54:14.810455
---

# 关于网传AcFan SystemService投毒事件的分析

# 关于网传AcFan SystemService投毒事件的分析

原创

Thanatos
Thanatos

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026年9月下旬以来，国内多个渠道陆续出现针对安卓远控木马`SystemService`的感染反馈。百度贴吧「病毒吧」发布的《安卓病毒"SystemService"的通告与解决方案》一帖在十余小时内累积160余楼回复，另有同吧更早发布的《最新安卓SystemService病毒》帖，均指向AcFan（俗称"A站"）客户端为传播途径，并称感染集中于小米、vivo/iQOO等机型。

现有公开信息多为网传截图与转述，受害者反馈之间相互矛盾，部分材料将不同组件的特征混合描述，且除个别已公开分析的变体外，该家族其余组件样本尚未公开，缺乏可交叉验证的实物证据。本次鉴定以用户提供的5件AcFan客户端样本为对象，采用静态逆向与root环境动态取证相结合的方式，验证送检样本是否实际搭载该木马家族成分，并明确现有已获取样本在该家族中所处的环节与能力边界。

## 1.摘要

### 1.1病毒确认

**SystemService木马家族客观存在，完整样本已由第三方捕获并公开分析。详细分析报告等详见文末链接，本文不再重复分析。**

### 1.2本次送检样本结论

**送检5件AcFan样本经静态逆向与root环境动态取证，未发现任何SystemService木马家族投毒成分，亦不具备投放该木马的技术能力。**

| 样本 | 来源 | 版本 | 包名 | 判定 |
| --- | --- | --- | --- | --- |
| A.apk | 网友提供 | 1.9.7 | `com.mscjsh.djrapcrp` | 未发现投毒 |
| tg\_acfun\_1.9.7 | 官方群组 | 1.9.7 | `com.pcmtku.yeghaxpq` | 未发现投毒 |
| y8l\_acfan\_1.9.8 | 第三方渠道 | 1.9.8 | `com.cghg.dawngallery` | 未发现投毒 |
| official\_acfun\_1.9.9 | 官方下载 | 1.9.9 | `com.rrakxu.oyhmnjcm` | 未发现投毒 |
| tg\_acfan\_1.8.2 | 官方群组 | 1.8.2 | `r9ge.anvzy.j2x6.kznbp4...` | 未发现投毒 |

### 1.3三项实测结论

**结论一：5件样本均未植入木马家族组件。**全系统包名扫描命中0项，全盘文件特征串扫描命中0项。样本C私有目录虽含41项动态载荷，经逐一鉴定全部归属商业广告SDK。

![全系统RAT组件扫描](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQr1dATlQHguybq1g9VduzwHDjeEgnLDJeTv9gGx5JrB7VOFNewbSL4Dg7CsSDiaEP0e08XSHp2icRdLvsaoOtSaXjibVwatOgxPGM/640?wx_fmt=webp&from=appmsg)

全系统RAT组件扫描

*图1：送检5件样本运行后，设备上不存在任何SystemService家族组件，全盘文件检索亦无家族特征串*

**结论二：`official_acfun_1.9.9`的official标记与实际身份不符。**该样本包名为`com.rrakxu.oyhmnjcm`（12位随机串），签名主体为`Auto/Auto/Auto`占位符，与官方发布物特征不符。其文件名内嵌毫秒时间戳`1790822893371`对应**2026-10-0110:48:13**；样本C内嵌构建时间戳为**2026-09-2119:23:54**；样本B内嵌`1785227144102`对应**2026-07-2816:25:44**。三者构建时间均落在木马活跃期内，但样本本体未携带恶意载荷。

**结论三：现有已获取木马样本为高危行为执行端，非完整家族。**本次持有的`com.servers.ozzbzk`经完整逆向确认为20条远程指令、15项权限、零网络层的能力执行模块：

![BridgeProvider指令分发表](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQpmjW66hnmKZSQnQuO1fjM7zpolyKtsYn0e9gx3PRaqVSXD5Sa1mxLn8lPKlUGRRV8lzJuPiaUBSlPHG6MGIiaCVG5297rvdrLZ8/640?wx_fmt=webp&from=appmsg)

BridgeProvider指令分发表

*图2：`BridgeProvider.call()`反编译结果，UID门禁仅放行root(0)/system(1000)/shell(2000)/自身；全部59个import中无`java.net`，该模块不具备C2通信能力*

参考材料所述27条指令、46项权限、含a11y无障碍控制端的完整变体，以及`com.tikttok.a11y`、`com.umhkmqa.a11y`、`com.vivo.tws.vivotws`等家族组件，均未包含在现有已获取样本中。

---

## 2.分析环境

### 2.1沙箱配置

| 项目 | 配置 |
| --- | --- |
| 虚拟化平台 | 雷电模拟器9（LDPlayer9），设备`emulator-5554` |
| Android版本 | 14（API34，Build`UQ1A.240205.09211156`） |
| 构建类型 | `user` /`release-keys` |
| 架构 | `x86_64` ，abilist为x86\_64,arm64-v8a,x86,armeabi-v7a,armeabi |
| 构建指纹 | `Xiaomi/unicorn/unicorn:14/UQ1A.240205.09211156/ucsm.20260921.115630:user/release-keys` |
| 设备标识 | `ro.product.model=2512BPNDAC` ，`ro.product.brand=XIAOMI`，`ro.product.manufacturer=XIAOMI` |
| 运营商参数 | `gsm.operator.alpha=CHINAMOBILE` ，`gsm.operator.numeric=302780` |
| 时区 | Asia/Shanghai |
| SELinux | Permissive |
| 权限上下文 | `uid=0(root)` ，`context=u:r:su:s0` |
| 网络 | `172.16.1.4/24` ，网关`172.16.1.1` |
| DNS | `10.16.82.154` 、`119.29.29.29`、`114.114.114.114` |
| 抓包 | `/system/bin/tcpdump` ，root态正常写盘 |

### 2.2环境适配依据

参考材料载明该家族"主要感染目标：小米、vivo/iQOO系列手机"，据此对沙箱作三项适配。

**其一，启用root。**`/data/data`目录在非root环境下不可读，应用私有目录取证是判定动态注入的核心环节。启用root后`adb shell id`返回`uid=0(root)`，`/data/data/<pkg>`全树可读，`tcpdump`可正常写盘。

![root环境建立](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQq4tLJguPx7JiceCGvBXibqw1wJM0UJfg59Csgk2t0oURTRlLNQ3vFbJ6Nia1zI1DibMLbuMVndOYHxS9FYWBGa9F7tccL4BQNBepI/640?wx_fmt=webp&from=appmsg)

root环境建立

*图3：`adb root`后取得完整root上下文，机型属性已伪装为XIAOMI 2512BPNDAC*

**其二，机型伪装为小米。**写入`ro.product.model`、`ro.product.brand`、`ro.product.manufacturer`为小米对应值。

**其三，注入运营商参数。**写入`gsm.operator.alpha=CHINAMOBILE`与`gsm.operator.numeric=302780`，使设备呈现已实名入网状态。

外网连通性经逐域名验证：`www.baidu.com`、`api.github.com`、`dl.google.com`、`cdn.jsdelivr.net`、`www.sexbar.site`、`cdn.ukaim.com`均可达，动态下载行为具备可观测条件。

### 2.3静态分析工具

| 组件 | 版本 | 用途 |
| --- | --- | --- |
| androguard | 4.1.4 | AndroidManifest解析、DEX结构分析 |
| jadx | 1.5.3 | DEX→Java反编译 |
| apktool | 2.11.1 | 资源解码、smali反汇编 |
| apksigner | build-tools r34 | APK签名验证、证书提取 |
| Python | 3.11.9（venv隔离） | 自动化扫描、载荷鉴定、pcap解析 |

---

## 3.样本清单与标识

### 3.1哈希链

| ID | 文件名 | 大小(字节) | MD5 | SHA-256 |
| --- | --- | --- | --- | --- |
| A | `A.apk` | 58,831,415 | `B42E24278491CA090A7D83909B59CFD8` | `94A611055FA48172EA8DD8A61B48E0DCA163D3C31FC1BEF191C72F7E9371AEB1` |
| B | `tg_acfun_1.9.7_1785227144102.apk` | 58,924,327 | `C48E829E767E0D700AE9610F58F3AF5C` | `16ADFD094DEE81DE314751CD57DA499E96978496691F2EEF87FF0211FF37EB03` |
| C | `y8l_acfan_1.9.8.apk` | 82,432,805 | `93B8A64E2BF7C1659F7898F522041C95` | `4136D63884AB81AB3CC7B00CC6835E315A5895AA05E6A30AC28577B570121E71` |
| D | `official_acfun_1.9.9_1790822893371.apk` | 63,846,345 | `F396A4FE88E7176CE234773B4BC310A7` | `8CD2A8CF28D5345F9FAFB41FD26FDF582CC7F07F32E158B65917F20C7378C32A` |
| E | `tg_acfan_1.8.2_26292276.apk` | 34,172,963 | `0CB91CC68AA48EFF94D2683DBF7AF529` | `D23188B0AD04C7C5BC7DDCFBCE2C6FCED964EC9764FCF2DFA4E886AAB460E1F1` |

### 3.2时间戳溯源

| ID | 时间戳来源 | 解析结果 |
| --- | --- | --- |
| A | — | 文件系统时间`2026-10-0400:50:52` |
| B | 文件名内嵌`1785227144102` | **2026-07-2816:25:44** |
| C | ZIP条目构建时间 | **2026-09-2119:23:54至19:24:02** （连续8秒内完成构建） |
| D | 文件名内嵌`1790822893371` | **2026-10-0110:48:13** |
| E | 文件系统时间`2026-10-0400:50:52` | — |

**时间戳分析结论**：5件样本构建/分发时间分布于2026-07-28至2026-10-01，与SystemService木马家族活跃期（2026年5月起）高度重叠。但**时间重叠不等于投毒**——本报告§4、§5的实测数据证实，5件样本本体均未携带木马载荷。

### 3.3包身份与签名主体

| ID | versionName | packageName | 签名主体(DN) | 证书SHA-256 |
| --- | --- | --- | --- | --- |
| A | 1.9.7 | `com.mscjsh.djrapcrp` | `CN=Auto,OU=Auto,O=Auto,L=Auto,ST=Auto,C=CN` | `ecd2d7f1…bbcb` |
| B | 1.9.7 | `com.pcmtku.yeghaxpq` | `CN=Auto,OU=Auto,O=Auto,L=Auto,ST=Auto,C=CN` | `09d00e81…6bea` |
| C | 1.9.8 | `com.cghg.dawngallery` | `CN=cghg,O=（中文公司名）,L=（中文）,ST=（中文）,C=CN` | `beb1c5a7…487f` |
| D | 1.9.9 | `com.rrakxu.oyhmnjcm` | `CN=Auto,OU=Auto,O=Auto,L=Auto,ST=Auto,C=CN` | `683e2b26…c6e9` |
| E | 1.8.2(code182) | `r9ge.anvzy.j2x6.kznbp4.d1773626169979095609` | `CN=gelx0fcrbk,OU=myOrg,O=myOrg,L=myCity,ST=myState,C=CN` | `7ce4b4ff…2b01` |

### 3.4身份异常分析

**5件样本packageName均为随机生成字符串**，与AcFan官方包名无任何关联：

* 样本D文件名标注`official_`，但包名为`com.rrakxu.oyhmnjcm`（12位随机串），签名主体为`Auto/Auto/Auto`占位符——**该official标记不成立**
* 样本E包名含50位数字后缀`d1773626169979095609`，签名主体为AndroidStudio默认调试模板`myOrg/myCity/myState`——**典型自动化重打包产物**
* 样本A与B签名主体字符串相同（`CN=Auto…`）但证书指纹不同——**同一主体名使用不同密钥分别签名**

**判定：5件样本均为非官方来源的盗版重签分发包。**

---

## 4.静态分析结果

### 4.1木马家族特征扫描

**扫描方法**：对每件APK的`classes*.dex`、`AndroidManifest.xml`、`resources.arsc`、`assets/**`全部条目执行字节级关键字匹配。

**扫描目标关键字（14项）**：

```
com.servers.ozzbzk     com.system.service        com.tikttok.a11y
com.umhkmqa.a11y       com.vivo.tws.vivotws      com.oplus.exsystemservice
com.mobiletools.systemhelper                      core.dex
BridgeProvider         PhishActivity             BlackScreenActivity
CameraCaptureHelper    AudioCaptureHelper        REMOTE_SUBMIX
phish_pending
```

**扫描结果**：

| 样本 | APK条目数 | DEX条目数 | 家族特征命中 |
| --- | --- | --- | --- |
| A | 982 | 2 | **0** |
| B | 988 | 2 | **0** |
| C | 4,220 | 7 | **0** （含415个dex/apk/so文件全量扫描） |
| D | 1,016 | 2 | **0** |
| E | 2,468 | 2 | **0** |

### 4.2权限与危险能力矩阵

| 权限 | A(1.9.7) | B(1.9.7) | C(1.9.8) | D(1.9.9) | E(1.8.2) |
| --- | --- | --- | --- | --- | --- |
| `REQUEST_INSTALL_PACKAGES` | ✗ | ✗ | **✓** | ✗ | **✓** |
| `INSTALL_PACKAGES` | ✗ | ✗ | ✗ | ✗ | ✗ |
| `DELETE_PACKAGES` | ✗ | ✗ | ✗ | ✗ | ✗ |
| `BIND_ACCESSIBILITY_SERVICE` | ✗ | ✗ | ✗ | ✗ | ✗ |
| `BIND_DEVICE_ADMIN` | ✗ | ✗ | ✗ | ✗ | ✗ |
| `SYSTEM_ALERT_WINDOW` | ✗ | ✗ | ✗ | ✗ | **✓** |
| `READ_SMS` | ✗ | ✗ | ✗ | ✗ | ✗ |
| `READ_CONTACTS` | ✗ | ✗ | ✗ | ✗ | ✗ |
| `READ_CALL_LOG` | ✗ | ✗ | ✗ | ✗ | ✗ |
| `ACCESS_FINE_LOCATION` | ✗ | ✗ | **✓** | ✗ | ✗ |
| `QUERY_ALL_PACKAGES` | ✗ | ✗ | **✓** | ✗ | ✗ |
| `MANAGE_EXTERNAL_STORAGE` | ✓ | ✓ | ✗ | ✓ | ✗ |
| `RECORD_AUDIO` | ✓ | ✓ | ✗ | ✓ | ✗ |
| `CAMERA` | ✓ | ✓ | ✗ | ✓ | ✓ |
| 权限总数 | 22 | 18 | 30 | 23 | 14 |

**关键判定**：

* **5件样本均无`READ_SMS`/`READ_CONTACTS`/`READ_CALL_LOG`/`BIND_DEVICE_ADMIN`权限**——与System...