import React from "react";
import { Button } from "react-bootstrap";
import { createFragmentContainer, graphql } from "react-relay";

const wellStyles = { maxWidth: 400, margin: "0 auto 10px" };

class FilmList extends React.Component {
  // handleClick = filmId => {
  //   this.props.history.push(`film/${filmId}`);
  // };

  render() {
    return (
      <div className="well" style={wellStyles}>
        {this.props.films.map(film => (
          <Button
            key={film.id}
            bsSize="large"
            block
            // onClick={() => this.handleClick(film.id)}
          >
            {film.title}
          </Button>
        ))}
      </div>
    );
  }
}

export default createFragmentContainer(FilmList, {
  films: graphql`
    fragment FilmList_films on Film @relay(plural: true) {
      title
    }
  `
});
