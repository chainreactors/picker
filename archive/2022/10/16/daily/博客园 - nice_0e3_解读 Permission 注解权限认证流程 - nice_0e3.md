---
title: 解读 Permission 注解权限认证流程 - nice_0e3
url: https://www.cnblogs.com/nice0e3/p/16794557.html
source: 博客园 - nice_0e3
date: 2022-10-16
fetch_date: 2025-10-03T20:02:12.882530
---

# 解读 Permission 注解权限认证流程 - nice_0e3

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

# [解读 Permission 注解权限认证流程](https://www.cnblogs.com/nice0e3/p/16794557.html "发布于 2022-10-15 17:03")

# 解读 Permission 注解权限认证流程

**Shiro 注解授权简介**

授权即访问控制，它将判断用户在应用程序中对资源是否拥有相应的访问权限。 如判断一个用户有查看页面的权限，编辑数据的权限，拥有某一按钮的权限等等。

```
@RequiresPermissions({"xxx:model:edit"})
   @RequestMapping({"delete"})
   public String delete(String id) {
      this.actModelService.delete(id)
      return "redirect:" + "delete";
   }
```

使用`@RequiresPermissions`注解必须使用以下配置

```
	<!-- AOP式方法级权限检查  -->
	<bean class="org.springframework.aop.framework.autoproxy.DefaultAdvisorAutoProxyCreator" depends-on="lifecycleBeanPostProcessor">
		<property name="proxyTargetClass" value="true" />
	</bean>
	<bean class="org.apache.shiro.spring.security.interceptor.AuthorizationAttributeSourceAdvisor">
    	<property name="securityManager" ref="securityManager"/>
	</bean>

<bean id="securityManager" class="org.apache.shiro.web.mgt.DefaultWebSecurityManager">
		<property name="realm" ref="systemAuthorizingRealm" />
		<property name="sessionManager" ref="sessionManager" />
		<property name="cacheManager" ref="shiroCacheManager" />
	</bean>
```

通过Spring的`DefaultAdvisorAutoProxyCreator` 自动代理底层也是aop,来到

`org.apache.shiro.spring.security.interceptor.AuthorizationAttributeSourceAdvisor`

