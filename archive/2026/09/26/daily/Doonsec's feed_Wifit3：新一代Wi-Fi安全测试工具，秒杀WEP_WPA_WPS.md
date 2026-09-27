---
title: Wifit3：新一代Wi-Fi安全测试工具，秒杀WEP/WPA/WPS
url: https://mp.weixin.qq.com/s/WEFSK8mrsoaxqBNQ7jWDyA
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:23:00.242305
---

# Wifit3：新一代Wi-Fi安全测试工具，秒杀WEP/WPA/WPS

# Wifit3：新一代Wi-Fi安全测试工具，秒杀WEP/WPA/WPS

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6O0yA9WicohDtTiaUaElLchZTjHXZ0XOLibanuaIphahu6zBvpcZXMbGdxcjAIaJc7npO0HW6ZQTknHxhdk6gOGt2RvL1Q12QT28A/640?from=appmsg)
> **导语**：刚入行渗透测试的新人第一个问题往往就是"我怎么黑 WiFi？"Wi-Fi 安全测试确实是渗透测试里最快能看到战果的环节，而且许多企业还留着老路由、WEP 加密、WPS 常开——这些配置放到今天基本等于裸奔。Wifit3 是最近冒出来的新工具，作者也是 Wifite2 的同一个人，走纯 Python 路线，把常见 WiFi 攻击全部收在一个包里。

---

## 一、工具简介

Wifit3 的作者同时也是 Wifite2 的作者。跟 Wifite2 不一样的地方是，它不再依赖 aircrack-ng、reaver 或 bully 这些传统工具，而是纯 Python 实现，底层用 PyUSB 和 Textual 库。

跨平台没问题，Linux、macOS、Windows 都能跑，只要有 USB 无线网卡就行。支持的网卡列表在它的 GitHub 仓库里有写。

扫描阶段，它同时扫 2.4 GHz 和 5 GHz，能判断目标用的是 WPA3 还是 WPA2/WPA3 混合模式，还能跟踪信号强度和加密类型。部分路由器能直接识别型号，甚至能从隐藏 SSID 的特征里把网络名给扒出来。

![Wifit3 WiFi AP 扫描结果](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PRIOHiaYfOVesGj7sQ4icExBjiaALiaIuT6FvBF2E94qKQbKTXMqjbueia08B8wCJap1KEEMHQIuo0mmoX7F6OqrkNYZibz87kXU2Mw/640?from=appmsg "Wifit3 WiFi AP 扫描结果")

上图是扫描结果，AP 列表出来了，SSID、BSSID、信号、信道、加密类型一目了然。

### 多网卡监听

插两张以上的无线网卡就能同时监听多个信道，留一张专门发包。Wifit3 会显示 beacon 帧、数据帧、注入帧和 deauth 帧，你在测试的时候能实时看见空中的流量情况。

## 二、攻击能力

### 2.1 握手抓包 + 离线破解

Wifit3 能监听 WiFi 流量并向客户端发 deauth（解除认证）帧，把客户端踢下线。客户端重新连路由器时会发起完整认证过程，这个过程中会泄露握手信息。工具把这些握手记录下来，密码在里面但是加密状态，之后可以用 hashcat 离线跑。

![Wifit3 抓包并捕获握手包](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6O2yibg8Spib8Hox6fdosJdmL9eoiahG22EsiaQic44MptqBCOJwVWzH1ribuCppR1aBJXscNWicEgNst2dmjQ7MSLWQxlgTqY2gkw3A0/640?from=appmsg "Wifit3 抓包并捕获握手包")

上图可以看到它抓握手包的全过程，客户端被踢下线后重新连接，握手被记录下来。

### 2.2 PMKID 捕获

除了完整握手，Wifit3 还能捕获 PMKID。PMKID 是路由器发出来的一段短哈希，和 WiFi 密码绑定。只要拿到这个哈希，不需要踢客户端、不需要完整握手，直接拿到本地用 hashcat 跑密码就行。

### 2.3 Evil Twin（WPA3）

针对 WPA3 还有个 Evil Twin（伪基站）模式。原理是把附近用户的设备从真 AP 上踢掉，引导它们连接自己搭建的假 AP，用户输入密码后工具就能拿到握手。这种手法对 WPA3 同样有效。

### 2.4 WPS 攻击

WPS 攻击走的是三种路线叠加：

* **Pixie Dust（快速攻击）**：利用 WPS 的随机数生成漏洞，不需要暴力枚举就能直接拿到 WPS PIN
* **按钮攻击**：等有人按路由器的 WPS 物理按键，抓认证期间交换的凭据
* **暴力枚举 PIN**：正常枚举 WPS PIN，遇到路由开始锁定尝试次数就暂停，等冷却期过了继续

![Wifit3 WPS 攻击抓取凭据](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NGHhPM7eEb3Oax63IWEYy8ic2Y4pqAPcOTtwuXt6UG4hZLy1oxduPUfIB4UUyoRVGtKsshZ7u7x8SRIOYg2MNXacM0mtpL335k/640?from=appmsg "Wifit3 WPS 攻击抓取凭据")

