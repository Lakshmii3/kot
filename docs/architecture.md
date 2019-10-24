# Software Architecture for King of Tokyo
## 1. Introduction
The main motivation behind documenting the architecture is to ensure the team is making good design decisions guided by separation of concerns and overall high cohesion in terms of designing the game. 

## 2. System Context
The major systems that comprise KOT are as folllows:
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
Channels is a project that takes Django and extends its abilities beyond HTTP - to handle WebSockets, chat protocols. It’s built on a Python specification called ASGI.(Asynchronous Server Gateway Interface)
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
#### To do

The websites frontend infrastructure will leverage React and [Flux](https://github.com/facebook/flux "Facebook Flux on GitHub") application architecture. Flux was developed to utilize a unidirectional data flow in React. 

The UI team has not yet completely decided which architectural data and state management approach to utilize. We intend to investigating Redux and Facebooks more recent Flux implementation. Redux differs from Flux since it’s an implementation utilizes only a single store no matter the application size. Flux allow for many stores.

![Flux](https://github.com/facebook/flux/blob/master/img/flux-diagram-white-background.png)





