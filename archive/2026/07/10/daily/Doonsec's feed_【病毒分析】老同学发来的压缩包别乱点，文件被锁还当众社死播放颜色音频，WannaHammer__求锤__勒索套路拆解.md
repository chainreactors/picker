---
title: 【病毒分析】老同学发来的压缩包别乱点，文件被锁还当众社死播放颜色音频，WannaHammer\"求锤\"勒索套路拆解
url: https://mp.weixin.qq.com/s/Fa3BEjgIGIQBRQQKAw379Q
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T05:02:04.425159
---

# 【病毒分析】老同学发来的压缩包别乱点，文件被锁还当众社死播放颜色音频，WannaHammer\"求锤\"勒索套路拆解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/887OLfia3YQYCmWGMMQbOjdH8wuBzJgAFGu1Vs5Iu37a79hrNeOjlYkHcS8Caib8JHQ4LGEN0HZF4OQLhROjWAxjVL8HqgAx8G4hKkhIATKrQ/0?wx_fmt=jpeg)

# 【病毒分析】老同学发来的压缩包别乱点，文件被锁还当众社死播放颜色音频，WannaHammer"求锤"勒索套路拆解

原创

CHQ
CHQ

solar应急响应团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/DxUXemrrntp3gibjPSCHmSEpdPDqfBcXT5e151v5AJSbV5JtaALLzQe0I1Jibbet7rTia8icjmgo5r4hpY3IMpYPIw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

依托 **Solar 安全运营响应团队**的日常实战沉淀，我们会定期分享在安全运营中处置的典型应急响应事件，涵盖**银狐木马、APT 攻击、勒索病毒**等各类主流威胁。

作为专业的应急响应中心，Solar 致力于为复杂多变的安全事件提供从深度溯源到闭环处置的全流程支持。针对银狐、APT 等具有高隐蔽性的威胁，我们不仅聚焦于对其攻击行为的深度剖析，更致力于还原其完整的活动链路，并同步输出切实可行的**清除闭环操作方案**。

**突发危机干预通道：**若您的核心资产正面临加密锁定或数据勒索风险，请通过文末二维码联系我们。我们提供全天候紧急介入服务，协助您快速切断攻击链路，全力挽回业务损失。

## 写在前面

近期，Solar应急响应团队陆续接到多位用户的求助反馈。说来也挺有意思，这些求助的共同点不是企业服务器被加密、不是核心业务中断、也不是面临天价赎金，而是桌面上弹出了一个花哨的窗口，文件后缀变成了`.#WannaHammer#`，窗口里循环播放着一段不堪入耳的音频，还敢留下一个QQ号让受害者去联系。

刚看到这个样本的时候，我们团队的反应是有点哭笑不得的。

这个勒索软件给自己起的名字叫 **WannaHammer 3.0**，直译过来大概是"想要锤子"。但在中文互联网的语境里，我们更习惯叫它"求锤"。这个名字本身就带着一种近乎挑衅的味道，仿佛攻击者在对受害者说："你来啊，求锤"

不过玩笑归玩笑，这个样本在行为设计上确实有点意思。它不像LockBit、Blackout那样主打企业级勒索、动辄索要数百万美元加密货币；也不像TellYouThePass走淘宝买密钥的"接地气"路线。WannaHammer的赎金是 **5块钱人民币**，支付方式直接走QQ转账。你没看错，五块钱。这个价格放在勒索软件家族里面，连白菜价都算不上。

但便宜不代表无害。

这个样本真正狠的地方不在于加密本身，而在于它对受害者心理的精准拿捏，**倒计时威胁、桌面壁纸篡改、禁用任务管理器、循环播放淫秽音频**。尤其是最后这个音频播放的设计，堪称"社死式勒索"的典型代表。想象一下，你的电脑突然开始大声播放不可描述的内容，而你又没法关掉它（任务管理器被禁用了），周围的人投来异样的目光……这种场景下，很多人可能宁可花五块钱买个清静。

攻击者留下的联系QQ号是 **368636048**。截至本文撰写时，该账号已无法被搜索到，搜索状态是异常（疑似被封禁）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQafAGt899r22gI6tqG62IKguyGpJSyDuK4M9GfIoQa7ZbwNvFcVlBLRpYiaa4A0s1y9erM0icqYEia5PkynO0B4cbeMnBWONO1b3c/640?wx_fmt=png&from=appmsg)

攻击者留下的QQ联系入口（该账号目前已无法搜索）

说起这个样本的整体风格，它的特征更有点复古。

