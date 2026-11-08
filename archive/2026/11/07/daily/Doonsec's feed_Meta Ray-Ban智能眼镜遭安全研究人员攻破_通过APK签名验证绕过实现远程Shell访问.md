---
title: Meta Ray-Ban智能眼镜遭安全研究人员攻破:通过APK签名验证绕过实现远程Shell访问
url: https://mp.weixin.qq.com/s/0zSs9XOGNRpCQNxhr2qzAQ
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:09:08.298874
---

# Meta Ray-Ban智能眼镜遭安全研究人员攻破:通过APK签名验证绕过实现远程Shell访问

# Meta Ray-Ban智能眼镜遭安全研究人员攻破:通过APK签名验证绕过实现远程Shell访问

tuto
tuto

杂杂咱谈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 一、事件概述

安全研究人员在对Meta Ray-Ban智能眼镜进行安全研究时，成功实现了设备上的任意代码执行，并进一步获得交互式Shell访问能力。

安全研究人员最初是为了研究2026年Pwn2Own的潜在攻击目标，尝试分析上一年度的相关设备。在对Meta Ray-Ban智能眼镜进行逆向分析后，发现其固件更新机制和Device Access Toolkit(DAT)应用安装流程存在安全问题。

整个攻击过程主要涉及：

* 逆向分析Meta AI手机应用。
* 从OTA更新服务器提取完整固件。
* 利用DAT应用安装机制替换官方APK。
* 绕过APK数字签名验证。
* 通过Wi-Fi Direct建立设备通信。
* 在眼镜上启动TCP Shell服务。

研究人员将漏洞报告给Meta，并通过漏洞赏金平台提交。根据作者披露，Meta已批准相关技术文章公开，作者认为相关问题已经得到修复。

## 二、固件提取: 从OTA更新机制入手

研究人员首先安装Meta AI手机应用，该应用负责智能眼镜的连接、照片同步以及固件更新。

为了获取眼镜固件，研究人员没有拆解设备，而是选择分析OTA更新机制。

### 1. 逆向分析 Meta AI 应用

通过JADX反编译Meta AI APK，研究人员定位到负责处理固件更新的类：

* `OtaArtifactFetcher`
* `OTAArtifactInfo`

其中，`OtaArtifactInfo`对象包含设备版本、构建信息以及固件下载地址等元数据。安全研究人员使用Frida Hook OTAArtifactInfo构造函数，提取其中的downloadUri参数，从而获得CDN上的固件下载链接。

### 2. 获取完整固件

最初提取到的固件包约为156 MB，但该文件属于增量更新包，其内容依赖设备当前安装的固件版本。

为了获得完整固件，研究人员继续分析GraphQL请求，发现一个名为：

```
device_firmware_full_update_only
```

的参数。

Meta AI应用默认将该参数设置为false。研究人员通过Frida修改对应请求参数，将其设置为true，成功获取完整固件下载地址。

下载并解压后，发现固件采用Android更新包结构，其中包含`payload.bin`。

