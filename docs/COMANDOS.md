# Comandos de uso e versionamento

Os exemplos usam PowerShell no Windows. Execute os comandos na raiz do projeto, exceto a clonagem, que parte da pasta onde você deseja armazená-lo.

## Clonagem

```powershell
git clone https://github.com/gabri-silva/Assistente-Qwen.git
Set-Location ./Assistente-Qwen
```

Um clone já contém o repositório Git e o remoto `origin`. Não execute `git init` novamente.

## Preparação e conversa

```powershell
ollama pull qwen3.5:9b
$env:PYTHONPATH = Join-Path (Get-Location).Path 'src'
python -m assistente.cli doctor
python -m assistente.cli remember 'Prefiro respostas em português'
python -m assistente.cli memories
python -m assistente.cli chat
```

Digite `/sair` na conversa para encerrar. O modelo baixado deve corresponder ao campo `model` da configuração.

## Arquivos de trabalho

```powershell
python -m assistente.cli write exemplo.txt 'Meu primeiro arquivo'
python -m assistente.cli read exemplo.txt
```

O destino é `workspace/exemplo.txt`. Caminhos absolutos e caminhos que saem da pasta de trabalho são rejeitados. Antes de sobrescrever novamente um arquivo que já possui `.bak`, preserve ou mova o backup.

## Configuração pessoal

```powershell
Copy-Item config.example.json data/config.json
python -m assistente.cli --config data/config.json doctor
python -m assistente.cli --config data/config.json chat
```

Edite a cópia conforme necessário. O diretório `data/` está ignorado pelo Git.

## Verificação

```powershell
$env:PYTHONPATH = Join-Path (Get-Location).Path 'src'
python -m assistente.cli --help
python -m unittest discover -s tests -v
```

Os testes verificam persistência de memória, limite de caminhos, backup de arquivos e formato da chamada de conversa com resposta simulada. Eles não comprovam geração real pelo modelo nem controle de navegador.

## Registrar alterações

```powershell
git status --short
git diff
# Escolha somente os arquivos que deseja versionar.
git add README.md docs/
git commit -m 'Atualiza documentacao'
```

Para publicar em um repositório onde você possui permissão:

```powershell
git remote -v
git push -u origin main
```

Contribuidores sem acesso de escrita devem usar seu próprio fork e abrir um pull request. Autentique-se no GitHub quando solicitado. Não coloque senhas ou tokens nos comandos nem nos arquivos versionados.

## Mais informações

Consulte o [guia de primeira execução](PRIMEIRA_EXECUCAO.md) e a [arquitetura](ARQUITETURA.md).
