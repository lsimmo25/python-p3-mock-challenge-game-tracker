class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
    
    @property
    def title(self):
        if isinstance(self._title, str) and len(self._title) > 0:
            return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, "_title"):
            print("Title has already been set")
        else:
            self._title = new_title


    def results(self):
        return self._results

    def players(self):
        return list({result.player for result in self._results})

    def average_score(self, player):
        player_results = [result.score for result in self._results if result.player == player]
        if not player_results:
            return 0
        else:
            return sum(player_results) / len(player_results)

class Player:
    def __init__(self, username):
        self.username = username
        self._results = []
    
    @property
    def username(self):
        return self._username

        
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2 <= len(new_username) <= 16:
            self._username = new_username
        else:
            raise ValueError("Username must be a string with length 2-16")



    def results(self):
        return self._results

    def games_played(self):
        return list({result.game for result in self._results if isinstance(result.game, Game)})

    def played_game(self, game):
        for result in self._results:
            if result.game == game:
                return True
        return False

    def num_times_played(self, game):
        return len([result.game for result in self._results if result.game == game])

class Result:
    all = []

    def __init__(self, player, game, score):
        if not isinstance(score, int):
            raise TypeError("Score must be an integer")
        self.player = player
        self.game = game
        self._score = score
        game.results().append(self)
        player.results().append(self)
        Result.all.append(self)
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        raise AttributeError("Score is immutable and cannot be modified")
    