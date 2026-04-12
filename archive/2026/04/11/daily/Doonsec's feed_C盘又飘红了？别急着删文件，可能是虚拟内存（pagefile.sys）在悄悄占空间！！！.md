---
title: C盘又飘红了？别急着删文件，可能是虚拟内存（pagefile.sys）在悄悄占空间！！！
url: https://mp.weixin.qq.com/s/dbdHEm5D8tVqUKWlC9vjhQ
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:46:14.611193
---

# C盘又飘红了？别急着删文件，可能是虚拟内存（pagefile.sys）在悄悄占空间！！！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquMo9aqu5EFnlmr7BfaysrR506oDQ1QPXArZxYVhl5XLOf9BCu3NaPeD7d4qXWm8ohYjToptBTScBc24lCSqtb3rKQibRYtyXYTM/0?wx_fmt=jpeg)

# C盘又飘红了？别急着删文件，可能是虚拟内存（pagefile.sys）在悄悄占空间！！！

阿伟
阿伟

船山信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**C盘又飘红了？别急着删文件，可能是虚拟内存（pagefile.sys）在悄悄占空间。作为系统性能的关键设置，虚拟内存放在C盘还是D盘更合理？今天从技术角度帮你理清windows虚拟内存怎么设置这个问题，并提供一套完整的C盘瘦身方案。**

****一、虚拟内存设置在C盘好还是D盘？电脑C盘和D盘的区别****

在探讨“虚拟内存设置在哪个盘”之前，我们先理清电脑c盘和d盘的本质区别。

C盘是系统盘，承载着Windows操作系统和核心驱动程序，其读写效率直接影响系统响应速度；

D盘则是数据盘，主要用于存放个人文件和非系统级应用程序。基于这一基础，虚拟内存（即页面文件pagefile.sys）的存放位置选择，其实并没有绝对的“好”与“不好”，关键取决于你的硬盘类型和C盘剩余空间。

为了更直观地对比两种选择的利弊，我整理了一个表格，方便你对号入座：

![虚拟内存设置在c盘好还是d盘1](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquOVARE2gKHc3EbAVPInibEddt0aNmDXvfx1ic9ictwuaTgf0zG2s6zr6Jd3b7MswwlbCrkTJhyEyLMPkZqPRh1tbPYuDvguFU5Zvs/640?wx_fmt=png&from=appmsg)

**那么，具体该怎么选？**

根据你的实际情况对号入座，可以更精准地做出决策：

### 情况一：C盘空间充足（例如剩余50GB以上），且是固态硬盘（SSD）

→ 建议留在C盘。这样既能享受最快的读写速度，也无需额外设置，保持系统默认即可。

### 情况二：C盘空间紧张（经常飘红）

→ 强烈建议将虚拟内存迁移到D盘。这是缓解C盘空间不足、防止系统因磁盘满载而变慢的有效方法之一。

### 情况三：C盘和D盘都是固态硬盘（SSD）

→ 选择剩余空间较大的那个盘。因为固态硬盘速度较快，放在两个盘性能差异不大，优先保证有足够空间容纳虚拟内存和后续文件增长即可。

**✅特别提醒：**如果你的C盘是机械硬盘（HDD），而D盘是固态硬盘（SSD），建议直接在D盘重装系统，将操作系统和虚拟内存都放在更快的SSD上。这样做能从根源上提升整体运行体验，远胜于仅迁移虚拟内存。如果暂时无法重装，那么将虚拟内存移到D盘（SSD）也是可选的折中方案，但系统盘（C盘）依然是HDD，整体性能瓶颈依然存在。

## 二、C盘虚拟内存可以删除吗？

**直接的回答是：不建议彻底删除虚拟内存**，但可以将它转移到其他分区，从而安全释放C盘空间。

### （一）为什么不建议完全删除虚拟内存？

1️⃣ 系统崩溃的“救命稻草”：当物理内存（内存条）不够用时，虚拟内存充当溢出缓冲区。如果彻底禁用，一旦运行大型程序或多任务，系统可能直接弹出“内存不足”的错误，甚至导致正在编辑的文档来不及保存就崩溃。

2️⃣ 故障诊断的必要文件：Windows在蓝屏时，需要虚拟内存来存储“故障转储文件”。如果没有这个文件，你蓝屏后连问题原因都查不到，只能干瞪眼。

3️⃣ 性能瓶颈的转移而非解决：禁用虚拟内存并不能提升电脑速度，只是把压力全部转嫁给物理内存。当物理内存满载时，系统会变得异常卡顿甚至死机。

