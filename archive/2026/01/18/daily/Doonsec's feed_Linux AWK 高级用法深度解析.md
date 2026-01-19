---
title: Linux AWK 高级用法深度解析
url: https://mp.weixin.qq.com/s/LNhSnbLrtyXVw4wMTHeBLg
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:44:05.057464
---

# Linux AWK 高级用法深度解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/G7WSQyicBkgjtxVibwOxyhAYweTcLJ5icsAOmqDlLKTRZrjGBHJticco5aznBKXR1Lu4GqqketChBjB357tqYpMYEw/0?wx_fmt=jpeg)

# Linux AWK 高级用法深度解析

原创

刘军军
刘军军

运维星火燎原

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/G7WSQyicBkgjtxVibwOxyhAYweTcLJ5icsAg3bDIPJeWM4zxibFMyXHnmLetGh63XVEUblqsVBzJwyjyhCHEV4c9WQ/640?wx_fmt=png&from=appmsg)

一、AWK 高级特性概述

AWK 不仅仅是一个文本处理工具，它是一门完整的编程语言。以下是 AWK 的高级特性分类：

|  |  |  |
| --- | --- | --- |
| 特性类别 | 主要功能 | 应用场景 |
| 数组处理 | 关联数组、多维数组 | 数据统计、分组汇总 |
| 函数编程 | 内置函数、自定义函数 | 复杂计算、字符串处理 |
| 模式匹配 | 正则表达式、范围模式 | 日志分析、数据提取 |
| 系统交互 | 执行系统命令、文件操作 | 系统管理、自动化脚本 |
| 高级I/O | 多文件处理、管道 | 大数据处理、报表生成 |

二、高级数组处理

2.1 关联数组深度应用

```
#!/bin/bash
# awk-advanced-arrays.sh

echo"=== AWK 高级数组处理 ==="

# 创建复杂的测试数据
cat > sales_data.txt << 'EOF'
2024-01-15,John,Electronics,1200.50,New York
2024-01-15,Jane,Clothing,850.75,Los Angeles
2024-01-15,Bob,Electronics,2100.00,New York
2024-01-16,John,Clothing,450.25,New York
2024-01-16,Jane,Electronics,1800.00,Los Angeles
2024-01-16,Alice,Books,320.50,Chicago
2024-01-17,Bob,Books,280.75,New York
2024-01-17,John,Electronics,950.00,New York
2024-01-17,Jane,Clothing,675.50,Los Angeles
EOF

echo"📊 销售数据:"
column -t -s',' sales_data.txt
echo"========================================"

# 1. 多维统计
echo"1. 📈 多维数据统计 (城市×品类):"
awk -F ',''
{
    date = $1
    salesperson = $2
    category = $3
    amount = $4
    city = $5

    # 多维统计
    sales_by_city_category[city][category] += amount
    sales_by_date_city[date][city] += amount
    salesperson_total[salesperson] += amount
    daily_total[date] += amount

    # 计数
    transaction_count[city][category]++
}
END {
    print "=== 城市×品类销售统计 ==="
    for (city in sales_by_city_category) {
        for (category in sales_by_city_category[city]) {
            printf "%-12s %-12s $%8.2f (%d笔)\n",
                   city, category,
                   sales_by_city_category[city][category],
                   transaction_count[city][category]
        }
    }

    print "\n=== 销售员业绩排名 ==="
    # 使用asorti对关联数组的索引进行排序
    n = asorti(salesperson_total, sorted_salespersons)
    for (i = n; i >= 1; i--) {
        person = sorted_salespersons[i]
        printf "%-8s: $%8.2f\n", person, salesperson_total[person]
    }
}' sales_data.txt

# 2. 数组的数组
echo -e "\n2. 🎯 复杂数据结构:"
awk -F ',''
{
    city = $5
    category = $3
    amount = $4

    # 创建城市→品类→金额的嵌套结构
    if (!(city in city_data)) {
        city_data[city]["total"] = 0
        city_data[city]["count"] = 0
        city_data[city]["categories"] = 0
    }

    city_data[city]["total"] += amount
    city_data[city]["count"]++

    if (!(category in city_data[city])) {
        city_data[city][category] = 0
        city_data[city]["categories"]++
    }
    city_data[city][category] += amount
}
END {
    print "=== 城市详细统计 ==="
    for (city in city_data) {
        printf "\n🏙️  城市: %s\n", city
        printf "   总销售额: $%.2f\n", city_data[city]["total"]
        printf "   交易笔数: %d\n", city_data[city]["count"]
        printf "   品类数量: %d\n", city_data[city]["categories"]

        # 输出每个品类的销售
        for (key in city_data[city]) {
            if (key != "total" && key != "count" && key != "categories") {
                printf "   %-12s: $%8.2f\n", key, city_data[city][key]
            }
        }
    }
}' sales_data.txt

# 清理
rm sales_data.txt
```

2.2 数组函数和操作

