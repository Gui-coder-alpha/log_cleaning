#/var/log/syslog and /var/log/auth.log
#arquivos a serem limpados

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
        self.determined_problems = ['misc dxgk','permission denied']
        for line in self.read_lines:
            true_line = line.lower()
            for paragraph in self.determined_problems:
                if paragraph in true_line:
                    paragraph = self.determined_problems
        print(self.determined_problems[paragraph])
        print('/////////////////////////////')


    def final_relatory(self):
        print('------------relatory------------')
        print(f"Observe a seguir o relatório de log: fail:")
        print(f"{self.problems['fail']}")
        print(f"error:{self.problems['error']}")
        print(f"failed:{self.problems['failed']}")
        print(f"unauthorized:{self.problems['unauthorized']}")
        print(f"critical:{self.problems['critical']}")
        print(f"denied:{self.problems['denied']}")
        print('------------final------------')

    def ALL_TASKS(self):
        self.transformation_readlines()
        self.separate_problems()
        self.final_relatory()       

FUNCTION_CLASS = Organize_files(path_storage)
FUNCTION_CLASS.ALL_TASKS()