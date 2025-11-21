#/var/log/syslog and /var/log/auth.log
#arquivos a serem limpados
import os

path_storage = "/home/guilh/log_cleaning/storage/test_files.csv"

class Organize_files:
    def __init__(self, path_storage):
        self.file_csv = path_storage

    def transformation_readlines(self):
        with open(self.file_csv, "r") as files_in_lines:
            self.read_lines = files_in_lines.readlines()

    def separate_problems(self):
        self.problems = {'fail':0,'error':0,'critical':0,'denied':0,
                    'unauthorized':0,'failed':0}
        for line in self.read_lines:
            line_sec = line.lower()
            for word in self.problems.keys():
                if word in line_sec:
                    self.problems[word] += 1

    def determined_errors(self):
        self.determined_problems = {'misc dxg':0, 'permission denied':0}
        for line in self.read_lines:
            true_line = line.lower()
            for paragraph in self.determined_problems:
                if paragraph in true_line:
                    self.determined_problems[paragraph] += 1

    def determined_directory(self):
        directory_path = "/proc/sys"
        self.armazened_directories = {}
        for root, dirs, files in os.walk(directory_path, directory_path):
            self.armazened_directories[root] = 0
        for line in self.read_lines:
            true_line = line.lower()
            for paragraph in self.armazened_directories:
                if paragraph in true_line:
                   self.armazened_directories[paragraph] += 1
        for values_equals_zero in list(self.armazened_directories.keys()):
            if self.armazened_directories[values_equals_zero] == 0:
                del self.armazened_directories[values_equals_zero]


    def final_relatory(self):
        print('------------------------relatory------------------------')
        print(f"Observe a seguir o relatório de log:")
        print(f"    -> fail:{self.problems['fail']}")
        print(f"    -> error:{self.problems['error']}")
        print(f"    -> failed:{self.problems['failed']}")
        print(f"    -> unauthorized:{self.problems['unauthorized']}")
        print(f"    -> critical:{self.problems['critical']}")
        print(f"    -> denied:{self.problems['denied']}")
        print("Determined problems here:")
        print(f"    -> Misc dxg:{self.determined_problems['misc dxg']}")
        print(f"    -> Permission denied:{self.determined_problems['permission denied']}")
        print(f"Access denied in directories:")
        print(f"    ->{self.armazened_directories}")
        print('------------------------final------------------------')

    def ALL_TASKS(self):
        self.transformation_readlines()
        self.determined_errors()
        self.separate_problems()
        self.determined_directory()
        self.final_relatory()     

FUNCTION_CLASS = Organize_files(path_storage)
FUNCTION_CLASS.ALL_TASKS()