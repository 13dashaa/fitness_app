
class ListExercises:

    def __init__(self, file_ex):
        with open(file_ex,  encoding='utf-8') as file:
            self.list_ex = {}
            cur_line = file.readline().strip()
            muscle = ''
            while (cur_line):
                if (":" in cur_line):
                    muscle = cur_line.split(': ')[-1]
                    cur_line = file.readline().strip()
                l = self.list_ex.get(muscle, [])
                l.append(cur_line)
                self.list_ex[muscle] = l
                cur_line = file.readline().strip()

    def get_keys(self):
        return self.list_ex.keys()