这种复古感来自哪里？首先，它的加密方案用的是魔改DES，密钥硬编码在程序里，这在现代勒索软件中已经非常少见了。其次，它的勒索UI设计、倒计时机制、禁用任务管理器这些手法，都让我们想起了大约十年前Android平台上流行的那些锁机软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQaTasEwBibbuVFegj64l4lfo01Euq8msFQKqF3z1tApRzhibgt3L41AureWIR7ibsrfSWfJEhYwaXmH4HkBKAicdnb9A8Wr2Zq7c4E/640?wx_fmt=png&from=appmsg)

十年前安卓平台流行的锁机软件界面

当年的锁机软件多采用全屏置顶窗口覆盖系统界面，搭配倒计时和解锁码机制，与本次WannaHammer 3.0的设计思路高度相似。国内在2014年6月首次发现此类恶作剧锁屏样本（Android.TkLocker），2015年第三季度新增感染手机接近35万部，累计捕获样本7.6万余个。

那时候还没有现在这么成熟的勒索软件产业链，没有暗网博客、没有谈判门户、没有RaaS（勒索即服务）平台。攻击者的手法很直接：锁你屏幕、让你看着倒计时、给你一个QQ号或微信群让你交钱。WannaHammer 3.0的出现，某种程度上像是把当年那套"原始但有效"的玩法，重新搬回了Windows桌面端。

接下来，我们就把这个样本从外到里、从行为到原理，完整地拆开来看一看。

## 一、攻击流程一览

在深入技术细节之前，我们先通过一张流程图来理清WannaHammer 3.0的完整攻击链路。这张图也同步了我们Solar应急响应团队在处置此类事件时的标准流程。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQa0l5HqEkRjexKs4jSBsuh0GgfK9M5jI8fZgPG0famnlyfF6B7PBxpnBicMGRQ3PTfa4pTYBWMr2e9yOI1vfLKGIvEcTNIAJQdQ/640?wx_fmt=png&from=appmsg)

WannaHammer 3.0 攻击流程示意图

上图清晰展示了整个攻击的三个阶段：

**第一阶段：传播（社工钓鱼）**

攻击者通过被盗的QQ等即时通讯账号，以"熟人"身份向联系人投递恶意程序。常见的话术包装包括"老同学的照片"、"刷赞工具"、"游戏外挂"等，利用熟人关系降低受害者的警惕心理。

**第二阶段：感染（文件加密）**

受害者执行恶意程序后，样本以桌面目录为起点，递归遍历文件系统。对符合条件的文件（小于50MB且未包含`#WannaHammer#`后缀）使用内置的魔改DES算法进行加密，并在文件名后追加`.#WannaHammer#`扩展名。加密完成后，原始文件内容被完全覆盖。

**第三阶段：恐吓（勒索界面）**

样本弹出全屏勒索窗口，显示倒计时（24小时）、随机码、勒索说明和联系QQ号。同时禁用任务管理器、修改桌面壁纸，并在后台循环播放内嵌的淫秽音频，制造"社死"压力迫使受害者尽快付款。

**应急响应流程** 如果中招了，正确的处置顺序是：

1. **保留现场：**不要关闭勒索窗口（倒计时即将结束前建议直接关机，否则该加密器会自动删除文件），不要删除样本文件，不要运行杀毒软件（样本会提示"暂时退出杀毒软件"，但我们不建议听从）
2. **联系Solar：**通过Solar应急响应团队：`应急响应.com`官方渠道提交工单或直接下载解密程序（末尾有教程）
3. **提交信息：**打包加密文件、样本文件和系统日志安全提交
4. **解密处理：**使用专用解密工具尝试恢复文件（由于该样本加密方案存在明显缺陷，可实现无密码批量恢复）
5. **恢复成功：**验证文件完整性，重建业务环境

## 二、样本基础信息

这个样本的整体体量不算大，基本信息如下表所示：

| 项目 | 内容 |
| --- | --- |
| 原始文件名 | 585579225f1a66a9b727abdddac028ad9894bc8f6e06bc1461a4b8bec35841a5.exe.bin |
| 文件大小 | 12,242,944 字节（约11.7MB） |
| 文件类型 | Windows可执行程序（EXE） |
| 目标架构 | x86，32位，GUI程序 |
| 字节序 | 小端序（Little-Endian） |
| MD5 | ba57d2ef027df0f85ac9085ff44956ae |
| SHA1 | 367f2ec9c01578f25e99e700e8c7627472c892cc |
| SHA256 | 585579225f1a66a9b727abdddac028ad9894bc8f6e06bc1461a4b8bec35841a5 |
| 加密后缀 | .#WannaHammer# |
| 病毒家族 | WannaHammer 3.0 |

