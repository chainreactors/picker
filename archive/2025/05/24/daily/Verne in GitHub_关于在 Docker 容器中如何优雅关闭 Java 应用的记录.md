---
title: 关于在 Docker 容器中如何优雅关闭 Java 应用的记录
url: https://blog.einverne.info/post/2025/05/docker-java-gracefully-stop.html
source: Verne in GitHub
date: 2025-05-24
fetch_date: 2025-10-06T22:27:07.165279
---

# 关于在 Docker 容器中如何优雅关闭 Java 应用的记录

[Verne in GitHub](/)

* [Archive](/archive.html)
* [Categories](/categories.html)
* [Friends](/friends.html)
* [Tags](/tags.html)
* Other
  + [About](/about.html)
  + [投资笔记](https://invest.einverne.info/)
  + [券商推荐](https://broker.einverne.info/)
  + [图书分享](https://book.einverne.info/)
  + [相册](https://photo.einverne.info/)
  + [Kindle 笔记](https://kindle.einverne.info/)
  + [IPFS 镜像](https://ipfs.einverne.info/)
  + [服务状态](https://status.einverne.info/)
  + [在线嘟嘟](https://m.einverne.info/%40einverne)

# 关于在 Docker 容器中如何优雅关闭 Java 应用的记录

Posted on 05/23/2025
, Last modified on 05/23/2025
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2025-05-23-docker-java-gracefully-stop.md)

这两天遇到一个和 Docker 运行相关的问题，我们使用 Azure App Service 来运行服务，但是每次重启服务的时候，发现不会出发 Javalin 的 stop，感觉 Java 进程没有接受到 Docker 容器停机的信号，然后就被系统杀死了，所以就这个问题，仔细地研究了一下 Docker 运行以及如何优雅地关闭 Docker 容器中的 Java 进程。

## 问题原因

信号是操作系统用于向正在运行的进程发送消息，使其以特定方式运行的一种方式，常见的情况是操作系统会向进程 ID 发送 SIGTERM 信号来终止进程，当我们执行 kill PID 的时候，也是发送 SIGTERM 信号。

使用 `docker stop` 命令时，Docker 会向容器内 PID 1 的进程发送 SIGTERM 信号，如果 Java 应用不是 PID 1 的进程，而是 Shell 的子进程，那么 SIGTERM 信号可能无法正确传递到 Java 应用。

当使用 Shell 脚本启动 Java 应用时，Shell 进程称为 PID，而 Java 进程成为子进程，Shell 进程不会将 SIGTERM 信号转发给子进程，导致 Java 应用永远不会收到关闭信号。

Azure App Service在容器关闭时会发送SIGTERM信号给容器内的PID 1进程。如果应用在默认的30秒超时时间内没有响应，系统会强制发送SIGKILL信号终止进程。

## 使用 exec 命令

在 Dockerfile 中直接使用 exec 格式

```
# 推荐的CMD格式
CMD ["java", "-jar", "application.jar"]

# 而不是
CMD java -jar application.jar
```

Java 进程代替 Shell 进程，成为 PID 1.

## Javalin

对于 Javalin 应用，需要配置服务器的优雅关闭机制

```
Javalin app = Javalin.create(config -> {
    // 配置优雅关闭超时时间
    config.jetty.modifyServer(server ->
        server.setStopTimeout(5000) // 等待5秒让现有请求完成
    );
});

// 添加关闭钩子
Runtime.getRuntime().addShutdownHook(new Thread(() -> {
    app.stop();
}));

// 配置服务器事件监听
app.events(event -> {
    event.serverStopping(() -> {
        System.out.println("服务器正在停止...");
        // 在这里执行清理工作
    });
    event.serverStopped(() -> {
        System.out.println("服务器已停止");
    });
});
```

## Related Posts

* [关于在 Docker 容器中如何优雅关闭 Java 应用的记录](/post/2025/05/docker-java-gracefully-stop.html) - 05/23/2025
* [使用 SyncTV 异地远程一起看视频](/post/2023/11/synctv.html) - 11/26/2023
* [Docker Compose 中使用环境变量](/post/2021/08/docker-compose-environment-variables.html) - 08/29/2021
* [docker volumes 中 -v 和 -mount 区别](/post/2018/03/docker-v-and-mount.html) - 03/13/2018
* [Dockerfile 基础镜像](/post/2017/05/dockerfile-base-image.html) - 05/02/2017
* [Docker 使用 nginx-proxy 来架设多个网站](/post/2017/02/docker-nginx-host-multiple-websites.html) - 02/20/2017

---

* [← Previous（前一篇）](/post/2025/05/ibkr-mutual-fund-etf-replicator.html "IBKR 使用教程系列之共同基金 ETF Replicator")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2025/05/ghostty.html "Zig 语言编写的开源终端 Ghostty")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2025/05/docker-java-gracefully-stop.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [docker 86](/tags.html#docker)
* [java 109](/tags.html#java)
* [sigterm 1](/tags.html#sigterm)
* [shell 18](/tags.html#shell)
* [dockerfile 7](/tags.html#dockerfile)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").