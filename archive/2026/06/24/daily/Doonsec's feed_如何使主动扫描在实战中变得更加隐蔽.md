---
title: 如何使主动扫描在实战中变得更加隐蔽
url: https://mp.weixin.qq.com/s/-uTSVaOUAJF5toYjtALHAw
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:05:32.765688
---

# 如何使主动扫描在实战中变得更加隐蔽

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquN2icQWSFTmahial43cDJCCv56eNM16PFuKJBxs1n2QOLR07BpU4ibjrYfSUiaQMH7dE6rXuDnKNHUvplL6MicK83ec9l1UymHfVrAQ/0?wx_fmt=jpeg)

# 如何使主动扫描在实战中变得更加隐蔽

原创

AzumiSaki
AzumiSaki

船山信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

团队大佬小浪曾说过：

在真实授权红队项目或外部暴露面评估中，主动扫描并不是越快、越全、越激进越好。成熟的资产探测流程应当以授权范围为边界，以业务安全为前提，以攻击路径验证为目标，通过分阶段、低影响、可复盘的方式逐步收集目标信息。

这种方式的核心目的不是隐藏扫描行为，而是减少无意义流量、降低业务影响、提高发现质量，并保证每一个主动动作都能解释其测试目的。在真实项目中，红队人员不仅要发现漏洞，还需要证明漏洞如何形成攻击路径、影响哪些业务资产、蓝队是否具备发现与响应能力，以及最终如何推动风险闭环。

在开始前首先确定工具是否齐全

```
subfinder -versiondnsx -versionhttpx -versionnaabu -versionkatana -versionnuclei -versionnmap --versionffuf -V
```

然后先纯被动收集

## Subfinder 被动子域名

```
```
subfinder \-dL scope/目标.txt \-all \-silent \-o raw/结果.txt
```
```

更保守安全一点，不用 `-all`：

```
```
subfinder \-dL scope/目标.txt \-silent \-o raw/结果.txt
```
```

如果配置了 API key，结果会好很多：

```
```
subfinder \-pc ~/.config/subfinder/provider-config.yaml \-dL scope/domains.txt \-all \-silent \-o raw/api配置.txt
```
```

Amass被动模式

```
```
amass enum \-passive \-df scope/目标.txt \-o raw/结果.txt
```
```

过滤 out-of-scope：

```
```

```
```

```
grep -vFf scope/out_of_scope.txt normalized/目标.txt \  > normalized/筛选后结果.txt
```

# 第 1 阶段：低噪音主动验证

目标：只确认哪些资产真实存在、哪些有 Web、哪些有少量常见端口。
不做漏洞扫描，不做大字典，不做全端口。

---

## DNS 解析验证：dnsx

先只查 A 记录：

```
```
dnsx \-l normalized/subdomains_in_scope.txt \-a \-silent \-resp \-rl 20 \-retry 1 \-o dns/dnsx_a.txt
```
```

JSON 输出，方便后续处理：

```
```
dnsx \-l normalized/subdomains_in_scope.txt \-a \-silent \-json \-rl 20 \-retry 1 \-o dns/dnsx_a.jsonl
```
```

提取解析成功的主机：

```
```
jq -r 'select(.a != null) | .host' dns/dnsx扫描结果.jsonl \  | sort -u \  > normalized/结果.txt
```

```

```
```

提取 IP：

```
```
jq -r 'select(.a != null) | .a[]?' dns/dnsx扫描结果.jsonl \  | sort-u \  > normalized/过滤结果.txt
```
```

dnsx 支持`-l`输入、A/AAAA/CNAME等记录查询、`-rl` 速率限制、       `-retry`重试、JSONL输出等参数。

### 一些小方法

```
```
-rl 10~30-retry 1先只查 A/CNAME不要一开始做大规模DNS爆破不要一开始开AXFR/ANY扫所有域
```
```

3.2 HTTP 存活探测：httpx

先只探测首页，不做截图、不跑路径、不探favicon、不开vhost：

```
httpx  -l normalized/目标.txt  -silent  -status-code  -title  -tech-detect  -web-server  -follow-host-redirects  -timeout 5  -retries 1  -rate-limit 20  -json  -o web/结果.jsonl
```

提取活跃URL：

```
jq -r '.url' web/httpx结果.jsonl  |sort -u \ web/过滤结果.txt
```

