---
title: Docker镜像构建还在瞎搞？运维大佬的生产级玩法，直接抄作业
url: https://mp.weixin.qq.com/s/XHfo_jYP8P6gxOmut_zawA
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:29:36.493021
---

# Docker镜像构建还在瞎搞？运维大佬的生产级玩法，直接抄作业

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GYcoKKbcBjNUFyicH73cfgy3zSgNUAbnb85sG9aEbf7ibn4hjj7IFUgpIALQR97Sia2LCMcA6ZMkLqSEeAQxk51ug/0?wx_fmt=jpeg)

# Docker镜像构建还在瞎搞？运维大佬的生产级玩法，直接抄作业

原创

小柳实验室
小柳实验室

小柳实验室

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/GYcoKKbcBjNrl929DxDeBczZLSiayqicia9ZzVPHicPdOljIvIf5VKuFsOBsT0CgH8jDXHn5NaI8lmyGgXa428twzg/640?wx_fmt=gif&from=appmsg)

作为运维工程师，你是不是也遇到过这些糟心事：

本地构建的Docker镜像，一到生产环境就各种报错？用docker commit做的镜像，被安全审计骂到狗血淋头？镜像体积大到离谱，传输一次要等半小时？

别慌！今天就给大家带来**企业级Docker镜像构建的保姆级教程**，从开发调试到生产合规，一步到位，新手也能直接抄作业！

## 先划重点：生产镜像的4个核心原则

咱运维做镜像，可不是随便打包个应用就行，必须围绕这4个目标：

1. 1. **可复现**：别人拿你的配置，能做出一模一样的镜像，杜绝“我这能跑”的玄学问题
2. 2. **可审计**：每一步操作都有记录，安全合规检查直接通关
3. 3. **安全可控**：坚决不用root用户，端口、权限全拿捏住
4. 4. **体积够小**：没用的依赖全删掉，传输部署嗖嗖快

基于这4个原则，**Dockerfile多阶段构建是生产环境的唯一标准答案**！像docker commit、直接导rootfs这种操作，只能临时调试用，敢上生产就是踩雷！

## 实战：5分钟搞定生产级Flask镜像

咱用Python Flask应用举例子，从0到1教你做一个符合企业规范的镜像，看完就能直接用。

### 第一步：准备基础文件，先把坑避开

首先建个项目目录，把需要的文件准备好：

```
mkdir flask-prod-app && cd flask-prod-app
```

#### 1. 写个简单的应用代码（app.py）

注意！生产环境不用写调试入口，全靠WSGI服务器启动：

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "这是生产级Docker镜像！稳得一批！"
```

#### 2. 明确依赖版本（requirements.txt）

版本号一定要锁死，避免自动更新踩坑：

```
flask==2.3.3          # Web框架
gunicorn==21.2.0      # 生产必备的WSGI服务器，比自带的调试服务器稳10倍
```

#### 3. 必加！.dockerignore文件

这个文件能过滤掉没用的东西，避免镜像变大、泄露敏感信息：

```
# 版本控制相关
.git
.gitignore

# 本地开发依赖
__pycache__/
*.pyc
.venv

# 敏感文件
.env
*.log
```

### 第二步：编写Dockerfile，多阶段构建是关键

多阶段构建的好处就是：**构建依赖和运行环境彻底分开**，最终的镜像只留必需品，体积直接砍半！

直接复制下面的代码，注释写得明明白白：

```
# ===== 第一阶段：构建阶段（只装依赖，不进最终镜像） =====
FROM docker.xuanyuan.run/python:3.10-slim AS builder

# 配置国内pip源，下载速度起飞
RUN mkdir -p /root/.pip \
    && echo "[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple" > /root/.pip/pip.conf

WORKDIR /build
COPY requirements.txt .
# 安装依赖到临时目录，--no-cache-dir 避免缓存占空间
RUN pip install --no-cache-dir -r requirements.txt -t ./vendor \
    && rm -rf /root/.cache/pip

# ===== 第二阶段：运行阶段（最终镜像，干干净净） =====
FROM docker.xuanyuan.run/python:3.10-slim

