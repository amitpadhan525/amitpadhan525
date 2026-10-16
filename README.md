<div align="center">

<!-- Hero Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,45:082736,100:00F5FF&height=220&section=header&text=AMIT%20PADHAN&fontSize=42&fontAlignY=36&desc=Offensive%20Security%20Researcher%20%E2%80%A2%20Linux%20Systems%20Engineer&descAlignY=58&descSize=16&fontColor=ffffff&descColor=00F5FF" width="100%" alt="Header Banner" />

<!-- Quick Connect & Profile Badges -->
<p align="center">
  <a href="https://amitpadhan525.github.io/"><img src="https://img.shields.io/badge/Portfolio-amitpadhan525.me-00F5FF?style=flat-square&logo=googlechrome&logoColor=black" alt="Portfolio"></a>
  <a href="https://tryhackme.com/p/amitpadhan525"><img src="https://img.shields.io/badge/TryHackMe-amitpadhan525-212C42?style=flat-square&logo=tryhackme&logoColor=white" alt="TryHackMe"></a>
  <a href="https://profile.hackthebox.com/profile/019c3941-83d7-70be-9be8-8f006c7a93f9"><img src="https://img.shields.io/badge/HackTheBox-amitpadhan525-9FEF00?style=flat-square&logo=hackthebox&logoColor=black" alt="HackTheBox"></a>
  <a href="https://github.com/amitpadhan979"><img src="https://img.shields.io/badge/Secondary_Profile-@amitpadhan979-181717?style=flat-square&logo=github&logoColor=white" alt="Secondary Profile"></a>
</p>

</div>

---

### 💻 System Terminal

```bash
┌──(amit㉿archlinux)-[~]
└─$ cat << 'EOF' > profile.json
{
  "engineer": "Amit Padhan",
  "specialization": "Offensive Security Researcher & Linux Systems Engineer",
  "workstation": "Arch Linux (Hyprland / Wayland + Kitty + Neovim)",
  "flagship_project": "linux-eye (Real-time Linux EDR Monitor)",
  "core_domains": [
    "Kernel Event Hooking (inotify, netlink udev)",
    "Host-based Intrusion Detection & Telemetry (EDR)",
    "Network Reconnaissance & Automated Exploitation Sandboxes",
    "Air-gapped & Offline AES-256-GCM Vault Architectures"
  ]
}
EOF
```

---

### 👁️ Flagship Spotlight: [linux-eye](https://github.com/amitpadhan525/linux-eye)
> **Lightweight real-time Linux security & endpoint detection monitor (EDR)**

<p align="center">
  <a href="https://github.com/amitpadhan525/linux-eye"><img src="https://img.shields.io/badge/Core_Project-LinuxEye_EDR-00F5FF?style=for-the-badge&logo=shield&logoColor=black" alt="LinuxEye EDR"></a>
  <a href="https://github.com/amitpadhan525/linux-eye/releases/latest"><img src="https://img.shields.io/github/v/release/amitpadhan525/linux-eye?style=for-the-badge&color=00F5FF&logo=github&logoColor=black" alt="Latest Release"></a>
  <a href="https://github.com/amitpadhan525/linux-eye"><img src="https://img.shields.io/badge/Platform-Linux%20Kernel%20%7C%20Systemd-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux Platform"></a>
  <a href="https://github.com/amitpadhan525/linux-eye"><img src="https://img.shields.io/github/stars/amitpadhan525/linux-eye?style=for-the-badge&color=00F5FF&logo=apachespark&logoColor=black" alt="Stars"></a>
</p>

An autonomous host-based intrusion detection daemon running seamlessly on Linux workstations and servers, watching for malicious behavior across 5 dedicated telemetry engines:

- ⚙️ **Process Telemetry Engine:** Intercepts suspicious process lifecycles via `psutil` (reverse shells like `bash -i` / `nc -e`, download-cradles like `curl | sh`, inline scripts, and persistence routines).
- 🌐 **Network Socket Engine:** Stateful rolling-window analyzer detecting automated port scanning and reconnaissance sweeps.
- 📂 **Kernel Filesystem Watcher:** Direct Linux kernel `inotify` hooks alerting on unauthorized modifications to `/etc/passwd`, `/etc/shadow`, and `/etc/sudoers`.
- 🔐 **Authentication & PAM Stream:** Asynchronous journal telemetry parsing sudo/SSH/PAM sessions to flag credential attacks and trigger sliding-window brute-force alerts.
- 🔌 **Hardware Netlink Engine:** Kernel netlink udev watcher flagging unauthorized USB storage and peripheral insertions.

---

