"""
By GK - Widget PC Optimizer
Créé par Oscar pour Gilles
"""

import tkinter as tk
from tkinter import ttk
import psutil
import subprocess
import threading
import os
import ctypes
import sys
import time

# --- Config ---
REFRESH_MS = 3000
WINDOW_WIDTH = 280
WINDOW_HEIGHT = 340

# Whitelist STRICTE : SEULS ces processus survivent à Optimiser
# Tout le reste est fermé sans exception
PROTECTED = {
    # Oscar / OpenClaw / WSL
    "node.exe", "wsl.exe", "wslhost.exe", "wslservice.exe",
    "wslrelay.exe", "vmmem", "vmmemwsl", "vmwp.exe", "vmcompute.exe",
    # Le widget
    "python.exe", "pythonw.exe", "python3.exe",
    # Windows critique (plantage si fermé)
    "explorer.exe", "dwm.exe", "csrss.exe", "smss.exe", "lsass.exe",
    "lsaiso.exe", "services.exe", "svchost.exe", "wininit.exe",
    "winlogon.exe", "fontdrvhost.exe", "sihost.exe", "taskhostw.exe",
    "runtimebroker.exe", "shellexperiencehost.exe",
    "startmenuexperiencehost.exe", "searchhost.exe", "textinputhost.exe",
    "ctfmon.exe", "conhost.exe", "dllhost.exe", "audiodg.exe",
    "system", "registry", "idle",
    # Sécurité Windows (pas touche)
    "securityhealthsystray.exe", "msmpeng.exe", "nissrv.exe",
    "securityhealthservice.exe", "microsoftsecurityapp.exe",
    "mpdefendercoreservice.exe", "smartscreen.exe", "sgrmbroker.exe",
    # Drivers essentiels
    "rtkauduservice64.exe", "intelaudioservice.exe",
    "dashost.exe", "wudfhost.exe", "unsecapp.exe",
    "esif_uf.exe", "dptf_helper.exe", "igfxcuiservicen.exe",
    "igfxemn.exe",
    # PowerShell/cmd (pour qu'Oscar continue)
    "powershell.exe", "pwsh.exe", "cmd.exe", "bash.exe",
    # PowerToys (Gilles l'utilise pour souris/clavier multi-PC)
    "powertoys.exe", "powertoys.mousewithoutborders.exe",
    "powertoys.mousewithoutbordershelper.exe",
    "powertoys.alwaysontop.exe", "powertoys.mousejumpui.exe",
    # Divers système
    "wmiprvse.exe", "searchindexer.exe", "ngciso.exe",
    "backgroundtaskhost.exe", "secure system",
}

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_color(percent):
    if percent < 70:
        return "#4CAF50"
    elif percent < 85:
        return "#FF9800"
    else:
        return "#F44336"

def get_label(percent):
    if percent < 70:
        return "OK"
    elif percent < 85:
        return "Attention"
    else:
        return "Saturé !"

