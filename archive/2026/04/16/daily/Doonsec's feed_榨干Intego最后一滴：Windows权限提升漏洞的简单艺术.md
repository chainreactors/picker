---
title: 榨干Intego最后一滴：Windows权限提升漏洞的简单艺术
url: https://mp.weixin.qq.com/s/ZmzubIfkycq-K5Hs3KuqNw
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:47:41.619716
---

# 榨干Intego最后一滴：Windows权限提升漏洞的简单艺术

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibeo7HFOSqUMwnQzNYTQzderGibVY8d2TjBLE0vdtTPjF4HGCnNsdK4VOrt3SVLSOMibeQhYwKqSByvU5Eh7hNIjiawUPfcR9sbmos/0?wx_fmt=jpeg)

# 榨干Intego最后一滴：Windows权限提升漏洞的简单艺术

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 安全软件Intego Windows版的“优化模块”存在一处本地权限提升漏洞，利用任意目录删除直接获取系统最高权限。这篇文章不是复杂理论，而是关于一个周日下午的无聊尝试变成了完整攻击链的真实故事。

一个阳光明媚的周日下午，同事Mathieu Farrell跟我分享了他在macOS版Intego上发现的三个漏洞。

说实话，我之前压根没听说过Intego这个安全软件。浏览他们官网找资料时，我才发现他们还做了Windows版本。反正闲着也是闲着，为什么不试试看呢？

几个小时后，我手里已经有了一个本地权限提升漏洞。

这个下午过得不算太坏。

## 漏洞本身很简单

问题出在Intego的“优化模块”上。这个功能让普通用户扫描重复文件，然后一键清理。听起来挺方便。

它的操作流程是：用户运行扫描，选中要删除的重复文件，点击“清理”。然后`IavService.exe`进程会以`SYSTEM`最高权限执行删除操作。

书面流程看着没问题。实际上，这就是我们通往权限提升的专属通道。

漏洞核心有两点：

* 优化模块在删除文件时，从不检查目标到底是普通文件还是目录联接点
* 它运行在SYSTEM权限下

把这两点跟安全圈里已经玩熟了的`Config.msi`删除技巧结合，你就能拿到一张单程车票，直达SYSTEM权限。

本技术分析涉及Intego 3.0.0.1版本。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcV3QdhQKJE72rWpoNT5esleYltB5Z515Xp9H4Hk6kdbIRSh36ribzCU0r6O8TneLkteY4SKCsLzlQdsaklnibdTVn1DUJ4H6MQY/640?wx_fmt=png&from=appmsg)

## 关于Config.msi的小把戏

在深入攻击细节前，先快速过一遍ZDI早前披露的`Config.msi`删除漏洞利用方法。Windows Installer服务在安装和回滚过程中，会把回滚脚本和文件存到`C:\Config.msi`目录里，并且这些文件会以SYSTEM权限处理。

攻击流程像这样：

