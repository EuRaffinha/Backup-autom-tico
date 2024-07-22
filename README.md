# Projeto de Backup Automático e Sincronização com Google Drive

## 1. Introdução

### Objetivo
O objetivo deste projeto é criar um sistema automatizado de backup que executa backups regulares dos dados críticos e sincroniza os cinco últimos backups do dia com o Google Drive, garantindo a integridade e segurança dos dados.

---

## 2. Funcionalidades

### Backup Automático
- Executa backups automáticos dez vezes ao dia.
- Horários configurados para execução: 08:00, 08:54, 09:48, 10:42, 11:36, 12:30, 13:24, 14:18, 15:12, 16:06 e 17:00.

### Sincronização com Google Drive
- Copia os cinco últimos backups do dia para a pasta de sincronização do Google Drive.
- Mantém os backups do dia anterior e adiciona os backups do dia atual à pasta de sincronização.

### Controle Manual
- Opções para executar o backup manualmente, habilitar ou desabilitar o backup automático e encerrar o programa.

---

## 3. Estrutura do Código

### `run_backup`
- Executa o processo de backup usando o executável fornecido.

### `find_latest_files`
- Encontra os cinco últimos arquivos modificados na pasta de destino do backup.

### `copy_files_to_sync`
- Copia os cinco últimos arquivos modificados para a pasta de sincronização do Google Drive.

### `backup_and_schedule`
- Função principal que gerencia o processo de backup e sincronização.

### `schedule_backups`
- Gerencia a execução automática dos backups de acordo com os horários agendados.

---

## 4. Como Utilizar

### Pré-requisitos
- Python 3.x instalado no sistema.
- Caminhos configurados corretamente para o executável do backup e pastas de destino e sincronização.

### Execução
1. Clone o repositório do GitHub.
2. Ajuste os caminhos conforme necessário no arquivo `macro.py`.
3. Execute o script `macro.py`.

### Menu Interativo
- **Executar backup manualmente**: Executa o backup e sincroniza os arquivos manualmente.
- **Habilitar backup automático**: Habilita a execução automática dos backups.
- **Desabilitar backup automático**: Desabilita a execução automática dos backups.
- **Sair**: Encerra o programa.

---

## 5. Exemplo de Uso

1. Executando o Script:

```bash
python macro.py
```

2. Saída Esperada:
```
Agendamentos configurados. O script será executado dez vezes ao dia entre 08:00 e 17:00.

Menu:
1. Executar backup manualmente
2. Habilitar backup automático
3. Desabilitar backup automático
4. Sair
Escolha uma opção: 
```

3. Verificação:
- Verifique a pasta de destino para garantir que os backups estão sendo criados.
- Verifique a pasta de sincronização do Google Drive para garantir que os cinco últimos backups estão presentes.

---

## 6. Conclusão

Este projeto fornece uma solução robusta para a criação e gerenciamento de backups automáticos, com a funcionalidade adicional de sincronização com o Google Drive. É uma ferramenta essencial para garantir a segurança e integridade dos dados críticos.

---

## 7. Contribuição

### Como Contribuir
1. Faça um fork do repositório.
2. Crie uma nova branch: `git checkout -b feature/nova-funcionalidade`.
3. Faça commit das suas alterações: `git commit -m 'Adiciona nova funcionalidade'`.
4. Faça push para a branch: `git push origin feature/nova-funcionalidade`.
5. Envie um pull request.

### Contato
- Para quaisquer dúvidas ou sugestões, entre em contato pelo dev.rafaelsan@gmail.com ou crie uma issue no GitHub.

