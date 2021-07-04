from brain import Brain
from tkinter import *

window = Tk()
window.title("Faras")

computer_score_data = 0
player_score_data = 0


def button_press():
    """
    Function to update all cards with proper value cards.
    :return:
    """
    brain = Brain()
    result_label.config(text=brain.win_check())
    score_check(brain.win_check())
    # --------------UPDATE COMPUTER IMAGES---
    computer_canvas1.computer1_img = PhotoImage(file=f"./assets/{brain.computer_cards[0]}.png")
    computer_canvas1.itemconfig(computer1, image=computer_canvas1.computer1_img)

    computer_canvas2.computer2_img = PhotoImage(file=f"./assets/{brain.computer_cards[1]}.png")
    computer_canvas2.itemconfig(computer2, image=computer_canvas2.computer2_img)

    computer_canvas3.computer3_img = PhotoImage(file=f"./assets/{brain.computer_cards[2]}.png")
    computer_canvas3.itemconfig(computer3, image=computer_canvas3.computer3_img)

    # --------------UPDATE PLAYER IMAGES------
    player_canvas1.player1_img = PhotoImage(file=f"./assets/{brain.player_cards[0]}.png")
    player_canvas1.itemconfig(player1, image=player_canvas1.player1_img)

    player_canvas2.player2_img = PhotoImage(file=f"./assets/{brain.player_cards[1]}.png")
    player_canvas2.itemconfig(player2, image=player_canvas2.player2_img)

    player_canvas3.player3_img = PhotoImage(file=f"./assets/{brain.player_cards[2]}.png")
    player_canvas3.itemconfig(player3, image=player_canvas3.player3_img)

    press_button.config(text="Replay")


def score_check(win_data):
    global computer_score_data, player_score_data
    win_list = str(win_data).split(" ", )
    if win_list[0].lower() == "player":
        player_score_data += 1
        player_score.config(text=f"Player: {player_score_data}")
    else:
        computer_score_data += 1
        computer_score.config(text=f"Computer: {computer_score_data}")


computer_canvas1 = Canvas(height=264, width=172)
computer_card1_img = PhotoImage(file="./assets/computer_back.png")
computer1 = computer_canvas1.create_image(86, 132, image=computer_card1_img)
computer_canvas1.grid(column=0, row=1)

computer_canvas2 = Canvas(height=264, width=172)
computer_card2_img = PhotoImage(file="./assets/computer_back.png")
computer2 = computer_canvas2.create_image(86, 132, image=computer_card2_img)
computer_canvas2.grid(column=1, row=1)

computer_canvas3 = Canvas(height=264, width=172)
computer_card3_img = PhotoImage(file="./assets/computer_back.png")
computer3 = computer_canvas3.create_image(86, 132, image=computer_card3_img)
computer_canvas3.grid(column=2, row=1)
# # ----------------------------------------------------

computer_score = Label(text=f"Computer: 0", font=("Arial", 12, "bold"))
computer_score.grid(row=0, column=0)

player_score = Label(text=f"Player: 0", font=("Arial", 12, "bold"))
player_score.grid(row=0, column=2)

result_label = Label(font=("Impact", 24, "normal"), fg="green")
result_label.grid(column=0, row=2, columnspan=3)
#
press_button = Button(text="Start Game", font=("Impact", 16, "normal"), command=lambda: button_press())
press_button.grid(column=0, row=3, columnspan=3)
#
# # --------------------------------------------------
player_canvas1 = Canvas(height=264, width=172)
player_card1_img = PhotoImage(file="./assets/player_back.png")
player1 = player_canvas1.create_image(86, 132, image=player_card1_img)
player_canvas1.grid(column=0, row=4)

player_canvas2 = Canvas(height=264, width=172)
player_card2_img = PhotoImage(file="./assets/player_back.png")
player2 = player_canvas2.create_image(86, 132, image=player_card1_img)
player_canvas2.grid(column=1, row=4)

player_canvas3 = Canvas(height=264, width=172)
player_card3_img = PhotoImage(file="./assets/player_back.png")
player3 = player_canvas3.create_image(86, 132, image=player_card1_img)
player_canvas3.grid(column=2, row=4)

window.mainloop()
