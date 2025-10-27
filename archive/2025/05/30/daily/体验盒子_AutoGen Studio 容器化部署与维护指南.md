---
title: AutoGen Studio 容器化部署与维护指南
url: https://www.uedbox.com/post/119359/
source: 体验盒子
date: 2025-05-30
fetch_date: 2025-10-06T22:26:51.460161
---

# AutoGen Studio 容器化部署与维护指南

[![体验盒子](https://www.uedbox.com/wp-content/themes/UB2019/imgs/logo.png)](https://www.uedbox.com)

* [博文](https://www.uedbox.com/blog/ "博文")
* [设计开发](https://www.uedbox.com/design/ "设计开发")
* [网络安全](https://www.uedbox.com/web-security/ "网络安全")
* [观点](https://www.uedbox.com/entertainment/ "观点")
* [服务](https://www.uedbox.com/service/ "服务")
* [AI导航](https://www.uedbox.com/aihub/ "AI导航")
* 更多
  + [关于](https://www.uedbox.com/about/ "关于")
  + [分享](https://www.uedbox.com/share/ "分享")
  + [老电影](https://www.uedbox.com/movie/ "老电影")
  + [搜索语法/SHDB](https://www.uedbox.com/shdb/ "搜索语法/SHDB")
  + [Exploits](https://www.uedbox.com/exploits/ "Exploits")
  + [SecTools](https://www.uedbox.com/tools/ "SecTools")
  + [UserAgent解析](https://www.uedbox.com/useragentparser/ "UserAgent解析")
  + [地理坐标在线转换](https://www.uedbox.com/geocoordinate/ "地理坐标在线转换")

# AutoGen Studio 容器化部署与维护指南

* 发表于 2025年05月29日
* [服务器](https://www.uedbox.com/design/%E6%9C%8D%E5%8A%A1%E5%99%A8/)

*适用于 macOS + OrbStack/Docker 环境*

---

目录表

Toggle

* [1. 安装前准备](#1_%E5%AE%89%E8%A3%85%E5%89%8D%E5%87%86%E5%A4%87)
  + [1.1 系统要求](#11_%E7%B3%BB%E7%BB%9F%E8%A6%81%E6%B1%82)
  + [1.2 环境验证](#12_%E7%8E%AF%E5%A2%83%E9%AA%8C%E8%AF%81)
* [2. 初始安装步骤](#2_%E5%88%9D%E5%A7%8B%E5%AE%89%E8%A3%85%E6%AD%A5%E9%AA%A4)
  + [2.1 创建项目目录](#21_%E5%88%9B%E5%BB%BA%E9%A1%B9%E7%9B%AE%E7%9B%AE%E5%BD%95)
  + [2.2 编写配置文件](#22_%E7%BC%96%E5%86%99%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6)
    - [Dockerfile](#Dockerfile)
    - [docker-compose.yml](#docker-composeyml)
  + [2.3 构建并启动容器](#23_%E6%9E%84%E5%BB%BA%E5%B9%B6%E5%90%AF%E5%8A%A8%E5%AE%B9%E5%99%A8)
* [3. 数据持久化](#3_%E6%95%B0%E6%8D%AE%E6%8C%81%E4%B9%85%E5%8C%96)
  + [3.1 数据目录结构](#31_%E6%95%B0%E6%8D%AE%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84)
  + [3.2 持久化原理](#32_%E6%8C%81%E4%B9%85%E5%8C%96%E5%8E%9F%E7%90%86)
* [4. 日常使用](#4_%E6%97%A5%E5%B8%B8%E4%BD%BF%E7%94%A8)
  + [4.1 服务管理命令](#41_%E6%9C%8D%E5%8A%A1%E7%AE%A1%E7%90%86%E5%91%BD%E4%BB%A4)
  + [4.2 访问 Web 界面](#42_%E8%AE%BF%E9%97%AE_Web_%E7%95%8C%E9%9D%A2)
* [5. 更新到新版本](#5_%E6%9B%B4%E6%96%B0%E5%88%B0%E6%96%B0%E7%89%88%E6%9C%AC)
  + [5.1 更新操作流程](#51_%E6%9B%B4%E6%96%B0%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B)
  + [5.2 注意事项​​](#52_%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9%E2%80%8B%E2%80%8B)
  + [5.3 回滚旧版本](#53_%E5%9B%9E%E6%BB%9A%E6%97%A7%E7%89%88%E6%9C%AC)
* [6. 备份与恢复](#6_%E5%A4%87%E4%BB%BD%E4%B8%8E%E6%81%A2%E5%A4%8D)
  + [6.1 数据备份](#61_%E6%95%B0%E6%8D%AE%E5%A4%87%E4%BB%BD)
  + [6.2 数据恢复](#62_%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D)
* [7. 故障排除](#7_%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4)
  + [7.1 常见问题](#71_%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98)
  + [7.2 环境重置](#72_%E7%8E%AF%E5%A2%83%E9%87%8D%E7%BD%AE)

## 1. 安装前准备

### 1.1 系统要求

* macOS 10.15 或更高版本（支持 Intel 和 Apple Silicon 芯片）
* 已安装 [OrbStack](https://orbstack.dev/) 或 Docker Desktop
* 终端基础操作能力（需熟悉
  `bash`
  命令）

### 1.2 环境验证

|  |  |
| --- | --- |
| 1  2  3  4 | # 验证 Docker 是否就绪  docker --version          # 示例输出: Docker version 24.0.6  docker-compose --version  # 示例输出: Docker Compose version v2.23.0 |

## 2. 初始安装步骤

### 2.1 创建项目目录

|  |  |
| --- | --- |
| 1  2  3 | mkdir -p ~/autogen-studio/data/.autogenstudio  cd ~/autogen-studio |

### 2.2 编写配置文件

#### Dockerfile

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23 | # 文件名必须为 "Dockerfile"（无扩展名）  FROM python:3.10-slim    # 安装系统依赖  RUN apt-get update && apt-get install -y \  curl \  build-essential \  && curl -fsSL https://deb.nodesource.com/setup\_16.x | bash - \  && apt-get install -y nodejs \  && rm -rf /var/lib/apt/lists/\*    # 安装前端工具链  RUN npm install -g gatsby-cli yarn    # 安装 AutoGen Studio  RUN pip install --no-cache-dir autogenstudio    # 暴露端口  EXPOSE 8081    # 启动命令  CMD ["autogenstudio", "ui", "--port", "8081", "--host", "0.0.0.0", "--appdir", "/data/.autogenstudio"] |

#### docker-compose.yml

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10 | services:  autogenstudio:  build: .  container\_name: autogenstudio  ports:  - "8081:8081"  volumes:  - ./data:/data  restart: always |

### 2.3 构建并启动容器

|  |  |
| --- | --- |
| 1  2 | docker compose up -d --build |

---

## 3. 数据持久化

### 3.1 数据目录结构

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10 | ~/autogen-studio/  ├── Dockerfile  ├── docker-compose.yml  └── data/  └── .autogenstudio/  ├── agents.json  ├── chat\_sessions.json  ├── settings.json  └── ... |

### 3.2 持久化原理

* 所有运行时产生的数据都保存在
  `./data/.autogenstudio`
  。
* 通过
  `volumes`
  将宿主机
  `data`
  映射到容器内
  `/data`
  ，保证数据不会因容器重建而丢失。

---

## 4. 日常使用

### 4.1 服务管理命令

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | # 启动服务  docker compose up -d    # 停止服务  docker compose down    # 查看日志  docker compose logs -f    # 重启服务  docker compose restart |

### 4.2 访问 Web 界面

浏览器访问：

|  |  |
| --- | --- |
| 1  2 | http://localhost:8081 |

---

## 5. 更新到新版本

### 5.1 更新操作流程

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10 | # 停止并移除现有容器  docker compose down    # 完全重建镜像（例如 AutoGen Studio 发布了新版本）  # 重新拉取最新依赖（如 Dockerfile 中版本无锁定）  docker compose build --no-cache    # 启动服务（原有数据自动挂载）  docker compose up -d |

### 5.2 注意事项​​

* ​性能开销​​：
  `--no-cache`
  会显著增加构建时间（需重新下载所有依赖）。
* ​旧镜像清理​​：重建后建议清理旧镜像：
  `docker image prune # 删除悬空镜像`
* ​数据安全​​：如果希望​​同时重置数据​​，需手动删除挂载目录：
  `rm -rf ./data/.autogenstudio`

### 5.3 回滚旧版本

若需回滚，请提前备份
`data/`
 目录，并恢复旧版
`Dockerfile`
。

---

## 6. 备份与恢复

### 6.1 数据备份

|  |  |
| --- | --- |
| 1  2 | tar -czf backup-autogenstudio-$(date +%F).tar.gz data/ |

### 6.2 数据恢复

|  |  |
| --- | --- |
| 1  2 | tar -xzf backup-autogenstudio-xxxx-xx-xx.tar.gz |

---

## 7. 故障排除

### 7.1 常见问题

| 问题描述 | 解决方案 |
| --- | --- |
| 无法访问网页 | 确保容器正常运行，访问的是  `localhost:8081` |
| 数据丢失 | 检查  `volumes`  是否挂载正确 |
| 日志中报错 | 查看详细日志  `docker compose logs -f` |
| 更改配置未生效 | 重启容器或重新构建  `docker compose up -d --build` |

### 7.2 环境重置

**⚠ 警告：将清空所有数据！**

|  |  |
| --- | --- |
| 1  2 | docker compose down -v  rm -rf data/ |

点赞(0)

打赏

分享

标签：[AutoGen](https://www.uedbox.com/post/tag/autogen/) , [AutoGen Studio](https://www.uedbox.com/post/tag/autogen-studio/) , [docker](https://www.uedbox.com/post/tag/docker/) , [OrbStack](https://www.uedbox.com/post/tag/orbstack/)  原文连接：**[AutoGen Studio 容器化部署与维护指南](https://www.uedbox.com/post/119359/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[肌理解剖师：中年人的小确幸](https://www.uedbox.com/post/119356/ "肌理解剖师：中年人的小确幸") [好用的Mac清理卸载软件推荐](https://www.uedbox.com/post/119673/ "好用的Mac清理卸载软件推荐")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

没有相关文章

[![Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/post/119731/ "Nginx 利用 fail2ban 自动封禁乱扫的 IP")

[![最新 绕过Cloudflare最佳实践](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

最新 绕过Cloudflare最佳实践](https://www.uedbox.com/post/119716/ "最新 绕过Cloudflare最佳实践")

[![NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/post/119688/ "NinjiaTag，兼容Apple Find My网络的开源防丢神器")

[![好用的Mac清理卸载软件推荐](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

好用的Mac清理卸载软件推荐](https://www.uedbox.com/post/119673/ "好用的Mac清理卸载软件推荐")

[![肌理解剖师：中年人的小确幸](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

肌理解剖师：中年人的小确幸](https://www.uedbox.com/post/119356/ "肌理解剖师：中年人的小确幸")

[![🔥 最新免费域名资源大全 | 永久免费域名获取](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

🔥 最新免费域名资源大全 | 永久免费域名获取](https://www.uedbox.com/post/119352/ "🔥 最新免费域名资源大全 | 永久免费域名获取")

[![Cursor agent ask manual区别](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Cursor agent ask manual区别](https://www.uedbox.com/post/119346/ "Cursor agent ask manual区别")

[![让一个 Git 项目丢弃之前的提交历史，只保留当前版本并将其作为最新版](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

让一个 Git 项目丢弃之前的提交历史，只保留当前版本并将其作为最新版](https://www.uedbox.com/post/119343/ "让一个 Git 项目丢弃之前的提交历史，只保留当前版本并将其作为最新版")

* [...