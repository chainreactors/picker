---
title: Linux 搭建 KMS 服务器
url: https://blog.upx8.com/3179
source: 黑海洋 - WIKI
date: 2023-01-16
fetch_date: 2025-10-04T03:59:51.897946
---

# Linux 搭建 KMS 服务器

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux 搭建 KMS 服务器

发布时间:
2023-01-15

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
17504

# 下载 [vlmcsd](https://blog.upx8.com/go/dHRwczovL2dpdGh1Yi5jb20vV2luZDQvdmxtY3NkLw)

下载文件并解压，把 `binaries\Linux\intel\static\` 下的 `vlmcsd-x64-musl-static` 上传至 VPS`/usr/bin/` 目录下，并改名为 `vlmcsd`。

# 给予执行权限

```
chmod +x /usr/bin/vlmcsd
```

# 开启KMS服务

```
/usr/bin/vlmcsd
```

默认为 1688 端口，激活时无需输入端口号。如需更为其他端口，可以像下面这样：

```
/usr/bin/vlmcsd -L 0.0.0.0:2333
```

> 据说改了端口不容易被发现。

# 防火墙开放端口

个人习惯使用 De­bian 系统，使用 UFW 管理防火墙。

```
ufw allow 1688/tcp
ufw reload
```

如果你想了解如何使用 UFW ，可以查看 [Debian/Ubuntu安装和配置 UFW](https://blog.upx8.com/3180) 这篇文章。

# 设置开机启动

```
vim /etc/rc.local
```

如果你不需要修改端口就直接加入 `/usr/bin/vlmcsd`

需要修改端口就加入 `/usr/bin/vlmcsd -L 0.0.0.0:2333`（2333 改为自己想设定的端口即可。）

# 测试 KMS 服务器

在解压的文件中进入到 `binaries\Windows\intel\` 这个路径中，打开 cmd，把 `vlmcs-Windows-x64.exe` 拖进去，在后面输入刚刚部署好的 KMS 服务器的 IP。

返回信息显示 `successful`，就说明 KMS 服务器可用。

[取消回复](https://blog.upx8.com/3179#respond-post-3179)

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