class Exercise:
    def __init__(self, name):
        self.__name = name.strip()

    def get_name(self):
        return self.__name


class StrengthExercise(Exercise):
    def __init__(self, name, muscle):
        super().__init__(name)
        self.__muscle = muscle

    def get_muscle(self):
        return self.__muscle


class TrainingStrengthExercise(StrengthExercise):
    def __init__(self, name, muscle, weight=0, numb_of_rep=15):
        super().__init__(name, muscle)
        self.__extra_weight = weight
        self.__numb_of_rep = numb_of_rep

    def __str__(self):
        return (f'{self.get_name()}\tMuscle group: {self.get_muscle()}\tExtra weight: {self.__extra_weight}'
                f'\tRepetatives: {self.__numb_of_rep}')

    def calc_total_ex_weight(self):
        return self.__extra_weight * self.__numb_of_rep


class TrainerCardioExercise(Exercise):
    def __init__(self, name, duration):
        super().__init__(name)
        self.__duration = duration

    def __str__(self):
        return f'{self.get_name()}\tDuration: {self.__duration}'


