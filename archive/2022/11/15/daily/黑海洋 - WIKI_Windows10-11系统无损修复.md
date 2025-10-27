---
title: Windows10-11系统无损修复
url: https://blog.upx8.com/3089
source: 黑海洋 - WIKI
date: 2022-11-15
fetch_date: 2025-10-03T22:45:49.383737
---

# Windows10-11系统无损修复

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Windows10-11系统无损修复

发布时间:
2022-11-14

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
37015

# **基础介绍**

**什么是无损修复？使用 ISO 文件 无损修复 Windows 11 系统**

无损修复（也称为 **原地升级** 或 **就地升级**）允许你重新安装Windows，保留应用程序文件和设置。它可以修复各种各样的问题，包括Windows更新错误，包括下载和更新的商店应用程序问题，或不可靠的窗口，如速度慢或崩溃。无损修复 在修复这些问题方面有很高的成功率，而不需要做重置，删除你现有的应用程序的麻烦。

**无损修复的注意事项**

对于无损修复，您需要注意以下 三件事：

1. 你的系统盘可能需要 15-20G 的可用空间（与升级到 Windows 11类似），修复过程可能随个人情况长达数小时（一般为1-2小时），敬请稍安勿躁；
2. 经过我的测试，这个方法不会对已安装的程序和个人文件造成影响，但是为了最大限度地安全起见，仍然建议你再开始之前**备份**您的必要资料。
3. 必须是能正常进入系统的 Windows 11 (仅限 家庭版 和 专业版)，如果您的 PC 卡在引导循环中或重新启动到安全模式，则无法进行。

**准备阶段（第一阶段）**

首先，从以下链接下载 Windows 11 ISO 文件 （**推荐使用 方法 3**

**方法 1**

进入这个页面 [Download Windows 11 (microsoft.com)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cubWljcm9zb2Z0LmNvbS96aC1jbi9zb2Z0d2FyZS1kb3dubG9hZC93aW5kb3dzMTE)

在 下载 Windows 11 磁盘映像 (ISO) 下，选择 Windows 11，单击 "下载" 并选择 "Windows" 的安装语言，单击 64 位下载以开始下载。