上图是 WPS 攻击的执行画面，工具通过发送 enrollee 身份和公钥，让路由器解密凭据，密码最终保存到文本文件。

### 2.5 WEP 破解

WEP 是老问题，Python 实现，走经典的 ARP request replay（ARP 请求重放）技术。原理是抓一个 ARP 包然后反复重放，快速积累 IV（初始化向量），攒够了直接导出密钥。

## 三、安装部署

按照惯例用 Kali Linux 来演示，别的系统也行。安装就三条命令：

```
kali > wget https://github.com/derv82/wifit3/releases/download/v0.3.2/wifit3-linux-x64 -q
kali > chmod 777 wifit3-linux-x64
kali > sudo cp wifit3 /usr/local/bin
```

![Wifit3 安装过程](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MsDyV8RLqX0vKHLZoh0gu9UX07mne7icQExAUZMrVPfKvqGyafko4uwdy1RIYUPxOWwZtsVmIzMdGJtxWoerSPMzZ3P0LaEwGA/640?from=appmsg "Wifit3 安装过程")

装完插上 USB 无线网卡，直接启动：

```
kali > wifit3
```

启动后选好网卡就能开始扫描了。

![选择无线网卡](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NvO0b1OYcrdmkv4ojwZYMjlWvLxw0D1VMibaHg24a9rAmToK9DkGKZ479j6GpXDAo0iayGC8EYG2jK2FNu6fXN9gLx54dA09W5Y/640?from=appmsg "选择无线网卡")

![Wifit3 实时攻击演示](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PYlVBpmvaRU90CKpiaDWTlxatP3Doe14gKuuB46pkgFibPY8bIvhahTdnCNNeR10quQeIKkqk57Y7CpPddCrQyic2RicSnT5BmynQ/640?from=appmsg "Wifit3 实时攻击演示")

## 四、红队视角

Wifit3 把 WiFi 渗透测试最常见的几条攻击路径全部整合进了同一个界面。以前要开 airodump-ng 扫 AP，切 aireplay-ng 发 deauth，另开窗口跑 aircrack-ng 破解，手忙脚乱。Wifit3 一个工具全搞定。

但实际用的时候有几个现实约束：

**无线网卡质量是瓶颈**。能跑注入的网卡（如 Atheros AR9271、Ralink RT3070）是最低要求，很多 USB 网卡虽然能扫描但不支持 packet injection（数据包注入），装得再好也白搭。工具本身能不能打，最后取决于硬件。

**WPA3 攻击依然有前提**。Evil Twin 模式对 WPA3 能用，但它本质上是社会工程学攻击的变体——引导用户主动连假 AP 而不是直接破解加密。如果目标用户很警惕，这条路就走不通。

**WPS 是短板**。现在大多数家用路由早就默认关掉 WPS 了，企业设备更不会开。枚举 PIN 的效率在路由有锁定机制的情况下会大幅下降。真正有价值的是 Pixie Dust 那一路，碰到开了 WPS 的目标一打一个准。

## 五、防御建议

红队视角说完，防御方也需要注意：

* **关掉 WPS**：这是最简单的一步，但 90% 的家庭和中小企业路由开着它
* **用 WPA3-Enterprise 替代 WPA2-Personal**：WPA3 的 SAE 握手本身就让离线字典攻击基本失效
* **隐藏 SSID 治标不治本**：虽然 Wifit3 能从 BSSID 特征反推隐藏 SSID，但至少增加了一层障碍
* **部署 802.11w（管理帧保护）**：能阻挡 deauth 攻击，不让攻击者轻易踢客户端
* **定期检查路由固件**：过时的固件可能存在额外的 WPS 漏洞或后门

## 六、总结

Wifit3 本身不是革命性工具，它的价值是把 WiFi 渗透测试几个最常用的操作整合到了一个界面里，免去来回切终端。对于新手来说，一个工具学会 WiFi 渗透的完整流程，门槛低了不少。但对于红队来说，任何工具都有局限，关键还是手里有没有能打注入的网卡，以及目标网络的真实防御水平。

工具仓库（官方 GitHub）：

* https://github.com/derv82/wifit3

原文出处：

* https://hackers-arise.com/wi-fi-hacking-testing-routers-with-wifit3/

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OvhMk29Y8KRia5f52Nm3PHVwIM6WMqEmLldPWAdvNw2Gh8TffvpFfGmksW8VoQicXiavpS4B4qnJjo95XHGWYYzj6pWSicA6icQzHw/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OfGBpNpHcwe8KNsdchYPb3fVhoNwGbs8nagMNxzicWia1XwBibMMzGD10VLYWOhPCMq5qjeUTFz5q0ZWQreYtCPn46x0QEczXyk4/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OyoNczwllyt7kE7oefVM9HibNRkIbtUuxEGfyHM9U4ko4nm8kNy4g1LsCJFAQDMFg8IKEpEnkdAxslSV0XOoaz1ceuOIj2PxvU/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NMjedibbctgGKsNMaEWW9w4fFN7Lb1MZaPs98kxF7mGFtH07EWPMA1rCRib6ibXPQuU1vwWnFDkVYsLJlYLECtDFeN47iaZPfickibY/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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