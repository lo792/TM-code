# Design du programme
## Architecture
## Classes
### Features
```mermaid
classDiagram
  class PlanWord {
    +list<str> blue_words
    +list<str> red_words
    +list<str> grey_words
    +str black_word
    +initialize(words)
    -select8Words()
  }
  class Announce {
    +int tour
    +str word
    +int times
  }
  class Leader {
    +PlanWord plan
    +list[Announce] announces
    +play(PlanWord plan, int tour) Announce
  }
  Leader *-- "1" PlanWord
  class Player {
    +list<list<str>> selectedResponseWords
    +play(Announce, wordList, tour) selectedWords
  }
  class Team {
    +int score
    +Player player
    +Leader leader
  }
  Team *-- Leader
  Team *-- Player
  class WordList {
    +list<str> words
    +initialize()
    -select_25_random_words() list<str>
  }
  class Game {
    +WordList wordsList
    +PlanWord planWord
    +Team redTeam
    +Team blueTeam
    +start_game()
    +end_game()
    +run_tour(Team team, PlanWord plan, WorldList words) int
    -check_winner_or_loser()
  }
  Game o-- "2" Team
  Game o-- "1" WordList
  class GameFactory {
    +buildGameWithRandomTeams(list<str> participants) Game
    +buildGameWithTeams(Team blue, Team red) Game
  }
  GameFactory ..|> Game : build
```
### User Inerface (UI)
```mermaid
classDiagram
  class Dimensions {
    +int width
    +int height
  }
  class Card {
    +Dimensions
    +str word_to_display
    +display()
  }
  class ScoreDisplayer {
    +int red_team_score
    +int blue_team_score
    +display()
  }
  class Board {
    +Dimensions dimensions
    +ScoreDisplayer scoreDisplayer
    +list[Card] cards
    +display()

  }
