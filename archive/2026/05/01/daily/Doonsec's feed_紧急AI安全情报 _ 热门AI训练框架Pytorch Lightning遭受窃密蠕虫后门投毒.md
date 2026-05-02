---
title: 紧急AI安全情报 | 热门AI训练框架Pytorch Lightning遭受窃密蠕虫后门投毒
url: https://mp.weixin.qq.com/s/fmRDeJOKIEtSOc88T922PA
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:55:41.613681
---

# 紧急AI安全情报 | 热门AI训练框架Pytorch Lightning遭受窃密蠕虫后门投毒

![cover_image](http://mmecoa.qpic.cn/mmecoa_jpg/cC2m1em2riagGjVG9IE1JicbcBndvDGeMFnnmYNicfwPHrWVvVkibibVG3Z8R9AF8njoNTHSp4Le4mCZSmdkzTSgJVOAgptMYRJHGck0H0ggbJWQ/0?wx_fmt=jpeg)

# 紧急AI安全情报 | 热门AI训练框架Pytorch Lightning遭受窃密蠕虫后门投毒

原创

悬镜安全情报中心
悬镜安全情报中心

悬镜安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmecoa.qpic.cn/mmecoa_gif/cC2m1em2riag8RW1Aia4qAcib8nnq9DLjjDiccGdEQ5SyJeSDtqaUia9F1FYA1z5SHKcOBSO8RrUmXg7wHTrWw5zHdoYtRia1LwJLOw5DH9gtamak/640?wx_fmt=gif&from=appmsg)

**AI风险情报概述**

Summary

