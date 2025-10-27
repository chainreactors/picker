---
title: Persistence – Windows Setup Script
url: http://pentestlab.blog/2024/02/05/persistence-windows-setup-script/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-03
fetch_date: 2025-10-06T22:28:28.532483
---

# Persistence – Windows Setup Script

[Skip to content](#content)

[Penetration Testing Lab](https://pentestlab.blog/)

Offensive Techniques & Methodologies

Menu

* [Methodologies](https://pentestlab.blog/methodologies/)
  + [Red Teaming](https://pentestlab.blog/methodologies/red-teaming/)
    - [Credential Access](https://pentestlab.blog/methodologies/red-teaming/credential-access/)
    - [Persistence](https://pentestlab.blog/methodologies/red-teaming/persistence/)
* [Resources](https://pentestlab.blog/resources/)
  + [Papers](https://pentestlab.blog/resources/papers/)
    - [Web Application](https://pentestlab.blog/resources/papers/web-application/)
  + [Presentations](https://pentestlab.blog/resources/presentations/)
    - [Defcon](https://pentestlab.blog/resources/presentations/defcon/)
    - [DerbyCon](https://pentestlab.blog/resources/presentations/derbycon/)
    - [Tools](https://pentestlab.blog/resources/presentations/tools/)
  + [Videos](https://pentestlab.blog/resources/videos/)
    - [BSides](https://pentestlab.blog/resources/videos/bsides/)
    - [Defcon](https://pentestlab.blog/resources/videos/defcon/)
    - [DerbyCon](https://pentestlab.blog/resources/videos/derbycon/)
    - [Hack In Paris](https://pentestlab.blog/resources/videos/hack-in-paris/)
* [Contact](https://pentestlab.blog/contact-the-lab/)
  + [About Us](https://pentestlab.blog/contact-the-lab/about-us/)

Posted on [February 5, 2024January 26, 2024](https://pentestlab.blog/2024/02/05/persistence-windows-setup-script/)

# Persistence – Windows Setup Script

![Unknown's avatar](https://0.gravatar.com/avatar/9161b274d6d350683293f1e03d228985ac0ff6ac6c89353f4b6bd1a7bc69daf4?s=32&d=identicon&r=G) by [Administrator](https://pentestlab.blog/author/worm1984/).In [Persistence](https://pentestlab.blog/category/red-team/persistence/).[Leave a Comment on Persistence – Windows Setup Script](https://pentestlab.blog/2024/02/05/persistence-windows-setup-script/#respond)

When the Windows Operating system is installed via a clean installation or via an upgrade, the Windows Setup binary is executed. The Windows setup allows custom scripts to be executed such as the *SetupComplete.cmd* and *ErrorHandler.cmd* to enable the installation of applications or the execution of other tasks during or after the Windows setup process is completed. These scripts are stored in the following location:

```
%WINDIR%\Setup\Scripts\SetupComplete.cmd
%WINDIR%\Setup\Scripts\ErrorHandler.cmd
```

Using the *ErrorHandler.cmd* script it is possible to execute arbitrary code when the Windows operating system is upgraded. Even though it could be considered as an unconventional tactic, it could be combined with scheduled tasks for example to run Windows Setup and establish persistence. The following code can be used as a proof of concept of code execution that will display a message box when the Windows Setup binary is initiated:

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Windows_setup1
{
    internal static class Program
    {
        [STAThread]
        static void Main()
        {
            string message = "Visit pentestlab.blog";
            string title = "Pentestlaboratories";
            MessageBox.Show(message, title);
        }
    }
}
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/windows-setup-script-message-box-code.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/01/windows-setup-script-message-box-code.png)

Windows Setup Script – Message Box Code

Since the Windows Setup will look during execution and when an error is caused in the setup process for the presence of *ErrorHandler.cmd* inside the *Scripts* folder, it is possible to use this script to execute arbitrary code.

[![](https://pentestlab.blog/wp-content/uploads/2024/01/windows-setup-script-folder.png?w=966)](https://pentestlab.blog/wp-content/uploads/2024/01/windows-setup-script-folder.png)

Windows Setup Script Path

Running the *setup.exe* will cause an error which as a result will force the execution of *ErrorHandler.cmd* script.

[![](https://pentestlab.blog/wp-content/uploads/2024/01/windows-setup-script-messagebox.png?w=858)](https://pentestlab.blog/wp-content/uploads/2024/01/windows-setup-script-messagebox.png)

Windows Setup Script – Message Box

Replacing the message box executable with an implant will allow a command and control session to be established.

[![](https://pentestlab.blog/wp-content/uploads/2024/01/windows-setup-script-c2.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/01/windows-setup-script-c2.png)

Windows Setup Script – C2

The process tree of the implant is specified below:

```
Setup.exe --> cmd.exe --> demon.x64.exe
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/windows-setup-script-process-tree.png?w=780)](https://pentestlab.blog/wp-content/uploads/2024/01/windows-setup-script-process-tree.png)

Windows Setup Script – Process Tree

## References

1. <https://www.hexacorn.com/blog/2022/01/16/beyond-good-ol-run-key-part-135/>
2. <https://cocomelonc.github.io/persistence/2023/07/16/malware-pers-22.html>

### Rate this:

### Share this:

* [Click to share on X (Opens in new window)
  X](https://pentestlab.blog/2024/02/05/persistence-windows-setup-script/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://pentestlab.blog/2024/02/05/persistence-windows-setup-script/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://pentestlab.blog/2024/02/05/persistence-windows-setup-script/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://pentestlab.blog/2024/02/05/persistence-windows-setup-script/?share=reddit)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://pentestlab.blog/2024/02/05/persistence-windows-setup-script/?share=mastodon)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://pentestlab.blog/2024/02/05/persistence-windows-setup-script/?share=tumblr)
* [Click to share on WhatsApp (Opens in new window)
  WhatsApp](https://pentestlab.blog/2024/02/05/persistence-windows-setup-script/?share=jetpack-whatsapp)
* [Click to share on Telegram (Opens in new window)
  Telegram](https://pentestlab.blog/2024/02/05/persistence-windows-setup-script/?share=telegram)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://pentestlab.blog/2024/02/05/persistence-windows-setup-script/?share=pinterest)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://pentestlab.blog/2024/02/05/persistence-windows-setup-script/?share=pocket)
* Click to email a link to a friend (Opens in new window)
  Email

Like Loading...

### *Related*

[C2](https://pentestlab.blog/tag/c2/)[Persistence](https://pentestlab.blog/tag/persistence/)

### Leave a comment [Cancel reply](/2024/02/05/persistence-windows-setup-script/#respond)

Δ

## Post navigation

[Previous Previous post: Persistence – Disk Clean-up](https://pentestlab.blog/2024/01/29/persistence-disk-clean-up/)

[Next Next post: AS-REP Roasting](https://pentestlab.blog/2024/02/20/as-rep-roasting/)

## Support pentestlab.blog

Pentestlab.blog has a long term history in the offensive security space by delivering content for over a decade. Articles discussed in pentestlab.blog have been used by cyber security professionals and red teamers for their day to day job and by students and lecturers in academia. If you have benefit by the content all these years and you would like to support us on the maintenance costs please consider a donation.

One-Time

Monthly

Yearly

#### Make a one-time donation

#### Make a monthly donation

#### Make a yearly donation

Choose an amount

£5.00

£15.00

£100.00

£5.00

£15.00

£100.00

£5.00

£15.00

£100.00

Or enter a custom amount

£

---

Your contribution is appreciated.

Your contribution is appreciated.

Your contribution is appreciated.

[Donate](https://subscribe.wordpress.com/memb...