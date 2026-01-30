---
title: Tracking Signal Identifiers
url: https://scriptjunkie.us/2026/01/tracking-signal-identifiers/
source: Thoughts on Security
date: 2026-01-29
fetch_date: 2026-01-30T04:02:40.918031
---

# Tracking Signal Identifiers

Something about Network Security. Exploits, research … profit!

# [Thoughts on Security](https://scriptjunkie.us/)

* [Home](https://scriptjunkie.us "Click for Home")
* [About](https://scriptjunkie.us/about/)
* [Building Secure Networks](https://scriptjunkie.us/building-secure-networks/)
* [Copyright/License](https://scriptjunkie.us/copyrightlicense/)
* [Important Stuff](https://scriptjunkie.us/important-stuff/)
* [Links](https://scriptjunkie.us/links/)
* [msfgui](https://scriptjunkie.us/msfgui/)
* [Privacy Policy](https://scriptjunkie.us/privacy-policy/)
* [sessionthief](https://scriptjunkie.us/http-sessionthief/)

« [schadnfreude](https://scriptjunkie.us/2021/11/schadnfreude/)

## Tracking Signal Identifiers

In the past few days Signal groups exploded in the news with [revelations that Signal groups are the primary](https://x.com/camhigby/status/2015093523733733474) "ICE tracker" channels, [may have dispatched Alex Pretti to his fatal encounter with DHS](https://www.dailymail.co.uk/news/article-15498429/Alex-Pretti-Minnesota-protest-groups-Signal-group-chats-organized.html), and are [under investigation by the FBI](https://www.nbcnews.com/tech/internet/fbi-investigating-minnesota-signal-minneapolis-group-ice-patel-kash-rcna256041). As groups frequently hit the 1000-member capacity, concern about infiltration is rampant. Key facets of the groups include:

1. [Frequently rapidly changing display names and usernames](https://x.com/camhigby/status/2015093909735571462) and
2. Members using aliases to avoid being identified by name.

**Today we'll evaluate the security of those measures. To summarize, it doesn't look good for this threat model. Users can be tracked through changing names by other users and the FBI can get members' phones.**

While Signal [claimed a few years ago](https://signal.org/bigbrother/santaclara/) all it could provide law enforcement was "Unix timestamps for when each account was created and the date that each account last connected to the Signal service. That’s it." in reality, there's far more information about accounts in identifiers it possesses, and that its server uses, and some is accessible to users as well.

Anyone in or invited to a group can get ID's for all members that Signal or AWS can obtain phone numbers for and can be linked to Apple/Google ID's and that will remain constant through username or display name changes. Some of this has been theorized before, but to prove the concept, here's a step by step guide:

1. Download Signal Desktop for Windows
2. Install it and link to your phone app
3. Quit signal (right-click on the tray icon and hit Quit. This is important!)
4. Download and unzip a current PowerShell from <https://github.com/PowerShell/PowerShell/releases/download/v7.5.4/PowerShell-7.5.4-win-x64.zip>
5. Right-click pwsh.exe and select run as administrator
6. Save <https://raw.githubusercontent.com/MatejKafka/PSSignalDecrypt/1c8aa1a4b5a29290f54dbd032c6228652aad8609/Unprotect-SignalConfig.ps1> in the same folder as pwsh.exe
7. In your pwsh window, run `pwsh -ep bypass .\unprotect-signalconfig.ps1` which will show you your database key. Copy it by double-clicking the big string of letters and numbers then right-clicking.
8. Type `wsl --install Ubuntu` and hit enter then `wsl -d Ubuntu` and hit enter to install and start an Ubuntu Linux distribution
9. Type `sudo apt install sqlcipher jq -y` and hit enter to install the tools to query the database file
10. Type `read KEY` hit enter, then paste in your key from above and hit enter again
11. Paste the following and hit enter. This will spit out a list of all groups you are part of and all their member ID's and also save it in "convomembers.txt" by enumerating the mapping between ID and display names, known phone numbers, and about information, then listing all group members matching them to profile information:

    `for USER in $(ls /mnt/c/Users/);do DB=/mnt/c/Users/$USER/AppData/Roaming/Signal/sql/db.sqlite ;if [ -f $DB ] ;then declare -A mappings;while IFS= read LINE ;do SID=$(echo $LINE|tr "," "\n"|grep serviceId|awk -F'"' '{print $4}');if [ ! -z "$SID" ] ;then mappings["$SID"]="$LINE";fi;done < <(echo "PRAGMA key = \"x'$KEY'\"; select json from conversations where type = 'private';"|sqlcipher $DB|tail -n +2|jq -cr '.|{serviceId, name, e164, profileName, profileFamilyName, about}');echo "PRAGMA key = \"x'$KEY'\"; select json from conversations where type <> 'private';" | sqlcipher $DB | tail -n +2 | jq -r '.name, .membersV2[].aci' 2>/dev/null| while IFS= read -r LINE ; do if [[ -v mappings["$LINE"] ]]; then echo "${mappings["$LINE"]}";else echo -e "\n$LINE";fi;done;fi;done| tee convomembers.txt`

    You'll see output like this:
    ![](https://scriptjunkie.us/wp-content/uploads/2026/01/signal-dump.png)
    Here, the three members of a group named "The Jedi Council" are listed. While the display name and about are the same as those visible in the signal UI, we can also see the "serviceID" which is the account ID for each.

    Not shown here, but you can also identify which accounts are admins by grabbing the membersV2 array for a group conversation and looking for those serviceID's with a role of 2. (Above we simply grabbed all ID's).
12. Take the convo's and people you care about, and note their serviceID's.

Now what?

Grabbing the account data from Signal either directly or via the cloud provider they rely on ([AWS](https://www.theverge.com/news/807147/signal-aws-outage-meredith-whittaker)) is trivial. The FBI can use National Security Letters, [as explained by the EFF](https://www.eff.org/issues/national-security-letters): "the FBI has issued hundreds of thousands of such letters seeking the private telecommunications and financial records of Americans without any prior approval from courts. In addition to this immense investigatory power, NSL statutes also permit the FBI to unilaterally gag recipients and prevent them from criticizing such actions publicly."

* Signal can do what the Signal Server does and do a simple DB query on their accounts table for the serviceId (a.k.a. aci or account id). This will return the account JSON for each. It will include a devices array which will include gcmId and/or apnId for each mobile device, and it will probably include [the phone number as well](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/storage/Account.java#L46-L47) (note how the number [provided to tests](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/test/java/org/whispersystems/textsecuregcm/storage/AccountTest.java#L81) is a plain phone number and that gets [directly set](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/test/java/org/whispersystems/textsecuregcm/tests/util/AccountsHelper.java#L40-L45) to [the number field](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/storage/Account.java#L175)).
  + This information is also likely cached in redis (see source analysis below).
  + It's a common task to grant access to an AWS hosted redis instances and probably trivial for Amazon to do so if they were served with an NSL, and not much more difficult to provide access to the underlying foundation DB as well.
  + So despite being apparently legally required, it's unlikely that Signal's cooperation would even be technically required here. Even if Signal might want to devote expensive time and resources to fight an NSL, they may never get the chance. It's worth noting that [AWS gets something like $10 billion from a single NSA contract alone](https://www.executivegov.com/articles/top-government-contracts-won-by-amazon-web-services).
* Google or Apple can then provide the phone number (and account owner name, email and likely location, birthday, payment details,...