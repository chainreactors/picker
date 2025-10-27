---
title: Java Zip Slip漏洞案例分析及实战挖掘
url: https://buaq.net/go-147076.html
source: unSafe.sh - 不安全
date: 2023-01-30
fetch_date: 2025-10-04T05:09:42.144649
---

# Java Zip Slip漏洞案例分析及实战挖掘

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/f1df6f1998c694058af7f19f30c570cd.jpg)

Java Zip Slip漏洞案例分析及实战挖掘

Zip Slip的漏洞成因非常简单，这个漏洞绑定的业务功能点：上传压缩包文件，后端解压压缩包保存其中的文件到服务器本地。漏洞成因：待上传的压缩包中可以构造条目名，
*2023-1-29 20:32:0
Author: [xz.aliyun.com(查看原文)](/jump-147076.htm)
阅读量:76
收藏*

---

Zip Slip的漏洞成因非常简单，这个漏洞绑定的业务功能点：上传压缩包文件，后端解压压缩包保存其中的文件到服务器本地。

漏洞成因：待上传的压缩包中可以构造条目名，后端保存文件的时候，常常将条目名提取出来并和保存目录拼接作为最后的保存文件路径，但是压缩包是可控的，从而其中保存的原始条目名也是可控的，因此可以在文件名处利用`../`跳转到任意目录，从而向任意目录写入新文件或者覆盖旧文件。具体案例可见下文。

