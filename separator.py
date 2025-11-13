#/var/log/syslog and /var/log/auth.log
#arquivos a serem limpados

path_storage="/home/guilh/log_cleaning/storage/test_files.csv"


class Organize_files:
    def __init__(self, file_csv):
        self.file_csv = file_csv
        with open(self.file_csv, "r") as test_files:
            conteudo = test_files.read()
            self.conteudo_primario = conteudo


    def separate_problems(self):
        denied_files = self.conteudo_primario.split()
        for denied_files in self.conteudo_primario:
            print(denied_files)
            
   
    def filtro(self):
        oi = 3
        return

Organize_files(path_storage)