---
title: 攻击技术研判 | 使用蜂鸣器对抗沙箱检测技术
url: https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490989&idx=1&sn=22346fc6a4586c666c2eb23478d3cd83&chksm=c187ddbcf6f054aa17b85b2d007c2949b5a606a19423365c3992e302e44ef40a4de28196a447&scene=58&subscene=0#rd
source: M01N Team
date: 2023-03-14
fetch_date: 2025-10-04T09:31:10.075309
---

# 攻击技术研判 | 使用蜂鸣器对抗沙箱检测技术

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwYSKT7e5OKt5ozRt570BMNu9TnSDFoialgXnIkjEw069F8B2mKgRy9giayuFpP0djicJ9wtDGbk9GCkg/0?wx_fmt=jpeg)

# 攻击技术研判 | 使用蜂鸣器对抗沙箱检测技术

原创

天元实验室

M01N Team

![](https://mmbiz.qpic.cn/mmbiz_gif/TPGibEO8KBwZvROFrVKkiby4AnglO8exsibQg9RxafrNUaIwQ0YnauYla1SwNXJibBGlibMlJKdsMvERMzFw1Qs3KibQ/640?wx_fmt=gif)

**情报背景**

近期，MINERVA安全团队发现了一些相似的新样本，在这些样本中存在着大量的反分析技术和防御规避技术，其最终目的是释放勒索病毒实现勒索攻击。在大量的反分析技术中，存在着较为少见的沙箱对抗技术。本文将对该技术进行剖析和扩展。

|  |  |
| --- | --- |
| **组织名称** | 无 |
| **相关工具** | Beep |
| **战术标签** | 防御规避 |
| **技术标签** | 沙箱检测对抗 |
| **情报来源** | https://minerva-labs.com/blog/beepin-out-of-the-sandbox-analyzing-a-new-extremely-evasive-malware/ |

**01** 攻击技术分析

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZvROFrVKkiby4AnglO8exsibVC3N5fPCkJ8fMwKA9aRlNLnUSU0BzR7Ahufjq2rafWiafc03eZyap8w/640?wx_fmt=png)

攻击过程如下:

1. 在经过反调试和反虚拟机检测后，恶意程序创建互斥变量；
2. 设置注册表并写入一个base64编码数据，其内容为一个base64后的powershell脚本；
3. 执行解码后的powershell脚本实现下载又一段payload,并调用regsvr32.exe执行，同时创建任务计划作持久化:间隔执行该powershell脚本；
4. 将shellcode注入至WWAHost.exe中并执行，并使用父进程欺骗技术，将explorer.exe 设置为 WWAHost.exe 的父进程；
5. payload 进行信息收集并下发勒索软件，实施勒索攻击,达到攻击目的；

**亮点 利用蜂鸣器实现延时执行 对抗沙箱检测**

出于性能考虑，沙箱在执行程序时不可能长时间等待程序执行，因此也衍生出了 延时执行的反沙箱技术：利用Windows API sleep 实现休眠，致使沙箱不执行恶意程序，进而绕过沙箱检测。

同时，沙箱开发者也通过hook Api的方式，缩短或绕过sleep的时间，对抗此类反沙箱技术。

现如今也存在着五花八门的API调用实现延迟执行恶意代码的效果，如: WaitForSingleObject、NtWaitForSingleObject、SetTimer、SetWaitableTimer、CreateTimerQueueTimer、socket 中的select函数等

而在本次事件中，攻击者利用了蜂鸣器API Beep 实现了延迟执行，较为少见。

根据MSDN可知，Beep函数如下：

```
BOOL Beep(  [in] DWORD dwFreq,  # 声音频率，赫兹为单位  [in] DWORD dwDuration # 声音的持续时间，毫秒为单位);
```

其功能为：执行可警告的代码，并且在声音结束之前不会将控制权返回给其调用者。

这也就意味着：根据设定的声音时间长短，程序会在声音结束前暂停其他功能函数的执行，从而达到和Sleep API 一样的功能，实现延迟执行的反沙箱技术。其中，原本用于告警的蜂鸣声也可以通过设置低频和短暂的时间间隔，达到听不见警报音的效果。

示例代码如下: 实现5分钟延迟执行

```
#include <Windows.h>#include <stdio.h>// 调用Beep 实现延迟执行int time_Beep(){// 设置延迟 300000毫秒 5分钟int wh_compter = 0;int wh_total = 300000;
while(wh_compter < wh_total){Beep(2, 1); // 2hertz, 1ms 设置低频和短暂的间隔时间实现听不见蜂鸣声wh_compter++;}
if(wh_compter > wh_total - 1)return 1;
return 0;}
int main(){if(time_Beep())printf("调用Beep 延迟执行成功 \n");elseprintf("调用Beep 延迟执行失败 \n!");
return 0;}
```

