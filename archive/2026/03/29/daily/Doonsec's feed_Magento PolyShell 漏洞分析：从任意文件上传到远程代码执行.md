---
title: Magento PolyShell 漏洞分析：从任意文件上传到远程代码执行
url: https://mp.weixin.qq.com/s/CMTONs0DYNaV3w-KZwfoGg
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:44:07.576723
---

# Magento PolyShell 漏洞分析：从任意文件上传到远程代码执行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfnPGrfX5p3XQbtac1lEXVLEIePgKZXNhpttsWiczqibUq1965SiaBUpRJzjbETDYaYyJeZXSM4dT65zmticScJY3slicC4CMB7jMBQ/0?wx_fmt=jpeg)

# Magento PolyShell 漏洞分析：从任意文件上传到远程代码执行

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 本文深入分析了 Magento/Adobe Commerce 中的一个高危漏洞（APSB25-94/PolyShell），该漏洞允许未授权攻击者通过 REST API 上传任意文件，在特定服务器配置下可导致远程代码执行或持久性 XSS。文章详细拆解了漏洞原理、利用条件、影响范围，并提供了临时的缓解与排查措施。

## 漏洞概述

**影响范围**：所有生产版本，包括 Magento Open Source 和 Adobe Commerce，最高版至 2.4.9-alpha2。

**危害等级**：高危。漏洞本质是未授权、无限制的文件上传。在特定服务器配置下，攻击者可上传恶意文件并执行，实现远程代码执行（RCE）。即使在安全配置下，攻击者也能在目标服务器上持久化存储一个可控文件，构成潜在威胁。

## 技术原理分析

漏洞位于处理购物车商品自定义选项文件上传的 REST API 端点。

* **攻击入口点**

  ：通过 `GuestCartItemRepositoryInterface::save()` 接口，对应的 REST API 端点为 `POST /rest/default/V1/guest-carts/:cartId/items`。攻击者无需身份认证。
* **触发路径**

  ：API 请求中，在 `cart_item.product_option.extension_attributes.custom_options` 里包含一个 `file_info` 对象，对象中包含 Base64 编码的文件数据、MIME 类型和文件名。

请求载荷示例：

POST /rest/default/V1/guest-carts/cart\_id/items HTTP/1.1
Host: example.com
Accept: application/json
Content-Type: application/json

{
  "cart\_item": {
    "qty": 1,
    "sku": "some\_product",
    "product\_option": {
      "extension\_attributes": {
        "custom\_options": [
          {
            "option\_id": "1",
            "option\_value": "file",
            "extension\_attributes": {
              "file\_info": {
                "base64\_encoded\_data": "...",
                "name": "shell.php",
                "type": "image/png"
              }
            }
          }
        ]
      }
    }
  }
}

文件上传的处理逻辑位于 `ImageProcessor::processImageContent` 方法。

关键在于验证环节，由 `ImageContentValidator::isValid` 负责。它检查以下几点：

