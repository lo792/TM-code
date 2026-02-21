# Design du programme
## Architecture
## Classes
### Features
```mermaid
classDiagram
  class WordType {
    str type (red, blue, black, grey)
  }
  class PlanWord {
    +list<str> blue_words
    +list<str> red_words
    +list<str> grey_words
    +str black_word
    +initialize(list<str> words)
    -select8Words()
    -get_word_type(str word) WordType
  }
  class Announce {
    +int tour
    +str word
    +int times
  }
  class Leader {
    +str name
    +PlanWord plan
    +list[Announce] announces
    +play(PlanWord plan, int tour) Announce
  }
  Leader *-- "1" PlanWord
  class Player {
    +str name
    +list<list<str>> selectedResponseWords
    +play(Announce, wordList, tour) selectedWords
  }
  class Team {
    +int score
    +Player player
    +Leader leader
    +add_point_sore()
  }
  Team *-- Leader
  Team *-- Player
  class WordList {
    +list<str> words
    +initialize()
    -select_25_random_words() list<str>
  }
  class State {
    +str state
  }
  class StateEnd {
    +str state = "fin du jeux"
  }
  class StateEndTour {
    +str state = "fin du tour"
  }
  class StateKeepOn {
    +str state = "on continue"
  }
  State <|-- StateEnd : instance
  State <|-- StateEndTour : instance
  State <|-- StateKeepOn : instance
  class Game {
    +WordList wordsList
    +PlanWord planWord
    +Team redTeam
    +Team blueTeam
    +start_game()
    +end_game()
    +run_tour(Team team)
    -check(str selectedWord, PlanWord plan, Team redteam, Team blueteam) State
  }
  Game o-- "2" Team
  Game o-- "1" WordList
  class GameFactory {
    +buildGameWithRandomTeamsAndRoles(list<str> participants) Game
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
  class CardGrid {
    +list<Card> cards
    +display()
  }
  class ScoreDisplayer {
    +int red_team_score
    +int blue_team_score
    +display()
  }
  class TourDisplayer {
    +str messsage
    +display()
  }
  class TeamDisplayer {
    +Team team
    +display()
  }
  class AnnounceDisplayer {
    +Announce announce
    +display()
  }
  class Sreen {
    +CardGrid cardGrid
    +ScoreDisplayer scoreDisplayer
    +TourDisplayer tourDisplayer
    +TeamDisplayer teamDisplayer
  }
  class PlayerScreen {
    +AnnounceDisplayer announceDisplayer
    +display()
  }
  class LeaderSreen {
    +PlanWord plan
    +display()
    -applyPlanWord() transformedPlanGrid
  }
  Screen <|-- PlayerScreen
  Screen <|-- LeaderScreen
  class Board {
    +Dimensions dimensions
    +checkIn() Screen
    +display()

  }
