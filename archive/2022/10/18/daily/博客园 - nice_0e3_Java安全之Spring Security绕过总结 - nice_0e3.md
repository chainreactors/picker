---
title: Java安全之Spring Security绕过总结 - nice_0e3
url: https://www.cnblogs.com/nice0e3/p/16798843.html
source: 博客园 - nice_0e3
date: 2022-10-18
fetch_date: 2025-10-03T20:07:27.281567
---

# Java安全之Spring Security绕过总结 - nice_0e3

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/nice0e3/)

# [nice\_0e3](https://www.cnblogs.com/nice0e3)

## 理想与热爱

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/nice0e3/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/nice_0e3)
* 订阅
* [管理](https://i.cnblogs.com/)

# [Java安全之Spring Security绕过总结](https://www.cnblogs.com/nice0e3/p/16798843.html "发布于 2022-10-17 12:57")

# Java安全之Spring Security绕过总结

## 前言

bypass！bypass！bypass！

## SpringSecurit使用

### 使用

```
@Configuration
@EnableWebSecurity //启用Web安全功能
public class AuthConfig {
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
						http.authorizeRequests() // 开启 HttpSecurity 配置
            .antMatchers("/admin/**").hasRole("ADMIN") // admin/** 模式URL必须具备ADMIN角色
            .antMatchers("/user/**").access("hasAnyRole('ADMIN','USER')") // 该模式需要ADMIN或USER角色
            .antMatchers("/db/**").access("hasRole('ADMIN') and hasRole('DBA')") // 需ADMIN和DBA角色
            .anyRequest().authenticated() // 用户访问其它URL都必须认证后访问（登录后访问）
            .and().formLogin().loginProcessingUrl("/login").permitAll() // 开启表单登录并配置登录接口
            .and().csrf().disable(); // 关闭csrf

        return http.build();
    }
```

| 方法 | 描述 |
| --- | --- |
| access(String) | 如果给定的SpEL表达式计算结果为true，就允许访问 |
| anonymous() | 允许匿名用户访问 |
| authenticated() | 允许认证过的用户访问 |
| denyAll() | 无条件拒绝所有访问 |
| fullyAuthenticated() | 如果用户是完整认证的话（不是通过Remember-me功能认证的），就允许访问 |
| hasAnyAuthority(String…) | 如果用户具备给定权限中的某一个的话，就允许访问 |
| hasAnyRole(String…) | 如果用户具备给定角色中的某一个的话，就允许访问 |
| hasAuthority(String) | 如果用户具备给定权限的话，就允许访问 |
| hasIpAddress(String) | 如果请求来自给定IP地址的话，就允许访问 |
| hasRole(String) | 如果用户具备给定角色的话，就允许访问 |
| not() | 对其他访问方法的结果求反 |
| permitAll() | 无条件允许访问 |
| rememberMe() | 如果用户是通过Remember-me功能认证的，就允许访问 |

​ 也可以通过集成`WebSecurityConfigurerAdapter`类的方式来configure()方法来制定Web安全的细节。

1、configure(WebSecurity)：通过重载该方法，可配置Spring Security的Filter链。

2、configure(HttpSecurity)：通过重载该方法，可配置如何通过拦截器保护请求。

Spring Security 支持的所有SpEL表达式如下：

| 安全表达式 | 计算结果 |
| --- | --- |
| authentication | 用户认证对象 |
| denyAll | 结果始终为false |
| hasAnyRole(list of roles) | 如果用户被授权指定的任意权限，结果为true |
| hasRole(role) | 如果用户被授予了指定的权限，结果 为true |
| hasIpAddress(IP Adress) | 用户地址 |
| isAnonymous() | 是否为匿名用户 |
| isAuthenticated() | 不是匿名用户 |
| isFullyAuthenticated | 不是匿名也不是remember-me认证 |
| isRemberMe() | remember-me认证 |
| permitAll | 始终true |
| principal | 用户主要信息对象 |

​

configure(AuthenticationManagerBuilder)：通过重载该方法，可配置user-detail（用户详细信息）服务。

| 方法 | 描述 |
| --- | --- |
| accountExpired(boolean) | 定义账号是否已经过期 |
| accountLocked(boolean) | 定义账号是否已经锁定 |
| and() | 用来连接配置 |
| authorities(GrantedAuthority…) | 授予某个用户一项或多项权限 |
| authorities(List) | 授予某个用户一项或多项权限 |
| authorities(String…) | 授予某个用户一项或多项权限 |
| credentialsExpired(boolean) | 定义凭证是否已经过期 |
| disabled(boolean) | 定义账号是否已被禁用 |
| password(String) | 定义用户的密码 |
| roles(String…) | 授予某个用户一项或多项角色 |

#### 用户存储方式

1、使用基于内存的用户存储：通过inMemoryAuthentication()方法，我们可以启用、配置并任意填充基于内存的用户存储。并且，我们可以调用withUser()方法为内存用户存储添加新的用户，这个方法的参数是username。withUser()方法返回的是UserDetailsManagerConfigurer.UserDetailsBuilder，这个对象提供了多个进一步配置用户的方法，包括设置用户密码的password()方法以及为给定用户授予一个或多个角色权限的roles()方法。需要注意的是，roles()方法是authorities()方法的简写形式。roles()方法所给定的值都会添加一个ROLE\_前缀，并将其作为权限授予给用户。因此上诉代码用户具有的权限为：ROLE\_USER,ROLE\_ADMIN。而借助passwordEncoder()方法来指定一个密码转码器（encoder），我们可以对用户密码进行加密存储。

```
@Configuration
@EnableWebSecurity //启用Web安全功能
public class AuthConfig {
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
						http.authorizeRequests() // 开启 HttpSecurity 配置
            .antMatchers("/admin/**").hasRole("ADMIN") // admin/** 模式URL必须具备ADMIN角色
            .antMatchers("/user/**").access("hasAnyRole('ADMIN','USER')") // 该模式需要ADMIN或USER角色
            .antMatchers("/db/**").access("hasRole('ADMIN') and hasRole('DBA')") // 需ADMIN和DBA角色
            .anyRequest().authenticated() // 用户访问其它URL都必须认证后访问（登录后访问）
            .and().formLogin().loginProcessingUrl("/login").permitAll() // 开启表单登录并配置登录接口
            .and().csrf().disable(); // 关闭csrf

        return http.build();

@Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.inMemoryAuthentication()
        .withUser("root").password("123").roles("ADMIN","DBA")
        .and()
        .withUser("admin").password("123").roles("ADMIN","USER")
        .and()
        .withUser("xxx").password("123").roles("USER");
    }
          }
```

2、基于数据库表进行认证：用户数据通常会存储在关系型数据库中，并通过JDBC进行访问。为了配置Spring Security使用以JDBC为支撑的用户存储，我们可以使用jdbcAuthentication()方法，并配置他的DataSource，这样的话，就能访问关系型数据库了。

3、基于LDAP进行认证：为了让Spring Security使用基于LDAP的认证，我们可以使用ldapAuthentication()方法。

```
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    // 配置 user-detail 服务
    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
    	// 基于 LDAP 配置认证
        auth.ldapAuthentication()
                .userSearchBase("ou=people")
                .userSearchFilter("(uid={0})")
                .groupSearchBase("ou=groups")
                .groupSearchFilter("member={0}")
                .passwordCompare()
                .passwordAttribute("password")
                .passwordEncoder(new BCryptPasswordEncoder());
    }
}
```

使用远程ldap

```
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.ldapAuthentication()
                .userSearchBase("ou=people")
                .userSearchFilter("(uid={0})")
                .groupSearchBase("ou=groups")
                .groupSearchFilter("member={0}")
                // 返回一个ContextSourceBuilder 对象
                .contextSource()
                // 指定远程 LDAP 服务器 的 地址
                .url("ldap://xxx.com:389/dc=xxx,dc=com");

    }
}
```

```
ldapAuthentication()：表示，基于LDAP的认证。
userSearchBase()：为查找用户提供基础查询
userSearchFilter()：提供过滤条件，用于搜索用户。
groupSearchBase()：为查找组指定了基础查询。
groupSearchFilter()：提供过滤条件，用于组。
passwordCompare()：希望通过 密码比对 进行认证。
passwordAttribute()：指定 密码 保存的属性名字，默认：userPassword。
passwordEncoder()：指定密码转换器。
```

### hasRole 和 hasAuthority

```
http.authorizeRequests()
        .antMatchers("/admin/**").hasAuthority("admin")
        .antMatchers("/user/**").hasAuthority("user")
        .anyRequest().authenticated()
```

和

```
http.authorizeRequests()
        .antMatchers("/admin/**").hasRole("admin")
        .antMatchers("/user/**").hasRole("user")
        .anyRequest().authenticated()
```

实际上这两个的效果都是一样的

### antMatchers 配置认证绕过

```
package pe...