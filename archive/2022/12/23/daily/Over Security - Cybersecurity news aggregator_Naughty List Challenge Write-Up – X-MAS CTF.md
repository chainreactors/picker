---
title: Naughty List Challenge Write-Up – X-MAS CTF
url: https://voidsec.com/naughty-list-challenge-write-up-x-mas-ctf/
source: Over Security - Cybersecurity news aggregator
date: 2022-12-23
fetch_date: 2025-10-04T02:21:22.034451
---

# Naughty List Challenge Write-Up – X-MAS CTF

[![VoidSec](//voidsec.com/wp-content/uploads/2018/02/Voidsec_logo.png)![VoidSec](//voidsec.com/wp-content/uploads/2018/02/Voidsec_logo_.png)![VoidSec](//voidsec.com/wp-content/uploads/2018/02/Voidsec_logo.png)![VoidSec](//voidsec.com/wp-content/uploads/2018/02/Voidsec_logo_.png)](https://voidsec.com/ "VoidSec - Some things in life are unpredictable, your Cyber Security doesn’t have to be one of them")

* [Blog](https://voidsec.com/category/blog/)
* [Advisories](https://voidsec.com/advisories/)

  + [Vulnerability Disclosure Policy](https://voidsec.com/disclosure-policy/)
* [About](https://voidsec.com/member/voidsec/)
* [Contact](https://voidsec.com/contact-me/)

* [Blog](https://voidsec.com/category/blog/)
* [Advisories](https://voidsec.com/advisories/)

  + [Vulnerability Disclosure Policy](https://voidsec.com/disclosure-policy/)
* [About](https://voidsec.com/member/voidsec/)
* [Contact](https://voidsec.com/contact-me/)

[Back to Posts](https://voidsec.com)

![](https://voidsec.com/wp-content/uploads/2022/12/Gabies_Santa_writing_bad_kids_on_his_bad_list_in_his_workshop_t_e1c21fd5-5562-4a12-a5ac-a7847c978083.png)

### Share this post

[Facebook](https://www.facebook.com/sharer.php?u=https://voidsec.com/naughty-list-challenge-write-up-x-mas-ctf/ "Facebook")
[Twitter](https://twitter.com/intent/tweet?text=Naughty+List+Challenge+Write-Up+%E2%80%93+X-MAS+CTF&url=https://voidsec.com/naughty-list-challenge-write-up-x-mas-ctf/ "X")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://voidsec.com/naughty-list-challenge-write-up-x-mas-ctf/&title=Naughty+List+Challenge+Write-Up+%E2%80%93+X-MAS+CTF "LinkedIn")
[Email](/cdn-cgi/l/email-protection#59662a2c3b333c3a2d6417382c3e312d207215302a2d721a313835353c373e3c720e2b302d3c740c29727c1c6b7c61697c606a72017414180a721a0d1f7f383429623b363d2064312d2d292a6376762f36303d2a3c3a773a36347637382c3e312d207435302a2d743a313835353c373e3c742e2b302d3c742c2974217434382a743a2d3f76 "Email")
[VK](https://vk.com/share.php?url=https://voidsec.com/naughty-list-challenge-write-up-x-mas-ctf/&title=Naughty+List+Challenge+Write-Up+%E2%80%93+X-MAS+CTF&image=https://voidsec.com/wp-content/uploads/2022/12/Gabies_Santa_writing_bad_kids_on_his_bad_list_in_his_workshop_t_e1c21fd5-5562-4a12-a5ac-a7847c978083.png&noparse=true "VK")
[Reddit](http://www.reddit.com/submit?url=https://voidsec.com/naughty-list-challenge-write-up-x-mas-ctf/&title=Naughty+List+Challenge+Write-Up+%E2%80%93+X-MAS+CTF "Reddit")
WhatsApp

## Naughty List Challenge Write-Up – X-MAS CTF

Posted by: voidsec

Post Date: December 22, 2022

---

[voidsec](https://voidsec.com/author/voidsec/ "Posts by voidsec")2023-06-14T17:50:41+02:00

**Reading Time:**   6 minutes

As the last post of the year, I decided to do something chill and a bit “off-topic” from my usual content. As the festivities are approaching, I have a bit more free time to dedicate to different stuff, like helping some friends with CTFs and such.

I’ve decided to post about this specific challenge because since it wasn’t the most complex nor the one with the most shenanigans to flex about, it likely wouldn’t get any write-ups. But it’s a perfect entry-level challenge, showing a real-world example of a subtle “logic bug” that can be inadvertently introduced by programmers. I enjoyed it very much and I don’t want it to get lost in the interweb; hat tip to the organizers: [HTsP team](https://htsp.ro/).

# Naughty List

The challenge began with the following prompt:

> “PinkiePie managed to get on the Naughty List this year. Use your skills to get him out of this situation and he might reward you!”

The following C++ source code was available to inspect:

naughty\_list.cpp

```
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <unordered_map>

#define ELF_MAX_NAUGHTY_COUNT 16

std::unordered_map<std::string, std::string> naughty_list{
    {"PinkiePie", "Very naughty"}};

void menu()
{
    std::cout << "1. Ask PinkiePie for the flag" << std::endl;
    std::cout << "2. Query naughty list" << std::endl;
    std::cout << "3. Add to naughty list" << std::endl;
}

void ask_pinkiepie()
{
    bool pinkiepie_naughty = false;
    auto it = naughty_list.begin();

    for (int i = 0; i < ELF_MAX_NAUGHTY_COUNT; i++)
    {
        if (it->first == "PinkiePie")
        {
            pinkiepie_naughty = true;
            break;
        }
        ++it;
        if (it == naughty_list.end())
        {
            break;
        }
    }

    if (pinkiepie_naughty)
    {
        std::cout
            << "PinkiePie will not tell you the flag if he is on the naughty list"
            << std::endl;
    }
    else
    {
        std::cout << "PinkiePie is satisfied. Here is your flag!" << std::endl;
        std::ifstream flag_file{"/flag.txt"};

        std::cout << flag_file.rdbuf() << std::endl;
    }
}

bool is_naughty(const std::string &name) { return !(naughty_list[name] == ""); }

void add_to_list(const std::string &name)
{
    if (naughty_list.size() == ELF_MAX_NAUGHTY_COUNT)
    {
        std::cout << "Adding this many people requires authorization from Elf "
                     "Resources.";
        return;
    }
    else
    {
        naughty_list.insert({name, "Naughty"});
    }
}

int main()
{
    int choice;

    while (true)
    {
        menu();

        std::cin >> choice;

        switch (choice)
        {
        case 1:
        {
            ask_pinkiepie();
        }
        break;
        case 2:
        case 3:
        {
            std::string name;
            std::cout << "Name: ";
            std::cout.flush();
            std::cin >> name;

            if (choice == 2)
            {
                if (is_naughty(name))
                {
                    std::cout << name << " is naughty!" << std::endl;
                }
                else
                {
                    std::cout << name << " is not naughty!" << std::endl;
                }
            }
            else if (choice == 3)
            {
                add_to_list(name);
            }
            else
            {
                std::cout
                    << "Tampering alert triggered. This incident will be reported!"
                    << std::endl;
            }
        }
        break;
        default:
        {
            exit(1);
        }
        }
    }
}
```

This C++ program is a simple command-line application that allows the user to perform several actions:

1. **Ask PinkiePie for the flag**: if the “PinkiePie” entry is present in the `naughty_list` unordered map, the program will output a message saying that PinkiePie will not tell you the flag. Otherwise, the program will open the file `flag.txt` and output its contents.
2. **Query the naughty list**: the user is prompted to enter a name, and the program will check whether the name is present in the `naughty_list` unordered map.
3. **Add a name to the naughty list**: the user is prompted to enter a name, and the program will add the name to the `naughty_list` unordered map with the value “Naughty”. However, if the unordered map is already at its maximum size (defined by the constant `ELF_MAX_NAUGHTY_COUNT`), the program will prevent adding a new item.

Table of Contents

* [C++ unordered map](#c-unordered-map)
* [Removing PinkiePie](#removing-pinkiepie)
* [The square bracket operator](#the-square-bracket-operator)
* [POC](#poc)
* [References](#references)

## C++ unordered map

The entire challenge revolves around the C++ unordered map.

> An unordered map is an associative container that contains key-value pairs with unique keys. Internally, the elements are not sorted in any particular order but are organized into buckets. Which bucket an element is placed into depends entirely on the hash of its key. – [en.cppreference.com](https://en.cppreference.com/w/cpp/container/unordered_map)

I’ve made an instrumented version of the source code to print the content of the map:

```
template<typename K, typename V>
void print_map(std::unordered_map...