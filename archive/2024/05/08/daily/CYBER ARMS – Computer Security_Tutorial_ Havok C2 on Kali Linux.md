---
title: Tutorial: Havok C2 on Kali Linux
url: https://cyberarms.wordpress.com/2024/05/07/tutorial-havok-c2-on-kali-linux/
source: CYBER ARMS – Computer Security
date: 2024-05-08
fetch_date: 2025-10-06T17:17:53.546518
---

# Tutorial: Havok C2 on Kali Linux

[Skip to content](#content)

[CYBER ARMS – Computer Security](https://cyberarms.wordpress.com/)

CyberSecurity Training and Offensive Security News

[![CYBER ARMS – Computer Security](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/cyberarms-security-1.jpg)](https://cyberarms.wordpress.com/)

# Tutorial: Havok C2 on Kali Linux

![](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havoc-c2-tutorial.jpg?w=1152)

This is a sneak peak preview of part of a chapter from my new book – “[Mastering Command and Control: Exploring C2 Frameworks using Kali Linux](https://www.amazon.com/Mastering-Command-Control-Exploring-Frameworks/dp/B0D1J6R6R8/)“

**Tool GitHub**: <https://github.com/HavocFramework/Havoc>
**Tool Wiki**: <https://havocframework.com/docs/welcome>

Havoc is a GUI driven multi-user Command and Control (C2) framework written in Golang, C and ASM. It is easy to use and has many great features making it a great option for Red Teams. It is also quickly becoming the “C2” of choice in online cyber-attacks, so it’s good for Blue Teams to be familiar with it too.

## Havoc**C2 – Installing**

Havoc in now included in the repositories of the newest version of Kali Linux. It can be installed by just entering the tool name.

Open a Kali Terminal and enter the following commands:

* ***sudo apt update***
* ***sudo apt upgrade***
* ***havoc*** (this will prompt you to install it)
* ***cd /usr/share/havoc***

[![](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-kali-linux.jpg?w=496)](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-kali-linux.jpg)

You need to run Havoc from the install directory as it uses a config file (havoc.yaotl) in its profile directory. There are a few settings you can change in the config file, including Host, Port, Users and Passwords. Though I will just use the default config for this chapter.

Havoc is made up of two parts, the Team Server and a Client. You need to have both running in separate terminal windows.

## Havoc**C2 – Start the Team Server**

* Enter, “***havoc server –profile ./profiles/havoc.yaotl -v***”

“-v” starts Havoc in verbose mode. If you want debug information, you can also add, “–debug”

[![](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-kali-linux-2.jpg?w=1024)](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-kali-linux-2.jpg)

## Havoc**C2 – Start the Client**

Now we need to start the client, or the user interface to Havoc.

* Open a Second Terminal
* Navigate to “*/usr/share/havoc*”
* Enter, “***havoc client***”

[![](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-kali-linux-3.jpg?w=1024)](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-kali-linux-3.jpg)

* Click “*New Profile*”
* Then click “*Connect*”

[![](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-tutorial-4.jpg?w=504)](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-tutorial-4.jpg)

You could also use a name and password from profile located at – *profiles/havoc.yaotl*

## **Havoc C2 – Create A Listener**

First up, we need to create a Listener. A Listener looks or listens for incoming shells when a target runs a payload, and creates the connection.

* Click “*View*” from the top menu
* Then, “*Listeners*”

[![](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-tutorial-5.jpg?w=347)](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-tutorial-5.jpg)

* Then, at the bottom of the screen click, “*Add*”

Add a name and select a Payload type. I just used HTTP. Lastly, set the Host IP address and Port

[![](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-tutorial-6.jpg?w=560)](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-tutorial-6.jpg)

Click “Save”

Havoc will save and then start the listener.

[![](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-tutorial-7.jpg?w=579)](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-tutorial-7.jpg)

You can see the status of the Havoc in the Event Viewer window.

## Havoc **C2 – Ge****nerating****a Payload**

Next, we need to make a payload or shellcode for the target to run.

* Click, “*Attack*” from the top menu and then, “*Payload*”

[![](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-tutorial-kali.jpg?w=568)](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-tutorial-kali.jpg)

Havoc gives you several options. We will just take the defaults and chose a Windows Executable for the payload type. You should see your new listener listed. If not, select it from the drop-down box. Make any changes you want, I made none, then click “*Generate*”. Havoc will create our attack payload. It will take a few seconds for it to generate, it will then prompt you to save it.

Now, all you need to do is Copy and Run this file on a target Windows system.

[![](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-tutorial-9-1.jpg?w=638)](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-tutorial-9-1.jpg)

And we have a live session!

[![](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-tutorial-10.jpg?w=817)](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/havok-c2-tutorial-10.jpg)

This is just the begining, in the full chapter we delve deeper into controlling the remote session.

***Read more on Havok and on 11 other C2s in my new book!***

[![](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/front-cover.jpg?w=830)](https://www.amazon.com/Mastering-Command-Control-Exploring-Frameworks/dp/B0D1J6R6R8/)

“[Mastering Command and Control](https://www.amazon.com/Mastering-Command-Control-Exploring-Frameworks/dp/B0D1J6R6R8/)” available on Amazon.com

### Share this:

* [Click to share on X (Opens in new window)
  X](https://cyberarms.wordpress.com/2024/05/07/tutorial-havok-c2-on-kali-linux/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://cyberarms.wordpress.com/2024/05/07/tutorial-havok-c2-on-kali-linux/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://cyberarms.wordpress.com/2024/05/07/tutorial-havok-c2-on-kali-linux/?share=linkedin)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://cyberarms.wordpress.com/2024/05/07/tutorial-havok-c2-on-kali-linux/?share=pinterest)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://cyberarms.wordpress.com/2024/05/07/tutorial-havok-c2-on-kali-linux/?share=reddit)

Like Loading...

### *Related*

![Unknown's avatar](https://0.gravatar.com/avatar/f0b8f7b136ca9027fe703cd7f8b882e83849e60171ec3983255fc21bbad6bd8f?s=49&d=https%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D49&r=G)Author  [CyberArms](https://cyberarms.wordpress.com/author/cyberarms/)Posted on [May 7, 2024](https://cyberarms.wordpress.com/2024/05/07/tutorial-havok-c2-on-kali-linux/)Categories [C2 Command and Control](https://cyberarms.wordpress.com/category/c2-command-and-control/)Tags [Computer Security](https://cyberarms.wordpress.com/tag/computer-security/), [Cyber Crime](https://cyberarms.wordpress.com/tag/cyber-crime/), [Cyber Security](https://cyberarms.wordpress.com/tag/cyber-security/), [Cyber War](https://cyberarms.wordpress.com/tag/cyber-war/), [Cybersecurity](https://cyberarms.wordpress.com/tag/cybersecurity/), [Hacking](https://cyberarms.wordpress.com/tag/hacking/), [Kali Linux](https://cyberarms.wordpress.com/tag/kali-linux/), [Linux](https://cyberarms.wordpress.com/tag/linux/), [Network Security](https://cyberarms.wordpress.com/tag/network-security/), [Pentesting](https://cyberarms.wordpress.com/tag/pentesting/), [Security](https://cyberarms.wordpress.com/tag/security/), [Tutorial](https://cyberarms.wordpress.com/tag/tutorial/), [Windows](https://cyberarms.wordpress.com/tag/windows/...