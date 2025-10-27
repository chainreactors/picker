---
title: Laravel Under The Hood -  What Are Facades?
url: https://buaq.net/go-247952.html
source: unSafe.sh - 不安全
date: 2024-06-30
fetch_date: 2025-10-06T16:54:41.205926
---

# Laravel Under The Hood -  What Are Facades?

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Laravel Under The Hood - What Are Facades?

You've just installed a fresh Laravel application, booted it up, and got the welcome page. Like ever
*2024-6-29 23:0:20
Author: [hackernoon.com(查看原文)](/jump-247952.htm)
阅读量:4
收藏*

---

You've just installed a fresh Laravel application, booted it up, and got the welcome page. Like everyone else, you try to see how it's rendered, so you hop into the `web.php` file and encounter this code:

```
<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});
```

It's obvious how we got the welcome view, but you're curious about how Laravel's router works, so you decide to dive into the code. The initial assumption is: There's a `Route` class on which we're calling a static method `get()`. However, upon clicking it, there is no `get()` method there. So, what kind of dark magic is happening? Let's demystify this!

## Regular Facades

> Please note that I stripped most of the PHPDocs and inlined the types just for simplicity, "..." refers to more code.

> I strongly suggest opening your IDE and following along with the code to avoid any confusion.

Following our example, let's explore the `Route` class.

```
<?php

namespace Illuminate\Support\Facades;

class Route extends Facade
{
    // ...

    protected static function getFacadeAccessor(): string
    {
        return 'router';
    }
}
```

There's not much here, just the `getFacadeAccessor()` method that returns the string `router`. Keeping this in mind, let's move to the parent class.

```
<?php

namespace Illuminate\Support\Facades;

use RuntimeException;
// ...

abstract class Facade
{
    // ...

    public static function __callStatic(string $method, array $args): mixed
    {
        $instance = static::getFacadeRoot();

        if (! $instance) {
            throw new RuntimeException('A facade root has not been set.');
        }

        return $instance->$method(...$args);
    }
}
```

Within the parent class, there are lots of methods, there isn't a `get()` method though. But there is an interesting one, the `__callStatic()` method. It's a *magic* method, invoked whenever an undefined static method, like `get()` in our case, is called. Therefore, our call `__callStatic('get', ['/', Closure()])` represents what we passed when invoking `Route::get()`, the route `/` and a `Closure()` that returns the welcome view.

When `__callStatic()` gets triggered, it first attempts to set a variable `$instance` by calling `getFacadeRoot()`, the `$instance` holds the actual class to which the call should be forwarded, let's take a closer look, it will make sense in a bit

```
// Facade.php

public static function getFacadeRoot()
{
    return static::resolveFacadeInstance(static::getFacadeAccessor());
}
```

Hey, look it is the `getFacadeAccessor()` from the child class `Route`, which we know returned the string `router`. This `router` string is then passed to `resolveFacadeInstance()`, which attempts to resolve it to a class, a sort of mapping that says "What class does this string represent?" Let's see.

```
// Facade.php

protected static function resolveFacadeInstance($name)
{
    if (isset(static::$resolvedInstance[$name])) {
        return static::$resolvedInstance[$name];
    }

    if (static::$app) {
        if (static::$cached) {
            return static::$resolvedInstance[$name] = static::$app[$name];
        }

        return static::$app[$name];
    }
}
```

It first checks if a static array, `$resolvedInstance`, has a value set with the given `$name` (which, again, is `router`). If it finds a match, it just returns that value. This is Laravel caching to optimize performance a little bit. This caching occurs within a single request. If this method is called multiple times with the same argument within the same request, it uses the cached value. Let's assume it's the initial call and proceed.

It then checks if `$app` is set, and `$app` is an instance of the application container

```
// Facade.php

protected static \Illuminate\Contracts\Foundation\Application $app;
```

If you're curious about what an application container is, think of it as a box where your classes are stored. When you need those classes, you simply reach into that box. Sometimes, this container performs a bit of magic. Even if the box is empty, and you reach to grab a class, it will get it for you. That's a topic for another article.

Now, you might wonder, "When is `$app` set?", because it needs to be, otherwise, we won't have our `$instance`. This application container gets set during our application's bootstrapping process. Let's take a quick look at the `\Illuminate\Foundation\Http\Kernel` class:

```
<?php

namespace Illuminate\Foundation\Http;

use Illuminate\Http\Request;
use Illuminate\Http\Response;
use Illuminate\Support\Facades\Facade;
use Illuminate\Contracts\Http\Kernel as KernelContract;
// ...

class Kernel implements KernelContract
{
    // ...

    protected $app;

    protected $bootstrappers = [
        \Illuminate\Foundation\Bootstrap\LoadEnvironmentVariables::class,
        \Illuminate\Foundation\Bootstrap\LoadConfiguration::class,
        \Illuminate\Foundation\Bootstrap\HandleExceptions::class,
        \Illuminate\Foundation\Bootstrap\RegisterFacades::class, // <- this guy
        \Illuminate\Foundation\Bootstrap\RegisterProviders::class,
        \Illuminate\Foundation\Bootstrap\BootProviders::class,
    ];

    public function bootstrap(): void
    {
        if (! $this->app->hasBeenBootstrapped()) {
            $this->app->bootstrapWith($this->bootstrappers());
        }
    }
}
```

When a request comes through, it's sent to the router. Just before that, the `bootstrap()` method is invoked, which uses the `bootstrappers` array to prepare the application. If you explore the `bootstrapWith()` method in the `\Illuminate\Foundation\Application` class, it iterates through these bootstrappers, calling their `bootstrap()` method.

For simplicity, let's just focus on `\Illuminate\Foundation\Bootstrap\RegisterFacades`, which we know contains a `bootstrap()` method that will be invoked in `bootstrapWith()`

```
<?php

namespace Illuminate\Foundation\Bootstrap;

use Illuminate\Contracts\Foundation\Application;
use Illuminate\Foundation\AliasLoader;
use Illuminate\Foundation\PackageManifest;
use Illuminate\Support\Facades\Facade;

class RegisterFacades
{
    // ...

    public function bootstrap(Application $app): void
    {
        Facade::clearResolvedInstances();

        Facade::setFacadeApplication($app); // Interested here

        AliasLoader::getInstance(array_merge(
            $app->make('config')->get('app.aliases', []),
            $app->make(PackageManifest::class)->aliases()
        ))->register();
    }
}
```

And there it is, we're setting the application container on the `Facade` class using the static method `setFacadeApplication().`

```
// RegisterFacades.php

public static function setFacadeApplication($app)
{
    static::$app = $app;
}
```

See, we assign the `$app` property that we're testing within `resolveFacadeInstance()`. This answers the question; let's continue.

```
// Facade.php

protected static function resolveFacadeInstance($name)
{
    if (isset(static::$resolvedInstance[$name])) {
        return static::$resolvedInstance[$name];
    }

    if (static::$app) {
        if (static::$cached) {
            return static::$resolvedInstance[$name] = static::$app[$name];
        }

        return static::$app[$name];
    }
}
```

We confirmed that `$app` is set during the application bootstrapping. The next step is to check whether the resolved i...