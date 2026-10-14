# Primeira execução no Windows

## 1. Instalar os requisitos

Instale [Python 3.11 ou superior](https://www.python.org/downloads/), [Git](https://git-scm.com/downloads) e [Ollama para Windows](https://ollama.com/download/windows). Abra o Ollama e reabra o PowerShell para atualizar o PATH.

Verifique:

```powershell
python --version
git --version
ollama --version
```

O aplicativo usa a biblioteca padrão do Python, sem pacotes adicionais.

## 2. Obter o projeto

No PowerShell, escolha a pasta onde deseja guardar o projeto e execute:

```powershell
git clone https://github.com/gabri-silva/Assistente-Qwen.git
Set-Location ./Assistente-Qwen
```

Se você já clonou ou extraiu o projeto, abra o PowerShell diretamente na raiz dele. Essa é a pasta que contém `README.md`, `config.example.json` e `src/`. Todos os comandos seguintes partem dessa pasta.

## 3. Baixar e configurar o modelo

```powershell
ollama pull qwen3.5:9b
```

Aguarde a conclusão. Escolha um tamanho compatível com RAM, VRAM e armazenamento disponíveis. Para experimentar `qwen3.5:4b`, baixe esse nome e altere `model` na configuração para o mesmo valor.

Opcionalmente, crie uma configuração pessoal ignorada pelo Git:

```powershell
Copy-Item config.example.json data/config.json
```

Ao usar esse arquivo, inclua `--config data/config.json` antes do subcomando, como em `python -m assistente.cli --config data/config.json chat`.

## 4. Verificar a conexão

```powershell
$env:PYTHONPATH = Join-Path (Get-Location).Path 'src'
python -m assistente.cli doctor
```

Resultado esperado: “Ollama acessível” e “Modelo configurado disponível”. O diagnóstico verifica o serviço e a presença do modelo. A conversa seguinte verifica a geração de respostas.

## 5. Guardar uma preferência e conversar

```powershell
python -m assistente.cli remember 'Prefiro respostas em português'
python -m assistente.cli chat
```

Digite uma mensagem depois de `Você:`. Para encerrar, digite `/sair`.

A memória explícita persiste em `data/memory.sqlite3` na configuração padrão. O histórico fica somente na sessão atual. Conversas e memórias não alteram os pesos do modelo.

## Próximas execuções

Abra o PowerShell na raiz do projeto, mantenha Ollama em execução e use:

```powershell
$env:PYTHONPATH = Join-Path (Get-Location).Path 'src'
python -m assistente.cli chat
```

Configure `PYTHONPATH` em cada nova janela. Nenhum caminho de usuário específico é necessário.

## Problemas comuns

| Sintoma | Como verificar |
| --- | --- |
| `python`, `git` ou `ollama` não reconhecido | Confirme a instalação e reabra o PowerShell para atualizar o PATH. |
| Falha de conexão ao Ollama | Abra o aplicativo e repita `doctor`. Em uma instalação pela CLI, `ollama serve` inicia o servidor em primeiro plano quando ele ainda não está ativo. |
| Modelo ausente | Baixe o nome indicado em `model` e aguarde a conclusão. |
| `No module named assistente` | Confirme que está na raiz do projeto e configure `PYTHONPATH` na mesma janela. |
| Resposta lenta ou falta de memória | Experimente um modelo menor e atualize a configuração para o mesmo nome baixado. |
| Instalador termina com código 5 | Examine as mensagens anteriores e o log do instalador. O código isolado não identifica a causa. Tente o instalador oficial diretamente e registre a mensagem apresentada. |

## Limites desta versão

O controle do navegador ainda não está implementado. Leitura e escrita usam comandos explícitos dentro de `workspace/`. Não há instalação automática de modelos nem alteração de arquivos pelo modelo durante a conversa.
