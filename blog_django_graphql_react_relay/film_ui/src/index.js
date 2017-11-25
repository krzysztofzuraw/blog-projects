import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/css/bootstrap-theme.css";

import React from "react";
import ReactDOM from "react-dom";
import { Router, Route, Switch } from "react-router-dom";
import createHistory from "history/createBrowserHistory";
import App from "./components/App";
import Film from "./components/Film";
import registerServiceWorker from "./registerServiceWorker";

const history = createHistory();

const router = (
  <Router history={history}>
    <Switch>
      <Route exact path="/" component={App} />
      <Route path="/film/:filmId" component={Film} />
    </Switch>
  </Router>
);

ReactDOM.render(router, document.getElementById("root"));
registerServiceWorker();
