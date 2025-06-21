init python:
    import random

# Definir as imagens das cartas (exemplo, as cartas de Card1.png até Card10.png)
image Card1 = "images/Card1.png"
image Card2 = "images/Card2.png"
image Card3 = "images/Card3.png"
image Card4 = "images/Card4.png"
image Card5 = "images/Card5.png"
image Card6 = "images/Card6.png"
image Card7 = "images/Card7.png"
image Card8 = "images/Card8.png"
image Card9 = "images/Card9.png"
image Card10 = "images/Card10.png"

# Definir o fundo da imagem
image background = "images/background_cart.jpg"
image defeat = "images/Lose.png"
image vitorias = "images/Win.png"
# Definir os efeitos das cartas
define card_effects = {
    1: "Hate",
    2: "Devil",
    3: "Poison",
    4: "Like",
    5: "God",
    6: "Heal",
    7: "Skip",
    8: "Instant Win",
    9: "Die",
    10: "Immortal",
}

# Definir variáveis do jogador
define pontos = 0
define turns = 0

label start:
    # Exibe o fundo de fundo
    show background

    "Seja Bem Vindo ás cartas da Vida"
    "O seu objetivo é conseguirem o máximo numero de pontos possível"
    "Boa sorte"

    while turns < 10:
        $ selected_card_numbers = random.sample(range(1, 11), 3)
        
        # Exibe as imagens das cartas nas posições específicas
        $ card0 = "Card" + str(selected_card_numbers[0])
        $ card1 = "Card" + str(selected_card_numbers[1])
        $ card2= "Card" + str(selected_card_numbers[2])
        show expression card0 at left
        show expression card1 at center
        show expression card2 at right
        

        # Exibe uma mensagem para o jogador
        "Aqui estão suas cartas aleatórias. Clique em uma delas para ver o efeito."

        # Espera o jogador clicar em uma das cartas
        menu:
            "Carta Esquerda":
                call carta_effect_1
            "Carta Centro":
                call carta_effect_2
            "Carta Direita":
                call carta_effect_3

        # Pausa para o jogador ver o resultado
        "Tu tens [pontos] e já jogaste [turns]"

        $ turns += 1
    
    if pontos < 0: 
        jump derrota
    if pontos > 0: 
        jump vitoria
    
    return

label carta_effect_1:
    window hide
    "Você escolheu a carta da esquerda."
    
    # Aplica o efeito da carta 1
    $ selected_card_number = selected_card_numbers[0]
    if selected_card_number == 1:
        "Você jogou a hate card, perdes 10 pontos."
        $ pontos -= 10
    elif selected_card_number == 2:
        "Você jogou a devil card, perdes 30 pontos."
        $ pontos -= 30
    elif selected_card_number == 3:
        "Você jogou a poison card, perdes 50 pontos."
        $ pontos -= 50
    elif selected_card_number == 4:
        "Você jogou a like card, perdes 5 pontos."
        $ pontos += 5
    elif selected_card_number == 5:
        "Você jogou a God card, perdes 15 pontos."
        $ pontos += 15
    elif selected_card_number == 6:
        "Você jogou a Heal card, perdes 25 pontos."
        $ pontos += 25
    elif selected_card_number == 7:
        "Você jogou a Skip, saltas um turno."
        $ turns += 1
    elif selected_card_number == 8:
        "Você jogou a Instant Win card, Ganhaste!"
        jump vitoria 
    elif selected_card_number == 9:
        "Você jogou a Die card."
        jump derrota
    elif selected_card_number == 10:
        "Você jogou a Immortal card, Ganhaste 500 pontos."
        $ pontos += 500

    window show
    return

label carta_effect_2:
    window hide
    "Você escolheu a carta do meio."
    
    $ selected_card_number = selected_card_numbers[1]
    if selected_card_number == 1:
        "Você jogou a hate card, perdes 10 pontos."
        $ pontos -= 10
    elif selected_card_number == 2:
        "Você jogou a devil card, perdes 30 pontos."
        $ pontos -= 30
    elif selected_card_number == 3:
        "Você jogou a poison card, perdes 50 pontos."
        $ pontos -= 50
    elif selected_card_number == 4:
        "Você jogou a like card, perdes 5 pontos."
        $ pontos += 5
    elif selected_card_number == 5:
        "Você jogou a God card, perdes 15 pontos."
        $ pontos += 15
    elif selected_card_number == 6:
        "Você jogou a Heal card, perdes 25 pontos."
        $ pontos += 25
    elif selected_card_number == 7:
        "Você jogou a Skip, saltas um turno."
        $ turns += 1
    elif selected_card_number == 8:
        "Você jogou a Instant Win card, Ganhaste!"
        jump vitoria 
    elif selected_card_number == 9:
        "Você jogou a Die card."
        jump derrota
    elif selected_card_number == 10:
        "Você jogou a Immortal card, Ganhaste 500 pontos."
        $ pontos += 500

    window show
    return

label carta_effect_3:
    window hide
    "Você escolheu a carta da direita."
    
    $ selected_card_number = selected_card_numbers[2]
    if selected_card_number == 1:
        "Você jogou a hate card, perdes 10 pontos."
        $ pontos -= 10
    elif selected_card_number == 2:
        "Você jogou a devil card, perdes 30 pontos."
        $ pontos -= 30
    elif selected_card_number == 3:
        "Você jogou a poison card, perdes 50 pontos."
        $ pontos -= 50
    elif selected_card_number == 4:
        "Você jogou a like card, perdes 5 pontos."
        $ pontos += 5
    elif selected_card_number == 5:
        "Você jogou a God card, perdes 15 pontos."
        $ pontos += 15
    elif selected_card_number == 6:
        "Você jogou a Heal card, perdes 25 pontos."
        $ pontos += 25
    elif selected_card_number == 7:
        "Você jogou a Skip, saltas um turno."
        $ turns += 1
    elif selected_card_number == 8:
        "Você jogou a Instant Win card, Ganhaste!"
        jump vitoria 
    elif selected_card_number == 9:
        "Você jogou a Die card."
        jump derrota
    elif selected_card_number == 10:
        "Você jogou a Immortal card, Ganhaste 500 pontos."
        $ pontos += 500

    return

label derrota: 
    show defeat:
        zoom 1
    "Perdeste"
    $renpy.quit()
    return

label vitoria: 
    show vitorias:
        zoom 2
    "Ganhaste"
    $renpy.quit()
    return