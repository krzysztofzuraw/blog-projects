import React from "react";
import {
  Grid,
  PageHeader,
  Panel,
  ListGroup,
  ListGroupItem
} from "react-bootstrap";

import { createFragmentContainer, graphql } from "react-relay";

class Film extends React.Component {
  render() {
    return (
      <Grid>
        <PageHeader style={{ "text-align": "center" }}>Film Title</PageHeader>
        <Panel header="Air date:" bsStyle="info">
          2017-01-02
        </Panel>
        <Panel header="Rating" bsStyle="warning">
          3
        </Panel>
        <Panel header="Description" bsStyle="primary">
          Some long text
        </Panel>
        <Panel footer="Actors">
          <ListGroup>
            <ListGroupItem href="#link1">Actor one</ListGroupItem>
            <ListGroupItem href="#link2">Actor two</ListGroupItem>
          </ListGroup>
        </Panel>
      </Grid>
    );
  }
}

export default createFragmentContainer(
  Film,
  graphql`
    fragment Film_film on Film {
      id
      airDate
    }
  `
);