### （二）如何清理电脑C盘内存？（实用方法合集）

既然不能删除，那我们该如何清理电脑c盘内存？下面提供四种经过2026年验证的实用方法，既有系统自带功能，也有更高效的软件方案。

#### 方法一：手动转移虚拟内存

⭐ 适用场景：C盘经常爆红，且你希望从根源上移走这个大文件。

✅ 成功概率：100%，但需重启生效。

**操作步骤：**

1.右键点击“此电脑”，选择“属性” -> 点击左侧的“高级系统设置”。

2.在弹出的窗口中，点击“高级”选项卡，在“性能”栏点击“设置”。

3.在性能选项窗口中，再次点击“高级”选项卡，然后在“虚拟内存”栏点击“更改”。

![虚拟内存设置在c盘好还是d盘2](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquMWt9N2ylicrmg7wBHLBoqBsXzaSxpYJFNPCibicQicFs3egtHuFzq5UWrdoHwicVPF1uzrgrn3NZjkhkAZ3ba2bBv6wV6BQzYicqj6s/640?wx_fmt=png&from=appmsg)

4.关键一步：取消勾选“自动管理所有驱动器的分页文件大小”。先选中C盘，然后勾选“无分页文件”，点击右边的“设置”按钮（这步是清除C盘的设置）。

![虚拟内存设置在c盘好还是d盘3](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquM9Pp67D5BjUINua2LbNPERo3NcYOqSOjhcXtkXW0JGsXN05RDT9LKF0gtEzESyTa58k4SQ0Ub2tx1eXCOJacHvyJVGVJibQiaI4/640?wx_fmt=png&from=appmsg)

5.选中D盘，勾选“系统管理的大小”或“自定义大小”。如果选择自定义，参考值：初始大小为物理内存的1.5倍，最大值为物理内存的3倍（例如16GB内存，可设初始24576MB，最大49152MB）。点击“设置”确认。

6.一路点击“确定”，系统会提示重启电脑。重启后，C盘根目录下的pagefile.sys就消失啦。

![虚拟内存设置在c盘好还是d盘4](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquMzaKkSX7UbrzGN0KibdWs0HvDrCJw7tUYO4DicibiaZ6epb4SuXdIHIvZ4YrNmGmBm86QUjp3ib2nKPdZ4ibv7leaEjwnRyu4Cav63E/640?wx_fmt=png&from=appmsg)

**权威提示：**操作前确保D盘至少有20-30GB的剩余空间，且D盘最好是固态硬盘。如果D盘是机械硬盘，迁移后读写速度可能下降，反而影响系统响应。

#### 方法二：使用系统自带工具深度清理

⭐ 适用场景：日常维护，删除临时文件、更新补丁备份。

✅ 成功概率：通常能清理出5-15GB空间。

**操作步骤：**

1.按下键盘上的Win+R组合键，调出运行对话框。在输入框中输入cleanmgr，然后按下回车。

2.选择你想要清理的磁盘驱动器（比如C盘），等待扫描完成。扫描后点击左下角的“清理系统文件”。

3.在列表中，重点勾选“Windows更新清理”、“临时文件”、“传递优化文件”等大项。

4.点击“确定”，耐心等待清理完成。这能删除Windows.old等升级遗留的“庞然大物”。

![虚拟内存设置在c盘好还是d盘8](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquOavibaEHqXgBP3eghe3KV8BeEvT34rpcibVnjhAKQicdYGKWfFic08BFGGgbfZTkGsu2xLa0reYNAKFeL085BPl7GXibxr11vricLaI/640?wx_fmt=png&from=appmsg)

#### 方法三：开启存储感知

⭐ 适用场景：不想手动操作，希望电脑自己保持清洁。

✅ 成功概率：长期有效，预防空间积压。

**操作步骤：**

1.按Win + I打开“设置”，进入“系统” -> “存储”。

2.打开“存储感知”开关。

![虚拟内存设置在c盘好还是d盘9](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquOhzVEQ5twDfBRKTcZ58n6Au6nt9FGicQiamK41jIicicLJMO1p2N3gaWQkZBm8tX0NxfclyERkBwcm7emqPTLQNXWpL2Z3D9KPw0E/640?wx_fmt=png&from=appmsg)

3.勾选“清理临时文件”和“自动用户内容清除”，设置“配置清理计划”，可设置运行频率为“每周”。

4.系统会自动在后台清理垃圾，保持C盘健康。

