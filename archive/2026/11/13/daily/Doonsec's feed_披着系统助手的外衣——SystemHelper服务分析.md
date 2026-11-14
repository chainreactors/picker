---
title: 披着系统助手的外衣——SystemHelper服务分析
url: https://mp.weixin.qq.com/s/cFiIBB7wPEDT6jgA2k90nA
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:19:46.254709
---

# 披着系统助手的外衣——SystemHelper服务分析

# 披着系统助手的外衣——SystemHelper服务分析

原创

吾爱pojie
吾爱pojie

吾爱破解论坛

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

作者**论****坛账号：windofsummer**

### 一、概述

近日在各大论坛帖子看到大量用户讨论，称 `com.mobiletools.systemhelper` 的系统组件会秘密上报多种敏感信息。我从Redmi K60 Ultra 提取出安装包，它在桌面上没有图标，唯一的界面 `TestActivity` 还挂着 signature 级权限，普通用户从安装到卸载都无法感知它的存在。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwfmjhxbib2PIHdsPj7GeiaUt4kE9t3C454xKENx6UHthzWtialmBHn0qtH8xpia8RZLpoDVgH07mu4lsJ5HeujoqS3M89ic2ZZDZYkA/640?wx_fmt=png&from=appmsg)

经分析，该组件随 ROM 预装且持平台签名，通过 `sharedUserId="com.mobiletools.systemhelper.uid"` 与同签名的配套工具共享数据目录，开机后常驻运行，按多个周期采集设备身份、双卡信息、基站参数、精确位置、应用使用画像等数据，加密后回传至联通设备管理平台 `dm.wo.com.cn`

该组件申请了 `READ_PRIVILEGED_PHONE_STATE`、`READ_PRECISE_PHONE_STATE`、`PACKAGE_USAGE_STATS`、`QUERY_ALL_PACKAGES`、`SCHEDULE_EXACT_ALARM` 等普通应用无法获得的权限，并内嵌百度定位 SDK，且在 Manifest 中硬编码 API\_KEY）。用户许可判断依赖系统设置 `device_provisioned`，也就是开机向导是否完成，相当于用户完成新机设置即默认授权，没有征求同意或关闭的界面。

二、执行链条（AI 总结）

```
 复制代码 隐藏代码
BOOT_COMPLETED (priority=2147483647)
 ├─ 排 4 分钟后无 action 自发广播
 └─ 排 4 条精确闹钟: 定位采集(1h) / 信号上报(12h) / 周期注册(24h) / 应用画像(24h)
        │ 首次延迟各叠一层 0~24h 随机错峰
4 分钟后
 ├─ 动态注册 SIM / 网络变化监听
 └─ 首次开机上报 RegType=F（之后每次开机为 B）
        │
所有上报汇聚 e1.b.a(ctx, RegType) → f1.p.d()
 ├─ 厂商 Reader 采集: 双卡 IMEI/ICCID/IMSI/MNC、基站 CID/TAC/PCI、
 │   eSIM、WiFi BSSID、蓝牙配对 MAC、内存、IPv6
 ├─ RegType=A 时追加: 应用使用时长/启动次数/每应用流量明细
 ├─ 排序: IMEI1>IMEI2 时双卡字段整体对调
 ├─ 脱敏: 非联通号段(46001/06/09/10)才打码 ICCID/IMSI、CID/TAC 做 SHA-256
 ├─ RegType=R 时从 signalhelper.db 取出 SigInfo[] 并清表
 ├─ 判定: 用户许可 && 中国网络 && 已联网 && (WiFi+中国网 || 非漫游+联通网)
 │    ├─ 通过 → SHA-256(json) 派生密钥 → RSA 信封 → AES-GCM 密文
 │    │         POST https://dm.wo.com.cn:18081/register
 │    │         成功后补发历史缓存
 │    └─ 不通过 → 明文 JSON 存 systemhelper.db（≤10 条）等待补发
 │
HTTPS 证书校验失败(SSLException) → 回退明文 http://dm.wo.com.cn:18080/register

独立链: GetSignalInfoReceiver(1h)
 └─ 百度定位(bd09ll, 高精度, 60s 超时) → 逐卡采信号
     → 仅 MNC 以 460 开头才写入 signalhelper.db（≤100 条）
```

### 三、样本哈希和下载地址

该样本已经上传至云盘，其哈希如下

```
 复制代码 隐藏代码
Name:SystemHelper_4.0.0-20260910.apk
Type:.apk
Size:3.7MB
Bytes:3884625
Modified:2026-11-07 09:27:58
Attributes:A
Copies:1
CRC32:f665678a
CRC64:749158cd5a42aa59
MD5:11ee024eb1a9fe68a9c403a23c882fd0
RIPEMD160:f3664271d452b58f9023ca389ad812ce0184c462
SHA1:633cb8e5723e2ec81970729a77c05df8a7e18a6d
BLAKE2S:c0d2359c2922a55a099a12a623186ccde6333cc4a630d6702a4d7dfb9fcfde97
SHA256:42fbfebedd8711b2ca22d3d969324f7ed7c757d838e143bf6cf4d2e8e1ed8556
SHA3_256:8eb67f24a4081790ba8be51218ba9ab4612cc83abce7e616295d4a2cd2cc5f74
```

