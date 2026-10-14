# Primeira execução no Windows

## 1. Instalar e abrir o Ollama

Baixe o instalador oficial em https://ollama.com/download/windows, instale e abra o aplicativo. Feche e abra novamente o PowerShell depois da instalação para atualizar o PATH.

Pré-requisito do projeto: Python 3.11 ou superior. O aplicativo usa a biblioteca padrão, sem instalação de pacotes adicionais.

## 2. Abrir a pasta e baixar o modelo

```powershell
Set-Location -LiteralPath 'C:\Users\gab02\OneDrive\Área de Trabalho\Assistente-Qwen'
ollama pull qwen3.5:9b
```

Aguarde a conclusão do download. O modelo 9B é a configuração inicial, ainda sem validação de RAM e VRAM do servidor. Para usar outro tamanho, altere o campo model em config.example.json e baixe o nome correspondente.

## 3. Verificar o ambiente

```powershell
$env:PYTHONPATH = Join-Path (Get-Location).Path 'src'
python -m assistente.cli doctor
```

Resultado esperado: “Ollama acessível” e “Modelo configurado disponível”. O diagnóstico verifica conexão e presença do modelo. A conversa seguinte verifica a geração de respostas.

## 4. Guardar uma preferência e conversar

```powershell
python -m assistente.cli remember 'Prefiro respostas em português'
python -m assistente.cli chat
```

Digite uma mensagem depois de Você:. Para encerrar, digite /sair. A memória explícita persiste no banco data/memory.sqlite3. O histórico da conversa fica apenas na sessão atual. Conversar não treina os pesos do modelo.

## Próximas execuções

Com o Ollama aberto, execute em cada nova janela do PowerShell:

```powershell
Set-Location -LiteralPath 'C:\Users\gab02\OneDrive\Área de Trabalho\Assistente-Qwen'
$env:PYTHONPATH = Join-Path (Get-Location).Path 'src'
python -m assistente.cli chat
```

## Problemas comuns

- Ollama não reconhecido: confirme a instalação e reabra o PowerShell.
- Falha de conexão: abra o Ollama e repita o diagnóstico. Em uma instalação via CLI, ollama serve inicia o servidor em primeiro plano, se ele ainda não estiver ativo.
- Modelo ausente: execute ollama pull qwen3.5:9b e aguarde a conclusão.
- No module named assistente: entre na pasta do projeto e configure PYTHONPATH na mesma janela antes de iniciar.
- Resposta lenta ou falta de memória: avalie um modelo menor, como qwen3.5:4b, e atualize a configuração para o mesmo nome.

## Limites desta versão

O controle do navegador ainda não está implementado. A leitura e a escrita de arquivos usam comandos explícitos limitados à pasta workspace. O banco e os arquivos de usuário ficam fora do Git, mas a pasta atual está no OneDrive e pode ser sincronizada por ele.

Este guia documenta comandos para o usuário executar. A instalação do Ollama, o download do modelo e a geração real de respostas não foram verificados nesta atualização.
