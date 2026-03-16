# Pickle Rick - TryHackMe Writeup

## 🚩 Room Information
- **Link:** [TryHackMe - Pickle Rick](https://tryhackme.com/room/picklerick)
- **Difficulty:** Easy
- **Category:** Offensive Security / Web Exploitation

---

## 📝 Summary
This Rick and Morty-themed room is a classic web-based challenge. The goal is to exploit a web server to find three ingredients Rick needs for his potion. It involves enumeration, command injection, and basic privilege escalation.

## 🛠️ Tools Used
- Nmap
- Gobuster
- Web Browser (DevTools)
- Netcat

---

## 🔍 Task Walkthrough

### Task 1: Enumeration
I started by scanning the target machine for open ports:
```bash
nmap -sV -sC -Pn <target_ip>
```
Ports found:
- **80 (HTTP):** Apache httpd 2.4.18
- **22 (SSH):** OpenSSH 7.2p2

#### Web Exploration
Visiting the website showed a simple landing page. Checking the source code (`Ctrl+U`) revealed a comment with a username: `R1ckRul3s`.

Next, I ran **Gobuster** to find hidden directories:
```bash
gobuster dir -u http://<target_ip> -w /usr/share/wordlists/dirb/common.txt
```
Key files found:
- `/robots.txt`: Contained the text `WubbaLubbaDubDub`.
- `/login.php`: A login portal.

### Task 2: Gaining Access
Using the username `R1ckRul3s` and the "password" found in `robots.txt` (`WubbaLubbaDubDub`), I successfully logged into the `/portal.php` panel.

### Task 3: Exploitation (Command Injection)
The portal had a command execution field. Testing it with `ls`:
```bash
Sup3rS3cretPickl3Ingr3di3nt.txt
assets
clue.txt
login.php
portal.php
robots.txt
```
I found the first ingredient! `cat Sup3rS3cretPickl3Ingr3di3nt.txt` was blocked, so I used `grep "." Sup3rS3cretPickl3Ingr3di3nt.txt` or `ls -la`.
**Ingredient 1:** `mr. meeseek hair`

#### Finding Ingredient 2
Running `ls /home/rick`:
```bash
second ingredients
```
Reading it with `cat` (some commands were filtered):
**Ingredient 2:** `1 jerry tear`

### Task 4: Privilege Escalation
Checking sudo privileges:
```bash
sudo -l
```
Result: `(ALL) NOPASSWD: ALL`. Rick's user has full sudo access without a password!

#### Finding Ingredient 3
```bash
sudo ls /root
sudo cat /root/3rd.txt
```
**Ingredient 3:** `fleeb juice`

---

## 🏁 Conclusion
The Pickle Rick room is an excellent introduction to web enumeration and command injection. It highlights the importance of checking source code, robots.txt, and directory brute-forcing.

---
*Created by [Amit Padhan](https://github.com/amitpadhan525)*
