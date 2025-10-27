---
title: Windows遭遇「删除文件失败」
url: https://blog.nsfocus.net/windows-5/
source: 绿盟科技技术博客
date: 2025-08-12
fetch_date: 2025-10-07T00:48:25.735147
---

# Windows遭遇「删除文件失败」

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# Windows遭遇「删除文件失败」

### Windows遭遇「删除文件失败」

[2025-08-11](https://blog.nsfocus.net/windows-5/ "Windows遭遇「删除文件失败」")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 382

标题: Windows遭遇「删除文件失败」

在某技术论坛看到有人分享小工具，用于“Windows文件解除占用强制删除”。在其
评论中提到火绒、360、IObit Unlocker等工具，均可用于删除那些正常操作无法删
除的文件。还有一些人碰上这种情况，用重启大法，重启Windows后再删。

Windows系统出现这类现象的底层技术原因，简单点说，相关句柄在内核态仍处于占
用状态。再多不展开，科普的目标是，碰上了，咋办？

前面那些工具当然可以一试，我一个也没试过。不讨论它们好不好的问题，这种事只
是个人选择。我只用微软Sysinternals中的Process Explorer解决此问题。这是微软
自家工具，官方下载点在

————————————————————————–
https://www.sysinternals.com/
https://learn.microsoft.com/en-us/sysinternals/
https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer
https://download.sysinternals.com/files/ProcessExplorer.zip
————————————————————————–

解压到任意目录即可使用，不必安装，原生便携版。右键选中procexp.exe，以管理
员身份运行。

————————————————————————–
Find
Find Handle or DLL (Ctrl+Shift+F)
————————————————————————–

在弹出的界面中输入删除失败的目标文件、目录；不需要绝对路径，可以是中间任一
部分，它会子串匹配。若有命中，会显示目标文件、目录以及占用它们的活动进程。
点击相应进程，就会在Process Explorer主界面中选中相应进程。

假设已在Process Explorer主界面选中相应进程，接下来查看”Lower Pane”。这步细
说一下，可能你那里看到的界面缺省没有”Lower Pane”。

————————————————————————–
View
Show Lower Pane (Ctrl+L)
Lower Pane View
Handles (Ctrl+H)
————————————————————————–

上面的操作看花眼了无所谓，不看也罢，直接按”Ctrl+H”查看Handles界面即可。对
Name列排序，查看当前选中进程所占用的文件路径；你删不掉的文件、目录应该就在
其中。

理论上，找到占用句柄的进程后，通过GUI操作正常退出该进程，被占用句柄将得到
释放，再删目标文件、目录，应该可以了。仍然删除失败时，再次”Find Handle”，
可能还有其他进程占用句柄。重复前述过程，直至”Find Handle”完全找不到目标文
件、目录。

前面是理想状态。不理想状态也挺多的，比如占用句柄的是explorer.exe，关闭资源
管理器不见得结束该进程，此处亦不展开。可用Process Explorer杀掉explorer.exe

————————————————————————–
右键选中目标进程
Kill Process (Del)
————————————————————————–

切勿选成”Kill Process\_Tree (Shift+Del)”，否则可能一瞬间杀掉许多前台进程，
大概率不是你想要的效果。

即使只杀explorer.exe，对一般用户也会带来无法继续的局面，没有状态栏了，没有
左下角的开始菜单了，等等。Process Explorer有机会让你重启explorer.exe

————————————————————————–
File
Run (Ctrl+R)
输入explorer.exe并回车
————————————————————————–

或者尝试”Ctrl+Shift+ESC”呼叫任务管理器

————————————————————————–
文件
运行新任务
输入explorer.exe并回车
————————————————————————–

重启explorer.exe后，至少表面上一切恢复正常，已能删除之前删除失败的文件、目
录。

关于explorer.exe更多信息，有兴趣者可参看

《Win10开管理员级资源管理器》
https://scz.617.cn/windows/202401111737.txt

占用句柄的既不是普通进程，也不是explorer.exe，将更复杂，可能是系统关键进程。
杀这种进程，会带来一系列复杂问题。此时，普通用户不要挣扎，重启Windows再删
吧。

高级用户可能不想杀掉占用句柄的进程，Handles界面中右键选中目标文件、目录，
有个”Close Handle”，理论上可以单独关闭(释放)所选Handle，但不建议这么干，因
为进程的代码逻辑几乎不会考虑外部关闭句柄这种情形带来的异常。就算当时表面上
没出事，很可能在后面某个阶段出事。高级用户在重启前或可一试，风险自负。

用前述办法，绝大多数因句柄占用引发的删除失败都能解决。但是，部分涉及驱动层
的句柄占用，前法可能不适用。比如VMware Guest中的PC版微信访问了Host中的图片，
一段时间内在Host中无法正常解除图片文件的句柄占用，但从Guest中可解除占用。
驱动层句柄占用，不多展开。无论如何，普通用户有个重启大法兜底。

那些用于此途的专项小工具，有其存在意义，毕竟非专业人士数量更多，对TA们来说，
傻瓜式强删更如所愿。

本文只考虑正常系统中文件删除失败时的补救措施，不考虑病毒、木马、rootkit等
情形。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/%E7%BE%8E%E5%9B%BD%E5%8F%91%E5%B8%83%E3%80%8A%E6%8C%81%E7%BB%AD%E5%BC%BA%E5%8C%96%E5%9B%BD%E5%AE%B6%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E5%B9%B6%E4%BF%AE%E8%AE%A2%E7%AC%AC13694%E5%8F%B7%E5%92%8C/)

[Next](https://blog.nsfocus.net/%E8%8E%B7%E5%8F%96windbgx%E7%A6%BB%E7%BA%BF%E5%AE%89%E8%A3%85%E5%8C%85/)

### Meet The Author

NSFOCUS

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)