---
title: .NET一款反序列化执行命令的白名单工具
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495523&idx=1&sn=f48df5389fa50fff412ce713f2f5d2ee&chksm=fa59418ecd2ec898251f254544340a9d7e031102ce347712954920ce98afc03460ae857eb1eb&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-09-26
fetch_date: 2025-10-06T18:29:47.977681
---

# .NET一款反序列化执行命令的白名单工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9P5HP8X3v3OwHq9iafUiaTzicFCI0N2EXiaEEzAjaSHOzxxPkHomrqrcRO6JlTOQU1O4ODgapk3cPIEA/0?wx_fmt=jpeg)

# .NET一款反序列化执行命令的白名单工具

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面

02

基本介绍

Sharp4AddUtil.exe 是一款用于管理和配置 Microsoft Office 加载项的 Windows 系统实用工具，具备了微软签名，属于系统白名单文件。一般用于帮助用户和开发者进行加载项的安装、卸载和修复，提供了一种简便的方式来处理 Office 加载项相关的问题。尽管 Sharp4AddUtil.exe 提供了多种便利功能，但它也存在严重的反序列化漏洞。这一漏洞允许攻击者利用该工具加载恶意的载荷，可能导致系统受到威胁。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9P5HP8X3v3OwHq9iafUiaTzicRdYR921QwlQ1EBGxXjrGapick5P6VRQGfWX5Au7S6De6vibde5ticwsFw/640?wx_fmt=jpeg&from=appmsg)

03

使用方法

首先，通过TextFormattingRunProperties链路，生成一个包含反序列化Poc的攻击载荷，载荷内容如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibfAdnicNVezlJNraV6JJUwAumAf9rZoiaA1ibZCPichkn17qblMYiazHMW2jTzpZz9eA3SnoU2Cd2picPQ/640?wx_fmt=png&from=appmsg)

接着，运行如下命令即可完成反序列化漏洞，弹出winver.exe进程，具体命令如下所示。

```
```
Sharp4AddUtil.exe -AddinRoot:.
```
```

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibfAdnicNVezlJNraV6JJUwAEoiaic8ZpUysP4owkLL6dUqTBexfosvnG0N79EVtbaHfvwVyVU6deGmA/640?wx_fmt=png&from=appmsg)

04

原理解析

在上文中，我们介绍了 Sharp4AddUtil.exe 的基本功能和反序列化漏洞。接下来，我们将进一步分析工具中的其他重要方法，以理解其在加载项管理中的具体实现。UpdateAddInsIfExist 方法检查加载项路径是否存在，且 AddIns.store 文件是否不存在或已过期。如果满足条件，调用 AddInStore.BuildAddInCache 方法构建或更新加载项缓存。

```
```
private static void UpdateAddInsIfExist(string addInsPath, Collection<string> warningsCollection)
{
    string path = Path.Combine(addInsPath, "AddIns.store");
    FileIOPermission fileIOPermission = new FileIOPermission(FileIOPermissionAccess.Read | FileIOPermissionAccess.PathDiscovery, addInsPath);
    fileIOPermission.Assert();

    if (Directory.Exists(addInsPath) && (!File.Exists(path) || AddInStore.AddInStoreIsOutOfDate(addInsPath)))
    {
        AddInStore.BuildAddInCache(addInsPath, warningsCollection);
    }
}
```
```

随后，AddInStoreIsOutOfDate 方法通过 GetAddInDeploymentState 方法获取当前的加载项部署状态，并检查其文件计数是否与期望值一致，确定加载项是否过期。

```
```
private static bool AddInStoreIsOutOfDate(string addInPath)
{
    if (addInPath == null)
    {
        throw new ArgumentNullException("addInPath");
    }

    string path = Path.Combine(addInPath, "AddIns.store");
    DateTime lastWriteTime = File.GetLastWriteTime(path);
    int num = 0;

    if (Directory.Exists(addInPath))
    {
        foreach (string path2 in Directory.GetDirectories(addInPath))
        {
            if (AddInStore.DirectoryNeedsUpdating(path2, lastWriteTime, ref num))
            {
                return true;
            }
        }
    }

    AddInDeploymentState addInDeploymentState = AddInStore.GetAddInDeploymentState(addInPath);
    return addInDeploymentState == null || num != addInDeploymentState.FileCount;
}
```
```

由于使用了 BinaryFormatter 进行反序列化，该方法容易受到反序列化攻击。攻击者可以构造恶意的加载项文件，当 ReadCache 方法尝试反序列化这些文件时，将会导致执行任意代码。

```
```
[SecuritySafeCritical]
private static T ReadCache<T>(string storeFileName, bool mustExist)
{
    new SecurityPermission(SecurityPermissionFlag.SerializationFormatter).Demand();
    new FileIOPermission(FileIOPermissionAccess.Read | FileIOPermissionAccess.PathDiscovery, storeFileName).Assert();
    BinaryFormatter binaryFormatter = new BinaryFormatter();
    T result = default(T);
    if (File.Exists(storeFileName))
    {
       using (Stream stream = File.OpenRead(storeFileName))
        {
             if (stream.Length < 12L)
                    {
                        throw new InvalidOperationException(string.Format(CultureInfo.CurrentCulture, Res.DeployedAddInsFileCorrupted, new object[] { storeFileName }));
                    }
                    BinaryReader binaryReader = new BinaryReader(stream);
                    int num = binaryReader.ReadInt32();
                    long num2 = binaryReader.ReadInt64();
                    try
                    {
                        result = (T)((object)binaryFormatter.Deserialize(stream));
                    }
                    catch (Exception innerException)
                    {
                        throw new InvalidOperationException(string.Format(CultureInfo.CurrentCulture, Res.CantDeserializeData, new object[] { storeFileName }), innerException);
                    }

        }
    }
}
```
```

综上，Sharp4AddUtil.exe 是一款功能丰富的 Office 加载项管理工具，能够高效地管理加载项的安装与更新。尽管提供了许多便利功能，但反序列化漏洞可以帮助红队利用白名单方式运行恶意代码。工具已经打包在星球，感兴趣的朋友可以加入自取。

05

推荐阅读

从漏洞分析到安全攻防，我们涵盖了.NET安全各个关键方面，为您呈现最新、最全面的.NET安全知识，下面是公众号发布的精华文章集合，推荐大家阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247493952&idx=4&sn=db68011fb075c1d02268811163646b53&chksm=fa5947adcd2ecebbb1ca6659f289a5e344e37d1136fe0bd9272b5578e4c71bb19bb250e934d3&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9tl26Kh2sQYI9guTCflSwQP8Gs9z7iamicOvlQv4UYzjwd378D03h7yEYFtZ6xA74qicInoed7qpBWg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495167&idx=1&sn=9280c55fdc7c9146e549be470cf9f120&chksm=fa594312cd2eca04bfe8fd1fd3890b389d9c700b9b69d897f919addac399bab4f4d2e55f6b4f&scene=21#wechat_redirect)

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

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt5...