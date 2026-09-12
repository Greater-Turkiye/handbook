> translation_of: tr/04-opsec.md

# 04 · Operational Security (OPSEC)

This page is here to protect **you**. Open-source defence analysis attracts the attention of state actors, troll networks and malicious individuals. The measures below are free and most are one-time settings.

## 1. A pseudonym is not anonymity

- Contributing under a pseudonym is allowed and supported. You don't have to reveal your identity to anyone — including the maintainers.
- But be aware: **GitHub, Telegram, Bluesky and other platforms comply with legal requests.** Records such as IP addresses, emails, phone numbers and payment details can be disclosed on request.
- A pseudonym makes it harder for colleagues, trolls or the curious to find you. It does **not** protect you against a state-level adversary.
- So the best OPSEC is **not breaking the rules**: a contribution that respects the red lines has nothing to hide.

### Pseudonym hygiene
- Pick a new name you have never used anywhere else (gaming accounts, forums, old social media).
- Don't use your own photo, or any image findable by reverse image search, as an avatar.
- Writing habits, working hours, mentioning your city, or phrases like "the base near us" can give you away.
- Don't link your real-name accounts and your pseudonymous account through follows, likes or tags.

## 2. GitHub email privacy

GitHub → **Settings → Emails**:
1. Enable **"Keep my email addresses private"**. GitHub gives you an address like `ID+username@users.noreply.github.com`.
2. Enable **"Block command line pushes that expose my email"**. Commits accidentally made with your real email will then be rejected.
3. Configure local git with that address:

```bash
git config --global user.name "your-pseudonym"
git config --global user.email "12345678+your-pseudonym@users.noreply.github.com"
```

If you have previously committed with your real email, those commits remain public; consider opening a fresh account.

## 3. Time zone in commits

Git records your **local time-zone offset** (e.g. `+0300`) in every commit. That can reveal your region. Commit in UTC:

```bash
# Bash / Git Bash / macOS / Linux
TZ=UTC git commit -m "evt: ..."

# To make it permanent (bash)
alias git='TZ=UTC git'
```

```powershell
# PowerShell (for the session)
$env:TZ = "UTC"
git commit -m "evt: ..."
```

Check: `git log -1 --format="%ad"` should show `+0000`. For commits made through the web interface this is generally handled on GitHub's side, but if unsure, work locally in UTC.

## 4. Devices and networks

- **NEVER use work or government devices or networks.** They may be monitored and logged; if you are a public servant, it can also create conflicts of interest and disciplinary problems.
- Keep your personal device's OS and browser updated.
- Use a separate browser profile for community work (only your pseudonymous accounts logged in there).
- Be careful on public Wi-Fi. Using a VPN or Tor is your choice; check whether they are legal where you are. Remember: Tor/VPN does not make you anonymous to a platform the moment you log in to your account.

## 5. Metadata stripping

No media files (photos, videos) are ever **committed** to the community ([06](06-sourcing-archiving.md)). Still, you may need to send an image privately to maintainers or add a screenshot to an issue:

- Photos can contain **EXIF** data (GPS location, device model, capture time). Strip it before sharing (e.g. `exiftool -all= file.jpg`) or create a new file by taking a screenshot.
- PDF and Office documents can contain author names, organisation names and edit history.
- Make sure screenshots don't show browser tabs, bookmarks, notifications, your username, or your clock and language settings.
- Images uploaded to GitHub usually have EXIF stripped, but don't rely on it.

## 6. No interaction with targets

- Do **not interact** with monitored people, channels or groups using sock-puppet accounts: no messages, no questions, no joining closed groups, no arguments.
- Passive observation: read only what is public. Follow Telegram channels via their **public web preview** where possible (`t.me/s/channelname`).
- Channel owners may see member lists; if you registered with a real phone number, keep it hidden (Telegram → Privacy → Phone number: Nobody).
- Don't reply to provocative content; screenshot and archive it and leave the rest to the maintainers.

## 7. Account security

- **Two-factor authentication (2FA) is mandatory.** The organisation does not accept members without 2FA.
- Order of preference: **passkey / hardware key** → **TOTP app** (Aegis, 2FAS, Ente Auth, etc.) → SMS (not recommended; vulnerable to SIM-swap attacks).
- Print or store **recovery codes** offline (encrypted USB, paper). Don't store them in plain text in a cloud notes app.
- Use unique, long passwords and a password manager.
- Your pseudonymous account's recovery email should not be tied to your real identity — but should be one you won't lose access to.
- In privileged roles (triager, reviewer, maintainer), regularly review your GitHub sessions and authorised OAuth apps.

## 8. Malicious links and files

People working in this field are **phishing and malware** targets. "Leaked document", "exclusive footage", "evidence file" are the classic lures.

- Don't open files from people you don't know, especially `.docx`, `.xlsm`, `.pdf`, `.zip`, `.rar`, `.iso`, `.lnk`, `.apk`.
- If you really must open one: use a **virtual machine (VM)** or a disposable environment (e.g. Windows Sandbox) with networking disabled.
- Check a link's real destination before clicking; don't open shortened links (we don't accept them as sources either).
- Urgent-sounding messages like "your GitHub account will be suspended" or "Telegram verification code" are usually phishing.
- If a PR or issue contains executable code, scripts or binaries, **don't run them**; notify the maintainers.

## 9. Private channel for sensitive matters

Some things must **not** be discussed in a public issue or PR:

- Noticing a red-line violation,
- Being sent classified/leaked material,
- Harassment, threats, your identity being exposed,
- Suspecting an account has been compromised,
- Reporting a security vulnerability.

For these, use the private contact address in [SECURITY.md](https://github.com/Greater-Turkiye/.github/blob/main/SECURITY.md). **PRs and issues on GitHub are public immediately** — even if deleted, they can persist in caches and notification emails.

## 10. If you are harassed or threatened

- Don't respond or argue. Record it with screenshots and archive links.
- Notify the maintainers through the private channel; use the platform's reporting mechanism.
- If there is a threat to your physical safety, contact law enforcement. The community will do what it can to protect you (hiding your account, adjusting attribution of your contributions, etc.).
- Taking a break is always a legitimate option.

## Summary checklist

- [ ] A new, unlinked pseudonym
- [ ] "Keep my email addresses private" + "Block command line pushes that expose my email"
- [ ] `user.email` = noreply address
- [ ] Commits in UTC (`+0000`)
- [ ] No work/government device or network
- [ ] 2FA (passkey/TOTP) + offline recovery codes
- [ ] Metadata stripped from media files
- [ ] No interaction with targets
- [ ] Suspicious files only in a VM/sandbox
- [ ] Sensitive matters only via the private channel
