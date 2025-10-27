---
title: [Golang]ByPass360一键开启谷歌浏览器调试模式
url: https://www.nctry.com/2772.html
source: TRY博客
date: 2025-08-06
fetch_date: 2025-10-07T00:17:44.526295
---

# [Golang]ByPass360一键开启谷歌浏览器调试模式

[![TRY博客](https://www.nctry.com/wp-content/uploads/2018/11/20181120_091128_42.png)](https://www.nctry.com)

* [随手记](https://www.nctry.com/xjb)
* [渗透学习](https://www.nctry.com/category/hacker)
* [本站友好作者](https://www.nctry.com/%E6%9C%AC%E7%AB%99%E5%8F%8B%E5%A5%BD%E4%BD%9C%E8%80%85)
* [隐私政策](https://www.nctry.com/privacy)
* [关于站长](https://www.nctry.com/about)
* [友链](https://www.nctry.com/link)

# [Golang]ByPass360一键开启谷歌浏览器调试模式

[TRY](https://www.nctry.com/2772.html)

2025-08-05

309

[0](https://www.nctry.com/2772.html#respond)

# 至少我们曾经在一起过。

来自：一言

## 分享一下几年前写的一个项目(点个免费的Star即可)。

项目地址: [https://github.com/TryGOTry/ChromeDebugLnk](https://www.nctry.com/go/?url=https://github.com/TryGOTry/ChromeDebugLnk)

# ChromeDebugLnk

## 中文介绍

**ChromeDebugLnk** 是一个基于 Go 语言开发的 Windows 工具，专门用于修改桌面、任务栏或用户指定路径中的浏览器快捷方式（支持 Chrome、Edge 和 Opera），以启用远程调试模式。该工具需要以管理员权限（UAC）运行，以绕过如 360 安全卫士等安全软件的限制，允许无缝修改快捷方式的属性。此外，它还提供通过修改 Windows 注册表来限制 Chrome 浏览器隐身模式的功能，适合需要特定浏览器配置的开发或管理场景。

## 运行截图

![](https://www.nctry.com/wp-content/uploads/2025/08/sc.png)

### 主要功能

1. 1. **快捷方式修改**：
      * 为 Chrome、Edge 或 Opera 浏览器的快捷方式添加远程调试参数（`--remote-debugging-port` 和 `--remote-allow-origins=*`）。
      * 支持修改桌面、公共桌面、任务栏或用户自定义路径中的快捷方式。
      * 自动检测快捷方式是否已启用调试模式，若已启用则跳过修改。
      * 调试端口会自动递增以避免冲突（默认端口为 `9222`）。
   2. **限制 Chrome 隐身模式**：
      * 通过修改注册表（`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome`）来禁用 Chrome 的隐身模式。
      * 支持移除已设置的隐身模式限制（通过 `-nobypass` 参数）。
   3. **自定义支持**：
      * 支持通过 `-u` 参数指定用户名，定位特定用户的桌面路径。
      * 支持通过 `-path` 参数指定任意快捷方式路径。
      * 支持通过 `-l` 参数指定特定的快捷方式名称（如 `Google Chrome.lnk`）。
   4. **安全性与隐形操作**：
      * 程序运行需要输入特定密码（`fuck360`），以防止未经授权的执行。
      * 支持在完成修改后自动删除自身（通过 `utils.DeleteSelf()`），实现隐形操作。
   5. **权限检查**：
      * 程序会检查是否以管理员权限运行，若权限不足则会提示并退出。

### 使用方法

程序通过命令行参数运行，以下是可用参数的详细说明：

* `-a <password>`：运行密码，必须为 `fuck360`，否则程序退出。
* `-p <port>`：指定远程调试端口，默认为 `9222`。
* `-l <name>`：指定要修改的快捷方式名称（例如 `Google Chrome`）。
* `-u <username>`：指定目标用户名，定位其桌面路径（例如 `User1`）。
* `-path <path>`：指定自定义快捷方式路径（例如 `C:\Users\User1\Desktop\Google Chrome.lnk`）。
* `-bypass`：启用 Chrome 隐身模式限制（修改注册表）。
* `-nobypass`：移除 Chrome 隐身模式限制。

#### 示例

1. 修改默认桌面上的 Chrome 快捷方式，启用调试模式：

   ```
   ChromeDebugLnk.exe -a fuck360 -p 9222
   ```
2. 修改指定用户的 Chrome 快捷方式：

   ```
   ChromeDebugLnk.exe -a fuck360 -u User1 -l "Google Chrome"
   ```
3. 启用 Chrome 隐身模式限制：

   ```
   ChromeDebugLnk.exe -a fuck360 -bypass
   ```
4. 修改指定路径的快捷方式：

   ```
   ChromeDebugLnk.exe -a fuck360 -path "C:\Users\Public\Desktop\Google Chrome.lnk"
   ```

   ## 如何编译

   ```
   go build -o ChromeDebugLnk.exe -ldflags "-w -s" main.go
   ```

   * **权限要求**：程序必须以管理员权限运行，否则会因 UAC 权限不足而退出。
   * **注册表修改**：启用或移除隐身模式限制后，需重启 Chrome 浏览器以生效。
   * **端口冲突**：程序会自动递增端口号以避免冲突，但建议检查端口是否被占用。
   * **快捷方式路径**：确保指定的快捷方式文件存在，否则程序会跳过不存在的文件。
   * **安全性**：密码验证和自删除功能确保程序的安全性和隐形性，适合在受控环境中使用。

本文作者为[TRY](https://www.nctry.com/2772.html)，转载请注明。

[bypass360](https://www.nctry.com/tag/bypass360) [chrome](https://www.nctry.com/tag/chrome) [cookie](https://www.nctry.com/tag/cookie) [debug](https://www.nctry.com/tag/debug)

0人点赞

发表评论
取消回复

昵称（必填）

邮箱（必填）

网址

表情
 图片
 链接
 代码

[x] 接收回复邮件通知
 提交评论

分享

微信

微博

QQ

by:TRY

蜀ICP备18037281号-2| TRY博客 |
Copyright © nctry.com

夜间模式
[ ]

---

100