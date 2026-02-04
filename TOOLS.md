# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Email Oscar

- Adresse : oscarcoachdigital@gmail.com
- Mot de passe : $$Reussite888!!
- Usage : envoi de mails automatisés, notifications, tests

## WhatsApp Oscar

- **Numéro dédié** : +33756968633
- **Connecté** : 2026-02-04
- **allowFrom** : +33652345180 (Gilles) + +33756968633 (Oscar)
- **selfChatMode** : false (numéro dédié)

## TTS

- Provider : ElevenLabs
- Voix : Chris (iP95p4xoKVk53GoZ742B) — charming, décontracté
- Modèle : eleven_multilingual_v2
- Langue : fr
- Fallback : Edge TTS (Vivienne fr-FR)

## Browser Automation

### Navigateur Headless (AUTONOME) ✅
- **Profile** : `openclaw`
- **Executable** : `/snap/bin/chromium` (Chromium 144 via snap)
- **Mode** : headless + noSandbox
- **Port CDP** : 18800
- **UserDataDir** : `/home/gillescoach/.openclaw/browser/openclaw/user-data`
- **Je peux naviguer sans intervention de Gilles !**

### Chrome Extension (via Browser Relay)
- OpenClaw Browser Relay installé (unpacked depuis WSL)
- Chemin : \\wsl$\Ubuntu\home\gillescoach\.openclaw\browser\chrome-extension
- **Accès aux cookies Gmail** : Sessions connectées dans Chrome
  - gilleskorzec@gmail.com (compte principal Gilles)
  - coachdigitalparis@gmail.com (compte pro)
  - oscarcoachdigital@gmail.com (compte Oscar)
- Je peux me connecter aux services via "Continue with Google"

## CRM Coach Digital

- **URL** : https://gillescoachdigital.vercel.app
- **Login** : oscarcoachdigital@gmail.com (via Google)
- **Rôle** : ADMIN
- Je peux m'y connecter via Browser Relay + "Continue with Google"

## Vercel

- Token : fQWMWeA7vKDfE97Yfu32x9vX
- Account : gilleskorzec@gmail.com
- Org : gilles-korzec-projects

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
