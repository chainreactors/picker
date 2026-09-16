---
title: iOS 27 发布当日即遭破解：AirLift 配对越狱 PoC 深度技术分析
url: https://mp.weixin.qq.com/s/rGODvKFJ_ID2-pTL2rgauw
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:02:43.791386
---

# iOS 27 发布当日即遭破解：AirLift 配对越狱 PoC 深度技术分析

# iOS 27 发布当日即遭破解：AirLift 配对越狱 PoC 深度技术分析

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NLmSdbjGO6rYu7omfxIW9uphjsoTjMrUvsUic0PvXY8faQiaavXALhyTXtybUDZicjkhx072bEM9p0IlEicucUVYTNeicUtGZMIH3A/640?from=appmsg)
> **导语**：iOS 27 正式版推送的当天，安全研究员 @0xjohnny（Johnny）即在 X 平台公开了名为 **AirLift（配对越狱）** 的沙箱逃逸概念验证工具。该工具针对苹果的 AirTraffic 媒体同步服务，无需在 iOS 上安装任何应用，仅通过一台已与目标设备配对的 Mac，就能读写 iOS 沙箱外的多个敏感目录。

---

![配对越狱攻击链路示意图](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PxibPR7bZW6sr7owokicuJowtPEIO9vUwdQA1vwt33Zq2pxjNjMJ12Dab5Mju1HyHT0PtDcQhctxCwMH2A5Mwkia4Ah1WaFPFpwE/640?from=appmsg "配对越狱攻击链路示意图")

## 一、事件速览

9 月 14 日，@0xjohnny 在 X 平台用一句话开场："庆祝 iOS 27 发布，顺便发个沙箱逃逸。" 推文 12 小时内拿到 18.5K 浏览，配套 GitHub 仓库 `0xjohnnydev/airlift` 同步开放下载。

测试机型是 iOS 27.0 RC（24A435），作者表示 iOS 27.0 正式版（24A437）同样可用，其他版本会弹警告。这是典型的负责任披露：攻击面完整公开但限制在已修复版本之外，避免被恶意利用。

PoC 用 Python 主控脚本配合两个 Objective-C 小工具（device\_helper.m 和 airtraffic\_host.m）通过 Xcode 工具链编译。运行一次只会写入随机金丝雀值、验证落地后立刻删除，不污染数据也不留痕。

## 二、攻击链路解剖

要理解这个漏洞，必须先看清 macOS 与 iOS 是怎么"配对通信"的。调用链从上到下分别是：

macOS 端：`MobileDevice.framework`（设备通信框架）→ `AirTrafficHost.framework`（媒体同步主机框架）。

iOS 端：`streaming_zip_conduit`（流式压缩管道）→ `afc`（苹果文件连接服务）→ `atc/AirTrafficDevice`（媒体同步守护进程）→ 图书同步客户端 → `ATLegacyAssetLink`（历史资源链接层）→ **ATAirlock（沙箱闸门）** → `NSFileManager`（文件管理器）。

攻击者只需在自己的 Mac 上启动 `airlift.py`，通过 Wi-Fi 或 USB 与已配对的 iPhone 建立连接。无需在 iPhone 上安装任何东西，整条链路全靠系统服务完成。这就是典型的"信任边界外溢"——苹果认为已配对的 Mac 是可信的，所以放宽了沙箱闸门的所有检查。

## 三、核心漏洞：沙箱闸门的路径验证缺陷

沙箱闸门是 iOS 端专门负责"沙箱内"到"沙箱外"流量审计的闸门组件。在 `-[沙箱闸门 processCompletedAsset:]`（资产完成处理方法）中，苹果原本的逻辑是：

```
// Books 的"持久化 ID"被直接拼到源路径，没有路径校验
NSString *source = [@"/var/mobile/Media/Airlock/Book"
    stringByAppendingPathComponent:asset.identifier];

// 目标路径仅检查字符串前缀
NSString *destination = [[@"/var/mobile/Media/"
    stringByAppendingPathComponent:asset.path]
    stringByStandardizingPath];

if (![destination hasPrefix:@"/var/mobile/Media/"])
    return;

[fileManager moveItemAtPath:source toPath:destination error:&error];
```

问题出在三处叠加的设计疏漏：

第一，**源路径不做校验**。Books 应用的"持久化 ID"字段直接被拼到源路径里，没有任何合法性检查。攻击者能控制这个字段就能注入 `..`（父目录引用）这样的相对路径。

第二，**目标路径只检查字符串前缀**。`hasPrefix:@"/var/mobile/Media/"` 只比对字符串本身，不解析符号链接。攻击者把目标路径的祖先目录换成指向 `/var/mobile` 外部的软链接，这个检查就被完美绕过。

第三，**流式压缩管道接受相对符号链接**。资产解压阶段，只要符号链接的相对路径还在解压目录范围内就会被保留，给攻击者构造软链接链的机会。

