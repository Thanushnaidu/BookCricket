import tkinter as tk
from tkinter import messagebox
import random as r

class BookCricketGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Cricket Game")
        self.root.geometry("600x550")
        self.root.configure(bg="lightblue")

        # Game variables
        self.total_overs = 0
        self.total_pages = 0
        self.overs = 1
        self.balls = 1
        self.runs = 0
        self.wickets = 0
        self.scorea = 0
        self.is_first_innings = True

        # UI setup
        self.setup_ui()

    def setup_ui(self):
        # Title
        tk.Label(self.root, text="Book Cricket", font=("Arial", 22, "bold"), bg="lightblue").pack(pady=10)

        # Input for overs and pages
        tk.Label(self.root, text="Enter number of overs:", bg="lightblue", font=("Arial", 12)).pack()
        self.overs_entry = tk.Entry(self.root)
        self.overs_entry.pack()

        tk.Label(self.root, text="Enter total number of pages:", bg="lightblue", font=("Arial", 12)).pack()
        self.pages_entry = tk.Entry(self.root)
        self.pages_entry.pack()

        # Buttons
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game,
                                      font=("Arial", 12, "bold"), bg="green", fg="white")
        self.start_button.pack(pady=15)

        self.bowl_button = tk.Button(self.root, text="Bowl Next Ball", command=self.bowl_ball,
                                     font=("Arial", 12, "bold"), bg="blue", fg="white", state="disabled")
        self.bowl_button.pack(pady=10)

        self.restart_button = tk.Button(self.root, text="Restart Game", command=self.restart_game,
                                        font=("Arial", 12, "bold"), bg="orange", fg="black", state="disabled")
        self.restart_button.pack(pady=5)

        # Info display
        self.info_frame = tk.Frame(self.root, bg="white", bd=2, relief="sunken")
        self.info_frame.pack(pady=15, fill="x")

        self.over_ball_label = tk.Label(self.info_frame, text="Over: 0 | Ball: 0", font=("Arial", 12), bg="white")
        self.over_ball_label.pack(pady=5)

        self.page_label = tk.Label(self.info_frame, text="Page number: ", font=("Arial", 12), bg="white")
        self.page_label.pack(pady=5)

        self.runs_label = tk.Label(self.info_frame, text="Runs: 0 | Wickets: 0", font=("Arial", 12), bg="white")
        self.runs_label.pack(pady=5)

    def start_game(self):
        try:
            self.total_overs = int(self.overs_entry.get())
            self.total_pages = int(self.pages_entry.get())
            if self.total_overs <= 0 or self.total_pages <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid positive numbers for overs and pages.")
            return

        # Reset game state
        self.overs = 1
        self.balls = 1
        self.runs = 0
        self.wickets = 0
        self.is_first_innings = True

        # Enable bowl button and update UI
        self.bowl_button.config(state="normal")
        self.restart_button.config(state="disabled")
        self.update_labels()

    def bowl_ball(self):
        if self.overs > self.total_overs or self.wickets >= 10:
            self.end_innings()
            return

        result = r.randint(1, self.total_pages)
        self.page_label.config(text=f"Page number: {result}")

        if result % 10 == 0:
            self.wickets += 1
            messagebox.showinfo("Wicket!", f"Wicket! Batsman is out on page {result}")
        elif result % 10 == 4:
            self.runs += 4
        elif result % 10 == 6:
            self.runs += 6
        else:
            self.runs += result % 10

        # Move to next ball
        self.balls += 1
        if self.balls > 6:  # End of over
            self.balls = 1
            self.overs += 1
            if self.overs <= self.total_overs:
                messagebox.showinfo("End of Over", f"End of over {self.overs - 1}")

        if self.overs > self.total_overs or self.wickets >= 10:
            self.end_innings()
        else:
            self.update_labels()

    def update_labels(self):
        self.over_ball_label.config(text=f"Over: {self.overs} | Ball: {self.balls}")
        self.runs_label.config(text=f"Runs: {self.runs} | Wickets: {self.wickets}")

    def end_innings(self):
        if self.is_first_innings:
            self.scorea = self.runs
            messagebox.showinfo("End of Innings", f"First innings over!\nScore: {self.runs}/{self.wickets}")
            self.reset_for_second_innings()
        else:
            scoreb = self.runs
            if self.scorea > scoreb:
                winner = "Team 1"
            elif scoreb > self.scorea:
                winner = "Team 2"
            else:
                winner = "Match Tied"
            messagebox.showinfo("Game Over", f"Match Over!\nTeam 1: {self.scorea}\nTeam 2: {scoreb}\nWinner: {winner}")
            self.bowl_button.config(state="disabled")
            self.restart_button.config(state="normal")

    def reset_for_second_innings(self):
        self.is_first_innings = False
        self.overs = 1
        self.balls = 1
        self.runs = 0
        self.wickets = 0
        self.update_labels()

    def restart_game(self):
        self.start_button.config(state="normal")
        self.bowl_button.config(state="disabled")
        self.restart_button.config(state="disabled")
        self.page_label.config(text="Page number: ")
        self.runs_label.config(text="Runs: 0 | Wickets: 0")
        self.over_ball_label.config(text="Over: 0 | Ball: 0")
        self.overs_entry.delete(0, tk.END)
        self.pages_entry.delete(0, tk.END)


# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = BookCricketGUI(root)
    root.mainloop()
