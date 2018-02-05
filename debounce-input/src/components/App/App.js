import React, { Component } from "react";

import SearchInput from "../SearchInput/SearchInput";
import SearchResult from "../SearchResult/SearchResult";

class App extends Component {
  render() {
    return (
      <div className="flex flex-col items-center h-screen w-full bg-teal-lighter bg-repeat">
        <div className="container md:max-w-sm md:mx-auto">
          <h1 className="block w-full text-center text-grey-darkest mb-6">
            Debounce in React
          </h1>
          <SearchInput />
        </div>
        {["some", "random", "typed"].map((result, key) => (
          <SearchResult text={result} key={key} />
        ))}
      </div>
    );
  }
}

export default App;
