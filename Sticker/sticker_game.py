"""
For the game first i  need to hace a picture of stickers,
Two players are there,
simultaneously card is shown,
options for the victory base on : if starting letter of the name matches the opponent card , same of the card i.e same person as the opponent's , or have the exaclty same card as the one of your opponent,
if one wins then the shown card are won by the winner.
"""


import pygame as p, random as r

p.init()


w, h =720, 600
win = p.display.set_mode((w, h))

imgs = {}
background = p.transform.scale(p.image.load('BACKGROUND.jpg'), (w ,h))

""" are the variables needed for the game"""
x ,y = 100, 200
player_gap = 300



# properties of the rectangle
b1_width, b1_height = b2_width, b2_height = 125, 50
menu_font = p.font.Font('Cute Notes.ttf', 50)                    # for the game name
menu_title_font = p.font.Font('All Things Must Pass.ttf', 30)      # for the game mode
menu_title_font1 = p.font.Font('All Things Must Pass.ttf', 20)    # for the option


font = p.font.SysFont("san-serif", 30)
font2 = p.font.SysFont("san-serif", 40)

font1 = p.font.SysFont("courier", 25, False, True)

# textt
menu_words = menu_font.render("Sticker Khelchas?" , True, (10, 255, 113))
menu_title = menu_title_font.render("PLAY MODE", True , (255,255,255))


text = font.render("PLACE" , True, (0, 0, 0))

# blitting the buttons
b1_x , b1_y = 300, h - 70
global temporary_value_one ,temporary_value_two
temporary_value_one, temporary_value_two = 0, 0




def loadImage():
    global characters
    win.blit(background, (0, 0))
    characters = ["chris", "triple", "gold", "under", "kurt", "kane", "brock", "rock", "big", "mark", "edge", "trish",
                  "shannon", "molly", "shelton", "bradshaw", "hardcore", "train", "booker-t", "booker-t", "robvandom",
                  "rhino", "billy","lita", "matthardy", "bubba", "matt", "faroo", "dvon","ricflair", "lance","scotty","tajiri", "charlie"]

    for chars in characters:
        imgs[chars] = p.transform.scale(p.image.load('images/' + chars + '.jpg'), (150, 250))

def menu():
    global letter_game , dittu_game
    run = True
    clr1, clr2 = "blue" , "blue"
    dittu_game = False
    letter_game = False

    a1 , b1 = 250,350   # for the "same" mode
    a2, b2 = 250, 420       # for the "dittu" mode
    we , he = 150, 40          #width and height of the rectangle around the modes
    while run:
        same = menu_title_font1.render("1. NAME", True, p.Color(clr1))
        dittu = menu_title_font1.render("2. DITTU", True, p.Color(clr2))
        win.blit(background, (0, 0))
        win.blit(menu_words, (5, 60))
        win.blit(menu_title, (200, 200))
        p.draw.rect(win,  (82, 56, 51),(a1, b1 , we , he), 1)
        p.draw.rect(win,  (82, 56, 51),(a2, b2 , we , he), 1)

        win.blit(same, (a1, b1))
        win.blit(dittu, (a2, b2))

        for e in p.event.get():
            if e.type == p.QUIT:
                run = False
                p.quit()
            """ this code is for the hover effect """
            if e.type == p.MOUSEMOTION:
                m_x , m_y = p.mouse.get_pos()
                if m_x > a1 and m_x < a1 + we :
                    if m_y > b1 and m_y < b1 + he:
                        clr1 = "red"
                    else:
                        clr1 = "blue"
                else:
                    clr1 = "blue"
                if m_x > a2 and m_x < a2 + we :
                    if m_y > b2 and m_y < b2 + he:
                        clr2 = "red"
                    else:
                        clr2 = "blue"
                else:
                    clr2 = "blue"

            """for clicking the mode"""
            if e.type == p.MOUSEBUTTONDOWN:
                m_x, m_y = p.mouse.get_pos()
                if m_x > a1 and m_x < a1 + we:
                    if m_y > b1 and m_y < b1 + he:
                        letter_game = True
                        main()
                if m_x > a2 and m_x < a2 + we :
                    if m_y > b2 and m_y < b2 + he:
                        dittu_game = True
                        main()



        p.display.update()


def drawing():

    score = font1.render(f'playerone card remaining : {player_one_cards_remaining}', True, (p.Color("white")))
    score1 = font1.render(f'playertwo card remaining: {player_two_cards_remaining}', True, (p.Color("white")))
    win.blit(score, (100, 20))
    win.blit(score1, (100, 40))
    p.display.update()

def ending(player):

    remarks = font2.render(f"{player} won in this round", True, (255, 255,255))
    win.blit(remarks, (200, 80))
    p.display.update()
    p.time.wait(1000)
    main()

