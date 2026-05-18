---
title: 173k Star！2026 最新开源方案：安全免费激活 Windows&amp;Office（附详细教程）
url: https://mp.weixin.qq.com/s/MRd52JSKbXQHDlNsqHcP-w
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:08:03.980798
---

# 173k Star！2026 最新开源方案：安全免费激活 Windows&amp;Office（附详细教程）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/W2hHqUjyRk228rlMLacGX3ic7u6iaTqoIp35ZoXfYbwf0KRQAjfmgRTuLeicPmv52deE5BExCU0crpdjF2Tr8Cdb1J5NKoSEE0L7bDSayicoHR8/0?wx_fmt=jpeg)

# 173k Star！2026 最新开源方案：安全免费激活 Windows&Office（附详细教程）

原创

d0ublewei
d0ublewei

大伯为安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### 一、 概述：为什么它是“激活神器”？

* 还在到处找充满了后门病毒的激活工具？或者好不容易找到一个，却被 Windows Defender 瞬间秒杀？
* **Microsoft Activation Scripts (简称 MAS)** 彻底终结了这些烦恼。作为 GitHub 上目前最火的开源激活项目（**目前已突破 173k+ Star**），它本质上是一组透明公开的脚本。
* 相比传统的 KMS 软件，它的优势无与伦比：

+ **完全开源透明**：你可以直接查看每一行代码，绝对安全无毒。
+ **不报毒**：由于不包含非法二进制文件，主流杀毒软件几乎不会误报。
+ **TSforge 新技术**：完美解决 Windows 10 停更（EOL）后的扩展安全更新激活。
+ **版本无忧**：无需重装，直接将家庭版无损升级为专业版（我的几台电脑都是用这玩意升级的）。

### 二、 实战：只需一条命令

**本方法不需要你下载任何压缩包，只需在电脑联网状态下运行一行指令即可唤出交互菜单。**

#### 步骤 1：打开 PowerShell

键盘 Win+R 调出运行框，然后输入以下指令打开 PowerShell（不要打开成 cmd 了）。

