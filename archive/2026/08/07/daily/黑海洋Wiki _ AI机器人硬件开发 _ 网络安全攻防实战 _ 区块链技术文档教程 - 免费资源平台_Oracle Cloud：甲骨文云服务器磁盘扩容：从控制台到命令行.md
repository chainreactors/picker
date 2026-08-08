---
title: Oracle Cloud：甲骨文云服务器磁盘扩容：从控制台到命令行
url: https://blog.upx8.com/Oracle-Cloud
source: 黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-08-07
fetch_date: 2026-08-08T03:23:59.282459
---

# Oracle Cloud：甲骨文云服务器磁盘扩容：从控制台到命令行

# [黑海洋 | Wiki](/ "黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# Oracle Cloud：甲骨文云服务器磁盘扩容：从控制台到命令行

发布时间:
2026-08-07 New Article

分类:
[共享资源/Free](https://blog.upx8.com/Free)

热度:
3349

![Oracle Cloud：甲骨文云服务器磁盘扩容：从控制台到命令行](https://cdn.skyimg.net/up/2026/8/7/2602f9bd.webp)

#### Oracle Cloud 引导卷（Boot Volume）在线扩容完整教程

本教程适用于 **Ubuntu/Debian** 系统，全程无需重启。

---

## 一、准备工作

登录实例，确认当前状态：

```
# 查看磁盘分区情况
lsblk

# 查看根分区使用情况和文件系统类型
df -h /
df -T /
```

---

## 二、OCI 控制台操作

1. 登录 **Oracle Cloud 控制台**
2. 进入：**Block Storage** → **Boot Volumes**
3. 找到对应实例的引导卷
4. 点击 **Edit**，输入更大的容量（只能扩不能缩）
5. 点击 **Save Changes** 保存

---

## 三、Linux 实例内手动扩容（通用方法）

### 第 1 步：安装必要工具

```
sudo apt-get update
sudo apt-get install cloud-guest-utils -y
```

### 第 2 步：刷新磁盘信息

让系统识别到新大小：

```
echo "1" | sudo tee /sys/class/block/sda/device/rescan
```

然后用 `lsblk` 确认磁盘总大小已更新。

### 第 3 步：扩展分区

```
sudo growpart /dev/sda 2
```

* 如果输出 `CHANGED: partition=2 ...`，说明分区已扩展
* 如果输出 `NOCHANGE: partition 2 is size xxx. it cannot be grown`，说明分区已经最大，**跳过此步**（你遇到的就是这个情况）

### 第 4 步：扩展文件系统

根据文件系统类型执行对应命令：

```
# ext4（最常见）
sudo resize2fs /dev/sda2

# 如果是 xfs
sudo xfs_growfs /
```

### 第 5 步：验证扩容结果

```
df -h /
```

现在根分区应该显示为新的大小了。

---

## 四、完整命令速查（复制粘贴版）

```
# 安装工具
sudo apt-get update && sudo apt-get install cloud-guest-utils -y

# 刷新磁盘
echo "1" | sudo tee /sys/class/block/sda/device/rescan

# 扩展分区（如果提示 NOCHANGE 就跳过）
sudo growpart /dev/sda 2

# 扩展文件系统（ext4）
sudo resize2fs /dev/sda2

# 验证
df -h /
```

---

## 五、常见问题

| 问题 | 解决方法 |
| --- | --- |
| `growpart: command not found` | `sudo apt-get install cloud-guest-utils -y` |
| `NOCHANGE: partition cannot be grown` | 分区已最大，直接执行 `resize2fs` |
| `resize2fs: Device or resource busy` | 正常提示，不影响扩容 |
| 文件系统是 xfs | 用 `xfs_growfs /` 代替 `resize2fs` |
| 需要重启吗？ | **不需要**，在线操作即可 |

[取消回复](https://blog.upx8.com/Oracle-Cloud#respond-post-9965)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [All](/all.html)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [便签](https://txt.upx8.com)
* [关于](/about.html)

[![又拍云赞助商](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2026 黑海洋. All rights reserved. [看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")