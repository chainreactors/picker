---
title: [windows]自动锁屏程序
url: https://www.freebuf.com/sectool/420727.html
source: FreeBuf网络安全行业门户
date: 2025-01-25
fetch_date: 2025-10-06T20:10:13.936779
---

# [windows]自动锁屏程序

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

[windows]自动锁屏程序

* ![]()
* 关注

* [工具](https://www.freebuf.com/articles/sectool)

[windows]自动锁屏程序

2025-01-24 11:03:49

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

因为单位经常要求电脑锁屏，突然有个想法，以下是几个关键点的分析和推荐的编程语言/框架：

## 功能需求

1. **自动锁定屏幕**：这是通过系统提供的 API 来实现的，可以通过模拟`Win + L`键来锁定屏幕。
2. **设定时间**：设置一个定时器，当鼠标不动一定时间后触发锁定。
3. **播放视频时不锁定**：通过判断当前是否有视频播放，可以用多种方式来检测，例如检查是否有媒体播放器进程在运行，或者通过监听音频和视频相关的 API。

## 适合的语言和框架

#### 1. **Python**

Python 作为脚本语言，写起来简洁，而且具有很多相关的库，可以用来快速开发这一类工具。

* **锁定屏幕**：
  可以使用`ctypes`或者`pyautogui`模拟`Win + L`键。
* **检测鼠标是否移动**：
  使用`pynput`库监听鼠标移动事件并进行计时。
* **判断是否播放视频**：
  可以通过检查视频播放器进程（例如`vlc.exe`、`wmplayer.exe`等）是否在运行，使用`psutil`来检查。
* **设置定时器和后台运行**：
  可以使用 Python 的`threading`模块来处理定时任务。

**代码示例：**

```
import ctypes
import time
import threading
from pynput.mouse import Listener
import psutil

# 锁定屏幕的函数
def lock_screen():
    ctypes.windll.user32.LockWorkStation()

# 检测是否播放视频的函数
def is_video_playing():
    video_players = ['vlc.exe', 'wmplayer.exe', 'mediaplayer.exe']
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() in video_players:
            return True
    return False

# 自动锁定屏幕的函数
class AutoLock:
    def __init__(self, timeout=300):
        self.timeout = timeout  # 默认 5 分钟
        self.last_move_time = time.time()  # 记录上次鼠标活动时间
        self.listener = Listener(on_move=self.on_move)
        self.listener.start()

    def on_move(self, x, y):
        self.last_move_time = time.time()  # 每次鼠标移动时更新时间

    def start_timer(self):
        while True:
            time.sleep(1)
            if time.time() - self.last_move_time > self.timeout and not is_video_playing():
                print("鼠标无活动，自动锁定屏幕")
                lock_screen()
                self.last_move_time = time.time()  # 锁定后重置时间

# 创建一个后台线程来定时检查
auto_lock = AutoLock(timeout=300)  # 设置为5分钟
lock_thread = threading.Thread(target=auto_lock.start_timer)
lock_thread.daemon = True
lock_thread.start()

# 主程序保持运行
while True:
    time.sleep(10)
```

**优点：**

* **简洁**：Python 语法简洁，开发速度快。
* **功能丰富**：可以通过第三方库（如`pynput`、`psutil`）轻松实现这些功能。
* **跨平台**：Python 脚本可以在多平台上运行，尽管本例是面向 Windows 的，但在 Linux 或 macOS 上可以通过适配相应的 API 来实现类似功能。

#### 2. **C# (Windows 专用)**

如果只在 Windows 平台上运行，C# 是一个非常合适的选择。C# 与 Windows API 紧密集成，可以轻松地访问系统功能（如屏幕锁定）和进程管理。

* **锁定屏幕**：
  可以直接调用 Windows API 来锁定屏幕。
* **检测鼠标是否移动**：
  可以利用`System.Windows.Forms`或`System.Management`来监听鼠标事件并计时。
* **判断是否播放视频**：
  通过检查进程列表来判断是否有视频播放器正在运行。

**代码示例：**

```
using System;
using System.Linq;
using System.Diagnostics;
using System.Threading;
using System.Runtime.InteropServices;
using System.Windows.Forms;

class AutoLockScreen
{
    // 调用Windows API来锁定屏幕
    [DllImport("user32.dll")]
    public static extern bool LockWorkStation();

    static void Main(string[] args)
    {
        Timer timer = new Timer(Callback, null, 0, 1000);
        Application.Run();  // 保持应用程序运行
    }

    static void Callback(object state)
    {
        if (IsMouseIdle() && !IsVideoPlaying())
        {
            LockWorkStation();
        }
    }

    // 判断鼠标是否静止
    static bool IsMouseIdle()
    {
        // 实际实现可以通过捕捉鼠标移动事件来判断
        // 这里我们简单返回 true 来模拟
        return true;
    }

    // 判断是否播放视频
    static bool IsVideoPlaying()
    {
        string[] videoPlayers = { "vlc", "wmplayer", "mediaplayer" };
        var processes = Process.GetProcesses();
        foreach (var process in processes)
        {
            if (videoPlayers.Any(player => process.ProcessName.ToLower().Contains(player)))
            {
                return true;
            }
        }
        return false;
    }
}
```

**优点：**

* **性能更高**：C# 是编译型语言，适合对性能有较高要求的场景。
* **强大的 Windows API 集成**：可以直接使用 Windows 提供的 API 完成任务，像`LockWorkStation`用于锁定屏幕非常方便。
* **UI 支持**：如果你需要图形界面或者系统托盘功能，C# 提供了强大的支持。

### 3. **AutoHotkey (AHK)**

如果你只需要快速实现简单的脚本，AutoHotkey 是一个非常适合自动化和系统控制的语言，特别是在 Windows 系统中。

* **锁定屏幕**：
  使用`LockWorkStation`系统命令来锁定屏幕。
* **检测鼠标是否移动**：
  可以使用`MouseMove`函数获取鼠标位置并进行检测。
* **判断是否播放视频**：
  可以通过`Process`命令查看系统中正在运行的进程。

**代码示例：**

```
#Persistent
SetTimer, CheckInactivity, 1000

CheckInactivity:
    ; 检查鼠标是否有活动
    MouseGetPos, MouseX, MouseY
    if (A_TimeIdle > 300000 && !IsVideoPlaying())  ; 如果 5 分钟没有活动并且没有视频播放
    {
        DllCall("user32.dll", "int", 0, "int", 0)  ; 锁定屏幕
    }
    return

IsVideoPlaying:
    Process, Exist, vlc.exe  ; 检查 VLC 是否在运行
    if (ErrorLevel) {
        return true
    }
    Process, Exist, wmplayer.exe  ; 检查 Windows Media Player 是否在运行
    return ErrorLevel > 0
```

**优点：**

* **快速实现**：AutoHotkey 脚本非常简单，适合快速实现自动化任务。
* **直接与操作系统交互**：对 Windows 系统的支持非常好，直接调用 Windows 函数。

### 总结

* **Python**：简洁且功能强大，适合快速开发和跨平台使用。使用`pynput`和`psutil`等库可以方便地完成所有需求。
* **C#**：适合 Windows 平台，能直接调用 Windows API，适合需要高性能或与 Windows 紧密集成的任务。
* **AutoHotkey**：适合快速编写简单的自动化脚本，尤其适合系统任务和简单的 UI 操作。

如果你想要一个跨平台的解决方案，并且对性能要求不是特别高，**Python**是非常好的选择。如果你只在 Windows 上运行且需要更强的性能和系统集成，**C#**是更好的选择。

# windows # 脚本

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

功能需求

适合的语言和框架

* 3. AutoHotkey (AHK)
* 总结

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)