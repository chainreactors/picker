---
title: PHP开发服务器远程源代码泄露漏洞原理剖析
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247500523&idx=1&sn=9ea77ceff0668330f4f0335064b8f8d3&chksm=fa521755cd259e436f5328e93c4ce6396fc8df2e2a97223994abff5f3b1311d0ef2eae169d6d&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2023-03-25
fetch_date: 2025-10-04T10:38:33.486841
---

# PHP开发服务器远程源代码泄露漏洞原理剖析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnR5jibvuTtVg7DvbUGnOV0V3w2NNwcr4hXlaib96yo38kly4ywN0TrfPSbze3RxrPnCUA4GyEicsAJsQ/0?wx_fmt=jpeg)

# PHP开发服务器远程源代码泄露漏洞原理剖析

山石网科安全技术研究院

‍PHP Built-in Server是PHP自带的Web服务器，多用于在研发阶段快速启动并运行一个可以执行PHP脚本的Web服务器。由于其性能及安全性并没有得到完好的保障，故PHP官方并不建议在生产环境下使用这个服务器。

**0****1**

**历史问题**

```
1、Windows下可以在文件名后面增加点号（.）来下载到PHP文件源码

2、Windows下通过修改文件名大小写来下载PHP文件源码

3、Windows下通过在文件名后面增加::$DATA来下载PHP文件源码

4、Linux下修改文件后缀的大小写造成解析漏洞
```

#

**0****2‍**

**PHP 开发服务器 <= 7.4.21 - 远程源泄露** **‍‍‍‍‍‍‍‍‍**

经过测试，我们发现该漏洞不存在于最新的 PHP 版本中。我们对不同版本的 PHP 进行了进一步测试，以确定错误修复的时间和原因。通过调查，我们发现 PHP 7.4.22 的补丁版本，通过比较未打补丁的代码和打补丁的代码，我们可以看到为修复漏洞所做的具体更改。

需要注意的是，虽然此问题已在 PHP 源代码中得到解决，但 Shodan 查询揭示了内置服务器的许多暴露实例。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR5jibvuTtVg7DvbUGnOV0V3fQZv9WibI0IBFjNBVSWiaBLlzJFsXmsZpBzyZ9pmHmzdDsET5golzkoQ/640?wx_fmt=png)

**0****3‍‍**

**原因‍**

为了充分了解该错误及其修复方式，我们在启用调试符号的情况下编译了已打补丁和未打补丁的 PHP 版本。使用概念验证 (PoC) 请求，我们触发了源代码泄露错误并观察了调试器中的代码流。

```
GET /phpinfo.php HTTP/1.1
Host: pd.research
\r\n
\r\n
GET / HTTP/1.1
\r\n
\r\n
```

所有对 CLI 服务器的 HTTP 请求都由`php_cli_server_client_read_request`. 跟踪看起来像这样：

```
main(...)
 do_cli_server(...)
  php_cli_server_do_event_loop(...)
   php_cli_server_do_event_for_each_fd(...)
     php_cli_server_poller_iter_on_active(...)
      php_cli_server_do_event_for_each_fd_callback(...)
        php_cli_server_recv_event_read_request(...)
         php_cli_server_client_read_request(...)
```

`php_cli_server_client_read_request`函数调用函数，`php_http_parser_execute`顾名思义，就是用来解析HTT当下面提到的请求的第一部分几乎完成解析时：

```
GET /phpinfo.php HTTP/1.1
Host: pd.research
\r\n
\r\n
```

并且 HTTP 请求不包含`Content-Length`标头，`CALLBACK2(message_complete)`在下面的代码中调用。在这里，是一个宏，它会在请求消息处理完成后`CALLBACK2`依次调用回调函数。`php_cli_server_client_read_request_on_message_complete`

```
if (parser->type == PHP_HTTP_REQUEST || php_http_should_keep_alive(parser)) {
/* Assume content-length 0 - read the next */
  CALLBACK2(message_complete); // Here
  state = NEW_MESSAGE(); // Afterwards the state is reverted back to start_state
}
```

