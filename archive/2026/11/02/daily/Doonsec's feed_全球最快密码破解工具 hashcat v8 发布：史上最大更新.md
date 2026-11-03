---
title: 全球最快密码破解工具 hashcat v8 发布：史上最大更新
url: https://mp.weixin.qq.com/s/qwEOhM1c_XrRF929AOfpiA
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:48:02.191189
---

# 全球最快密码破解工具 hashcat v8 发布：史上最大更新

# 全球最快密码破解工具 hashcat v8 发布：史上最大更新

原创

ralap
ralap

网络个人修炼

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

之前 24 年有写过 hashcat 相关介绍，后续更新都是常规修复性更新。而在上个月末（10 月 26 日），官方发布 v8.0.0，宣布这是项目历史上最大的一次更新——官方原话是：此前没有任何一个版本改动过如此多的文件，也没有任何一个版本积累过如此多的更新日志条目。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aj4fOOkmqMLZyXryUqSdLNst1XoeRvR29fvq7eicjYOtZBN7Gv0gdwIIYo5zP9GwKnMwL6MMNrk2kqcu54Bzw0LUvr5mSyv75zWGQOP6JEak/640?wx_fmt=png&from=appmsg)

看一组数字：

* 11 项重大特性 + 4 个全新攻击模式
* 4,091 个文件改动，新增 43.9 万行、删除 22.9 万行
* 146 个新哈希模式、26 个新哈希原语、306 项 Bug 修复.
* 63 位贡献者参与，其中 43 位是首次贡献

![](https://mmbiz.qpic.cn/mmbiz_png/aj4fOOkmqMKHp4SPqv2yNk4Bdql21bLAdL0icc0nToWrbpyN2mzVMhBJdJm0YXbFTO0dzVPWx3m27KCqShFexGL5Kx3pUhfaoqEYXBFVQZsg/640?wx_fmt=png&from=appmsg)

下面就来看看和旧版到底有什么区别，哪些功能值得关注。

---

## 一、4 个全新攻击模式

##

新增攻击模式是本次更新最亮眼的部分，直接拓展了密码审计的攻击思路，不再局限于传统字典、掩码、组合攻击：

1. **PCFG 概率上下文无关语法攻击（-a 4）**

   PCFG 是近些年密码破解领域效果很强的攻击方式，之前大多依靠独立脚本、第三方工具实现。现在 hashcat 原生内置 PCFG 攻击，直接基于真实密码的结构概率生成候选密码，针对用户习惯的密码（日期、手机号、后缀符号、大小写穿插）命中率远高于传统掩码。
2. **Hash Recipes（-m 4000）：命令行自定义哈希**

   遇到官方没收录的哈希，不用再自己写 C 插件了。直接在命令行输入公式（如 `md5(md5(salt) . pass)`），hashcat 会现场将其编译进 GPU 内核。这套语法支持数十种算法和变换，速度极快，极大扩充了未知样本的破解能力。
3. **Table 攻击（-a 5）**

   老牌攻击方式回归，沿用了 hashcat-legacy 时代的原始编号，通过 token 替换表生成候选，可覆盖 leetspeak、emoji、键盘布局变形等场景。
4. **Feed 攻击（-a 8）与掩码内嵌词表（-a 12）**

* 掩码内嵌词表：用 `?w` / `?q` 占位符把词表嵌入掩码任意位置，如 `?w?d?d` 表示"每个词后接两位数字"

* Feed 攻击：候选生成器以插件形式运行（可用 C 或 Rust 编写），完整支持 keyspace 计算、任务分发和断点恢复

---

## 二、字典攻击能力升级

##

字典是 hashcat 使用频率最高的载体，本次改动集中在“大”和“多”：

* **超大哈希列表装载提速（多核并行）**：现在所有 CPU 核心都会参与哈希列表的计数、解析、排序和去重。官方数据显示，在 7950X 上装载 5000 万条 NTLM 从旧版的 40 秒直接降到 1.7 秒；在 RTX 4090 下处理 5000 万条 NTLM 的破解速度，也从 1.1 GH/s 飙升到了 58 GH/s。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aj4fOOkmqMIjYECTawOKwJNibWS6eygOibe69W4L8tCRMtq7uTRdNEZR2FjEk2zaAS0uBYqg1m4XSicdSGAtG3pTusMdSDAhXx1JuAAPsB6zG8/640?wx_fmt=png&from=appmsg)

