import random
import time

class Dealer:
    def __init__(self):
        self.name = "Dealer"
        self.cards = []

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

def initiate_players():
    players = []

    num_players = int(input("How many players in the game?: "))
    for index in range(num_players):
        player_name = input("What's the name of the player {index}? ".format(index=index+1))
        players.append(Player(player_name))
    return players

def initiate_dealer():
    dealer = Dealer()
    return dealer

def shuffle_deck():
    deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10,"J","Q","K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10,"J","Q","K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10,"J","Q","K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10,"J","Q","K"]
    shuffled_deck = []
    for card in range(len(deck)):
        shuffled_deck.append(deck.pop(random.randint(0, len(deck)-1)))
    return shuffled_deck

def give_card(player):
        global deck
        player.cards.append(deck.pop(0))

def give_initial_cards(dealer, players):
    for player in players + [dealer]:
        give_card(player)
    for player in players + [dealer]:
        give_card(player)
    dealer.known_cards = dealer.cards[1]

def show_cards():
    cards = "\nPlayers cards:"
    for player in players:
        cards += ("\n{name}: {cards}".format(name=player.name, cards = player.cards))
    cards += ("\n{name}: {card}, unknown card".format(name = dealer.name, card = dealer.known_cards))
    print(cards)

def compute_points(cards):
    points = 0
    aces = 0
    for card in cards:
        if card in ["J", "Q", "K"]:
            points += 10
        elif card in range(2,11):
            points += card
        else:
            aces += 1
    for ace in range(aces):
        if points <= 10:
            points += 11
        else:
            points +=1
    return points

def player_turn(player):
    time.sleep(5)
    print("\n----- {name}'s Turn ------".format(name=player.name))
    print("\nHi {name}, it's your turn!".format(name=player.name))
    print("\nYour cards: {cards}".format(cards = player.cards))
    player.points = compute_points(player.cards)
    print("Your points: {points}".format(points = player.points))
    if player.points == 21:
        print("Black JacK!")
    else:
        player_choice = input("\nDo you want another card? (y/n) ")
        while player_choice != "n":
            while player_choice != "y":
                player_choice = input("\nDo you want another card? (y/n) ")
            give_card(player)
            print("Your cards: {cards}".format(cards = player.cards))
            player.points = compute_points(player.cards)
            print("Your points: {points}".format(points = player.points))
            if player.points > 21:
                print("You lost")
                player.points = 0
                break
            elif player.points == 21:
                print("Black Jack!")
                break
            else:
                player_choice = input("\nDo you want another card? (y/n) ")

def dealer_turn(dealer):
    players_points = []
    for player in players:
        players_points.append(player.points)
    dealer_playing = True
    while dealer_playing == True:
        dealer.points = compute_points(dealer.cards)
        print("\nDealer cards: {cards}".format(cards = dealer.cards))
        print("Dealer points: {points}".format(points = dealer.points))
        print("Dealer thinking...")
        time.sleep(5)
        players_to_beat = 0
        for point in players_points:
            if point > dealer.points:
                players_to_beat += 1
        if players_to_beat >= 1:
            print("\nDealer decided to get a new card.")
            give_card(dealer)
            if compute_points(dealer.cards) > 21:
                print("Dealer cards: {cards}".format(cards = dealer.cards))
                print("Dealer lost.")
                break
        else:
            dealer_playing = False
            print("\nDealer decided to stop.")
            print("Dealer won.")
            break

def end_game(dealer, players):
    for player in players + [dealer]:
        player.cards.clear()
        

players = initiate_players()
dealer = initiate_dealer()

playing = "y"

while playing != "n" :
    
    deck = shuffle_deck()
    print("\n-------Giving cards-----")
    time.sleep(3)
    give_initial_cards(dealer, players)
    show_cards()
    for player in players:
        player_turn(player)
    dealer_turn(dealer)
    end_game(dealer, players)

    playing = input("\n Press any key to go on playing. Else press n: ")
