---
title: PHPDoc 语法大全
url: https://www.yanglong.pro/phpdoc-%e8%af%ad%e6%b3%95%e5%a4%a7%e5%85%a8/
source: 杨龙
date: 2026-06-08
fetch_date: 2026-06-09T06:02:30.982167
---

# PHPDoc 语法大全

[跳至正文](#content)

# [杨龙](https://www.yanglong.pro/)

菜单

* [首页](https://www.yanglong.pro/)
* [links](https://www.yanglong.pro/link/)

# PHPDoc 语法大全

[发表评论](https://www.yanglong.pro/phpdoc-%E8%AF%AD%E6%B3%95%E5%A4%A7%E5%85%A8/#respond)

我来为您整理一份完整的 PHPDoc 语法大全。

## PHPDoc 语法大全

### 1. 基本结构

```
/**
 * 简短描述（一行）
 *
 * 详细描述（多行）
 * 可以包含更多信息
 *
 * @tag 标签内容
 */
```

### 2. 常用标签

#### **@param** – 参数说明

```
/**
 * @param string $name 参数描述
 * @param int $age 年龄
 * @param array|null $data 可选数据
 * @param mixed $value 混合类型
 */
```

#### **@return** – 返回值

```
/**
 * @return string 返回用户名称
 * @return bool 返回布尔值
 * @return void 无返回值
 * @return array|object 多种返回类型
 */
```

#### **@var** – 变量类型

```
/**
 * @var string 用户名
 * @var int 年龄
 * @var array 数据数组
 */
public $name;
```

#### **@throws** / **@exception** – 异常

```
/**
 * @throws InvalidArgumentException 参数无效时抛出
 * @throws RuntimeException 运行时错误
 */
```

### 3. 类型声明

#### 基本类型

* `string` – 字符串
* `int` / `integer` – 整数
* `float` / `double` – 浮点数
* `bool` / `boolean` – 布尔值
* `array` – 数组
* `object` – 对象
* `callable` – 可调用
* `resource` – 资源
* `mixed` – 混合类型
* `void` – 无类型
* `null` – null值

#### 复合类型

```
/**
 * @param string|int $id ID可以是字符串或整数
 * @return array|null 返回数组或null
 * @var object|false 对象或false
 */
```

#### 数组类型

```
/**
 * @param string[] $names 字符串数组
 * @return int[][] 二维整数数组
 * @var array<string, int> 键为字符串，值为整数的数组
 */
```

#### 泛型/集合类型（PHPStan/Psalm风格）

```
/**
 * @param list<string> $items 列表
 * @return array<int, User> 用户数组
 * @var Collection<User> 用户集合
 */
```

### 4. 类相关标签

#### **@package** – 包名

```
/**
 * @package App\Models
 */
```

#### **@subpackage** – 子包

```
/**
 * @subpackage Controllers
 */
```

#### **@author** – 作者

```
/**
 * @author John Doe <john@example.com>
 */
```

#### **@copyright** – 版权

```
/**
 * @copyright 2024 Company Name
 */
```

#### **@license** – 许可证

```
/**
 * @license MIT
 */
```

#### **@version** – 版本

```
/**
 * @version 1.0.0
 */
```

#### **@since** – 起始版本

```
/**
 * @since 2.0.0
 */
```

#### **@deprecated** – 已废弃

```
/**
 * @deprecated 3.0.0 使用 newMethod() 替代
 */
```

### 5. 方法相关标签

#### **@abstract** – 抽象方法

```
/**
 * @abstract
 */
```

#### **@final** – 最终方法

```
/**
 * @final
 */
```

#### **@static** – 静态方法

```
/**
 * @static
 */
```

#### **@access** – 访问权限

```
/**
 * @access public
 * @access private
 * @access protected
 */
```

### 6. 继承和引用

#### **@inheritDoc** – 继承父类文档

```
/**
 * {@inheritDoc}
 */
```

#### **@see** – 参考

```
/**
 * @see MyClass::myMethod()
 * @see https://example.com
 * @see ClassName
 */
```

#### **@link** – 链接

```
/**
 * @link https://example.com 描述
 */
```

#### **@uses** – 使用

```
/**
 * @uses MyClass::method()
 */
```

#### **@used-by** – 被使用

```
/**
 * @used-by AnotherClass::anotherMethod()
 */
```

### 7. 属性和常量

#### **@property** – 魔术属性

```
/**
 * @property string $name 用户名
 * @property-read int $id 只读ID
 * @property-write string $password 只写密码
 */
```

#### **@method** – 魔术方法

```
/**
 * @method static User find(int $id) 查找用户
 * @method string getName() 获取名称
 */
```

#### **@const** – 常量

```
/**
 * @const int MAX_SIZE 最大尺寸
 */
```

### 8. 命名空间和类引用

#### **@category** – 分类

```
/**
 * @category Database
 */
```

#### **@todo** – 待办

```
/**
 * @todo 实现缓存功能
 */
```

#### **@fixme** – 需要修复

```
/**
 * @fixme 修复内存泄漏问题
 */
```

#### **@internal** – 内部使用

```
/**
 * @internal 仅供内部使用
 */
```

### 9. 完整示例

```
<?php

namespace App\Services;

use App\Models\User;
use Exception;

/**
 * 用户服务类
 *
 * 提供用户相关的业务逻辑处理
 *
 * @package App\Services
 * @author John Doe <john@example.com>
 * @version 1.0.0
 * @since 2024-01-01
 * @copyright 2024 Company
 * @license MIT
 */
class UserService
{
    /**
     * @var UserRepository 用户仓库
     */
    private $userRepository;

    /**
     * @var int 最大尝试次数
     * @const
     */
    const MAX_ATTEMPTS = 3;

    /**
     * 构造函数
     *
     * @param UserRepository $userRepository 用户仓库实例
     */
    public function __construct(UserRepository $userRepository)
    {
        $this->userRepository = $userRepository;
    }

    /**
     * 根据ID获取用户信息
     *
     * 从数据库中查询用户详细信息，包括关联的角色和权限
     *
     * @param int $id 用户ID，必须大于0
     * @param bool $withRelations 是否加载关联数据，默认true
     * @return User|null 返回用户对象，未找到返回null
     * @throws InvalidArgumentException 当ID无效时抛出
     * @throws DatabaseException 数据库查询失败时抛出
     * @see UserRepository::findById()
     * @link https://example.com/docs/user-api
     * @since 1.0.0
     * @deprecated 2.0.0 使用 getUserById() 替代
     *
     * @example
     * ```
php
     * $service = new UserService($repository);
     * $user = $service->findUser(123, true);
     * ```
     */
    public function findUser(int $id, bool $withRelations = true): ?User
    {
        if ($id <= 0) {
            throw new InvalidArgumentException("Invalid user ID: {$id}");
        }

        return $this->userRepository->findById($id, $withRelations);
    }

    /**
     * 批量获取用户列表
     *
     * @param array $ids 用户ID数组
     * @param int $page 页码，从1开始
     * @param int $perPage 每页数量
     * @return array{
     *     data: User[],
     *     total: int,
     *     page: int,
     *     perPage: int
     * } 分页结果
     * @throws Exception 查询失败时抛出
     */
    public function getUsers(array $ids, int $page = 1, int $perPage = 20): array
    {
        // 实现代码
    }

    /**
     * 创建新用户
     *
     * @param array<string, mixed> $data 用户数据
     *   - name: string 用户名（必填）
     *   - email: string 邮箱（必填）
     *   - age: int|null 年龄（可选）
     * @return User 创建的用户对象
     * @throws ValidationException 数据验证失败
     * @throws DuplicateException 用户已存在
     */
    public function createUser(array $data): User
    {
        // 实现代码
    }

    /**
     * 魔术方法：动态获取属性
     *
     * @property-read string $version 版本号
     * @property-read array $config 配置信息
     *
     * @param string $name 属性名
     * @return mixed 属性值
     * @throws BadMethodCallException 属性不存在
     */
    public function __get(string $name)
    {
        // 实现代码
    }

    /**
     * 魔术方法：动态调用方法
     *
     * @method static User findById(int $id) 通过ID查找
     * @method array findAll() 查找所有用户
     *
     * @param string $name 方法名
     * @param array $arguments 参数
     * @return mixed
     */
    public function __call(string $name, array $arguments)
    {
        // 实现代码
    }
}
```

### 10. IDE支持的工具

* **PhpStorm** – 完全支持PHPDoc
* **VS Code** + PHP Intelephense
* **PHPDocumentor** – 生成文档工具
* **PHPStan** – 静态分析
* **Psalm** – 静态分析
* **phpcs** + Squiz标准

### 11. 最佳实践

1. ✅ 始终使用 `/** */` 而不是 `/* */`
2. ✅ 保持描述简洁明了
3. ✅ 为所有公共API添加文档
4. ✅ 使用正确的类型声明
5. ✅ 包含示例代码（复杂功能）
6. ✅ 标注废弃方法和替代方案
7. ❌ 不要过度文档化显而易见的代码
8. ❌ 避免冗余信息

这份PHPDoc语法大全涵盖了日常开发中常用的所有标签和用法。不同的IDE和静态分析工具可能支持额外的扩展标签，建议根据项目需求选择合适的工具链。

本条目发布于[2026年6月8日](https://www.yanglong.pro/phpdoc-%E8%AF%AD%E6%B3%95%E5%A4%A7%E5%85%A8/ "09:23")。属于[PHP](https://www.yanglong.pro/category/php/)分类，被贴了 [PHPDoc](https://www.yanglong.pro/tag/phpdoc/) 标签。作者是[杨龙](https://www.yanglong.pro/author/admin/ "查看所有由杨龙发布的文章")。

### 文章导航

[← Call to undefined method GuzzleHttp\Psr7\Utils::redactUserInfo()](https://www.yanglong.pro/call-to-undefined-method-guzzlehttppsr7utilsredactuserinfo/)

### 发表回复 [取消回复](/phpdoc-%E8%AF%AD%E6%B3%95%E5%A4%A7%E5%85%A8/#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

评论 \*

显示名称 \*

邮箱 \*

网站

搜索

搜索

[502](https://www.yanglong.pro/tag/502/)
[certbot](https://www.yanglong.pro/tag/certbot/)
[composer](https://www.yanglong.pro/tag/composer/)
[docker](https://www.yanglong.pro/tag/docker/)
[ElasticSearch](https://www.yanglong.pro/tag/elasticsearch/)
[Flask-RESTful](https://www.yanglong.pro/tag/flask-restful/)
[flex](https://www.yanglong.pro/tag/flex/)
[gizp](https://www.yanglong.pro/tag/gizp/)
[goaccess](https://www.yanglong.pro/tag/goaccess/)
[GuzzleHttp](https://www.yanglong.pro/tag/guzzlehttp/)
[InnoDB存储引擎](https://www.yanglong.pro/tag/innodb%E5%AD%98%E5%82%A8%E5%BC%95%E6%93%8E/)
[javascript](https://www.yanglong.pro/tag/javascript/)
[jdk](https://www.yanglong.pro/tag/jdk/)
[laravel](https://www.yanglong.pro...