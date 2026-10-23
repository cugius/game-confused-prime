#!/usr/bin/env python3
"""Export embedded audio and SVGs without modifying the standalone game."""
import argparse
import base64
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def exports():
    source = (ROOT / 'index.html').read_bytes()
    html = source.decode('utf-8')
    match = re.search(r'<script[^>]*id="musicAssets"[^>]*>(.*?)</script>', html, re.S)
    if not match:
        raise ValueError('musicAssets JSON not found')
    tracks = json.loads(match.group(1))
    files = {}
    manifest = {'source': 'index.html', 'source_sha256': digest(source), 'audio': [], 'icons': []}
    for key, track in tracks.items():
        data = base64.b64decode(track['data'], validate=True)
        if digest(data) != track['sha256']:
            raise ValueError(f'Audio checksum mismatch: {key}')
        if not 0 <= track['loopStart'] < track['loopEnd']:
            raise ValueError(f'Invalid loop: {key}')
        path = f'assets/audio/{key}.mp3'
        files[path] = data
        manifest['audio'].append({**{k: v for k, v in track.items() if k != 'data'},
                                  'key': key, 'path': path, 'bytes': len(data)})
    uris = dict.fromkeys(re.findall(r'url\("(data:image/svg\+xml,[^"]+)"\)', html))
    for index, uri in enumerate(uris, 1):
        data = unquote(uri.split(',', 1)[1]).encode('utf-8')
        ET.fromstring(data)
        path = f'assets/icons/icon-{index:02d}.svg'
        files[path] = data
        # Keep every CSS selector that uses this exact drawing.
        selectors = []
        for block in re.finditer(r'([^{}]+)\{([^{}]*)\}', html):
            if uri in block.group(2):
                selectors.append(block.group(1).strip())
        manifest['icons'].append({'path': path, 'sha256': digest(data),
                                  'bytes': len(data), 'selectors': selectors})
    files['assets/manifest.json'] = (json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode()
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify exports; never write files')
    args = parser.parse_args()
    files = exports()
    stale = []
    for name, data in files.items():
        path = ROOT / name
        if args.check:
            if not path.is_file() or path.read_bytes() != data:
                stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    if stale:
        parser.exit(1, 'Missing or stale exports: ' + ', '.join(stale) + '\n')
    print(f'{len(files)} exports ' + ('verified' if args.check else 'written') + '; index.html untouched')


if __name__ == '__main__':
    main()
