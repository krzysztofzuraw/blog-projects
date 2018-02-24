import { ADD_WORD, addWord } from "./index";

describe("Actions", () => {
  it("should create action to add word", () => {
    const expectedAction = {
      type: ADD_WORD,
      word: "fake"
    };

    expect(addWord("fake")).toEqual(expectedAction);
  });
});