生成摘要：

```
jq -r '[.url, .status_code, .title, (.tech // [] | join(",")), .webserver] | @tsv' web/httpx_low.jsonl  |sort -u \ report/结果.tsv column -t -s $'\t' report/结果.tsv | less -S
```

httpx官方说明它用于HTTP探测、Web服务配置分析、HTTP响应验证和技术元数据收集；它也支持超时、延迟等优化参数，并提醒某些探测如     -path、-vhost、-screenshot应按特定场景使用，而不是默认全开。

低噪音建议

```
-rate-limit 10~30-timeout 5-retries 1不加 -path不加 -screenshot不加 -vhost不加 -favicon不加 -tls-probe3.3 低噪音端口发现：naabu top ports
```

只扫常见端口：

```
naabu  -l normalized/目标.txt  -top-ports 100  -rate 100  -retries 1  -timeout 1500  -silent  -json  -o ports/结果.jsonl
```

提取开放端口：

```
jq -r '.host + ":" + (.port|tostring)' ports/目标.jsonl  | sort -u \ports/提取结果.txt
```

提取 host：

```
cut -d: -f1 ports/目标.txt  | sort -u \ports/提取结果.txt
```

提取端口列表：

```
cut -d: -f2 ports/目标.txt  | sort -n -u  | paste -sd, - \ports/结果.csv
```

Naabu官方说明它面向多主机/批量端口扫描，并建议根据运行环境调整rate；官方也建议root下运行以获得更好结果。

更保守版本

```
naabu  -l normalized/目标.txt  -top-ports 50  -rate 50  -retries 1  -timeout 2000  -silent  -json  -o ports/结果.jsonl
```

授权 IP 段低噪音Nmap

对scope/ip\_scope.txt只做top 100 TCP：

```
sudo nmap  -sS  -Pn  --top-ports 100  -T2  --max-rate 50  --max-retries 2  -iL scope/ip_scope.txt  -oA nmap/nmap_ip_top100_low
```

Nmap的-T模板从T0到T5，越高越激进；--max-rate用于限制发包速率，例如限制为每秒100包。

低噪音建议

```
-T2 或 T3--top-ports 100--max-rate 30100--max-retries 12不要 -A不要 --script vuln不要 -p-
```

4. 低噪音阶段产出怎么分析

先找高价值入口：

```
jq -r ' select( (.title // "" | test("admin|login|sign in|dashboard|console|portal|sso|vpn|jenkins|gitlab|nexus|harbor|grafana|kibana|swagger|api"; "i")) or ((.tech // []) | tostring | test("Jenkins|GitLab|Grafana|Kibana|Spring|Laravel|Django|WordPress|Drupal|Confluence|Jira"; "i")) ) | [.url, .status_code, .title, (.tech // [] | join(","))] | @tsv' web/httpx_low.jsonl  | sort -u \report/high_value_web_candidates.tsv
```

挑选后续中噪音目标：

```
cut -f1 report/high_value_web_candidates.tsv  | sort -u \web/selected_urls.txt
```

也可以手工补充：

```
nano web/selected_urls.txt
```

第 2 阶段：中噪音枚举

中噪音不是“全量轰炸”，而是对低噪音阶段筛出的目标做更深入确认。

建议只对这些目标进入中噪音：

```
dev / test / staging / uatadmin / dashboard / consoleapi / swagger / graphqljenkins / gitlab / nexus / harborvpn / sso / portal返回 401 / 403 的管理入口非标准端口 Web 服务低噪音阶段命中敏感技术栈的目标
```

5.1 中噪音 HTTP 探测：httpx 加路径探测

准备小路径字典：

```
cat > web/paths_small.txt << 'EOF'/adminloginsignindashboardconsoleapiapi/v1api/v2swaggerswagger-uiswagger-ui.htmlopenapi.jsonv3/api-docsgraphqlgraphiqlactuatoractuator/healthhealthmetricsdebugconfig.env.git/HEADbackupbackupsuploadsfilesrobots.txtsitemap.xmlserver-statusEOF
```

对筛选目标做路径探测：

```
httpx  -l web/selected_urls.txt  -path web/paths_small.txt  -status-code  -title  -tech-detect  -follow-host-redirects  -timeout 6  -retries 1  -rate-limit 10  -json  -o web/httpx_paths_small.jsonl
```

