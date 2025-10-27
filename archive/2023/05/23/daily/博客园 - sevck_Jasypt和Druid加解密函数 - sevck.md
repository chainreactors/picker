---
title: Jasypt和Druid加解密函数 - sevck
url: https://www.cnblogs.com/sevck/p/17421208.html
source: 博客园 - sevck
date: 2023-05-23
fetch_date: 2025-10-04T11:36:41.508907
---

# Jasypt和Druid加解密函数 - sevck

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

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/sevck/)

# [Sevck's Blog](https://www.cnblogs.com/sevck)

## 关注互联网安全，软件开发，这里记录着我的渗透心得、开发文摘、随笔心情(Linux,Windows,Python,Java.Lua,JS,C++在学习)。JAVA安全网:https://www.javasec.cn

* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* 订阅
* [管理](https://i.cnblogs.com/)

# [Jasypt和Druid加解密函数](https://www.cnblogs.com/sevck/p/17421208.html "发布于 2023-05-22 17:18")

spring boot jasypt 加解密

jasypt 加密ENC() 需要启动参数秘钥

Druid 加密，需要public-key

```
package com.example.demo;

import com.alibaba.druid.filter.config.ConfigTools;
import org.jasypt.encryption.pbe.PooledPBEStringEncryptor;
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.EnvironmentStringPBEConfig;
import org.jasypt.encryption.pbe.config.SimpleStringPBEConfig;

class JasyptUtil {
    private static final String PBEWITHMD5ANDDES = "PBEWithMD5AndDES";
    private static final String PBEWITHHMACSHA512ANDAES_256 = "PBEWITHHMACSHA512ANDAES_256";

    public String DruidEncyrpt(String publickey, String text) throws Exception {
        return ConfigTools.decrypt(publickey, text);
    }

    /**
     * @param text  待加密原文
     * @param crack 盐值（密钥）
     * @return 加密后的字符串
     * @Description: Jasypt加密（PBEWithMD5AndDES）
     */
    public static String encryptWithMD5(String text, String crack) {
        //1.创建加解密工具实例
        StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
        //2.加解密配置
        EnvironmentStringPBEConfig config = new EnvironmentStringPBEConfig();
        config.setAlgorithm(PBEWITHMD5ANDDES);
        config.setPassword(crack);
        encryptor.setConfig(config);
        //3.加密
        return encryptor.encrypt(text);
    }

    /**
     * @param text  待解密原文
     * @param crack 盐值（密钥）
     * @return 解密后的字符串
     * @Description: Jasypt解密（PBEWithMD5AndDES）
     */
    public static String decryptWithMD5(String text, String crack) {
        //1.创建加解密工具实例
        StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
        //2.加解密配置
        EnvironmentStringPBEConfig config = new EnvironmentStringPBEConfig();
        config.setAlgorithm(PBEWITHMD5ANDDES);
        config.setPassword(crack);
        encryptor.setConfig(config);
        //解密
        return encryptor.decrypt(text);
    }

    /**
     * @param text  待加密的原文
     * @param crack 盐值（密钥）
     * @return 加密后的字符串
     * @Description: jasypt 加密（PBEWITHHMACSHA512ANDAES_256）
     */
    public static String encryptWithSHA512(String text, String crack) {
        //1.创建加解密工具实例
        PooledPBEStringEncryptor encryptor = new PooledPBEStringEncryptor();
        //2.加解密配置
        SimpleStringPBEConfig config = new SimpleStringPBEConfig();
        config.setPassword(crack);
        config.setAlgorithm(PBEWITHHMACSHA512ANDAES_256);
        // 为减少配置文件的书写，以下都是 Jasypt 3.x 版本，配置文件默认配置
        config.setKeyObtentionIterations("1000");
        config.setPoolSize("1");
        config.setProviderName("SunJCE");
        config.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        config.setIvGeneratorClassName("org.jasypt.iv.RandomIvGenerator");
        config.setStringOutputType("base64");
        encryptor.setConfig(config);
        //3.加密
        return encryptor.encrypt(text);
    }

    /**
     * @param text  待解密原文
     * @param crack 盐值（密钥）
     * @return 解密后的字符串
     * @Description: jasypt 解密（PBEWITHHMACSHA512ANDAES_256）
     */
    public static String decryptWithSHA512(String text, String crack) {
        //1.创建加解密工具实例
        PooledPBEStringEncryptor encryptor = new PooledPBEStringEncryptor();
        //2.加解密配置
        SimpleStringPBEConfig config = new SimpleStringPBEConfig();
        config.setPassword(crack);
        config.setAlgorithm(PBEWITHHMACSHA512ANDAES_256);
        // 为减少配置文件的书写，以下都是 Jasypt 3.x 版本，配置文件默认配置
        config.setKeyObtentionIterations("1000");
        config.setPoolSize("1");
        config.setProviderName("SunJCE");
        config.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        config.setIvGeneratorClassName("org.jasypt.iv.RandomIvGenerator");
        config.setStringOutputType("base64");
        encryptor.setConfig(config);
        //3.解密
        return encryptor.decrypt(text);
    }

    public static void main(String[] args) {
        String text = "xxxxxxxxxxxxlvXSw=";
        String key = "jasypt key";  // -Djasypt.encryptor.password=
        String ret = JasyptUtil.decryptWithSHA512(text,key);
        System.out.println(ret);

    }

}
```

【版权所有@Sevck 博客地址http://www.cnblogs.com/sevck】 可以转载，注明出处.

posted @
2023-05-22 17:18
[sevck](https://www.cnblogs.com/sevck)
阅读(576)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)