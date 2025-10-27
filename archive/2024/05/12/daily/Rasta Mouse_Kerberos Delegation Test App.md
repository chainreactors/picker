---
title: Kerberos Delegation Test App
url: https://rastamouse.me/kerberos-delegation-test-app/
source: Rasta Mouse
date: 2024-05-12
fetch_date: 2025-10-06T17:17:20.679462
---

# Kerberos Delegation Test App

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

11 May 2024

4 min read

# Kerberos Delegation Test App

I have been quietly working on some new Kerberos course content, and although it’s not complete yet, I wanted to take a small segue to write this post. My approach to tackling the content required capturing and decrypting legitimate Kerberos traffic on the wire, so that readers could understand the protocol at the packet level. This proved to be really worthwhile, as I uncovered some of [my own misconceptions](https://x.com/_RastaMouse/status/1788294382296207639) about Kerberos.

When explaining the concept of delegation, authors will often use the front-end web server / back-end server (typically SQL or file share) analogy, such as this example from [HackAndDo](https://twitter.com/HackAndDo).

![](https://i0.wp.com/en.hackndo.com/assets/uploads/2019/02/webfsuser.png?w=1200&ssl=1)

Image Credit: [Kerberos Delegation](https://en.hackndo.com/constrained-unconstrained-delegation/)

Instead of just talking about this scenario “in theory”, I wanted to build an actual, working application that would do this for real, so that I could capture and analyse the packets. I initially spent quite a bit of time trying to figure out how to use IIS and ASPX for this, but most of what I read online was for older versions and nothing really worked for me (alas). Instead, I turned to trusty ASP.NET Core, and it turned out to be wayyyy easier than I expected.

I’m providing this little write-up in the hope that it’ll be useful to others who want to setup something similar in their lab. Note that even though ASP.NET Core is cross-platform, this app will only function on Windows.

I created an ASP.NET Core Web API application, but you could use any project type such as Blazor or Razor Pages. You will then want to add the [Negotiate](https://www.nuget.org/packages/Microsoft.AspNetCore.Authentication.Negotiate) NuGet package, which adds Negotiate, Kerberos, and NTLM authentication handlers.

The way I had my lab setup is with the delegation configured on the web server computer account. The MS documentation states that this package can be used with [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel) (which is the default web server platform built into ASP.NET Core), but this requires [User Mode](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode#user-mode) authentication, and that in turn requires delegation be set on a domain user account and not a computer account. However, [HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys) supports [Kernel Mode](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode#kernel-mode) authentication, so that’s what I went with. HTTP.sys only runs on Windows, hence the limitation of this app.

Here, I am adding the authentication services and configuring HTTP.sys to use the `Negotiate` scheme. This allows a client and server to negotiate between Kerberos and NTLM. You can also set this to Kerberos or NTLM explicitly depending on your needs (helpful when testing protocol transition).

```
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddAuthentication(HttpSysDefaults.AuthenticationScheme);
builder.Services.AddAuthorization();

builder.WebHost.UseHttpSys(opts =>
{
    // change scheme as desired
    opts.Authentication.Schemes = AuthenticationSchemes.Negotiate;
    opts.Authentication.AllowAnonymous = false;
});
```

Where you wire up the functional bits of code depends on which type of project you’re using. Since mine is an API project, I’m using [FastEndpoints](https://fast-endpoints.com/). Consider the following example.

```
public override void Configure()
{
    Get("/whoami");
}

public override Task HandleAsync(CancellationToken ct)
{
    var user = (WindowsIdentity)HttpContext.User.Identity!;

    WindowsIdentity.RunImpersonated(user.AccessToken, () =>
    {
        var impersonated = WindowsIdentity.GetCurrent();

        Response = new WhoAmIRecord(
            impersonated.Name,
            impersonated.ImpersonationLevel.ToString());
    });

    return Task.CompletedTask;
}
```

All of the complicated negotiation and authentication stuff happens behind the scenes in ASP.NET Core, so we don’t have to deal with it directly. We can just grab the authenticated user’s identity from the `HttpContext` property of the incoming HTTP request. The `RunImpersonated` method can then be used, which takes in the `AccessToken` of the authenticated user, and the code executed inside the function delegate will be as that user. For this simple `/whoami` endpoint, I’m just echo’ing back the impersonated username.

I can run the app as the local administrator user on the web server.

```
C:\Users\Administrator\Desktop\KerbApp>whoami
web\administrator

C:\Users\Administrator\Desktop\KerbApp>KerbApp.exe --urls http://*:80
[08:51:17 INF] Registered 5 endpoints in 79 milliseconds.
[08:51:17 INF] No validators found in the system!
[08:51:17 INF] Now listening on: http://*:80/
[08:51:17 INF] Application started. Press Ctrl+C to shut down.
[08:51:17 INF] Hosting environment: Production
[08:51:17 INF] Content root path: C:\Users\Administrator\Desktop\KerbApp
```

And when I hit the endpoint as a domain user, I see my own username being returned.

```
PS C:\Users\hades> $resp = Invoke-WebRequest -Uri http://web.contoso.com/whoami -UseDefaultCredentials
PS C:\Users\hades> $resp.Content
{"username":"CONTOSO\\hades","impersonationLevel":"Impersonation"}
```

The exchange between the client, KDC, and web server looks like this:

![](https://i0.wp.com/rastamouse.me/wp-content/uploads/2024/05/image-3-1024x178.png?resize=1024%2C178&ssl=1)

Adding interaction with a back-end file server is also really simple. Here’s an example endpoint to list filenames from a share.

```
public override void Configure()
{
    Get("/files");
}

public override Task HandleAsync(CancellationToken ct)
{
    var user = (WindowsIdentity)HttpContext.User.Identity!;

    WindowsIdentity.RunImpersonated(user.AccessToken, () =>
    {
        Response = Directory.GetFiles(_config["SharePath"]!);
    });

    return Task.CompletedTask;
}
```

```
PS C:\Users\hades> $resp = Invoke-WebRequest -Uri http://web.contoso.com/files -UseDefaultCredentials
PS C:\Users\hades> $resp.Content
["\\\\fs.contoso.com\\demo\\file1.txt","\\\\fs.contoso.com\\demo\\file2.txt"]
```

Here’s a capture of the TGS-REQ from the web server to the KDC. It shows how it sends the hades user’s HTTP service ticket to request a CIFS service ticket on their behalf (S4U2proxy).

![](https://i0.wp.com/rastamouse.me/wp-content/uploads/2024/05/image-2-984x1024.png?resize=984%2C1024&ssl=1)

A complete copy of my source code can be found [here](https://github.com/rasta-mouse/KerbApp).

### Published by:

[![Rasta Mouse](https://www.gravatar.com/avatar/2b44f5ca5458931c49e1fa57da6705c1?s=250&r=x&d=mp)](/author/rasta/ "Rasta Mouse")

Rasta Mouse © 2025

* [Sign up](#/portal/)

[Powered by Ghost](https://ghost.org/)