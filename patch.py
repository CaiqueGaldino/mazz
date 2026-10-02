import time
import os
import re

service_file = r'C:\Users\caiquegaldino\Desktop\Projetos\mand\controle_estoque_mandioca\lib\services\firebase_sync_service.dart'
with open(service_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Add a timer
if 'Timer.periodic(const Duration(minutes: 1)' not in content:
    content = content.replace(
        'Future<void> initialize() async {',
        'Future<void> initialize() async {\n      _connectivityTimer = Timer.periodic(const Duration(minutes: 1), (_) => syncAllToCloud());\n'
    )

with open(service_file, 'w', encoding='utf-8') as f:
    f.write(content)
