from time import *
import random
from tkinter import *

main_window = Tk()
main_window.geometry("600x400")
main_window.configure(bg='lightgreen')


def calculate_errors(original, user):
    if len(original) == 0:
        return 0

    correct_characters = sum(1 for char1, char2 in zip(original, user) if char1 == char2)
    accuracy = (correct_characters / len(original)) * 100
    return accuracy


def generate_sentence():
    sentences = [
        "Two things are infinite: the universe and human stupidity and I'm not sure about the universe.",
        "So many books, so little time.",
        "You only live once, but if you do it right, once is enough",
        "A friend is someone who knows all about you and still loves you",
        "Without music, life would be a mistake.",
        "The way to get started is to quit talking and begin doing"
    ]
    return random.choice(sentences)


def typing_test():
    new_window = Toplevel(main_window)
    new_window.configure(bg="light blue")
    new_window.geometry("600x400")
    label_instruction = Label(new_window, text="Type the following sentence", font=("Comic Sans MS", 28), background="light blue")
    label_instruction.pack()
    sentence_to_type = generate_sentence()
    label_sentence = Label(new_window, text=sentence_to_type, font=("Arial", 18), background="light blue")
    label_sentence.place(x=40, y=100)
    start_time = time()
    user_input = Entry(new_window, width=80, font=18)
    user_input.place(x=0, y=140)

    def calculate_speed_and_display_results():
        end_time = time()
        time_taken = end_time - start_time
        words_typed = sentence_to_type.split()[:len(user_input.get().split())]
        characters_typed = len(" ".join(words_typed))
        words_per_minute = len(user_input.get().split()) / (time_taken / 60)
        accuracy_percentage = calculate_errors(sentence_to_type, user_input.get())

        result_label = Label(new_window, text=f"Your typing speed: {words_per_minute:.2f} WPM\nAccuracy: {accuracy_percentage:.2f}%",
                            font=("Arial", 14), background='light blue')
        result_label.place(x=160, y=230)

        retry_button = Button(new_window, text="Retry", font=("Arial", 12), width=10, height=2, command=retry)
        exit_button = Button(new_window, text="Exit", font=("Arial", 12), width=10, height=2, command=new_window.destroy)

        retry_button.place(x=100, y=300)
        exit_button.place(x=350, y=300)

    def retry():
        new_window.destroy()
        typing_test()

    submit_button = Button(new_window, text="Submit", font=("Arial", 12), width=10, height=2, command=calculate_speed_and_display_results)
    submit_button.place(x=260, y=180)


welcome_label = Label(main_window, text="Welcome to simple Typing speed tester!", font=("Comic Sans MS", 22), background='lightblue')
ready_label = Label(main_window, text="Are you Ready?", font=("Comic Sans MS", 26), background='lightblue')
welcome_label.pack()
ready_label.place(x=180, y=80)
yes_button = Button(main_window, text="Yes", font=18, width=10, height=2, command=typing_test)
no_button = Button(main_window, text="No", font=18, width=10, height=2)
yes_button.place(x=120, y=180)
no_button.place(x=360, y=180)

main_window.mainloop()
