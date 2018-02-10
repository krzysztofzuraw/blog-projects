import React, { Component } from "react";

class SearchInput extends Component {
  render() {
    const { handleChange } = this.props;
    return (
      <form className="mb-4" onChange={handleChange}>
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
    );
  }
}

export default SearchInput;
