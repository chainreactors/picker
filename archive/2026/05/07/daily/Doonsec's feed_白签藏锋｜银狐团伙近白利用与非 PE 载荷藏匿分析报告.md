---
title: 白签藏锋｜银狐团伙近白利用与非 PE 载荷藏匿分析报告
url: https://mp.weixin.qq.com/s/Ab-21iUmfxeg3z4EcjW6eA
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:52:03.591166
---

# 白签藏锋｜银狐团伙近白利用与非 PE 载荷藏匿分析报告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jHUbrwW0VwXGOkO4R1Ao9Orp01AkRLhiaicZKAKO3f51CT57XNXHEZmEoHiaegKGFdKRgr0zzocAqLibRZrKkTtvZlY6GOjgGBJygtgCEVTn6PQ/0?wx_fmt=jpeg)

# 白签藏锋｜银狐团伙近白利用与非 PE 载荷藏匿分析报告

原创

腾讯安全威胁情报
腾讯安全威胁情报

腾讯安全威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 一、概述

近期捕获到一起借 **Hello GPT 翻译器**名义投递的钓鱼样本。攻击者仿造官网 `cn-hellogpt.com`，向用户分发伪装成 AI 翻译工具的安装包。用户完成看似正常的安装流程后，恶意模块转入后台，在 `%APPDATA%\Roaming` 目录下释放两组随机命名的恶意文件，并通过计划任务完成持久化。

这批样本和传统的“白 + 黑 DLL”白利用不太一样。以往攻击者常把恶意逻辑放在外置黑 DLL 中，DLL 本身特征明显，容易被静态扫描或行为检测命中。本次样本把执行入口改进到合法签名程序内部，再把核心代码拆到多组非 PE 自定义文件中，形成一套更隐蔽的 **“近白利用 + 非 PE 载荷藏匿”** 链路：

* 对 **杭州顺网科技**、**万能输入法** 的合法签名程序做二进制 PATCH，把恶意 ShellCode 缝入内部执行路径；
* 将后续核心恶意代码藏在非 PE 格式的自定义文件（`.oi / .vc / .ti / .er / .ce / .ou / .pt`）中；
* 用虚假控制流、流程平坦化、花指令和字符串运行时解密增加静态分析成本；
* 执行 **AMSI 扫描绕过 + ETW 遥测致盲 + 国内主流安全软件关停** 的安全规避链；
* 注入 **sihost.exe / UserAccountBroker.exe / EDPNotify.exe** 等微软原生签名进程，维持 C2 长期驻留。

综合投递方式、载荷组织和对抗手法判断，该样本属于银狐木马分支变种。相比此前常见样本，这次的变化集中在两个点：合法签名程序被改造成 Loader，核心恶意代码转入非 PE 自定义载荷。

---

## 二、初始入口：伪装 Hello GPT 的钓鱼网站

