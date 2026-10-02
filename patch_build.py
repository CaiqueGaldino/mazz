import os

build_file = r'C:\Users\caiquegaldino\Desktop\Projetos\mand\controle_estoque_mandioca\build_release.ps1'
with open(build_file, 'r', encoding='utf-8') as f:
    content = f.read()

if '--icon' not in content:
    content = content.replace(
        '--outputDir ',
        '--outputDir  \n    --icon "windows\\runner\\resources\\app_icon.ico"'
    )

with open(build_file, 'w', encoding='utf-8') as f:
    f.write(content)
