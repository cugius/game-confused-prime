"""Test funzionali di Confused Prime. Richiede Playwright con Chromium.

  pip install playwright && python -m playwright install chromium
  python3 tests/test_app.py

Variabile opzionale CHROME_PATH per usare un Chromium già installato.
"""
import json
import os
import pathlib
import subprocess
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
URL = (ROOT / "index.html").as_uri()
IOS_UA = ("Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 "
          "(KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1")
results = []


def check(name, ok, detail=""):
    results.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + (f" — {detail}" if detail else ""))


def new_page(browser, ua=None, w=390, h=844, prefs=None):
    kwargs = {"viewport": {"width": w, "height": h}, "has_touch": True, "is_mobile": True}
    if ua:
        kwargs["user_agent"] = ua
    ctx = browser.new_context(**kwargs)
    base = {"tutorial": True, "language": "it"}
    base.update(prefs or {})
    ctx.add_init_script("localStorage.setItem('cbm-primi-v1',JSON.stringify(%s))" % json.dumps(base))
    pg = ctx.new_page()
    errors = []
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto(URL)
    pg.wait_for_timeout(300)
    return ctx, pg, errors


def main():
    # 1. build coerente con i sorgenti
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build.py"), "--check"], capture_output=True, text=True)
    check("build: index.html corrisponde a src/", r.returncode == 0, r.stdout.strip())
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "lint.py")], capture_output=True, text=True)
    check("lint: nessun pattern vietato", r.returncode == 0, (r.stdout + r.stderr).strip().splitlines()[-1] if (r.stdout + r.stderr).strip() else "")

    launch = {"executable_path": os.environ["CHROME_PATH"]} if os.environ.get("CHROME_PATH") else {}
    with sync_playwright() as p:
        b = p.chromium.launch(**launch)

        # 2. traduzioni: ogni riga ha sei lingue non vuote
        ctx, pg, errs = new_page(b)
        rows = pg.evaluate("I18N_ROWS")
        bad = [r[0] for r in rows if len(r) != 6 or any(not str(c).strip() for c in r)]
        check("i18n: ogni riga ha 6 lingue non vuote", not bad, f"{len(rows)} righe" + (f", difettose: {bad[:3]}" if bad else ""))

        # 3. aptica e riduci movimento per piattaforma
        pg.click("#homeSettings"); pg.click("#stab-audio"); pg.wait_for_timeout(150)
        check("aptica: visibile fuori da iOS", pg.evaluate("!!document.getElementById('settingHaptic')"))
        check("riduci movimento: presente", pg.evaluate("!!document.getElementById('settingMotion')"))
        pg.click("#settingMotion")
        check("riduci movimento: attiva la classe", pg.evaluate("document.documentElement.classList.contains('reduce-motion')"))
        check("riduci movimento: salvato", pg.evaluate("JSON.parse(localStorage.getItem('cbm-primi-v1')).reduceMotion===true"))
        pg.click("#settingMotion")
        check("riduci movimento: si disattiva", not pg.evaluate("document.documentElement.classList.contains('reduce-motion')"))
        check("nessun errore JS", not errs, "; ".join(errs))
        ctx.close()

        ctx, pg, errs = new_page(b, ua=IOS_UA)
        pg.click("#homeSettings"); pg.click("#stab-audio"); pg.wait_for_timeout(150)
        check("aptica: nascosta su iOS", not pg.evaluate("!!document.getElementById('settingHaptic')"))
        check("riduci movimento: presente su iOS", pg.evaluate("!!document.getElementById('settingMotion')"))
        ctx.close()

        # 4. zoom bloccato solo sul campo di gioco
        ctx, pg, errs = new_page(b)
        pg.click("#train"); pg.wait_for_timeout(300)
        on_board = pg.evaluate("(()=>{const e=new Event('gesturestart',{cancelable:true,bubbles:true});document.getElementById('board').dispatchEvent(e);return e.defaultPrevented})()")
        pg.click("#pause"); pg.wait_for_timeout(150)
        in_menu = pg.evaluate("(()=>{const e=new Event('gesturestart',{cancelable:true,bubbles:true});document.getElementById('modal').dispatchEvent(e);return e.defaultPrevented})()")
        check("zoom: bloccato sul campo di gioco", on_board)
        check("zoom: libero nel menu di pausa", not in_menu)
        pg.evaluate("document.getElementById('resume').click()"); pg.wait_for_timeout(100)
        pg.evaluate("goHome()"); pg.wait_for_timeout(100)
        on_home = pg.evaluate("(()=>{const e=new Event('gesturestart',{cancelable:true,bubbles:true});document.getElementById('home').dispatchEvent(e);return e.defaultPrevented})()")
        check("zoom: libero in home", not on_home)
        ctx.close()

        # 5. area di tocco 44×44 per Pausa e Suggerimento (pseudo-elemento)
        ctx, pg, errs = new_page(b, w=320, h=568)
        pg.click("#train"); pg.wait_for_timeout(300)
        sizes = pg.evaluate("""(()=>{const f=(el)=>{const s=getComputedStyle(el,'::after');return [parseFloat(s.width),parseFloat(s.height)]};
            return {pause:f(document.getElementById('pause')),hint:f(document.getElementById('hint'))}})()""")
        check("UX-08: area di tocco Pausa ≥ 44×44 su 320×568", sizes["pause"][0] >= 44 and sizes["pause"][1] >= 44, str(sizes["pause"]))
        check("UX-08: area di tocco Suggerimento ≥ 44 px in altezza", sizes["hint"][1] >= 44, str(sizes["hint"]))
        ctx.close()

        # 6. salvataggio v1 con valori fuori tipo: si carica senza errori e si corregge
        ctx = b.new_context(viewport={"width": 390, "height": 844})
        ctx.add_init_script("localStorage.setItem('cbm-primi-v1',JSON.stringify({hintsUsed:'x',bestNormal:-5,hintsDay:7,language:'it'}))")
        pg = ctx.new_page(); errs = []; pg.on("pageerror", lambda e: errs.append(str(e))); pg.goto(URL); pg.wait_for_timeout(200)
        fixed = pg.evaluate("({h:prefs.hintsUsed,b:prefs.bestNormal,d:prefs.hintsDay,v:prefs.v,l:prefs.language})")
        check("salvataggi: valori fuori tipo corretti", fixed == {"h": 0, "b": 0, "d": "", "v": 2, "l": "it"} and not errs, json.dumps(fixed))
        ctx.close()

        # 7. layout: home senza scroll su schermi bassi
        for w, h in [(390, 844), (320, 568), (568, 320), (844, 340), (640, 360)]:
            ctx, pg, errs = new_page(b, w=w, h=h)
            fits = pg.evaluate("document.documentElement.scrollHeight<=innerHeight+1 && document.documentElement.scrollWidth<=innerWidth+1")
            check(f"layout: home senza scroll a {w}×{h}", fits)
            ctx.close()

        # 8. lingua e controlli: testi di input a 16 px (no zoom automatico iOS)
        ctx, pg, errs = new_page(b)
        pg.click("#homeSettings"); pg.wait_for_timeout(100)
        fs = pg.evaluate("parseFloat(getComputedStyle(document.getElementById('languageSelect')).fontSize)")
        check("input: select lingua a 16 px", fs >= 16, f"{fs}px")
        pg.select_option("#languageSelect", "de"); pg.wait_for_timeout(150)
        check("lingua: cambio applicato e scheda conservata", pg.evaluate("document.documentElement.lang")=="de" and pg.evaluate("document.querySelector('.sheet-tabs [aria-selected=true]').dataset.tab")=="game")
        ctx.close()

        # 8b. versione mostrata coincide con src/VERSION
        ctx, pg, errs = new_page(b)
        ver = (ROOT / "src" / "VERSION").read_text(encoding="utf-8").strip()
        footer = pg.evaluate("document.querySelector('.home .footer').textContent")
        check("versione: footer coerente con src/VERSION", f"v{ver}" in footer, footer)
        ctx.close()

        # 9. tutorial isolato dalla raccolta
        ctx, pg, errs = new_page(b)
        pg.click("#train"); pg.wait_for_timeout(300)
        src = (ROOT / "src" / "app.js").read_text(encoding="utf-8")
        check("tutorial: nessuna registrazione dei primi", "if(kind==='fuse'&&!tutorial)recordPrime" in src or "!tutorial)recordPrime" in src)
        ctx.close()

        b.close()

    failed = [n for n, ok in results if not ok]
    print(f"\n{len(results) - len(failed)}/{len(results)} test superati")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
