---
title: 泛微云桥文件上传与JFinal Bypass
url: https://y4tacker.github.io/2024/07/26/year/2024/7/%E6%B3%9B%E5%BE%AE%E4%BA%91%E6%A1%A5%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E4%B8%8EJFinal-Bypass/
source: Y4tacker:Hacking The World!
date: 2024-07-26
fetch_date: 2025-10-06T17:40:31.041210
---

# 泛微云桥文件上传与JFinal Bypass

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

Previous post Next post Back to top Share post

1. [1. 漏洞分析](#%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
2. [2. Bypass JFinal WebShell落地限制](#Bypass-JFinal-WebShell%E8%90%BD%E5%9C%B0%E9%99%90%E5%88%B6)
3. [3. Bypass JFinal WebShell访问限制](#Bypass-JFinal-WebShell%E8%AE%BF%E9%97%AE%E9%99%90%E5%88%B6)

# 泛微云桥文件上传与JFinal Bypass

Y4tacker

2024-07-26 (Updated: 2025-09-02)

[Java](/categories/Java/)

[Java](/tags/Java/), [云桥](/tags/%E4%BA%91%E6%A1%A5/)

## 漏洞分析

无意间发现泛微官网做了紧急安全更新<https://www.weaver.com.cn/cs/security/edm20240725_kdielfrovkewpiiuyrtewtw.html>

比较好的是官网公告中给出了实际利用的地址:`/wxclient/app/recruit/resume/addResume?fileElementld=aaa`

因此我们直接进入代码看看逻辑即可

经过简单的搜索发现，对应处理类在`weaver.weixin.app.recruit.controller.ResumeController#addResume`

逻辑非常简单，只需要关注第一个if所在片段即可，因为后面的处理逻辑主要与数据库操作有关

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` | ``` @ActionKey("/wxclient/app/recruit/resume/addResume") @Before({Tx.class}) public void addResume() throws Exception {     try {         WxBaseFile wbFile = null;         if (this.getContentType().toLowerCase().startsWith("multipart/form-data")) {             wbFile = this.getWxBaseFile(this.wxBaseFileService, this.getPara("fileElementId"), (String)null, 2097152, (String)null);         }          ResumeModel model = (ResumeModel)this.getModel(ResumeModel.class, "resume");         if (wbFile != null) {             model.set("accessory", wbFile.getId());         }          if (this.resumeService.addResume(model, this.getPara("sysagentid"))) {             this.renderJsonMsgForIE("提交成功", true);         } else {             this.renderJsonMsgForIE("提交失败", false);         }      } catch (Exception var3) {         if (var3.getMessage().indexOf("2097152") != -1) {             this.renderJsonMsgForIE("上传文件大小不能超过2M", false);         } else {             this.log.error(var3.getMessage(), var3);             this.renderJsonMsgForIE("程序异常，请联系管理员！", false);         }          throw var3;     } } ``` |

对应在`weaver.weixin.core.controller.BaseController#getWxBaseFile(weaver.weixin.base.service.WxBaseFileService, String, String, int, String)`，由于传入的参数中`filePath`与`fileEncoding`为空，所以会分别调用`FileUploadTools`的不同方法，编码比较简单就是`UTF-8`，我们主要看文件路径处理部分

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` | ``` public WxBaseFile getWxBaseFile(WxBaseFileService wxBaseFileService, String parameterName, String filePath, int fileMaxSize, String fileEncoding) throws Exception {     String _filePath = StrKit.isBlank(filePath) ? FileUploadTools.getRandomFilePath() : filePath;     int _fileMaxSize = fileMaxSize == -1 ? FileUploadTools.getMaxSize() : fileMaxSize;     String _fileEncoding = StrKit.isBlank(fileEncoding) ? FileUploadTools.getEncoding() : fileEncoding;     UploadFile uf = null;      try {         uf = this.getFile(parameterName, _filePath, _fileMaxSize, _fileEncoding);     } catch (Exception var11) {         this.getFile();         throw var11;     }      return this.parseUploadFile(wxBaseFileService, uf); } ``` |

从以下逻辑中我们不难推断出文件上传的路径为`/upload/年月/两个随机字符/`

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` | ``` // weaver.weixin.base.file.FileUploadTools#getRandomFilePath private static SimpleDateFormat sdf = new SimpleDateFormat("yyyyMM");  public static String getRandomFilePath() {     return initFilePath(); }  public static String initFilePath() {     StringBuffer sb = new StringBuffer();     if (GCONST.getFileRootPath() != null && !"".equals(GCONST.getFileRootPath())) {         sb.append(GCONST.getFileRootPath());     } else {         sb.append(PathKit.getWebRootPath() + File.separator + "upload");     }      sb.append(File.separator + sdf.format(new Date()));     sb.append(File.separator + getUpEng());     return sb.toString(); }  public static String getUpEng() {     Random r = new Random();     char c = (char)(r.nextInt(26) + 65);     char b = (char)(r.nextInt(26) + 65);     return String.valueOf(c) + String.valueOf(b); } ``` |

回到`weaver.weixin.core.controller.BaseController#getWxBaseFile(weaver.weixin.base.service.WxBaseFileService, String, String, int, String)`

我们重点是查看`try-catch`分支的代码

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` try {     uf = this.getFile(parameterName, _filePath, _fileMaxSize, _fileEncoding); } catch (Exception var11) {     this.getFile();     throw var11; } ``` |

跟进`com.jfinal.core.Controller#getFile(java.lang.String, java.lang.String, java.lang.Integer, java.lang.String)`，在第一行`getFiles`的调用中可以看到先是初始化了一个`MultipartRequest`对象

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` | ``` public UploadFile getFile(String parameterName, String saveDirectory, Integer maxPostSize, String encoding) {     this.getFiles(saveDirectory, maxPostSize, encoding);     return this.getFile(parameterName); }  public List<UploadFile> getFiles(String saveDirectory, Integer maxPostSize, String encoding) {     if (!(this.request instanceof MultipartRequest)) {         this.request = new MultipartRequest(this.request, saveDirectory, maxPostSize, encoding);     }      return ((MultipartRequest)this.request).getFiles(); }  public UploadFile getFile(String parameterName) {     List<UploadFile> uploadFiles = this.getFiles();     Iterator var4 = uploadFiles.iterator();      while(var4.hasNext()) {         UploadFile uploadFile = (UploadFile)var4.next();         if (uploadFile.getParameterName().equals(parameterName)) {             return uploadFile;         }     }      return null; } ``` |

同样的在初始化过程中，我们主要可以看它通过`wrapMultipartRequest`包装了我们的请求

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 ``` | ``` public MultipartRequest(HttpServletRequest request, String saveDirectory, int maxPostSize, String encoding) {     super(request);     this.wrapMultipartRequest(request, saveDirectory, maxPostSize, encoding); }  public MultipartRequest(HttpServletRequest request, String saveDirectory, int maxPostSize) {     super(request);     this.wrapMultipartRequest(request, saveDirectory, maxPostSize, encoding); }  public MultipartRequest(HttpServletRequest request, String saveDirectory) {     super(request);     this.wrapMultipartRequest(request, saveDirectory, maxPostSize, encoding); }  public MultipartRequest(HttpServletRequest request) {     super(request);     this.wrapMultipartRequest(request, saveDirectory, maxPostSize, encoding); }   private void wrapMultipartRequest(HttpServletRequest request, String saveDirectory, int maxPostSize, String encoding) {     if (!isMultipartSupported) {         throw new RuntimeException("Oreilly cos.jar is not found, Multipart post can not be supported.");     } else {         saveDirectory = this.handleSaveDirectory(saveDirectory);         File dir = new File(saveDirectory);         if (!dir.exists() && !dir.mkdirs()) {             throw new RuntimeException("Directory " + saveDirectory + " not exists and can not create directory.");         } else {             this.uploadFiles = new ArrayList();              try {                 this.multipartRequest = new com.oreilly.servlet.MultipartRequest(request, saveDirectory, maxPostSize, encoding, fileRenamePolicy);                 Enumeration files = this.multipartRequest.getFileNames();                  while(files.hasMoreElements()) {                     String name = (String)files.nextElement();                     String filesystemName = this.multipartRequest.getFilesystemName(name);                     if (filesystemName != null) {                         String originalFileName = this.multipartRequest.getOriginalFileName(name);                         String contentType = this.multipartRequest.getContentType(name);                         UploadFile uploadF...