**CALLBACK2(…) 是如何工作的？**

```
#define CALLBACK2(FOR)                                               \\
do {                                                                 \\
  if (settings->on_##FOR) {                                          \\
    if (0 != settings->on_##FOR(parser)) return (p - data);          \\
  }                                                                  \\
}                     \\
while (0)
```

预处理后，CALLBACK2(message\_complete)转换为：

```
do {
if (settings->on_message_complete) {
 if (0 != **settings->on_message_complete**(parser)) return (p - data);
}
} while (0)
```

**settings**是一个类型的结构，`php_http_parser_settings`

设置变量的每个成员都填充有各自的回调函数。

然后将此对**设置**`php_http_parser_execute`的引用作为参数传递给函数。

```
nbytes_consumed = php_http_parser_execute(&client->parser, &settings, buf, nbytes_read);
```

同样，有`CALLBACK`和`CALLBACK_NOCLEAR`宏的工作方式几乎相同。

因此，`CALLBACK2(message_complete)`结果在调用`php_cli_server_client_read_request_on_message_complete(...)`和`CALLBACK(path)`调用`php_cli_server_client_read_request_on_path(...)`等。

```
static int php_cli_server_client_read_request_on_message_complete(php_http_parser *parser)
{
 ...
 php_cli_server_request_translate_vpath(&client->request, client->server->document_root, client->server->document_root_len);
 ...
}
```

很快，我们进入`php_cli_server_request_translate_vpath`功能。此函数将请求的 PHP 文件的路径转换为文件系统上的完整路径。如果请求的文件是目录，它会检查目录中是否存在索引文件，`index.php`如果`index.html`找到，则使用其中一个文件的路径。这允许服务器响应请求提供正确的文件

简而言之，此函数将结构`vpath`和`path_translated`成员设置为`request`结构。所以，对于当前解析的请求，

```
GET /phpinfo.php HTTP/1.1
Host: pd.research
\r\n
\r\n
```

我们最终进入了`**request->path_translated**`设置了的条件分支。这个很重要，后面会用到。

```
static void php_cli_server_request_translate_vpath(php_cli_server_request *request, const char *document_root, size_t document_root_len) {
...
    else {

     pefree(request->vpath, 1);
     request->vpath = pestrndup(vpath, q - vpath, 1);
     request->vpath_len = q - vpath;
     // At this time buf is equal to /tmp/php/phpinfo.php where /tmp/php/
     // is whatever the server's working directory is.
     request->path_translated = buf;
     // so the request->path_translated is now /tmp/php/phpinfo.php
     request->path_translated_len = q - buf;
     ...
    }
...

}
```

函数调用堆栈展开后，我们继续执行内部流程`php_http_parser_execute`。现在，请求的第二部分被解析为状态恢复为`start_state`：

```
GET / HTTP/1.1
\r\n
\r\n
```

和最初的请求一样，我们进入`php_cli_server_client_read_request_on_message_complete`函数，然后调用`php_cli_server_request_translate_vpath`. 这个过程用于像第一次请求一样解析和处理后续请求。

这一次，在 内部`php_cli_server_request_translate_vpath`，由于我们请求的是目录 ( `/`) 而不是文件，因此我们将输入不同的代码块。

```
...
// loops and checks for index.php, index.html inside working dir
while (*file) {
 size_t l = strlen(*file);
 memmove(q, *file, l + 1);
 if (!php_sys_stat(buf, &sb) && (sb.st_mode & S_IFREG)) {
  q += l
  break;
 }
 file++;
}

 if (!*file || is_static_file) {
 // In case, index files are not present we enter here

  if (prev_path) {
  pefree(prev_path, 1);
  }

  pefree(buf, 1);
  return; // This time we return from the function
      // and no request->vpath or request->path_translated
      // is set.
 }
...
```

