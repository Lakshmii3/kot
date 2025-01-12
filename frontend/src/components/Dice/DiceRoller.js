import React from 'react';
import "./DiceRoller.css";
import Button from "react-bootstrap/Button";

import * as Constants from '../../constants'

import DiceBoard from './DiceBoard'

import GameInstance from './../../services/gameService'

class DiceRoller extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      username: props.currentUser,
      gameRoom: props.currentRoom,
      rolledDice: [],
      selectedDice: [],
      allowReroll: true
    };

    this.AttemptReroll = this.AttemptReroll.bind(this);
  }

  componentDidMount() {
    // ... do something with fetchedData e.g. set the data
  }

  selectedDiceCallback = (selectedDice) => {
    this.setState({ selectedDice: selectedDice });
    // console.log('selected :', selectedDice);
    // console.log('total :', this.state.rolledDice.length);
  }

  async AttemptReroll(/*e*/) {

    try {

      this.sendSelectedDice();

      let rerollThisMany = this.CalculateRerollCount();

      let result = await this.RequestDiceRoll(rerollThisMany);

      if (result) {
        this.setState({ rolledDice: result });
      }
    } catch (exception) {
      console.log(exception);
    }
  }

  sendSelectedDice() {

    let selected = this.state.rolledDice;

    if (selected && selected.length > 0) {
      const messageObject = {
        from: this.props.currentUser,
        data: selected
      };

      GameInstance.sendSelectedDice(messageObject);
      this.setState({
        message: ''
      })
    }
  }

  CalculateRerollCount() {
    if (this.state && this.state.selectedDice && this.state.rolledDice) {
      let keptDice = this.state.selectedDice.length;
      let totalDice = this.state.rolledDice.length;
      let reroll = totalDice - keptDice;
      if (reroll)
        return reroll;
    }

    return 0;
  }

  async RequestDiceRoll(rerollThisMany) {
    try {

      // TO DO: Provide rerollThisMany to server request

      const res = await fetch(Constants.REST_ENDPOINT_DICE);
      const json_data = await res.json();

      var result = [];

      result.push([json_data.dice1, json_data.dice1_selected]);
      result.push([json_data.dice2, json_data.dice2_selected]);
      result.push([json_data.dice3, json_data.dice3_selected]);
      result.push([json_data.dice4, json_data.dice4_selected]);
      result.push([json_data.dice5, json_data.dice5_selected]);
      result.push([json_data.dice6, json_data.dice6_selected]);

      this.state.allowReroll = json_data.allowReroll;

      return result;
    } catch (err) {
      console.log(err);
    }
  }

  render() {
    return (
      <div className="DiceRoller">
        <DiceBoard ref={this.textInput} callbackSendDiceSelectionOut={this.selectedDiceCallback} data={this.state.rolledDice} currentUser={this.state.username} currentRoom={this.state.gameRoom} />
        <Button className="btn btn-secondary" disabled={!this.state.allowReroll} onClick={this.AttemptReroll}>Roll</Button>
      </div>
    )
  }
}

export default DiceRoller;