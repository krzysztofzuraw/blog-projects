import React from "react";

import { shallow, mount } from "enzyme";

import App from "./App";

describe("App Component", () => {
  it("renders correctly", () => {
    const wrapper = shallow(<App />);
    expect(wrapper).toMatchSnapshot();
  });

  it("should set state when input has changed", () => {
    const wrapper = mount(<App />);
    const searchInputWrapper = wrapper.find("#search");
    searchInputWrapper.simulate("change", {
      target: { value: "Fake Name" }
    });

    setTimeout(() => {
      expect(wrapper.state().typedWords).toEqual(["Fake Name"]);
    }, 200);
  });
});
