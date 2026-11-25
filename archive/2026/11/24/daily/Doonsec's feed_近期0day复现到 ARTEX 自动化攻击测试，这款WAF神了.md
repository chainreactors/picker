---
title: 近期0day复现到 ARTEX 自动化攻击测试，这款WAF神了
url: https://mp.weixin.qq.com/s/kPAkeGK7cR_7v9_1ZLqhvQ
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:46:06.786316
---

# 近期0day复现到 ARTEX 自动化攻击测试，这款WAF神了

# 近期0day复现到 ARTEX 自动化攻击测试，这款WAF神了

原创

仙草里没有草噜丶
仙草里没有草噜丶

泷羽Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

现在部署一个网站，光靠服务器本身的安全配置其实还不够。尤其是一些对外开放的 Web 服务，一旦存在 SQL 注入、未授权访问或者其他应用层漏洞，即使服务器配置得再严格，也可能成为攻击者的入口。

WAF（Web 应用防火墙）就是解决这类问题的重要防护手段之一。它部署在 Web 流量入口，对访问请求进行检测和过滤，在攻击请求到达后端应用之前，尽可能将其拦截下来。

不过，WAF 到底能不能拦住漏洞利用请求，不能只看面板上有没有开启防护规则。真正有效的测试，还是要准备一个存在漏洞的环境，使用对应的 PoC 或攻击请求进行验证，再观察 WAF 的拦截结果和日志记录。

这次我们就围绕雷池社区版（SafeLine WAF）做一次实际测试。

整个过程分为几个部分：先在服务器上部署雷池，随后搭建近期公开的漏洞靶场，分别测试 CVE-2026-132165、CVE-2026-77378 和 Git LFS CVE-2026-105802。最后再使用最近比较受关注的 ARTEX 进行自动化攻击测试，看看面对真实的 SQL 注入请求，雷池能否及时识别并阻断。

这里不只是单纯安装一个 WAF，而是尽量把漏洞环境、攻击请求、反向代理和防护日志串起来。这样测试完之后，我们能够看到攻击请求是如何进入防护系统的，又是在哪个环节被拦截的。

## 一、雷池 WAF 安装部署

在搭建环境之前，先说一下服务器的网络问题。

雷池安装过程中需要下载相关组件和镜像，如果服务器访问外网不稳定，很容易在安装或者拉取镜像时卡住。因此，环境搭建时建议优先使用网络条件比较好的国外服务器；使用国内服务器的话，建议提前配置好网络访问环境。

![image-20261120234322165](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfMdvJ8rvF2T7MU4EuRm9j2R8zAMdDQvsNhTRhn3vEd03qBOB8P41HA4TSmT6Xp57XCfhia2qd4KTSvwncv7jzEG3icAnYoBf5UnQ/640?wx_fmt=other&from=appmsg)

### 1. 更新系统

准备好一台 Linux 服务器，先更新系统软件包：

```
bashapt update -y && apt upgrade
```

### 2. 安装雷池

系统更新完成后，执行雷池社区版的安装命令：

```
bashbash -c "$(curl -fsSLk https://waf-ce.chaitin.cn/release/latest/manager.sh)"
```

等待安装程序执行即可。如果安装过程中没有正常完成，可以按 `CTRL+C` 结束当前安装程序，再重新执行一次安装命令。

![image-20261121000053868](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfN4b7Vib15cI1ianGKZlzEib1q3mLTZic8ovpTnKubGNcSVXzMLVsCH5zn9sRMkpFuzLreLqdyepaY8hVEnlaKSkdEjG1FHfZicmSlE/640?wx_fmt=other&from=appmsg)

安装完成后，终端会显示对应的登录信息。

此时访问服务器公网 IP 的 9443 端口，输入终端给出的账号和密码，就可以进入雷池管理界面。

![image-20261121002920679](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfMBIfohqZOa75V95FXm2z7kHJ1ESyBsSwT2UNnyIPOLjqObykiciakqjnrahmhKibX5nJW1tG24Z7aQuzHJFRk1BiawyIXrZR3vj4U/640?wx_fmt=other&from=appmsg)

成功登录后就能看到雷池的管理首页，至此基础部署已经完成。

![image-20261121003014867](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfNCYbYEcRCGZCMaa6aclH2us929ZGWbiboBMbbhcYpLvTaOBNDic6jribUKeWdaVic3xgZHmicfRvjh78lOjseBibsU07gibwYAr9ksIE/640?wx_fmt=other&from=appmsg)

接下来开始搭建漏洞环境，把实际的攻击请求接入雷池进行测试。

