import React, { Component } from "react";
import debounce from "lodash.debounce";

import SearchInput from "../SearchInput/SearchInput";
import SearchResult from "../SearchResult/SearchResult";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { typedWords: [] };

    this.emitChangeDebounced = debounce(this.emitChange, 250);
  }

  componentWillUnmount() {
    this.emitChangeDebounced.cancel();
  }

  handleChange = event => {
    this.emitChangeDebounced(event);
  };

  emitChange = value => {
    if (value !== "") {
      let typedWords = [...this.state.typedWords, value];
      this.setState({ typedWords });
    }
  };

  render() {
    return (
      <div className="flex flex-col items-center min-h-screen w-full bg-teal-lighter bg-repeat">
        <div className="container md:max-w-sm md:mx-auto">
          <h1 className="block w-full text-center text-grey-darkest mb-6">
            Debounce in React
          </h1>
          <SearchInput handleChange={this.handleChange} />
        </div>
        {this.state.typedWords.map((word, key) => (
          <SearchResult text={word} key={key} />
        ))}
      </div>
    );
  }
}

export default App;
