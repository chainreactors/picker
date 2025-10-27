---
title: QQ截图工具独立版
url: https://blog.upx8.com/3316
source: 黑海洋 - WIKI
date: 2023-03-21
fetch_date: 2025-10-04T10:09:09.936788
---

# QQ截图工具独立版

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# QQ截图工具独立版

发布时间:
2023-03-20

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
65305

![](https://img.776161.xyz/img/20230320/3859486794.png)

QQ 和微信都自带截图功能，但相比之下，**QQ 的截图工具比微信要强大不少****。**
先来对比下微信和 QQ 自带的截图工具
从工具栏的对比也能看出 QQ 的要比微信功能更多，不仅包含了常用的框选，标注，还有其他几个超强的功能。 **有大佬把 QQ 截图工具单独从 QQ 中提取了出来，做成了独立版。无需 QQ 就能使用。**

**1. 文字提取功能**

截图后点击工具栏上的这个图标：

就可以**轻而易举把图像里的文字等信息提取出来**。准确率相当高。

从图中可以看到非常轻松就提取出来了，还标识了识别出文字的位置。
**2. 图片识别功能**截图后点击工具栏的这个图标：

**原本是翻译功能，提取版将翻译功能改成了图片识别功能。可以调用百度搜图搜索相似的图片**。
这里小编在 B 站找个视频片段截图，可以轻松找到类似的图片。

**3. 截长图功能**

截图后点击工具栏的这个图标：

选择截图区域后，滚动鼠标滑轮，会自动拼接成长图，超级实用

软件为绿色版，解压后点击 init.bat 会自动创建个快捷方式，点击后即可直接使用。
希望有一天，微信截图也能支持这几个功能。

#### 使用说明

运行 Init.bat 创建桌面快捷方式 (或者主程序是 Bin\QQScreenShot.exe, 自己手动运行)
单击托盘图标，或默认使用快捷键 Ctrl+Alt+A 截图

功能:

1. 滚轮音量功能开启后，鼠标放到任务栏最下面可以通过滚动鼠标中键控制系统总音量大小 (win7/win10 下测试可用)
2. 默认不再使用 PaddleOCR, 如有需要，请自行下载并解压，
   下载链接:
   链接：https://pan.baidu.com/s/1yENiFF3KDdZTDfqig6X98A
   提取码：oa7c

下载 ocr\_system.zip 后解压到 Bin\ocr\_system 文件夹下，然后 右键托盘图标 -> 切换 OCR 引擎 -> 选择 PaddleOCR -> 确定 即可

---

更新事项 (v2.4.1):

1. 修复了获取 PaddleOCR 结果长度为 0 时构造字符串导致崩溃

---

更新事项 (v2.4):

1. 新增” 切换 OCR 引擎” 功能 (可以使用 QQ 自带的 OCR 识别啦！，逆向的时候发现其实是可以本地调用 QQ 的 OCR 的)
2. “切换热键” 功能改成了选择组合键的方式
3. 消息提醒不再使用托盘气泡，全面改成用 QQ 的 dll 中的 ShowResultTipsWin 函数实现
4. PaddleOCR 改成了线程中获取 OCR 结果，不会再有卡顿了 (PaddleOCR 默认不再集成，请查看第 0x3 节在网盘里自行下载并解压)

---

更新事项 (v2.3):

1. 修复百度识图问题 (百度识图不再接受 HTTP 的 POST 请求，修复为用 libcurl 发送 HTTPS 的 POST 请求)
2. 点击 OCR 按钮后不再需要手动关闭截图
3. 增加” 切换热键” 功能，共 Ctrl+Alt+A/Ctrl+Q/Ctrl+Shift+A 三种热键
4. 增加” 滚轮音量” 功能，可以通过在任务栏底部滑动鼠标滚轮来控制系统音量大小

---

下载地址：[https://wwtc.lanzoum.com/iwqpG0qn1jpa](https://blog.upx8.com/go/aHR0cHM6Ly93d3RjLmxhbnpvdW0uY29tL2l3cXBHMHFuMWpwYQ)

1. ![崔](//q2.qlogo.cn/headimg_dl?dst_uin=4217508&spec=100)

   **崔**

   2023-07-07 16:50:46

   [回复](https://blog.upx8.com/3316/comment-page-1?replyTo=27338#respond-post-3316)

   感谢分享

[取消回复](https://blog.upx8.com/3316#respond-post-3316)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")