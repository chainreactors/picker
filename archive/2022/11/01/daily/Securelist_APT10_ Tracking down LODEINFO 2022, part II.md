---
title: APT10: Tracking down LODEINFO 2022, part II
url: https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/
source: Securelist
date: 2022-11-01
fetch_date: 2025-10-03T21:24:53.855027
---

# APT10: Tracking down LODEINFO 2022, part II

Solutions for:

* [Home Products](https://www.kaspersky.com/home-security?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_prodmen_sm-team_______d5c53f9a5bd411f7)
* [Small Business 1-50 employees](https://www.kaspersky.com/small-business-security?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_prodmen_sm-team_______d5c53f9a5bd411f7 "font-icons icon-small-business")
* [Medium Business 51-999 employees](https://www.kaspersky.com/small-to-medium-business-security?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_prodmen_sm-team_______d5c53f9a5bd411f7)
* [Enterprise 1000+ employees](https://www.kaspersky.com/enterprise-security?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_prodmen_sm-team_______d5c53f9a5bd411f7)

by Kaspersky

* [CompanyAccount](https://companyaccount.kaspersky.com/account/login?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)* [Get In Touch](https://www.kaspersky.com/enterprise-security/contact?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)* Dark mode off* English
        + [Russian](https://securelist.ru)
        + [Spanish](https://securelist.lat)
        + [Brazil](https://securelist.com.br)

* [Solutions](https://www.kaspersky.com/enterprise-security?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)
  + - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/iot-embed-security.png)](https://www.kaspersky.com/enterprise-security/embedded-security-internet-of-things?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)[Internet of Things & Embedded Security](https://www.kaspersky.com/enterprise-security/embedded-security-internet-of-things?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)

      [Learn More](https://www.kaspersky.com/enterprise-security/embedded-security-internet-of-things?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)

      - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/transportation-cybersecurity.png)](https://www.kaspersky.com/enterprise-security/industrial-solution?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)[Industrial Cybersecurity](https://www.kaspersky.com/enterprise-security/industrial-solution?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)

        [Learn More](https://www.kaspersky.com/enterprise-security/industrial-solution?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)

        - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/fraud-prevention.png)](https://www.kaspersky.com/enterprise-security/fraud-prevention?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)[Fraud Prevention](https://www.kaspersky.com/enterprise-security/fraud-prevention?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)

          [Learn More](https://www.kaspersky.com/enterprise-security/fraud-prevention?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)

          - [KasperskyOS-based solutions](https://www.kaspersky.com/enterprise-security/kasperskyos?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)

            [Learn More](https://www.kaspersky.com/enterprise-security/kasperskyos?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)+ - ###### Other solutions

        - [Kaspersky for Security Operations Center](https://www.kaspersky.com/enterprise-security/security-operations-center-soc?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)- [Kaspersky IoT Infrastructure Security](https://www.kaspersky.com/enterprise-security/kaspersky-iot-infrastructure-security?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)- [Kaspersky Secure Remote Workspace](https://www.kaspersky.com/enterprise-security/kaspersky-secure-remote-workspace?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)* [Industries](https://www.kaspersky.com/enterprise-security/industries?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)
    + - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/national-cybersecurity.png)](https://www.kaspersky.com/enterprise-security/national-cybersecurity?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)[National Cybersecurity](https://www.kaspersky.com/enterprise-security/national-cybersecurity?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)

        [Learn More](https://www.kaspersky.com/enterprise-security/national-cybersecurity?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)

        - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/industrial-cybersecurity.png)](https://www.kaspersky.com/enterprise-security/industrial?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)[Industrial Cybersecurity](https://www.kaspersky.com/enterprise-security/industrial?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)

          [Learn More](https://www.kaspersky.com/enterprise-security/industrial?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)

          - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/financial-cybersecurity.png)](https://www.kaspersky.com/enterprise-security/finance?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)[Finance Services Cybersecurity](https://www.kaspersky.com/enterprise-security/finance?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)

            [Learn More](https://www.kaspersky.com/enterprise-security/finance?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)

            - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/healthcare-cybersecurity.png)](https://www.kaspersky.com/enterprise-security/healthcare?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)[Healthcare Cybersecurity](https://www.kaspersky.com/enterprise-security/healthcare?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)

              [Learn More](https://www.kaspersky.com/enterprise-security/healthcare?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)

              - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/transportation-cybersecurity.png)](https://www.kaspersky.com/enterprise-security/transportation-cybersecurity-it-infrastructure?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)[Transportation Cybersecurity](https://www.kaspersky.com/enterprise-security/transportation-cybersecurity-it-infrastructure?icid=gl_seclistheader_acq_ona_smm__onl_b2b_securelist_main-menu_sm-team_______001391deb99c290f)

                [Learn More](https://www.kaspersky.com/enterprise-security/transportation-cybersecurity-it-infrastructure?icid=gl_se...