![虚拟内存设置在c盘好还是d盘10](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquPRQozhN7vxAfHvLuHPS8YR8CyRkT7BqibFZibOetJBiaJs2B2nKM9Lm6PRvDScnI3wFgC1Hm9xvg2lfptic6vicliaxFISCtpnzXWFs/640?wx_fmt=png&from=appmsg)

## 三、windows虚拟内存怎么设置？2026最新图解指南

### ▶虚拟内存设置步骤分解：

**1.入口：**右键“此电脑” -> “属性” -> “高级系统设置” -> “性能”栏的“设置” -> “高级” -> “虚拟内存”的“更改”。

![虚拟内存设置在c盘好还是d盘11](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquPibicJanFJpIPqABmW3zVuOAf4bLIV33PQn0wFsdb2Lic7LLGWUc2FfyVFPyicK59ajp4ky0wJLNFpCCEoKLG3Ww2zgVibJ1Cmga7A/640?wx_fmt=png&from=appmsg)

![虚拟内存设置在c盘好还是d盘12](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquNvP2u8k6QNub8BDPmR1b7YdkZKpQJ3KpavHby58ugut82jkEXL9YYZOJDApNurB8SQCyWdxAf79VjNnXqdOGnyrrNvzpibe7tg/640?wx_fmt=png&from=appmsg)

**2.逻辑：**必须遵循“先清后设”的原则。

* 先选C盘 -> 设为“无分页文件” -> 点击“设置”（生效）。
* 再选D盘 -> 设为“自定义大小”或“系统管理的大小” -> 点击“设置”（生效）。

**3.大小建议：**

* 8GB内存用户：初始设为8192MB - 12288MB，最大值设为16384MB - 24576MB。
* 16GB内存用户：初始设为12288MB - 16384MB，最大值设为24576MB - 32768MB。
* 32GB及以上内存用户：可以适当调小，甚至设置为“系统管理的大小”，因为物理内存已经非常充裕了。

**注意事项：**最大值不宜设置为“无限制”，以防异常进程耗尽磁盘空间。设置前请确保目标驱动器有充足剩余空间（建议至少为虚拟内存最大值的1.2倍）。

![虚拟内存设置在c盘好还是d盘13](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquOPhFnXVr891bAttIlxmHk4yrNqJtg9YadAUMtR5HHzWFZxTagO1iacGc082a8QNa8nJ35VrwH6hTYNvMvTlVic5NhNoQNKljDp4/640?wx_fmt=png&from=appmsg)

## 四、高频问题解答FAQ

**Q1：我把虚拟内存移到了D盘，C盘里还有一个hiberfil.sys文件能删吗？**

A：可以。hiberfil.sys是休眠文件。如果你从不使用“休眠”模式（注意不是睡眠），在命令提示符（管理员）中输入 powercfg /h off 即可删除它，瞬间释放与内存大小相当的C盘空间。

**Q****2：设置虚拟内存后，D盘****空间变小了，会影响D盘文件存储吗？**

A：虚拟内存文件（pagefile.sys）在D盘根目录是隐藏的，会固定占用你设定的“初始大小”的空间。如果你的D盘容量本身就不大（比如只有100GB），建议将虚拟内存大小适当调小，或交由“系统管理”，避免D盘也变红。

**Q3：为什么我设置了自定义大小，系统运行反而变慢了？**

A：这通常是因为“初始大小”设得太小。当系统需要更多虚拟内存时，会频繁去扩展“最大值”，这种动态扩展的过程非常消耗资源，导致卡顿。建议将初始大小设得高一些（如内存的1.5倍），减少动态扩展的频率。

**Q4：我的C盘是SSD，D盘是HDD，到底该放哪里？**

A：这种情况下，建议将虚拟内存留在C盘（SSD）。因为虚拟内存需要频繁读写，放在慢速的HDD上会拖慢整个系统的响应速度。如果C盘空间实在紧张，可以考虑升级C盘容量或增加一条内存条，减少对虚拟内存的依赖。

**Q5：虚拟内存可以设置在移动硬盘或U盘上吗？**

A：绝对不建议。移动硬盘和U盘的读写速度远低于内置硬盘，且通过USB接口传输延迟高，会导致系统异常卡顿。同时，如果意外断开连接，系统会立即崩溃。

虚拟内存放C盘还是D盘，关键看硬盘类型和空间。若C盘紧张且D盘是SSD，建议迁移；定期维护，能有效释放空间。以上就是关于虚拟内存设置在c盘好还是d盘的解答，希望对你有帮助！

参考链接：

https://www.callmysoft.com/support/7755.html#mao0

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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