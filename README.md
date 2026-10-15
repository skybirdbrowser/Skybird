# Skybird 0.4.0

**Skybird** é um navegador desktop independente, com foco em leveza, simplicidade e privacidade básica. A interface é minimalista e o projeto usa Python, PySide6 e Qt WebEngine (Chromium).

> **Estado:** versão experimental em desenvolvimento. A interface e o instalador devem ser validados em cada sistema antes de uma distribuição ampla.

## Estrutura do projeto

- `skybird/`: código principal do navegador, separado por responsabilidade.
- `assets/`: página inicial, ícones SVG e recursos visuais.
- `installer/`: interface e lógica do instalador/desinstalador do Windows.
- `tests/`: testes automatizados da lógica e dos arquivos do projeto.
- `scripts/build/`: scripts para gerar pacotes de Windows, Linux e macOS.
- `scripts/run/`: atalhos de execução a partir do código-fonte.
- `docs/`: documentação técnica e instruções de distribuição.
- `.github/`: workflows de teste/compilação e modelos de issues.

## Funcionalidades

- Interface minimalista em azul e branco, com página inicial local.
- Abas: criar, fechar, reordenar e reabrir; menu de contexto e favicons.
- Barra de endereço que aceita URLs, endereços locais e pesquisas na web.
- Favoritos, histórico, localizar texto na página, zoom e tela cheia.
- Downloads para a pasta de downloads do sistema, com nomes tratados para evitar sobrescrita.
- Restauração da sessão; abas inativas restauradas sob demanda.
- Pedidos de câmera, microfone, localização e notificações com solicitação de permissão.
- Opções básicas de privacidade, incluindo bloqueio de rastreadores conhecidos, controle de cookies de terceiros e limpeza de dados.

## Plataformas

O código contém scripts de execução para Windows, Linux e macOS. **No momento, a versão empacotada/testada pelo mantenedor é a de Windows; as execuções e os instaladores de Linux/macOS ainda precisam de validação nativa.** Não interprete a existência dos scripts como garantia de compatibilidade em toda distribuição ou versão do sistema.

## Requisitos de desenvolvimento

- Python 3.11, 3.12 ou 3.13.
- Internet para instalar as dependências indicadas em `requirements.txt`.
- Ambiente gráfico compatível com Qt WebEngine.

## Executar a partir do código-fonte

| Sistema | Comando |
|---|---|
| Windows | Execute `scripts\run\run_skybird.bat` |
| Linux | `bash scripts/run/run_skybird.sh` |
| macOS | `bash scripts/run/run_skybird.sh` ou abra `scripts/run/run_skybird.command` |

Os scripts criam um ambiente virtual `.venv` e instalam as dependências na primeira execução.

Execução manual:

```bash
python -m venv .venv
# Ative o ambiente virtual no seu sistema e depois execute:
python -m pip install -r requirements.txt
python main.py
```

Em Debian/Ubuntu, se Qt indicar bibliotecas de sistema ausentes, talvez seja necessário instalar dependências como `libxcb-cursor0`, `libnss3`, `libasound2` (ou `libasound2t64` em versões recentes), `libxkbcommon-x11-0` e `libegl1`.

## Testes

Os testes automatizados de lógica não precisam abrir a interface gráfica nem instalar PySide6:

```bash
python -m unittest discover -s tests -v
```

Esses testes não substituem a validação manual do navegador real. Antes de publicar uma release, teste navegação, pesquisa, abas, downloads, reprodução de vídeo, suspensão/reativação de abas e instalação no sistema de destino.

## Gerar instalador para Windows

Em Windows, com Python 3.11–3.13 e acesso à internet, execute `scripts/build/build_windows.bat`. Ele prepara o ambiente de build e utiliza PyInstaller para gerar o instalador na pasta `dist`. O processo ainda precisa ser executado e validado em Windows antes de declarar o instalador como testado.

## Gerar pacotes para Linux e macOS

Os scripts `scripts/build/build_linux.sh`/`scripts/build/build_linux.py` geram `.deb` e `.tar.gz` em Linux; `scripts/build/build_macos.command`/`scripts/build/build_macos.py` geram `.dmg` e `.zip` em macOS. Os builds precisam rodar no sistema operacional de destino. Para gerar os pacotes sem ter essas máquinas, publique o código-fonte completo e execute o workflow **Build packages (Linux and macOS)** em `.github/workflows/build-linux-macos.yml`.

As instruções completas estão em [`docs/INSTALLADORES-LINUX-MAC.md`](docs/INSTALLADORES-LINUX-MAC.md). Os pacotes são não assinados/não notarizados inicialmente e precisam ser testados nos sistemas de destino antes de serem anunciados como releases estáveis.

## Leveza e privacidade

O projeto tenta reduzir recursos desnecessários por meio de restauração de abas sob demanda, suspensão de abas ociosas, gravação de dados em lote e cache limitado. Isso **não é uma garantia de consumo específico de RAM/CPU**; qualquer afirmação de desempenho deve ser sustentada por medições reproduzíveis. Consulte [`docs/MOTOR.md`](docs/MOTOR.md).

As proteções de privacidade são básicas e não tornam o navegador anônimo nem garantem bloqueio total de rastreamento. O Qt WebEngine recebe atualizações de segurança por meio das versões do PySide6/Qt; manter essas dependências atualizadas é importante.

## Licença do código

O código-fonte original do Skybird está disponível sob **GNU General Public License v3.0 ou qualquer versão posterior (GPL-3.0-or-later)**. Consulte [`LICENSE`](LICENSE).

O nome **Skybird**, o logotipo e os arquivos que reproduzem a identidade visual oficial não são licenciados pela GPL. O uso dessas marcas e dos ativos de marca é tratado separadamente em [`TRADEMARKS.md`](TRADEMARKS.md). É permitido criar e distribuir forks conforme a GPL, mas uma versão modificada não pode se apresentar como a versão oficial nem reutilizar o nome/logotipo como sua própria identidade.

## Dependências de terceiros

O Skybird utiliza PySide6, Qt WebEngine e Chromium, que têm titulares de direitos e termos próprios. Consulte [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md). As obrigações de distribuição de binários devem ser revisadas para as versões exatas das dependências empacotadas.

## Contribuir

Leia [`CONTRIBUTING.md`](CONTRIBUTING.md) antes de abrir uma issue ou pull request. Para reportar um possível problema de segurança, consulte [`SECURITY.md`](SECURITY.md).

## Situação dos instaladores

As releases devem informar exatamente quais instaladores foram gerados e testados. Não publique um artefato como funcional antes de executar e validar a compilação e a instalação no sistema correspondente.