VT上多家引擎已能识别该样本，检测结果如下：

| 引擎名称 | 检测结果 |
| --- | --- |
| Avast | Win32:Malware-gen |
| AhnLab-V3 | Trojan/Win.Generic.C5576951 |
| ALYac | Gen:Variant.Tedy.512515 |
| Avira | TR/Ransom.imrnt |
| BitDefenderTheta | Gen:NN.ZexaF.36802.yq0@aSdxC8m |
| CrowdStrike Falcon | Win/malicious\_confidence\_100% (W) |
| Cylance | Unsafe |
| DeepInstinct | MALICIOUS |
| Emsisoft | Gen:Variant.Tedy.512515 (B) |
| ESET-NOD32 | A Variant Of MSIL/Filecoder.LU |
| GData | Gen:Variant.Tedy.512515 |
| Ikarus | Trojan.MSIL.Crypt |
| K7GW | Trojan (0052f4e41) |

从检测结果可以看出，主流安全厂商普遍将其归类为勒索软件（Ransom）或文件加密型恶意程序，置信度普遍较高。

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQY1X2WURajia2MCgCPjAws7f9oFryoM4u4VsNyluyTNfT5ozwERwZUMaC9LlfMlicS1icyBoDgqpkSRak77bnDuhlHzaEC3mnufDw/640?wx_fmt=png&from=appmsg)

思而听沙箱运行结果

## 三、勒索信内容全解析

WannaHammer 3.0的勒索信写得相当有个人风格，措辞随意、口语化严重，甚至带有一种莫名其妙的亲切感。为了便于分析，我们将勒索信的完整内容摘录如下，并逐段做解读。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQbdHAACqvBU8gpicOEUUaNsIWVw0OibKFa0YzXUjttdJqzhXCKoz1S8VgAhicWzMITgwnoSIUibic8Nn3cVkyW5iad6GJaY4S69aqGCY/640?wx_fmt=png&from=appmsg)

勒索信完整内容

```
我的电脑出了什么问题？
您的一些重要文件被我加密保存了。
照片、图片、文档、压缩包、音频、视频文件、exe文件等，几乎所有类型的文件都被加密了，因此不能正常打开。
这和一般文件损坏有本质上的区别，您大可在网上找找恢复文件的方法，我敢保证，没有我们的解密服务，就算老天爷来了也不能恢复这些文档。
有没有恢复这些文档的方法？
当然有可恢复的方法，只能通过我们的解密服务才能恢复，我以人格担保，能够提供安全有效的恢复服务。
但这是收费的，也不能无限期的推迟。
您点击“免费恢复”按钮可恢复一部分文件，你放心，我是绝对不会骗你的。
但想要恢复全部文档，需要付款点费用。
是否随时都可以固定金额付款，就会恢复的吗？当然不是，推迟付款时间越长对你不利。
最好3天之内付款费用，过了三天费用就会翻倍。
还有，一个礼拜之内未付款，将会永远恢复不了。
对了，忘了告诉你，对半年以上没钱付款的穷人，会有活动免费恢复，能否轮到到你，就要看您运气怎么样了。
我怎么付款？
请加我的QQ：368636048，向我发一张你电脑现在的照片（桌面），并且向我支付5元即可解锁。
要注意：付款后请将“解锁码”发给我！
收到作者给你的解锁密码后请填写在编辑框内，并且点击“解密被加密的文件”按钮，即可解密文件，解密时请耐心等待，如果您强行关闭软件可能导致部分文件永久损坏！！
最好周五晚上6点到八点或周末找我！
付款后，可立刻开始恢复工作。
怎么联系我？
如果你想解密的话请现在加我的QQ368636048
我强烈建议，为了避免不必要的麻烦，恢复工作结束之前，请不要关闭或者删除该软件，并且暂时退出杀毒软件。不管由于什么原因，万一该软件被删除了，很可能会导致付款后也不能恢复信息的情况。
```

关于这份勒索信，有几个值得研究的细节：

**第一，定价策略的心理学。** 五块钱的赎金定价非常微妙，它低到让大多数受害者不会为值不值得而犹豫，但又高到足以让攻击者在足够多的感染量下获得可观收益。这是一种典型的"薄利多销"思路，和当年锁机软件动辄索要20元、50元的定价相比，反而更符合当下互联网用户的付费心理阈值。

**第二，时间压力的阶梯式设计。** 三天翻倍、一周永久删除、半年"抽奖"免费恢复，这种层层递进的时间压力设计，本质上是在逼迫受害者尽快做出"花钱消灾"的决定。尤其是"半年以后抽奖免费"这个说法，更像是画饼，实际可操作性几乎为零。

