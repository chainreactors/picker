---
title: 升级 Mastodon 从 4.1.19 至 4.2.x
url: https://blog.einverne.info/post/2024/09/mastodon-upgrade-from-4-1-19-to-4-2.html
source: Verne in GitHub
date: 2024-09-15
fetch_date: 2025-10-06T18:20:00.241052
---

# 升级 Mastodon 从 4.1.19 至 4.2.x

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

# 升级 Mastodon 从 4.1.19 至 4.2.x

Posted on 09/14/2024
, Last modified on 09/14/2024
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2024-09-14-mastodon-upgrade-from-4-1-19-to-4-2.md)

记录一下 Mastodon 实例维护，为 4.1.19 升级至 4.2.x 的过程。因为之前的版本还在 4.1.x 所以先按照官方的教程升级到了 4.1.19 最新的版本，然后开始研究如何跨版本升级，之前已经成功将 Mastodon 从 V3 升级到了 V4 版本，我大致猜测应该也差不多，但是为了数据安全起见，还是做了好充分的备份。

## 备份

首先是数据库备份

```
docker exec mastodon-db-1 pg_dump -Fc -U mastodon mastodon > ~/20240914mastodon_backup.dump
```

## 升级

然后修改 docker-compose 文件的版本至 `4.2.0`

然后执行 `docker-compose pull` 拉取最新的镜像。

首先执行

```
docker-compose run --rm -e SKIP_POST_DEPLOYMENT_MIGRATIONS=true web bundle exec rails db:migrate
```

然后运行 Mastodon 实例

```
docker-compose up -d
```

然后执行后处理

```
docker-compose run --rm web bundle exec rails db:migrate
```

最后如果使用 Elsticsearch，那么重新构建索引

```
docker-compose run --rm web bin/tootctl search deploy --reset-chewy
```

完成版本更新，欢迎大家使用 [EV Mastodon](https://m.einverne.info/)

接下来就是小版本的升级，拉取镜像，然后更新即可。

## Related Posts

* [使用 GitHub Actions 构建 Docker 镜像并上传到 GitHub Packages](/post/2024/12/github-actions-docker-image-github-packages.html) - 12/21/2024
* [Wallabag 个人的网站收藏工具](/post/2024/11/wallabag-your-personal-bookmarks.html) - 11/01/2024
* [升级 Mastodon 从 4.1.19 至 4.2.x](/post/2024/09/mastodon-upgrade-from-4-1-19-to-4-2.html) - 09/14/2024
* [使用 SyncTV 异地远程一起看视频](/post/2023/11/synctv.html) - 11/26/2023
* [Mastodon 升级到 V4 版本](/post/2022/11/mastodon-upgrade-to-version-4.html) - 11/15/2022
* [使用 Owncast 搭建自己的在线视频串流直播间](/post/2022/06/use-owncast-build-your-own-livestream.html) - 06/29/2022
* [在停止的 Docker 中其中执行命令](/post/2022/06/run-commands-in-stopped-docker-container.html) - 06/02/2022
* [使用 Docker 安装 Mastodon 实例搭建自己的社交网络](/post/2022/04/install-mastodon-by-docker.html) - 04/21/2022
* [使用 Nginx Proxy Manager 管理 Nginx 代理](/post/2022/02/nginx-proxy-manager.html) - 02/16/2022
* [chevereto 备份及恢复记录](/post/2018/05/chevereto-backup-and-restore.html) - 05/16/2018
* [树莓派中安装 Docker 及 docker compose](/post/2018/03/respberry-pi-install-docker.html) - 03/15/2018
* [docker volumes 中 -v 和 -mount 区别](/post/2018/03/docker-v-and-mount.html) - 03/13/2018
* [docker-compose 中 links 和 depends\_on 区别](/post/2018/03/docker-compose-links-vs-depends-on-differences.html) - 03/12/2018
* [使用 docker compose 管理多个容器](/post/2018/02/docker-compose.html) - 02/15/2018

---

* [← Previous（前一篇）](/post/2024/09/mediacms.html "自托管的开源视频分享平台 MediaCMS")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2024/09/emotivoice.html "EmotiVoice 网易开源的中英文 TTS 引擎")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2024/09/mastodon-upgrade-from-4-1-19-to-4-2.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [mastodon 6](/tags.html#mastodon)
* [mastodon-upgrade 2](/tags.html#mastodon-upgrade)
* [ruby 4](/tags.html#ruby)
* [docker 86](/tags.html#docker)
* [docker-compose 12](/tags.html#docker-compose)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").