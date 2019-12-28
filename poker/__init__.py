import random


class Card(object):
    """一张牌"""

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)

    def __repr__(self):
        return self.__str__()


class Poker(object):
    """一副牌"""

    def __init__(self):
        self._cards = [Card(suite, face)
                       for suite in '♠♥♣♦'
                       for face in range(1, 14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌(随机乱序)"""
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌"""
        return self._current < len(self._cards)


class Player(object):
    """玩家"""

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []
        self._score = 0

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    @property
    def score(self):
        return self._score

    def get(self, card):
        """摸牌"""
        self._cards_on_hand.append(card)
        if 1 < card.face < 10:
            self._score += card.face
        elif card.face > 9:
            self._score += 10
        else :
            if self._score + 10 > 21:
                self._score += 1
            else:
                self._score += 10

    def arrange(self, card_key):
        """玩家整理手上的牌"""
        self._cards_on_hand.sort(key=card_key)


# 排序规则-先根据花色再根据点数排序
def get_key(card):
    return (card.suite, card.face)


def main():
    p = Poker()
    p.shuffle()
    players = [Player('dealer'), Player('player')]
    for _ in range(2):
        for player in players:
            player.get(p.next)
    print(players[0].name + ':', end=' ')
    print(players[0].cards_on_hand[0], '**')
    print(players[1].name + ':', end=' ')
    print(players[1].cards_on_hand, player.score)
    dealer_win = False
    while True:
        if input('enter y for draw a card , enter n for skip:') == 'y':
            players[1].get(p.next)
            print(players[1].name + ':', end=' ')
            player.arrange(get_key)
            print(players[1].cards_on_hand, player.score)
        else:
            print(players[1].name + ':', end=' ')
            player.arrange(get_key)
            print(players[1].cards_on_hand, player.score)
            break
        if players[1].score > 21:
            print('bust , dealer win')
            dealer_win = True
            break
    while not dealer_win:
        print(players[0].name + ':', end=' ')
        print(players[0].cards_on_hand, players[0].score)
        if players[0].score > 21:
            print('bust , player win')
            break
        elif players[0].score > players[1].score:
            print('dealer win')
            break
        else:
            players[0].get(p.next)


if __name__ == '__main__':
    main()
