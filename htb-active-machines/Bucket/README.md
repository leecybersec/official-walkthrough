# \_\__LeeCyberSec_\_\_
| About Author | **Hack The Box Walkthrough** |
| :-------------------------------- |-------------------------------|
| **I'm Hades - Red/purple teamer** <br> `Email:` [tuvn@protonmail.com](mailto:tuvn@protonmail.com) <br> <br> `Platform:` [HackTheBox](https://www.hackthebox.eu/profile/167764) \|\| [TryHackMe](https://tryhackme.com/p/leecybersec) \|\| [PentesterLab](https://pentesterlab.com/profile/leecybersec) <br> <br> <img src="http://www.hackthebox.eu/badge/image/167764" alt="Hack The Box"> <br> <br> *Support me at [buymeacoffee](https://www.buymeacoffee.com/leecybersec)* <br> <a href='https://www.buymeacoffee.com/leecybersec' target="blank"><img src="images/bymeacoffee.png" width="200"/></a> | ![](images/1.png) |

## Information Gathering

### Openning Services

``` bash

```

## Foothold

...

At listener, I got reverse shell

``` bash
┌──(Hades㉿10.10.14.6)-[3.0:53.2]~
└─$ sudo nc -nvlp 443
listening on [any] 443 ...
connect to [10.10.14.6] from (UNKNOWN) [10.10.10.233] 40322
sh: no job control in this shell
sh-4.2$ id
id
uid=48(...) gid=48(...) groups=48(...)
sh-4.2$
```

## Privilege Escalation

### User Shell

...

Get user shell

```
┌──(Hades㉿10.10.14.6)-[2.8:66.2]~
└─$ ...
Last login: Thu Apr 15 08:39:14 2021 from 10.10.14.6
[...@armageddon ~]$ id
uid=1000(...) gid=1000(...) groups=1000(...)
```

### Root Shell

Run `sudo -s` to be root

```
[...@...]$ sudo -s

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

[sudo] password for dirty_sock: 
[...@armageddon ]# id
uid=0(root) gid=0(root) groups=0(root)
[...@armageddon ]#
```