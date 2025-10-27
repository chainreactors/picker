---
title: Kali Linux 2023.1发布-10周年版-Kali Purple
url: https://blog.upx8.com/3322
source: 黑海洋 - WIKI
date: 2023-03-21
fetch_date: 2025-10-04T10:09:08.683661
---

# Kali Linux 2023.1发布-10周年版-Kali Purple

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Kali Linux 2023.1发布-10周年版-Kali Purple

发布时间:
2023-03-20

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
27077

**Kali Linux 2023.1 发布（Kali Purple 和 Python 变更）**

**10th anniversary**

今天我们发布了 Kali 2023.1（也是我们**10 周年**-2023 年 3 月 13 日，星期一）！当您读完这篇文章时，它就可以立即[下载](https://blog.upx8.com/go/aHR0cHM6Ly93d3cua2FsaS5vcmcvZ2V0LWthbGkv)或[更新了。](https://blog.upx8.com/go/aHR0cHM6Ly93d3cua2FsaS5vcmcvZG9jcy9nZW5lcmFsLXVzZS91cGRhdGluZy1rYWxpLw)

鉴于我们成立 10 周年，我们很高兴地宣布，我们准备了一些特别的东西来庆祝。[请继续关注2023 年 3 月 15 日星期三](https://blog.upx8.com/go/aHR0cHM6Ly93d3cudGltZWFuZGRhdGUuY29tL2NvdW50ZG93bi9iaXJ0aGRheT9pc289MjAyMzAzMTVUMTImcDA9JTNBJm1zZz1LYWxpKzEwK1llYXJzJmZvbnQ9Y3Vyc2l2ZSZjc3o9MSM)12:00:00 [UTC/+0 GMT](https://blog.upx8.com/go/aHR0cHM6Ly90aW1lLmlzL1VUQw)发布的博文，了解更多信息！

[![Kali Linux 2023.1发布-10周年版-Kali Purple](https://www.ddosi.org/wp-content/uploads/2023/03/1-18.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIzLzAzLzEtMTgud2VicA)

[自 12 月发布 2022.4以来的](https://blog.upx8.com/go/aHR0cHM6Ly93d3cua2FsaS5vcmcvYmxvZy9rYWxpLWxpbnV4LTIwMjIuNC1yZWxlYXNlLw)[变更](https://blog.upx8.com/go/aHR0cHM6Ly9idWdzLmthbGkub3JnL2NoYW5nZWxvZ19wYWdlLnBocA)日志摘要：

* **[Kali Purple](https://blog.upx8.com/go/aHR0cHM6Ly93d3cua2FsaS5vcmcvYmxvZy9rYWxpLWxpbnV4LTIwMjMtMS1yZWxlYXNlLyNrYWxpLXB1cnBsZQ)** – 新时代的曙光。**Kali不仅是进攻，而且开始防守**
* **[Python 变化](https://blog.upx8.com/go/aHR0cHM6Ly93d3cua2FsaS5vcmcvYmxvZy9rYWxpLWxpbnV4LTIwMjMtMS1yZWxlYXNlLyNweXRob24tdXBkYXRlcy0tY2hhbmdlcw)**– Python 3.11 和 PIP 的变化向前发展
* **[2023 主题](https://blog.upx8.com/go/aHR0cHM6Ly93d3cua2FsaS5vcmcvYmxvZy9rYWxpLWxpbnV4LTIwMjMtMS1yZWxlYXNlLyMyMDIzLXRoZW1lLXJlZnJlc2g)**– 我们每年一次的主题更新！这一次，旧的又是新的
* **[桌面更新](https://blog.upx8.com/go/aHR0cHM6Ly93d3cua2FsaS5vcmcvYmxvZy9rYWxpLWxpbnV4LTIwMjMtMS1yZWxlYXNlLyNkZXNrdG9wLXVwZGF0ZXM)**– Xfce 4.18 和 KDE Plasma 5.27
* **[默认内核设置](https://blog.upx8.com/go/aHR0cHM6Ly93d3cua2FsaS5vcmcvYmxvZy9rYWxpLWxpbnV4LTIwMjMtMS1yZWxlYXNlLyNkZWZhdWx0LWtlcm5lbC1zZXR0aW5ncw)**– 是什么让 Kali 内核与众不同
* **[新工具](https://blog.upx8.com/go/aHR0cHM6Ly93d3cua2FsaS5vcmcvYmxvZy9rYWxpLWxpbnV4LTIwMjMtMS1yZWxlYXNlLyNuZXctdG9vbHMtaW4ta2FsaQ)**– 一如既往，添加了各种新工具

---

## Kali Purple

> ***我们正在公平竞争**！*

多年来，我们已经完善了我们的专长，即进攻性安全。**我们现在开始涉足一个新领域，防御性安全！**我们正在进行“Kali Purple”的初步技术预览预发布。这仍处于起步阶段，需要时间才能成熟。但是你可以开始看到 Kali 正在扩展的方向。您也可以成为帮助塑造方向的一部分！

[![Kali Linux 2023.1发布-10周年版-Kali Purple](https://www.ddosi.org/wp-content/uploads/2023/03/2-12.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIzLzAzLzItMTIud2VicA)

**什么是kali **Purple**？**

**蓝色和紫色团队的一站式商店。**

> *感觉脸红？情绪低落？*卡莉紫：你就是你！

还记得十年前我们用 Kali Linux 做了什么吗？或者在那之前使用[BackTrack](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuYmFja3RyYWNrLWxpbnV4Lm9yZy8)？我们让每个人都可以访问攻击性安全。不需要昂贵的许可证，不需要商业级的基础设施，不需要编写代码或编译工具来使它全部工作……只需下载 Kali Linux 并做你想做的事。

**我们很高兴开始新的旅程，其使命是为防御性安全做同样的事情：只需下载 Kali Purple 并做你想做的事。**

Kali Purple 从一个概念验证开始，演变成一个框架，然后是一个平台*（就像今天的 Kali 一样）*。目标是让每个人都能获得企业级安全性。

---

**什么是Kali Purple？**

在更高的层次上，Kali Purple 包括：

* 终极 SOC In-A-Box 的参考架构；完美的：
  + 学习
  + 练习 SOC 分析和威胁搜寻
  + 安全控制设计与测试
  + 蓝色/红色/紫色组队练习
  + Kali 间谍 vs. 间谍比赛（Blue vs. Red）-红蓝对抗
  + 保护中小型环境
* **超过 100 种防御工具**，例如：
  + [Arkime](https://blog.upx8.com/go/aHR0cHM6Ly9wa2cua2FsaS5vcmcvcGtnL2Fya2ltZQ) – 完整的数据包捕获和分析
  + [CyberChef](https://blog.upx8.com/go/aHR0cHM6Ly9wa2cua2FsaS5vcmcvcGtnL2N5YmVyY2hlZg) – 网络瑞士军刀
  + `Elastic Security`– 安全信息和事件管理
  + [GVM——](https://blog.upx8.com/go/aHR0cHM6Ly93d3cua2FsaS5vcmcvdG9vbHMvZ3ZtLw)漏洞扫描器
  + [TheHive](https://blog.upx8.com/go/aHR0cHM6Ly9wa2cua2FsaS5vcmcvcGtnL3RoZWhpdmU) – 事件响应平台
  + `Malcolm`– 网络流量分析工具套件
  + [Suricata](https://blog.upx8.com/go/aHR0cHM6Ly9wa2cua2FsaS5vcmcvcGtnL3N1cmljYXRh) – 入侵检测系统
  + [Zeek](https://blog.upx8.com/go/aHR0cHM6Ly9wa2cua2FsaS5vcmcvcGtnL3plZWs) -（另一个）入侵检测系统*（都有它们的用例！）*
  + *……当然还有所有常用的[Kali 工具](https://blog.upx8.com/go/aHR0cHM6Ly93d3cua2FsaS5vcmcvdG9vbHMv)*
* 防御工具[文档](https://blog.upx8.com/go/aHR0cHM6Ly9naXRsYWIuY29tL2thbGlsaW51eC9rYWxpLXB1cnBsZS9kb2N1bWVudGF0aW9u)
* [预生成镜像](https://blog.upx8.com/go/aHR0cHM6Ly93d3cua2FsaS5vcmcvZ2V0LWthbGkv)
* Kali Autopilot – 用于自动攻击的攻击脚本生成器/框架
* Kali Purple Hub 供社区分享：
  + 练习 pcaps
  + 蓝队练习的 Kali Autopilot 脚本
* [社区维基](https://blog.upx8.com/go/aHR0cHM6Ly9naXRsYWIuY29tL2thbGlsaW51eC9rYWxpLXB1cnBsZS9kb2N1bWVudGF0aW9uLy0vd2lraXMvaG9tZQ)
* 根据 NIST CSF（美国国家标准与技术研究院关键基础设施网络安全）的防御菜单结构：
  + 确认
  + 保护
  + 探测
  + 回应
  + 恢复
* 用于社区协作和娱乐的Kali Purple [Discord频道](https://blog.upx8.com/go/aHR0cHM6Ly9kaXNjb3JkLmthbGkub3JnLw)
* 和主题：安装程序、菜单项和 Xfce！

……而这只是我们旅程的开始。

### kali purple工作原理

[![Kali Linux 2023.1发布-10周年版-Kali Purple](https://www.ddosi.org/wp-content/uploads/2023/03/Kali-Purple-03-Architecture-scaled.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIzLzAzL0thbGktUHVycGxlLTAzLUFyY2hpdGVjdHVyZS1zY2FsZWQud2VicA)

### 截图

这就是它的样子。一些防御工具：

****Elastic SIEM****：

[![Kali Linux 2023.1发布-10周年版-Kali Purple](https://www.ddosi.org/wp-content/uploads/2023/03/3-8-scaled.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIzLzAzLzMtOC1zY2FsZWQud2VicA)

****Arkime****：

[![Kali Linux 2023.1发布-10周年版-Kali Purple](https://www.ddosi.org/wp-content/uploads/2023/03/4-7-scaled.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIzLzAzLzQtNy1zY2FsZWQud2VicA)

****Malcolm****:

[![Kali Linux 2023.1发布-10周年版-Kali Purple](https://www.ddosi.org/wp-content/uploads/2023/03/5-6-scaled.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIzLzAzLzUtNi1zY2FsZWQud2VicA)

**安装程序、菜单和 Xfce**：

[![Kali Linux 2023.1发布-10周年版-Kali Purple](https://www.ddosi.org/wp-content/uploads/2023/03/6-5.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIzLzAzLzYtNS53ZWJw)
[![Kali Linux 2023.1发布-10周年版-Kali Purple](https://www.ddosi.org/wp-content/uploads/2023/03/7-5.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIzLzAzLzctNS53ZWJw)
[![Kali Linux 2023.1发布-10周年版-Kali Purple](https://www.ddosi.org/wp-content/uploads/2023/03/8-4.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIzLzAzLzgtNC53ZWJw)

其他更多截图:

[![Kali Linux 2023.1发布-10周年版-Kali Purple](https://www.ddosi.org/wp-content/uploads/2023/03/2-13-scaled.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIzLzAzLzItMTMtc2NhbGVkLndlYnA)[![Kali Linux 2023.1发布-10周年版-Kali Purple](https://www.ddosi.org/wp-content/uploads/2023/03/3-9-scaled.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIzLzAzLzMtOS1zY2FsZWQud2VicA)
[![Kali Linux 2023.1发布-10周年版-Kali Purple](https://www.ddosi.org/wp-content/uploads/2023/03/4-8-scaled.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIzLzAzLzQtOC1zY2FsZWQud2VicA)
[![Kali Linux 2023.1发布-10周年版-Kali Purple](https://www.ddosi.org/wp-content/uploads/2023/03/5-7-scaled.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIzLzAzLzUtNy1zY2FsZWQud2VicA)
[![Kali Linux 2023.1发布-10周年版-Kali Purple](https://www.ddosi.org/wp-content/uploads/2023/03/8-5.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIzLzAzLzgtNS53ZWJw)
[![Kali Linux 2023.1发布-10周年版-Kali Purple](https://www.ddosi.org/wp-content/uploads/2023/03/9-5.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDIzLzAzLzktNS53ZWJw)

请前往[Kali Purple wiki](https://blog.upx8.com/go/aHR0cHM6Ly9naXRsYWIuY29tL2thbGlsaW51eC9kb2N1bWVudGF0aW9uL2thbGktcHVycGxlLy0vd2lraXMvaG9tZQ)加入这项运动。

## Python 更新和更改

Debian 正准备发布其下一个稳定版本（大约每 2 年发布一次，看起来可能是今年夏天）。结果，包在所有地方都得到了更新。活跃的软件包维护者正在将他们的工作升级到最新版本，否则，等待下一个版本的时间很长！Python 也不例外，**Python 3.11 现在在 Debian 中**，它带有更多信息错误回溯和巨大的速度提升（[在 10-60% 之间](https://blog.upx8.com/go/aHR0cHM6Ly9kb2NzLnB5dGhvbi5vcmcvMy93aGF0c25ldy8zLjExLmh0bWw)）。升级的影响不会像[`py...