攻击者注册仿冒域名 `cn-hellogpt[.]com`、`hallogpt[.]com`，克隆真实 AI 翻译工具的界面风格，并在站内批量生成“使用教程”“实战指南”等 SEO 软文，提高站点在搜索引擎中的可信度和权重。行业人员通过搜索引擎检索相关工具关键词时，可能直接进入攻击者设计好的下载链路。![](https://mmbiz.qpic.cn/sz_mmbiz_png/jHUbrwW0VwVib705WYc5xSekTkicLHECaYZV8KbkdliadMDnHsEpEbMeMdiat7AibzN1IyKMkutPQN4kHBGESbRqqtZiaMP1bjdoS1yz6oXM7TER0/640?wx_fmt=png&from=appmsg)

用户被引导下载的安装包，在外观上完整还原了一款普通翻译软件的 NSIS 安装向导。用户一路点击“下一步”完成安装时，后门植入流程同步执行：![](https://mmbiz.qpic.cn/sz_mmbiz_png/jHUbrwW0VwXmUISHdXKWYyH823apQCeuoLGJ8D1WMw3ufdZm2hg7jFVibNE5tgn7ptaPJP9eGSv7icRa6jmp8UkO4lXpeOwgaDhR4hJ8ibXdxw/640?wx_fmt=png&from=appmsg)

---

## 三、样本执行流程：延迟释放与伪装持久化

安装包运行后不会立即释放恶意载荷，而是等待用户按流程完整点完安装向导，借真实用户交互规避沙箱环境。随后，样本在 `%APPDATA%\Roaming` 目录下创建两个以 `comain_` 为前缀的子目录，分别释放两组恶意文件。

持久化阶段，样本将两个主 EXE 模块注册为伪装的系统计划任务。任务被挂靠到 `\Microsoft\Windows\Application Experience\` 路径下，命名为 `Diagnostics` 与 `Diagnostics2`，并照搬微软原生任务的官方描述（“允许用户在 AD RMS 权限策略模板……”）。从任务计划程序中看，这两个任务很容易被误认为系统组件。![](https://mmbiz.qpic.cn/mmbiz_png/jHUbrwW0VwXgza2Ciba78rfrlN85CLps8RuIkX46IYzDicFfia1esZDbO3vFB7dxA6thT9zW2LibrGQZyjLGFA0Em4YoVlxnfjicrLicf5J4aibiaHs/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/jHUbrwW0VwVZEWOYcMnIjwGFhuLvC3DYpE6B1RWrXhfljLoJapazU5d9k5j4rqVpAZwDATZlaV7MVOQoyRaC4vcjiaCNMich85c5IibhDIVQDU/640?wx_fmt=png&from=appmsg)

**第一组：comain\_ev2c34 套件**

![](https://mmbiz.qpic.cn/mmbiz_jpg/jHUbrwW0VwXjJoRoxVqicMtSibGO6Y4u3IpWvNKiaPDEMm34a3iaxyOlYB4LVMh22d9vX8ZTlQBib67leicFXnSf9hYcylnEH8dNmlXrUg3vdyo2M/640?wx_fmt=jpeg)

**第二组：comain\_ev2f79 套件**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jHUbrwW0VwXwXpmB5kNmia5nftgEoEMvMiaibY9w2HMEHobj9XyZdZBIeWFYsW0Pnia295xeNullkcnUddd7C9dZjkdD7VCcIVsBzxV2FGuPVTw/640?wx_fmt=jpeg)

下图左侧 `ev2c34.exe` 保留“深圳市世强电脑科技有限公司”签名，右侧 `ev2f79.exe` 保留 “Hangzhou Shunwang Technology Co., Ltd” 签名。两个 EXE 宿主都带有原始知名厂商数字签名，这也是近白利用最核心的伪装点：静态层面看起来接近合法程序，运行后却进入恶意执行链。![](https://mmbiz.qpic.cn/sz_mmbiz_png/jHUbrwW0VwX3DicFic9a7gXanKAK4ia9dMAbGBRQKeoIGHrrJ1MTdBTKSNOs59eDibTXy1uSJDlfu9Lm0Z99X1e8qMFmiaZLH5YSa4g6hzmZsiaLk/640?wx_fmt=png&from=appmsg)

---

## 四、近白利用：MFC 消息回调劫持 + XOR 0x36 自解密

### 4.1 劫持切入点：`CWnd::ReflectChildNotify`

以 `ev2f79.exe`（篡改自顺网的恶意主程序）为例。攻击者没有选择替换 EntryPoint 或 TLS 回调这类更显眼的劫持位置，而是把 MFC 框架中用于**处理子窗口通知的反射函数 `CWnd::ReflectChildNotify`** 改写为 Loader 入口。

应用进入消息循环后，`WM_VSCROLL`、`WM_HSCROLL`、`WM_CTLCOLOR*`、`WM_DRAWITEM`（528）等常规 UI 消息都会触发该函数。也就是说，程序只要正常跑起来，就会自动拉起恶意代码。

cpp

```
int __thiscall CWnd::ReflectChildNotify(...) {

if (a2 > 0x111) {

if (a2 < 0x114 || a2 > 0x115 && a2 != 528)

return loader_read_xor36_and_exec_file();

}

if (a2 != 273) {

if (a2 > 0x2F && a2 != 57) {

...

result = loader_read_xor36_and_exec_file();

if (!*a5) return 0;

return result;

}

return loader_read_xor36_and_exec_file();

}

...

}
```

### 4.2 Loader 逻辑：文件名解密 + XOR 0x36 自解密执行

`loader_read_xor36_and_exec_file` 承担完整装载动作：先解密同目录下的恶意文件名 `otrm.oi`，再以 `XOR 0x36` 对整个文件逐字节解密，最后直接跳转执行。原始 EXE 相对官方版本只改动了少量函数，整体特征高度贴近合法程序，静态识别难度明显提高：

cpp

```
int __cdecl loader_read_xor36_and_exec_file() {

// --- 运行时解密恶意文件名 ---

encNameDwords[0] = 0x44393B46;  // 解密后得到 "otrm.oi"

encNameDwords[1] = 0x27404605;

...

for (i = 61240; ; v1 = i) {

*((_BYTE *)encNameDwords + v0) = v1 ^ (*((_BYTE *)encNameDwords + v0) - v2);

if (++v0 >= nameLen) break;

v2 = BYTE1(i);

}

pGetModuleFileNameA(0, pathBuf, 260u);

pCreateFileA(pathBuf, 0x80000000, 1u, 0, 3u, 128u, 0);

fileSize = pGetFileSize(hFile, 0);

if (fileSize) {

payloadEntry = pVirtualAlloc(0, fileSize, 0x3000, PAGE_EXECUTE_READWRITE);

pReadFile(hFile, payloadEntry, fileSize, &bytesRead, 0);

// --- XOR 0x36 解密 payload ---

for (j = 0; j < bytesRead; ++j)

*((_BYTE *)payloadEntry + j) ^= 0x36u;

return payloadEntry();       // 直接跳转执行

}

}
```

---

## 五、非 PE 载荷的对抗护甲

被解密并装入内存的非 PE 模块（`.oi / .vc / .ti / .er`）使用了同一套反分析护甲。反编译视角下可以看到大量异或表达式与花指令，整体呈现典型的 OLLVM 风格保护。![](https://mmbiz.qpic.cn/sz_mmbiz_png/jHUbrwW0VwWzOjupzF6t3TPqZG0AHEZI1HS9s1Ricz0C4Fpm1xtteK463fbq5DiamvT0DEIwAqvjR1S2PCaCcpg1M2HyH7Q0zxic1LIib1myXyE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jHUbrwW0VwUSnB4pVqsaltLhVTcS2XesiaCn9uvnqcezrwIloNOwfDJgq0SWwx1Q6icJncefvSWjl7NM06laly3fES6s4j843vo4Hcz7iaiamGs/640?wx_fmt=jpeg)

`otrm.oi` 被装载后会继续调用 `SetIoC` 导出函数。该函数先申请 `SeDebugPrivilege` 提权，随后拉起系统 **VSSVC（卷影副本）服务**，再通过线程池注入将 `yinma.vc` 与 `dxyvnb.ti` 两个载荷写入 `VSSVC.exe`。

---

## 六、注入 VSSVC 后的三重对抗

### 6.1 AMSI 双函数 Patch

`dxyvnb.ti` 负责 AMSI 扫描绕过。样本通过 12 字节 PATCH，将 `amsi.dll` 中的 `AmsiScanBuffer` 与 `AmsiScanString` 首部改写为返回安全结果（`S_OK + AMSI_RESULT_CLEAN`）的短桩代码。后续扫描请求在交给杀软 Provider 前就被截断。![](https://mmbiz.qpic.cn/sz_mmbiz_png/jHUbrwW0VwWEavC1cLpJuzgXcW41hNTQZG5jDyeDq3g4TJQZINTffuZSMeWkDm11H9Y4iaI1HWAx4geDdgj4p7D8IehyUaZCibDh7RfJ4AYFM/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/jHUbrwW0VwVGXHQPOo4EdvuvTW15DicEOWRiaMte5hfSxsjK9lQNjgn6UBickzFGZwYuKMRYzI3Gziaqu7yEHyPibCDIcP3IROlhAAlml17Zakrw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jHUbrwW0VwXvmWopVSBRA967yzFD3ED5saBOpmLRl9zrt0g6Yg8sJ5Z80BBicL41wl5UzfFJZsOiaicIUOZy2oPY7YHZ6CuTke0FRjqqgUd5No/640?wx_fmt=jpeg)

### 6.2 ETW 单字节致盲

针对微软 ETW 遥测框架，样本只改写 `ntdll!EtwEventWrite` 入口的第一个字节为 `0xC3`（ret）。这一字节 PATCH 会让进程内所有 ETW 事件，包括 Defender 的 AMSI 子通道、PowerShell ScriptBlock 日志、.NET CLR 运行时遥测等，在离开进程前被静默丢弃。下游依赖 ETW Consumer 的 EDR 分析链路也会随之失效。![](https://mmbiz.qpic.cn/mmbiz_png/jHUbrwW0VwUyicyT84r33t9mSSIZlx3PHHa0AJrQ0DOfvo2FPDovOA7UsXQZglVejXrLYUv4uWsTzpIVCL0iaAeILTtvZPHjJIWJbSefrMbm4/640?wx_fmt=png&from=appmsg)

### 6.3 注入 svchost 并围剿国内安全软件

`yinma.vc` 解密展开为标准 PE 后，会读取外部 `ntrin.er` 恶意载荷，再次通过线程池注入将其写入系统中 **PID 最小的 svchost.exe** 进程。

这个目标选择并不随机。PID 最小的 `svchost.exe` 通常对应 `-k DcomLaunch` 或 `-k RPCSS`，权限为 SYSTEM，并运行在敏感服务组内。攻击者借它作为执行进程，在应用层结束国内安全软件时成功率更高。

被注入的 `svchost.exe` 会启动监控线程，按照运行时解密出的硬编码字符串表循环探测，并主动结束对应安全软件进程：![](https://mmbiz.qpic.cn/mmbiz_png/jHUbrwW0VwVj3oyZZxJuhnuxFBwpia4GSU5pklhuB1ejNZRa5pBicRLVbNwDKyzkibfnyAFORmP3AgXxKRHBT5X38wzqY7tuiaoGgeMhkwzXUAw/640?wx_fmt=png&from=appmsg)

---

## 七、fhkan 模块：三件套注入 + Mutex 门控

`ev2c34.exe`（篡改自万能输入法）运行后，先解密装载 `fhkan.oi`，再调用其中的 `AndStop` 函数。该函数承担本轮攻击的主业务调度职责，核心逻辑包括：

### 7.1 Mutex 单实例守卫 + C2 上线标记

`fhkan` 使用两个 **Base64 编码的 Mutex** 作为状态位，分别表示“已上线”和“本地守卫正在运行”。下图是 `UserAccountBroker.exe` 与 `edpnotify.exe` 持有的 Mutex：![](https://mmbiz.qpic.cn/mmbiz_png/jHUbrwW0VwU8mKvnawJcxQgwJBDHGhW80DCM8G7z4vCoGYZEM6myMwfBluPXLo9zrjicA2R9uwvuwCE9F9ngJ4LxghhsyvotyibiavSrufqeyM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jHUbrwW0VwWUKbIWmwcNBasj9SmKmOG0OEdvJRkzbEOnHADsY7cVrbWkPNiaxsJZTfWfVJIqyO3GnJY8IvmhtS7bbmfDxwJYO1W9NMSy17fQ/640?wx_fmt=jpeg)

当 `fhkan` 启动时会首先检查这两个 Mutex：

* 都不存在 → 进入**主分支**，执行跨进程注入；
* 已存在 → 说明木马已经在运行，当前实例直接退出，避免重复感染。

### 7.2 注入“微软签名 Shell 三件套”

`fhkan` 完成自解密后，会注入三个微软原生签名的用户态 Shell 进程，构建冗余且隐蔽的 C2 宿主：

![](https://mmbiz.qpic.cn/mmbiz_jpg/jHUbrwW0VwWNuycjENLkCCUicfQQSrRQ7J3dRJ8sY0SPsHibpPwrPjIT3VRIliasfOuhqJuvFN4OsbbZVVoVnE4YeMMe2F47qOqNWgNam4exsI/640?wx_fmt=jpeg)

这三个进程都有适合驻留的特征：

* 三者均为微软签名，更容易被 EDR 或杀软默认放行出站连接；
* 三者均为系统功能模块，分别承担 **Shell 基础设施（sihost）**、**用户账户...