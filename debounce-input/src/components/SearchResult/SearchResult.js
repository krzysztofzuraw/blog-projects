import React from "react";

function SearchResult(props) {
  const { text } = props;
  return (
    <div className="container md:max-w-sm md:mx-auto">
      <span>{text}</span>
    </div>
  );
}

export default SearchResult;
