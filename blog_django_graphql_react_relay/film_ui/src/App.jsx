import React, { Component } from "react";
import { Row, Col, Tab, Nav, NavItem, PageHeader } from "react-bootstrap";

class App extends Component {
  render() {
    return (
      <div>
        <PageHeader>Films database</PageHeader>
        <Tab.Container id="left-tabs-example" defaultActiveKey="first">
          <Row className="clearfix">
            <Col sm={4}>
              <Nav bsStyle="pills" stacked>
                <NavItem eventKey="first">Pulp Fiction</NavItem>
                <NavItem eventKey="second">Django</NavItem>
              </Nav>
            </Col>
            <Col sm={8}>
              <Tab.Content animation>
                <Tab.Pane eventKey="first">Pulp Fiction content</Tab.Pane>
                <Tab.Pane eventKey="second">Django content</Tab.Pane>
              </Tab.Content>
            </Col>
          </Row>
        </Tab.Container>
      </div>
    );
  }
}

export default App;
