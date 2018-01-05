import React, { Component } from "react";
import { FormGroup, ControlLabel, FormControl } from "react-bootstrap";

import CreateFilmMutation from "../mutations/CreateFilmMutation";

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
    const target = event.target;
    const name = target.name;
    const value =
      target.type === "select-one" ? parseInt(target.value, 10) : target.value;
    this.setState({
      [name]: value
    });
  };

  handleSubmit = () => {
    CreateFilmMutation(this.state.title, this.state.date, this.state.rating);
  };

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <FormGroup>
          <ControlLabel>Enter details of new film</ControlLabel>
          <FormControl
            type="text"
            name="title"
            value={this.state.title}
            placeholder="Title"
            onChange={this.handleChange}
          />
        </FormGroup>
        <FormGroup>
          <ControlLabel>Enter details of new film</ControlLabel>
          <FormControl
            type="date"
            name="date"
            value={this.state.date}
            placeholder="Air date"
            onChange={this.handleChange}
          />
        </FormGroup>
        <FormGroup onChange={this.handleChange}>
          <ControlLabel>Select rating</ControlLabel>
          <FormControl
            componentClass="select"
            placeholder="select"
            name="rating"
          >
            <option value="0">0</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
          </FormControl>
        </FormGroup>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}
