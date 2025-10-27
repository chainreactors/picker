---
title: [2024]制作任意签名者的数字签名证书
url: https://key08.com/index.php/2024/05/08/1897.html
source: 白帽Wiki - 一个简单的wiki
date: 2024-05-09
fetch_date: 2025-10-06T17:16:20.137142
---

# [2024]制作任意签名者的数字签名证书

[![](https://key08.com/avatar_pack.gif)](https://key08.com/)

# 白帽Wiki

从2012年开始专注高级网络安全技术研究

查你所想

![](https://key08.com/avatar_pack.gif)

### 一只鸭子

* [首页](https://key08.com/)
* [板块活动记录](https://key08.com/index.php/1596.html "板块活动记录")
* [IDA Internal](https://key08.com/index.php/2365.html "IDA Internal")
* [EDR开发相关](https://key08.com/index.php/project_ayy_waf.html "EDR开发相关")
* [威胁追踪](https://key08.com/index.php/cve_detect.html "威胁追踪")
* [Hypervisor](https://key08.com/index.php/hypervisor_code.html "Hypervisor")
* [机器学习&神经网络](https://key08.com/index.php/keras.html "机器学习&神经网络")
* [EFI驱动编写](https://key08.com/index.php/EFI_Driver_Code.html "EFI驱动编写")
* [关于&联系方式](https://key08.com/index.php/215273185.html "关于&联系方式")

×

# [白帽Wiki - 一个简单的wiki](https://key08.com/)

## [[2024]制作任意签名者的数字签名证书](https://key08.com/index.php/2024/05/08/1897.html)

[huoji](https://key08.com/index.php/author/1/)
 [数字签名](https://key08.com/index.php/tag/%E6%95%B0%E5%AD%97%E7%AD%BE%E5%90%8D/),[zheng'sh](https://key08.com/index.php/tag/zheng-sh/)
 2024-05-08
 1294 次浏览
 0 次点赞

### 简介
自制证书,CA链不可信.
一般这种证书在软件开发领域是为了测试目的,在没加入系统证书之前,是\*\*不可信的\*\*，这个工具很常见,软件开发领域非常常见的工具
### 教程
下载这个工具
https://github.com/chris2511/xca/releases/
下载完后点创建证书
![](https://key08.com/usr/uploads/2024/05/3610405338.png)
主要需要填的是主体这里,这里是显示的,为了方便,我瞎JB填的.
![](https://key08.com/usr/uploads/2024/05/1588651117.png)
然后就可以打了,打之前需要加到系统信任证书里面才可以打
效果就这样
![](https://key08.com/usr/uploads/2024/05/3704170040.png)
不过这个证书别想干坏事了, 因为这个只在本机生效,其他机器不会信任,除非用户点确定加入到信任证书里面.

![](https://key08.com/usr/themes/GreenGrapes/img/creativecommons-cc.png)

本文由 [huoji](https://key08.com/index.php/author/1/) 创作，采用 [知识共享署名 3.0](http://creativecommons.org/licenses/by/3.0/cn)，可自由转载、引用，但需署名作者且注明文章出处。

 点赞 0

* 上一篇: [[2024]用EDR剖析流行黑产组织对抗安全软件的多重手段](https://key08.com/index.php/2024/05/02/1888.html "[2024]用EDR剖析流行黑产组织对抗安全软件的多重手段")
* 下一篇: [[2024]imgui win11主题](https://key08.com/index.php/2024/05/08/1904.html "[2024]imgui win11主题")

还不快抢沙发

[取消回复](https://key08.com/index.php/2024/05/08/1897.html#respond-post-1897)

添加新评论

提交评论

![icon_mrgreen.png](https://key08.com/usr/plugins/Smilies/tieba/icon_mrgreen.png)![icon_neutral.png](https://key08.com/usr/plugins/Smilies/tieba/icon_neutral.png)![icon_twisted.png](https://key08.com/usr/plugins/Smilies/tieba/icon_twisted.png)![icon_arrow.png](https://key08.com/usr/plugins/Smilies/tieba/icon_arrow.png)![icon_eek.png](https://key08.com/usr/plugins/Smilies/tieba/icon_eek.png)![icon_smile.png](https://key08.com/usr/plugins/Smilies/tieba/icon_smile.png)![icon_confused.png](https://key08.com/usr/plugins/Smilies/tieba/icon_confused.png)![icon_cool.png](https://key08.com/usr/plugins/Smilies/tieba/icon_cool.png)![icon_evil.png](https://key08.com/usr/plugins/Smilies/tieba/icon_evil.png)![icon_biggrin.png](https://key08.com/usr/plugins/Smilies/tieba/icon_biggrin.png)![icon_idea.png](https://key08.com/usr/plugins/Smilies/tieba/icon_idea.png)![icon_redface.png](https://key08.com/usr/plugins/Smilies/tieba/icon_redface.png)![icon_razz.png](https://key08.com/usr/plugins/Smilies/tieba/icon_razz.png)![icon_rolleyes.png](https://key08.com/usr/plugins/Smilies/tieba/icon_rolleyes.png)![icon_wink.png](https://key08.com/usr/plugins/Smilies/tieba/icon_wink.png)![icon_cry.png](https://key08.com/usr/plugins/Smilies/tieba/icon_cry.png)![icon_surprised.png](https://key08.com/usr/plugins/Smilies/tieba/icon_surprised.png)![icon_lol.png](https://key08.com/usr/plugins/Smilies/tieba/icon_lol.png)![icon_mad.png](https://key08.com/usr/plugins/Smilies/tieba/icon_mad.png)![icon_sad.png](https://key08.com/usr/plugins/Smilies/tieba/icon_sad.png)![icon_exclaim.png](https://key08.com/usr/plugins/Smilies/tieba/icon_exclaim.png)![icon_question.png](https://key08.com/usr/plugins/Smilies/tieba/icon_question.png)

![选择表情](https://key08.com/usr/plugins/Smilies/tieba/icon_smile.png)

[![](https://img.buymeacoffee.com/button-api/?text=Trust Feature For Human Duck&emoji=&slug=huoji&button_colour=16a085&font_colour=ffffff&font_family=Cookie&outline_colour=ffffff&coffee_colour=FFDD00)](https://www.buymeacoffee.com/huoji)

* [最新Wiki](#sidebar-new)
* [最新评论](#sidebar-comment)
* [随机Wiki](#sidebar-rand)

* [[2025]中外AI大战!让AI们通过MCP玩帝国时代2](https://key08.com/index.php/2025/10/04/2816.html)
* [[2025]"ucpd.sys后门事件"详细分析技术报告-他是后门.....吗?](https://key08.com/index.php/2025/09/18/2815.html)
* [[2025]阻止漏洞驱动利用(byovd)技术致盲安全软件](https://key08.com/index.php/2025/09/15/2785.html)
* [[2025]深入研究R3通过网络(WFP架构)致盲EDR的技术原理与解决方案](https://key08.com/index.php/2025/08/31/2761.html)
* [[2025]从0制作IDA的F5代码还原功能(hex-rays插件) 上](https://key08.com/index.php/2025/08/12/2731.html)
* [[2025]VMP源码学习——变异分析](https://key08.com/index.php/2025/07/31/2729.html)
* [[2025]SleepDuck-通用堆栈欺骗检测POC,检测SleepMask](https://key08.com/index.php/2025/07/13/2716.html)
* [[2025]聊一下企业内网中办公网终端的EDR安全运营](https://key08.com/index.php/2025/07/06/2697.html)
* [[2025]Windows的内存防护机制](https://key08.com/index.php/2025/06/23/2688.html)
* [[2025]windbg ttd restore dotnet jit protection exploration](https://key08.com/index.php/2025/06/18/2683.html)
* [[2025]PE代码执行虚拟机详解&原理&源码](https://key08.com/index.php/2025/06/16/2663.html)
* [[2025] Introduction to IDA's Internal Principles (Part 4): function parameter number calc](https://key08.com/index.php/2025/05/18/2560.html)
* [此内容被密码保护](https://key08.com/index.php/2025/05/14/2549.html)
* [此内容被密码保护](https://key08.com/index.php/2025/05/13/2545.html)
* [此内容被密码保护](https://key08.com/index.php/2025/05/09/2541.html)

* 安全小白：[”标准的导出表hook:“打错字了师傅](https://key08.com/index.php/2025/09/15/2785.html/comment-page-1#comment-213)
* 电脑维修：[学到了](https://key08.com/index.php/2021/11/15/1394.html/comment-page-1#comment-212)
* 1：[内容被隐藏](https://key08.com/index.php/2025/05/06/2507.html/comment-page-1#comment-211)
* anon：[鸭总操我](https://key08.com/index.php/2025/04/15/2424.html/comment-page-1#comment-210)
* huojifans：[从加载hid.dll开始后面就是SteamTools的操作](https://key08.com/index.php/2025/01/03/2330.html/comment-page-1#comment-209)
* jijiyaya：[怎么十多年了，感觉没啥长进啊](https://key08.com/index.php/215273185.html/comment-page-1#comment-208)
* ikun：[用户喜欢装N款安全软件，兼容爆炸](https://key08.com/index.php/2024/11/23/2268.html/comment-page-1#comment-207)
* huoji：[看了一下，确实有那片文章。但是那个不是本人。我对他们的言论不负责...](https://key08.com/index.php/2021/03/05/945.html/comment-page-1#comment-206)
* k：[知网上的这篇论文用的您的图片及数据](https://key08.com/index.php/2021/03/05/945.html/comment-page-1#comment-205)
* huoji：[不是 我不是搞学术的](https://key08.com/index.php/2021/03/05/945.html/comment-page-1#comment-204)

* [此内容已经被删除](https://key08.com/index.php/2020/07/23/728.html "此内容已经被删除")
* [[2022]从微软代码中学习C/C++项目代码规范](https://key08.com/index.php/2022/01/12/1430.html "[2022]从微软代码中学习C/C++项目代码规范")
* [[2017]恶意代码的启发式检测技术研究](https://key08.com/index.php/2019/11/09/199.html "[2017]恶意代码的启发式检测技术研究")
* [此内容已经被删除](https://key08.com/index.php/2019/11/12/278.html "此内容已经被删除")
* [[2023]VMP还原day4:简单计算vm block跳转地址](https://key08.com/index.php/2023/04/16/1740.html "[2023]VMP还原day4:简单计算vm block跳转地址")
* [[2024]深度了解现代安全软件对抗与缓解措施](https://key08.com/index.php/2024/11/23/2268.html "[2024]深度了解现代安全软件对抗与缓解措施")
* [此内容已经被删除](https://key08.com/index.php/2020/03/10/635.html "此内容已经被删除")
* [[2025] Introduction to IDA's Internal Principles (Part 4): function parameter number calc](https://key08.com/index.php/2025/05/18/2560.html "[2025] Introduction to IDA's Internal Principles (Part 4): function parameter number calc")
* [此内容已经被删除](https://key08.com/index.php/2019/12/02/358.html "此内容已经被删除")
* [[2021]PatchGuard的 sub\_1403DA6F0 回调研究(二)](https://key08.com/index.php/2021/08/01/1282.html "[2021]PatchGuard的 sub_1403DA6F0 回调研究(二)")

友情链接

* [幽灵网安](https://bbs.wghostk.com)
* [vxjump](http://www.vxjump.net/)
* [华域联盟](https://www.cnhackhy.com/)
* [Nuclear'Atk](https://lcx.cc/)
* [吾爱漏洞](http://www.52bug.cn/)
* [游侠安全网](http://www.youxia.org/)
* [黑客导航](http://www.hac-ker.com/)
* [安云网](http://www.anyun.org/)
* [MD5超级解密](http://www.ttmd5.com/)
* [IT同路人导航](https://www.id05.com/)
* [FAKE-CHEATER](https://blog.renjing.wang/)
* [anti-debug](https://anti-debug.checkpoint.com...