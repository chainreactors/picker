---
title: 离线不上传，敏感文档拖一下就转 - Filee
url: https://mp.weixin.qq.com/s/6k75DKu20NZJOy173HTMgQ
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:39:47.459031
---

# 离线不上传，敏感文档拖一下就转 - Filee

# 离线不上传，敏感文档拖一下就转 - Filee

GSDK
GSDK

GSDK安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

安全人的工具箱 · 专挑那些"少传一次文件就少一次风险"的工具

你有没有遇到过这种场景：

`手上一份内部文档要转格式，公司明文禁止往外传；
客户发来的 HWP、报告里的截图，传在线转换站怕留痕；
应急取证材料要转 PDF 归档，又不能碰外网；
转换站免费是免费，但谁知道文件在服务器上躺多久。`

装软件、开窗口、上传、下载……一套流程下来十分钟就没了，还平白多了一次数据外泄的风险。

01一句话定位

**它不是又一个在线转换网站，而是把转换能力装进你鼠标指针的本地工具——文件从头到尾不离开你的电脑。**

按住一个快捷键，把文件拖过去，光标旁边会弹出一圈格式菜单，只显示这个文件能转的格式。松手，转换完成，结果就放在原文件旁边。全程离线、不上传，也不依赖 Office。

项目地址：

`https://github.com/KnifeLemon/Filee`

![Filee 主界面：拖放区与最近转换](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA19NflxL7V5n0pnicaSqNmgVrkBSPRIUZZJuIhH2CRk1CXlQ7NLpguBrxbN2uRVnGyjFBavm5ckxyksWGxRXiaIEUAkEUVx7ZP9m0/640?from=appmsg)

Filee 主界面：拖放区与最近转换

02核心亮点

🛡️ 全程离线，文件不上传

处理内部文档、敏感截图、客户资料，最怕的就是"传上去容易、撤回来难"。Filee 的转换全程在本机完成，文件不离开电脑，结果保存在原文件旁边。可选引擎（Ghostscript、LibreOffice、FFmpeg 等）只在需要时下载，还带固定 SHA-256 校验。

🍩 甜甜圈菜单，就在光标处

不用打开任何应用窗口。按住键、拖文件、丢到格式上，三步完成。菜单只显示当前文件"能转的"格式，不用在一长串列表里翻找。

🌐 浏览器里直接拖

从 Chrome、Edge、Firefox、Safari 拖入图片、链接或下载项就能转。链接下载不带你的浏览器登录态，不用担心私密页面被"顺手"读取。

⚙️ 一类文件，一套工具栏

每种文件类型有独立的甜甜圈，可拖拽排序。预设里能调质量、尺寸、DPI、PDF 页面与压缩、音视频参数、输出目录，还能从预设库直接装别人分享的配置。

🔁 多步转换，自动规划

像 HWP → HWPX → DOCX 这种需要绕一圈的路线，Filee 自己找出来，你不用手动中转。

📂 批量并行 + 文件夹监听

一次拖一堆文件并行处理；开启文件夹监听后，任何落进目录的新文件都会自动转好。

![可自定义排列的甜甜圈工具栏](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA18ECYTJtgbHX45TTqK3uIC6yQZwzWxqoKXFCFTaLo0OTr0SECs0onheoRJ5euthfibsX9tPA8iaCUhTUCibaWSrjRSB5YcmHPBJx4/640?from=appmsg)

可自定义排列的甜甜圈工具栏

03上手指南

Windows 用户，一行命令装好：

`winget install KnifeLemon.Filee`

装完就能用：**按住快捷键 → 拖文件 → 选格式**。想批量处理，命令行也支持：

`filee convert *.png --to webp --quality 80 -o converted`

macOS 13+ 和 Linux x64/ARM64 也有安装包（Linux 拖拽手势需要 X11）。底层是 **C# / .NET 10 / Avalonia 12**，MIT 协议开源，代码可自行审计。

04谁最该装

`需要处理内部文档、敏感截图，又不能往外传的安全从业者；
做应急响应、取证归档，要求文件全程不离本机的人；
经常和 PDF、Office 文档、HWP、电子书、字幕、CAD 打交道的人；
对数据外泄敏感、不敢用在线转换站的人。`

**一句话概括：离线、不上传，270 种格式拖一下就在本机转完——敏感文件从此不用出内网。**

⚠️ **免责声明**

注：工具仅供安全研究与学习之用，若将工具做其他用途，由使用者承担全部法律及连带责任，作者及发布者不承担任何法律及连带责任。信息及工具收集于互联网，真实性及安全性自测！！

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Xu1xJEZRrFjUe1HmsusbqLJiaQvscUlHp1kgYagMRTFy1TyiaryxmOjvkpS6UKic5ricVOjdicibiaLMTibKkUqiafYD8vw/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过