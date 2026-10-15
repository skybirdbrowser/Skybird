# Dependências e avisos de terceiros

O Skybird incorpora ou depende de componentes de terceiros. O código do Skybird não substitui nem elimina os termos de cada componente.

## Dependências conhecidas

- **Python** — runtime e biblioteca padrão; consulte `https://www.python.org/` para informações de licença.
- **PySide6 / Qt for Python** — bindings Python para Qt.
- **Qt WebEngine** — componente de navegação integrado ao Qt, baseado em Chromium.
- **Chromium e componentes incluídos** — possuem avisos de copyright e licenças de terceiros próprios.
- **PyInstaller** — ferramenta de empacotamento usada pelos processos de build do Windows, Linux e macOS.

Este arquivo é um índice informativo, não uma lista completa de todos os componentes binários. A árvore de dependências e os avisos exatos podem variar conforme a versão instalada e a plataforma.

## Antes de distribuir binários

1. Registre as versões exatas de Python, PySide6, Qt WebEngine, Chromium e ferramentas de empacotamento usadas no build.
2. Inclua nos pacotes os arquivos de licença, copyright e atribuição exigidos pelas distribuições oficiais dessas dependências.
3. Verifique as condições LGPL/GPL/comerciais e de redistribuição dos componentes do Qt e os avisos dos componentes Chromium incluídos.
4. Não remova páginas de créditos ou avisos de licença que façam parte do pacote distribuído.
5. Documente alterações feitas a componentes de terceiros, quando aplicável.

A publicação deste repositório sob GPL-3.0-or-later não significa que o Skybird seja titular dos direitos de componentes de terceiros ou que todos os requisitos de distribuição binária estejam automaticamente satisfeitos.
