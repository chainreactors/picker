---
title: 你与顶尖挖洞大神的距离，只差这份信息收集“降维打击”指南
url: https://mp.weixin.qq.com/s/VShhEUo7maojp8vD1b8epA
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:24:07.047414
---

# 你与顶尖挖洞大神的距离，只差这份信息收集“降维打击”指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sSbvsVNNPovgOVUbZ4oqaibCTpib2nb5yuTEamFIM5TRsFBITBlicnyWO9rv6KnIuS7rn5xRnf88EESLK1e2YG33w/0?wx_fmt=jpeg)

# 你与顶尖挖洞大神的距离，只差这份信息收集“降维打击”指南

原创

逍遥
逍遥

逍遥子讲安全

![]()

在小说阅读器中沉浸阅读

> 在SRC的世界里，信息收集的差距，决定了你是“辛苦挖矿”还是“精准淘金”

我盯着屏幕上的数字——连续三个月，我在某头部互联网公司SRC榜单上的排名稳居前三。这并非偶然，而是一套系统性信息收集方法论带来的必然结果。今天，我将毫无保留地分享这套让我的挖洞效率提升5倍、漏洞质量提高3倍的工业级信息收集体系。

## 一、残酷现实：为什么你的信息收集总是无效？

让我先问几个刺痛人心的问题：

* **你是不是还在用那些人人都会的工具**，扫着人人都会扫的目标？
* **你的“资产列表”是不是永远那几个子域名**，换个参数都怕出问题？
* **你有没有算过自己的时间投资回报率**——花了多少小时，找到几个有效漏洞？

如果你的答案是肯定的，那么恭喜，你正处在99%的研究者所处的“红海竞争区”。在这里，每个目标都有无数双眼睛盯着，每个漏洞都有无数双手抢着。而我将带你进入的，是那1%的“蓝海无人区”。

## 二、认知跃迁：从“工具使用者”到“情报架构师”

大多数人把信息收集等同于“运行几个扫描工具”。而顶尖研究者构建的是 **“持续运转的情报生产流水线”** 。两者的区别如下：

| 维度 | 传统收集 | 工业级收集 |
| --- | --- | --- |
| **视角** | 单次任务 | 持续监控 |
| **范围** | 已知资产 | 全维度攻击面 |
| **深度** | 表面扫描 | 业务上下文理解 |
| **输出** | 资产列表 | 可行动报与攻击路径 |
| **更新** | 手动触发 | 实时自动化 |

转变思维后，我建立了一套“四维收集模型”，接下来将逐层拆解。

## 三、第一维：宽度扩展——把攻击面放大100倍

### 3.1 证书透明度：发现别人看不到的资产

当大家还在爆破子域名时，我通过证书透明度日志发现了23个未在DNS记录中的内部系统。方法很简单，但99%的人不会坚持做：

python

```
# 实时证书监控脚本import jsonfrom websocket import create_connection
def monitor_certificates(company_keywords):    ws = create_connection("wss://certstream.calidog.io/")
    try:        while True:            try:                message = json.loads(ws.recv())                if message['message_type'] == "heartbeat":                    continue
                domains = message['data']['leaf_cert']['all_domains']                cert_info = message['data']['leaf_cert']['subject']
                # 多关键词匹配，不只是域名                for keyword in company_keywords:                    if (any(keyword in domain for domain in domains) or                         keyword.lower() in str(cert_info).lower()):
                        print(f"[+] 发现新证书: {domains}")                        print(f"    组织信息: {cert_info}")                        print(f"    有效期: {message['data']['leaf_cert']['not_before']} 至 {message['data']['leaf_cert']['not_after']}")
                        # 自动触发进一步侦察                        launch_deep_scan(domains)
            except Exception as e:                print(f"[-] 处理错误: {e}")                continue
    except KeyboardInterrupt:        ws.close()
```

关键洞察：证书不仅包含域名，还暴露组织架构、部门信息，甚至泄露合并收购中的未整合资产。

### 3.2 搜索引擎的“高级玩法”

别再只会用`site:target.com`了，这些语法组合才是宝藏：

bash

```
# FOFA高级搜索组合# 1. 通过证书发现关联资产cert="Target Corp" && country="CN"
# 2. 通过特定技术栈缩小范围app="Spring Boot" && icon_hash="116323821"
# 3. 通过历史漏洞反查title="Apache Struts2" && after="2024-01-01"
# 4. 通过业务特征定位body="在线支付" && header="API-Version"
# Shodan的企业级用法# 查找所有使用特定中间件的资产product:"nginx" org:"Target Company"
# 发现暴露的管理接口"Admin Panel" port:"8080,8443,9000"
```

```

```

### 3.3 GitHub情报挖掘：代码泄露的“富矿”

去年，我通过GitHub监控发现了某公司测试环境的数据库凭证，从而找到了7个有效漏洞。这是我的监控策略：

python