class PCWidget(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("⚡ By GK")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.configure(bg="#1e1e2e")

        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = screen_w - WINDOW_WIDTH - 20
        y = screen_h - WINDOW_HEIGHT - 60
        self.geometry(f"+{x}+{y}")

        style = ttk.Style()
        style.theme_use("default")
        style.configure("green.Horizontal.TProgressbar", troughcolor="#2e2e3e", background="#4CAF50")
        style.configure("orange.Horizontal.TProgressbar", troughcolor="#2e2e3e", background="#FF9800")
        style.configure("red.Horizontal.TProgressbar", troughcolor="#2e2e3e", background="#F44336")

        tk.Label(self, text="⚡ By GK", font=("Segoe UI", 13, "bold"),
                 bg="#1e1e2e", fg="#80cbc4").pack(pady=(10, 5))

        # --- RAM ---
        self.ram_title = tk.Label(self, text="🧠 RAM", font=("Segoe UI", 11, "bold"),
                                   bg="#1e1e2e", fg="white", anchor="w")
        self.ram_title.pack(fill="x", padx=15, pady=(5, 2))
        self.ram_bar = ttk.Progressbar(self, length=250, mode="determinate")
        self.ram_bar.pack(padx=15, pady=2)
        self.ram_label = tk.Label(self, text="", font=("Segoe UI", 10),
                                   bg="#1e1e2e", fg="#aaaaaa", anchor="w")
        self.ram_label.pack(fill="x", padx=15)
        self.ram_status = tk.Label(self, text="", font=("Segoe UI", 9, "bold"),
                                    bg="#1e1e2e", anchor="w")
        self.ram_status.pack(fill="x", padx=15, pady=(0, 5))

        # --- Disque ---
        self.disk_title = tk.Label(self, text="💾 Disque C:", font=("Segoe UI", 11, "bold"),
                                    bg="#1e1e2e", fg="white", anchor="w")
        self.disk_title.pack(fill="x", padx=15, pady=(5, 2))
        self.disk_bar = ttk.Progressbar(self, length=250, mode="determinate")
        self.disk_bar.pack(padx=15, pady=2)
        self.disk_label = tk.Label(self, text="", font=("Segoe UI", 10),
                                    bg="#1e1e2e", fg="#aaaaaa", anchor="w")
        self.disk_label.pack(fill="x", padx=15)
        self.disk_status = tk.Label(self, text="", font=("Segoe UI", 9, "bold"),
                                     bg="#1e1e2e", anchor="w")
        self.disk_status.pack(fill="x", padx=15, pady=(0, 10))

        # --- Bouton ---
        self.opt_btn = tk.Button(self, text="⚡ Optimiser", font=("Segoe UI", 11, "bold"),
                                  bg="#4CAF50", fg="white", activebackground="#388E3C",
                                  relief="flat", cursor="hand2", height=1,
                                  command=self.run_optimize)
        self.opt_btn.pack(fill="x", padx=15, pady=(5, 5))

        # --- Résultat ---
        self.result_label = tk.Label(self, text="", font=("Segoe UI", 9),
                                      bg="#1e1e2e", fg="#80cbc4", wraplength=250,
                                      justify="left", anchor="w")
        self.result_label.pack(fill="x", padx=15, pady=(0, 10))

        self.update_stats()

    def update_bar_style(self, bar, percent):
        if percent < 70:
            bar.configure(style="green.Horizontal.TProgressbar")
        elif percent < 85:
            bar.configure(style="orange.Horizontal.TProgressbar")
        else:
            bar.configure(style="red.Horizontal.TProgressbar")

    def update_stats(self):
        ram = psutil.virtual_memory()
        ram_pct = ram.percent
        ram_used_gb = round(ram.used / (1024**3), 1)
        ram_total_gb = round(ram.total / (1024**3), 1)
        self.ram_bar["value"] = ram_pct
        self.update_bar_style(self.ram_bar, ram_pct)
        self.ram_label.config(text=f"{ram_used_gb} Go / {ram_total_gb} Go ({ram_pct}%)")
        self.ram_status.config(text=get_label(ram_pct), fg=get_color(ram_pct))

        disk = psutil.disk_usage("C:\\")
        disk_pct = disk.percent
        disk_used_gb = round(disk.used / (1024**3))
        disk_total_gb = round(disk.total / (1024**3))
        disk_free_gb = round(disk.free / (1024**3))
        self.disk_bar["value"] = disk_pct
        self.update_bar_style(self.disk_bar, disk_pct)
        self.disk_label.config(text=f"{disk_used_gb} Go / {disk_total_gb} Go — {disk_free_gb} Go libres")
        self.disk_status.config(text=get_label(disk_pct), fg=get_color(disk_pct))

        self.after(REFRESH_MS, self.update_stats)

    def run_optimize(self):
        self.opt_btn.config(state="disabled", text="⏳ Nettoyage total...", bg="#666666")
        self.result_label.config(text="")
        thread = threading.Thread(target=self.optimize, daemon=True)
        thread.start()

    def optimize(self):
        ram_before = psutil.virtual_memory().used
        disk_before = psutil.disk_usage("C:\\").used
        killed_apps = []
        my_pid = os.getpid()

        # 1. FERMER TOUT via taskkill (plus fiable que psutil)
        # D'abord lister ce qu'on va tuer
        targets = []
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                pname = proc.info['name'] or ""
                pid = proc.info['pid']
                if pid == my_pid or pid == 0 or pid == 4:
                    continue
                if pname.lower() in PROTECTED:
                    continue
                targets.append((pid, pname))
            except:
                pass

        # Tuer via taskkill /F (force) — bien plus efficace
        for pid, pname in targets:
            try:
                subprocess.run(
                    ["taskkill", "/F", "/PID", str(pid)],
                    capture_output=True, timeout=5
                )
                app = pname.replace(".exe", "")
                if app not in killed_apps:
                    killed_apps.append(app)
            except:
                pass

        # 2. Fichiers temporaires
        temp_count = 0
        try:
            temp_dir = os.path.expandvars(r"%TEMP%")
            for root, dirs, files in os.walk(temp_dir):
                for f in files:
                    try:
                        os.remove(os.path.join(root, f))
                        temp_count += 1
                    except:
                        pass
        except:
            pass

        # 3. Corbeille
        try:
            ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0x07)
        except:
            pass

        # Résultat
        time.sleep(3)
        ram_after = psutil.virtual_memory().used
        disk_after = psutil.disk_usage("C:\\").used

        ram_saved = max(0, (ram_before - ram_after)) / (1024**3)
        disk_saved = max(0, (disk_before - disk_after)) / (1024**3)

        result_lines = []
        if killed_apps:
            notable = [a for a in killed_apps if len(a) > 3][:10]
            if notable:
                result_lines.append("Fermé : " + ", ".join(notable))
            result_lines.append(f"({len(killed_apps)} processus fermés)")
        if temp_count > 0:
            result_lines.append(f"Temp : {temp_count} fichiers nettoyés")
        result_lines.append(f"✅ Libéré : {ram_saved:.1f} Go RAM, {disk_saved:.1f} Go disque")

        result_text = "\n".join(result_lines)
        self.after(0, lambda: self.opt_btn.config(
            state="normal", text="⚡ Optimiser", bg="#4CAF50"))
        self.after(0, lambda: self.result_label.config(text=result_text))

if __name__ == "__main__":
    app = PCWidget()
    app.mainloop()
