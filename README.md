# 🐞 Bug Bounty Hunter Checklist

Este checklist está diseñado para ayudarme a mantener un flujo organizado y profesional en mis procesos de búsqueda de vulnerabilidades. Ideal para plataformas como HackerOne, Bugcrowd, Intigriti y programas privados.

---

## 🔐 1. Preparación y Legalidad

- [ ] ✅ Crear y mantener perfiles en plataformas de Bug Bounty.
- [ ] 📄 Leer y aceptar las reglas del programa (Scope, OOS, NDA si aplica).
- [ ] ⚖️ No realizar ataques destructivos o afectar a otros usuarios.
- [ ] 👤 Usar cuentas de prueba o secundarias para pruebas.

---

## 🌐 2. Recolección de Información (Recon)

### Herramientas:
- `Amass`, `Subfinder`, `Assetfinder` – Enumeración de subdominios
- `httpx`, `httprobe` – Verificación de dominios activos
- `nmap`, `naabu` – Escaneo de puertos
- `waybackurls`, `gau`, `hakrawler` – URLs históricas y endpoints
- `dnsx`, `shuffledns` – DNS brute force
- `gf`, `qsreplace` – Parámetros vulnerables
- `ffuf`, `dirsearch` – Fuzzing de directorios y archivos

### Checklist Recon:
- [ ] Subdominios identificados
- [ ] Puertos abiertos mapeados
- [ ] Endpoints sensibles detectados
- [ ] Parámetros comunes extraídos
- [ ] Identificación de tecnologías con `Wappalyzer` o `whatweb`

---

## 🧪 3. Testing Manual y Automatizado

### 🛠 Herramientas principales:
- `Burp Suite` (+ extensiones: ActiveScan++, Param Miner, Turbo Intruder)
- `OWASP ZAP`, `Postman`, `Insomnia`

### Vulnerabilidades a probar:
- [ ] XSS (Reflected, Stored, DOM-based)
- [ ] SQL Injection (Classic, Blind, Time-based)
- [ ] CSRF (en formularios críticos)
- [ ] IDOR (control de acceso)
- [ ] LFI / RFI / RCE
- [ ] Open Redirect
- [ ] SSRF (usar `Interactsh`)
- [ ] Subdomain Takeover
- [ ] Fuga de tokens / claves API
- [ ] Configuraciones inseguras (headers, CORS, etc.)

---

## 🧰 4. APIs y Aplicaciones Móviles

### Testing API:
- [ ] Revisar documentación pública
- [ ] Testear endpoints con Postman/Burp
- [ ] Autorización: pruebas con tokens ajenos o sin token
- [ ] API Rate Limit Testing

### Mobile:
- [ ] Decompilar APK (`APKTool`, `Jadx`)
- [ ] Análisis estático (`MobSF`)
- [ ] Hooking dinámico (`Frida`, `Xposed`)
- [ ] Análisis de tráfico desde app móvil a backend

---

## 🔍 5. Credenciales y Fugas

- [ ] Buscar leaks con `GitLeaks`, `TruffleHog`, `GitDorker`
- [ ] Google Dorking (indexación de información sensible)
- [ ] Buscar credenciales filtradas en `HaveIBeenPwned`, `DeHashed`
- [ ] Enumeración de correos con `Hunter.io`

---

## 🧠 6. Reporte Profesional

- [ ] Título claro del hallazgo
- [ ] Descripción detallada y paso a paso
- [ ] Evidencias: capturas, requests/response, video
- [ ] Impacto claro y justificado
- [ ] Recomendación de mitigación
- [ ] Inglés técnico correcto y conciso

---

## 🔐 7. Seguridad Personal

- [ ] Usar VPN (WireGuard / ProtonVPN)
- [ ] Configurar entorno en VM o contenedor Docker
- [ ] Separar entorno de trabajo del personal

---

## 📦 Repos y Recursos útiles

- [`PayloadsAllTheThings`](https://github.com/swisskyrepo/PayloadsAllTheThings)
- [`BugBountyHunterChecklist`](https://github.com/EdOverflow/BugBountyHunterChecklist)
- [`HackTricks`](https://book.hacktricks.xyz/)
- [`Awesome-Bugbounty`](https://github.com/djadmin/awesome-bug-bounty)

---

## 🧱 To-Do personal

- [ ] Automatizar flujo de recon con scripts
- [ ] Mantener histórico de hallazgos
- [ ] Seguir aprendiendo y documentando técnicas nuevas
- [ ] Colaborar con la comunidad (writeups, blog, tools)

---

