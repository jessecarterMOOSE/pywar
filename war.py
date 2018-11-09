from random import shuffle
import matplotlib.pyplot as plt


def play(shuffle_won_cards=True, verbose=False, max_hands=10000, plot_progress=False):
    deck = range(2, 15)*4
    shuffle(deck)

    if verbose:
        print 'starting deck:'
        print deck
        print

    player1 = deck[::2]
    player2 = deck[1::2]

    if verbose:
        print 'player 1 staring deck:', player1
        print 'player 2 staring deck:', player2

    hand_num = 0

    player1_num_cards = [len(player1)]
    player2_num_cards = [len(player2)]

    done = False

    while not done:

        table = []

        card1 = player1.pop(0)
        card2 = player2.pop(0)

        table.append(card1)
        table.append(card2)

        done_with_hand = False
        while not done_with_hand:
            if card1 > card2:
                if verbose:
                    print 'player 1 wins, gets:', table
                done_with_hand = True
                if shuffle_won_cards:
                    shuffle(table)
                player1 += table
            elif card1 < card2:
                if verbose:
                    print 'player 1 wins, gets:', table
                done_with_hand = True
                if shuffle_won_cards:
                    shuffle(table)
                player2 += table
            else:
                if verbose:
                    print 'WAR!'
                if len(player1) < 4 or len(player2) < 4:
                    done = True
                    break
                for _ in range(1, 4):
                    card1 = player1.pop(0)
                    card2 = player2.pop(0)

                    table.append(card1)
                    table.append(card2)

                card1 = player1.pop(0)
                card2 = player2.pop(0)

                table.append(card1)
                table.append(card2)

        hand_num += 1

        if verbose:
            print 'after hand', hand_num
            print 'player 1 has', len(player1), 'cards:', player1
            print 'player 2 has', len(player2), 'cards:', player2

        player1_num_cards.append(len(player1))
        player2_num_cards.append(len(player2))

        if len(player1) is 0 or len(player2) is 0:
            done = True

        if hand_num >= max_hands:
            print 'reached maximum number of hands, starting over'
            done = True

    if plot_progress:
        plt.plot(range(0, hand_num+1), player1_num_cards, label='player 1', lw=1, alpha=0.8)
        plt.plot(range(0, hand_num+1), player2_num_cards, label='player 2', lw=1, alpha=0.8)

        plt.legend()
        plt.show()

    return hand_num

num_rounds = 1000
counts = []
for i in range(0, num_rounds):
    if i % 100 == 0:
        print 'done with', i, 'rounds'
    counts.append(play())

plt.hist(counts, bins='auto', normed=True)
plt.show()