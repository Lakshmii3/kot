# Software Architecture for King of Tokyo

## 1. Introduction

The main motivation behind documenting the architecture is to ensure the team is making good design decisions guided by separation of concerns and overall high cohesion in terms of designing the game. 

## 2. System Context

The major systems that comprise KOT are as follows:

- Django backend for routing and providing a RESTful API
- MySQL database for storing player and game session data
- Django channels for asynchronous Websocket communication
- React frontend for the user interface leveraging Redux

#### To do: Diagram should map out the basic systems involved with KOT and how they interact with each other.

## 2.1 Backend

### Vanilla Django

 Django is built around the simple concept of requests and responses: the browser makes a request, Django calls a view, which returns a response that’s sent back to the browser.  

![Vanilla](https://i.imgur.com/1HzpGJe.png_)

### Django Channels

Channels is a project that takes Django and extends its abilities beyond HTTP - to handle WebSockets, chat protocols. It’s built on a Python specification called ASGI (Asynchronous Server Gateway Interface).
It does this by taking the core of Django and layering a fully asynchronous layer underneath, running Django itself in a synchronous mode but handling connections and sockets asynchronously, and giving you the choice to write in either style.

Django Channels supports WebSockets which is a protocol that provides full-duplex communication — a persistent, open connection between the client and the server, with either able to send data at any time.

Channels also allow for background tasks that run on the same servers as the rest of Django. HTTP requests continue to behave the same as before, but also get routed over channels

Channels are essentially task queues: messages get pushed onto the channel by producers, and then given to one of the consumers listening on that channel. 
Channels is designed to use Redis as its preferred channel layer, though there is support for other types.

**This means we might have to set up a Redis instance for WebSocket communication along with the MySQL for Django's HTTP requests**

![Django with Channels](https://i.imgur.com/Ds5TcD3.png)

## 2.2 Midtier
#### To do

## 2.3 Frontend

The websites frontend infrastructure will leverage React and [Flux](https://github.com/facebook/flux "Facebook Flux on GitHub") application architecture. Flux was developed to utilize a unidirectional data flow in React.

The UI team has not yet completely decided which architectural data and state management approach to utilize. We intend to investigating Redux and Facebooks more recent Flux implementation. Redux differs from Flux since it’s an implementation utilizes only a single store no matter the application size. Flux allow for many stores.

![Flux](/docs/flux-diagram-white-background.png "Flux Architecture (Source: https://github.com/facebook/flux)")

## 2.4 Sitemap Outline

### Game Lobby Page

- Game Lobby with updating list of available games. Creating a game would notify others online so that they may choose to join the game.
- Player enters the lobby after logging in.
- Lobby consists of a list of active games and players looking for games.

![Game Lobby](/docs/kot_lobby_basic_mock.jpg "To do: Add Game Lobby Mockup Image")

### Game Area Page

Features:

- Gameboard that enforces KoT rules and allows players to take turns in real-time
- Game controls provide KoT game mechanic input. Player can otherwise optionally use MUD style command based gameplay. Controls will enable/disable as game state progresses to improve user experience.
- Game log that tracks all player choices reporting live as they occur
- Players will have ability to chat with other within the game network.
- The game area will include the components highlighted on the Game Area shown below.

Component listing indicate development priority.

- Diceboard: The strip of boxes to the right of PlayerDetails changes to show the players current roll. This area will also update to show the other players roles. The player can click those dice they wish to keep or lock. Locked dice will not be rerolled. Dice will outline in red when locked. Dice still avialbe for rolling are outlined in green.

- PlayerControls: A series of buttons for performing game mechanics such as including "Roll", "Reroll", "Leave Tokyo City" and "Enter Tokyo City".

- GameConsole:  The game log showing the players interaction with the opponent’s and game responses to actions.

- PlayerDetails: Series of text areas organized in a column describing the player's current game standing stats. These include Victory (VPs), Hearts and Energy Points. Counters collected shall also be shown.

- CardStore: A row of 3 cards (CardDetails) that can be purchased by players durring their turns. Card slots will be randomly replaced after purchase.

- CardDetails: Shows cards details including name, cost, effect and footnote and card type. CardDetails appear within the CardStore representing each card available for sale.

- PlayerAbilities: A stacked series of buttons each representing a card purchased or earned by the player. Cards can be activated by clicking. Cards will be disabled or enabled when accessable given the players current turn phase.

- OpponentStatus: A column of vertically stacked areas describing the status of each player in the game and ability card details. Abilites often allow the player to interact with opponents durring a turn. Links will appear under oponents if ability options are available durring the current turn.

- MUDCommandShell: A scrollable text area with textbox for interacting with the game via MUD style text commands. Any Player Ability, Player Control or Player resources (heart, energy, claws, etc.) can be leveraged via text command or by interacting with an associated UI control.

- ChatShell: A scrollable text area with textbox for sending chat messages to other players.

### Game Landing

Note: This will probably be the last page to be developed.

Main landing page for the site. This page provides the user with access to login UI and community building mechanics such as rankings, achievments, etc.

Login will not be developed until the game lobby and gameboard is far enough along for multiplayer matchmaking to make sense.

![Game Area](/docs/kot_gameboard_basic_mock.jpg "Gameboard Wireframe")

## 4 Installation

Clone this repository

`git clone https://github.com/borisv13/kot.git`

Create a Python virtual environment.

`py -m venv env`

Activate the python virtual environment.

`.\env\Scripts\activate`

Navigate to the backend directory.

 `cd .\kot\backend\`

 Install Python dependencies.

`run pip install -r requirements.txt`

Create the local database

`python manage.py migrate`

Run webpack to build the components

`npm run webpack`

Run Django development server on port 8000

`python manage.py runserver 8000`

## License

MIT License