* 文件数据非空且使用 Base64 正确编码。
* 通过 PHP 的 `getimagesizefromstring` 函数能解析出有效的图片属性（尺寸和 MIME 类型）。
* 从数据解析出的 MIME 类型必须在允许列表中（默认包括 image/jpg, image/jpeg, image/gif, image/png）。
* 文件名不能包含 `/ ? * : " ; < > ( ) | { } \` 等特殊字符。

注意，这里**没有**检查文件扩展名是否与 MIME 类型匹配。这就是漏洞的核心。攻击者可以提交一个“多重格式”文件，它既是一个有效的 PNG/GIF（能通过 `getimagesizefromstring` 验证），同时又包含 PHP 代码。

生成这种文件很简单：

1. **GIF 头部+PHP 载荷**

   ：在 PHP 代码前添加 `GIF89a` 头部，就能骗过 `getimagesizefromstring`，使其认为这是一个有效的 GIF 文件。
2. **在 PNG 注释中嵌入 PHP**

   ：使用 ExifTool 等工具，将 PHP 代码写入一个微小 PNG 图片的注释（Comment）字段。这样既能保持 PNG 格式完全有效，又能携带载荷。

## 影响范围与利用条件

**受影响版本**：

* Magento Open Source 2.x 至 2.4.9-alpha2。
* Adobe Commerce 2.x 至 2.4.9-alpha2。

**利用前提条件**：

1. 攻击者需要知道一个有效的产品 SKU。这可以通过前端的 GraphQL API 轻松查询获得：

   POST /graphql HTTP/1.1
   {"query":"{ products(search: "", pageSize: 1) { items { sku } } }"}
2. 攻击者需要创建一个访客购物车（Guest Cart），通过 `POST /rest/default/V1/guest-carts` 即可获得购物车 ID。
3. **最关键**

   ：服务器配置必须允许访问上传的文件。默认情况下，Magento/Adobe 的配置应该是安全的。

**服务器配置是关键**：

在 Apache 环境中，`pub/media/.htaccess` 文件包含 `php_flag engine 0`，这会禁用该目录下 PHP 文件的解析。`pub/media/custom_options/.htaccess` 文件则默认拒绝所有访问。

如果这些 `.htaccess` 文件**缺失**，或者 Apache 配置的 `AccessFileName` 被修改（例如改为 `.config`）而文件未重命名，攻击者就有可能：

* 访问到上传的文件，造成存储型 XSS（如果文件内容可控）。
* 执行上传的 PHP 文件，实现 RCE（如果 `.php` 文件可解析）。

在 Nginx 环境中，官方示例配置包含针对 `pub/media/custom_options` 路径的 `deny all` 指令。如果管理员在自定义配置时移除了这些限制，同样会导致漏洞可利用。

换句话说，这个漏洞的实际影响严重依赖目标站点的部署配置。但就算现在配置安全，如果服务器上已经存在攻击者上传的恶意文件，未来配置一旦变更，风险就会立刻显现。

## 漏洞复现与 PoC

一个完整的利用脚本需要几步：

1. 通过 GraphQL 获取一个产品 SKU。
2. 创建一个访客购物车，获取 cart\_id。
3. 构造一个包含恶意“图片”的 Polyglot 载荷。例如，使用 ExifTool 将 PHP 代码注入到一个 1x1 像素 PNG 的注释中并 Base64 编码。
4. 将载荷通过 `/rest/default/V1/guest-carts/{cart_id}/items` 端点上传，并指定一个 `.php` 扩展名。
5. 尝试访问上传的文件，检查是否可访问或可执行。

上传成功后，文件路径通常为 `pub/media/custom_options/quote/{filename[0]}/{filename[1]}/{filename}`。

例如，上传文件 `shell.php` 后，可以尝试访问以下 URL 验证：

* `/pub/media/custom_options/quote/s/h/shell.php`
* `/media/custom_options/quote/s/h/shell.php`

## 修复建议与缓解措施

**官方补丁状态**：在 2.4.9-alpha3 版本中，Adobe 引入了修复。新增了 `Magento\Catalog\Model\Product\Option\Type\File\ImageContentProcessor` 类，并在 `validateBeforeSaveToTmp` 方法中添加了对文件扩展名的检查，会阻止一系列可执行文件类型（如 .php, .phtml, .sh 等）的上传。但截至分析时，此修复尚未应用到稳定版分支。

**临时缓解方案**：

* **应用第三方补丁**

  ：可以使用社区提供的临时补丁，例如 `markshust/magento-polyshell-patch`。
* **检查服务器配置**

  ：

+ 确保 `pub/media/.htaccess` 和 `pub/media/custom_options/.htaccess` 文件存在且内容正确。
+ 对于 Nginx，复查配置，确保对 `pub/media/custom_options` 路径有严格的访问控制（`deny all`）并禁止执行 PHP。

* **主动搜索可疑文件**

  ：在服务器上运行以下命令，查找已上传的非图片文件：

  find pub/media/custom\_options/ -type f ! -name '.htaccess'

   仔细审查所有找到的文件，特别是那些扩展名不是 .png, .jpg, .jpeg, .gif 的文件。对于 .svg 文件要格外小心，它们可能用于 XSS。删除所有可疑或不应存在的文件。

最后，保持关注官方安全公告，一旦补丁发布，立即升级到已修复的版本。

---

### 参考资料

[1] https://slcyber.io/research-center/magento-polyshell-unauthenticated-file-upload-to-rce-in-magento-apsb25-94/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过