[![图片](https://filestore.community.support.microsoft.com/api/images/7302dad4-e5eb-4575-bd32-343d7dbf5cdb?upload=true)](https://blog.upx8.com/go/aHR0cHM6Ly9maWxlc3RvcmUuY29tbXVuaXR5LnN1cHBvcnQubWljcm9zb2Z0LmNvbS9hcGkvaW1hZ2VzLzczMDJkYWQ0LWU1ZWItNDU3NS1iZDMyLTM0M2Q3ZGJmNWNkYj91cGxvYWQ9dHJ1ZQ)

修改日期 2022年3月10日17点26分

**~~方法 2~~**

~~如果你嫌官网下的太慢 又碰巧 不是家庭中文版 的，你可以通过下面的百度云分享链接进行下载（虽然可能更慢就是了）~~

~~百度云分享链接：~~[~~https://pan.baidu.com/s/10id584ruTDWO\_VYGbql3uA~~](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4uYmFpZHUuY29tL3MvMTBpZDU4NHJ1VERXT19WWUdicWwzdUE) ~~提取码：nq4v~~

[![图片](https://filestore.community.support.microsoft.com/api/images/e09a2938-0f38-4352-a9d7-b958b320d012?upload=true)](https://blog.upx8.com/go/aHR0cHM6Ly9maWxlc3RvcmUuY29tbXVuaXR5LnN1cHBvcnQubWljcm9zb2Z0LmNvbS9hcGkvaW1hZ2VzL2UwOWEyOTM4LTBmMzgtNDM1Mi1hOWQ3LWI5NThiMzIwZDAxMj91cGxvYWQ9dHJ1ZQ)

**方法 3**

使用 Media Creation Tool 媒体创建工具 来创建一个 ISO 镜像

进入这个页面 [Download Windows 11 (microsoft.com)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cubWljcm9zb2Z0LmNvbS96aC1jbi9zb2Z0d2FyZS1kb3dubG9hZC93aW5kb3dzMTE)

点击 "立即下载工具"

[![图片](https://filestore.community.support.microsoft.com/api/images/8ff5eb3d-54f3-409c-aaae-2bd676dd258d?upload=true)](https://blog.upx8.com/go/aHR0cHM6Ly9maWxlc3RvcmUuY29tbXVuaXR5LnN1cHBvcnQubWljcm9zb2Z0LmNvbS9hcGkvaW1hZ2VzLzhmZjVlYjNkLTU0ZjMtNDA5Yy1hYWFlLTJiZDY3NmRkMjU4ZD91cGxvYWQ9dHJ1ZQ)

打开它并且选择 ISO 文件

[![图片](https://filestore.community.support.microsoft.com/api/images/c438d6a7-3149-4f42-9106-705f79c84396?upload=true)](https://blog.upx8.com/go/aHR0cHM6Ly9maWxlc3RvcmUuY29tbXVuaXR5LnN1cHBvcnQubWljcm9zb2Z0LmNvbS9hcGkvaW1hZ2VzL2M0MzhkNmE3LTMxNDktNGY0Mi05MTA2LTcwNWY3OWM4NDM5Nj91cGxvYWQ9dHJ1ZQ)

**修复阶段（第二阶段）**

当 ISO 文件下载完成之后，双击打开它，并运行 setup.exe

[![图片](https://filestore.community.support.microsoft.com/api/images/78f4efe0-2e68-4a35-9ef2-5c02ebaea1f4?upload=true)](https://blog.upx8.com/go/aHR0cHM6Ly9maWxlc3RvcmUuY29tbXVuaXR5LnN1cHBvcnQubWljcm9zb2Z0LmNvbS9hcGkvaW1hZ2VzLzc4ZjRlZmUwLTJlNjgtNGEzNS05ZWYyLTVjMDJlYmFlYTFmND91cGxvYWQ9dHJ1ZQ)

打开之后 这里选择 更改安装程序下载的更新方式 ，

[![图片](https://filestore.community.support.microsoft.com/api/images/65448363-69f2-41ad-a1e3-5ee5a56ff0ab?upload=true)](https://blog.upx8.com/go/aHR0cHM6Ly9maWxlc3RvcmUuY29tbXVuaXR5LnN1cHBvcnQubWljcm9zb2Z0LmNvbS9hcGkvaW1hZ2VzLzY1NDQ4MzYzLTY5ZjItNDFhZC1hMWUzLTVlZTVhNTZmZjBhYj91cGxvYWQ9dHJ1ZQ)

然后勾选 "不是现在" 再点击下一页

[![图片](https://filestore.community.support.microsoft.com/api/images/d9f3828f-ba44-40ad-ad3b-822b13363b2f?upload=true)](https://blog.upx8.com/go/aHR0cHM6Ly9maWxlc3RvcmUuY29tbXVuaXR5LnN1cHBvcnQubWljcm9zb2Z0LmNvbS9hcGkvaW1hZ2VzL2Q5ZjM4MjhmLWJhNDQtNDBhZC1hZDNiLTgyMmIxMzM2M2IyZj91cGxvYWQ9dHJ1ZQ)

接受许可条款

[![图片](https://filestore.community.support.microsoft.com/api/images/429fae57-c0a3-4c24-ad83-3f5c15398913?upload=true)](https://blog.upx8.com/go/aHR0cHM6Ly9maWxlc3RvcmUuY29tbXVuaXR5LnN1cHBvcnQubWljcm9zb2Z0LmNvbS9hcGkvaW1hZ2VzLzQyOWZhZTU3LWMwYTMtNGMyNC1hZDgzLTNmNWMxNTM5ODkxMz91cGxvYWQ9dHJ1ZQ)

下一步 确认 你的文件、应用程序。设置被保留。它还会向你显示它要安装的 Windows 版本。

**如果出现需要您输入密钥的话，就说明你下载的 ISO 与您当前的系统版本并不相符。**

[![图片](https://filestore.community.support.microsoft.com/api/images/2f9758ea-7d45-4c0c-8ced-3e6a1da2d593?upload=true)](https://blog.upx8.com/go/aHR0cHM6Ly9maWxlc3RvcmUuY29tbXVuaXR5LnN1cHBvcnQubWljcm9zb2Z0LmNvbS9hcGkvaW1hZ2VzLzJmOTc1OGVhLTdkNDUtNGMwYy04Y2VkLTNlNmExZGEyZDU5Mz91cGxvYWQ9dHJ1ZQ)

如果你需要删除应用 并重新 安装 Windows，请单击 "更改要保留的内容" 并选择适合你的一项 然后单击下一页

[![图片](https://filestore.community.support.microsoft.com/api/images/4a6d2b4f-a999-4b2b-8b28-32857e4efef8?upload=true)](https://blog.upx8.com/go/aHR0cHM6Ly9maWxlc3RvcmUuY29tbXVuaXR5LnN1cHBvcnQubWljcm9zb2Z0LmNvbS9hcGkvaW1hZ2VzLzRhNmQyYjRmLWE5OTktNGIyYi04YjI4LTMyODU3ZTRlZmVmOD91cGxvYWQ9dHJ1ZQ)

点击安装就可以开始 进行 无损修复了

不是精简版的可以用（[FixWin 11(Win11系统修复工具) V11](https://blog.upx8.com/go/aHR0cHM6Ly9tLnhpdG9uZ3poaWppYS5uZXQvc29mdC8yNDYzNzcuaHRtbA)）：https://m.xitongzhijia.net/soft/246377.html

[取消回复](https://blog.upx8.com/3089#respond-post-3089)

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