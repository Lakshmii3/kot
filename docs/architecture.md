# Software Architecture for King of Tokyo
## 1. Introduction
The main motivation behind documenting the architecture is to ensure the team is making good design decisions guided by separation of concerns and overall high cohesion in terms of designing the game. 

## 2. System Context
The major systems that comprise KOT are as folllows:
- Django backend for routing and providing a RESTful API
- MySQL database for storing player and game session data
- Django channels for asynchronous Websocket communication
- React frontend for the user interface  

#### To do: Figure 1 should map out the basic systems involved with KOT and how they interact with each other. 

## 2.1 Backend
### Vanilla Django 
 Django is built around the simple concept of requests and responses: the browser makes a request, Django calls a view, which returns a response that’s sent back to the browser. 

![Vanilla](https://i.imgur.com/1HzpGJe.png_)

### Django Channels
Django Channels supports WebSockets which is a protocol that provides full-duplex communication — a persistent, open connection between the client and the server, with either able to send data at any time.

Channels also allow for background tasks that run on the same servers as the rest of Django. HTTP requests continue to behave the same as before, but also get routed over channels

Channels are essentially task queues: messages get pushed onto the channel by producers, and then given to one of the consumers listening on that channel. 
Channels is designed to use Redis as its preferred channel layer, though there is support for other types (and a first-class API for creating custom channel layers). Documentation: 

![Django with Channels](https://i.imgur.com/Ds5TcD3.png)

## 2.2 Midtier
#### To do

## 2.3 Frontend
#### To do



