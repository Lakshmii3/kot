import React from 'react';
import "./Lobby.css";
import Button from 'react-bootstrap/Button';

const LobbyLayout = (props) => {
    return (
        <div className="container">
            <div className="row">
                <div className="col-sm">
                    <Button onClick={""}>Create Game</Button>
                </div>
                <div className="col-sm">
                    <Button onClick={""}>Join Game</Button>
                </div>
            </div>
        </div>
    );
}

export default LobbyLayout;
