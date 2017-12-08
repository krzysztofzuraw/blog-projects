import React from "react";
import {
  Grid,
  PageHeader,
  Panel,
  ListGroup,
  ListGroupItem
} from "react-bootstrap";

export default class Film extends React.Component {
  render() {
    const { airDate, title, rating, actors } = this.props.film;
    debugger;
    return (
      <Grid>
        <PageHeader style={{ "text-align": "center" }}>{title}</PageHeader>
        <Panel header="Air date:" bsStyle="info">
          {airDate}
        </Panel>
        <Panel header="Rating" bsStyle="warning">
          {rating}
        </Panel>
        <Panel header="Description" bsStyle="primary">
          Some long text
        </Panel>
        <Panel footer="Actors">
          <ListGroup>
            {actors.map(actor => (
              <ListGroupItem key={actor.id} href="#link1">
                {actor.firstName} {actor.lastName}
              </ListGroupItem>
            ))}
          </ListGroup>
        </Panel>
      </Grid>
    );
  }
}