![](https://mmbiz.qpic.cn/mmbiz_jpg/xoBWaEOhvRHNSyCXVTvd8NuovqTdGiapiay8SUt3qvh4B59bmyOBBGBGIxjCVmP9tZp6a4PfGYica7oUJs9k9XwSWtqZe31dSb4ib2xsHVpOeiaA/640?wx_fmt=jpeg&from=appmsg)

随后使用`payload-dumper`提取系统镜像，并挂载文件系统进行分析。

![](https://mmbiz.qpic.cn/mmbiz_jpg/xoBWaEOhvRFFcsIsg2EkwKdg6Ug3quBX7CEoIOvUpAXeqaicU3gUqFImoYK8SG1zWMjpb2OvcrxMuPVM29Dt61bkuia1jhDTLiazZr530jzWNI/640?wx_fmt=jpeg&from=appmsg)

## 三、核心漏洞: DAT应用安装机制存在安全缺陷

获取固件后，研究人员开始寻找进入智能眼镜系统的方法。

关键突破口是Meta提供的Device Access Toolkit(DAT)。

DAT是Meta面向开发者提供的设备访问工具包，允许开发者编写能够与智能眼镜交互的应用程序。

![](https://mmbiz.qpic.cn/mmbiz_jpg/xoBWaEOhvRGgVK0v0BQp1wUwojcFmFwYGyBfIwsqB5QQ9zwaxByCLQzy5BanCZPvFQN7chmBlibibhfgCzvSSeaic9ibDXSrRVrKZ5KgSWcnC60/640?wx_fmt=jpeg&from=appmsg)

### 1. DAT APK 安装流程

研究人员发现，Meta AI应用在建立开发者访问会话时，会动态下载DAT APK，并将其安装到智能眼镜上。

在分析固件版本后发现：

截至固件版本126，设备没有强制验证DAT APK是否由Meta官方签名。

这意味着攻击者可以尝试替换官方DAT APK，安装自行签名的恶意APK。

### 2. 利用 Frida 替换官方 APK

研究人员使用Frida Hook DAT安装流程，将原本准备安装的官方APK替换成自己制作的APK。

主要修改内容包括：

* 替换待安装的APK文件。
* 修改应用名称为 `DAT Probe`。
* 替换对应的应用包信息。
* 保留原有安装流程，使Meta AI应用继续完成APK下发。

最终，研究人员成功让自签名DAT APK在智能眼镜上运行，实现了任意应用代码执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xoBWaEOhvRHoJEHILaNrhfuAlMoH5Pm7w4S7SA4HJlCwdxh8zBFgO0qfzeibZCctxeLicnic3EtialCo5bCUqTjJ4eO3G7UM4pB9FPjcSwYvCws/640?wx_fmt=jpeg&from=appmsg)

## 四、建立调试通道: 利用声音反馈定位执行状态

Meta Ray-Ban智能眼镜没有显示屏，也没有方便使用的控制台或日志输出接口，因此研究人员很难直接判断代码是否正常运行。

为了解决这一问题，研究人员使用Android的`ToneGenerator`功能，通过不同次数的蜂鸣声反馈程序执行状态。

| 蜂鸣次数 | 对应状态 |
| --- | --- |
| 3 次 | 监听器启动，开始寻找 Wi-Fi Direct 地址 |
| 5 次 | 成功获取 Wi-Fi Direct 地址 |
| 4 次 | TCP 31337 端口成功绑定 |
| 6 次 | 执行过程中出现错误 |

通过这种方式，研究人员发现Camera Access示例应用无法正常建立DAT会话。

原因是该应用预期智能眼镜上运行的是官方DAT APK。当替换成自制APK后，设备无法通过DWA就绪检测，导致连接被关闭。

### 绕过 DWA 就绪检测

研究人员继续使用Frida Hook：

```
startDwaReadinessProbe()
```

将该检测函数修改为空操作，从而禁用相关就绪检测和超时处理，保持通信连接。

这使得自制DAT APK能够继续运行并维持与手机端的连接。

## 五、获取交互式Shell: 通过Wi-Fi Direct建立通信

在成功运行自制DAT APK后，研究人员进一步实现了从手机向智能眼镜发送命令的能力。

### 1. 利用 Wi-Fi Direct 建立连接

Meta AI应用在同步智能眼镜中的照片和视频时，会创建一个Wi-Fi Direct网络组，使用的网段为：

```
192.168.49.x
```

智能眼镜连接该网络后，会获得对应的IP地址。

研究人员通过Hook Camera Access应用，调用Meta AI应用的Link Lease接口：

```
sub = device.createLinkLease(2, 1, cb);

highLeaseSubscriptions.push(sub);
```

从而请求建立高优先级连接，促使智能眼镜加入Wi-Fi Direct网络。

### 2. 在眼镜上启动 TCP Shell

安全研究人员在自制DAT APK中创建TCP ServerSocket，监听：

```
TCP 31337
```

手机端随后通过Netcat连接智能眼镜：

```
nc <glasses-ip> 31337
```

连接成功后，可以发送系统命令，例如：

```
id
```

研究人员获得的执行身份信息如下：

```
uid=10097(u0_a97)
gid=10097(u0_a97)
groups=3003(inet)
```

这表明研究人员已经获得智能眼镜Android应用上下文中的命令执行能力。

## 六、Meta修复后的再次绕过: Mobile Config配置篡改

研究人员最初获得Shell访问能力后，持续研究设备权限提升问题。

然而，大约5天后，原有访问方式失效。

研究人员推测，可能是Meta发现并修复了相关问题，也可能与自身操作安全不足有关。

随后，研究人员发现了另一条绕过路径。

### 1. 固件版本 127 引入签名验证

在固件版本127中，Meta开始强制验证DAT APK的数字签名。

相关配置项为：

```
wss_appmanager.signature_verification_enabled
```

该配置用于控制设备是否检查待安装应用是否由Meta签名。

因此，之前直接替换DAT APK的方法不再有效。

### 2. 分析 Mobile Config 配置机制

研究人员进一步分析发现，智能眼镜并非完全独立获取配置，而是通过配对手机请求配置文件。

整个流程如下：

1. 智能眼镜向配对手机请求配置。
2. 手机从Meta服务器获取Mobile Config。
3. 手机通过Airship将配置转发给智能眼镜。
4. 智能眼镜加载配置并应用对应功能开关。

Mobile Config中包含大量功能标志，可以在不更新固件的情况下调整设备功能。

### 3. 绕过配置文件完整性验证

研究人员发现，智能眼镜虽然会检查配置文件的结构是否合法，但没有验证配置文件是否遭到篡改。

因此，攻击者可以在手机端修改配置文件中的功能开关。

研究人员通过修改 `0.mctable` 文件中的一个字节，将对应配置值从：

```
0x80
```

修改为：

```
0x00
```

从而关闭APK签名验证功能。

完成修改后，智能眼镜接受了被篡改的配置，研究人员再次成功安装自签名DAT APK。

这意味着即使固件版本127增加了签名验证机制，攻击者仍可能通过Mobile Config配置篡改绕过该保护。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xoBWaEOhvRHial0nJYn6FC5cH9uibHLK4iauE4cKU96oDRz3GeCylFure0RFg1QCHcGrNJn7XFLVD0vGLTibL7QcYxfGiaJ9yzgcgZY7jIEB1CBc/640?wx_fmt=jpeg&from=appmsg)

## 七、攻击链总结

本次研究的核心并非单一漏洞，而是多个安全机制缺陷组合形成的攻击路径。

```
逆向分析 Meta AI 手机应用
          |
          v
提取 OTA 固件下载地址
          |
          v
获取完整 Android 固件
          |
          v
分析 DAT APK 安装机制
          |
          v
替换官方 DAT APK
          |
          v
绕过 APK 签名验证
          |
          v
在智能眼镜运行自定义 APK
          |
          v
利用 Wi-Fi Direct 建立通信
          |
          v
监听 TCP 31337 端口
          |
          v
获得交互式 Shell
```

固件版本127增加签名验证后，研究人员又发现了另一条绕过路径：

```
修改手机端 Mobile Config
          |
          v
篡改 0.mctable 配置值
          |
          v
关闭 DAT APK 签名验证
          |
          v
重新安装自签名 APK
```

关键安全问题对比：

| 安全环节 | 发现的问题 |
| --- | --- |
| DAT APK 安装 | 早期固件未强制验证 APK 签名 |
| DWA 就绪检测 | 可通过 Hook 绕过相关检测 |
| Wi-Fi Direct | 可利用设备连接机制建立通信 |
| Mobile Config | 配置文件缺少有效的防篡改验证 |
| 签名验证开关 | 本地配置篡改可绕过新增保护机制 |

## 八、漏洞影响与安全风险

本次研究表明，智能眼镜虽然属于轻量级可穿戴设备，但其底层仍然运行Android系统，并具备应用安装、无线通信、摄像头及数据同步等功能。

如果类似问题被恶意利用，可能产生以下风险：

1. 未经授权的代码执行: 攻击者可能通过DAT安装机制运行非官方应用。
2. 设备控制能力增强: 获得Shell后，可以进一步分析设备内部服务和系统攻击面。
3. 隐私数据风险: 智能眼镜涉及照片、视频及其他个人数据，未经授权的应用执行可能扩大隐私泄露风险。
4. 安全机制绕过: Mobile Config缺乏有效防篡改验证，使设备新增的APK签名保护机制仍存在被绕过的可能。

## 九、厂商响应与修复情况

研究人员表示，已经通过Meta漏洞赏金平台提交了相关问题。

Meta已批准其发布技术研究内容。作者据此推测相关问题已经修复。

不过，目前没有披露：

* Meta官方安全公告编号。
* 对应漏洞的CVE编号。
* 具体受影响的产品型号。
* 完整修复固件版本及发布时间。
* 漏洞赏金的最终金额。

## 十、安全建议

针对Meta Ray-Ban智能眼镜及类似Android可穿戴设备，建议：

* 及时安装厂商发布的最新固件及安全更新。
* 使用官方Meta AI应用进行设备连接和固件升级。
* 不要安装来源不明的DAT APK或第三方设备访问应用。
* 谨慎开启开发者模式及设备调试功能。
* 避免使用经过修改的配对手机应用或配置文件。
* 厂商应对Mobile Config实施数字签名验证及完整性校验，避免客户端能够任意修改安全关键配置。
* 对APK安装流程实施强制签名校验，并确保相关安全策略无法被低信任级别的配置覆盖。

## 十一、总结

此次Meta Ray-Ban智能眼镜安全研究展示了一个值得关注的问题：设备固件本身具备安全保护，并不意味着整个应用安装和配置管理体系同样安全。

研究人员先通过OTA机制获取完整固件，再利用DAT安装流程实现自签名APK执行，随后通过Wi-Fi Direct和TCP 31337建立交互式Shell。

当Meta在固件版本127中引入APK签名验证后，研究人员又通过Mobile Config配置篡改找到了新的绕过方式。

这次研究也说明，智能眼镜、智能手表等可穿戴设备正在成为值得重点关注的物联网安全研究对象，其应用安装机制、配置管理机制和无线通信接口都可能成为新的攻击入口。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LCF75xtxMiaiaUiauC6TKOGdQ4TYySakdjbD0xCM5iakCGJ1S98zU7AahSSrSrtoqdNQUSjoQZ2ia7KHDichAXQSQsPw/0?wx_fmt=png)

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