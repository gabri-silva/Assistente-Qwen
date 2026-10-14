# Assistente Qwen

Assistente local em português, desenvolvido em Python com Qwen 3.5 via Ollama, memória persistente e comandos para arquivos. Projeto em estágio inicial, com interface de terminal.

## Recursos disponíveis

- Conversa com um modelo executado pelo Ollama no mesmo computador.
- Memórias explícitas armazenadas em SQLite.
- Leitura e escrita de texto UTF-8 dentro de `workspace/`.
- Backup `.bak` antes da primeira sobrescrita de um arquivo. Uma nova sobrescrita exige preservar ou mover o backup existente.
- Diagnóstico de conexão e testes automatizados.

O controle do navegador possui apenas um contrato de integração. Ações autônomas, Open WebUI, RAG, voz e fine-tuning ainda não estão implementados. Conversar com o assistente não treina os pesos do modelo.

## Requisitos

- Python 3.11 ou superior, com SQLite disponível.
- Git para clonar e versionar o projeto.
- [Ollama](https://ollama.com/download) instalado e em execução.
- Memória e armazenamento suficientes para o modelo escolhido. O modelo padrão é `qwen3.5:9b`, mas a configuração permite outro tamanho.

O aplicativo usa a biblioteca padrão do Python. Os exemplos abaixo usam PowerShell no Windows e devem ser executados na raiz do projeto.

## Início rápido

Em uma pasta de sua escolha:

```powershell
git clone https://github.com/gabri-silva/Assistente-Qwen.git
Set-Location ./Assistente-Qwen
ollama pull qwen3.5:9b
$env:PYTHONPATH = Join-Path (Get-Location).Path 'src'
python -m assistente.cli doctor
python -m assistente.cli chat
```

Digite `/sair` para encerrar. Consulte o [guia de primeira execução](docs/PRIMEIRA_EXECUCAO.md) para configuração e solução de problemas.

## Memória e arquivos

```powershell
python -m assistente.cli remember 'Prefiro respostas em português'
python -m assistente.cli memories
python -m assistente.cli write exemplo.txt 'Meu primeiro arquivo'
python -m assistente.cli read exemplo.txt
```

Os caminhos de arquivos são relativos a `workspace/`. As operações são solicitadas explicitamente pela CLI, sem execução de ferramentas pelo modelo. A memória persiste entre sessões, enquanto o histórico da conversa permanece somente na sessão atual.

## Configuração

A configuração padrão fica em `config.example.json`. Para manter uma configuração própria fora do versionamento:

```powershell
Copy-Item config.example.json data/config.json
python -m assistente.cli --config data/config.json doctor
python -m assistente.cli --config data/config.json chat
```

Edite `model` para escolher o modelo e baixe o mesmo nome com `ollama pull`. Os caminhos `workspace` e `database` são relativos à raiz do projeto. O cliente aceita somente endpoints locais do Ollama. A opção `--config` deve aparecer antes do subcomando.

## Estrutura

```text
config.example.json       Configuração de exemplo
src/assistente/cli.py      Comandos e conversa
src/assistente/ollama.py   Cliente HTTP para Ollama
src/assistente/memory.py   Memória SQLite
src/assistente/tools/     Arquivos e contrato de navegador
data/                    Dados locais ignorados pelo Git
workspace/               Arquivos de usuário ignorados pelo Git
scripts/run.ps1           Atalho PowerShell
tests/                   Testes dos componentes
docs/                    Guias de uso e arquitetura
```

## Desenvolvimento

```powershell
$env:PYTHONPATH = Join-Path (Get-Location).Path 'src'
python -m unittest discover -s tests -v
```

Os testes da API usam uma resposta simulada e não precisam do Ollama. Para verificar o serviço real, execute `doctor` e depois envie uma mensagem em `chat`.

## Dados locais

O Git ignora memórias, arquivos de usuário e perfis de navegador. Serviços de sincronização de pastas podem copiar esses dados independentemente do Git. Escolha o local de armazenamento conforme suas necessidades de privacidade.

## Documentação

- [Primeira execução](docs/PRIMEIRA_EXECUCAO.md)
- [Comandos de uso e versionamento](docs/COMANDOS.md)
- [Arquitetura e próximos passos](docs/ARQUITETURA.md)

## Referências

- [Qwen 3.5 no Ollama](https://ollama.com/library/qwen3.5)
- [API de conversa](https://docs.ollama.com/api/chat)
- [API de modelos instalados](https://docs.ollama.com/api/tags)