```
# FOFA高级搜索组合# 1. 通过证书发现关联资产cert="Target Corp" && country="CN"
# 2. 通过特定技术栈缩小范围app="Spring Boot" && icon_hash="116323821"
# 3. 通过历史漏洞反查title="Apache Struts2" && after="2024-01-01"
# 4. 通过业务特征定位body="在线支付" && header="API-Version"
# Shodan的企业级用法# 查找所有使用特定中间件的资产product:"nginx" org:"Target Company"
# 发现暴露的管理接口"Admin Panel" port:"8080,8443,9000"
```

四、第二维：深度挖掘——从资产到业务理解

### 4.1 技术栈指纹的“超精细化”识别

我的指纹库有327个技术栈识别模式，但这只是基础。真正的价值在于理解技术栈的**版本差异**和**配置特征**：

yaml

```
# 技术栈深度指纹示例Spring_Boot_Detection:  indicators:    headers:      - "X-Application-Context"      - "Set-Cookie: JSESSIONID"    endpoints:      - "/actuator/health"      - "/actuator/env"      - "/actuator/metrics"    error_patterns:      - "Whitelabel Error Page"      - "This application has no explicit mapping"  version_detection:    method_1: "检查 /actuator/info 的 build.version"    method_2: "分析 Spring Boot 特定的错误页面格式"    method_3: "通过依赖库版本反推"
  # 配置特征提取  config_patterns:    database: "spring.datasource"    security: "spring.security"    cache: "spring.cache"    external_services: "cloud.aws"
```

4.2 业务逻辑的“上帝视角”映射

我开发了一个业务逻辑自动分析器，它通过模拟用户行为来理解系统：

Python

```
class BusinessLogicMapper:    def map_application_flow(self, start_url):        """自动映射应用的用户流程"""
        # 1. 识别关键业务页面        key_pages = self.identify_key_pages(start_url)
        # 2. 分析页面功能        page_analyses = {}        for page in key_pages:            analysis = {                'function': self.determine_page_function(page),                'inputs': self.extract_input_fields(page),                'actions': self.extract_possible_actions(page),                'transitions': self.find_page_transitions(page),                'sensitive_data': self.identify_sensitive_data_elements(page)            }            page_analyses[page] = analysis
        # 3. 构建业务流程图        business_flow = self.build_flow_chart(page_analyses)
        # 4. 识别特权功能        privileged_functions = self.find_privileged_functions(business_flow)
        return {            'business_flow': business_flow,            'privileged_functions': privileged_functions,            'attack_surface': self.calculate_attack_surface(business_flow)        }
    def determine_page_function(self, page):        """智能判断页面功能"""        function_indicators = {            '用户注册': ['注册', 'signup', 'register', 'create account'],            '登录认证': ['登录', 'signin', 'login', 'authenticate'],            '支付交易': ['支付', '付款', 'checkout', 'purchase', 'order'],            '密码管理': ['密码', 'password', '重置密码', 'forgot password'],            '管理功能': ['管理', 'admin', '控制台', 'dashboard', '设置']        }
        page_content = self.fetch_page_content(page)        for function, indicators in function_indicators.items():            if any(indicator in page_content for indicator in indicators):                return function
        return '其他功能'
```

4.3 API的“全自动”发现与文档重建

现代应用大量依赖API，但文档往往不全。我的解决方案是：

javascript

```
// API自动发现与测试框架class APIDiscoverySuite {    constructor(baseURL) {        this.baseURL = baseURL;        this.discoveredEndpoints = new Set();        this.apiSpec = {            endpoints: {},            authentication: {},            dataModels: {}        };    }
    async discover() {        // 1. 从JavaScript文件中提取API端点        const jsFiles = await this.extractJavaScriptFiles();        const endpointsFromJS = this.parseEndpointsFromJavaScript(jsFiles);
        // 2. 从网络请求中捕获API调用        const capturedRequests = await this.captureNetworkTraffic();        const endpointsFromTraffic = this.extractEndpointsFromRequests(capturedRequests);
        // 3. 常见API路径爆破        const commonPaths = await this.bruteForceCommonAPIPaths();
        // 合并所有发现的端点        const allEndpoints = new Set([            ...endpointsFromJS,            ...endpointsFromTraffic,            ...commonPaths        ]);
        // 4. 分析每个端点        for (const endpoint of allEndpoints) {            const analysis = await this.analyzeEndpoint(endpoint);            this.apiSpec.endpoints[endpoint] = analysis;
            // 自动识别认证机制            if (analysis.requiresAuth) {                this.apiSpec.authentication[endpoint] = analysis.authType;            }
            // 推断数据模型            if (analysis.sampleResponse) {                const dataModel = this.inferDataModel(analysis.sampleResponse);                this.apiSpec.dataModels[endpoint] = dataModel;            }        }
        return this.apiSpec;    }
    async analyzeEndpoint(endpoint) {        const analysis = {            methods: [],            parameters: {},            requiresAuth: false,            rateLimiting: null,            responseFormats: []        };
        // 测试支持的HTTP方法        const methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH'];        for (const method of methods) {            const response = await this.testMethod(endpoint, method);            if (response.status !== 405 && response.status !== 404) {                analysis.methods.push(method);
                // 分析参数                if (method === 'GET') {                    analysis.parameters = this.extractParametersFromURL(endpoint);                } else {                    analysis.parameters = await this.inferBodyParameters(endpoint, method);      ...