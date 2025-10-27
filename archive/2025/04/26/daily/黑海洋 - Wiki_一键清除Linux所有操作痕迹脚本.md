---
title: 一键清除Linux所有操作痕迹脚本
url: https://blog.upx8.com/4773
source: 黑海洋 - Wiki
date: 2025-04-26
fetch_date: 2025-10-06T22:06:37.639180
---

# 一键清除Linux所有操作痕迹脚本

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 一键清除Linux所有操作痕迹脚本

发布时间:
2025-04-25

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
90322

在 Linux 系统中，如果你想**彻底清除 root 登录历史记录、命令记录、临时缓存等，如IP地址**（包括 `/var/log/wtmp`、`/var/log/btmp` 和 `systemd-journald` 日志），可以按照以下方法操作：

### 一键清除Linux所有操作痕迹 - 脚本

```
bash <(wget -qO- https://raw.githubusercontent.com/hadis898/allscript/refs/heads/main/clear_all_logs.sh)
```

### ![](https://cdn.skyimg.net/up/2025/4/29/a088d6ad.webp)

选择`5`一键清理所有记录

![](https://cdn.skyimg.net/up/2025/4/29/02240916.webp)

完成后自动断开连接，不放心的话可以验证下。

**验证命令：**
`last`                             # 检查登录记录，加`root`参数就表示只查root
`history`                        # 检查命令历史
`journalctl -u sshd`       # 检查SSH日志
`ls -la /var/log/`          # 检查系统日志
`cat ~/.bash_history`     # 检查bash历史文件

---

**以下没需求可以不用看。**

## **手动操作**

## **1. 清除 `/var/log/wtmp`（成功登录记录）**

`wtmp` 文件存储了所有用户的登录历史，可以用 `last` 命令查看。
**清除方法**：

```
# 清空 wtmp 文件（所有登录记录）
sudo echo > /var/log/wtmp

# 验证是否清除成功
sudo last root  # 应该显示 "wtmp begins [空日期]"
```

## **2. 清除 `/var/log/btmp`（失败登录记录）**

`btmp` 文件存储了失败的登录尝试，可以用 `lastb` 命令查看。
**清除方法**：

```
# 清空 btmp 文件
sudo echo > /var/log/btmp

# 验证是否清除成功
sudo lastb root  # 应该显示 "btmp begins [空日期]"
```

## **3. 清除 `systemd-journald` 日志**

如果系统使用 `journald`（现代 Debian 默认），执行：

```
# 删除所有日志（慎用！）
sudo journalctl --flush --rotate
sudo rm -rf /var/log/journal/*
sudo systemctl restart systemd-journald

# 或者只删除 SSH 相关日志
sudo journalctl --vacuum-time=1s -u sshd
```

* `--vacuum-time=1s`：删除 1 秒前的日志（几乎全部清除）
* `-u sshd`：仅删除 SSH 日志

## **4. 清除 `/var/log/auth.log`（如果存在）**

如果系统使用 `rsyslog`，可能会有 `/var/log/auth.log`：

```
# 清空 auth.log
sudo echo > /var/log/auth.log

# 或者只删除 root 相关的记录
sudo sed -i '/root/d' /var/log/auth.log
```

## **5. 防止未来记录（可选）**

如果你希望**未来也不记录登录日志**，可以修改 SSH 配置：

```
sudo nano /etc/ssh/sshd_config
```

修改以下行：

```
LogLevel QUIET      # 关闭 SSH 日志
SyslogFacility AUTHPRIV
```

然后重启 SSH：

```
sudo systemctl restart sshd
```

## **6. 检查是否清除干净**

```
# 检查 wtmp/btmp
sudo last root
sudo lastb root

# 检查 journald 日志
sudo journalctl -u sshd _UID=0

# 检查 auth.log（如果存在）
sudo grep "root" /var/log/auth.log
```

如果返回**空结果或无记录**，说明清除成功。

## **⚠️ 注意事项**

1. **审计合规性**：在生产环境中，清除日志可能违反安全政策或法律要求。
2. **临时文件**：某些工具（如 `logrotate`）可能会备份日志，检查 `/var/log/` 下是否有 `*.gz` 或 `*.old` 文件。
3. **内存日志**：`systemd-journald` 可能会缓存部分日志在内存，重启后才会完全清除。

### **总结**

| 文件/日志 | 清除方法 | 验证命令 |
| --- | --- | --- |
| `/var/log/wtmp` | `sudo echo > /var/log/wtmp` | `last root` |
| `/var/log/btmp` | `sudo echo > /var/log/btmp` | `lastb root` |
| `journald` | `sudo journalctl --vacuum-time=1s` | `journalctl -u sshd` |
| `/var/log/auth.log` | `sudo echo > /var/log/auth.log` | `grep "root" auth.log` |

如果你需要**完全隐身**，建议：

1. 清除上述所有日志。
2. 修改 SSH 配置关闭日志。
3. 重启服务器确保内存日志也被清除。

### **注意事项：**

请勿非法用途，仅供研究。

1. ![米姆米姆](//q2.qlogo.cn/headimg_dl?dst_uin=669155&spec=100)

   **米姆米姆**

   2025-05-23 21:26:07

   [回复](https://blog.upx8.com/4773/comment-page-1?replyTo=30603#respond-post-4773)

   谢谢大佬
2. ![1076769966](//q2.qlogo.cn/headimg_dl?dst_uin=1076769966&spec=100)

   **1076769966**

   2025-05-02 18:06:43

   [回复](https://blog.upx8.com/4773/comment-page-1?replyTo=30582#respond-post-4773)

   牛皮啊
3. ![NetDemon](//q2.qlogo.cn/headimg_dl?dst_uin=108666&spec=100)

   **NetDemon**

   2025-04-28 11:03:17

   [回复](https://blog.upx8.com/4773/comment-page-1?replyTo=30576#respond-post-4773)

   伸手了，谢谢

[取消回复](https://blog.upx8.com/4773#respond-post-4773)

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