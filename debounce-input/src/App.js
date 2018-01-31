import React, { Component } from "react";

class App extends Component {
  render() {
    return (
      <div className="flex items-center h-screen w-full bg-teal-lighter">
        <div className="w-full bg-white rounded shadow-lg p-8 m-4 md:max-w-sm md:mx-auto">
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
              <input
                className="border py-2 px-3 text-grey-darkest"
                name="search"
                type="text"
                id="search"
              />
            </div>
          </form>
        </div>
      </div>
    );
  }
}

export default App;