最后，在请求解析完成后，我们从`php_http_parser_execute`. `nbytes_consumed`比较已解析字节长度 ( ) 和已读取字节长度( )的返回值`nbytes_read`（更多信息请参见此处）。如果它们相等，代码流继续，我们进入`php_cli_server_dispatch`函数。

```
static  int  php_cli_server_dispatch(php_cli_server *server, php_cli_server_client *client) {
...
 if (client->request.ext_len != 3
 || (ext[0] != 'p' && ext[0] != 'P') || (ext[1] != 'h' && ext[1] != 'H') || (ext[2] != 'p' && ext[2] != 'P')
 || !client->request.path_translated) {

 is_static_file = 1;
 }
...
}
```

上面提供的代码包括一个检查，以确定请求的文件是否应该被视为静态文件或作为 PHP 文件执行。这是通过检查文件的扩展名来完成的。如果扩展名不是`.php`或`.PHP`，或者扩展名的长度不等于 3，则认为该文件是静态文件。这通过将`is_static_file`变量设置为 1 来指示。

该代码还检查对象的`path_translated`字段`client->request`是否不为空。该字段包含文件系统上所请求文件的完整路径，用于定位和提供文件。如果该`path_translated`字段为空，则表示找不到请求的文件，请求将被视为错误。

代码流继续执行该`php_cli_server_begin_send_static`函数，因为`is_static_file`它被设置为 true。

```
if (!is_static_file) {
   ... // Executes the file as PHP script
} else {
   ...
   if (SUCCESS != php_cli_server_begin_send_static(server, client)) {
    php_cli_server_close_connection(server, client);
  }
 ...
}
```

## ‍‍

**0****4‍**

**错误**

这就是错误所在。如上述代码块中所示，在解析第二个请求后，`vpath`设置为`/`并假设未找到索引文件`client->request.ext`将设置为`NULL`. 但是，`client->request.path_translated`仍然设置为`/tmp/php/phpinfo.php`来自第一个请求。检查是在`client->request.ext`第二个请求的时候执行的，我们进入这个分支并将其设置`is_static_file`为`1`。基本上，将请求的文件视为静态文件而不是 PHP 脚本。

```
static int php_cli_server_begin_send_static(php_cli_server *server, php_cli_server_client *client) {
 #ifdef PHP_WIN32
 ...
 #else
 fd = client->request.path_translated ? open(client->request.path_translated, O_RDONLY): -1;
 #endif...
 client->file_fd = fd;
 ...
}
```

请注意，此函数打开文件描述符并将其检索到存储在`client->request.path_translated`. 在我们的示例中，`client->request.path_translated`将设置为`/tmp/php/phpinfo.php`. 这种差异，即检查发生在`client->request.ext`第二个请求上，但随后打开`client->request.path_translated`第一个请求设置的文件，导致源代码泄露。

现在文件被标记为`is_static_file`，代码流现在只读取 fd 并将其作为静态文件返回，而不是执行它。

**0****5‍**

**修复**

PHP 7.4.22 中引入了检查。此修复程序在解析请求路径时检查结构的`vpath`成员是否不为 NULL。`request`如果它不为 NULL，则函数返回 1。

```
static int php_cli_server_client_read_request_on_path(php_http_parser *parser, const char *at, size_t length)
{
 ...
   if (UNEXPECTED(client->request.vpath != NULL)) {
   return 1;
  }
 ...
 }
 return 0;
}
```

解析请求消息第一部分的路径时，`client->request.vpath`最初为 NULL，后来设置为`/phpinfo.php`。但是，当解析请求的第二部分的路径时，`client->request.vpath`已经设置了而不是 NULL，这导致函数返回 1。

```
#define CALLBACK(FOR)                                                \\
do {                                                                 \\
  CALLBACK_NOCLEAR(FOR);                                             \\
  FOR##_mark = NULL;                                                 \\
} while (0)

#define CALLBACK_NOCLEAR(FOR)                                        \\
do {                                                                 \\
  if (FOR##_mark) {                     ...