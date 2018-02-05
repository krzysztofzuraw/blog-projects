import React, { Component } from "react";

class App extends Component {
  render() {
    return (
      <div className="flex flex-col items-center h-screen w-full bg-teal-lighter bg-repeat">
        <div className="container md:max-w-sm md:mx-auto">
          <h1 className="block w-full text-center text-grey-darkest mb-6">
            Debounce in React
          </h1>
          <form className="mb-4">
            <div className="flex flex-col mb-4 md:w-full">
              <label
                className="mb-2 uppercase font-bold text-lg text-grey-darkest"
                htmlFor="search-input"
              >
                Search input:
              </label>
              <input className="field" name="search" type="text" id="search" />
            </div>
          </form>
        </div>
        <div className="container md:max-w-sm md:mx-auto">
          <span>Your typed characters</span>
        </div>
      </div>
    );
  }
}

export default App;
