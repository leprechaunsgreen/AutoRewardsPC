# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path
import os

BASE_DIR = Path(os.getcwd())

block_cipher = None

a = Analysis(
    [str(BASE_DIR / 'src' / '__main__.py')],
    pathex=[str(BASE_DIR / 'src')],
    binaries=[],
    datas=[
        (str(BASE_DIR / 'src' / 'assets'), 'assets'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AutoRewardsPC',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon=str(BASE_DIR / 'src' / 'assets' / 'icon.ico'),
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='AutoRewardsPC',
)
