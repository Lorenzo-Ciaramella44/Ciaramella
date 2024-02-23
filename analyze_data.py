import shutil
import sys

def copia_file(nome_file_input, nome_file_output):
    shutil.copy(nome_file_input, nome_file_output)

if __name__ == "__main__":
    nome_file_input = sys.argv[1]
    nome_file_output = sys.argv[2]
    copia_file(nome_file_input, nome_file_output)