* **多字典合并为一个 Keyspace**：`--skip`、`--limit`、`--keyspace` 现在可以作用于多个词表或整个词表目录（combinator 攻击的左侧也接受目录）。分布式跑包时，一个节点分到的区间可以正好跨过文件边界——从上一个词表的末尾接到下一个词表的开头，不再需要手动拆字典。目录内文件按名称排序，保证每个节点看到的顺序一致。

* 共享机器的内存预算：HASHCAT\_DEVICE\_MEM\_LIMIT 和 HASHCAT\_HOST\_MEM\_LIMIT 可以给每个进程单独设定显存和内存上限（单位 MiB），同机跑多个任务时不用再担心互相挤压。

---

## 三、规则引擎重构

##

hashcat 的 rule 规则作为老手的杀招，本次规则修改适用范围：

* 规则可以应用到所有攻击模式：-r 以前只在 straight 和 association 中生效，现在扩展到 combinator、brute-force、PCFG、table、hybrid 以及掩码内嵌词表；掩码文件、--increment、Markov 参数和自定义字符集的行为保持不变。
* 调试输出能看出是哪条规则命中的：在 combinator、brute-force、hybrid 和掩码内嵌词表攻击中，会标出产生命中的那条规则
* 规则文件加载同步优化：大规则文件加载更快、占用内存更少，--stdout 下规则处理用满所有 CPU 核心。

---

四、硬件后端改版与整体性能优化

算力底层也是 v8 的重头戏，硬件不再局限于 NVIDIA、AMD 消费级显卡。这次原生加入了对 FPGA 的支持：把 FPGA 板卡当作设备、和显卡并排列出来，首发支持 7 种板卡，目前专攻 bcrypt 这类慢哈希。两块板子跑到 8.9 kH/s，比 RTX 4090 的 7.8 kH/s 还略快，功耗却低得多。平台侧，苹果 M 系列用上了 Metal 4、默认原生 arm64，AMD 也能跑在 Mesa 的开源 OpenCL 驱动上。但硬件门槛反而提高了：最低要 CUDA 12.0、HIP 6.2.0、OpenCL 1.2，OpenCL 1.0/1.1 直接不支持了，核显也不再默认跟着独立显卡一起启用。多卡协同还顺手修了个老毛病：规避了单卡跑满、其余显卡闲置的资源浪费问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aj4fOOkmqMJ0Ec6gQKZp35qYYVjL69ppaa1RJdnmYM56qf7mxcjRvjJPRoQSjU8p7TrYHPQqhvqkvN2dGrSwn5rh1icJtl8Y0uS4dHwY8xYs/640?wx_fmt=png&from=appmsg)

对于日常使用来说，整体使用变化不大，但--restore 不再自动执行，改为打印命令让你确认，-w 还能填但已经不起作用，一律按原 profile 3 跑；以及-m 72000移除等变动还是需要注意。

---

参考链接

[1]https://hashcat.net/hashcat/

[2]https://raw.githubusercontent.com/hashcat/hashcat/v8.0.0/docs/releases\_notes\_v8.0.0.md

[3]https://hashcat.net/forum/thread-13700-post-64570.html

---

相关阅读

[hashcat密码破解工具安装及使用](https://mp.weixin.qq.com/s?__biz=MzkzMDQ0NzQwNA==&mid=2247484702&idx=1&sn=b67714c30c3ce95ad7391ad76b95c47a&scene=21#wechat_redirect)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5y2fUaoQPfKkAnrPt4lEpmGwWaLib4DxIATR0yiaZib3hQAtBDDAMUulZJL39cia5ttpCR5mbu0opYiawr47diaCwhFg/0?wx_fmt=png)

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