```
powershell
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/W2hHqUjyRk0pOJNBnfuhWhhF8HvsAAficulUn35KAyWcJOWv7xA7LhM8rpbPkKx8icgiaa0KEgkV350qt0Pdcd2WAf2wLQ5gU221t8fuGLSEWc/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/W2hHqUjyRk0HXp8QwcvjBkgdhbmbORtIMFO0vZknj5j4wT3YadTc6jAdfbk4XDs1yEnHXsSsiadx3pkat20a7SWI9NpxKVYhHeRRuUmrZjP0/640?wx_fmt=png&from=appmsg)

#### 步骤 2：输入并执行脚本命令

在 PowerShell 窗口中，直接复制并粘贴以下命令，然后按 **Enter（回车）** 键。

```
irm https://get.activated.win | iex
```

> **tips**：
>
> * 这句命令的作用是直接从 MAS 官方托管地址下载并执行脚本流。
> * 可能会出现无法解析域名的情况，请将电脑的 **DNS** 临时修改为 `8.8.8.8` 或 `114.114.114.114` 后重试。
> * 如果提示"未能创建 SSL/TLS 安全通道"，需要运行 `[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; irm https://get.activated.win | iex` 命令以开启安全传输协议。

![](https://mmbiz.qpic.cn/mmbiz_png/W2hHqUjyRk2VwxBVDOKcLwJKV8uSxDYrd8uR6O9COBMdMSOtApmY0MKCpXtxQlAFUzIx0AiaHD21wr03lVIPMWibr6QrPkLAL6lNX70x43QtA/640?wx_fmt=png&from=appmsg)

#### 步骤 3：根据交互菜单进行选择

稍等片刻（取决于你的网速）后就会弹出一个新的交互菜单。请根据你的需求输入对应的**数字**：

* **[1] HWID**：这是**最推荐**的方式。用于永久激活 Windows 10/11。它会将你的硬件信息上传到微软服务器，重装系统后只要联网也会自动激活。
* **[2] Ohook**：这是目前 **Office** 最完美的激活方式。不更改系统文件，直接利用 Office 内置逻辑实现永久激活。
* **[3] TSforge**：针对 Windows/Office 的新型激活方式，特别推荐用于开启 Win10 EOL 后的扩展更新支持。
* **[4] Online KMS**：在线 KMS 激活，有效期 180 天，支持设置自动续订任务。
* **[5] Check Activation Status**：随时查询当前系统和 Office 的激活剩余时间。
* **[8] Troubleshoot**：如果激活报错，选择这个进行一键修复。

![](https://mmbiz.qpic.cn/mmbiz_jpg/W2hHqUjyRk04M0vzicplFiawEp9MLE14sHDBPr7oOMiaGJA3f5Rfw7BSia1dDCUv8bLxOAg9oRgxGUNBAd4kIomzw55oHpODG4sR75iaiaAuOkEibo/640?wx_fmt=jpeg&from=appmsg)

#### 步骤 4：激活成功验证

输入数字后（比如 1），系统会自动进入开始激活的界面，等待片刻......当看到 **"Successful"** 或绿色成功提示时，说明激活已完成。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/W2hHqUjyRk1wRd1rEQ6O40f2OcUkaNg50AGMCDtMZzLhLpiawaAepj0LiaeXjdSAicYh5Mld1kbMEAeAU7PaRc3t4RTOhDicWP5piaUQNR2QUibbk/640?wx_fmt=jpeg&from=appmsg)

### 三、 进阶：如何升级专业版？

这是很多人最关心的功能，因为新买的电脑预装系统基本都是家庭版（Home），功能受限，升级操作如下：

1. **进入版本转换**：在主菜单直接按下 **[6]** 键（Change Windows Edition）。
2. **选择版本**：在弹出的子菜单中输入对应数字选择 Professional (专业版)。
3. **等待转换**：系统会自动安装专业版特征包并重启（过程不影响个人文件）。
4. **重新激活**：重启后系统就是专业版了，并且已激活。如果激活掉了，重新运行脚本并按 **[1]** 执行 HWID 永久激活即可。

### 四、 备选方案

如果有朋友还是想使用本地工具进行激活，这里提供一个我也在用的工具，按如下方法自取。

星标、点赞、转发、推荐一键四连，感谢支持

**关注公众号，聊天框发送消息"****win激活****"获取工具**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/A0oia22fd2WzSQnmezsVkg1uTsIJE6VWsg7n1qYzj5NQ8J3RM2FEIhXg6aAbjk4ibUISNYx7QKF6ic5xX0148TrBg/640?wx_fmt=gif)

**END**

**往期****精彩****回顾**

[墙裂推荐！！一键更换Linux优质的软件源和docker源，要多方便有多方便](http://mp.weixin.qq.com/s?__biz=MzkwOTU5Mjk5MA==&mid=2247484068&idx=1&sn=5148291a4ab17d5f2f4a5a748e025c7a&chksm=c1391255f64e9b431be5e8f583f61f5c784fce80c271c104f215d4c16d1f98756f22dcef4c59&scene=21#wechat_redirect)

[frp | 开源内网穿透利器，速速用起来](http://mp.weixin.qq.com/s?__biz=MzkwOTU5Mjk5MA==&mid=2247484042&idx=1&sn=255c5fe152d22c1f306b9d67700968ef&chksm=c139127bf64e9b6d3d492141b4df6490f9b39801f543397ca670dca2b1880f1e851074001a73&scene=21#wechat_redirect)

[大闹天宫 | 被安全社区誉为可以“黑掉整个宇宙”的神器-1](http://mp.weixin.qq.com/s?__biz=MzkwOTU5Mjk5MA==&mid=2247484269&idx=1&sn=89c229b2b23d190d6258ec953de099a8&chksm=c139139cf64e9a8a9fbcc492d0c3bf12b30a3f5c0570e5b14654fc46436da442bd6ea8aabbad&scene=21#wechat_redirect)

[Metasploit漏洞利用 | 被安全社区誉为可以“黑掉整个宇宙”的神器-2](http://mp.weixin.qq.com/s?__biz=MzkwOTU5Mjk5MA==&mid=2247484286&idx=1&sn=d5def061da282fefd601b4c5e1c2c004&chksm=c139138ff64e9a9963a1f52f222b3ff961f3c91a421e95d574a3ec5302b8b00a6a6bb4fffc86&scene=21#wechat_redirect)

[Metasploit木马生成 | 被安全社区誉为可以“黑掉整个宇宙”的神器-3](http://mp.weixin.qq.com/s?__biz=MzkwOTU5Mjk5MA==&mid=2247484322&idx=1&sn=48b7542fd2bb682a69580b2c1b0fbe4b&chksm=c1391353f64e9a45fad59242fb001c5333a16abde0d4d119d9fe8abbc949b5d92463b25313cd&scene=21#wechat_redirect)

[内网渗透 | MSF&FRP | 无法直接访问的目标如何通过搭建代理进一步渗透？](http://mp.weixin.qq.com/s?__biz=MzkwOTU5Mjk5MA==&mid=2247484396&idx=1&sn=8e5738bb18fe72c4d2cd9acab4d48590&chksm=c139131df64e9a0b23b06c62499955c81ae5fdeca4313580d89135ff0eeedbca08b1971b6f43&scene=21#wechat_redirect)

[目标网络限制严格CS拿不到权限怎么办？试试这个高级玩法—隧道上线](http://mp.weixin.qq.com/s?__biz=MzkwOTU5Mjk5MA==&mid=2247484582&idx=1&sn=2bf7793dc905f67de4f34e7bafbc4792&chksm=c1391457f64e9d412e163079f9ffa099bff668ba11533a30499599ed8197a7a3771a92c2d13b&scene=21#wechat_redirect)

[HVV | 记一次护网Webshell告警分析研判，真真假假](http://mp.weixin.qq.com/s?__biz=MzkwOTU5Mjk5MA==&mid=2247484909&idx=1&sn=405ef4c91618e264ba0ed16574d01e86&chksm=c139151cf64e9c0a3c256379a5d3cd1062d0029655700855bda8a2747981769dbc0d92b03315&scene=21#wechat_redirect)

[HVV | 记一次护网服务器被攻破的应急响应，有意思](http://mp.weixin.qq.com/s?__biz=MzkwOTU5Mjk5MA==&mid=2247484941&idx=1&sn=b791457517a1d0d8776fac03dec918b5&chksm=c13916fcf64e9fea8a6d8507873821477523ecaa1debb5a4c7d1fda348624a12591f8a1e3f3d&scene=21#wechat_redirect)

[有粉丝问：火绒剑下线了怎么办？注意！有办法但是有风险！](http://mp.weixin.qq.com/s?__biz=MzkwOTU5Mjk5MA==&mid=2247484998&idx=1&sn=a7712e589aec59dd244fbe88f9d3700b&chksm=c13916b7f64e9fa12e56f2df4b9cda1f9dbe6be214cb50fa74972c5131691967b27f240fcb9c&scene=21#wechat_redirect)

[Payload速查项目，我愿称它为网安字典](https://mp.weixin.qq.com/s?__biz=MzkwOTU5Mjk5MA==&mid=2247487113&idx=1&sn=8bd25a8f505ff213b090db01d6c862b3&scene=21#wechat_redirect)

**扫码关注**

渗透测试

信息安全

安全工具

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A0oia22fd2WyrAOlXqEIveZwbyvjHFSs52s4O3kbODcicXls4vO8G7WkaPhtFRWw7eUia2NjBpfEzactEz6KIJARg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/A0oia22fd2WzSQnmezsVkg1uTsIJE6VWseibCibicsibGEckS6ekQ48nCwemGSCIYBGUG1V8ia5BAQnql46JuEpJ0vBA/640?wx_fmt=gif)

学习视频戳“阅读原文”一起来充电吧!

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/A0oia22fd2WzkZ9SvSrZWGdLNXSiaQnekkiaFgHQ6Gmt4vGh2TxV9Nd3vt0AutmVFewrM7QWubBzuMNmYSZSjZ0pA/0?wx_fmt=png)

大伯为安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/A0oia22fd2WzkZ9SvSrZWGdLNXSiaQnekkiaFgHQ6Gmt4vGh2TxV9Nd3vt0AutmVFewrM7QWubBzuMNmYSZSjZ0pA/0?wx_fmt=png)

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