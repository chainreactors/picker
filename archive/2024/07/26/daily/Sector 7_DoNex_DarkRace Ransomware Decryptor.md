---
title: DoNex/DarkRace Ransomware Decryptor
url: https://sector7.computest.nl/post/2024-04-donex-darkrace-ransomware/
source: Sector 7
date: 2024-07-26
fetch_date: 2025-10-06T17:48:58.656940
---

# DoNex/DarkRace Ransomware Decryptor

[![](/images/logo.png)](/)

* [Research](/)
* [About](/about/)
* [Contact](/contact/)
* [Computest](https://computest.nl/)

* [Mastodon](https://infosec.exchange/%40sector7)
* [Bluesky](https://bsky.app/profile/sector7-nl.bsky.social)
* [LinkedIn](https://www.linkedin.com/company/computest)
* [GitHub](https://github.com/sector7-nl)
* [RSS](/index.xml)

July 25, 2024

# DoNex/DarkRace Ransomware Decryptor

![](/post/2024-04-donex-darkrace-ransomware/header.jpg)

Computest Sector 7 was asked by Team High-Tech Crime of the Dutch Police to help with writing a decryptor for the DoNex/DarkRace ransomware. DoNex is a relatively new ransomware group, which probably explains why its encryptor contains a simple to abuse mistake. It appears to be the same group that was working under the name DarkRace last year, as the DoNex encryptor we investigated is essentially the same as a DarkRace encryptor we looked at. We have submitted our decryptor to the [No More Ransom](https://www.nomoreransom.org/) initiative to help victims recover their files for free.

Gijs Rijnders, the analyst from the Dutch Police who worked on this, has found this weakness in the encryption procedure: it uses a stream cipher (Salsa20) without generating a new nonce or key for each file. Stream ciphers work by generating a keystream, based on the key and nonce, and then XOR-ing the keystream with the parts of the files that are encrypted. By re-using the key and nonce, all encrypted files end up encrypted with the same keystream. Therefore, it would be possible to find an encrypted file for which the unencrypted file is still available, then XOR those files to recover the keystream. With the keystream all other files can be recovered (even though the actual key is not known). For more information, Gijs presented his research at [REcon 2024](https://crysearch.nl/index.php?p=research).

In practice, having the unencrypted version of a file still available is quite common after a ransomware attack: for example, the file might have been downloaded from the internet and still available online, or received by email and still available in a mailbox. How much of the keystream do we need to recover? Thankfully, we don’t need to find the original of the largest encrypted file. Any file that is at least 1 MiB will do.

We investigated a sample of the ransomware encryptor (SHA256 hash: `0adde4246aaa9fb3964d1d6cf3c29b1b13074015b250eb8e5591339f92e1e3ca`) to make sure we fully understood how the encryption procedure works. See the rest of this post for these findings, and if you are interested in the decryptor, see [the page with the decryption tools at No More Ransom](https://www.nomoreransom.org/en/decryption-tools.html#DoNex).

# Encryption process

## Configuration

First, the device reads its own configuration from an XML string in its data section. This string is XORed with the byte 0xA9.

```
for ( i = 0; i < 0x21C0; i += 64 )
{
	*(__m128i *)&xml_config[i] = _mm_xor_si128((__m128i)xmmword_4295D0, *(__m128i *)&xml_config[i]);
	*(__m128i *)&xml_config[i + 16] = _mm_xor_si128((__m128i)xmmword_4295D0, *(__m128i *)&xml_config[i + 16]);
	*(__m128i *)&xml_config[i + 32] = _mm_xor_si128(*(__m128i *)&xml_config[i + 32], (__m128i)xmmword_4295D0);
	*(__m128i *)&xml_config[i + 48] = _mm_xor_si128((__m128i)xmmword_4295D0, *(__m128i *)&xml_config[i + 48]);
}
for ( ; i < 0x21E7; ++i )
	xml_config[i] ^= 0xA9u;
```

Result:

```
<?xml version='1.0' encoding='UTF-8'?>
<root>
	<white_extens>386;adv;ani;bat;bin;cab;cmd;com;cpl;cur;deskthemepack;diagcab;diagcfg;diagpkg;dll;drv;exe;hlp;icl;icns;ico;ics;idx;lnk;mod;mpa;msc;msp;msstyles;msu;nls;nomedia;ocx;prf;ps1;rom;rtp;scr;shs;spl;sys;theme;themepack;wpx;lock;key;hta;msi;pdb;search-ms</white_extens>
	<white_files>bootmgr;autorun.inf;boot.ini;bootfont.bin;bootsect.bak;desktop.ini;iconcache.db;ntldr;ntuser.dat;ntuser.dat.log;ntuser.ini;thumbs.db;GDIPFONTCACHEV1.DAT;d3d9caps.dat</white_files>
	<white_folders>$recycle.bin;config.msi;$windows.~bt;$windows.~ws;windows;boot;program files;program files (x86);programdata;system volume information;tor browser;windows.old;intel;msocache;perflogs;x64dbg;public;all users;default;microsoft;appdata</white_folders>
	<kill_keep>sql;oracle;mysq;chrome;veeam;firefox;excel;msaccess;onenote;outlook;powerpnt;winword;wuauclt</kill_keep>
	<services>vss;sql;svc$;memtas;mepocs;msexchange;sophos;veeam;backup;GxVss;GxBlr;GxFWD;GxCVD;GxCIMgr</services>
	<black_db>ldf;mdf</black_db>
	<encryption_thread>30</encryption_thread>
	<walk_thread>15</walk_thread>
	<local_disks>true</local_disks>
	<network_shares>true</network_shares>
	<kill_processes>true</kill_processes>
	<kill_services>true</kill_services>
	<shutdown_system>true</shutdown_system>
	<delete_eventlogs>true</delete_eventlogs>
	<cmd>wmic shadowcopy delete /nointeractive</cmd>
	<cmd>vssadmin Delete Shadows /All /Quiet</cmd>
	<content>            !!! DoNex ransomware warning !!!

&gt;&gt;&gt;&gt; Your data are stolen and encrypted

	The data will be published on TOR website if you do not pay the ransom

	Links for Tor Browser:
	(...)

&gt;&gt;&gt;&gt; What guarantees that we will not deceive you?

	We are not a politically motivated group and we do not need anything other than your money.

	If you pay, we will provide you the programs for decryption and we will delete your data.

	If we do not give you decrypters, or we do not delete your data after payment, then nobody will pay us in the future.

	Therefore to us our reputation is very important. We attack the companies worldwide and there is no dissatisfied victim after payment.

&gt;&gt;&gt;&gt; You need contact us and decrypt one file for free on these TOR sites with your personal DECRYPTION ID

	Download and install TOR Browser https://www.torproject.org/
	Write to a chat and wait for the answer, we will always answer you.

	You can install qtox to contanct us online https://tox.chat/download.html
	Tox ID Contact: (...)

	Mail (OnionMail) Support: (...)

&gt;&gt;&gt;&gt; Warning! Do not DELETE or MODIFY any files, it can lead to recovery problems!

&gt;&gt;&gt;&gt; Warning! If you do not pay the ransom we will attack your company repeatedly again!
	</content>
	<ico>AAA(...)</ico>
</root>
```

The configuration specifies for example which file extensions and folders to ignore, which processes to terminate and what commands to run first, the ransom note and an icon.

Then, it runs the specified commands one by one. For our sample, the commands are:

* `wmic shadowcopy delete /nointeractive`
* `vssadmin Delete Shadows /All /Quiet`

## Keys

Next, it generates the key that will be used for the Salsa20 encryption of files. It calls `CryptGenRandom` to generate 16 random bytes, so sadly, predictable keys here are ruled out.

The Salsa20 key is then encrypted using a RSA public key. This encrypted key is appended to every file encrypted by the ransomware. The RSA public key used for the encryption is also obtained from the executable, but it is in the overlay data (the data after the data for the PE format). To read it, it opens its own executable file and then parses the PE header to find the end of the last section and starts reading the data after that. This is done to make it easy to generate a new version, with a different encryption key, allowing the files for each customer to be encrypted using a new RSA key.

The key data format consists of a 512 byte hex-encoded modulus, followed by 6 hex-encoded bytes for the exponent (0x10001, or 65537), together denoting the RSA public key. Finally, the last 9 bytes are the file extension that is appended to every file (`f58A66B51` for our sample). The file extension is located in the overlay data too, as it is likely to change in a new version or for different victims.

```
00037e00  45 33 39 35 38 38 30 30  41 34 45 45 37 34 42 46  |E3958800A4EE74BF|
00037e10  35 39 38 33 39 36 37 45  33 43 36 35 38 36 39 33  |5983967E3C658693|
00037e20  43 41 39 33 37 37 37 45  42 38 43 41 37 39 46 44  |CA93777EB...