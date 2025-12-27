---
title: Burp Suite 正则生成插件
url: https://darkless.cn/2025/09/24/brg/
source: darkless
date: 2025-12-26
fetch_date: 2025-12-27T03:23:07.256343
---

# Burp Suite 正则生成插件

[![](/images/logo1.svg)](/)
[darkless](/)

* [首页](/)
* [归档](/archives/)
* [标签](/tags/)
* [分类](/categories/)
* [文档](https://doc.darkless.cn/)
* [安全工具](https://darkless.notion.site/12832eebad358008894af8e247044d02)
* [留言](/contact/)

* [首页](/)
* [归档](/archives/)
* [标签](/tags/)
* [分类](/categories/)
* [文档](https://doc.darkless.cn/)
* [安全工具](https://darkless.notion.site/12832eebad358008894af8e247044d02)
* [留言](/contact/)

Burp Suite 正则生成插件

![](https://cdn.jsdelivr.net/gh/handbye/images@master/uPic/2025/12/4r7Z3K.png)

![](/images/avatar.webp)

darkless

2025-12-26

2025-12-26

* [web安全](/categories/web%E5%AE%89%E5%85%A8/)
* [安全工具](/categories/web%E5%AE%89%E5%85%A8/%E5%AE%89%E5%85%A8%E5%B7%A5%E5%85%B7/)

* [安全工具](/tags/%E5%AE%89%E5%85%A8%E5%B7%A5%E5%85%B7/)
* [burpsuite](/tags/burpsuite/)

# **Burp Suite Regex Generator**

> github地址：<https://github.com/handbye/BRG>

一个智能的Burp Suite插件，用于生成精确的正则表达式模式。

### **核心功能**

快速生成两种类型的正则表达式：

1. **Escape Literal** - 完全精确匹配
2. **Smart Precise** - 上下文定位 + 值匹配（推荐）

### **Smart Precise 原理**

使用**正则断言**（lookaround assertions）实现：

* **上下文** → 用于精确定位（不包含在匹配结果中）
* **值模式** → 通用正则，可匹配同类值

### **示例**

**HTTP响应**：

|  |
| --- |
| ``` {"code": 200, "message": "success", "data": {...}} ``` |

**操作**：选中 `success`

**生成的正则**：

|  |
| --- |
| ``` (?<="message":\s*")[a-z0-9]+(?=") ``` |

**工作原理**：

* `(?<="message":\s*")` - 正向后顾：确保前面是 `"message": "`
* `[a-z0-9]+` - 匹配模式：任何字母数字组合
* `(?=")` - 正向先行：确保后面是 `"`

**匹配结果**：

* ✅ 匹配 `success`（只匹配值本身）
* ✅ 也能匹配 `error`、`failed` 等
* ✅ 不会匹配其他字段的值（上下文限制）
* ✅ 结果中不包含 `"message":` 或引号

### **自动模式识别**

Smart Precise会自动识别值的类型，生成相应的通用模式：

| **值类型** | **示例** | **生成模式** |
| --- | --- | --- |
| Base64 | `iVBORw0KGgoAAAA...` | `[A-Za-z0-9+/]+=*` |
| 十六进制 | `abc123def456` | `[0-9a-fA-F]+` |
| UUID | `550e8400-e29b-41d4...` | `[0-9a-f]{8}-[0-9a-f]{4}-...` |
| 字母数字 | `la91gabie35w9e8...` | `[a-z0-9]+` |
| 纯数字 | `12345` | `\d+` |
| 纯字母 | `success` | `[a-z]+` |

### **使用方法**

1. 在Burp Suite中选中要匹配的值
2. 右键 → **Generate Regex**
3. 选择模式：
   * **Escape Literal** - 完全精确匹配选中的文本
   * **✓ Smart Precise** - 生成带上下文的通用模式（推荐）
4. 在弹出对话框中：
   * 查看生成的正则表达式
   * 在完整的请求/响应中测试
   * 复制到剪贴板使用

### **安装**

### **方法1：从Release下载**

1. 下载 `regex-generator-1.0.jar`
2. Burp Suite → Extender → Extensions → Add
3. 选择下载的JAR文件

### **方法2：从源码编译**

|  |
| --- |
| ``` # 需要Java 17 export JAVA_HOME=/path/to/jdk-17 mvn clean package  # 生成的文件：target/regex-generator-1.0.jar ``` |

### **实际应用场景**

### **场景1：API响应消息**

|  |
| --- |
| ``` {"message": "success"} ``` |

选中 `success` → 生成：`(?<="message":\s*")[a-z]+(?=")`
可用于匹配任何message值

### **场景2：Base64图片数据**

|  |
| --- |
| ``` {"image": "iVBORw0KGgoAAAA..."} ``` |

选中Base64 → 生成：`(?<="image":\s*")[A-Za-z0-9+/]+=*(?=")`
可用于提取任何Base64图片

### **场景3：Token/Identifier**

|  |
| --- |
| ``` {"identifier": "la91gabie35w9e8gmyrnkvryl47hzaa1"} ``` |

选中identifier值 → 生成：`(?<="identifier":\s*")[a-z0-9]+(?=")`
可用于匹配任何identifier

## 图片

![image.png](/../post_images/d99571d859de22f4331e38938576eb6c.png)

### **技术细节**

* **Java版本**：17
* **Burp API**：Montoya API 2023.12.1
* **正则引擎**：Java `java.util.regex.Pattern`
* **上下文长度**：最多12个字符，自动处理换行边界

### **优势**

✅ **精确定位** - 使用上下文确保在正确位置匹配
✅ **值匹配** - 匹配结果只包含值本身，不含上下文
✅ **通用性强** - 自动生成可复用的模式
✅ **智能识别** - 自动检测Base64、UUID等常见格式
✅ **易于测试** - 内置测试功能，显示完整请求/响应

Burp Suite 正则生成插件

/2025/09/24/brg/

作者

darkless

发布于

2025-12-26 08:00

许可

* [安全工具](/tags/%E5%AE%89%E5%85%A8%E5%B7%A5%E5%85%B7/)
* [burpsuite](/tags/burpsuite/)

[ubuntu安装IDA9.0并开启mcp
下一篇](/2025/09/24/IDA-mcp/ "ubuntu安装IDA9.0并开启mcp")

评论

评论插件加载失败
点击重新加载

正在加载评论插件

1. [Burp Suite Regex Generator](#Burp-Suite-Regex-Generator)
   1. [核心功能](#%E6%A0%B8%E5%BF%83%E5%8A%9F%E8%83%BD)
   2. [Smart Precise 原理](#Smart-Precise-%E5%8E%9F%E7%90%86)
   3. [示例](#%E7%A4%BA%E4%BE%8B)
   4. [自动模式识别](#%E8%87%AA%E5%8A%A8%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB)
   5. [使用方法](#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95)
   6. [安装](#%E5%AE%89%E8%A3%85)
   7. [方法1：从Release下载](#%E6%96%B9%E6%B3%951%EF%BC%9A%E4%BB%8ERelease%E4%B8%8B%E8%BD%BD)
   8. [方法2：从源码编译](#%E6%96%B9%E6%B3%952%EF%BC%9A%E4%BB%8E%E6%BA%90%E7%A0%81%E7%BC%96%E8%AF%91)
   9. [实际应用场景](#%E5%AE%9E%E9%99%85%E5%BA%94%E7%94%A8%E5%9C%BA%E6%99%AF)
   10. [场景1：API响应消息](#%E5%9C%BA%E6%99%AF1%EF%BC%9AAPI%E5%93%8D%E5%BA%94%E6%B6%88%E6%81%AF)
   11. [场景2：Base64图片数据](#%E5%9C%BA%E6%99%AF2%EF%BC%9ABase64%E5%9B%BE%E7%89%87%E6%95%B0%E6%8D%AE)
   12. [场景3：Token/Identifier](#%E5%9C%BA%E6%99%AF3%EF%BC%9AToken-Identifier)
2. [图片](#%E5%9B%BE%E7%89%87)
   1. [技术细节](#%E6%8A%80%E6%9C%AF%E7%BB%86%E8%8A%82)
   2. [优势](#%E4%BC%98%E5%8A%BF)

© 2019 - 2025
   [darkless](/)

由 [Hexo](https://hexo.io) 驱动 & 主题 [Keep](https://github.com/XPoet/hexo-theme-keep)

![]()

1. [Burp Suite Regex Generator](#Burp-Suite-Regex-Generator)
   1. [核心功能](#%E6%A0%B8%E5%BF%83%E5%8A%9F%E8%83%BD)
   2. [Smart Precise 原理](#Smart-Precise-%E5%8E%9F%E7%90%86)
   3. [示例](#%E7%A4%BA%E4%BE%8B)
   4. [自动模式识别](#%E8%87%AA%E5%8A%A8%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB)
   5. [使用方法](#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95)
   6. [安装](#%E5%AE%89%E8%A3%85)
   7. [方法1：从Release下载](#%E6%96%B9%E6%B3%951%EF%BC%9A%E4%BB%8ERelease%E4%B8%8B%E8%BD%BD)
   8. [方法2：从源码编译](#%E6%96%B9%E6%B3%952%EF%BC%9A%E4%BB%8E%E6%BA%90%E7%A0%81%E7%BC%96%E8%AF%91)
   9. [实际应用场景](#%E5%AE%9E%E9%99%85%E5%BA%94%E7%94%A8%E5%9C%BA%E6%99%AF)
   10. [场景1：API响应消息](#%E5%9C%BA%E6%99%AF1%EF%BC%9AAPI%E5%93%8D%E5%BA%94%E6%B6%88%E6%81%AF)
   11. [场景2：Base64图片数据](#%E5%9C%BA%E6%99%AF2%EF%BC%9ABase64%E5%9B%BE%E7%89%87%E6%95%B0%E6%8D%AE)
   12. [场景3：Token/Identifier](#%E5%9C%BA%E6%99%AF3%EF%BC%9AToken-Identifier)
2. [图片](#%E5%9B%BE%E7%89%87)
   1. [技术细节](#%E6%8A%80%E6%9C%AF%E7%BB%86%E8%8A%82)
   2. [优势](#%E4%BC%98%E5%8A%BF)