蓝奏云盘（密码:1234）：http://wwbtl.zizi2.com/ijzet4f34hdc

123云盘：https://1839112232.share.123pan.cn/123pan/sASPTd-VQpMh

---

此外，还提取了小米自带的系统安全组件，网传所说的录屏在此apk中，其哈希如下：

```
 复制代码 隐藏代码
Name:系统安全组件_3.1.9-20261023.0.apk
Type:.apk
Size:13.8MB
Bytes:14519458
Modified:2026-11-07 09:27:16
Attributes:A
Copies:1
CRC32:5b994c8f
CRC64:aa81b824d6a517d2
MD5:fbb760a60b7ca8de490dfe7d60fbb0d2
RIPEMD160:10d1e6d7652f5364b616dc7cbb53f0840cd8aa0d
SHA1:54417be2d784e8289ef28f4bae0a3b93b2604d01
BLAKE2S:ae9a200b736b86ccc21d626abcf7c04a0d84fa7ede5c3b79c3ec93f5cc56fafa
SHA256:d82549f1580d591a6d07e46ace15e7c93f34a5000f7f528bd96d20374efa18f5
SHA3_256:b6ac76a61581ad9216edd998e4c49d191d1c95b78071bac1b4445577014113c1
```

蓝奏云盘（密码1234）：http://wwbtl.zizi2.com/ioasV4f3548f

123云盘：https://1839112232.share.123pan.cn/123pan/sASPTd-jJQMh

### 四、样本分析

将 SystemHelper\_4.0.0-20260910.apk 拖入JADX反编译，并导出反编译后的代码和资源文件。该程序没有加壳，所有的变量名和类名在编译时都被混淆，但好在代码完整可读。

首先读取`AndroidManifest.xml`查询其申请的所有权限，可以发现其申请了明显超出其服务范围内的敏感权限，包括但不限于：精确定位信息；Wifi连接信息；读取所有已安装应用；读取所有的应用使用时长统计；读取设备标识（IMEI）、通话状态、SIM信息等

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbweN708xviaSHEbNTNhulYQuUpEoHtTI4Ousib0AVPHVWfHmph0BZJjqepPdib2mquj14OhoyTetDcf1ZGwVJicGVaERl4vTibMMWbyk/640?wx_fmt=png&from=appmsg)

继续分析`AndroidManifest.xml`，其在 `Manifest` 的 `Application` 中的 `meta-data` 字段直接硬编码了百度地图的API Key，为`IGY6EFGRsixbYqk7GeZdAOD2Od3Rj7iF`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwfyO04Gqac1icgIZqsgny6rLvKXsqlnpxDliaWVOZmwmkJtNQE0t0JG9Frg5zaV2UB2ZSiaZNQNqNYDGSZxJUu669uEvoO8SBamzY/640?wx_fmt=png&from=appmsg)

组件解包后源码共 550 个 Java 文件，自有业务代码集中在 `com/mobiletools/systemhelper`（13 个文件）、`f1`（设备读取）、`e1`（采集上报线程）、`g1`（工具与存储）四个包，业务类名全部混淆为单字母。

#### 1. 开机调度

`OnBootReceiver` 在清单里的 intent-filter priority 是 `2147483647`，意味着它抢在几乎所有组件之前收到开机广播。

它收到开机广播时为了避开开机时的资源竞争，防止被用户发现。它延迟4分钟后再开始动手，具体行为是先不开始采集，只排闹钟，真正干活的是 4 分钟后那条**没有设置 action** 的自发广播。其中定位采集默认1h一次，为了防止固定时间上报被用户发现，它采用随机时间+固定时间机制。信号上报、周期注册、应用画像为随机时间+12或24小时

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwcv3LWwK0937rLO8oSCt41jg535BNLJeicicicGzuJ0kP7mogulUuhjmsOFr9J59AH0lkLogBMutWMINpJAptzIjqdOmFicKtYQr68/640?wx_fmt=png&from=appmsg)

五条闹钟全部是 `setExactAndAllowWhileIdle`，配合 `SCHEDULE_EXACT_ALARM` 权限，Doze 模式下照样精确唤醒。三类周期任务的首次延迟来自类加载时就生成好的三个随机值，随机量只在第一次排程时叠加，之后固定按 12/24 小时循环。设备量上来之后，这个设计能让上报请求摊开在全天，不出现整点流量尖峰。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwfsKSZVsWOT0icwN9TKyPuqaRRCUtDibBo8ibbnH3sIrmXLyougtxiaaiaKvc0JWtxkcsEaseh1lZADsjiaruX88JJhKHd9H5Tr63QLo/640?wx_fmt=png&from=appmsg)

