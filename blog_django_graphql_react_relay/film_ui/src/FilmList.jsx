import React from "react";
import { Button } from "react-bootstrap";
import { withRouter } from "react-router-dom";

const filmList = ["Pulp Fiction", "Django"];

const wellStyles = { maxWidth: 400, margin: "0 auto 10px" };

class FilmList extends React.Component {
  handleClick = filmId => {
    this.props.history.push(`film/${filmId}`);
  };

  render() {
    return (
      <div className="well" style={wellStyles}>
        {filmList.map(key => (
          <Button
            key={key}
            bsSize="large"
            block
            onClick={() => this.handleClick(key)}
          >
            {key}
          </Button>
        ))}
      </div>
    );
  }
}

export default withRouter(FilmList);