```
#!/bin/bash
# awk-array-functions.sh

echo"=== AWK 数组函数高级应用 ==="

# 创建测试数据
cat > student_scores.txt << 'EOF'
Alice:Math:95:Physics:88:Chemistry:92
Bob:Math:78:Physics:85:Chemistry:90
Carol:Math:92:Physics:96:Chemistry:94
David:Math:85:Physics:82:Chemistry:88
Eve:Math:91:Physics:89:Chemistry:93
EOF

echo"📊 学生成绩数据:"
cat student_scores.txt
echo"========================================"

# 1. 数组长度和遍历
echo"1. 📏 数组操作函数:"
awk -F ':''
{
    student = $1
    # 动态创建科目→成绩的映射
    for (i = 2; i <= NF; i += 2) {
        subject = $i
        score = $(i+1)
        scores[student][subject] = score
        subjects[subject]++  # 记录所有科目
    }
}
END {
    print "=== 学生成绩统计 ==="

    # 获取学生数量
    student_count = length(scores)
    printf "学生数量: %d\n", student_count

    # 获取科目数量
    subject_count = length(subjects)
    printf "科目数量: %d\n", subject_count

    # 遍历所有学生
    print "\n📋 学生列表:"
    for (student in scores) {
        printf "%-8s", student
    }
    print ""

    # 遍历所有科目并计算平均分
    print "\n📊 科目平均分:"
    for (subject in subjects) {
        total = 0
        count = 0
        for (student in scores) {
            if (subject in scores[student]) {
                total += scores[student][subject]
                count++
            }
        }
        avg = total / count
        printf "%-10s: %.1f\n", subject, avg
    }

    # 删除数组元素示例
    print "\n🗑️  删除Bob的数据后:"
    delete scores["Bob"]
    for (student in scores) {
        printf "%-8s", student
    }
    print ""
}' student_scores.txt

# 2. 数组复制和比较
echo -e "\n2. 🔄 数组的复制和比较:"
awk '
BEGIN {
    # 创建源数组
    source["Math"] = 90
    source["Physics"] = 85
    source["Chemistry"] = 92

    print "源数组:"
    for (key in source) {
        printf "  %s: %d\n", key, source[key]
    }

    # 数组复制（手动）
    print "\n复制数组:"
    for (key in source) {
        copy[key] = source[key]
        printf "  %s: %d\n", key, copy[key]
    }

    # 检查数组是否相等
    is_equal = 1
    for (key in source) {
        if (!(key in copy) || source[key] != copy[key]) {
            is_equal = 0
            break
        }
    }
    if (length(source) != length(copy)) {
        is_equal = 0
    }

    print "\n数组相等:", is_equal ? "是" : "否"

    # 修改副本并再次比较
    copy["Math"] = 95
    is_equal_after = 1
    for (key in source) {
        if (!(key in copy) || source[key] != copy[key]) {
            is_equal_after = 0
            break
        }
    }
    print "修改后相等:", is_equal_after ? "是" : "否"
}'

# 清理
rm student_scores.txt
```

三、高级函数编程

3.1 自定义函数深度应用

```
#!/bin/bash
# awk-custom-functions.sh

echo"=== AWK 自定义函数高级应用 ==="

# 创建金融交易数据
cat > transactions.txt << 'EOF'
2024-01-15T10:30:25,INV-001,John Doe,1500.00,COMPLETED
2024-01-15T11:15:30,INV-002,Jane Smith,2750.50,COMPLETED
2024-01-15T12:45:15,INV-003,Bob Johnson,980.75,PENDING
2024-01-15T14:20:40,INV-004,Alice Brown,3200.25,COMPLETED
2024-01-15T15:55:10,INV-005,Charlie Wilson,450.00,FAILED
EOF

echo"💳 交易数据:"
cat transactions.txt
echo"========================================"

# 1. 自定义函数库
echo"1. 🛠️  自定义函数库实现:"
awk -F ',''
# 函数定义必须在BEGIN之前
function format_amount(amount) {
    if (amount >= 1000) {
        return sprintf("$%\'d", amount)
    } else {
        return sprintf("$%.2f", amount)
    }
}

function get_status_color(status) {
    switch (status) {
        case "COMPLETED":
            return "✅"
        case "PENDING":
            return "⏳"
        case "FAILED":
            return "❌"
        default:
            return "❓"
    }
}

function parse_timestamp(timestamp,    datetime, date, time) {
    split(timestamp, datetime, "T")
    date = datetime[1]
    time = datetime[2]
    gsub(/-/, "/", date)  # 转换日期格式
    return date "" time
}

function calculate_tax(amount, rate) {
    return amount * rate
}

function generate_report_line(transaction,    fields) {
    split(transaction, fields, ",")
    return sprintf("%s %s %-12s %12s %s",
        get_status_color(fields[5]),
        parse_timestamp(fields[1]),
        fields[3],
        format_amount(fields[4]),
        fields[5])
}

# 主处理逻辑
{
    # 使用自定义函数处理数据
    formatted = generate_report_line($0)
    print formatted

    # 统计信息
    total_amount += $4
    status_count[$5]++
}
END {
    print "\n=== 交易统计 ==="
    printf "总交易金额: %s\n", format_amount(total_amount)
    printf "平均交易额: %s\n", format_amount(total_amount / NR)

    print "\n交易状态分布:"
    for (status in status_count) {
        printf "%-10s: %d 笔\n", status, status_count[status]
    }

    # 计算税费示例
    tax_rate = 0.08
    tax_amount = calculate_tax(total_amount, tax_rate)
    printf "\n税费估算 (%.1f%%): %s\n", tax_rate * 100, format_amount(tax_amount)
}' transactions.txt

# 2. 递归函数和数...