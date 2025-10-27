---
title: Scoop - 最好用的 Windows 包管理器
url: https://blog.upx8.com/3093
source: 黑海洋 - WIKI
date: 2022-11-17
fetch_date: 2025-10-03T23:01:04.623761
---

# Scoop - 最好用的 Windows 包管理器

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Scoop - 最好用的 Windows 包管理器(软件管理)

发布时间:
2022-11-16

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
35641

## 前言

[Scoop](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5bmFYUm9kV0l1WTI5dEwyeDFhMlZ6WVcxd2MyOXVMM05qYjI5dw) 是一个 Win­dows 包管理工具，类似于 De­bian 的 `apt`、ma­cOS 的 `homebrew`。它由开源社区驱动，体验可能是是目前所有 Win­dows 包管理工具中最好的。对开发者来说，包管理器能非常方便的部署开发环境，比如 Python 、Node.js 。而对于像博主这样的普通的计算机使用者来说，可以方便的安装一些常用软件，尤其是开源软件，免去了手动去官网下载的繁琐步骤，而且后续对软件进行升级只需要输入一行命令，非常便捷。

## 环境要求

* Windows 7 SP1 + / Windows Server 2008+
* [PowerShell 5](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5aGEyRXViWE12ZDIxbU5XUnZkMjVzYjJGaw)（或更高版本，包括 [PowerShell Core](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5a2IyTnpMbTFwWTNKdmMyOW1kQzVqYjIwdlpXNHRkWE12Y0c5M1pYSnphR1ZzYkM5elkzSnBjSFJwYm1jdmFXNXpkR0ZzYkM5cGJuTjBZV3hzYVc1bkxYQnZkMlZ5YzJobGJHd3RZMjl5WlMxdmJpMTNhVzVrYjNkelAzWnBaWGM5Y0c5M1pYSnphR1ZzYkMwMg)）和 [.NET Framework 4.5](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5M2QzY3ViV2xqY205emIyWjBMbU52YlM5dVpYUXZaRzkzYm14dllXUQ)（或更高版本）
* Windows 用户名为英文（Windows 用户环境变量中路径值不支持中文字符）
* **正常、快速**的访问 GitHub 并下载资源

## 安装 Scoop

Scoop 默认使用普通用户权限，其本体和安装的软件默认会放在 `%USERPROFILE%\scoop`(即 `C:\Users\用户名\scoop`)，使用管理员权限进行全局安装 (`-g`) 的软件在 `C:\ProgramData\scoop`。如果有自定安装路径的需求，那么要提前设置好环境变量，否则后续再改不是一件容易的事情。

* 打开 PowerShell
* 设置用户安装路径

```
$env:SCOOP='D:\Scoop'
[Environment]::SetEnvironmentVariable('SCOOP', $env:SCOOP, 'User')
```

* 设置全局安装路径（需要管理员权限）

```
$env:SCOOP_GLOBAL='D:\Scoop_Global'
[Environment]::SetEnvironmentVariable('SCOOP_GLOBAL', $env:SCOOP_GLOBAL, 'Machine')
```

* 设置允许 PowerShell 执行本地脚本

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

* 安装 Scoop

```
iwr -useb https://gitee.com/RubyKids/scoop-cn/raw/main/install.ps1 | iex
```

* 没安装过 Git 则需要安装。

```
scoop install git
```

## 基础使用

最基础的使用方法和其它包管理器类似，这里就不做赘述了，直接上命令列表：

* `scoop search <app>` - 搜索软件
* `scoop install <app>` - 安装软件
* `scoop info <app>` - 查看软件详细信息
* `scoop list` - 查看已安装软件
* `scoop uninstall <app>` - 卸载软件，`-p`删除配置文件。
* `scoop update` - 更新 scoop 本体和软件列表
* `scoop update <app>` - 更新指定软件
* `scoop update *` - 更新所有已安装的软件
* `scoop checkup` - 检查 scoop 的问题并给出解决问题的建议
* `scoop help` - 查看命令列表
* `scoop help <command>` - 查看命令帮助说明

## 进阶使用

### 添加 bucket

所有的包管理器都会有相应的软件仓库 ，而 bucket 就是 Scoop 中的软件仓库。细心的你可能会发现 `scoop` 翻译为中文是 “舀”，而 `bucket` 是 “水桶”，所以安装软件可以理解为从水桶里舀水，似乎很形象的说。

Scoop 默认软件仓库（main bucket）软件数量是有限的，但是可以进行额外的添加。通过 `scoop bucket known` 命令可以查看官方认可的 bucket：

```
$ scoop bucket known
main
extras
versions
nightlies
nirsoft
php
nerd-fonts
nonportable
java
games
jetbrains
```

