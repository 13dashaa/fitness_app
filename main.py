import exercises
import functions
import training

training_list = training.UserTrainings()
print("If u want to create new training press 1")
if input() == '1':
    user_training = training.Training()


    list_exercises = functions.ListExercises("exercises.txt")

    print("To add an exercise enter 1")
    while input() == '1':
        for key in list_exercises.list_ex.keys():
            print(key.capitalize())
        user_muscles = input('Choose one of these muscle groups:\n').strip().lower()
        print("Avalible exercises:")
        print(*list_exercises.list_ex[user_muscles], sep='\n')
        exercise = exercises.TrainingStrengthExercise(input("Exercise name from list:").strip().lower(),
                                                      user_muscles,
                                                      int(input("Extra weight:")),
                                                      int(input("Amount of repetatives:")))

        user_training.add_record(exercise)
        print("To add an exercise enter 1")
    training_list.add_record(user_training)


training_list.show_rec()
