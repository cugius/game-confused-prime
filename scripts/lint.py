#!/usr/bin/env python3
"""Controlli statici su src/app.js: pattern vietati e sintassi. Esce con errore se qualcosa non va.

  python3 scripts/lint.py
"""
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
JS = (ROOT / "src" / "app.js").read_text(encoding="utf-8")
HTML = (ROOT / "src" / "body.html").read_text(encoding="utf-8") + (ROOT / "src" / "head.html").read_text(encoding="utf-8")
errors = []

FORBIDDEN = {
    r"window\.__\w+": "variabile globale di debug (CODE-06)",
    r"\bconsole\.(log|debug|table)\(": "log di debug nel rilascio (CODE-06)",
    r"\bdebugger\b": "breakpoint nel rilascio (CODE-06)",
    r"\balert\(": "dialogo bloccante",
}
for pat, msg in FORBIDDEN.items():
    for m in re.finditer(pat, JS):
        line = JS[: m.start()].count("\n") + 1
        errors.append(f"app.js:{line}: {msg}: {m.group(0)}")

# Nessun URL esterno: le uniche eccezioni sono i namespace SVG.
for m in re.finditer(r"https?://[^\s'\"<>)]+", JS + HTML):
    if "www.w3.org" in m.group(0):
        continue
    errors.append(f"URL esterno: {m.group(0)}")

# innerHTML: elencati per la revisione manuale (SEC-04), non bloccanti.
inner = [JS[: m.start()].count("\n") + 1 for m in re.finditer(r"\.innerHTML\s*=", JS)]
print(f"innerHTML in app.js: {len(inner)} assegnazioni (righe {', '.join(map(str, inner))}). Revisione in docs/CANON.md.")

node = shutil.which("node")
if node:
    script = ROOT / "src" / "app.js"
    r = subprocess.run([node, "--check", str(script)], capture_output=True, text=True)
    if r.returncode != 0:
        errors.append("sintassi JavaScript: " + r.stderr.strip())
else:
    print("node non trovato: controllo di sintassi saltato (il test funzionale lo copre).")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("lint ok")
