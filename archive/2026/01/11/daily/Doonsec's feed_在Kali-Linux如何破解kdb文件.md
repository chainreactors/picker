---
title: 在Kali-Linux如何破解kdb文件
url: https://mp.weixin.qq.com/s/NzN5LWBksMegaf4iA8hRFQ
source: Doonsec's feed
date: 2026-01-11
fetch_date: 2026-01-12T03:37:12.745747
---

# 在Kali-Linux如何破解kdb文件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zzUI49wvajAGibGEnwJoVM39icCgEJmYf9cqubg56tmTaYbficjZ4FUKd9HicUfl8n6e00r1vQYC3XsqohVGF1bJKg/0?wx_fmt=jpeg)

# 在Kali-Linux如何破解kdb文件

原创

SecCeo

泷羽Sec-Ceo

![]()

在小说阅读器中沉浸阅读

### 项目地址

> GitHub - r3nt0n/keepass4brute： Bruteforce Keepass databases （KDBX 4.x format）

# **引言**

KeePass是一款开源密码管理器，它将所有密码加密存储于扩展名为.kdbx的数据库文件中。该文件采用AES-256等强加密算法，其安全性完全依赖于用户设置的主密码，构成了一个本地化的数字密码保险库。

在合法的安全评估或密码恢复场景中，专家常需从kdbx文件中提取其密码验证哈希。这是进行离线密码强度测试或尝试恢复访问权限的关键第一步，为后续的字典或暴力破解提供攻击入口。

为此，安全社区通常使用经典工具`keepass2john`来提取此哈希。然而，随着KeePass版本更新，新的kdbx文件格式可能导致旧版工具报错“File version '40000' is not supported”，这正是本文要解决的核心兼容性问题。

# **keepass2john 的局限性**

当执行命令后，`keepass2john` 抛出 `File version ‘40000’ is currently not supported!` 这一明确错误。这表明目标 `.kdbx` 文件使用了版本号为 `40000` 的内部文件格式。该版本对应于 KeePass 2.50 及以上版本所采用的新格式，其核心在于引入了 **Argon2** 作为新的密钥衍生函数（KDF）以替代旧的 AES-KDF。

```
keepass2john it.kdbx
```

```
! it.kdbx : File version '40000' is currently not supported!
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zzUI49wvajAGibGEnwJoVM39icCgEJmYf9ALEiaDL8LEkuh1Lptqd4jXZPKicVLMtBUh1VwlbVO9YnkA6RO1R9B9dA/640?wx_fmt=png&from=appmsg)

该错误产生的根本原因在于 `keepass2john` 工具版本滞后于 KeePass 软件的更新速度。KeePass 开发者为提升安全性会更新文件格式和加密参数，但开源破解工具集的更新和维护往往存在延迟，导致旧版 `keepass2john` 无法识别和解析新格式的文件头与加密结构。

这一局限性直接中断了渗透测试或取证工作中的标准流程。安全人员在面对最新的目标环境时，其工具链若无法及时应对，将严重影响评估的效率和完整性。它迫使我们必须寻找替代方案，以适应不断变化的技术环境。

# 替代工具 keepass4brute

## 关于项目

KDBX 4.x 格式（Keepass >=2.36）尚不被 keepass2john 支持，因此目前没有已知的方法可以提取哈希并进行破解。 这个工具是针对当前情况的一个快速简易补丁。它尝试直接使用提供的字典对数据库文件进行暴力破解以测试密码短语。

## 依赖关系

* keepassxc-cli

## 环境准备与安装步骤

### 添加官方的 Debian 稳定源

```
echo "deb http://deb.debian.org/debian stable main contrib non-free" | sudo tee -a /etc/apt/sources.list
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zzUI49wvajAGibGEnwJoVM39icCgEJmYf9Jwf9oJzj8g4N0kk5zicjz4cyfs0InUkUzAzraJuvHL8qvsocOzHQicCg/640?wx_fmt=png&from=appmsg)

### 更新软件包列表

```
sudo apt update
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zzUI49wvajAGibGEnwJoVM39icCgEJmYf9mdqf3OuRY7liaoUOZCqrduS8T3J0Cl9y5uIyPTib92dEjxVVP6YfWKBA/640?wx_fmt=png&from=appmsg)

### 安装 keepassxc（依赖环境）

```
sudo apt install keepassxc -t stable
```

```
#安装完成后，可以选择移除稳定源（或保留以备后用）
# sudo sed -i '/deb.debian.org\/debian stable/d' /etc/apt/sources.list
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zzUI49wvajAGibGEnwJoVM39icCgEJmYf9ymhIwYN794DEDL8kVDichnF6uUH4qKnWiaUEEUJEuTLKMofl0BqH41fg/640?wx_fmt=png&from=appmsg)

### 克隆或获取 keepass4brute 工具

```
wget https://raw.githubusercontent.com/r3nt0n/keepass4brute/refs/heads/master/keepass4brute.sh
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zzUI49wvajAGibGEnwJoVM39icCgEJmYf9Sro3Qib8J7NyhTBu11xy1LrrKMQ9DPy155lGOXZQY62sy5OpbvOpLNg/640?wx_fmt=png&from=appmsg)

### 使用方法示例

* 命令格式说明

```
./keepass4brute.sh <kdbx-file> <wordlist>
```

`<kdbx-file>`：需要破解的文件

`<wordlist>`：密码字典

* 示例

```
./keepass4brute.sh it.kdbx password.txt
```

```
[*] Password found: 741852
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zzUI49wvajAGibGEnwJoVM39icCgEJmYf9iaWp4NogwOgT9w8YSMfduegh0VRbMY41NUaRza5iaCNO6PTGW3cBlM9g/640?wx_fmt=png&from=appmsg)

成功获取到密码：741852

---

打开it.kdbx文件

```
keepassxc it.kdbx --pw-stdin
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zzUI49wvajAGibGEnwJoVM39icCgEJmYf9bXnA2fqu0bcZkEayddSnYbB4ReZhJc5oJylN43KdHujt6iaHGdLAudw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zzUI49wvajAGibGEnwJoVM39icCgEJmYf9PeY6q3WibsD728t16ia7zcnjNlAqehGHYfszaHPkPsAa5BvGzUMicqBcA/640?wx_fmt=png&from=appmsg)

成功打开文件

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/zzUI49wvajALtSt2zdpkRUcmXeeDQIp0cWe9VV4zzXHbahcKicvQoaG3BNzt3R6ayahaicCgYtByVCjyUqbaZm1Q/0?wx_fmt=png)

泷羽Sec-Ceo

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/zzUI49wvajALtSt2zdpkRUcmXeeDQIp0cWe9VV4zzXHbahcKicvQoaG3BNzt3R6ayahaicCgYtByVCjyUqbaZm1Q/0?wx_fmt=png)

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