**第三，"周五晚上六点到八点或周末找我"。** 这句话暴露了一个很有趣的信息，攻击者可能是一个需要正常上班的人又或者是在校的学生，只有下班和周末才有时间处理"业务"。这种作息规律，某种程度上也印证了该样本背后可能是一个个体攻击者或小团伙，而非成熟的组织化运营团队。

**第四，"暂时退出杀毒软件"的提示。** 这是典型的社会工程手法，试图让受害者在焦虑状态下主动降低系统安全防护，从而确保勒索程序能持续运行、不被查杀清除。

## 四、勒索界面与行为特征

当样本在受害者系统中运行后，会呈现以下行为特征：

### 4.1 全屏勒索窗口

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQZJA5d2U0PLaaZDDmmIT05uiaVZLq5Lcia4JZ0jSlnkCiatWiaPibGMzA2qguQnqCkiceHfdtj4Vy5Zzz7f0ldNrSyIxia6YIqhicHrJkE/640?wx_fmt=png&from=appmsg)

WannaHammer 3.0 勒索界面

### 4.2 倒计时与删除机制

样本在Windows目录下创建四个状态文件（`H.DDOS`、`M.DDOS`、`S.DDOS`、`X.DDOS`），分别用于记录倒计时的小时、分钟、秒和运行状态标记。定时器每秒递减，当倒计时归零后，样本会执行桌面目录的递归删除操作，将加密后的文件全部清除。

这种设计的目的很明确，给受害者施加"倒计时炸弹"式的心理压力，迫使其在规定时间内完成付款。

### 4.3 禁用任务管理器

样本通过修改注册表实现任务管理器的禁用：

```
HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System\DisableTaskMgr = 1
```

这意味着受害者无法通过常规的Ctrl+Shift+Esc或Ctrl+Alt+Del组合键调出任务管理器来终止勒索进程。对于普通用户来说，这几乎等同于束手无策。

### 4.4 桌面壁纸篡改

样本还会修改桌面壁纸，在桌面上留下明显的勒索提示信息，进一步强化心理威慑。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQanRxzM8vZW93AV0VAok4QFGKEHWdFlJHnUYwS2N1QMNrzkwWk0ZsEP2wRxf1NmibiaxVFia4LFv8nfdQiaWtTR8oqnJ1QLjQjJdz0/640?wx_fmt=png&from=appmsg)

被篡改的桌面壁纸

### 4.5 音频播放，最社死的一环

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQZlbjJ5bxVWicah4Qwr1W4xoUTbYbFgwYgtiadrzp4750wPKrG2Gd2TTYkQhCyXNq7yI87dSVxWboJL7sC3HcxsqRYSHMJUnb9uE/640?wx_fmt=png&from=appmsg)

样本内嵌音频资源提取信息

WannaHammer 3.0最恶毒的操作，是在勒索窗口打开后自动循环播放一段内容不堪入耳的国产淫秽音频。

这段音频并不是从外部下载的，而是以内嵌WAV资源的形式打包在程序文件中，资源标识为`iext2_IDR_WAVE1`。播放时通过`PlaySoundA`函数从程序资源区直接加载，使用`0x42007`标志参数，实现了不依赖外部文件、异步循环播放、失败静默的效果。

这意味着：

* 你在磁盘上找不到这个音频文件，它不存在于文件系统中
* 你无法通过删除文件来停止播放，数据在程序资源段里
* 它会在后台持续循环播放，直到你付款解密或强制关机

这个设计的恶毒之处不在于技术难度，而在于对**社交场景**的精准打击。无论是办公室、图书馆、教室还是家庭客厅，电脑突然开始大声播放不可描述的内容，受害者第一反应绝对不是"我要分析一下这个恶意样本"，而是"赶紧让它停下来"。五块钱的赎金在这种场景下，简直不能更划算了。

## 五、逆向分析

本节基于Solar应急响应团队对捕获样本的完整逆向分析，系统梳理WannaHammer 3.0的攻击链、技术原理及检测指标。以下所有分析结论均基于实际样本的静态分析和动态调试结果，分析环境为完全隔离的虚拟化沙箱。

### 5.1 样本概览

| 属性 | 值 |
| --- | --- |
| 文件类型 | Windows可执行程序（PE32） |
| 文件大小 | 约11.7MB（含内嵌音频资源） |
| 威胁类型 | 勒索软件 / 文件加密器 |
| 目标平台 |...