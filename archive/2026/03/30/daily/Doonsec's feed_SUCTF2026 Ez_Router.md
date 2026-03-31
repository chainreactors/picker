---
title: SUCTF2026 Ez_Router
url: https://mp.weixin.qq.com/s/Yf4I5lTc0dwNyJq2exjqEg
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:30:23.122474
---

# SUCTF2026 Ez_Router

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1nHvQsR72HeWFlUKI3ZcoxoN24YQeWbD3NRQbKNWcTnEXGsD6KfgVWsEicHgGib3an2EYx0n6CnajmKQ46pe98AoD3WhaMqD4T4/0?wx_fmt=jpeg)

# SUCTF2026 Ez\_Router

zer00ne
zer00ne

看雪学苑

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K2CTWKib54CvEXWSegiclPGkF4IQESibBaqjGXd6ZEHQdfsibGTTexQgGNMDMxqYZ8MeX49nP5ZqKDnibT8XDIiafZfWJdXLLjAkuf98/640?wx_fmt=png&from=appmsg)

**前端越权**

通过抓包登录的报文, 我们可以发现如果先是随便输入一对账密。

会抓到一个发向http的包：

```
GET /www/http?auth=0&action=login HTTP/1.1
Host: 192.168.41.128:8080
Cache-Control: max-age=0
Accept-Language: zh-CN,zh;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://192.168.41.128:8080/index.html
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```

可以看到有一个参数auth=0

此时如果放行报文就会登录失败, 但是将auth的值改成1就可以登录成功

```
GET /control.html HTTP/1.1
Host: 192.168.41.128:8080
Cache-Control: max-age=0
Accept-Language: zh-CN,zh;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://192.168.41.128:8080/index.html
Accept-Encoding: gzip, deflate, br
Cookie: session_id=72cb56e041a043ee6dfc3427033ef203
Connection: keep-alive
```

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K3KYz3LiaYPgNiajNGSfdsARLIaIiacslW92X3Zauv9YsIKHFVgc10YlbyIONMBSTHia63TxT3oUkzQFM7SA5wWKCbd6ZZThPmFWWc/640?wx_fmt=png&from=appmsg)

**二进制分析**

### 架构分析

首先可以来到`固件与备份`, 将这个项目下载得到二进制文件：

```
├── http
├── lib
│   └── libutils.so
├── mainproc
├── start.sh
├── tmp
│   └── sessions
└── www
    ├── cgi-bin
    │   ├── download.cgi
    │   ├── list.cgi
    │   ├── login.cgi
    │   ├── ping.cgi
    │   ├── restart.sh
    │   ├── vpn.cgi
    │   └── wifi.cgi
    ├── control.html
    ├── css
    │   ├── dashboard.css
    │   ├── fontawesome
    │   │   └── css
    │   │       └── all.min.css
    │   └── fonts
    │       ├── inter.css
    │       └── Inter-Regular.woff2
    ├── index.html
    └── js
        └── dashboard.js
```

首先可以分析得到请求的传输流程`html -> /cgi-bin/*.cgi`

对http进行分析, 可以发现这个文件:

1. 将请求转发给`/cgi-bin/*.cgi`
2. 处理静态资源, 并对除了login.html的静态资源进行鉴权
3. 接收`login.cgi`的重定向请求, 并为`auth=1`的会话设置cookie

接下来我们可以结合html页面和`cgi`综合分析每个业务逻辑的链路

### 业务逻辑

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K0bWk5bDSXdicJ8l8uKdDXhdFl3RPo0F7hcShT5WYKRz7BZ8uoslfDIFtjRf24pHGfoon5w2eUdSRg1N45ib0rA5KcwlMjga4U7M/640?wx_fmt=other&from=appmsg)![]()

除了重启按钮以外, 几乎每一个接口都有对应的cgi

直接从docker启动脚本中发现：

```
#!/bin/bash

# Ensure sessions directory exists
mkdir -p /app/tmp/sessions

# Start the main backend process in the background
echo "Starting mainproc..."
./mainproc &

# Give mainproc a moment to initialize (e.g., set up message queues)
sleep 2

# Start the Web Server in the foreground on port 80
echo "Starting http server on port 80..."
./http 80
```

起docker的时候顺手将`mainproc`拉起放置在后台, 可以猜测具体的功能实现在`mainproc`中

### mainproc

现在就该重点分析mainproc了

首先可以发现这个文件中的`init_array`存在一个函数指针：

```
__attribute__((constructor)) voidInit() {
void *ptr = malloc(0xf000);
void *heap_current = sbrk(0);
uintptr_t page_align_mask = ~((uintptr_t)0xFFF);
void *heap_base = (void *)((uintptr_t)ptr & page_align_mask);
mprotect(heap_base, 0x21000, PROT_READ | PROT_WRITE | PROT_EXEC);
free(ptr);
}
```

获取了堆的基地址, 并为其添加了**x**(可执行权限)

```
intmain(int argc, char *argv[]) {
if (argc > 1 && strcmp(argv[1], "-d") == 0) {
if (daemon(1, 0) < 0) {
perror("daemon");
exit(1);
        }
    }
setvbuf(stdout, NULL, _IONBF, 0);
setvbuf(stderr, NULL, _IONBF, 0);
struct router_msgbuf msg;
while (1) {
memset(&msg, 0, sizeof(msg))
if (CFG_GET(0, &msg, sizeof(msg)) == -1) {
usleep(100000);
continue;
        }

dispatch_action(&msg);
    }
return 0;
}
```

