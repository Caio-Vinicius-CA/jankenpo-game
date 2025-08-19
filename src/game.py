import random

choices = ["Pedra","Papel","Tesoura"]

class JanKenPo:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.draws = 0

    def play(self, player_choice):
        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            self.draws += 1
            result = "Empate!"
        elif (player_choice == "Pedra" and computer_choice == "Tesoura") or \
             (player_choice == "Papel" and computer_choice == "Pedra") or \
             (player_choice == "Tesoura" and computer_choice == "Papel"):
            self.player_score += 1
            result = "Você venceu!"
        else:
            self.computer_score += 1
            result = "Computador venceu!"

        return {
            "player":player_choice,
            "computer": computer_choice,
            "result": result,
            "score": {
                "player": self.player_score,
                "computer": self.computer_score,
                "draws": self.draws,
            }
        }
