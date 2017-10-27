import React, { Component } from "react";
import { PageHeader } from "react-bootstrap";

import FilmList from "./FilmList";

class App extends Component {
  render() {
    return (
      <div>
        <PageHeader style={{ "text-align": "center" }}>
          Films database
        </PageHeader>
        <FilmList />
      </div>
    );
  }
}

export default App;
