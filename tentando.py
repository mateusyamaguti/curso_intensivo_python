class Player:
    def __init__(self):
        self.set_player_name()

    def set_player_name(self):
        self.name = str(input("Player, what's you name?\n"))




def test_set_player_name(monkeypatch):
    # provided inputs
    name = 'Tranberd'

    # creating iterator object
    answers = iter([name])

    # using lambda statement for mocking
    monkeypatch.setattr('builtins.input', lambda name: next(answers))

    player = Player()
    assert player.name == name

