import shutil

def read_text_file(file_path):
    """Lê o conteúdo de um arquivo de texto e retorna como string."""
    with open(file_path, 'r') as file:
        return file.read()

def write_text_file(data, file_path):
    """Escreve uma string em um arquivo de texto."""
    with open(file_path, 'w') as file:
        file.write(data)

def copy_file(origin, destination):
    """Copia um arquivo e seus metadados de origin para destination."""
    shutil.copy2(origin, destination)

def move_file(origin, destination):
    """Move um arquivo e seus metadados de origin para destination."""
    shutil.move(origin, destination)