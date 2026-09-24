---
title: GaGaSpeedVaultBox，一个把保险箱钥匙只交给你的开源密码管理器
url: https://mp.weixin.qq.com/s/NIEmXvfWid-cjC1pBWJwYw
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:05:54.280763
---

# GaGaSpeedVaultBox，一个把保险箱钥匙只交给你的开源密码管理器

# GaGaSpeedVaultBox，一个把保险箱钥匙只交给你的开源密码管理器

原创

李逍遥
李逍遥

SPEEDCoding

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

GZH WORKBENCH

GaGaSpeedVaultBox，一个把保险箱钥匙只交给你的开源密码管理器

导读 · CONTENTS

01一、它是什么？

02二、为什么值得你试试？

03三、功能截图

01

一、它是什么？

SECTION

**GaGaSpeedVaultBox** 是一款**本地优先、端到端加密**的桌面保险箱（密码管理器），以开源形式发布 v0.1.0 版本。

它和市面上大多数"云端密码管理器"有一个本质区别：

POINT 1🔐 **你的数据只存在你自己的设备上**；

POINT 2🔑 **主密码永远不会离开设备**；

POINT 3📖 **代码完全开源**。

用一句话概括：**你的秘密，只属于你。**

02

二、为什么值得你试试？

SECTION

**1. 真正的本地加密，不是口号**

POINT 1采用 **AES-256-GCM** 认证加密，密钥由主密码通过 **Argon2id**（抗暴力破解的顶级密钥派生算法）生成；

POINT 2所有数据以密文形式存放在本地 SQLite 数据库中；

POINT 3主密码丢失且未设置恢复问题时，**任何人都无法恢复**。

**2. 功能够用，且免费开源**

POINT 1✅ 初始化保险箱、解锁 / 一键锁定 / 闲置自动锁定

POINT 2✅ 账号条目的增、删、改、查，一键复制

POINT 3✅ 修改主密码（容器整体重加密，数据不丢失）

POINT 4✅ 忘记密码？预设恢复问题即可重包保险箱

POINT 5✅ 关闭应用前自动落盘，不怕丢数据

POINT 6✅ 可选的**自建服务器同步**——数据全程密文传输，服务器只存"看不懂的密文"

**3. 无广告、无追踪、无套路**

不嵌入任何统计、广告、崩溃上报组件。不收集、不上传、不出售任何个人信息。

03

三、功能截图

SECTION

以下为界面预览：

**▶ 初始化向导：选择「仅本地」或「自建服务器同步」模式**

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4Zic6aEEhic6Tibot8Vhbvh9DnJM1sYGanJx7Yiaeo3PQNnhkzWsGgoVY1rG17f8CGhib6YJ2o3Q0IbIhOwt2t5B4TdpicKqF3WIGBia0/640?wx_fmt=png&from=appmsg)

**▶ 解锁界面：主密码输入 + 恢复入口**

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4buoo8MVaiaUsWuwEWnt2ZmyUmiaCJiadZ6FxgOTZzFLYES3Qn7VTXibLBpoALyb9YBlSetVUfZGC33okhrUzoMibKRBZoCBS2lmhmk/640?wx_fmt=png&from=appmsg)

**▶ 保险箱主页：条目列表、搜索、一键复制**

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4b3j0tP2ve960h7nhSyZhkgUyxvjQwa6gNNmic2HysJibNibMcyNoCg5ur9n3YIB4FdoR9GM1nEU6sczP8oBicqiciaArlB0q3ukHHqE/640?wx_fmt=png&from=appmsg)

**▶ 设置页：自动锁定、修改主密码、同步管理、关于**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aAtnic7raQxLFh3iaEzm9OvgKqoCU5KWLOHnBAlk2ibrmFMO1iciaiapqqJs59ze8IMNBoEibWttJq5oEt7diaxHdPPQBvnoHk4hSx2HM/640?wx_fmt=png&from=appmsg)

04

四、如何获取？

SECTION

渠道 · 地址

渠道🌐 官网下载

地址(https://www.speedforensic.cn/resource-center/tool/96)

渠道🐙 GitHub 仓库（开源 / 提 Issue）

地址(https://github.com/ShinLee666/GaGaSpeedVaultBox)

支持 **Windows x64**（macOS / Linux 可参照 README 自行编译）。

**安装提示**：首次启动请设置主密码并牢记，或设置好恢复问题——主密码无法找回，这是安全设计的代价，也是承诺。

∞

五、写在最后

FINAL WORDS

GaGaSpeedVaultBox 刚刚发布 v0.1.0，还有很多功能在规划中（浏览器插件、移动端、更多条目类型……）。如果你喜欢：

POINT 1👉 到 GitHub 给我们一颗 **Star**，这是对我们最大的鼓励；

POINT 2👉 遇到问题或有好想法，随时提 Issue；

POINT 3👉 欢迎开发者参与共建，让隐私工具变得更好。

*VaultBox · 本地优先的端到端加密保险箱 · MIT 开源协议 · v0.1.0*

如果觉得有用，欢迎点赞、在看、转发三连。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ubxw8wJEYdluKbaN4LDwroa6C5W8flqTtNkiaZBpt9ibcVXJTlDmAHJHcR5TBR7AREPYETB3XUJF6v692P7GaD5A/0?wx_fmt=png)

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