![image-20221015113319240](https://img2022.cnblogs.com/blog/1993669/202210/1993669-20221015170212892-427036748.png)

```
package org.apache.shiro.spring.security.interceptor;

public class AuthorizationAttributeSourceAdvisor extends StaticMethodMatcherPointcutAdvisor {
    private static final Logger log = LoggerFactory.getLogger(AuthorizationAttributeSourceAdvisor.class);
    private static final Class<? extends Annotation>[] AUTHZ_ANNOTATION_CLASSES = new Class[]{RequiresPermissions.class, RequiresRoles.class, RequiresUser.class, RequiresGuest.class, RequiresAuthentication.class};
    protected SecurityManager securityManager = null;

    public AuthorizationAttributeSourceAdvisor() {
        this.setAdvice(new AopAllianceAnnotationsAuthorizingMethodInterceptor());
    }

    public SecurityManager getSecurityManager() {
        return this.securityManager;
    }

    public void setSecurityManager(SecurityManager securityManager) {
        this.securityManager = securityManager;
    }

    public boolean matches(Method method, Class targetClass) {
        Method m = method;
        if (this.isAuthzAnnotationPresent(method)) {
            return true;
        } else {
            if (targetClass != null) {
                try {
                    m = targetClass.getMethod(m.getName(), m.getParameterTypes());
                    if (this.isAuthzAnnotationPresent(m)) {
                        return true;
                    }
                } catch (NoSuchMethodException var5) {
                }
            }

            return false;
        }
    }

 // ...

        return false;
    }
}
```

matches方法来判断是否切入，true为切入，false不切入。

`this.setAdvice(new AopAllianceAnnotationsAuthorizingMethodInterceptor());`

这里设置了增强advice，为`AopAllianceAnnotationsAuthorizingMethodInterceptor`

![image-20221015122827996](https://img2022.cnblogs.com/blog/1993669/202210/1993669-20221015170223717-932809927.png)

`org.apache.shiro.spring.security.interceptor.AopAllianceAnnotationsAuthorizingMethodInterceptor#invoke`

```
 public Object invoke(org.aopalliance.intercept.MethodInvocation methodInvocation) throws Throwable {
        MethodInvocation mi = this.createMethodInvocation(methodInvocation);
        return super.invoke(mi);
    }
```

![image-20221015123139122](https://img2022.cnblogs.com/blog/1993669/202210/1993669-20221015170231713-899362248.png)

![image-20221015123046808](https://img2022.cnblogs.com/blog/1993669/202210/1993669-20221015170242176-1338341104.png)

<https://blog.csdn.net/chaitoudaren/article/details/105278868>

来到

`org.apache.shiro.authz.aop.AnnotationsAuthorizingMethodInterceptor#assertAuthorized`

```
protected void assertAuthorized(MethodInvocation methodInvocation) throws AuthorizationException {
        Collection<AuthorizingAnnotationMethodInterceptor> aamis = this.getMethodInterceptors();
        if (aamis != null && !aamis.isEmpty()) {
            Iterator var3 = aamis.iterator();

            while(var3.hasNext()) {
                AuthorizingAnnotationMethodInterceptor aami = (AuthorizingAnnotationMethodInterceptor)var3.next();
                if (aami.supports(methodInvocation)) {
                    aami.assertAuthorized(methodInvocation);
                }
```

![image-20221015125049643](https://img2022.cnblogs.com/blog/1993669/202210/1993669-20221015170249206-208535608.png)

获取方法拦截器，即shiro鉴权用到的五个注解

* **RequiresAuthentication:**

  > 使用该注解标注的类，实例，方法在访问或调用时，当前Subject必须在当前session中已经过认证。
* **RequiresGuest:**

  > 使用该注解标注的类，实例，方法在访问或调用时，当前Subject可以是“gust”身份，不需要经过认证或者在原先的session中存在记录。
* **RequiresPermissions:**

  > 当前Subject需要拥有某些特定的权限时，才能执行被该注解标注的方法。如果当前Subject不具有这样的权限，则方法不会被执行。
* **RequiresRoles:**

  > 当前Subject必须拥有所有指定的角色时，才能访问被该注解标注的方法。如果当天Subject不同时拥有所有指定角色，则方法不会执行还会抛出AuthorizationException异常。
* **RequiresUser**

  > 当前Subject必须是应用的用户，才能访问或调用被该注解标注的类，实例，方法。

![image-20221015125455497](https://img2022.cnblogs.com/blog/1993669/202210/1993669-20221015170256224-266581988.png)

遍历这五个方法拦截器与请求的方法拦截器进行匹配，请求路由代码中用到的是RequiresPermissions。

然后调用`aami.assertAuthorized(methodInvocation);`进行认证。

```
 public void assertAuthorized(MethodInvocation mi) throws AuthorizationException {
        try {
            ((AuthorizingAnnotationHandler)this.getHandler()).assertAuthorized(this.getAnnotation(mi));
        } catch (AuthorizationException var3) {
            if (var3.getCause() == null) {
                var3.initCause(new AuthorizationException("Not authorized to invoke method: " + mi.getMethod()));
            }

            throw var3;
        }
```

来到`org.apache.shiro.authz.aop.PermissionAnnotationHandler#assertAuthorized`

`this.getAnnotationValue(a);`方法获取`@RequiresPermissions`内容，即权限标识

调用 `this.getSubject();`获取身份信息

先来看看他是如何获取到身份信息的

```
// org.apache.shiro.aop.AnnotationHandler#getSubject

protected Subject getSubject() {
    return SecurityUtils.getSubject();
}

//org.apache.shiro.SecurityUtils#getSubject
 public static Subject getSubject() {
        Subject subject = ThreadContext.getSubject();
        if (subject == null) {
            subject = (new Subject.Builder()).buildSubject();
          ...