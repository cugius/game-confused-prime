#!/usr/bin/env python3
"""Ricostruisce index.html (l'unico file distribuito) dai sorgenti in src/.

  python3 scripts/build.py          # scrive index.html
  python3 scripts/build.py --check  # esce con errore se index.html non corrisponde ai sorgenti

Non modificare index.html a mano: modificare src/ e rigenerare.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT = ROOT / "index.html"
MUSIC_OPEN = '<script type="application/json" id="musicAssets">'


def read(name):
    return (SRC / name).read_text(encoding="utf-8")


def build():
    version = read("VERSION").strip()
    return (
        read("head.html")
        + read("style.css")
        + "\n"
        + read("body.html")
        + MUSIC_OPEN
        + read("music.json")
        + "</script>\n<script>\n"
        + read("app.js")
        + "\n"
        + read("tail.html")
    ).replace("{{VERSION}}", version)


def main(argv):
    text = build()
    if "--check" in argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != text:
            print("index.html non corrisponde a src/: esegui python3 scripts/build.py")
            return 1
        print("index.html aggiornato rispetto a src/")
        return 0
    OUT.write_text(text, encoding="utf-8", newline="")
    print(f"scritto {OUT} ({len(text)} caratteri)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