## 二、近期 0day 漏洞 CVE-2026-132165 复现与防护测试

先来测试 CVE-2026-132165。

这次使用的是 GitHub 上的公开靶场项目，通过 Docker 搭建漏洞环境，再运行项目提供的 PoC 验证漏洞是否存在。完成验证后，将站点接入雷池，通过反向代理重新发起测试，观察防护效果。

### 1. 搭建漏洞靶场

首先克隆项目：

```
bashgit clone https://github.com/abraxas/drupal-install-takeover.git
cd drupal-install-takeover
```

![image-20261121005554796](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfM7x1OOC2s2FicBILr0F0v2qBIHDCxFR6K0KHMxUwJtfI18tBFsjVYrNGPksvl7Ie8ounCKqIsvT8iaj7UJXRY95pgVXkb2WV6fo/640?wx_fmt=other&from=appmsg)

进入项目中的 `lab` 目录，设置 Docker Compose 项目名称，然后启动环境：

```
bashcd lab

export COMPOSE_PROJECT_NAME=cve-2026-132165

docker compose up --build -d
```

正常情况下，Docker 会自动构建所需镜像并启动对应容器。

### 2. 解决 Docker 镜像拉取问题

如果执行构建命令时发现 Docker 无法正常拉取镜像，可以先检查服务器的网络连接情况。

![image-20261121010124031](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfNU4D2UbWSEd9oaodwUV4FJbVP6pkzmG4hcg54XPjMjianuser9V3thaZkXTebhsF9lTH7hsR9bzkLk1fCSOibIMiaxnHmLFX1xdw/640?wx_fmt=other&from=appmsg)

这里通过配置 Docker 镜像加速来解决拉取失败的问题。

先创建 Docker 配置目录，并备份原有配置文件：

```
bashmkdir -p /etc/docker

[ ! -f /etc/docker/daemon.json ] || \
cp -a /etc/docker/daemon.json /etc/docker/daemon.json.bak
```

接下来修改 Docker 的 daemon.json，加入镜像加速地址：

```
pythonpython3 - <<'PY'
import json
from pathlib import Path

p = Path("/etc/docker/daemon.json")

if p.exists():
    config = json.loads(p.read_text())
else:
    config = {}

mirrors = config.get("registry-mirrors", [])
mirror = "https://docker.m.daocloud.io"

if mirror notin mirrors:
    mirrors.insert(0, mirror)

config["registry-mirrors"] = mirrors

p.write_text(json.dumps(config, indent=2) + "\n")
print(p.read_text())
PY
```

配置完成后，重新加载 systemd 并重启 Docker：

```
bashsystemctl daemon-reload
systemctl restart docker
```

重新执行镜像构建操作即可。

![image-20261121010148032](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfNpIiaNId9LtS4hXy42mvusYtoMu91PNlP6PcqtrRTX5CTQLPTLN90kWDE9voloia70S62EUU3IWGJh42BnwfDMnh9icHffHaXqNc/640?wx_fmt=other&from=appmsg)

### 3. 运行 PoC 验证漏洞

靶场启动完成后，运行项目提供的 PoC。

如果输出结果中出现 `SUCCESS`，就说明本次漏洞验证成功。

![image-20261121011018400](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfOMEcFibn6t0IJlhiahr8riastfNwKJdjtSZno8sDEwUPYctWYEmnTOkd1eC0A2JwdibzejWF5YdxzI8JAkCy67VhowZSoAZNicYtg8/640?wx_fmt=other&from=appmsg)

这里有两个字段需要特别留意：

* `takeover=yes`

  ：表示漏洞版本中的测试账户已经被替换，账户接管验证成功。
* `rce=no`

  ：表示本次验证没有执行系统命令，也没有建立反弹 Shell。

这两个结果不能混为一谈。项目作者明确说明，这个靶场验证的是管理员账户接管，并不是完整的远程代码执行（RCE）。

![image-20261121015721175](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfOqltQO3VjBDBvdkhMfqsoSAOHOkHlEcTYNzm5LsnnDFeorxXxB3bJmJ27zsutEqaJ4kGTevSPdIeqfFHGBLAYAH41olWsgic6M/640?wx_fmt=other&from=appmsg)

### 4. 安装 Drupal 站点

接下来需要完成靶场中的站点安装。

![image-20261121020211017](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfPwFUAfcCQTvXBvrnmU5vRtqiaqaUxNzTiakcicicCsr2a9VHzVZAOvicyHzlMKZyVFSHbpgIxduruCbO1guLRwY0Bbj8ibJkCToyn2s/640?wx_fmt=other&from=appmsg)

