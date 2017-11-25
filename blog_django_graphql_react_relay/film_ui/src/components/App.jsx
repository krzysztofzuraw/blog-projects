import React, { Component } from "react";
import { PageHeader } from "react-bootstrap";
import { QueryRenderer, graphql } from "react-relay";
import environment from "../Enviroment";

import FilmList from "./FilmList";

const FilmListQuery = graphql`
  query AppQuery {
    films {
      id
      title
    }
  }
`;

class App extends Component {
  render() {
    return (
      <QueryRenderer
        environment={environment}
        query={FilmListQuery}
        render={({ error, props }) => {
          if (error) {
            return <div>{error.message}</div>;
          } else if (props) {
            return <FilmList films={props.films} />;
          }
          return <div>Loading</div>;
        }}
      />
    );
  }
}

export default App;
