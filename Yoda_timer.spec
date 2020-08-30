# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Yoda_timer.py'],
             pathex=['.'],
             binaries=[],
             datas=[('resourses/pictures/yoda.png', 'resourses/pictures'), ('resourses/pictures/yoda_icon.png', 'resourses/pictures'), ('resourses/font/LCD1.ttf', 'resourses/font'), ('resourses/font/DroidSans.ttf', 'resourses/font'), ('resourses/sounds/clock.wav', 'resourses/sounds')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Yoda Timer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False, icon='C:/Users/1/Desktop/Питон/pygame/Yoda_timer/resourses/pictures/yoda_icon.ico')
