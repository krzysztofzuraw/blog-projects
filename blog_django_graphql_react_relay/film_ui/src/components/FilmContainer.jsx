import React, { Component } from "react";
import { QueryRenderer, graphql } from "react-relay";
import environment from "../Environment";

import Film from "./Film.jsx";

const FilmQuery = graphql`
  query FilmContainerQuery($filmID: ID!) {
    film(id: $filmID) {
      airDate
      title
      rating
      actors {
        id
        firstName
        lastName
      }
    }
  }
`;

export default class FilmContainer extends Component {
  render() {
    return (
      <QueryRenderer
        environment={environment}
        query={FilmQuery}
        variables={{
          filmID: this.props.match.params.filmId
        }}
        render={({ error, props }) => {
          if (error) {
            return <div>{error.message}</div>;
          } else if (props) {
            return <Film film={props.film} />;
          }
          return <div>Loading</div>;
        }}
      />
    );
  }
}
