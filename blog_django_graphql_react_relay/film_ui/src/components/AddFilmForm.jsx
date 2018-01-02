import React, { Component } from "react";
import { FormGroup, ControlLabel, FormControl, Radio } from "react-bootstrap";

export default class AddFilmForm extends Component {
  constructor(props) {
    super(props);

    this.state = {
      title: "",
      date: "",
      rating: 0
    };
  }

  handleChange = event => {
    debugger;
    const target = event.target;
    // const value =
  };

  render() {
    return (
      <form>
        <FormGroup>
          <ControlLabel>Enter details of new film</ControlLabel>
          <FormControl
            type="text"
            // value={this.state.value}
            placeholder="Title"
            onChange={this.handleChange}
          />
        </FormGroup>
        <FormGroup>
          <ControlLabel>Enter details of new film</ControlLabel>
          <FormControl
            type="date"
            // value={this.state.value}
            placeholder="Air date"
            onChange={this.handleChange}
          />
        </FormGroup>
        <FormGroup onChange={this.handleChange}>
          <ControlLabel>Select rating</ControlLabel>
          <FormControl componentClass="select" placeholder="select">
            <option value="0">0</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
          </FormControl>
        </FormGroup>
      </form>
    );
  }
}
