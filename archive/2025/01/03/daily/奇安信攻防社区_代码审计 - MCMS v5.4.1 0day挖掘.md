---
title: 代码审计 - MCMS v5.4.1 0day挖掘
url: https://forum.butian.net/share/4006
source: 奇安信攻防社区
date: 2025-01-03
fetch_date: 2025-10-06T20:04:31.981019
---

# 代码审计 - MCMS v5.4.1 0day挖掘

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 代码审计 - MCMS v5.4.1 0day挖掘

* [漏洞分析](https://forum.butian.net/topic/48)

记一次 MCMS v5.4.1 代码审计，编号为 CVE-2024-42990&CVE-2024-42991。本文由笔者首发于先知社区的技术文章板块：https://xz.aliyun.com/t/16630

一、前言
----
`MingSoft MCMS` 是中国铭飞 (MingSoft) 公司的一个完整开源的 `J2ee` 系统，可以到 Github 下载到源码，官网 [铭软・铭飞官网・低代码开发平台・免费开源Java Cms](https://mingsoft.net/)
笔者针对 `MCMS v5.4.1` 进行代码审计，发现存在一个后台 `uploadTemplate` 绕过限制上传 jsp 实现 rce，以及一个前台文件上传 rce，本文将对完整的漏洞挖掘与利用思路进行讲解
MCMS 的最新版本已更新到 `5.4.2`，且已对上述漏洞进行了修复
二、声明
----
该文章仅供学习用途使用，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关
三、环境搭建
------
版本：MCMS v5.4.1，[Release 5.4.1 · ming-soft/MCMS · GitHub](https://github.com/ming-soft/MCMS/releases/tag/5.4.1)
打包成 war，使用 tomcat 搭建
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a844bb288ea2464c8f7cc48ac925141209524b00.png)
四、后台文件上传 CVE-2024-42990
-----------------------
> 该 CVE 编号已分配，但详细信息尚未公开
在后台找到文件上传的地方
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-e56adfff0220d551773e88785129bb7d31213129.png)
抓包，找到对应的路由 `/ms-mcms/ms/file/uploadTemplate.do`
上传一个 zip，里面包含着 jsp，会发现他提示
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-5102539a341818676328435f23510c4654659281.png)
说明他有一个地方在检查我们上传的文件，所以要找到这个地方，查看对应的代码逻辑
最后找到是在 `FileVerifyAop.class`
```java
@Around("uploadPointCut()")
public Object uploadAop(ProceedingJoinPoint joinPoint) throws Throwable {
UploadConfigBean bean = (UploadConfigBean)super.getType(joinPoint, UploadConfigBean.class);
String uploadFileName = FileNameUtil.cleanInvalid(bean.getFile().getOriginalFilename());
if (StringUtils.isBlank(uploadFileName)) {
return ResultData.build().error("文件名不能为空!");
} else {
InputStream inputStream = bean.getFile().getInputStream();
String mimeType = BasicUtil.getMimeType(inputStream, uploadFileName);
if ("zip".equalsIgnoreCase(mimeType)) {
try {
this.checkZip(bean.getFile(), false);
} catch (Exception var7) {
return ResultData.build().error(var7.getMessage());
}
}
return joinPoint.proceed();
}
}
```
打下断点跟踪一下，判断后缀是 zip 之后会进入 `checkZip` 函数，跟进去看一下
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-880c996b3ed4286e7ab77c63253bbe145ee61d94.png)
可以看到他是先解压出来，然后检测每个文件的后缀，如果后缀等于 jsp，就返回 jsp 不可以上传
所以我们需要绕过这个 checkzip。可以看到他进入 check 是需要他得到的后缀为 zip。我们跟进去看看他是如何 `getMimeType` 的
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-fbc79ad888deb2d8782e9e3c04b05895563e5b99.png)
可以发现他返回 `fileType` 之前还获取了 `contentType`，并重新对 `fileType` 进行了赋值，这是否意味着我们可以从这里进行控制返回的 `fileType`？
我们跟进 `parse` 函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-9dc6cc5b913b0dc9d760373d0a55a19dcb19d995.png)
可以发现 type 从这里赋值了，我们进入 `detect` 函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-5112026a02e9a364deef10aaa9fcca2197a512f1.png)
type 在这里赋值了，继续跟进 `detect` 函数。这里是一个循环，要进入第二次循环的 `detect`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-51436ed73ea9bcc3a546b4b29bd10a602c3df720.png)
```java
public MediaType detect(InputStream input, Metadata metadata) throws IOException {
List<MimeType> possibleTypes = null;
if (input != null) {
input.mark(this.getMinLength());
try {
byte[] prefix = this.readMagicHeader(input);
possibleTypes = this.getMimeType(prefix);
} finally {
input.reset();
}
}
String resourceName = metadata.get("resourceName");
String name;
if (resourceName != null) {
name = null;
boolean isHttp = false;
try {
URI uri = new URI(resourceName);
String scheme = uri.getScheme();
isHttp = scheme != null && scheme.startsWith("http");
String path = uri.getPath();
if (path != null) {
int slash = path.lastIndexOf(47);
if (slash + 1 < path.length()) {
name = path.substring(slash + 1);
}
}
} catch (URISyntaxException var16) {
name = resourceName;
}
if (name != null) {
MimeType hint = this.getMimeType(name);
if (!isHttp || !hint.isInterpreted()) {
possibleTypes = this.applyHint(possibleTypes, hint);
}
}
}
name = metadata.get("Content-Type");
if (name != null) {
try {
MimeType hint = this.forName(name);
possibleTypes = this.applyHint(possibleTypes, hint);
} catch (MimeTypeException var14) {
}
}
return possibleTypes != null && !possibleTypes.isEmpty() ? ((MimeType)possibleTypes.get(0)).getType() : MediaType.OCTET\_STREAM;
}
```
这个函数最后返回的就是 `possibleTypes`，所以跟进这个 `getMimeType`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-2b2601e08e59d93697c8d5b43c2256ec728c8a80.png)
发现他是通过文件的二进制数据进行判定是什么 type，在 `eval` 函数中通过数据来判别类型，识别完结果是这个
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-3c39943f7dc3efd190560a0cebae4cbbb65baa5c.png)
这里就可以直接猜测，他识别的是文件头，即在上传的 zip 文件中，添加图片的文件头
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-f31bf820479a059554439b96ff5ebfadba936101.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-33fe6a3a9fd93a37db77f4a71be3dda1a9f21b94.png)
可以看到结果发生了变化，回到起点看看
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-7d4af9e1d56916f4ba2d54cbbd35e77f7297e67a.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-11fdd46e6d5ee7bb9cd7e95282bc626ef358fd5a.png)
成功绕过了 `checkzip` 函数，然后尝试压缩一个 jsp 上传看看
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-6a28e48f2a2fe04110cfcf71527ced6d27fef7b8.png)
发现还是报这个错误，但是和前面的报的不一样，前面是这样的
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-20b5fd39a16d78584daa3b2357bb508af4e8301c.png)
那就继续跟一下，发现是在 `ManageFileAction.class` 的 `uploadTemplate` 路由同样有判断
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a4ddb3164b6f981fc20cd78fdc182ef9286b56e8.png)
跟进到这个 `getType` 函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-bcf15ff1cedd452f366a46c2094690db5948bb91.png)
发现好像同样是由二进制数据判定的，那就往 jsp 文件中加入图片头
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-9ece55b39ed79f9b183264c678c21edd57522a04.png)
然后上传压缩包
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-c5b6570c5dfaad38992de751a8675b12dba49c61.png)
最后访问 jsp 即可
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-1378e279be9dee890b684ec7f17d0b7e004099c6.png)
五、前台文件上传 CVE-2024-42991
-----------------------
该漏洞源于前端文件上传功能的不当处理，可能导致远程命令执行
### 方式一：上传 xml 修改 jsp 解析后缀
在 MCMS 的历史漏洞中，有一个前台文件上传。具体路由是 `/static/plugins/ueditor/1.4.3.3/jsp/editor.do`
经过开发者的修复，能上传的文件变得很有限，详见 `ueditor` 的 `config.json`
```json
/\* 上传文件配置 \*/
"fileActionName": "uploadfile", /\* controller里,执行上传视频的action名称 \*/
"fileFieldName": "upfile", /\* 提交的文件表单名称 \*/
"filePathFormat": "/ueditor/jsp/upload/file/{yyyy}{mm}{dd}/{time}{rand:6}", /\* 上传保存路径,可以自定义保存路径和文件名格式 \*/
"fileUrlPrefix": "", /\* 文件访问路径前缀 \*/
"fileMaxSize": 51200000, /\* 上传大小限制，单位B，默认50MB \*/
"fileAllowFiles": [
".png", ".jpg", ".jpeg", ".gif", ".bmp",
".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid",
".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso",
".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".xml"
], /\* 上传文件格式显示 \*/
```
可以上传 xml 文件
如果环境是 Tomcat，就可以上传 `web.xml` 修改 Tomcat 解析 jsp 的后缀
```xml
<servlet-mapping>
<servlet-name>jsp</servlet-name>
<url-pattern>\*.js...