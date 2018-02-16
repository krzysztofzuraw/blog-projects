import React from "react";

import { shallow } from "enzyme";

import SearchInput from "./SearchInput";

describe("SearchInput Component", () => {
  it("renders correctly", () => {
    const wrapper = shallow(<SearchInput />);
    expect(wrapper).toMatchSnapshot();
  });
});