### 🛠️ Tech Stack & Arsenal

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,c,cpp,bash,java,lua,dart,arch,kali,linux,docker,git,github,neovim,vscode&theme=dark" alt="Tech Stack Icons" />
  </a>
</p>

| Domain | Tools & Technologies |
| :--- | :--- |
| **Languages** | `Python` · `C / C++` · `Bash` · `Java` · `Lua` · `Dart` |
| **Offensive Security** | `Nmap` · `Burp Suite` · `Wireshark` · `Metasploit` · `Gobuster` · `Evil-WinRM` · `Hashcat` · `Hydra` |
| **Systems & Virtualization** | `Arch Linux` · `Kali Linux` · `QEMU / KVM` · `Docker` · `Systemd` · `Linux Bridge (br0)` |
| **Desktop Environment** | `Hyprland (Wayland)` · `Waybar` · `Kitty` · `Neovim` · `SDDM (QML)` |

---

### 📂 Engineering Projects & Security Research

| Project | Stack | Description | Stars |
| :--- | :--- | :--- | :---: |
| [**locker**](https://github.com/amitpadhan525/locker) | `Python` `AES-256-GCM` | 100% offline, zero-knowledge encrypted vault & virtual drive application with automated backup. | [![Stars](https://img.shields.io/github/stars/amitpadhan525/locker?style=flat-square&color=00F5FF)](https://github.com/amitpadhan525/locker) |
| [**ReconX**](https://github.com/amitpadhan525/ReconX) | `Python` `Sockets` | Multi-threaded network reconnaissance framework with TCP scanning, banner grabbing, and fuzzing. | [![Stars](https://img.shields.io/github/stars/amitpadhan525/ReconX?style=flat-square&color=00F5FF)](https://github.com/amitpadhan525/ReconX) |
| [**qemu-kvm-lab**](https://github.com/amitpadhan525/qemu-kvm-lab) | `Shell` `QEMU/KVM` | Automated isolated virtualization lab environment on Arch Linux (Win 11, Kali, Metasploitable2, TPM 2.0). | [![Stars](https://img.shields.io/github/stars/amitpadhan525/qemu-kvm-lab?style=flat-square&color=00F5FF)](https://github.com/amitpadhan525/qemu-kvm-lab) |
| [**cybersecurity-labs**](https://github.com/amitpadhan525/cybersecurity-labs) | `Markdown` `Labs` | Practical vulnerability assessments, penetration testing notes, and hands-on CTF writeups. | [![Stars](https://img.shields.io/github/stars/amitpadhan525/cybersecurity-labs?style=flat-square&color=00F5FF)](https://github.com/amitpadhan525/cybersecurity-labs) |
| [**linux-dotfiles**](https://github.com/amitpadhan525/linux-dotfiles) | `Shell` `Hyprland` | Daily driver Arch Linux Wayland desktop environment setup (Catppuccin Mocha, Waybar, Rofi, Kitty). | [![Stars](https://img.shields.io/github/stars/amitpadhan525/linux-dotfiles?style=flat-square&color=00F5FF)](https://github.com/amitpadhan525/linux-dotfiles) |
| [**security-notes**](https://github.com/amitpadhan525/security-notes) | `Markdown` `CTF` | Curated offensive security documentation, TryHackMe & Hack The Box walkthroughs, and cheat sheets. | [![Stars](https://img.shields.io/github/stars/amitpadhan525/security-notes?style=flat-square&color=00F5FF)](https://github.com/amitpadhan525/security-notes) |
| [**erp-autologin**](https://github.com/amitpadhan525/erp-autologin) | `Java` `Android` | Automated login assistant featuring on-device OCR CAPTCHA recognition and secure credential storage. | [![Stars](https://img.shields.io/github/stars/amitpadhan525/erp-autologin?style=flat-square&color=00F5FF)](https://github.com/amitpadhan525/erp-autologin) |

---

### 📊 GitHub Activity & Metrics

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=amitpadhan525&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00F5FF&icon_color=00F5FF" height="155" alt="GitHub Stats" />
&nbsp;
<img src="https://streak-stats.demolab.com/?user=amitpadhan525&theme=tokyonight&hide_border=true&background=0D1117&ring=00F5FF&fire=00F5FF&currStreakNum=00F5FF&sideNums=ffffff" height="155" alt="GitHub Streak Stats" />

<br/><br/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=amitpadhan525&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00F5FF&text_color=ffffff" height="145" alt="Top Languages" />

</div>

---

<div align="center">

<sub>*All security tools, scripts, and lab configurations are developed strictly for authorized security assessments, defensive engineering, academic research, and ethical educational purposes.*</sub>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00F5FF,100:0D1117&height=70&section=footer" width="100%" alt="Footer Banner" />

</div>
