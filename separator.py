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
        problems = {'fail':0,'error':0,'critical':0,'denied':0,
                    'unauthorized':0,'failed':0}
        for line in self.read_lines:
            line_sec = line.lower()
            for word in problems.keys():
                if word in line_sec:
                    problems[word] += 1
        print(problems)
    
    
    def ALL_TASKS(self):
        self.transformation_readlines()
        self.separate_problems()
   
       

FUNCTION_CLASS = Organize_files(path_storage)
FUNCTION_CLASS.ALL_TASKS()





   # def transformation_split(self):
     #   with open(self.file_csv, "r") as files_in_split:
      #      read_str = files_in_split.read()
       #     self.read_split = read_str.split()