按照页面提示继续操作，一路点击下一步，完成站点初始化。

![image-20261121020403831](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfMM0VHf4EXltMPkWzfs5ibVbOzpOjWCVcvb4gKanVJicuXAp3Jxk4rs77ETU1PQnMiaptibFkZJ2QFskiaGR7VwCK4apZV4czoV6uU8/640?wx_fmt=other&from=appmsg)

站点安装完成后，接下来需要调整 PoC 中的目标地址，将原来的地址修改为经过反向代理之后使用的域名。

![image-20261121015854634](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfPkkVicuHTsWxvtZVQvJAJeXxgD0NYziatBbSXvib8U84rwjrNNhr17p246COmLx0KZK0QjIe8ib5TD5eBRVK5rXbKicXibRnL9MXq2M/640?wx_fmt=other&from=appmsg)

配置完成后，再次使用 PoC 发起请求。

![image-20261121015929136](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfOcPiczmAKLVaecsTv4fjAAFs0Emovicltet6v3ZcsMiaia7xiaI1ZcGjBABkk8PiaGPJskJ2E4fEM7QqOEpuFocS5TS9N4bJptEfiaT4/640?wx_fmt=other&from=appmsg)

从本次测试结果来看，攻击请求已经被雷池成功拦截。至此，CVE-2026-132165 的靶场搭建、漏洞验证以及 WAF 防护测试就完成了。

## 三、CVE-2026-77378：ListFormatHelper SQL 注入

接下来测试另一个漏洞：CVE-2026-77378。

这个环境主要用于验证 ListFormatHelper 相关的 SQL 注入问题。与前面的 Drupal 靶场不同，这次项目中准备了漏洞版本和修复版本，可以同时启动两个容器进行对照测试。

这样做的好处是，除了验证漏洞版本是否存在问题，还能检查修复版本在相同测试条件下的表现。

### 1. 下载项目

先回到用户主目录，克隆对应的 GitHub 项目：

```
bashcd ~

git clone https://github.com/googlesky/CVE-2026-77378.git

cd CVE-2026-77378
```

![image-20261121123225603](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfOffaiabT1DzF6J4MibfP2HwLzvN2mFz2GxGNKAzMdnib9dRVT9cD0X3c70CUkVgtMT3Gs7DGntQMbOicpPVqEyflPXZHoS4TFt0Uk/640?wx_fmt=other&from=appmsg)

### 2. 创建 Docker 启动脚本

为了方便管理两个版本的漏洞环境，这里创建一个 `run-lab-docker.sh` 脚本。

脚本主要负责三件事情：构建漏洞版本和修复版本镜像、启动两个测试容器，以及运行 PoC 对两个环境进行全量测试。

创建脚本：

```
bashcat > run-lab-docker.sh <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

NET="cve77378lab"
HERE="$(cd "$(dirname "$0")" && pwd)"

build() {
    echo"[+] Building vulnerable helper"
    docker build -f "$HERE/lab/lab.Dockerfile" \
        --target vuln \
        -t cve-2026-77378:vuln \
        "$HERE/lab"

    echo"[+] Building fixed helper"
    docker build -f "$HERE/lab/lab.Dockerfile" \
        --target fixed \
        -t cve-2026-77378:fixed \
        "$HERE/lab"

    echo"[+] Building PoC runner"
    docker build -t cve-2026-77378-poc:local"$HERE/poc"
}

up() {
    docker network inspect "$NET" >/dev/null 2>&1 || \
        docker network create "$NET" >/dev/null

    for side in vuln fixed; do
        docker rm -f "bolt-$side" >/dev/null 2>&1 || true

        docker run -d \
            --name "bolt-$side" \
            --network "$NET" \
            --cpus 2 \
            --memory 1g \
            "cve-2026-77378:$side" >/dev/null

        echo"[+] Started bolt-$side"
    done
}

sweep() {
    mkdir -p "$HERE/evidence"

    for mode in check exploit probe mitigation; do
        for side in vuln fixed; do
            echo
            echo"========== $mode / bolt-$side =========="

            logfile="$HERE/evidence/${mode}-${side}-docker-run.txt"

            if docker run --rm \
                --network "$NET" \
                --cpus 1 \
                --memory 256m \
                cve-2026-77378-poc:local \
                "$mode""--host=bolt-$side" \
                > "$logfile" 2>&1; then
                rc=0
            else
                rc=$?
            fi

            cat"$logfile"
            echo"[+] Exit code: $rc...