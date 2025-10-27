---
title: 偶然？还是必然？ — 谁是罪魁祸首
url: https://h4ck.org.cn/2025/08/21237
source: obaby@mars
date: 2025-08-10
fetch_date: 2025-10-07T00:17:34.851602
---

# 偶然？还是必然？ — 谁是罪魁祸首

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[后台开发『BackEnd』](https://h4ck.org.cn/cats/cxsj/backend)

# 偶然？还是必然？ — 谁是罪魁祸首

2025年8月9日
[47 条评论](https://h4ck.org.cn/2025/08/21237#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/330A1674-tuya-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/330A1674-tuya.jpg)

宝子放假，转眼假期已经过了一半，想着找个周末带宝子回老家住几天，大姐家的孩子周日要办升学宴，既然都回来了，不去也不合适，刚好就可以周六回老家，周日去淄博。

对象说，周日青岛会下大暴雨，还是下班之后直接回吧，不然第二天很可能走不了。

就这样，马不停蹄，下班买点东西就直接接上孩子往回走。天气预报零点的雨，在九点多到潍坊的时候就开始逐渐大了。

对象开车的时候，自己打开手机想回复下评论，但是却发现一个问题，那就是页面非常卡。刚开始还以为是网络问题，但是切到短视频却异常流畅。

瞬间有种不祥的预感，那就是服务器的 cpu 肯定又跑满了。

之前看到威言威语发的[《暂时停用腾讯EdgeOne了》](https://www.weisay.com/blog/temporarily-disabled-edgeone.html) ，感觉自己的系统貌似没什么太大的问题。但是，实际上是在这之前，切换到 eo 之后，也出现过一次 cpu 跑满的情况，当时重启 php 之后一切正常了，以为是偶发事件。所以也没再关注，但是这次尝试远程重启服务之后，只是瞬间缓解。几分钟之后就又卡死了，**所以昨天能发评论的宝子真的都是真爱，么么哒(๑•́₃•̀๑)，因为我自己都打不开我的后台。**😂

这种感觉还有一个前兆，那就是后台资源库突然多了个文件。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/53FC004E74654E68CDC38C58829D0DF9.png)](https://h4ck.org.cn/wp-content/uploads/2025/08/53FC004E74654E68CDC38C58829D0DF9.png)

不过这个文件看起来是某个插件的压缩包，但是描述是另外一个域名，猜测是另外一个域名传上来的。但是。搜了下这个用户不存在，所以最后直接把插件和文件一起删除了。

但是这个 cpu 跑满的感觉还是感觉是 cc，不然不至于 php 能直接占满了全部资源。

到家之后，看了下 eo 的后台没什么能配置地方。但是，通过服务器的访问记录却发现，有几个地址在频繁请求登录页面：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250808-214858-1-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250808-214858-1.jpg) [![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250808-223424-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250808-223424.jpg)

当然，更诡异的是这里面好几个 ip 竟然都是腾讯的海外节点。这就有点奇怪了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250809-112749.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250809-112749.jpg) [![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250809-112803.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250809-112803.jpg)

尤其是 163 这个，按照常理来说，如果是 cdn 节点回源，应该不会摁着这一个地址回源，并且这个请求频率大概率会被 cdn 拦截，然而，现在的现象是不单没被拦截，还高频访问，一个地址在一秒内发起了几十个请求。这尼玛就离谱了，查了一下加速域名的节点，发现这些都不在 eo 的节点列表内。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250809-113027.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250809-113027.jpg)

那么，此时会合理的猜的就是 eo 的机房内或者是在某些地方的节点回源会泄露原始服务器地址，这样这一系列的请求就说的通了。这些请求本身并没有结果 cdn，所以直接是从机房发起的请求。

在回源地址泄露之后，有人通过 bot 控制了大量机房内的机器，尝试对 wp 的登录地址进行暴力破解，而这告诉 cc 也导致了家里的 mac mini 的服务器资源瞬间被耗尽了。

所以这个问题不是 eo 本身导致的，但是确实是套了 eo 的国外节点之后，有 eo 的某些请求泄露回源地址导致出现了直接针对服务器的 cc 攻击。这个攻击目标很明确，就是破解登录密码。本来想直接封锁那几个 ip，但是封锁之后发现还是不断的有新的开始尝试，于是，最新版本的工具就出现了，直接写个脚本，通过检测 nginx 访问日志，实现对 ip 动态风控。

代码如下：

```
#!/bin/bash

# 实时监控日志文件并自动封锁恶意IP
# 使用方法: sudo ./realtime_block.sh

LOG_FILE="/home/wwwlogs/h4ck.org.cn.log"
BLOCKED_IPS_FILE="/tmp/blocked_ips.txt"
MAX_REQUESTS_PER_MINUTE=10
BLOCK_DURATION=3600  # 封锁时间（秒）
DEBUG_MODE=false  # 设置为true启用调试模式
QUIET_MODE=false  # 设置为true启用静默模式（只显示新增封锁）
ATTACK_HISTORY_FILE="/tmp/attack_history.txt"  # 攻击历史记录文件

# 检查是否以root权限运行
if [ "$EUID" -ne 0 ]; then
    echo "请使用sudo运行此脚本"
    exit 1
fi

# 检查inotify-tools是否安装
if ! command -v inotifywait &> /dev/null; then
    echo "请先安装inotify-tools:"
    echo "Ubuntu/Debian: sudo apt-get install inotify-tools"
    echo "CentOS/RHEL: sudo yum install inotify-tools"
    exit 1
fi

# 检查日志文件是否存在
if [ ! -f "$LOG_FILE" ]; then
    echo "错误: 日志文件 $LOG_FILE 不存在"
    exit 1
fi

# 创建iptables链（如果不存在）
iptables -N BLOCK_MALICIOUS_IPS 2>/dev/null

# 确保BLOCK_MALICIOUS_IPS链在INPUT链的最前面
iptables -C INPUT -j BLOCK_MALICIOUS_IPS 2>/dev/null || iptables -I INPUT 1 -j BLOCK_MALICIOUS_IPS

# 初始化文件
touch "$BLOCKED_IPS_FILE"
touch "$ATTACK_HISTORY_FILE"

# 函数：检查并修复iptables配置
check_iptables_config() {
    echo "检查iptables配置..."

    # 检查BLOCK_MALICIOUS_IPS链是否存在
    if ! iptables -L BLOCK_MALICIOUS_IPS >/dev/null 2>&1; then
        echo "创建BLOCK_MALICIOUS_IPS链..."
        iptables -N BLOCK_MALICIOUS_IPS
    fi

    # 检查INPUT链中是否包含BLOCK_MALICIOUS_IPS
    if ! iptables -C INPUT -j BLOCK_MALICIOUS_IPS 2>/dev/null; then
        echo "将BLOCK_MALICIOUS_IPS链插入到INPUT链的最前面..."
        iptables -I INPUT 1 -j BLOCK_MALICIOUS_IPS
    fi

    # 显示当前配置
    echo "当前iptables配置:"
    iptables -L INPUT -n --line-numbers | head -10
    echo "BLOCK_MALICIOUS_IPS链规则:"
    iptables -L BLOCK_MALICIOUS_IPS -n
}

# 函数：重新加载已封锁的IP到iptables
reload_blocked_ips() {
    echo "重新加载已封锁的IP到iptables..."

    if [ -f "$BLOCKED_IPS_FILE" ]; then
        local count=0
        while read -r ip; do
            if [ -n "$ip" ]; then
                # 检查iptables中是否已有此规则
                if ! iptables -C BLOCK_MALICIOUS_IPS -s "$ip" -j DROP 2>/dev/null; then
                    iptables -A BLOCK_MALICIOUS_IPS -s "$ip" -j DROP
                    count=$((count + 1))
                fi
            fi
        done < "$BLOCKED_IPS_FILE"
        echo "重新加载了 $count 个IP到iptables"
    fi
}

# 检查并修复iptables配置
check_iptables_config

# 重新加载已封锁的IP
reload_blocked_ips

echo "开始实时监控日志文件: $LOG_FILE"
echo "最大请求频率: $MAX_REQUESTS_PER_MINUTE 次/分钟"
echo "封锁时间: $BLOCK_DURATION 秒"

# 函数：封锁IP
block_ip() {
    local ip=$1
    local reason=$2

    # 检查IP是否已经被封锁
    if ! grep -q "^$ip$" "$BLOCKED_IPS_FILE"; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') - 封锁IP: $ip (原因: $reason)"

        # 添加到iptables（确保规则正确添加）
        iptables -A BLOCK_MALICIOUS_IPS -s "$ip" -j DROP

        # 验证规则是否添加成功
        if iptables -C BLOCK_MALICIOUS_IPS -s "$ip" -j DROP 2>/dev/null; then
            echo "$(date '+%Y-%m-%d %H:%M:%S') - 成功添加iptables规则: $ip"
        else
            echo "$(date '+%Y-%m-%d %H:%M:%S') - 警告: iptables规则添加失败: $ip"
        fi

        # 记录到文件
        echo "$ip" >> "$BLOCKED_IPS_FILE"

        # 记录日志
        echo "$(date '+%Y-%m-%d %H:%M:%S') - 封锁IP: $ip (原因: $reason)" >> /var/log/realtime_block.log
    else
        echo "$(date '+%Y-%m-%d %H:%M:%S') - IP $ip 已经被封锁"
    fi
}

# 函数：记录攻击历史
record_attack() {
    local ip=$1
    local attack_type=$2
    local timestamp=$(date +%s)
    echo "$ip|$attack_type|$timestamp" >> "$ATTACK_HISTORY_FILE"
}

# 函数：检查攻击历史
check_attack_history() {
    local ip=$1
    local attack_type=$2
    local current_time=$(date +%s)
    local time_window=300  # 5分钟时间窗口

    # 清理过期的攻击记录
    local temp_file="/tmp/temp_attack_history.txt"
    while IFS='|' read -r record_ip record_type record_time; do
        if [ $((current_time - record_time)) -lt $time_window ]; then
            echo "$record_ip|$record_type|$record_time" >> "$temp_file"
        fi
    done < "$ATTACK_HISTORY_FILE"

    mv "$temp_file" "$ATTACK_HISTORY_FILE" 2>/dev/null

    # 统计该IP在时间窗口内的攻击次数
    local attack_count=$(grep "^$ip|" "$ATTACK_HISTORY_FILE" | wc -l)
    echo "$attack_count"
}

# 函数：分析新日志条目
analyze_new_logs() {
    local new_lines="$1"

    if [ -n "$new_lines" ]; then
        if [ "$DEBUG_MODE" = true ]; then
            echo "DEBUG: 分析新日志行数: $(echo "$new_lines" | wc -l)"
        fi

        # 统计IP请求频率
        local ip_counts=$(echo "$new_lines" | awk '{print $1}' | sort | uniq -c | sort -nr)

        if [ "$DEBUG_MODE" = true ] && [ -n "$ip_counts" ]; then
            echo "DEBUG: IP统计结果:"
            echo "$ip_counts"
        fi

        # 检查每个IP的请求频率
        while read -r count ip; do
            if [ -n "$ip" ] && [ "$count" -gt "$MAX_REQUESTS_PER_MINUTE" ]; then
                record_attack "$ip" "high_frequency"
                local total_attacks=$(che...