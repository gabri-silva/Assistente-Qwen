# Arquitetura e próximos passos

## Fluxo atual

Usuário → CLI Python → API Ollama local → Qwen 3.5.
Memórias explícitas em SQLite entram no contexto de novas conversas.
Os comandos read/write atuam somente em workspace. Não há execução de shell pelo modelo.

## Evolução

1. Validar RAM, GPU e VRAM, instalar Ollama e testar o tamanho do modelo.
2. Acrescentar Open WebUI, com dados persistentes e serviço limitado ao host/rede autorizada.
3. Implementar BrowserAdapter com Browser Use ou Playwright, conforme o navegador instalado. Definir perfil e contas autorizadas. Não conectar automaticamente o perfil pessoal.
4. Adicionar chamadas de ferramentas ao ciclo do agente. Registrar ações e pedir aprovação para envios, compras e exclusões.
5. Implementar consulta a documentos (RAG) e avaliar resultados com perguntas reais.
6. Reunir exemplos corrigidos, remover dados sensíveis e avaliar um ajuste LoRA/QLoRA separado. Manter versões de dados, adaptadores e avaliações.

O limite de caminhos implementado é adequado para o protótipo com uso individual. Ele não é isolamento de sistema operacional nem defesa contra outro processo modificando links simultaneamente. Usar processo/contêiner com permissões próprias antes de disponibilizar operações autônomas.
