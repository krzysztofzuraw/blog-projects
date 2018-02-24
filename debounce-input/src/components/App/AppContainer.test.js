import React from "react";

import { mount } from "enzyme";

import { AppContainer } from "./AppContainer";

function setup() {
  const props = {
    addWord: jest.fn(),
    words: []
  };

  const enzymeWrapper = mount(<AppContainer {...props} />);

  return {
    props,
    enzymeWrapper
  };
}

describe("AppContainer", () => {
  it("should set state when input has changed", () => {
    const { enzymeWrapper, props } = setup();
    const searchInputWrapper = enzymeWrapper.find("#search");
    searchInputWrapper.simulate("change", {
      target: { value: "Fake Name" }
    });

    setTimeout(() => {
      expect(props.addWord.mock.calls.length).toBe(1);
      expect(props.addWord.mock.calls[0]).toEqual(["Fake Name"]);
    }, 200);
  });
});
