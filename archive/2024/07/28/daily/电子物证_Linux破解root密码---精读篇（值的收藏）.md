---
title: Linux破解root密码---精读篇（值的收藏）
url: https://mp.weixin.qq.com/s?__biz=MzAwNDcwMDgzMA==&mid=2651047718&idx=1&sn=01c5289e0719bb946d12b52f9297aa50&chksm=80d088d7b7a701c178e91d8df70db350cb8f1e7f163cb68d65438cb8656a2b610a97fe6a8272&scene=58&subscene=0#rd
source: 电子物证
date: 2024-07-28
fetch_date: 2025-10-06T17:41:32.572808
---

# Linux破解root密码---精读篇（值的收藏）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dDhDhftpRFuTQicq2FdMdavj4N1NITYiaavasevQsFA3pWxanMpTQxx7uAFSYyetCFkic3KTsdpSzrfib0iaDibxTCGQ/0?wx_fmt=jpeg)

# Linux破解root密码---精读篇（值的收藏）

电子物证

以下文章来源于火华子1016
，作者火华子1016

![](http://wx.qlogo.cn/mmhead/QnM5bMcic4Z12O9KAc0QzWp4A55XkUVX2HBynomKUMIic9CO55FPIhDmNibhYn4AdPWHXV7MJJd1dw/0)

**火华子1016**
.

C语言、JAVA语言、Python、shell脚本、Linux操作系统

Linux破解root密码---精读篇（值的收藏）

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/JhdS4IP8ocGRmgSlJFNBribjpzd8bE1ex15FPyMmSLHs5nQAE1ek3PED35MfzVyD7exkvvw6KVAribib9h0B7WTTA/640?wx_fmt=jpeg)

****图片来源：福建省·福州市·鼓楼区·三坊七巷****

---

**【前言】**

    忘记密码，真的是在生活中在常见的不过的事情了，不知道宝子们平时是如何保存自己的密码，或者是如何设计自己的密码，才不会让在需要的时候忘记，但各种密码实在太多，时间一久，忘记是在正常不过的事情了。

    在Linux中，忘记root密码还是可以重置或者是破解的，通过**rd.break**内核参数或者init=/bin/bash采用bash环境来处理即可,本篇小编则为大家娓娓道来。

**【目录】**

**一 使用rd.break破解root密码**

**二 **破解root密码的原理解释****

**三 优化修改密码后的启动时间**

**四 使用bash破解密码**

**五 总结**

**一 **使用rd.break破解root密码****

    开机启动，显示如下界面

