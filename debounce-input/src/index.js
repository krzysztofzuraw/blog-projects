import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import "./index.css";
import AppContainer from "./components/App/AppContainer";
import registerServiceWorker from "./registerServiceWorker";

import store from "./store";

const root = (
  <Provider store={store}>
    <AppContainer />
  </Provider>
);

ReactDOM.render(root, document.getElementById("root"));
registerServiceWorker();