以上官方认可的 bucket 可以通过下面这个命令直接添加：

```
scoop bucket add <bucketname>
```

[extras](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5bmFYUm9kV0l1WTI5dEwyeDFhMlZ6WVcxd2MyOXVMM05qYjI5d0xXVjRkSEpoY3c) 涵盖了大部分因为种种原因不能被收录进主仓库的常用软件，这个是强推荐添加的。

```
scoop bucket add extras
```

比如博主经常会使用到的写盘工具 Ru­fus 就在 `extras` 这个仓库中。

```
scoop install rufus
```

[nerd-fonts](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5bmFYUm9kV0l1WTI5dEwyMWhkSFJvWlhkcVltVnlaMlZ5TDNOamIyOXdMVzVsY21RdFptOXVkSE0) 包含了美化终端时会用到的 Pow­er­line 字体

```
scoop bucket add nerd-fonts
```

当添加 `nerd-fonts` 仓库后可以通过以下命令搜索到所有的字体：

```
scoop search "-NF"
```

安装字体需要使用管理员权限：

```
sudo scoop install FiraCode-NF
```

#### 第三方 bucket

添加第三方 bucket

```
scoop bucket add <bucketname> https://github.com/xxx/xxx
```

从第三方 bucket 中安装软件

```
scoop install <bucketname>/<app>
```

### 清理安装包缓存

Scoop 会保留下载的安装包，对于卸载后又想再安装的情况，不需要重复下载。但长期累积会占用大量的磁盘空间，如果用不到就成了垃圾。这时可以使用 `scoop cache` 命令来清理。

* `scoop cache show` - 显示安装包缓存
* `scoop cache rm <app>` - 删除指定应用的安装包缓存
* `scoop cache rm *` - 删除所有的安装包缓存

如果你不希望安装和更新软件时保留安装包缓存，可以加上 `-k` 或 `--no-cache` 选项来禁用缓存：

* `scoop install -k <app>`
* `scoop update -k *`

### 删除旧版本软件

当软件被更新后 Scoop 还会保留软件的旧版本，更新软件后可以通过 `scoop cleanup` 命令进行删除。

* `scoop cleanup <app>` - 删除指定软件的旧版本
* `scoop cleanup *` - 删除所有软件的旧版本

与安装软件一样，删除旧版本软件的同时也可以清理安装包缓存，同样是加上 `-k` 选项。

* `scoop cleanup -k <app>` - 删除指定软件的旧版本并清除安装包缓存
* `scoop cleanup -k *` - 删除所有软件的旧版本并清除安装包缓存

### 全局安装

全局安装就是给系统中的所有用户都安装，且环境变量是系统变量，对于需要设置系统变量的一些软件就需要全局安装，比如 Node.js、Python ，否则某些情况会出现无法找到命令的问题。

使用 `scoop install <app>` 命令加上 `-g` 或 `--global` 选项可对软件进行全局安装，全局安装需要管理员权限，所以需要提前以管理员权限运行的 Pow­er­Shell 。更简单的方式是先安装 `sudo`，然后用 `sudo` 命令来提权执行：

```
scoop install sudo
sudo scoop install -g <app>
```

> 达成在 Win­dows 上使用`sudo`的成就

使用 `scoop list` 命令查看已装软件时，全局安装的软件末尾会有 `*global*` 标志。

```
➜ scoop list
Installed apps:

  7zip 19.00
  adb 30.0.0
  aria2 1.35.0-1
  busybox 3466-g53c09d0e1
  CascadiaCode-NF 2.1.0 [nerd-fonts]
  colortool 1904.29002
  dark 3.11.2 *global*
  ffmpeg 4.2.3
  figlet 1.0-go
  FiraCode-NF 2.1.0 [nerd-fonts]
  git 2.26.2.windows.1 *global*
  innounp 0.49
  iperf3 3.1.3
  lessmsi 1.6.91 *global*
  lxrunoffline 3.4.1 [extras]
  nano 4.9-4
  neofetch 7.0.0
  nodejs-lts 12.17.0 *global*
  python 3.8.3 *global*
  rclone 1.52.0
  rufus 3.10 [extras]
  screentogif 2.24.2 [extras]
  sudo 0.2020.01.26
```

此外对于全局软件的更新和卸载等其它操作，都需要加上 `-g` 选项：

* `sudo scoop update -g *` - 更新所有软件（且包含全局软件）
* `sudo scoop uninstall -g <app>` - 卸载全局软件
* `sudo scoop uninstall -gp <app>` - 卸载全局软件（并删除配置文件）
* `sudo scoop cleanup -g *` - 删除所有全局软件的旧版本
* `sudo scoop cleanup -gk *` - 删除所有全局软件的旧版本（并清除安装包包缓存）

