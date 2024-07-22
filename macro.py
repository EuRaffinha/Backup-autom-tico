import os
import shutil
import time
import schedule
from threading import Thread

# Caminho do executável do backup - ajuste conforme necessário
backup_exe_path = r"C:\\Program Files\Backup.exe"  # Exemplo: "C:\\Caminho\\Para\\SeuBackup.exe"

# Pasta de destino do backup - ajuste conforme necessário
backup_destination_path = r"C:\\backup_acesse"  # Exemplo: "D:\\Caminho\\Para\\Backups"

# Pasta de sincronização com Google Drive - ajuste conforme necessário
google_drive_sync_path = r"C:\\BackupGoogleDrive"  # Exemplo: "D:\\Caminho\\Para\\GoogleDriveSync"

# Variável global para controlar o backup automático
auto_backup_enabled = True

# Função para executar o backup
def run_backup(exe_path):
    # Verificar se o arquivo existe
    if not os.path.isfile(exe_path):
        print(f"O arquivo especificado não foi encontrado: {exe_path}")
        return False

    try:
        # Usar `os.startfile` para abrir o executável
        os.startfile(exe_path)
        return True
    except Exception as e:
        print(f"Erro ao executar o backup: {e}")
        return False

# Função para encontrar os cinco últimos arquivos modificados na pasta de destino
def find_latest_files(directory, count=5):
    try:
        files = os.listdir(directory)
        if not files:
            print("A pasta de destino está vazia.")
            return []

        paths = [os.path.join(directory, basename) for basename in files]
        latest_files = sorted(paths, key=os.path.getmtime, reverse=True)[:count]
        return latest_files
    except Exception as e:
        print(f"Erro ao encontrar os arquivos modificados: {e}")
        return []

# Função para copiar arquivos para a pasta de sincronização
def copy_files_to_sync(files, sync_path):
    try:
        if not os.path.exists(sync_path):
            os.makedirs(sync_path)

        for file in files:
            destination_path = os.path.join(sync_path, os.path.basename(file))
            shutil.copy(file, destination_path)
            print(f"Arquivo '{file}' copiado para a pasta de sincronização.")
    except Exception as e:
        print(f"Erro ao copiar arquivos para a pasta de sincronização: {e}")

def backup_and_schedule():
    # Executar o backup
    print("Iniciando o backup automático...")
    backup_status = run_backup(backup_exe_path)
    
    if backup_status:
        print("Backup concluído com sucesso.")
        
        # Esperar alguns segundos para garantir que o arquivo de backup seja gravado
        time.sleep(10)
        
        # Encontrar os cinco últimos arquivos modificados na pasta de destino
        latest_files = find_latest_files(backup_destination_path, count=5)
        
        if latest_files:
            # Copiar os cinco últimos arquivos modificados para a pasta de sincronização
            copy_files_to_sync(latest_files, google_drive_sync_path)
        else:
            print("Nenhum arquivo recente encontrado na pasta de destino.")
    else:
        print("Falha na execução do backup.")

def schedule_backups():
    global auto_backup_enabled
    while True:
        if auto_backup_enabled:
            schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Agendar a execução do backup dez vezes ao dia
    schedule.every().day.at("08:00").do(backup_and_schedule)
    schedule.every().day.at("08:54").do(backup_and_schedule)
    schedule.every().day.at("09:48").do(backup_and_schedule)
    schedule.every().day.at("10:42").do(backup_and_schedule)
    schedule.every().day.at("11:36").do(backup_and_schedule)
    schedule.every().day.at("12:30").do(backup_and_schedule)
    schedule.every().day.at("13:24").do(backup_and_schedule)
    schedule.every().day.at("14:18").do(backup_and_schedule)
    schedule.every().day.at("15:12").do(backup_and_schedule)
    schedule.every().day.at("16:06").do(backup_and_schedule)
    schedule.every().day.at("17:00").do(backup_and_schedule)
    
    print("Agendamentos configurados. O script será executado dez vezes ao dia entre 08:00 e 17:00.")
    
    # Iniciar agendamento em uma thread separada
    schedule_thread = Thread(target=schedule_backups)
    schedule_thread.daemon = True
    schedule_thread.start()
    
    while True:
        print("\nMenu:")
        print("1. Executar backup manualmente")
        print("2. Habilitar backup automático")
        print("3. Desabilitar backup automático")
        print("4. Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            backup_and_schedule()
        elif choice == "2":
            auto_backup_enabled = True
            print("Backup automático habilitado.")
        elif choice == "3":
            auto_backup_enabled = False
            print("Backup automático desabilitado.")
        elif choice == "4":
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")
