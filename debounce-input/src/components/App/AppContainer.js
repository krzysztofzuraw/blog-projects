import React from "react";
import { connect } from "react-redux";

import { addWord } from "../../actions/index";

import App from "./App";

export const AppContainer = props => (
  <App addWord={props.addWord} words={props.words} />
);

const mapDispatchToProps = dispatch => ({
  addWord: word => dispatch(addWord(word))
});

const mapStateToProps = state => ({
  words: state.words
});

export default connect(mapStateToProps, mapDispatchToProps)(AppContainer);
