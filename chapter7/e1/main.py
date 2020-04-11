from chapter7.e1.game import Player, BlackJack


def main():
    """
    Let's play Black Jack!
    """
    player1 = Player()
    player2 = Player()

    game = BlackJack()
    deck = game.get_initial_deck()

    game.add_player(player1).add_player(player2)

    player1.draw(deck).draw(deck)  # 2枚引く
    player2.draw(deck).draw(deck).draw(deck)  # 3枚引く

    print("####### Battle! ########")
    print(f"player1's hand: {[card for card in player1.hand]}")
    print(f"player2's hand: {[card for card in player2.hand]}")
    print(f"player1: {player1.evaluate_hand()} points")
    print(f"player2: {player2.evaluate_hand()} points")
    print(
        f"Win for player{1 if player1.evaluate_hand() > player2.evaluate_hand() else 2}!!!!!!"
    )


if __name__ == "__main__":
    main()
