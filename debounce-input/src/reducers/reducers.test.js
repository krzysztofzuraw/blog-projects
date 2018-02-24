import { words } from "./index";
import { ADD_WORD } from "../actions/index";

describe("Words reducer", () => {
  it("should return initial state", () => {
    expect(words(undefined, {})).toEqual([]);
  });

  it("should handle ADD_WORD on initial state", () => {
    expect(words([], { type: ADD_WORD, word: "tom" })).toEqual(["tom"]);
  });

  it("should handle ADD_WORD on existing state", () => {
    expect(words(["tim"], { type: ADD_WORD, word: "tom" })).toEqual([
      "tom",
      "tim"
    ]);
  });
});
