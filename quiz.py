
import time
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import random
from PIL import Image, ImageTk
import pyttsx3
import speech_recognition as sr
import csv
import os

from questions import Questions
from voice_questions import VoiceQuestions


class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry('1500x1000')

        self.engine = pyttsx3.init()

        self.nickname = simpledialog.askstring("Nickname", "Enter your nickname:")
        if not self.nickname:
            self.nickname = "Anonymous"

        self.background_image = Image.open("quizz.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)
        self.root.bind("<Configure>", self.resize_background)

        self.skip_button = tk.Button(self.root, text=">", font=("Arial", 24), command=self.skip_question, bg="red", fg="white")
        self.skip_button.place(relx=0.95, rely=0.5, anchor="e")

        self.index = 0
        self.voice_index = 0
        self.score = 0

        self.start_time = time.time()

        self.selected_questions = random.sample(Questions, 3)
        self.selected_voice_questions = random.sample(VoiceQuestions, 5)

        self.frame = tk.Frame(root, relief=tk.RAISED, bd=5, bg='#2d3250')
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=750, height=400)

        self.timer_label = tk.Label(self.root, text="Time: 00:00", font=("Arial", 30), bg="black", fg="white")
        self.timer_label.place(x=640, y=10)
        self.update_timer()

        self.question_label = tk.Label(self.frame, text="", font=("Arial", 16), wraplength=500, justify="center", bg='#2d3250', fg="White")
        self.question_label.pack(pady=20, expand=True)

        self.option_frames = []
        self.buttons = {}
        self.listen_buttons = {}

        for opt in ["a", "b", "c", "d"]:
            option_frame = tk.Frame(self.frame, bg='#2d3250')
            option_frame.pack(pady=10)

            label = tk.Label(option_frame, text=opt.upper(), font=("Arial", 14), bg='#2d3250', fg="White")
            label.grid(row=0, column=0, padx=10)

            self.buttons[opt] = tk.Button(option_frame, text="", font=("Arial", 14), width=30,
                                          command=lambda opt=opt: self.submit_answer(opt))
            self.buttons[opt].grid(row=0, column=1, padx=10)

            self.listen_buttons[opt] = tk.Button(option_frame, text="🎧", font=("Arial", 14), bg="#5b5b5b", fg="White",
                                                 command=lambda opt=opt: self.play_sound(self.selected_questions[self.index].__dict__[opt]))
            self.listen_buttons[opt].grid(row=0, column=2, padx=10)

            self.option_frames.append(option_frame)

        self.display_new_question()

    def resize_background(self, event):
        new_width = event.width
        new_height = event.height
        self.background_image = Image.open("quizz.jpg")
        self.background_image = self.background_image.resize((new_width, new_height))
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label.config(image=self.background_photo)

    def update_timer(self):
        elapsed = int(time.time() - self.start_time)
        minutes = elapsed // 60
        seconds = elapsed % 60
        self.timer_label.config(text=f"Time: {minutes:02d}:{seconds:02d}")
        self.root.after(1000, self.update_timer)

    def display_new_question(self):
        if self.index < len(self.selected_questions):
            question = self.selected_questions[self.index]
            self.question_label.config(text=question.que)
            for opt in ["a", "b", "c", "d"]:
                self.buttons[opt].config(text=getattr(question, opt), bg="white")
            self.play_sound(question.que)
        else:
            self.start_voice_questions()

    def play_sound(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def submit_answer(self, answer):
        question = self.selected_questions[self.index]
        correct_btn = self.buttons[question.correct_answer]

        if answer == question.correct_answer:
            self.score += 1
            self.buttons[answer].config(bg="green")
        else:
            self.buttons[answer].config(bg="red")
            correct_btn.config(bg="green")

        self.root.after(1000, self.next_question)

    def next_question(self):
        self.index += 1
        self.display_new_question()

    def start_voice_questions(self):
        self.clear_screen()
        self.display_voice_question()

    def clear_screen(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def display_voice_question(self):
        if self.voice_index < len(self.selected_voice_questions):
            voice_question = self.selected_voice_questions[self.voice_index]
            self.question_label = tk.Label(self.frame, text=voice_question.sentence, font=("Arial", 16), wraplength=500, justify="center", bg='#2d3250', fg="White")
            self.question_label.pack(pady=20, expand=True)

            self.mic_button = tk.Button(self.frame, text="🎤", font=("Arial", 40), bg="white", command=self.check_voice_answer)
            self.mic_button.pack(pady=20)

            self.play_sound(voice_question.sentence)
        else:
            self.show_results()

    def check_voice_answer(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                self.mic_button.config(bg="yellow")
                audio = r.listen(source, timeout=5)
                text = r.recognize_google(audio).lower()

                correct_answer = self.selected_voice_questions[self.voice_index].answer.lower()
                if text == correct_answer:
                    self.score += 1
                    self.mic_button.config(bg="green")
                else:
                    self.mic_button.config(bg="red")
            except Exception:
                self.mic_button.config(bg="red")

        self.root.after(1500, self.next_voice_question)

    def next_voice_question(self):
        self.voice_index += 1
        self.clear_screen()
        self.display_voice_question()

    def show_results(self):
        total_time = int(time.time() - self.start_time)
        self.save_leaderboard(self.nickname, self.score, total_time)
        rankings = self.load_leaderboard()

        result_text = f"Your score: {self.score}/{len(self.selected_questions) + len(self.selected_voice_questions)}\n\nLeaderboard:\n"
        for i, entry in enumerate(rankings, start=1):
            result_text += f"{i}. {entry['nickname']} - Score: {entry['score']}, Time: {entry['time']}s\n"

        messagebox.showinfo("Results", result_text)
        self.root.destroy()

    def save_leaderboard(self, nickname, score, total_time):
        file_exists = os.path.exists("leaderboard.csv")
        with open("leaderboard.csv", mode="a", newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["nickname", "score", "time"])
            writer.writerow([nickname, score, total_time])

    def load_leaderboard(self):
        entries = []
        if os.path.exists("leaderboard.csv"):
            with open("leaderboard.csv", mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    entries.append({
                        "nickname": row["nickname"],
                        "score": int(row["score"]),
                        "time": int(row["time"])
                    })
        return sorted(entries, key=lambda x: (-x["score"], x["time"]))

    def skip_question(self):
        if self.index < len(self.selected_questions):
            self.index += 1
            self.display_new_question()
        elif self.voice_index < len(self.selected_voice_questions):
            self.voice_index += 1
            self.clear_screen()
            self.display_voice_question()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
