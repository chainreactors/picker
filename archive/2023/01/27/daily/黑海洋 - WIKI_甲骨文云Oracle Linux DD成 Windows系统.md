---
title: 甲骨文云Oracle Linux DD成 Windows系统
url: https://blog.upx8.com/3201
source: 黑海洋 - WIKI
date: 2023-01-27
fetch_date: 2025-10-04T04:58:48.336325
---

# 甲骨文云Oracle Linux DD成 Windows系统

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 甲骨文云Oracle Linux DD成 Windows系统

发布时间:
2023-01-27

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
19630

ADM尝试 别用 ARM

**更新组件**

```
apt update -y && apt install -y curl && apt install -y socat && apt install wget -y
```

**依赖**

```
apt-get install -y xz-utils openssl gawk file
```

**代码安装**

### DD Windows Server 2012 R2 64位 精简版 [账户Administrator密码nat.ee]

```
wget --no-check-certificate -qO InstallNET.sh 'https://moeclub.org/attachment/LinuxShell/InstallNET.sh' && bash InstallNET.sh -dd 'https://oss.sunpma.com/Windows/Oracle_Win_Server2012R2_64_Administrator_nat.ee.gz'
```

### DD Windows7 sp1 64位 企业精简版 [账户Administrator密码nat.ee]

```
wget --no-check-certificate -qO InstallNET.sh 'https://moeclub.org/attachment/LinuxShell/InstallNET.sh' && bash InstallNET.sh -dd 'https://oss.sunpma.com/Windows/Oracle_Win7_sp1_64_Administrator_nat.ee.gz'
```

**# DD Windows10 2021LTSC 64位 企业深度精简版 [账户Administrator密码nat.ee]**

```
wget --no-check-certificate -qO InstallNET.sh 'https://sunpma.com/other/oss/InstallNET.sh' && bash InstallNET.sh -dd 'https://oss.sunpma.com/Windows/Oracle_Win10_2021LTSC_64_Administrator_nat.ee.gz'
```

**#等30分钟左右，ping3389看看通了没：[https://tcp.ping.pe/](https://blog.upx8.com/go/aHR0cHM6Ly90Y3AucGluZy5wZS8)**

[![甲骨文云 DD成Windows](https://alay.cc/wp-content/uploads/2022/11/%E7%94%B2%E9%AA%A8%E6%96%87%E4%BA%91-dd%E6%88%90windows.png)](https://alay.cc/wp-content/uploads/2022/11/%E7%94%B2%E9%AA%A8%E6%96%87%E4%BA%91-dd%E6%88%90windows.png)

**#系统下载（自行更换系统地址）：**[https://oss.sunpma.com/?Windows](https://blog.upx8.com/go/aHR0cHM6Ly9vc3Muc3VucG1hLmNvbS8_V2luZG93cw)

[取消回复](https://blog.upx8.com/3201#respond-post-3201)

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