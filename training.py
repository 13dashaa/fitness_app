class Record:
    def __init__(self):
        self.records = []



    def add_record(self, user_ex):
        self.records.append(user_ex)


class Training(Record):

    def __init__(self):

        super().__init__()
        self.__totalExtraWeight = 0


    def calculate_weight(self):
        for ex in self.records:
            self.__totalExtraWeight += ex.calc_total_ex_weight()
        return self.__totalExtraWeight

    def add_record(self, user_ex):

        self.records.append(user_ex)
        self.__totalExtraWeight = self.calculate_weight()
    def show_ex(self):

        for ex in self.records:
            print(ex)

        print(f'Total training weight: {self.__totalExtraWeight}')


class UserTrainings(Record):

    def show_rec(self):
        for i in range(len(self.records)):
            print(f'Training {i+1}')
            self.records[i].show_ex()


