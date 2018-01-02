import React from "react";
import { Button, ListGroup, ListGroupItem } from "react-bootstrap";
import { createFragmentContainer, graphql } from "react-relay";
import { Link } from "react-router-dom";

import AddFilmForm from "./AddFilmForm";

const wellStyles = { maxWidth: 400, margin: "0 auto 10px" };

class FilmList extends React.Component {
  render() {
    return (
      <div>
        <div className="well" style={wellStyles}>
          <ListGroup>
            {this.props.films.map(film => (
              <ListGroupItem key={film.id}>
                <Link to={`film/${film.id}`}>{film.title}</Link>
              </ListGroupItem>
            ))}
          </ListGroup>
        </div>
        <div className="well" style={wellStyles}>
          <AddFilmForm />
        </div>
      </div>
    );
  }
}

export default createFragmentContainer(FilmList, {
  films: graphql`
    fragment FilmList_films on Film @relay(plural: true) {
      id
      title
    }
  `
});