接着在dispatch\_action函数中可以发现一个巨大的`switch-case`结构(IDA的反编译会变成if-else结构)

```
switch (msg->mtype) {
case 0x6374fe30:
Set_WIFI(msg);
break;
case 0x74122f00:
case 0x74122c02:
Add_MAC(msg);
break;
case 0x32ee2000:
case 0x32ef2030:
Del_MAC(msg);
break;
case 0x9313f7e0:
Set_VPN(msg);
break;
case 0xe6133f10:
Edit_VPN_Custom(msg);
break;
case 0x96e7ff60:
Apply_VPN();
break;
default:
printf("[WARN] Received unknown message type: 0x%lx\n", msg->mtype);
break;
```

根据不同的魔数, 调用不同功能的函数, 从cgi中提取不同的功能可以整理出接口与处理函数的对应关系。

接下来应该梳理不同结构体, 结构体从IDA静态分析不是很容易, 推荐通过gdb调试描绘结构体轮廓。

**黑白名单 :**

```
struct __attribute__((packed)) mac_req {
    int idx;
    char mac[0x10];
    char note[0x1c];
};
```

**wifi设置 :**

```
struct wifi_req {
    char ssid[0x40];
    char password[0x40];
};
```

这两种结构体只会在堆上创建两种不同大小的堆块, 没有具体的作用

**vpn :**

在vpn.cgi中

```
struct __attribute__((packed)) vpn_recv {
        char action[0x20];
        char name[0x20];
        char proto[0x20];
        char server[0x30];
        char user[0x20];
        char pass[0x20];
        char cert[8];
        char gap[1];
        char custom[3000];
};
```

在mainproc中

```
struct vpn_config_req {
    uint16_t custom_len;
    char _pad[6];
    char cert[8];
    void (*apply_cb)(struct vpn_config_req *);
    char action[0x20];
    char name[0x20];
    char proto[0x20];
    char server[0x30];
    char user[0x20];
    char pass[0x20];
    char *custom_ptr;
};
```

可以发现vpn结构体在两个进程中的结构差异很大, 且在mainproc中存在函数和内存两种指针。

**不同的处理函数的逻辑很简单**, 包括vpn也是, 从cgi结构体中将同名成员复制到mainproc结构体中。

但是注意, 这里使用了**不安全的strcpy**且没有做保护：

```
void Set_VPN(struct router_msgbuf *msg) {
    int idx = 0;
if (vpn_list[idx]) {
printf("[!] VPN already configured once. Use Edit_VPN_Custom for modifications.\n");
return;
    }

struct vpn_recv *input = (struct vpn_recv *)msg->payload;

    vpn_list[idx] = (struct vpn_config_req *)malloc(sizeof(struct vpn_config_req));
    size_t custom_len = strlen(input->custom);
    vpn_list[idx]->custom_len = custom_len;
if (custom_len > 0) {
        vpn_list[idx]->custom_ptr = malloc(custom_len + 1);
memcpy(vpn_list[idx]->custom_ptr, input->custom, custom_len);
        vpn_list[idx]->custom_ptr[custom_len] = '\0';
    } else {
        vpn_list[idx]->custom_ptr = NULL;
    }
    vpn_list[idx]->apply_cb = default_vpn_apply;
strcpy(vpn_list[idx]->action, input->action);
strcpy(vpn_list[idx]->name, input->name);
strcpy(vpn_list[idx]->proto, input->proto);
strcpy(vpn_list[idx]->server, input->server);
strcpy(vpn_list[idx]->user, input->user);
strcpy(vpn_list[idx]->pass, input->pass);
memcpy(vpn_list[idx]->cert, input->cert,sizeof(input->cert));
}
```

我们知道这些成员都是从json中取出来的, 一般的json都会在字段的结构加上'\0'

但如果我们前往.so审计

```
voidextract_json_string(constchar *json, constchar *key, char *out, size_t max_len) {
    out[0] = '\0';
char search_key[128];
snprintf(search_key, sizeof(search_key), ""%s"", key);

char *p = strstr(json, search_key);
if (!p) return;

    p += strlen(search_key);
while (*p == ' ' || *p == ':') p++;

if (*p == '"') {
        p++;
size_t i = 0;
while (*p != '"' && *p != '\0' && i < max_len) {
if (*p == '\\' && *(p+1) != '\0') {
if (*(p+1) == '\\' && *(p+2) == 'x' && isxdigit(*(p+3)) && isxdigit(*(p+4))) {
char hex[3] = { *(p+3), *(p+4), 0 };
                    out[i++] = (char)strtol(hex, NULL, 16);
                    p += 4;
                }
else if (*(p+1) == 'x' && isxdigit(*(p+2)) && isxdigit(*(p+3))) {
char hex[3] = { *(p+2), *(p+3), 0 };
                    out[i++] = (char)strtol(hex, NULL, 16);
                    p += 3;
                }
else {
                    p++;
if (*p == 'n') out[i++] = '\n';
else if (*p == 'r') out[i++] = '\r';
else if (*p == '"') out[i++] = '"';
else if (*p == '\\') out[i++] = '\\';
else out[i++] = *p;
                }
            } else {
                out[i++] = *p;
            }
            p++;
        }
if (i < max_len) {
            out[i] = '\0';
        }
    }
}...