# 1. 配置时区+装必要工具，解决容器时间不对的问题
RUN apt update && apt install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/* \
    && ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo Asia/Shanghai > /etc/timezone \
    # 2. 生产核心操作：创建普通用户，坚决不用root！
    && useradd -m -u 1001 appuser

# 切换到普通用户，后续操作都没root权限
USER appuser

# 3. 复制构建阶段的依赖
WORKDIR /app
COPY --from=builder /build/vendor ./vendor
ENV PYTHONPATH=/app/vendor

# 4. 复制应用代码，指定归属用户，避免权限问题
COPY --chown=appuser:appuser app.py .

# 5. 环境变量+端口声明，支持动态配置
ENV WORKERS=2
EXPOSE 5000

# 6. 生产级启动命令，支持优雅退出
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:5000 --workers ${WORKERS} --graceful-timeout 30 app:app"]
```

### 第三步：构建+验证，两步搞定

#### 1. 构建镜像（注意Tag命名规范，别用latest！）

```
docker build -t flask-prod-app:1.0-prod .
```

Tag格式建议：`镜像名:版本-环境`，比如上面的`1.0-prod`，一看就知道是生产环境的1.0版本。

#### 2. 本地验证，确保没问题

```
# 启动容器
docker run -d -p 5000:5000 --name flask-test flask-prod-app:1.0-prod

# 访问测试，能看到返回内容就对了
curl http://localhost:5000

# 关键验证：是不是普通用户运行？
docker exec -it flask-test whoami
# 输出appuser就对了！

# 测试完清理容器
docker stop flask-test && docker rm flask-test
```

### 第四步：生产部署，用docker-compose更省心

生产环境不能直接docker run，用docker-compose加一堆配置，稳定性拉满！

写个`docker-compose.prod.yml`：

```
version: '3.8'
services:
  flask-app:
    image: flask-prod-app:1.0-prod
    user: 1001  # 和镜像里的用户UID一致，强化权限管控
    ports:
      - "5000:5000"  # 公网部署记得换LB/Ingress，别直接暴露
    restart: always  # 容器挂了自动重启，高可用必备
    mem_limit: 512m   # 限制内存，防止占用太多资源
    cpus: 0.5         # 限制CPU核心
    # 健康检查，自动检测应用状态
    healthcheck:
      test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:5000/')"]
      interval: 30s
      timeout: 10s
      retries: 3
    networks:
      - app-net

networks:
  app-net:
    driver: bridge
```

启动命令：

```
docker-compose -f docker-compose.prod.yml up -d
```

## 那些临时场景的玩法（严禁上生产！）

有些特殊情况，比如本地调试、内网离线部署，咱也得会，但一定要记住：**这些方法只能临时用！**

### 1. docker commit：手动做镜像，仅调试用

比如临时装个Nginx测试环境：

```
# 启动临时容器
docker run -it --name nginx-temp docker.xuanyuan.run/ubuntu:22.04 bash
# 容器内装Nginx
sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list && apt update && apt install -y nginx
# 另开终端提交镜像，一定要标test-only
docker commit nginx-temp nginx-test:only-for-debug
```

### 2. 离线迁移：docker save/load，生产级离线部署用这个

内网服务器没网？用这个方法迁移镜像，完整保留所有配置：

```
# 能联网的机器：导出镜像为tar包
docker save -o flask-prod-app-1.0-prod.tar flask-prod-app:1.0-prod
# 拷贝到内网机器，导入镜像
docker load -i flask-prod-app-1.0-prod.tar
# 然后用docker-compose启动就行
```

## 运维大佬的保命规范：这4条红线别踩！

1. 1. **绝对不能用root用户运行应用**：容器被黑了也不会拿到主机root权限，这是底线！
2. 2. **禁止用docker commit的镜像上生产**：没记录、不可追溯，安全审计直接打回！
3. 3. **端口别直接暴露到公网**：一定要用LB/Ingress转发，加网络策略管控！
4. 4. **镜像Tag别用latest**：版本混乱，出问题都不知道回滚到哪个版本！

## 常见踩坑指南，避坑=涨工资

1. 1. **alpine镜像运行报错**：alpine用的是musl libc，不是glibc，有些软件不兼容。解决方案：换slim镜像，或者手动装glibc。
2. 2. **pip装包编译失败**：缺少gcc、make这些工具。解决方案：构建阶段装，运行阶段删掉。
3. 3. **容器时间不对**：默认是UTC时区。解决方案：Dockerfile里配置上海时区，前面的例子已经写了！

## 最后总结

Docker镜像构建，说复杂也复杂，说简单也简单，核心就记住：

* • 生产环境：**Dockerfile多阶段构建+非root用户+规范Tag**，这三板斧砍下去，啥问题都解决。
* • 临时场景：docker commit、rootfs导入只能救急，千万别上头！

掌握这些方法，你做的镜像不仅能通过安全审计，还能跑得稳、传得快，运维效率直接翻倍！

![](https://mmbiz.qpic.cn/mmbiz_gif/GYcoKKbcBjPM88logbaFhsxVIxHGfN8sCHicaficYa68jS5OPPbibIUFk0oecCnia6xwiae0OX8gr1hGBSd3ca8RbXQ/640?wx_fmt=gif&from=appmsg)

#### 📬 关注我

#### 推荐阅读

#### [Redis主从复制深度解析：数据高可用与负载均衡的核心方案](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484720&idx=1&sn=d8f5606ddae7446b218ba78b20192e91&scene=21#wechat_redirect)

#### [运维必备｜Zabbix 从 0 到 1 搭建企业级监控，告警自动喊你处理！](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484738&idx=1&sn=dfca8b99647de349ea542f006a0447e6&scene=21#wechat_redirect)

#### [15分钟搞定业务宕机！运维必备排查指南（附实操命令）](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484707&idx=1&sn=a2aeb0d301f8a1ea7fabc6df7b9fcc37&scene=21#wechat_redirect)

#### [SCP 与 rsync 到底怎么选？运维老鸟的文件传输避坑指南](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484660&idx=1&sn=31cfde90b5d344f43aee94da3e741938&scene=21#wechat_redirect)

#### [效率拉满！Docker+Nginx 一站式部署 Java（JAR/WAR 通用），运维再也不加班](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484652&idx=1&sn=c2f21df196ddf1449e0228d1644af976&scene=21#wechat_redirect)

#### [别再搞混Nginx和OpenResty！90%运维都踩过的坑，一文讲透核心差异](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484642&idx=1&sn=9d801f6e32d1d48ca178f50b6f7a2f65&scene=21#wechat_redirect)

#### [开发运维必备神器！HexHub 一站式搞定数据库、SSH、Docker 所有需求](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484642&idx=2&sn=e294ce7ce735d6358ddfe44dd56de1cb&scene=21#wechat_redirect)

#### [网络排查神器！掌握 tcpdump，让网络故障无处遁形](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484599&idx=1&sn=ec867d8dcaba4dfce556d3e6b7105b1a&scene=21#wechat_redirect)

#### [MySQL 与 PostgreSQL：两个老对手的技术对决与选型指南](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484564&idx=1&sn=813b062f9a0b64ea53e4d55a5bef164f&scene=21#wechat_redirect)

#### [高性能存储刚需党必看！Docker 部署 RustFS，效率直接拉满](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484488&idx=1&sn=a558fdf75c460836f091c7fc294fac15&scene=21#wechat_redirect)

#### [别再用第三方短链了！这个开源神器3分钟搭建专属短网址平台](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484520&idx=1&sn=d9f808127d673d6cb5ebb6a075ad254c&scene=21#wechat_redirect)

#### [Linux服务器重启后服务不自启？systemd实战指南 + 混沌演练验证](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484524&idx=1&sn=bb6f6bcff27fa7290592f9eae4ef72bc&scene=21#wechat_redirect)

#### [502 Bad Gateway 不是终点：一次生产事故背后的全链路复盘](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484459&idx=1&sn=04fbd75534f6474ebe2643baa3f081a7&scene=21#wechat_redirect)

#### [备份做了，但能恢复吗？MySQL 数据恢复终极指南来了！](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484442&idx=1&sn=d6256ad2948324bc0361b8651da81dd7&scene=21#wechat_redirect)

#### [Firewalld 实战全攻略：从入门到精通，搭配 ipset 打造高效防护体系！](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484423&idx=1&sn=df5ed942097c767c8c93bc5f1750e734&s...