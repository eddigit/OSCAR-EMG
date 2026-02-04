# Guide : Synchroniser le Workspace Oscar via Git

## Situation actuelle

- **LOCAL (WSL)** : Workspace Oscar pushé sur GitHub → `github.com/eddigit/OSCAR-EMG`
- **Emergent Agent** : Workspace dans `/root/clawd/` — pas encore connecté à Git

## Étapes pour synchroniser Emergent Agent

### 1. Ouvrir le Terminal dans VS Code Emergent

Dans VS Code en ligne :
- `Ctrl+J` pour ouvrir le panneau du bas
- Ou menu ☰ → Terminal → New Terminal

### 2. Aller dans le dossier clawd

```bash
cd ~/clawd
```

### 3. Initialiser Git et connecter au repo

```bash
# Configurer Git
git config --global user.name "Oscar"
git config --global user.email "oscarcoachdigital@gmail.com"

# Initialiser le repo
git init
git remote add origin https://github.com/eddigit/OSCAR-EMG.git

# Récupérer le contenu du repo (mon workspace LOCAL)
git fetch origin
git reset --hard origin/main
```

### 4. Pour synchroniser ensuite

**Récupérer les changements (pull) :**
```bash
cd ~/clawd && git pull origin main
```

**Envoyer les changements (push) :**
```bash
cd ~/clawd && git add -A && git commit -m "Update from Emergent" && git push origin main
```

## Fichiers sensibles

Ces fichiers sont dans `.gitignore` et doivent être copiés manuellement :
- `QUICKREF.md` (tous les tokens/mots de passe)
- `tools/gmail-token*.json`
- `memory/infra/gmail-*.md`

→ Les créer manuellement sur Emergent après le clone.

## Workflow quotidien

1. **LOCAL fait un changement** → `git push`
2. **Emergent récupère** → `git pull`
3. **Emergent fait un changement** → `git push`
4. **LOCAL récupère** → `git pull`

C'est tout ! 🔄
