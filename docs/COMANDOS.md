# Comandos e registro da preparação

Data: 14/10/2026. Projeto: Assistente-Qwen.

## Executados na preparação

```powershell
[Environment]::GetFolderPath('Desktop')
Get-Command git, python, ollama -ErrorAction SilentlyContinue
python work/create_project.py
```

O último comando executou um gerador da sessão: criou as pastas e gravou os arquivos iniciais. O gerador é temporário e não é necessário para usar o projeto. O caminho de destino foi conferido para evitar sobrescrita.

Os comandos Git e de verificação executados estão registrados abaixo após sua conclusão.

## Comandos futuros, ainda não executados

```powershell
Set-Location -LiteralPath 'C:\Users\gab02\OneDrive\Área de Trabalho\Assistente-Qwen'
ollama pull qwen3.5:9b
$env:PYTHONPATH = Join-Path (Get-Location).Path 'src'
python -m assistente.cli doctor
python -m assistente.cli chat
```

Instalar Ollama primeiro. Não há download de modelo, instalação de pacotes ou conexão ao navegador na preparação inicial.

## Versionamento e verificações executados

```powershell
git -C 'C:/Users/gab02/OneDrive/Área de Trabalho/Assistente-Qwen' init -b main
$projectPath = 'C:\Users\gab02\OneDrive\Área de Trabalho\Assistente-Qwen'
$env:PYTHONPATH = Join-Path $projectPath 'src'
$env:TMP = Join-Path $projectPath 'data\test-temp'
$env:TEMP = $env:TMP
New-Item -ItemType Directory -Force -Path $env:TMP
python -m unittest discover -s tests -v
python -m assistente.cli --help
git -C 'C:/Users/gab02/OneDrive/Área de Trabalho/Assistente-Qwen' add .
git -C 'C:/Users/gab02/OneDrive/Área de Trabalho/Assistente-Qwen' commit -m 'Estrutura inicial do assistente local Qwen'
git -C 'C:/Users/gab02/OneDrive/Área de Trabalho/Assistente-Qwen' status --short
```

Os quatro testes passaram. O teste da API usa resposta simulada, pois Ollama não está instalado. O diretório temporário foi direcionado para data/test-temp devido às permissões da sessão. A implementação fecha conexões SQLite explicitamente para liberar arquivos no Windows.

A identidade Git existente foi preservada. Não foi criado repositório remoto nem realizado push.

## Guia de primeira execução

Consulte [PRIMEIRA_EXECUCAO.md](PRIMEIRA_EXECUCAO.md) para os comandos de instalação e uso. Eles permanecem instruções para execução futura, sem registro de instalação ou download nesta etapa.