![](https://mmbiz.qpic.cn/mmbiz_png/JhdS4IP8ocGRmgSlJFNBribjpzd8bE1exycSQggWbpNtUwZfhcRXrjicMeZ2BNicJKhiaP8H1xwkXD81HmyLoY9BVg/640?wx_fmt=png&from=appmsg)

    按**e**进入

![](https://mmbiz.qpic.cn/mmbiz_png/JhdS4IP8ocGRmgSlJFNBribjpzd8bE1exzvmxy4PKHJglhZ7HDNT6aqCibEEPbglXaALLCoEI7KFHvSEYPiaziboEQ/640?wx_fmt=png&from=appmsg)

    找到加载linux内核的行，在末尾添加**rd.break**，然后按住**Ctrl+x**键，开始启动

![](https://mmbiz.qpic.cn/mmbiz_png/JhdS4IP8ocGRmgSlJFNBribjpzd8bE1exTudgFBcoen2IfWgq7bibRt9AqE6lTOWIbXNP8KgkHSbicdCdIcup45jw/640?wx_fmt=png&from=appmsg)

    简单的查看

![](https://mmbiz.qpic.cn/mmbiz_png/JhdS4IP8ocGRmgSlJFNBribjpzd8bE1exKCYET51kwjVc3ARd19jZd82Oc58DiajX65vPecKr7v9WxPInS1wzhLA/640?wx_fmt=png&from=appmsg)

    发现根目录下边与原来的系统不一样，因为，rd.break是RAM disk里边的操作状态，因此，不能直接获取原本Linux系统操作环境，所以我们还需chroot的支持，更由于SELinux的问题，还需要加上/autorelabel的操作来搞定root密码。

![](https://mmbiz.qpic.cn/mmbiz_png/JhdS4IP8ocGha7h2fxOIV3GoiaTbgKNjgMibe8VzFBEAjhKWeqhvMrNeFGpAZFXwicMyTRpWHSU4ibhMZxh6icIzI9A/640?wx_fmt=png&from=appmsg)

**重要提示：**上图中的输入必须全部正确无误，否则修改失败。

    系统等待的时间较长(2~3)分钟（原理见本篇2.3小节）

![](https://mmbiz.qpic.cn/mmbiz_png/JhdS4IP8ocGha7h2fxOIV3GoiaTbgKNjgL8bdYn9ibV4iaYBHsyN3pcl5RYZ5UyZFwZ4QQibJYG2d9JOlmTUAcIZXg/640?wx_fmt=png&from=appmsg)

    进入登录界面，使用root用户并输入新密码登录成功。

![](https://mmbiz.qpic.cn/mmbiz_png/JhdS4IP8ocGha7h2fxOIV3GoiaTbgKNjgj2GfIbS62yqqCQCPmkUbphhDUwtCjlSXPjtQK7Q7U8VjRV4sHWjiafA/640?wx_fmt=png&from=appmsg)

**二 ****破解root密码的原理解释******

    2.1 修改root密码需要使用内核参数rd.break

    2.2 chroot用来切换根目录，上文中则切换到/sysroot目录下

    2.3 /autorelabel的作用，因为在rd.break的RAM disk环境下，系统没有SELinux的，而刚才已经修改了/etc/shadow文件（这个文件是用来保存密码）

```
[root@centos ~]# grep root /etc/shadowroot:$6$x6qUPUTp$YY7HHotjTVNdIeZUtdZO/D2aEuWRdEBnMR3kMRQtQRettFArathpDvi1ERqWyJO.znZxDpZ7By0RqBHHv.EAC0:19869:0:99999:7:::
```

    此时，这个文件的SELinux安全上下文的特性将会被取消，如果我们没有让系统启动时自动恢复SELinux的安全上下文，那么我们的系统将无法登录，加上/autorelabel就是要让系统重新启动的时重新写入SELinux的类型到每个文件中，因此会花费较长的时间。

    当然，此时的SELinux为Enforceing模式。

    如果以上的解释过于难理解，小编为宝子们想到一种简单且容易的，你家大门的密码从123被你修改为了1234，但你告诉自己，我们家的密码就是1234，没有谁动过的，必须将刚才的操作从记忆中抹除，装着一切都没有发生过。

    说到这里，小编真的有很多想法写出来，比如SELinux是个什么？如果root密码都可以随意修改，那么还有什么安全可言，我家的三瓜两枣被人拿走什么时候自己都不知道，或者糟糕的家伙破解密码进来给系统搞几个漏洞，这不就是糟糕开门糟糕到家了。好了，言归正传，接下来聊聊修改密码后优化启动时间的问题。

**三 优化修改密码后的启动时间**

    当前系统的SELinux模式为Enforcing

```
[root@centos ~]# cat /etc/selinux/config
# This file controls the state of SELinux on the system.# SELINUX= can take one of these three values:#     enforcing - SELinux security policy is enforced.#     permissive - SELinux prints warnings instead of enforcing.#     disabled - No SELinux policy is loaded.SELINUX=enforcing# SELINUXTYPE= can take one of three two values:#     targeted - Targeted processes are protected,#     minimum - Modification of targeted policy. Only selected processes are protected. #     mls - Multi Level Security protection.SELINUXTYPE=targeted [root@centos ~]# getenforce Enforcing
```

    前文中我们已经知道，启动时间长就是SELinux造成的，那么，我们就从这个地方入手。

![](https://mmbiz.qpic.cn/mmbiz_jpg/JhdS4IP8ocGha7h2fxOIV3GoiaTbgKNjgdqky9m8pECJHtDibPribiauHkuOO2dkricTQ0YDCzBtCZlexL5K4xBicia3g/640?wx_fmt=jpeg)

图1

![](https://mmbiz.qpic.cn/mmbiz_png/JhdS4IP8ocGha7h2fxOIV3GoiaTbgKNjgylRVgBiahx1Oa98GgX1ymXVjEhS8VibiburcUbnYuaL5tWp8dQEAgIB4g/640?wx_fmt=png&from=appmsg)

图2

![](https://mmbiz.qpic.cn/mmbiz_png/JhdS4IP8ocGha7h2fxOIV3GoiaTbgKNjgGn5ficQNt4FPXcY5OeozibqboF1D60tVs7w1yVmLaYbObrP8zMrxnQnw/640?wx_fmt=png&from=appmsg)

图3

![](https://mmbiz.qpic.cn/mmbiz_png/JhdS4IP8ocGha7h2fxOIV3GoiaTbgKNjgh50r3SibxfRkiavksdGOfI5H6ibxicSDtHyyhg1GS17iaLWTmCukTshzj5Q/640?wx_fmt=png&from=appmsg)

图4

    此处无解释，相信宝子们可以理解，真的真的要认真理解呀！融会贯通，成为自己的知识。

    重启发现时间确实快了不少，就是正常reboot的节奏，登录进来后，做如下操作。

```
[root@centos ~]# getenforce Permissive[root@centos ~]# restorecon -Rv /etc   #修改/etc下的文件restorecon reset /etc/selinux/config context system_u:object_r:unlabeled_t:s0->system_u:object_r:selinux_config_t:s0restorecon reset /etc/shadow context system_u:object_r:unlabeled_t:s0->system_u:object_r:shadow_t:s0[root@centos ~]# setenforce 1   #将Permissive修改为Enforcing[root@centos ~]# getenforce Enforcing[root@centos ~]# vim /etc/selinux/config #修改配置文件如下保存退出
# This file controls the state of SELinux on the system.# SELINUX= can take one of these three values:#     enforcing - SELinux security policy is enforced.#     permissive - SELinux prints warnings instead of enforcing.#     disabled - No SELinux policy is loaded.SELINUX=enforcing  #将Permissive修改为enforcing# SELINUXTYPE= can take one of three two values:#     targeted - Targeted processes are protected,#     minimum - Modification of targeted policy. Only selected processes are protected. #     mls - Multi Level Security protection.SELINUXTYPE=targeted
```

****四 使用bash破解密码****

    前文中我们在从RAM disk环境切换到根系统目录，本小节讲的是直接提供一个bash环境**【init=/bin/bash】**，不需要root密码而具有root权限，当然，这中环境只能用来修复，具体操作如下：

![](https://mmbiz.qpic.cn/mmbiz_png/JhdS4IP8ocGha7h2fxOIV3GoiaTbgKNjg5cgVnSib8ibVKmbHw1WTtRRPJTEicIAd88ibLhUFEzLfsLBKHKQFiaBVOew/640?wx_fmt=png&from=appmsg)

    我们做简单的查看

![](https://mmbiz.qpic.cn/mmbiz_png/JhdS4IP8ocGha7h2fxOIV3GoiaTbgKNjgiah9xIBHun8uDg7xBK0bHHac88qcnCBCuTeVEWTnIO3eYj78icsmkSEw/640?wx_fmt=png&from=appmsg)

    接着做如下处理，还里依旧是一个字符也不能错，**注意**此时从新挂载的地方发生变化。

![](https://mmbiz.qpic.cn/mmbiz_png/JhdS4IP8ocGha7h2fxOIV3GoiaTbgKNjgDxvIgSYwAt0IKbaDsPN6nEedLVciaicc4sU96PPuic8JQEzO4sZia79JrQ/640?wx_fmt=png&from=appmsg)

    强制关机

![](https://mmbiz.qpic.cn/mmbiz_png/JhdS4IP8ocGha7h2fxOIV3GoiaTbgKNjgfGc8zjA9AJkrcaN7krfthgGGhZjJoguulQeznWiaWyAyj2LZkRYWDiaw/640?wx_fmt=png&from=appmsg)

    开机进入登录界面

![](https://mmbiz.qpic.cn/mmbiz_png/JhdS4IP8ocGha7h2fxOIV3GoiaTbgKNjgOzy4uc7Q1H0Sy7MyChCP9ibt2bnQoYlFB1WoBSMEyowUmoCjndTrZvQ/640?wx_fmt=png&from=appmsg)

    来到登录界面，使用root用户和新的密码登录即可

![](https://mmbiz.qpic.cn/mmbiz_png/JhdS4IP8ocGha7h2fxOIV3GoiaTbgKNjgFBjeWhXo4pKCa1dgvOx3GnmlOOFxNxejGmApazy1teYyiblJI4nT2Gg/640?wx_fmt=png&from=appmsg)

**五 总结**

**感谢宝子们认真读完此篇，真的是泰酷辣！接下来需要宝子们在心中默默回忆一遍，看是否还能想起来，这样在修改密码的时候就能变换出不同的操作，此篇还有优化空间，这里就不展开说啦，留下给宝子们来优化。**

**-****--结束**

******点赞![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_80@2x.png)关注![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_80@2x.png)分享![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_80@2x.png)*****宝子********们************如果觉得还OK，可以动动可爱的小手分享**给身边的好朋友！我们一起进步，每一个点赞关注分享都是小编前进的动力！***

---

【往期回顾】

[Linux命令行配置临时Ipv4---终结篇](http://mp.weixin.qq.com/s?__biz=MzkyNTY5NjQ3MA==&mid=2247483874&idx=1&sn=5e038cc0ba19f3d3dea186dc8794b321&chksm=c1c3e95bf6b4604d24bcd1e674055ee4a0114cc56d86ffd559820863a79cff861e111a6d7a5a&scene=21#wechat_redirect)

[Linux启动失败进入grub界面解决方式](http://mp.weixin.qq.com/s?__biz=MzkyNTY5NjQ3MA==&mid=2247483914&idx=1&sn=38adc58a9fdb8614bece654c3d7aa916&chksm=c1c3eab3f6b463a58ae862ae138192b4444be15b8e2dfa6021ba2c5e57de65916ae90da2b4b9&scene=21#wechat_redirect)

[Linux中逻辑卷-卷组-物理卷之间的关系](http://mp.weixin.qq.com/s?__biz=MzkyNTY5NjQ3MA==&mid=2247483827&idx=1&sn=d843874d797229b1bf996e9489a19705&chksm=c1c3e90af6b4601ce523a17c29a088ac418d3866b2fd4...