# Histórico de versões

## 0.4.0

- Versão-base atual do projeto para a etapa de distribuição multiplataforma.
- Atualizados os metadados da aplicação, as instruções de build, os nomes dos pacotes e o workflow para usar a versão `0.4.0` e a tag `v0.4.0`.
- Os instaladores Linux e macOS ainda precisam ser gerados e validados nos runners de destino antes de serem publicados.

## 0.3.0

- Incluídos scripts de empacotamento e workflow do GitHub Actions para preparar pacotes Linux e macOS; os binários finais ainda precisam ser compilados e testados nos runners de destino.
- Organização da aplicação em módulos (`skybird/`) e testes automatizados para a lógica sem Qt.
- Abas restauradas sob demanda e suspensão de abas ociosas.
- Gravações em lote para histórico, favoritos e sessão; cache HTTP limitado.
- Recursos básicos de privacidade: bloqueio de rastreadores conhecidos, controle de cookies de terceiros, sinais DNT/GPC e limpeza de dados.
- Melhorias em downloads, navegação por URL/pesquisa, permissões de sites, favicons, zoom, localização na página, tela cheia e restauração de abas.
- Instalador próprio para Windows e scripts de execução para Windows, Linux e macOS.
- Interface do instalador Windows refinada, com identidade visual branca e azul, seleção de destino mais clara, opções agrupadas e progresso explícito.

Esta versão continua experimental. Consulte o README para limitações conhecidas e validações ainda necessárias.