北京时间4月30日，悬镜AI安全情报中心在Pypi官方仓库中监测到热门AI训练框架Pytorch Lightning 开发者凭证被盗导致攻击者连续发布2个被植入[Shai-Hulud 窃密蠕虫变种](https://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647797236&idx=1&sn=0c56db1e3e8a808f8bf288185d4731d1&scene=21#wechat_redirect)的投毒版本（lightning 2.6.2 及 2.6.3）。这是继[模型网关LiteLLM](https://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647798867&idx=1&sn=d51e8b89a95e1c12d7c4db220befd443&scene=21#wechat_redirect)、[AI推理框架 Xinference](https://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647799026&idx=1&sn=1729fca9f605b1ead40156146881a6cd&scene=21#wechat_redirect) 遭受供应链投毒之后再一起热门AI数字供应链投毒事件。lightning 是基于 pytorch 框架的封装库，提供开箱即用的AI训练组件和功能，lightning 框架库在Pypi官方仓库月下载量近800万次，历史总下载量超9600万次。

![](https://mmecoa.qpic.cn/mmecoa_png/cC2m1em2riahf5qteWqibuKZWwEosMaibsckic7d1j5YaNT5vRCHNnAOWrObxR8d6L9uFTlpjt6PKtesibjKbcicGnPV5wuiaJ2biaMOlSRaQboibEAQ/640?wx_fmt=png&from=appmsg)

lightning Pypi官方仓库下载量统计

此次遭受投毒的是Pypi仓库的 lightning 而非下载量更庞大的pytorch-lightning 库，开发者一旦加载存在投毒代码的lightning python库（import  lightning）即触发恶意代码攻击。该恶意样本具备多维度敏感数据窃取能力，可批量枚举并窃取受害者系统中的各类会话令牌、账号凭证、本地环境变量及云服务密钥；同时会使用窃取的Github Token进一步滥用 GitHub API 接口，劫持受害者有效身份凭据，将窃密数据主动外发并提交至特定代码仓库；此外还会横向侵染开发者本地环境中的 NPM 包 Tar包，实现供应链层面的持久扩散与跨供应链生态的二次传播。

|  |  |  |
| --- | --- | --- |
| 组件名 | 投毒版本 | 发布时间 |
| lightning | 2.6.3; 2.6.3 | 2026.04.30 20:45 |

此次投毒攻击从北京时间4月30号晚上8点45分开始，在5月1号凌晨1点左右Pytorch Lightning官方将Pypi仓库上的lightning投毒版本（2.6.2、2.6.3）移除并回滚到安全版本（2.6.1），整个攻击持续4个半小时左右。在此期间存在更新或安装 Python lightning 框架的个人开发者与企业应重点排查自身系统是否已被感染入侵。

针对此次AI供应链投毒事件，悬镜安全已于第一时间将投毒相关技术细节向供应链情报订阅用户推送预警。

**供应链投毒分析**

Poisoning Analysis

1

**窃密蠕虫后门植入**

此次针对 lightning 框架的代码投毒首先通过在框架入口 \_\_init\_\_.py 文件中植入恶意代码，导入lightning库后立即启动后台线程加载第一阶段payload代码 \_runtime/start.py ，第一阶段 payload 实际为 JS 蠕虫后门加载器，首先检测目标系统环境并下载安装对应版本的JS Bun 运行时环境，接着调用bun执行近 11MB大小的高度混淆的Shai-Hulud窃密蠕虫JS 后门文件 \_runtime/route\_runtime.js 。

以2.6.3版本为例，\_\_init\_\_.py 文件中中恶意代码如下所示：

![](https://mmecoa.qpic.cn/mmecoa_png/cC2m1em2riaiaPBRPVoEicdq7AxqbmLI9FRvoTvWulcZcSZMlm5kiaUdogMYQOzSW31eRHJ0LA9HPyFOxPv7rUxsxCEZhBwwazMp4Fvb41Kghz4/640?wx_fmt=png&from=appmsg)

\_\_init\_\_.py恶意代码

\_runtime/start.py 后门加载器代码如下所示，其主要功能是先检测目标系统环境，如下所示：

![](https://mmecoa.qpic.cn/mmecoa_png/cC2m1em2riahZaJnIGiaJZyM6dnvicoHicSs7gwEnDSR3j7tspHZghkU4xsYBl61ib9eCJ9MjuiayYBmU5XyzH7ibD7ibw2qlVd1qY8ayoCkticf8qmg/640?wx_fmt=png&from=appmsg)

加载器start.py检测系统环境

加载器接着下载安装对应版本的JS Bun 运行时环境，并调用bun执行近 11MB大小的Shai-Hulud 窃密蠕虫后门文件\_runtime/route\_runtime.js ，蠕虫后门代码被高度混淆，如下图所示：

![](https://mmecoa.qpic.cn/sz_mmecoa_png/cC2m1em2riaiasQPzXuvqQxLkONAu8CEHLeZsRic4XpCDkc6os2vfkwT0libnJatibibU5UstKv0atMQLJAK3fjwJib3UiaR7wTpI4ZKDGqP6kibfoI4/640?wx_fmt=png&from=appmsg)

蠕虫加载器下载bun环境并执行js后门

![](https://mmecoa.qpic.cn/mmecoa_png/cC2m1em2riahOSwNgpv2tbRrpM3Q9dfKdbvicDr3opjM63H0weoDU5CHOQSpuhx4hWsMCDaHiblLxgHia1XNFWUyGnos2RhZ3DARz9MRX7x8RxU/640?wx_fmt=png&from=appmsg)

蠕虫后门高度混淆代码

Shai-Hulud 窃密蠕虫后门 route\_runtime.js 主要功能包括：

* 目标系统全域敏感信息采集
* 双通道窃密数据加密外传
* GitHub 仓库代码及配置文件投毒
* NPM 生态蠕虫感染链式传播

2

**敏感信息遍历采集**

Shai-Hulud 窃密蠕虫后门重点采集以下几类敏感数据：

* 开发配置：GitHub Token、NPM Token、SSH 密钥、MCP配置等；

* 云环境：AWS / GCP / Azure 凭证；

* 加密货币：涉及包括比特币、莱特币、门罗币、Exodus、Atomic等；

* VPN 环境：涉及NordVPN、ProtonVPN、CyberGhost、Windscribe 和 OpenVPN；

* CI/CD环境：GitHub Actions 密钥、环境变量等；
* 系统信息：本地凭证文件、Shell 历史、环境变量等；

3

**窃密数据外传**

蠕虫后门除了直接将数据加密后通过HTTPS POST 直传回攻击者 C2服务器外，还会利用窃取的Github Token通过GitHub API新建公开仓库，仓库描述中包含“A Mini Shai‑Hulud has Appeared”，所有被盗数据经过RSA-2048加密后推送到这些新建仓库中。截至目前，本轮 Shai‑Hulud 窃密蠕虫已完成 2400+ 的Github仓库窃密推送。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/cC2m1em2riaiau1RkQ0jvzXibicBjDVZWDj5ia99HmtKe2aMcCWKBN7wKIUJ3KqYyd3WELY3ft7UpIAh61uCgicteCAibquYics6WdiaoL0ODxLufuXM/640?wx_fmt=png&from=appmsg)

Github仓库窃密推送情况

![](https://mmecoa.qpic.cn/mmecoa_png/cC2m1em2riahOH3VOO5wrm83SmJaWRpPA6uDXxm5D21ib0AAm4Nj0T9UXnfibSpiaQKVf78UQibnJ8CBoAI5bf0d3EmbibOoqcYkDErBBKETicfjk4/640?wx_fmt=png&from=appmsg)

窃密数据样本

4

**Githu仓库投毒**

蠕虫后门一旦获取到Github Token后会向Github仓库中的 .claude/、.vscode/\*、GitHub Actions 工作流等目标位置植入恶意代码文件及配置文件，设计恶意文件如下所示：

```
.claude/router_runtime.js.claude/settings.json.claude/setup.mjs.vscode/tasks.json.vscode/setup.mjs.github/workflows/format-check.yml
```

5

**NPM生态蠕虫扩散**

蠕虫后门在获取NPM Token 后，会遍历受害者系统本地 NPM 环境下的NPM .tgz包，通过篡改tar包注入 setup.mjs 与 router\_runtime.js 后门文件，并劫持package.json 添加 preinstall 钩子，最后通过自动升补丁版本号并重新发布恶意NPM包。NPM生态开发者安装恶意NPM包即中招，形成闭环蠕虫传播，实现跨NPM生态的横向扩散。

6

**IoC 数据**

此次 Pytorch Lightning 供应链投毒涉及的部分恶意IoC数据如下表所示：

![](https://mmecoa.qpic.cn/mmecoa_jpg/cC2m1em2riahUPv0ksfamPnvTxk22sSv01mqQiaNuqRP6U3C7BhsmuGwq4um6UyJmza0ehmjyaZgBzIxaQ2Afpvoic9jpzXF98PibB3lt6FXte8/640?wx_fmt=jpeg)

**排查方式**

Investigation Method

1. 使用pip show lightning查询是否已经安装存在投毒版本（2.6.2;2.6.3），如果已安装请立即使用 pip install lightning==2.6.1 回滚到安全版本；
2. 更换所有暴露的私钥、API Token、开发环境凭据（包括 Git、SSH、Kubernetes等），并对云环境各类密钥token 全部轮换（AWS / GCP / Azure 云密钥等）；
3. Git仓库排查，查找描述含 "A Mini Shai Hulud has Appeared" 的异常仓库，审计仓库 .claude/、.vscode/、GitHub Actions 工作流是否存在异常篡改记录，检查是否有 claude@users.noreply.github.com 发起的异常提交；
4. 检测本地所有 NPM .tgz 包文件，重点排查package.json文件中异常新增的 preinstall和postinstall脚本；
5. 使用悬镜开源工具 OpenSCA-cli 将受影响的组件包按如下示例保存为db.json文件，并在opensca配置文件中指定db.json文件路径后，直接执行扫描命令（opensca-cli -path ${project\_path}），即可快速获知您的项目是否受到投毒包影响。

```
[     {         "product": "lightning",         "version": "[2.6.2, 2.6.3]",         "language": "Python",         "id": "XMIRROR-MAL45-D57F7E88",         "description": "热门AI训练框架 lightning 遭受窃密蠕虫后门投毒",         "release_date": "2026-04-30"     }]
```

6. 恶意IoC快速排查脚本

```
#!/bin/bash# 功能：检查是否安装 lighting 2.6.2 / 2.6.3 恶意版本# 用法：./check_lighting_ioc.sh# 定义需要拦截的版本MALICIOUS_VERSIONS=("2.6.2" "2.6.3")# 查询已安装的 lightning 版本（兼容 pip / pip3）INSTALLED=$(pip3 show lightning 2>/dev/null | grep ^Version: | awk '{print $2}')if [ -z "$INSTALLED" ]; then    INSTALLED=$(pip show lightning 2>/dev/null | grep ^Version: | awk '{print $2}')fi# 未安装则直接退出if [ -z "$INSTALLED" ]; then    echo "lightning 未安装"    exit 0fi# 匹配恶意版本for v in "${MALICIOUS_VERSIONS[@]}"; do    if [ "$INSTALLED" = "$v" ]; then        echo -e "\033[31mCompromised!\033[0m"        echo "已安装恶意版本 lightning $INSTALLED"        exit 1    fidone# 安全版本echo "lightning 版本安全：$INSTALLED"
```

```
#!/bin/bash# 功能：递归扫描指定目录，计算文件MD5，匹配恶意IOC，命中则告警# 用法：sudo ./check_lightning_md5_ioc.sh 目标扫描目录 (如 /tmp /root /home)# 定义恶意MD5 IOC列表MALICIOUS_MD5=("7382555752a3598d43653afb08e316b7""40d0f21b64ec8fb3a7a1959897252e09""d13a51964d8fe90b015e03d66cbbc4da")# 检查是否传入目录参数if [ $# -ne 1 ]; then    echo "用法：$0 <需要扫描的目录>"    echo "示例：$0 /tmp"    exit 1fiSCAN_DIR="$1"# 检查目录是否存在if [ ! -d "$SCAN_DIR" ]; then    echo "错误：目录 $SCAN_DIR 不存在"    exit 1fiecho "============================================="echo "  开始扫描目录：$SCAN_DIR"echo "  递归扫描所有文件，匹配恶意MD5..."echo "============================================="echo# 递归遍历文件 + 计算MD5 + 匹配IOCfind "$SCAN_DIR" -type f | while read -r file; do    # 计算文件MD5    current_md5=$(md5sum "$file" 2>/dev/null | awk '{print $1}')    # 跳过无法读取的文件    if [ -z "$current_md5" ]; then        continue    fi    # 匹配恶意MD5    for malicious in "${MALICIOUS_MD5[@]}"; do        if [ "$current_md5" == "$malicious" ]; then            echo -e "\033[31m[!] Compromised! 发现恶意文件：\033[0m"            echo "文件路径：$file"            echo "匹配MD5：$current_md5"            echo "---------------------------------------------"        fi    donedoneecho -e "\n扫描完成！"
```

情报驱动，以AI治理AI！悬镜安全新一代AI原生安全治理技术[“问境AIST”AI原生安全测试平台](https://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647798623&idx=1&sn=6a34afc9df56d9ad01bc1e1683eb9634&scene=21#wechat_redirect)和[“灵境AIDR”智能体安全卫士](https://mp.weixin...