提取有价值响应：

```
jq -r ' select(.status_code == 200 or .status_code == 204 or .status_code == 301 or .status_code == 302 or .status_code == 401 or .status_code == 403) | [.url, .status_code, .title] | @tsv' web/httpx_paths_small.jsonl  | sort -u \report/httpx_paths_interesting.tsv5.2 中噪音端口：naabu top 1000
```

只对低噪音阶段确认过的活跃host做top 1000：

```
naabu  -l normalized/resolved_hosts.txt  -top-ports 1000  -rate 200  -retries 1  -timeout 1500  -silent  -json  -o ports/naabu_top1000.jsonl
```

提取结果：

```
jq -r '.host + ":" + (.port|tostring)' ports/naabu_top1000.jsonl  | sort -u \ports/open_hostports_top1000.txt
```

按端口看服务：

```
awk -F: '{print $2}' ports/open_hostports_top1000.txt  | sort -n  | uniq -c  | sort -nr \report/port_frequency_top1000.txtcat report/port_frequency_top1000.txt
```

5.3 Nmap 服务识别：只扫已开放端口

生成 Nmap 输入：

```
cut -d: -f1 ports/open_hostports_top1000.txt  | sort -u \nmap/hosts_for_service_detect.txtcut -d: -f2 ports/open_hostports_top1000.txt  | sort -n -u  | paste -sd, - \nmap/ports_for_service_detect.csvPORTS=$(cat nmap/ports_for_service_detect.csv)
```

轻量服务识别：

```
sudo nmap  -sV  --version-light  -Pn  -p "$PORTS"  -iL nmap/hosts_for_service_detect.txt  -T2  --max-rate 50  --max-retries 2  -oA nmap/service_detect_light
```

稍微深入一点，但仍然不要对全范围跑：

```
sudo nmap  -sV  -sC  -Pn  -p "$PORTS"  -iL nmap/hosts_for_service_detect.txt  -T2  --max-rate 50  --max-retries 2  -oA nmap/service_detect_default_scripts
```

注意：-sC 是默认脚本，不等于 --script vuln。真实资产里不要一开始全量跑 --script vuln。

5.4 Web 爬取：Katana 浅层爬

先深度1：

```
katana  -list web/selected_urls.txt  -d 1  -jc  -kf robotstxt,sitemapxml  -c 3  -p 3  -rl 5  -timeout 6  -retry 1  -jsonl  -silent  -o web/katana_d1.jsonl
```

如果结果稳定，再深度2：

```
katana  -list web/selected_urls.txt  -d 2  -jc  -kf robotstxt,sitemapxml  -c 5  -p 3  -rl 10  -timeout 6  -retry 1  -jsonl  -silent  -o web/katana_d2.jsonl
```

Katana支持-d 控制爬取深度、-jc 开启JS端点解析、-kf爬取known files、-c/-p/-rl控制并发和速率。

提取URL：

```
jq -r '.request.endpoint // .url // empty' web/katana_d*.jsonl  | sort -u \web/crawled_urls.txt
```

筛选高价值端点：

```
grep -Ei 'api|admin|login|auth|token|upload|download|export|debug|swagger|graphql|config|backup|actuator|metrics|internal|private'  web/crawled_urls.txt  | sort -u \report/interesting_crawled_urls.txt
```

5.5 ffuf小字典目录枚举

ffuf适合目录、参数、虚拟主机等fuzz；官方Wiki说明它支持-o输出文件、-of json输出JSON、-json输出jsonlines。

准备中小字典：

```
cat > ffuf/dirs_medium.txt << 'EOF'adminadministratorloginsignindashboardconsolemanagemanagerapiapi/v1api/v2swaggerswagger-uiswagger-ui.htmlopenapi.jsonv3/api-docsgraphqlgraphiqlactuatoractuator/healthactuator/envhealthmetricsdebugconfigconfiguration.env.git.git/HEADbackupbackupsbakoldtmptestdevstaginguploadsuploadfilesdownloadexportreportsserver-statusrobots.txtsitemap.xmlEOF
```

单目标跑法：

```
ffuf  -w ffuf/dirs_medium.txt  -u https://target.example.com/FUZZ -mc 200,204,301,302,307,308,401,403  -t 5  -rate 10  -timeout 6  -o ffuf/target_dirs.json  -of json
```...