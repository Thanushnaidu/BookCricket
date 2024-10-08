import tkinter as tk
from tkinter import messagebox
import random as r

class BookCricketGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Cricket Game")
        self.root.geometry("600x500")
        self.root.configure(bg="lightblue")

        # Game variables
        self.overs = 1
        self.runs = 0
        self.wickets = 0
        self.perf = 0
        self.balls = 1
        self.total_overs = 0
        self.total_pages = 0
        self.scorea = 0
        self.is_first_innings = True

        # Initialize UI components
        self.setup_ui()

    def setup_ui(self):
        # Title
        self.title_label = tk.Label(self.root, text="Book Cricket", font=("Arial", 20, "bold"), bg="lightblue")
        self.title_label.pack(pady=10)

        # Input fields for overs and pages
        self.overs_label = tk.Label(self.root, text="Enter no of overs:", font=("Arial", 12), bg="lightblue")
        self.overs_label.pack()
        self.overs_entry = tk.Entry(self.root)
        self.overs_entry.pack()

        self.pages_label = tk.Label(self.root, text="Enter total no of pages in textbook:", font=("Arial", 12), bg="lightblue")
        self.pages_label.pack()
        self.pages_entry = tk.Entry(self.root)
        self.pages_entry.pack()

        # Start button
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game, font=("Arial", 12, "bold"), bg="green", fg="white")
        self.start_button.pack(pady=20)

        # Display area for game info
        self.info_frame = tk.Frame(self.root, bg="white", bd=2, relief="sunken")
        self.info_frame.pack(pady=10)

        self.over_ball_label = tk.Label(self.info_frame, text="Over: 0 | Ball: 0", font=("Arial", 12), bg="white")
        self.over_ball_label.pack()

        self.page_label = tk.Label(self.info_frame, text="Page number: ", font=("Arial", 12), bg="white")
        self.page_label.pack()

        self.runs_label = tk.Label(self.info_frame, text="Runs: 0 | Wickets: 0", font=("Arial", 12), bg="white")
        self.runs_label.pack()

        # Bowl button
        self.bowl_button = tk.Button(self.root, text="Bowl Next Ball", command=self.bowl_ball, font=("Arial", 12, "bold"), bg="blue", fg="white")
        self.bowl_button.pack(pady=20)
        self.bowl_button.config(state="disabled")  # Disabled until the game starts

    def start_game(self):
        try:
            self.total_overs = int(self.overs_entry.get())
            self.total_pages = int(self.pages_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for overs and pages.")
            return

        self.overs = 1
        self.runs = 0
        self.wickets = 0
        self.perf = 0
        self.balls = 1
        self.scorea = 0
        self.is_first_innings = True

        # Update UI and enable the bowl button
        self.update_labels()
        self.bowl_button.config(state="normal")

    def bowl_ball(self):
        if self.balls > 6:
            return  # In case we exceed ball count, prevent further action

        n = range(0, self.total_pages)
        result = r.choice(n)
        self.page_label.config(text=f"Page number: {result}")

        if result % 10 == 0:
            self.wickets += 1
            messagebox.showinfo("Wicket!", f"Wicket! Batsman is out on page {result}")
        elif result % 10 == 4:
            self.runs += 4
            messagebox.showinfo("Four!", "That's a Four!")
        elif result % 10 == 6:
            self.runs += 6
            messagebox.showinfo("Six!", "It's a Six!")
        else:
            self.runs += result % 10

        self.balls += 1
        if self.balls > 6:
            self.end_over()

        # Check if innings or game is over
        if self.wickets >= 10 or self.overs > self.total_overs:
            self.end_innings()
            return

        # Update display
        self.update_labels()

    def update_labels(self):
        self.over_ball_label.config(text=f"Over: {self.overs} | Ball: {self.balls}")
        self.runs_label.config(text=f"Runs: {self.runs} | Wickets: {self.wickets}")

    def end_over(self):
        self.balls = 1
        self.overs += 1

        if self.overs > self.total_overs:
            self.end_innings()
        else:
            messagebox.showinfo("End of Over", f"End of over {self.overs - 1}")

    def end_innings(self):
        if self.is_first_innings:
            self.scorea = self.runs
            messagebox.showinfo("End of Innings", f"First innings over. Score: {self.runs}/{self.wickets}")
            self.reset_for_second_innings()
        else:
            self.end_game()

    def reset_for_second_innings(self):
        self.is_first_innings = False
        self.overs = 1
        self.runs = 0
        self.wickets = 0
        self.balls = 1
        self.update_labels()

    def end_game(self):
        scoreb = self.runs
        if self.scorea > scoreb:
            messagebox.showinfo("Game Over", f"1st Batting Team has won! ScoreA: {self.scorea}, ScoreB: {scoreb}")
        else:
            messagebox.showinfo("Game Over", f"2nd Batting Team has won! ScoreA: {self.scorea}, ScoreB: {scoreb}")

        self.bowl_button.config(state="disabled")  # Disable bowl button after game ends

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = BookCricketGUI(root)
    root.mainloop()