执行成功，实现延时执行。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZvROFrVKkiby4AnglO8exsib3LXnQpJsR2fgNiaYY1ibt9yx7oibRfFHAfnKW8wrq7TZicRUILahhsXhaQ/640?wx_fmt=png)

**延时执行组合技**

利用Beep API实现延时执行，对现有hook Sleep函数进行检测对抗的沙箱而言，具有一定的防御规避效果，可作为沙箱对抗检测技术中的一部分。随着沙箱的持续升级，hook beep函数解决延时执行的功能也会随之出现。

因此，在单个API 进行延时执行被绕过的攻防场景下，利用多个延时执行API，实现的反沙箱检测技术显得更为稳固。比如下图思路：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZvROFrVKkiby4AnglO8exsibibZLt5Yiaxlzcv0EG10A8YCuia26oGmXVWkhWcJHiaSJRSre8DXxIqIy1g/640?wx_fmt=png)

1. 使用GetTickCount64记录首个时间戳，记录起始执行程序的时间；
2. 多次循环调用sleep 函数 和 beep 函数 实现 延时执行；
3. 再一次调用GetTickCount64记录时间戳，并比较。如果 GetTickCount64[2] - GetTickCount64[1] 的时间少于sleep与beep延时调用的时间，说明程序的sleep 或者 beep的API被hook,判定程序处于沙箱环境中，则退出程序；

**02**总结

本文对利用蜂鸣器Beep的沙箱检测对抗技术进行了简要分析，并探讨了延时执行的攻防对抗作为沙箱检测的长期话题。从终端产品检测防御角度考虑，我们不仅需要考虑对Beep函数及其异常参数进行检测，还要考虑面对组合技时的防御检测机制，以应对沙箱检测对抗手段。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZvROFrVKkiby4AnglO8exsibeoj7U94neHyibZdZ42gErKV4kEwPibuWOOAvUQbsWDhdazeKPAnEcugg/640?wx_fmt=png)

**绿盟科技天元实验室**专注于新型实战化攻防对抗技术研究。

研究目标包括：漏洞利用技术、防御绕过技术、攻击隐匿技术、攻击持久化技术等蓝军技术，以及攻击技战术、攻击框架的研究。涵盖Web安全、终端安全、AD安全、云安全等多个技术领域的攻击技术研究，以及工业互联网、车联网等业务场景的攻击技术研究。通过研究攻击对抗技术，从攻击视角提供识别风险的方法和手段，为威胁对抗提供决策支撑。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwZvROFrVKkiby4AnglO8exsibCJFD4via13e6UnA0B8EoNwgWxqspZJHpMvFibbGGGfph11a2L8NAxFPg/640?wx_fmt=jpeg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZvROFrVKkiby4AnglO8exsibibXUPtK4MRNxP2ib6tia1MTuzibWgqQiaiaH4Y4rBU4g1Mtp0BLkdE9HtGMQ/640?wx_fmt=png)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

**往期推荐**

[攻击技术研判 | Earth Kitsune滥用vcruntime140.dll和Chrome扩展等实现持久化](http://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490905&idx=1&sn=2c1426495bfdc73b5ca85a0dfba899c6&chksm=c187dd48f6f0545e04c5a10a2a04126f7ff9671068053f09eb8cf50e9401c5fc30597b6f86a3&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZvROFrVKkiby4AnglO8exsiblCJPw4AI7jI6ZKDicaBQbjiaNQvp3p7zWMmG8dDuXmQtfT7k2zOCBJyg/640?wx_fmt=png)

[攻击技术研判 | 曝光一周年，向日葵RCE漏洞在野利用再现](http://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490787&idx=1&sn=a87fa18a4b7e8e4b01b67abd9a8c0c51&chksm=c187dcf2f6f055e41de2982d637ae09a257cacf3e7bf2b23fcfcded679911d1682d49a5485ba&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZvROFrVKkiby4AnglO8exsiblCJPw4AI7jI6ZKDicaBQbjiaNQvp3p7zWMmG8dDuXmQtfT7k2zOCBJyg/640?wx_fmt=png)

[攻击技术研判 | 针对仿真与静态分析的代码混淆技术](http://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490716&idx=1&sn=67da0e3f8d1a52c4a2b12d9568ae29e4&chksm=c187dc8df6f0559b355bee3d28817da818cbfd3bb795c2644e9aef6036cf4f244a14a0a681f1&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZvROFrVKkiby4AnglO8exsiblCJPw4AI7jI6ZKDicaBQbjiaNQvp3p7zWMmG8dDuXmQtfT7k2zOCBJyg/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

M01N Team

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

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