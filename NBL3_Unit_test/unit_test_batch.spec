# -*- mode: python -*-

block_cipher = None


a = Analysis(['unit_test_batch.py'],
             pathex=['C:\\Users\\Chao\\Documents\\github\\gakki_python\\NBL3_Unit_test'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='unit_test_batch',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
