---
title: Wikileaks: A case study on journalism and encryption
url: https://blog.torproject.org/wikileaks-case-study-on-journalism-and-encryption/
source: Tor Project blog
date: 2024-08-27
fetch_date: 2025-10-06T18:08:36.413382
---

# Wikileaks: A case study on journalism and encryption

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Wikileaks: A case study on journalism and encryption

by [isabela](/author/isabela)
| August 26, 2024

![](/wikileaks-case-study-on-journalism-and-encryption/lead.png)

*Earlier this year I was asked to join [the Intercept Brasil](https://www.intercept.com.br/) as a contributor to write about the intersection of technology and human rights. Like dozens of other news sites around the world, Intercept Brasil uses Tor-powered tools and other encrypted services for their journalistic work. This is a summary of an article that was originally published under the headline [Como a criptografia e a seguranÃ§a de dados salvaram Julian Assange e o Wikileaks](https://www.intercept.com.br/2024/07/12/como-a-criptografia-e-a-seguranca-de-dados-salvaram-julian-assange-e-o-wikileaks/) (How encryption and data security saved Julian Assange and Wikileaks), in which I reflect on the role of encryption and some of Tor's contributions to modern investigative journalism.*

---

Julian Assange is finally free in his homeland of Australia. The journalist, who spent years under persecution for exposing war crimes committed by the United States, shaped investigative journalism by utilizing encrypted technologies to safeguard sources, their information--and journalism itself.

Drawing from his experience as a member of the hacker community, Assange recognized that encryption could offer a shield for investigative journalists to protect them and their sources from potential retribution. And he leveraged encrypted technologies like Tor and Tails for his own work with [Wikileaks](https://wikileaks.org/). In fact, to this day, Tor and Tails are prominently featured technologies on the Wikileaks website.

## Anonymity and security online

Tor, a decentralized network maintained by volunteers worldwide, employs 'onion routing' to obscure the origin of internet traffic. Each connection within the Tor network is layered with encryption, akin to the layers of an onion, ensuring that no single server can access all the information in transit. This architecture allows Tor to offer robust anonymity, making it a cornerstone for secure online communications.

However, Tor's capabilities extend beyond mere connection protection. The Tor Project developed the Tor Browser, a modified version of Firefox, designed to seamlessly connect to the Tor network while safeguarding user privacy. Prior to the Tor Browser, users had to configure standard browsers to connect to Tor, a process fraught with complexity and privacy leaks. The Tor Browser improved this experience with a modern, user-friendly UX that makes connecting to the Tor network easy. This prevents such leaks and ensures that users could access websites without revealing their identities.

That's why using Tor Browser and the Tor network in tandem is fundamental to guaranteeing anonymity. It's the only way to access [.onion sites](https://blog.torproject.org/how-we-plant-and-grow-new-onions/), websites that obfuscate the origin of the servers that host these sites. This way, no one knows who is accessing the site or where they are hosted.

## Secure channels: Wikileaks and .onion sites

WikiLeaks utilized a .onion site to receive information from sources anonymously. This method provided a confidential channel for whistleblowers to contact journalists without fear of exposure. Yet, Assange and his team knew that anonymity on the internet was only part of the solution. They needed to address the digital traces left on the source's computer.

For example, if the source had a file saved on their computer and decided to send it to Wikileaks, it would be possible to find the trace of that file on the source's computer. It was also necessary to offer the option of having an operating system that is not associated with the computer and that offers the same level of protection that the Tor network and Tor Browser offer. Enter Tails, an operating system that runs from a USB drive, allowing users to operate in a secure environment without leaving any digital footprint on the host machine.

## The toolkit for investigative journalism

This trinity of tools--.onion sites, Tor Browser and the Tails operating system--has become a 'basic kit' for modern investigative journalism. Their adoption spread across the globe, with numerous [news organizations incorporating these technologies to protect their work and sources](https://community.torproject.org/onion-services/). SecureDrop, developed by the Freedom of the Press Foundation, and SafeBox, used by the Forbidden Stories project, are other examples of how Tor-powered tools have been adopted to keep journalists and their sources safe.

Snowden's revelations about the US mass surveillance program became another milestone in the creation of a more user-friendly and secure file-sharing system akin to Dropbox or Google Drive--but with better privacy and anonymity protections. OnionShare was created, a simple tool [allowing users to share files through a .onion server on their computer](https://www.youtube.com/watch?v=gCDbHkpkNJ0), generating a .onion address to be sent to the person they want to share the file with and ensuring that the transfer remained confidential and untraceable. The added benefit, the filesharing address can be deactivated at any time in the application.

But that begs the question: What is a safe way to share this .onion address with someone else? My answer is Signal, a messaging app that uses encryption and other features to ensure user security. It has become indispensable for secure communication, and unlike its commercial counterparts, Signal is managed by a nonprofit organization. That means it can prioritize user privacy and security without the need to monetize user data.

## A lasting legacy: encryption's role in modern journalism

Assange's case has illustrated that the truth can upset a lot of people, and retaliation can be powerful--suppressing both the messenger and their message. And today, the potential for censorship looms even larger over anyone that dares to publish what governments and corporations might find inconvenient. Censorship often occurs through blocking of website domains, which restricts access to news sites and social media platforms. During the Arab Spring, Facebook was censored. Incredibly, it became the first major platform to adopt a .onion address, offering an alternative way to access the platform when its regular domain was blocked. Since then, major news organizations around the world like the [New York Times](https://www.nytimesn7cgmftshazwhfgzm37qxb44r64ytbb2dj3x62d2lljsciiyd.onion), [BBC](https://www.bbcnewsd73hkzno2ini43t4gblxvycyac5aw4gnv7t2rccijh7745uqd.onion/), and [Deutsche Welle](https://dwnewsgngmhlplxy6o2twtfgjnrnjxbegbwqx6wnotdhkzt562tszfid.onion/) have launched a .onion domain to ensure their content remains accessible, even in regions where these sites are censored.

Julian Assange's legacy is not merely in the revelations published by WikiLeaks, but in the lasting impact he has had on journalistic practices. By adopting tools that use encryption to protect people on the internet, Assange demonstrated to the world how journalists could adapt their work to the digital age and protect themselves from the threats that came with it. His example has been followed by others and improved upon ever since, and many important news stories have reached the public thanks to the use of these technologies.

---

**For news outlets, apps or services that are interested in launching their own .onion site, please visit [Onionspray](https://onionservices.torproject.org/apps/web/onionspray/)âa tool designed to simplify the setup of Onion Services for existing public website...