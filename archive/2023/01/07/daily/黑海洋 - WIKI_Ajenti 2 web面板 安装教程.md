---
title: Ajenti 2 web面板 安装教程
url: https://blog.upx8.com/3165
source: 黑海洋 - WIKI
date: 2023-01-07
fetch_date: 2025-10-04T03:15:47.103176
---

# Ajenti 2 web面板 安装教程

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Ajenti 2 web面板 安装教程

发布时间:
2023-01-06

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
15207

# ![](//imgsrc.baidu.com/imgad/pic/item/81cb39dbb6fd5266717efed0ee18972bd5073699.jpg)

# 安装

官网：[http://docs.ajenti.org/en/latest/man/install.html](https://blog.upx8.com/go/aHR0cDovL2RvY3MuYWplbnRpLm9yZy9lbi9sYXRlc3QvbWFuL2luc3RhbGwuaHRtbA)

github：[https://github.com/ajenti/ajenti](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2FqZW50aS9hamVudGk)

相关教程：[https://wzfou.com/ajenti/](https://blog.upx8.com/go/aHR0cHM6Ly93emZvdS5jb20vYWplbnRpLw)

支持的操作系统：

* Debian 9 或更高版本
* Ubuntu 仿生或更高版本
* RHEL 8 或更高版本

其他基于 Linux 的系统*可能也*可以，但您必须使用手动安装方法。

## 自动安装

```
curl https://raw.githubusercontent.com/ajenti/ajenti/master/scripts/install.sh | sudo bash -s -
```

## 虚拟环境自动安装

请注意，此安装方法仍在测试中。Ajenti 在前面提到的支持的操作系统上成功启动，但所有功能都没有经过测试。请在此处将此安装方法的任何问题报告为问题：[https ://github.com/ajenti/ajenti/issues](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2FqZW50aS9hamVudGkvaXNzdWVz)

```
curl https://raw.githubusercontent.com/ajenti/ajenti/master/scripts/install-venv.sh | sudo bash -s -
```

## 手动安装

### 本机依赖项：Debian/Ubuntu

启用 Universe 存储库（仅限 Ubuntu）：

```
sudo add-apt-repository universe
```

```
sudo apt-get install build-essential python3-pip python3-dev python3-lxml libssl-dev python3-dbus python3-augeas python3-apt ntpdate
```

### 本机依赖项：RHEL

启用 EPEL 存储库：

```
sudo dnf install epel-release
```

```
sudo dnf install -y gcc python3-devel python3-pip python3-pillow python3-augeas python3-dbus chrony openssl-devel redhat-lsb-core
```

### 安装 Ajenti 2

升级画中画：

```
sudo pip3 install setuptools pip wheel -U
```

最小安装：

```
sudo pip3 install ajenti-panel ajenti.plugin.core ajenti.plugin.dashboard ajenti.plugin.settings ajenti.plugin.plugins
```

使用所有插件：

```
sudo pip3 install ajenti-panel ajenti.plugin.ace ajenti.plugin.augeas ajenti.plugin.auth-users ajenti.plugin.core ajenti.plugin.dashboard ajenti.plugin.datetime ajenti.plugin.filemanager ajenti.plugin.filesystem ajenti.plugin.network ajenti.plugin.notepad ajenti.plugin.packages ajenti.plugin.passwd ajenti.plugin.plugins ajenti.plugin.power ajenti.plugin.services ajenti.plugin.settings ajenti.plugin.terminal
```

## 卸载 Ajenti 2

Ajenti 是一组随 pip 安装的 Python 模块，随初始化脚本（systemd 或 sysvinit）一起提供。所以有必要删除 init 脚本，然后是 Python 库和配置文件。

### 系统化

```
sudo systemctl stop ajenti.service
sudo systemctl disable ajenti.service
sudo systemctl daemon-reload
sudo rm -f /lib/systemd/system/ajenti.service
```

### 系统初始化

```
/etc/init.d/ajenti stop
rm -f /etc/init/ajenti.conf
```

### Python3模块

列出 Ajenti 的所有模块：

```
sudo pip3 list | grep aj
```

结果应该是这样的（最终或多或少的插件）：

```
aj                         2.1.43
ajenti-panel               2.1.43
ajenti.plugin.ace          0.30
ajenti.plugin.auth-users   0.31
ajenti.plugin.core         0.99
ajenti.plugin.dashboard    0.39
ajenti.plugin.filesystem   0.47
ajenti.plugin.passwd       0.24
ajenti.plugin.plugins      0.47
ajenti.plugin.session-list 0.4
ajenti.plugin.settings     0.30
```

然后简单地删除所有这些模块：

```
sudo pip3 uninstall -y aj ajenti-panel ajenti.plugin.ace ajenti.plugin.auth-users ajenti.plugin.core ajenti.plugin.dashboard ajenti.plugin.filesystem ajenti.plugin.passwd ajenti.plugin.plugins ajenti.plugin.session-list ajenti.plugin.settings
```

### 配置文件

如果您以后不需要它，只需删除目录/etc/ajenti/：

```
sudo rm -rf /etc/ajenti/
```

[取消回复](https://blog.upx8.com/3165#respond-post-3165)

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