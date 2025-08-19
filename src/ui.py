import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from game import JanKenPo

class JanKenPoUI:
    def __init__(self, root):
        self.root = root
        self.root.title("JanKenPo - Pedra, Papel, Tesoura")
        self.root.geometry("500x400")
        self.root.config(bg="#f0f0f0")
    
        self.game = JanKenPo()

        # Título
        self.label_title = tk.Label(root, text="Escolha sua Jogada!", font=("Arial", 18, "bold"), bg="#f0f0f0")
        self.label_title.pack(pady=10)

        # Área dos botões
        frame_buttons = tk.Frame(root, bg="#f0f0f0")
        frame_buttons.pack(pady=20)

        self.images = {
            "Pedra": ImageTk.PhotoImage(Image.open("assets/rock1.png").resize((80,80))),
            "Papel": ImageTk.PhotoImage(Image.open("assets/paper1.png").resize((80,80))),
            "Tesoura": ImageTk.PhotoImage(Image.open("assets/scissors1.png").resize((80,80)))
        }

        for choice, img in self.images.items():
            btn = tk.Button(frame_buttons, image=img, text=choice, compound="top", font=("Arial", 12), command=lambda c=choice: self.make_play(c))
            btn.pack(side="left", padx=15)

        # Label resultado
        self.label_result = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
        self.label_result.pack(pady=10)

        # Placar
        self.label_score = tk.Label(root, text="Você: 0 | Computador: 0\nEmpates: 0", font=("Arial", 12), bg="#f0f0f0")
        self.label_score.pack(pady=10)

    def make_play(self, player_choice):
        outcome = self.game.play(player_choice)

        self.label_result.config(
            text=f"Você escolheu: {outcome['player']} | Computador: {outcome['computer']}\n{outcome['result']}"
        )

        score = outcome['score']
        self.label_score.config(
            text=f"Você: {score['player']} | Computador: {score['computer']}\nEmpates: {score['draws']}"
        )