1. 想办法用某个SYSTEM权限的操作，通过重解析点删除`C:\Config.msi`文件夹
2. 攻击者重建`C:\Config.msi`，并放入自己写的`.rbs`和`.rbf`回滚脚本和文件
3. 触发一个MSI安装并强制其失败，引发回滚操作
4. Windows Installer以SYSTEM权限加载并执行我们的回滚文件，默认会在`C:\Program Files\Common Files\microsoft shared\ink\`路径下释放一个HID.DLL
5. 按`CTRL+ALT+DEL`启动屏幕键盘osk.exe，就能获得一个SYSTEM权限的命令行窗口

这个技巧不算新东西，我们在分析Avira的CVE-2026-27748和CVE-2026-27750时就用过类似的思路。

## 攻击实战：一步一步来

假设我们手里只有一个普通权限账户`limited1`。

第一步，在一个干净的新目录里，创建两个内容完全相同的文件。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibc7fRjkBGO5eOSuvwkp7icgzaryqQvhgRFyiaYD2ia5nllibgY3H8zACPgiagBh4N4v115SFbAe4UXPzViblow54bfTUkm6qcruFegvc/640?wx_fmt=png&from=appmsg)

mkdir c:\foobar
echo 123 > c:\foobar\deleteme1.txt
echo 123 > c:\foobar\deleteme2.txt

然后，打开Intego的优化功能，选择“扫描特定位置”，选中我们刚建的`c:\foobar`目录。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibctygs6nNy72Crj8ZT3iaGotle2WibNgg21yDxmiaktV4z9YquP1RticOsekwxvibtMSxfgWrWFUAENLCKpSuFSZUYnVQLJ077OhD1I/640?wx_fmt=png&from=appmsg)

等着扫描完成，选中我们控制的目录，点击“立即扫描”。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibd8qZRO20ojaWZ8DBZV7CEN15icZYAD3prlZxRRTnN9Ctib8dsA3wxZ9rCib6XJSdHB9dosQB3zratFqpybcMwURACUJkqezfFJVI/640?wx_fmt=png&from=appmsg)

在真正点击“清理”按钮前，有些事情要先准备好。

先运行一下`FolderOrFileDeleteToSystem.exe`这个工具。这是ZDI公开的PoC工具，用来探测系统级别的删除操作。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibdqial5F3EG6zCeASaKb0qpBpsjZ7RJkWQoGWMfmeERLUibU31bGAjmvL9TFFnklwurzM1sib1gQ5Cfx511c7MGGvvc3YGQTHvhGk/640?wx_fmt=png&from=appmsg)

接着，在另一个命令行窗口里执行这几条关键命令。

先把`c:\foobar`目录里的所有文件删光。然后，创建一个指向`C:\config.msi`的符号链接（symlink）。最后，再去点那个“清理”按钮。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibf1hQ2iaiaXCE0LmuibyPXmVUiaZLvqAzZ1uHv4MXGa9LIOJGFbFsaEEro0Y0K7PKXqDtvNzjpnECGXlAISfibEebVBqKmiawrNCAMaM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdAJlCfEjShtChM5ziae0DP25xZWQcCaW0OiaYC1kJ9nicur0N1Ps5LIcFI5GTmTs5lQickcVzXgKmgv2G1kZ4skzM0GXqRicoVZZPM/640?wx_fmt=png&from=appmsg)

点击清理。

现在，可以准备享受成果了。

漏洞利用成功的话，`IavService.exe`会以SYSTEM权限删除掉`C:\config.msi`目录。之后，只需要按`CTRL+ALT+DEL`启动屏幕键盘，系统就会加载我们预先埋下的DLL，从而打开一个SYSTEM权限的命令提示符窗口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdLahplQd8UqyicPQnfVkvIicsQmE9GYX5J8vpib1YmHKkW39oSfyvnhD9x8MyOBPTE5bfvzkJdBvQBvV50FVuCbQyudzurDCF3LQ/640?wx_fmt=png&from=appmsg)

DLL被成功释放。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibelELBOGcM1JbXibtvjQD0wzGv5NFfUKfRCtHBR4jzL0NWXrbeiaxnCLJJ8IfhhbqtnP3uuMsoNYX1ibmQDr8sh4ZbA8ibyQdGBo2A/640?wx_fmt=png&from=appmsg)

Procmon的监控记录证实了SYSTEM权限的删除操作。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcjYodeVxCoic5CMlhLTvGLAEkHxDvlicUfUkLYDbMVBwlTrfarh43DURF3gxcmQXSuzRYgNeDnPrI5LzwmLqcmoMu9lvZJXVCZY/640?wx_fmt=png&from=appmsg)

成功访问SYSTEM命令行。

## 漏洞是怎么发生的？看代码

分析`IavService.exe`的代码，问题就出在删除文件的流程上。

这个过程存在典型的TOCTOU漏洞。

1. 时间点A（检查时）：程序调用`GetFileAttributesW()`获取文件属性。
2. 用户在界面上点击“清理”，这中间有个时间窗口。
3. 时间点B（使用时）：通过`IavFilesUtil_RemoveFile`函数调用`DeleteFileW()`来删除文件。

代码里从来不验证文件属性里是否包含`FILE_ATTRIBUTE_REPARSE_POINT (0x400)`或者`FILE_ATTRIBUTE_DIRECTORY (0x10)`。这意味着目录联接点和符号链接可以畅通无阻地通过检查。

下面是存在漏洞的函数的简化伪代码。

**函数：IavFileDeleteEx\_DeleteFileEx**

这个函数负责初始检查并协调删除。它以SYSTEM权限运行，但完全不验证文件类型。

bool IavFileDeleteEx\_DeleteFileEx(wstring\* filepath\_wstring\_ptr,
                                   void\* stack\_frame\_base,
                                   void\* unused\_param)
{
    // 检查时刻
    file\_attributes = GetFileAttributesW(\*filepath\_wstring\_ptr);

    // 代码没有验证：
    // - if (file\_attributes & FILE\_ATTRIBUTE\_REPARSE\_POINT)  // 0x400
    // - if (file\_attributes & FILE\_ATTRIBUTE\_DIRECTORY)      // 0x10
    // 这让符号链接和目录都溜了过去

    // 它只检查文件是不是只读的
    if ((file\_attributes & FILE\_ATTRIBUTE\_READONLY) != 0)
    {
        if (!SetFileAttributesW(\*filepath\_wstring\_ptr,
                                file\_attributes & ~FILE\_ATTRIBUTE\_READONLY))
        {
            // 移除只读属性失败
            // ...
        }
    }

    // 程序在这里暂停，等待用户确认删除

    IavFileDeleteEx\_KillProcessUsingFile(filepath\_wstring\_ptr);

    temp\_filepath.assign(\*filepath\_wstring\_ptr);

    // 使用时刻
    deletion\_succeeded = IavFilesUtil\_RemoveFile(&temp\_filepath);

    temp\_filepath.~wstring();

    if (deletion\_succeeded)
    {
        goto CLEANUP\_AND\_RETURN\_SUCCESS;
    }
}

**函数：IavFilesUtil\_RemoveFile**

这才是真正出问题的地方。这里能揪出三个关键缺陷：

1. 不验证类型——从不检查重解析点或目录。
2. 危险的备用路径——`std::filesystem::remove()`会处理目录并跟随联接点。
3. 永远返回TRUE——就算删除失败了也返回成功。

bool IavFilesUtil\_RemoveFile(wstring\* filepath\_wstring)
{
    wchar\_t\* filepath\_ptr;

    DWORD file\_attributes = GetFileAttributesW(filepath\_ptr);

    // 仍然不检查“这是目录还是符号链接”。
    // 只检查文件是否存在以及是否只读
    if (file\_attributes != INVALID\_FILE\_ATTRIBUTES &&
        (file\_attributes & FILE\_ATTRIBUTE\_READONLY))
    {
        if (!SetFileAttributesW(filepath\_ptr,
                                file\_attributes & ~FILE\_ATTRIBUTE\_READONLY))
        {
            // 如果移除只读属性失败，记录下来
            // ...
        }
    }

    // 获取文件路径指针
    if (filepath\_wstring->capacity >= 8)
    {
        filepath\_ptr = (wchar\_t\*)filepath\_wstring->data\_ptr;
    }
    else
    {
        filepath\_ptr = (wchar\_t\*)&filepath\_wstring->inline\_buffer;
    }

    if (!DeleteFileW(filepath\_ptr))
    {
        // 如果失败了，记录日志，但还是返回true (?)
        DWORD error\_code = GetLastError();

        LogFormatted(LOG\_LEVEL\_WARNING,
                    L"Failed to ::DeleteFile %s trying with std::filesystem %d",
                    filepath\_ptr,
                    error\_code);

        std::error\_code ec;
        std::filesystem::remove(filepath\_ptr, ec);

        return TRUE;
    }

    // 删除成功，返回true
    return TRUE;
}

## 完整的攻击链条

1. 扫描器发现`c:\foobar\deleteme2.txt`是重复文件，准备标记删除。
2. `GetFileAttributesW()`检查了它的属性（但没查类型）。
3. 用户点击“清理”，但攻击者行动更快：
   * 删光`c:\foobar\`里的所有文件
   * 把`c:\foobar\deleteme2.txt`替换成一个指向`\RPC Control`的NT对象目录联接点
   * 在`\RPC Control\deleteme2.txt`处创建一个指向`C:\Config.msi`的NT符号链接
4. 由于NT符号链接的存在，`DeleteFileW()`调用失败。
5. 程序进入回退路径，调用`std::filesystem::remove()`，而它会跟随NT符号链接。
6. `RemoveDirectoryW()`以SYSTEM权限执行，成功删除`C:\Config.msi`。
7. 函数返回`TRUE`，对调用者来说一切正常。

## 我的看法：老问题，新面孔

这个漏洞本身不复杂，却非常有效。它再一次证明：在赋予软件高权限之前，必须对它的每一个操作都做彻底的边界检查。特别是文件系统操作，Windows平台上的符号链接和联接点从来就是权限提升漏洞的“老朋友”了。

Intego作为一个安全软件，在最基础的“删除”功能上翻车，实在有点讽刺。安全产品本应成为系统的最后一道防线，但糟糕的代码实现反而让它变成了攻击者的跳板。

更让人无奈的是漏洞披露的时间线。我们团队从2025年11月开始尝试联系Intego，过程拖沓，响应缓慢。尽管通过CERT-FR进行了协调，但直到我们按计划发布macOS版的漏洞分析后，才发布了这个Windows版本的分析。这反映了一些安全厂商在漏洞响应上的真实态度。

最后，还是得谢谢Mathieu。要不是他发现的macOS版漏洞让我在周日下午手痒，我也不会去碰这个Windows版本。

## 时间线：一次典型的漏洞披露拉锯战

下面是这次漏洞协调披露过程中的关键时间点，希望给关注这方面的人提供一点透明度。

* 2025-11-06：尝试通过dpo@intego.com联系厂商，询问安全报告联系人。
* 2025-12-08：尝试通过info@intego.com再次联系厂商。
* 2025-12-16：由于未能直接联系到厂商，将漏洞报告提交给CERT-FR，并告知披露日期定为2025年12月30日。
* 2025-12-17：CERT-FR确认收到报告。建议将发布日期推迟至次年2月中旬，以争取更多时间协调。
* 2025-12-18：我们同意将发布日期推迟至2026年2月10日。
* 2026-01-17：Intego客服回复称报告已转交相关部门审核，会通过邮件提供更新。
* 2026-02-10：发布macOS版Intego的第一篇漏洞分析文章。
* 2026-04-07：发布本篇关于Windows版Intego的分析文章。
...