## 四、PoC 工作原理

配对越狱工具的攻击流程是这样的：

1. **第一次移动**：在 `/var/mobile/Media/Airlock/Book/` 下放置相对符号链接指向 `..`，流式压缩管道因为它还在解压目录内而接受。
2. **第二次移动**：用 Books 持久化 ID 注入 `..`，让沙箱闸门把这个符号链接文件移动到 `/var/mobile/Media/` 下，移动后符号链接指向 `/var/mobile`。
3. **第三次移动**：构造目标路径为 `/var/mobile/<受控目录>/<文件>`。由于符号链接的"祖先"已指向 `/var/mobile`，文件管理器实际写入的就是目标路径。
4. **金丝雀验证**：写入随机金丝雀值，通过 AFC 读取回来比对，确认落地后立即删除。

读取操作间接一些：把已知文件移入 Media 目录，通过 AFC 读取再移回原位。整个过程对 iPhone 用户完全静默——没有弹窗，没有日志。

## 五、影响范围与缓解

PoC 已确认可读写 `/var/mobile` 整个根、`/var/mobile/Documents`（用户文档）、`/var/mobile/Library/Preferences`（应用偏好设置）、`/var/mobile/Library/SpringBoard`（桌面状态）、`/var/mobile/Library/SMS`（短信数据库）、`/var/mobile/Library/Safari`（历史、书签、Cookie）、`/var/mobile/Containers/Data/Application`（所有沙箱应用数据）、`/var/mobile/Containers/Shared/AppGroup`（应用共享组）、`/var/tmp`。

唯一攻不破的是 `MobileGestalt.plist`（系统标识配置）——存储设备的硬件识别和行为开关，作者明确表示"暂未涉及，正在研究"。一旦这条防线被突破，就是完整的设备指纹克隆加行为伪装能力。

普通用户暂时不需要恐慌——攻击前提是攻击者必须物理接触或远程控制一台与你的 iPhone 配对过的 Mac。威胁主要落在三个场景：企业 BYOD 设备被离职员工反查、家庭成员间隐私侵犯、越狱研究者找新工具链。但对企业安全团队这是一记警钟：员工换岗或离职时必须清除 iPhone 上的 Mac 配对记录（设置 → 通用 → 传输或还原 iPhone → 重置）。

## 六、红队视角总结

配对越狱工具的真正价值不在于"突破沙箱"这个表层结果，而在于它展示了一种系统化的攻击者思维：**信任边界外溢**。苹果设计沙箱闸门时的假设是"已配对 Mac 是可信的"，但这个假设在 BYOD 时代已经千疮百孔。对于红队，这意味着企业移动设备管理（MDM）必须把"Mac 配对记录"作为离职流程的强制清除项；对于蓝队，要把沙箱闸门这类"信任代理"组件列入深度审计清单；对于越狱研究者，iOS 27 的攻击面才刚刚开始——系统标识配置那条线一旦打通，整个生态又会进入新一轮攻防周期。

代码已在 GitHub 开源，欢迎下载到本地编译研究。建议在隔离的 macOS 测试环境跑，不要拿生产设备玩。

## 附录：PoC 程序下载

**官方仓库**：https://github.com/0xjohnnydev/airlift

下载后编译运行（需要 macOS 与 Xcode 命令行工具）：

```
git clone https://github.com/0xjohnnydev/airlift.git
cd airlift
make              # 编译两个 Objective-C helper
./airlift.py      # 列出已配对 iPhone 并交互选择
./airlift.py --device <UDID> --target /var/mobile/Library/Safari --verbose
```

**重要提示**：

1. 必须在已配对的 Mac 上运行
2. 仅适用于 iOS 27.0 RC（24A435）和正式版（24A437）
3. 默认写入金丝雀值后立即删除，不破坏数据
4. 仅限合法安全研究、合规审查使用

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6O5lpdMDRrJNmWSChUbvQUkb9k3yqhsb0iapwjOB0Epk8qHuFTLk8VBzN3mywITrnMChkd4kWBJtkpVdAmhXwQNyuLxj622UmWc/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PwBQg3S0wLgNas5KVP9sQzsGfsXWbLufmTc8rLSq1NqibfSwogeAwWnB1xNxB81XZn3yfqKQAibcSYDZka6icEQhTNzo49KvCc6Y/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OghPqdWhD2VxIuNsxt7mp0pp5ReQ7mlP07NwfjL0mQQcbOISCnp0c3xicia9DqJRcP0BIrpzgjf45Rj6CTBz00d3QfrvLZtiaz2U/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MgQGmwoRqURUwIgLSG2J26iaS1B2KL7kRbhuMpBMrxX4GHgTMPp9kxCcaUMWMVZUYNsKEbHicMzZRRAGemCxpYu7bfJJ3aAvSNg/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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