import React, { Component } from 'react';
import "./Gameboard.css";

import GameConsole from '../components/GameConsole/GameConsole'
import DiceRoller from './../components/Dice/DiceRoller'

import GameInstance from './../services/gameService'

export default class GameboardLayout extends Component {

    constructor(props) {
        super(props);

        let userName = 'Guest_1234';
        let roomName = 'Room_1234';
        if (props.location && props.location.state) {
            userName = userName;
            roomName = roomName;
        }

        this.state = {
            username: userName,
            gameRoom: roomName,
            loggedIn: true
        };

        GameInstance.connect(this.state.gameRoom);
    }

    render() {
        return (
            <div>
                <br />
                <h4>{this.state.gameRoom}</h4>
                <div className="container">
                    {
                        this.state.loggedIn ?
                            <div className="row">
                                <div className="col-sm">
                                    <DiceRoller currentUser={this.state.username} currentRoom={this.state.gameRoom} />
                                </div>
                                <div className="col-sm">
                                    <GameConsole />
                                </div>
                                <div className="col-sm">
                                    <p>Chatroom Placeholder</p>
                                </div>
                            </div>
                            :
                            <p>Please login</p>
                    }
                </div>
            </div>
        );
    }
}
