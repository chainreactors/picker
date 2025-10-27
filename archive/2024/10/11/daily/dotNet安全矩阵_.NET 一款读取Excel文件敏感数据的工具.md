---
title: .NET 一款读取Excel文件敏感数据的工具
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495901&idx=3&sn=d976df27d45430d151019c1c9aa4c23e&chksm=fa595e30cd2ed72660dcc1139704dd772e941a719e2649cdc840117ebed55ef395f462558c7e&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-10-11
fetch_date: 2025-10-06T18:53:04.198239
---

# .NET 一款读取Excel文件敏感数据的工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibibIGvSxdwIh0YNN2QT8socCCJ861hkjYRhnp8I2RiaTmOtNicwJG0zfoxRAl2D2kouTZHeb8q8DecQ/0?wx_fmt=jpeg)

# .NET 一款读取Excel文件敏感数据的工具

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面

02

基本介绍

Sharp4ReadExcel.exe 是一款专为红队活动设计的工具，能够自动化地读取 Microsoft Excel 表格内容，该工具支持 XLS 和 XLSX 两种扩展名，可用于在内网环境中批量收集信息，快速查找敏感数据。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibibIGvSxdwIh0YNN2QT8socjCfMRpXW9WFy0BqMQmEcvpBRckA7HQx63QYfLPsOK3eClbacbXIMKw/640?wx_fmt=jpeg&from=appmsg)

03

使用方法

Sharp4ReadExcel.exe 主要用于打开和读取指定的 Excel 表格内容，支持指定路径及密码。

## 3.1 读取工作表名称

用户可以获取 Excel 文件中所有工作表的名称，便于快速定位所需数据。要读取 Excel 文件中的工作表名称，可以使用以下命令。

```
Sharp4ReadExcel.exe sheets 123.xlsx
```

例如，获取奖品发放情况\_抽奖助手.xlsx表格的工作区名，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibibIGvSxdwIh0YNN2QT8soc2AIglp25ODnIAZ8FlOuJC8iapyZBGHCMiaBibU35RoCoyib2QYZrCVGFtQ/640?wx_fmt=png&from=appmsg)

## 3.2 读取工作表内容

要读取特定工作区的内容，可以使用如下命令，其中，sheetName 为目标工作表名称，123.xlsx 为目标 Excel 文件，password 为工作表的密码（如果有）

```
Sharp4ReadExcel.exe read sheetName password 123.xlsx
```

例如，读取奖品发放情况\_抽奖助手.xlsx表格的工作区内容，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibibIGvSxdwIh0YNN2QT8socWCDWEqVPYu1SBwiaRTEPA6MD7BlG79R6I9MPasI8PN0aQicIYd2B8MFg/640?wx_fmt=png&from=appmsg)

04

原理解析

我们来详细分析 Sharp4ReadExcel.exe 工具的代码，分为两个主要部分：获取工作表名称和读取工作表内容。

首先，通过Excel.Application xlApp = new Excel.Application(); 创建 Excel 应用实例，并使用 foreach 循环遍历所有工作表，并将名称输出到控制台

```
```
if (args[0].ToLower() == "sheets")
{
    if (File.Exists(Path.GetFullPath(args[1])))
    {
        if (Path.GetExtension(args[1]).ToLower() == ".xls" || Path.GetExtension(args[1]).ToLower() == ".xlsx")
        {
            Excel.Application xlApp = new Excel.Application();
            Excel.Workbook xlWorkbook = xlApp.Workbooks.Open(Path.GetFullPath(args[1]), Type.Missing, true);
            String[] sheets = new string[xlWorkbook.Worksheets.Count];
            int i = 0;
            foreach (Excel.Worksheet wSheet in xlWorkbook.Worksheets)
            {
                Console.WriteLine("Sheet Name Found: " + (sheets[i] = wSheet.Name));
                i++;
            }

            xlWorkbook.Close(false, null, null);
            xlApp.Quit();
            Marshal.ReleaseComObject(xlWorkbook);
            Marshal.ReleaseComObject(xlApp);
            System.Environment.Exit(0);
        }
        else
        {
            Console.WriteLine("Error...Did not provide an Excel Worksheet");
            System.Environment.Exit(0);
        }
    }
}
```
```

随后，使用 xlApp.Workbooks.Open 方法打开文件，并提供密码进行保护解除，再通过PrintExcelGrid(xlRange, rowCount, colCount); 调用自定义函数输出工作表数据。

```
```
string pass = args[2].ToString();
Excel.Application xlApp = new Excel.Application();
Excel.Workbook xlWorkbook = xlApp.Workbooks.Open(Path.GetFullPath(args[3]), Type.Missing, true, Type.Missing, pass, pass);
xlWorkbook.Password = pass;
xlWorkbook.Unprotect(pass);
Excel._Worksheet xlWorksheet = (Excel._Worksheet)xlWorkbook.Sheets[args[1]];
xlWorksheet.Unprotect(pass);
Excel.Range xlRange = xlWorksheet.UsedRange;
int rowCount = xlRange.Rows.Count;
int colCount = xlRange.Columns.Count;

PrintExcelGrid(xlRange, rowCount, colCount);

xlWorkbook.Close(false, null, null);
xlApp.Quit();
Marshal.ReleaseComObject(xlWorksheet);
Marshal.ReleaseComObject(xlWorkbook);
Marshal.ReleaseComObject(xlApp);
System.Environment.Exit(0);
```
```

综上，Sharp4ReadExcel.exe 是一款功能强大的 Excel 数据读取工具，适合红队成员在执行渗透测试时使用。通过简单的命令行操作，用户可以快速获取 Excel 文件中的重要信息，提升信息收集的效率。工具已经打包在星球，感兴趣的朋友可以加入自取。

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

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58Ueoynsb0my3uzMAb7VwM5bgtnb4nbl4c9xdEjGraUXic6pO0p38xmWiaRQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOc2SogKzZ16SD7dpzF3v81kia4ZAx5QU5ibnNibEo8kZZSJgrficz4Ckxwg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

星球文化始终认为授人以鱼不如授人以渔！加入星球后可以跟星主和嘉宾们一对一提问交流，20+个专题栏目涵盖了点、线、面、体等知识面，助力师傅们快速成长！其中主题包括.NET Tricks、漏洞分析、内存马、代码审计、预编译、反序列化、webshell免杀、命令执行、C#工具库等等。![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YiccvW0LwqSx3grm4bgM0fz01qCxrYGBR94wibZ7sk1zIO9DzCgviab9vmUic8qmvynXhSM8LxFhGG97w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

    我们倾力打造专刊、视频等配套学习资源，循序渐进的方式引导加深安全攻防技术提高以及岗位内推等等服务。![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9XgicSeCfnDO0KyvDNdCZhG3pTSWHRekG0Wrp0FXyHO1mz9ia5uiaICjCmg5jIzx4ERLU8MjXWVSkCw/640?wx_fmt=other&fr...