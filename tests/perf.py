"""Misure di memoria e frame (MEM-04/05). Richiede Playwright con Chromium.

  python3 tests/perf.py

Stampa l'heap JavaScript dopo ogni ciclo partita/menu/home e il tempo medio tra frame durante la partita.
Le misure in headless non sostituiscono il profilo su dispositivo fisico.
"""
import os
import pathlib
import statistics
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
URL = (ROOT / "index.html").as_uri()


def heap(cdp, pg):
    cdp.send("HeapProfiler.collectGarbage")
    pg.wait_for_timeout(120)
    cdp.send("HeapProfiler.collectGarbage")
    m = cdp.send("Runtime.getHeapUsage")
    return m["usedSize"] / 1048576


def main():
    launch = {"executable_path": os.environ["CHROME_PATH"]} if os.environ.get("CHROME_PATH") else {}
    with sync_playwright() as p:
        b = p.chromium.launch(**launch)
        ctx = b.new_context(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True)
        ctx.add_init_script("localStorage.setItem('cbm-primi-v1',JSON.stringify({tutorial:true,music:false,sound:false,language:'en'}))")
        pg = ctx.new_page()
        errors = []
        pg.on("pageerror", lambda e: errors.append(str(e)))
        pg.goto(URL)
        pg.wait_for_timeout(300)
        cdp = ctx.new_cdp_session(pg)
        cdp.send("Runtime.enable")

        samples = []
        for cycle in range(1, 11):
            pg.click("#train"); pg.wait_for_timeout(250)
            pg.evaluate("goHome()")
            pg.click("#homeSettings"); pg.wait_for_timeout(120)
            pg.evaluate("document.getElementById('sheetClose').click()")
            pg.click("#homeInfo"); pg.wait_for_timeout(120)
            pg.evaluate("document.getElementById('sheetClose').click()")
            pg.evaluate("document.dispatchEvent(new Event('visibilitychange'))")
            samples.append(heap(cdp, pg))
            print(f"ciclo {cycle:2d}: heap {samples[-1]:.2f} MB, nodi DOM {pg.evaluate('document.getElementsByTagName(\"*\").length')}")

        growth = samples[-1] - samples[1]
        print(f"crescita dal ciclo 2 al 10: {growth:+.2f} MB")

        pg.click("#train"); pg.wait_for_timeout(300)
        deltas = pg.evaluate("""new Promise(res=>{const t=[];let last=null;const step=ts=>{if(last!==null)t.push(ts-last);last=ts;if(t.length<180)requestAnimationFrame(step);else res(t)};requestAnimationFrame(step)})""")
        print(f"frame durante la partita: media {statistics.mean(deltas):.1f} ms, p95 {sorted(deltas)[int(len(deltas)*0.95)]:.1f} ms (headless)")
        ctx.close()
        b.close()
    if errors:
        print("errori JS:", errors)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
