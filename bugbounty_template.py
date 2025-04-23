# bugbounty_template.py
"""
Script inicial para automatizar la fase de reconocimiento en un programa de Bug Bounty.
Este script hace uso de subfinder, httpx, y nmap para identificar objetivos activos.
"""

import os
import subprocess
from datetime import datetime

# Configuración inicial
TARGET = input("Dominio objetivo (sin https): ").strip()
DIRECTORY = f"recon_{TARGET.replace('.', '_')}_{datetime.now().strftime('%Y%m%d')}"
os.makedirs(DIRECTORY, exist_ok=True)

print(f"[+] Carpeta creada: {DIRECTORY}")

# 1. Subfinder - Enumeración de subdominios
print("[+] Ejecutando subfinder...")
subfinder_output = os.path.join(DIRECTORY, "subdomains.txt")
subprocess.run(["subfinder", "-d", TARGET, "-silent", "-o", subfinder_output])

# 2. httpx - Verificar qué dominios están activos
print("[+] Verificando dominios activos con httpx...")
httpx_output = os.path.join(DIRECTORY, "live_subdomains.txt")
with open(httpx_output, "w") as out:
    subprocess.run(["httpx", "-l", subfinder_output, "-silent"], stdout=out)

# 3. nmap - Escaneo de puertos básicos
print("[+] Escaneando puertos con nmap (top 1000)...")
with open(httpx_output, "r") as live_file:
    for line in live_file:
        domain = line.strip().replace("https://", "").replace("http://", "")
        domain_dir = os.path.join(DIRECTORY, domain)
        os.makedirs(domain_dir, exist_ok=True)
        nmap_out = os.path.join(domain_dir, "nmap.txt")
        subprocess.run(["nmap", "-T4", "-sV", "--top-ports", "1000", "-oN", nmap_out, domain])

print("[+] Reconocimiento básico finalizado. Revisar la carpeta:", DIRECTORY)