player_one = True
first_game = True

def main():
    global  temporary_value_one, temporary_value_two, first_game, player_one, player_one_cards_remaining, player_two_cards_remaining

    run = True
    loadImage()
    game_won = False
    colors = "green"
    clock = p.time.Clock()
    characters = ["chris", "triple", "gold", "under", "kurt", "kane", "brock", "rock", "big", "mark", "edge", "trish",
                  "shannon", "molly","shelton","bradshaw", "hardcore", "train", "booker-t","booker-t", "robvandom","rhino", "billy",
                  "lita", "matthardy", "bubba", "matt", "faroo", "dvon","ricflair", "lance","scotty","tajiri", "charlie"]
    length = len(characters) - r.randrange(1,10)
    player_one_cards_remaining = 30 if first_game else temporary_value_one
    player_two_cards_remaining = 30 if first_game else temporary_value_two
    ran = r.randint(0, length)
    ran1 = r.randint(0, length)

    # counting the card number
    global  card_number_one ,card_number_two
    card_number_one, card_number_two = 0, 0
    while run:
        clock.tick(60)
        rand_x = r.randrange(0, 50)  # for the orientation of the cards
        rand_y = r.randrange(0, 50)
        p.draw.rect(win, colors, (b1_x, b1_y, b1_width, b1_height))
        # blitting the text
        win.blit(text, (b1_x + 25, b1_y + 15))  # here text is "place" word
        for e in p.event.get():
            if e.type == p.QUIT:
                run = False
                p.quit()
            if e.type == p.KEYDOWN:
                if e.key == p.K_m:
                    menu()
            if e.type == p.MOUSEBUTTONDOWN:
                m_x , m_y = p.mouse.get_pos()


                if player_one and player_one_cards_remaining > 0 and not game_won:
                    ran = r.randint(0, length)
                    if m_x > b1_x and m_x < b1_x + b1_width:
                        if m_y >  b1_y and m_y < b1_y + b1_height:
                            colors = "light blue"
                            win.blit(imgs[characters[ran]], (x + rand_x, y + rand_y))
                            card_number_one += 1                                                             # keeps track of the number of cards that has been drawned
                            player_one = not player_one
                            print(ran, ran1)

                            if letter_game:
                                if characters[ran][0] == characters[ran1][0]:
                                    player_two_cards_remaining -= card_number_two     # card number will subtract the remaining cards of the player who lost the round
                                    player_one_cards_remaining += card_number_two     # if player one wins the game then it will add the number of cards of player two cards
                                    temporary_value_two = player_two_cards_remaining
                                    temporary_value_one = player_one_cards_remaining
                                    card_number_one = card_number_two = 0
                                    first_game = False
                                    player_one = not player_one                               # used to make the turn after victory
                                    game_won = True
                                    ending("Player 1")
                                if dittu_game:
                                    if ran == ran1:
                                        player_two_cards_remaining -= card_number_two  # card number will subtract the remaining cards of the player who lost the round
                                        player_one_cards_remaining += card_number_two  # if player one wins the game then it will add the number of cards of player two cards
                                        temporary_value_two = player_two_cards_remaining
                                        temporary_value_one = player_one_cards_remaining
                                        card_number_one = card_number_two = 0
                                        first_game = False
                                        player_one = not player_one  # used to make the turn after victory
                                        game_won = True
                                        ending("Player 1")
                elif not player_one and player_two_cards_remaining > 0 and not game_won:
                    ran1 = r.randint(0, length)
                    colors = "green"
                    win.blit(imgs[characters[ran1]], (x + player_gap + rand_x, y + rand_y))
                    card_number_two += 1
                    player_one = not player_one
                    print(ran, ran1)

                    if letter_game:
                        if characters[ran1][0] == characters[ran][0]:
                            player_one_cards_remaining -= card_number_one
                            player_two_cards_remaining += card_number_one    # similar to player one comment
                            print( ran, ran1)
                            temporary_value_two = player_two_cards_remaining
                            temporary_value_one = player_one_cards_remaining
                            card_number_one = card_number_two = 0
                            first_game = False
                            player_one = player_one                    # used to make the turn after victory
                            game_won = True
                            ending("Player 2")
                    if dittu_game:

                        if ran1 == ran:
                            player_one_cards_remaining -= card_number_one
                            player_two_cards_remaining += card_number_one  # similar to player one comment
                            temporary_value_two = player_two_cards_remaining
                            temporary_value_one = player_one_cards_remaining
                            card_number_one = card_number_two = 0
                            first_game = False
                            player_one = player_one  # used to make the turn after victory
                            game_won = True
                            ending("Player 2")



        drawing()
        p.display.update()

if __name__ == '__main__':
    menu()

p.quit()