# Assistente Qwen local

Base inicial para um assistente em português no servidor onde fica o navegador pessoal.

## Disponível nesta versão

- Conversa pelo endpoint local do Ollama, com Qwen 3.5 configurável.
- Memórias explícitas em SQLite, reaproveitadas ao iniciar uma conversa.
- Leitura e escrita de texto UTF-8 na pasta `workspace`, com backup antes da primeira sobrescrita.
- Comando de diagnóstico, testes e repositório Git local.

## Estado das integrações

O Ollama e o modelo ainda precisam ser instalados. `qwen3.5:9b` é uma escolha inicial configurável, sem validação do hardware. A edição de arquivos acontece por comandos explícitos, sem ações autônomas do modelo. O navegador tem somente um contrato de integração, ainda sem implementação. Open WebUI, RAG, voz e fine-tuning não estão instalados.

## Primeiro uso (PowerShell)

Instale Ollama a partir de https://ollama.com/download e mantenha o serviço em execução. Depois:

```powershell
Set-Location -LiteralPath 'C:\Users\gab02\OneDrive\Área de Trabalho\Assistente-Qwen'
ollama pull qwen3.5:9b
$env:PYTHONPATH = Join-Path (Get-Location).Path 'src'
python -m assistente.cli doctor
python -m assistente.cli remember 'Prefiro respostas em português'
python -m assistente.cli chat
```

O aplicativo usa apenas a biblioteca padrão do Python. O modelo não ganha acesso ao navegador ou ao sistema automaticamente. Conversas não treinam os pesos. O comando `remember` guarda fatos, não realiza fine-tuning.

```powershell
python -m assistente.cli write exemplo.txt 'Meu primeiro arquivo'
python -m assistente.cli read exemplo.txt
python -m unittest discover -s tests -v
```

Arquivos de usuário, memórias e perfis do navegador ficam fora do Git. A Área de Trabalho atual está em OneDrive: o Git é local, mas a pasta pode ser sincronizada pelo OneDrive. Isso também vale para futuros dados locais. Se precisar de isolamento da nuvem, mova o projeto para uma pasta fora do OneDrive antes de armazenar dados pessoais.

## Estrutura

```text
config.example.json       Configuração local e tamanho do modelo
src/assistente/cli.py      Interface de comandos e conversa
src/assistente/ollama.py   Cliente HTTP local
src/assistente/memory.py   Memória persistente
src/assistente/tools/     Arquivos e contrato de navegador
data/                    Banco local, ignorado pelo Git
workspace/               Arquivos editáveis, ignorados pelo Git
scripts/                 Atalho de execução PowerShell
tests/                   Validação dos componentes
docs/                    Arquitetura e comandos
```

## Fontes

- https://ollama.com/library/qwen3.5
- https://docs.ollama.com/api/chat
- https://docs.ollama.com/api/tags
- https://docs.openwebui.com/getting-started/quick-start/