在Zip Slip公布者[文章](https://security.snyk.io/research/zip-slip-vulnerability "文章")中，提到，Java中的Zip Slip漏洞尤其普遍：

> The vulnerability has been found in multiple ecosystems, including JavaScript, Ruby, .NET and Go, but is especially prevalent in Java, where there is no central library offering high level processing of archive (e.g. zip) files. The lack of such a library led to vulnerable code snippets being hand crafted and shared among developer communities such as StackOverflow.

本文从原生的Java.util.zip->zt-zip->spring integration zip进行Zip Slip漏洞分析，并在最后附上此漏洞的代审案例。

```
import zipfile

if __name__ == "__main__":
    try:
        zipFile = zipfile.ZipFile("poc.zip", "a", zipfile.ZIP_DEFLATED)  ##生成的zip文件
        info = zipfile.ZipInfo("poc.zip")
        zipFile.write("D:/tgao/pass/1", "../password", zipfile.ZIP_DEFLATED)  ##压缩的文件和在zip中显示的文件名
        zipFile.close()
    except IOError as e:
        raise e
```

上述生成的恶意zip，在Zip Slip中，会取出`../password`，并与保存目录拼接，其中获取`../password`的java方法类似与`zipEntry.getName()`。

漏洞代码：实际场景下的的zip包是可控的，如通过文件上传等功能

```
package zip;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Enumeration;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;

public class Zip1 {
    public static void main(String[] args) throws IOException {
        //解压zip的包
        String fileAddress = "D:/pythonProject/exp/ctf/poc.zip";
        //zip文件解压路径
        String unZipAddress = "D:/tgao/pass/";
        //去目录下寻找文件
        File file = new File(fileAddress);
        ZipFile zipFile = null;
        try {
            zipFile = new ZipFile(file);//设置编码格式
        } catch (IOException exception) {
            exception.printStackTrace();
            System.out.println("解压文件不存在!");
        }
        Enumeration e = zipFile.entries();
        while(e.hasMoreElements()) {
            ZipEntry zipEntry = (ZipEntry)e.nextElement();
            File f = new File(unZipAddress + zipEntry.getName());
            f.getParentFile().mkdirs();
            f.createNewFile();
            InputStream is = zipFile.getInputStream(zipEntry);
            FileOutputStream fos = new FileOutputStream(f);
            int length = 0;
            byte[] b = new byte[1024];
            while((length=is.read(b, 0, 1024))!=-1) {
                fos.write(b, 0, length);
            }
            is.close();
            fos.close();
        }
        if (zipFile != null) {
            zipFile.close();
        }
    }
}
```

漏洞成因： `File f = new File(unZipAddress + zipEntry.getName());`中`zipEntry.getName()`的值是可控的，从而造成路径穿越，最终写入任意文件。

引入依赖：

```
<dependency>
  <groupId>org.zeroturnaround</groupId>
  <artifactId>zt-zip</artifactId>
  <version>1.12</version>xml
</dependency>
```

zt-zip组件中的解压功能，是在原生的java.util.zip基础上进行的封装。

```
package zip;

import org.zeroturnaround.zip.ZipUtil;

import java.io.File;

public class Zip2 {
    public static void main(String[] args) {
        File zip = new File("D:/pythonProject/exp/ctf/poc.zip");
        File dir = new File("D:/tgao/pass");
        ZipUtil.unpack(zip, dir);
    }
}
```

跟进`org.zeroturnaround.zip.ZipUtil#unpack(java.io.File, java.io.File)`
![](https://xzfile.aliyuncs.com/media/upload/picture/20230129110441-aca86b52-9f81-1.png)

继续跟进`org.zeroturnaround.zip.ZipUtil#unpack(java.io.File, java.io.File, org.zeroturnaround.zip.NameMapper)`
![](https://xzfile.aliyuncs.com/media/upload/picture/20230129110738-16132fe6-9f82-1.png)

在上述方法中使用`new ZipUtil.Unpacker(outputDir, mapper)`创建`ZipEntryCallback`对象`(ZipUtil.Unpacker)`
可以先看其中的`org.zeroturnaround.zip.ZipUtil.Unpacker#process`方法
![](https://xzfile.aliyuncs.com/media/upload/picture/20230129111047-86d5afa6-9f82-1.png)

上述代码中的`this.mapper`在调用`org.zeroturnaround.zip.ZipUtil#unpack(java.io.File, java.io.File)`方法中传入的
![](https://xzfile.aliyuncs.com/media/upload/picture/20230129110947-632debc2-9f82-1.png)

进入`org.zeroturnaround.zip.IdentityNameMapper`
![](https://xzfile.aliyuncs.com/media/upload/picture/20230129111145-a92fcdb6-9f82-1.png)

上述的map方法直接将传入的name参数返回并没有任何的过滤。
因此，再看`org.zeroturnaround.zip.ZipUtil.Unpacker#process`方法对`zipEntry.getName()`没有任何的过滤。所以导致了Zip Slip漏洞的产生。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230129111221-bed5d1a6-9f82-1.png)

再回来看看`org.zeroturnaround.zip.ZipUtil#unpack(java.io.File, java.io.File, org.zeroturnaround.zip.NameMapper)`
![](https://xzfile.aliyuncs.com/media/upload/picture/20230129111327-e66d9898-9f82-1.png)

跟进`org.zeroturnaround.zip.ZipUtil#iterate(java.io.File, org.zeroturnaround.zip.ZipEntryCallback)`
![](https://xzfile.aliyuncs.com/media/upload/picture/20230129111354-f66e2d70-9f82-1.png)

继续跟进`org.zeroturnaround.zip.ZipUtil#iterate(java.io.File, org.zeroturnaround.zip.ZipEntryCallback, java.nio.charset.Charset)`
![](https://xzfile.aliyuncs.com/media/upload/picture/20230129111423-07a225ce-9f83-1.png)

可以看到调用了原生的`java.util.zip.ZipFile#ZipFile(java.io.File)`等API
此方法中也没有任何的过滤，直接将zip流内容和ZipEntry传入了`org.zeroturnaround.zip.ZipUtil.Unpacker#process`(`Unpacker#process`在上文已讲过)。

在zt-zip在1.13版本中进行了修复：[https://github.com/zeroturnaround/zt-zip/commit/759b72f33bc8f4d69f84f09fcb7f010ad45d6fff#](https://github.com/zeroturnaround/zt-zip/commit/759b72f33bc8f4d69f84f09fcb7f010ad45d6fff)
![](https://xzfile.aliyuncs.com/media/upload/picture/20230129111523-2b2c5f50-9f83-1.png)

## CVE-2018-1261

引入依赖

```
<dependency>
  <groupId>org.springframework.integration</groupId>
  <artifactId>spring-integration-zip</artifactId>
  <version>1.0.0.RELEASE</version>
</dependency>

<dependency>
  <groupId>org.slf4j</groupId>
  <artifactId>slf4j-api</artifactId>
  <version>1.7.30</version>
</dependency>
<dependency>
  <groupId>org.slf4j</groupId>
  <artifactId>slf4j-simple</artifactId>
  <version>1.7.30</version>
  <type>jar</type>
</dependency>
```

`spring-integration-zip`依赖于`zt-zip`

漏洞代码：实际场景下的的zip包是可控的，如通过文件上传等功能

```
package zip;

import org.springframework.core.io.DefaultResourceLoader;
import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;
import org.springframework.integration.support.MessageBuilder;
import org.springframework.integration.zip.transformer.UnZipTransformer;
import org.springframework.messaging.Message;

import java.io.File;
import java.io.InputStream;

public class Zip3 {
    private static ResourceLoader resourceLoader = new DefaultResourceLoader();

    public static void main(String[] args) {
        final Resource evilResource = resourceLoader.getResource("classpath:poc.zip");
        try{
            InputStream evilIS = evilResource.getInputStream();
            Message<InputStream> evilMessage = MessageBuilder.withPayload(evilIS).build();
            UnZipTransformer unZipTransformer = new UnZipTransformer();
            unZipTransformer.transform(evilMessage);
        }catch (Exception e){
            System.out.println(e);
        }
    }
}
```

跟进`org.springframework.integration.zip.transformer.UnZipTransformer#UnZipTransformer`构造方法
![](https://xzfile.aliyuncs.com/media/upload/picture/20230129112113-fc1205de-9f83-1.png)

跟进`org.springframework.integration.zip.transformer.AbstractZipTransformer#AbstractZipTransformer`构造方法
![](https://xzfi...