代码里还留着一句直白的日志`"测试助手修改后的rand ： "`，直接印证了周期的用途。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwfYUdX43ZT1iczc4ibXu0ibv5FWe6neZdZqib183eOibS8OvUER6OQqTeDs8VNbmM8gjAENKpt5hnfzIHqpFjVlE8QDM96rE5JSjLAE/640?wx_fmt=png&from=appmsg)

#### 2. 自续期循环

三个周期 Receiver 的 `onReceive` 是同一个模子，以 `AppInfoRegisterReceiver` 为例，每触发一次就自己续一次，无限循环。全程没有前台 Service、没有通知，用户找不到任何停止入口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwcYibpXZObOBkmkfKyp1JibWA3q3cGHJCvS2UreXNHX6Cg5LMIoOJvUuYmgiaxdzoOaDjiafIxIs9egZqO663mmUYg8BzGXGSZXPY4/640?wx_fmt=png&from=appmsg)

#### 3. 采集总控

所有上报汇入 `e1.b.a()`，它只做两件事：把 Context 存进全局 `g1.d.f2648d`（后面反射全靠它），然后交给 `f1.p.d()`。总控骨架：

```
 复制代码 隐藏代码
// f1.p.d(Context, RegType)
e1.b bVar = new e1.b();
bVar.W = str;                       // 记录 RegType: F/B/S/A/R/T
k(context, bVar);                   // ① 采集（选厂商 Reader 并填充）
if (!str.trim().equals("T")) {
    i(context, bVar);               // ② 比对 ICCID1 是否变化
    j(context, bVar);               //    比对 ICCID2
} elseif (!i(context, bVar) && !j(context, bVar)) {
    return bVar;                    // SIM 没变，不上报
}
l(bVar);                            // ③ 排序 + 脱敏
// ④ 按 RegType 分流
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwdYm798M2GweuvWialaxwicbXnoZN0piaxBoiccwSXzbvAZ158fopXB2BuLqDXyOoDsHvectX1aYKvmcGlnt3r70S9eGfvfR9VNRf4/640?wx_fmt=png&from=appmsg)

#### 4. 厂商适配

组件针对 15 个厂商做了适配，`p.f()` 读 `ro.product.manufacturer` 建立映射，`p.e()` 按厂商 new 出 14 个 `f1.a` 子类之一。各子类的差异化集中在版本号读取和许可判断上（AI总结）：

| 子类 | 厂商 | 差异点 |
| --- | --- | --- |
| `f1.n` | 小米 | IMEI 走 `miui.telephony.TelephonyManager.getImeiForSlot` 反射；SWVersion 拼 `ro.mi.os.version.incremental` + `persist.sys.xms.version`；HWVersion 按型号取 `ro.miui.cust_hardware` 或 `ro.build.hardware.version` |
| `f1.l` | vivo | 唯一读 `operator_service_improve_plan` 的子类；HWVersion 取 `ro.vivo.hardware_version`；SWVersion 按 `ro.vivo.op.entry` 是否含 UNICOM 选不同产品版本属性 |
| `f1.i` | 三星 | 版本号取 `ril.sw_ver` / `ril.hw_ver` |
| `f1.e` / `f1.f` | OPPO / OnePlus | HWVersion 取 `ro.build.hardware.version`，重写许可判断 |
| `f1.m` | WIKO | 读 `Settings.System.switch_dual_card_slots` 决定 IMEI 归属哪个卡槽 |
| `f1.g` / `f1.k` | PTAC / 天翼 | SWVersion 剥离 `ro.config.product_version_pre` 前缀，拼 `ro.huawei.build.display.id` |
| `f1.c` | 摩托罗拉 | 硬编码 `HWVersion="H-2-01"`，SWVersion 取 `ro.product.carrier_revision` |
| `f1.b` /`d`/`h`/`j`/`o` | 联通品牌/nubia/realme/TDTECH/ZTE | 仅替换版本号来源（`ro.build.display.id`、`ro.product.hardware` 等） |

![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbwfujV2MnCicr01X42OkjzO1IicV35fHkLt7fjRS68KVTV4ia6Asibhhua76IoKGC4O60mhFdAtNIU2vlHmW7y3FKUfU5IUSoA8ib9Jg/640?wx_fmt=png&from=appmsg)

子类主干流程不变，只重写 b() 填充入口和 v() 许可判断。

#### 5. 许可开关

基类 f1.a.b() 填充数据前先算该全局开关，device\_provisioned`就是“开机向导是否完成”。也就是说对绝大多数机型，用户把新手机设置走完，采集就算获得授权了，没有任何征求同意的环节。`

`vivo 分支的`operator\_service\_improve\_plan`即运营商服务改进计划是全部 14 个厂商里唯一接近显式同意的判断。它检测vivo是否许可通过，不通过时只填 Model、OS 版本、内存画像就返回；通过时才继续 WiFi、蓝牙、双卡。

![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbwdnEl4gox8DMyhyHzEKg9N9ohue6GxscyLhIW2RDwx1NykpgjWc9FCly1iaSQlXbIMT7nTeRa4rDQoVO0xlQRUvVR05LZtQ0Vl4/640?wx_fmt=png&from=appmsg)

```
...