### 代理设置

Scoop 默认使用的是系统代理，如果你想手动指定代理，可以输入下面的命令。需要注意的是只支持 http 协议。

```
scoop config proxy localhost:1080
```

> 设置完可以通过`scoop config proxy`查看。

如果你想取消代理，那么输入下面的命令，这将会恢复使用系统代理。

```
scoop config rm proxy
```

### 开启多线程下载

使用 Scoop 安装 Aria2 后，Scoop 会自动调用 Aria2 进行多线程加速下载。

```
scoop install aria2
```

使用 `scoop config` 命令可以对 Aria2 进行设置，比如 `scoop config aria2-enabled false` 可以禁止调用 Aria2 下载。以下是与 Aria2 有关的设置选项：

* `aria2-enabled`: 开启 Aria2 下载，默认`true`
* [`aria2-retry-wait`](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5aGNtbGhNaTVuYVhSb2RXSXVhVzh2YldGdWRXRnNMMlZ1TDJoMGJXd3ZZWEpwWVRKakxtaDBiV3dqWTIxa2IzQjBhVzl1TFhKbGRISjVMWGRoYVhR): 重试等待秒数，默认`2`
* [`aria2-split`](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5aGNtbGhNaTVuYVhSb2RXSXVhVzh2YldGdWRXRnNMMlZ1TDJoMGJXd3ZZWEpwWVRKakxtaDBiV3dqWTIxa2IzQjBhVzl1TFhN): 单任务最大连接数，默认`5`
* [`aria2-max-connection-per-server`](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5aGNtbGhNaTVuYVhSb2RXSXVhVzh2YldGdWRXRnNMMlZ1TDJoMGJXd3ZZWEpwWVRKakxtaDBiV3dqWTIxa2IzQjBhVzl1TFhn): 单服务器最大连接数，默认`5` ，最大`16`
* [`aria2-min-split-size`](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5aGNtbGhNaTVuYVhSb2RXSXVhVzh2YldGdWRXRnNMMlZ1TDJoMGJXd3ZZWEpwWVRKakxtaDBiV3dqWTIxa2IzQjBhVzl1TFdz): 最小文件分片大小，默认`5M`

博主在这里推荐以下优化设置，单任务最大连接数设置为 `32`，单服务器最大连接数设置为 `16`，最小文件分片大小设置为 `1M`

```
scoop config aria2-split 32
scoop config aria2-max-connection-per-server 16
scoop config aria2-min-split-size 1M
```

## 常用命令总结

看到这里一定有很多小伙伴已经懵逼了，最后总结一波 Scoop 在日常使用中的常用命令：

```
# 更新 scoop 及软件包列表
scoop update

## 安装软件 ##
# 非全局安装（并禁止安装包缓存）
scoop install -k <app>
# 全局安装（并禁止安装包缓存）
sudo scoop install -gk <app>

## 卸载软件 ##
# 卸载非全局软件（并删除配置文件）
scoop uninstall -p <app>
# 卸载全局软件（并删除配置文件）
sudo scoop uninstall -gp <app>

## 更新软件 ##
# 更新所有非全局软件（并禁止安装包缓存）
scoop update -k *
# 更新所有软件（并禁止安装包缓存）
sudo scoop update -gk *

## 垃圾清理 ##
# 删除所有旧版本非全局软件（并删除软件包缓存）
scoop cleanup -k *
# 删除所有旧版本软件（并删除软件包缓存）
sudo scoop cleanup -gk *
# 清除软件包缓存
scoop cache rm *
```

## 尾巴

Scoop 的使用方法和功能远不止上面提及的这些，但作为一个普通用户也只会用到一些基本的命令和功能。纵观全网也很少有人把基础功能都说明白，这也是在 0202 年咕鸽随便一搜一大把 Scoop 教程和笔记文章的情况下博主依然写这样一篇更加全面教程的原因。希望这篇教程对你有所帮助。

## 参考资料

[Scoop Documentation](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5bmFYUm9kV0l1WTI5dEwyeDFhMlZ6WVcxd2MyOXVMM05qYjI5d0wzZHBhMms)

[再谈谈 Scoop 这个 Windows 下的软件包管理器](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5M2QzY3VhRFF3TkdKcExtTnZiUzlpYkc5bkx6SXdNVGd2TURVdmRHRnNheTFoWW05MWRDMXpZMjl2Y0MxMGFHVXRjR0ZqYTJGblpTMXRZVzVoWjJWeUxXWnZjaTEzYVc1a2IzZHpMV0ZuWVdsdUx3)

[「一行代码」搞定软件安装卸载，用 Scoop 管理你的 Windows 软件](https:/...