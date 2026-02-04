# MEMORY.md — Mémoire Long Terme d'Oscar

## Qui est Gilles
- Entrepreneur legaltech + coaching avocats
- Pas dev de formation mais très expérimenté (200+ sites, dizaine d'apps, MVP cabinet avocats)
- Expert low-code/no-code, apprend vite
- Priorité actuelle : LE COMMERCIAL — vendre l'application, trouver des clients
- Communique principalement via WhatsApp
- Parle parfois en vocal (Wispr Flow transcrit sa voix en texte)
- Tutoiement, direct, pas de blabla

## Setup technique

### PC Local (Gilles)
- PC Asus, Windows 11, 24 Go RAM, disque 476 Go
- Oscar LOCAL tourne dans WSL2 via OpenClaw gateway
- Outils quotidiens : Claude Desktop, Wispr Flow, Chrome, PowerToys (multi-PC)
- Dashboard local : http://127.0.0.1:18789 (raccourci bureau avec icône éclair)
- Widget "By GK" : monitoring RAM/disque + bouton optimiser

### VPS Production (LWS) — CRÉÉ LE 04/02/2026
- **IP : 180.149.198.23**
- **Dashboard : http://180.149.198.23:18789**
- **Token : OscarVPS2026SecureToken!**
- OpenClaw 2026.2.2-3 + service systemd
- Chromium 144 headless (navigation autonome)
- Workspace complet synchronisé
- ⚠️ **EXPIRE DANS 5 JOURS (~09/02/2026) — À RENOUVELER**
- WhatsApp : en attente rétablissement compte Meta
- Doc complète : `/memory/infra/vps-lws.md`

## Équipe
- Gilles : le patron, décideur
- Oscar (moi) : assistant quotidien via WhatsApp/OpenClaw
- Opus : Claude Opus via claude.ai, cerveau lourd pour tâches complexes

## Règle d'Or - AUTONOMIE
**JE FAIS, JE NE DEMANDE PAS.**
- Tout ce que je peux faire, je le fais moi-même
- Je ne demande à Gilles que si : impossible, bloqué, ou besoin d'une info que je n'ai pas
- Je prends TOUJOURS l'initiative
- Gilles ne m'a pas créé pour lui déléguer du travail, mais pour que JE fasse le travail

## Brief Communication Clients (validé 04/02/2026)
- **Vouvoiement** avec tous les clients
- **Tutoiement** uniquement avec Gilles
- Si on me demande "T'es une IA?" → je ne mens pas mais je n'en fais pas un sujet
- Réponse : "Collaborateur digital de Gilles, écrits uniquement, Gilles pour les RDV/appels"
- **Seul** : infos générales, documentation
- **Après validation Gilles** : RDV, devis, engagements
- **Transfert direct** : négociation, litiges, clients mécontents

Doc complet : `/memory/brief-communication-clients.md`

## Communication Triangulaire (testée 04/02/2026)
1. Client → Oscar WhatsApp (+33756968633)
2. Oscar → Gilles WhatsApp (+33652345180) pour valider
3. Gilles répond
4. Oscar → Client confirme

**Ça marche !** Test réussi à 01:22.

## Référence Rapide
**TOUJOURS lire `QUICKREF.md` au démarrage** — contient TOUS les accès critiques (VPS, CRM, tokens, URLs).

## Leçons apprises
- 2026-02-03 : **TOUJOURS vérifier que le build Vercel est passé avant de dire "c'est fait"** — pusher sur GitHub ne suffit pas, il faut confirmer le deploy
- 2026-02-03 : Les commandes PowerShell via WSL ont des problèmes d'échappement de parenthèses — utiliser chr() ou des variables
- 2026-02-03 : Les scans récursifs du disque C: via WSL timeout — faire des requêtes ciblées
- 2026-02-03 : taskkill /F est plus fiable que psutil.kill() pour fermer des processus Windows
- 2026-02-03 : La whitelist du widget doit utiliser du match exact (lowercase .exe), pas du match partiel
- 2026-02-03 : Gilles utilise Wispr Flow (voice-to-text), donc ses messages peuvent avoir des erreurs de transcription — interpréter le sens, pas la lettre
- 2026-02-03 : **TOUJOURS sauvegarder les infos clients dans memory/clients/, pas seulement dans Slack** — le contexte se compacte et les détails se perdent
- 2026-02-04 : **Documenter IMMÉDIATEMENT** les décisions stratégiques dans memory/projects/ — ne jamais compter sur le contexte de session
- 2026-02-03 : Vercel peut mettre les builds en "STAGED" au lieu de prod — utiliser l'API pour promouvoir manuellement si nécessaire
- 2026-02-03 : Le CRM utilise PostgreSQL via Prisma (pas MongoDB) — DB hébergée sur db.prisma.io
- 2026-02-04 : **NE JAMAIS CONFONDRE les numéros** — Gilles = 06 52 34 51 80 / Oscar = 07 56 96 86 33
- 2026-02-04 : **DOCUMENTER IMMÉDIATEMENT toute config/infra/installation** — VPS, serveurs, mots de passe, tokens → fichier dans memory/infra/ + MEMORY.md. JAMAIS compter sur le contexte de session. C'est NON NÉGOCIABLE.

## CRM Coach Digital
- **URL : https://gillescoachdigital.vercel.app**
- Projet Vercel : tesla-inspired-agency-crm (prj_kUpgzCjcGvTh8My1oo0GRMfeKsm9)
- GitHub : eddigit/gillescoachdigital
- Base de données : PostgreSQL via Prisma (db.prisma.io)
- Oscar est ADMIN (oscarcoachdigital@gmail.com)
- Variable GMAIL_COOKIES ajoutée le 04/02/2026

## Fiches clients
Toutes les fiches sont dans `/memory/clients/` avec INDEX.md
Clients stratégiques: Clarisse Surin (Bâtonnière), Hannah Taieb (mécène)

## Projets
### Application cabinet d'avocats avec IA
- MVP construit, phase commerciale
- Logiciel de gestion de cabinet avec IA intégrée
- Marché : avocats veulent des solutions LOCALES → gros avantage
- CA faible depuis 1 an car focus dev du logiciel → maintenant il faut VENDRE
- Gilles gère aussi la communication/campagne des prochains bâtonniers → réseau + visibilité
- Stack à documenter

### Vision "Oscar & Associés" (définie 04/02/2026)
**Concept :** VPS central avec plusieurs agents IA pour cabinets d'avocats
- Oscar = agent principal (moi)
- Agent Commercial = prospection LinkedIn/Email
- Agents Clients = un par cabinet, personnalisé (nom, avatar, WhatsApp dédié)

**Pricing validé :**
- ESSENTIEL 400€/mois (logiciel + 2h accompagnement)
- PRO 800€/mois (logiciel + 5h + hotline)
- PREMIUM 1500€/mois (logiciel + agent dédié + Gilles)

**Plan :**
1. Semaine du 04/02 : VPS + Oscar autonome
2. Semaine du 10/02 : Agent commercial
3. Mars : Premier client pilote

Doc complet : `/memory/projects/vision-oscar-associes.md`

### Widget By GK
- Fichier : C:\Users\clari\pc_widget.py
- Python + tkinter + psutil
- Démarrage auto via oscar_startup.ps1

## Oscar Dashboard (déployé 04/02/2026)
- **URL** : https://oscar.coachdigitalparis.com
- **GitHub** : github.com/eddigit/oscar-dashboard
- **Vercel Project** : oscar-dashboard
- Interface chat moderne Next.js/React
- Prêt pour connexion au backend OpenClaw

## Fork OpenClaw
- **Repo** : github.com/eddigit/openclaw
- Fork du projet officiel openclaw/openclaw
- Licence MIT - libre de modifier/redistribuer
- Base pour créer nos propres agents

## À améliorer
- Connecter le dashboard au backend OpenClaw (API)
- Créer agents spécialisés (commercial, admin)
- Explorer les services svchost pour réduire la RAM Windows
- Documenter le setup complet de Gilles pour pouvoir le reconstruire si besoin
