---
title: Espanso: Text Replacement, the Easy Way
url: https://www.blackhillsinfosec.com/espanso-text-replacement/
source: Black Hills Information Security, Inc.
date: 2025-05-29
fetch_date: 2025-10-06T22:29:17.917285
---

# Espanso: Text Replacement, the Easy Way

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

28
May
2025

[Chris Sullo'](https://www.blackhillsinfosec.com/category/author/chris-sullo/), [General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/)
[espanso](https://www.blackhillsinfosec.com/tag/espanso/), [text expander](https://www.blackhillsinfosec.com/tag/text-expander/), [text replacement](https://www.blackhillsinfosec.com/tag/text-replacement/)

# [Espanso: Text Replacement, the Easy Way](https://www.blackhillsinfosec.com/espanso-text-replacement/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/Sullo-150x150.png)

| [Sullo](https://www.blackhillsinfosec.com/team/chris-sullo/)

*Chris has been working in security for 30 years, mainly doing penetration testing in both consulting and corporate environments. Chris is the author of the Nikto web scanner, founder of the RVAsec conference, and has been involved in many OSS projects and community efforts.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/espanso_header-1.png)

[Espanso](https://espanso.org/) is a powerful cross-platform and open-source text replacement (or text expander) tool. At a simple level: it replaces what you type with something else. For example, imagine typing three characters and having your full email address magically appear? Microsoft Word’s autocorrect and smart completion on phones can do a few of these things, but with Espanso, it can be quite powerful when combined with advanced features such as running shell commands.

This blog focuses on using Espanso on Linux (shell commands) for the purposes of assisting with a penetration tester’s common tasks, although it can be used for just about anything.

### Why Use a Text Expander?

While some of our work might become automated using LLMs, a lot of grunt work will never die. Sending emails, writing commands, getting your external IP address—heck, even typing your phone number or mailing address—are an inefficient waste of time. In addition, a text expander will cut down on errors from typos and reduce the overall number of mistakes.

### Installation

Espanso has installation packages for Windows, macOS, and Linux [on their website](https://espanso.org/install/). It can also be installed manually using the [source code located on GitHub](https://github.com/espanso/espanso). After installation, the program uses a configuration file and a match file; both are YAML and easily updated for your needs.

By default, Espanso doesn’t need much *configuration* to operate successfully. The matches are where the money is, so to speak.

### Match & Replace

The base.yaml file, located in the Espanso config directory, contains the match-and-replace rules. You can also add your own YAML files to make management of the rules easier.

The project’s [extensive documentation](https://espanso.org/docs/get-started/) explains how to locate this file on your system, but Espanso itself contains a handy shortcut which will open the file with your default editor. The command below will open the file for editing:

```
espanso edit
```

The basic idea is that it will match a text string that you type, known as a trigger, and replace it with something else. A simple example of this is:

```
- trigger: ":me"
    replace: "Chris"
```

In almost any location on my system, if I type `:me` then Espanso will replace it with `Chris`.

As in the default Espanso examples, I tend to use a colon before triggers as it’s not a common pattern in English. If you’re in camp `vim` like me, just be careful and don’t clobber things you’ll need!

The previous example only saves me 5 characters of typing and isn’t really that useful. But writing out my entire signature is *really* useful, so I have this (well, very close to this at least):

```
  - trigger: ":me"
    replace: "Chris Sullo | [email protected] | 555-867-5309"
```

I have simple replacements for my phone number, address, email address, and others. Even with the most basic usage, Espanso can save you time. But with some additional features, it can get much more powerful.

An important note about [YAML](https://yaml.org/): whitespace matters (like Python 😔). If you aren’t comfortable with the format, simply copy and edit existing lines to retain the indentation.

### Advanced Usage

##### **Variables**

Espanso can use internal variables to make matching a little more dynamic without resorting to full shell commands. The example below replaces the `{{time}}` value with the current hour and minute.

```
  - trigger: :now
    replace: It's {{time}}
    vars:
      - name: time
...