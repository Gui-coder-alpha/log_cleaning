#/var/log/syslog and /var/log/auth.log
#arquivos a serem limpados

path_storage = "/home/guilh/log_cleaning/storage/test_files.csv"


class Organize_files:
    def __init__(self, path_storage):
        self.file_csv = path_storage

    def transformation(self):
        with open(self.file_csv, "r") as test_files:
            self.conteudo = test_files.read().split()
            #print(self.conteudo)

    def separate_problems(self):
        problems = ["denied","fail","failed","Fail","Failed","error","critical","unauthorized"]
        if problems in self.conteudo:
            print("hi")
        else:
            print("none")
            
    
    
    def ALL_TASKS(self):
        self.transformation()
        self.separate_problems()
   
       

FUNCTION_CLASS = Organize_files(path_storage)
FUNCTION_CLASS.ALL_TASKS()