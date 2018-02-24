import { combineReducers } from "redux";

import { ADD_WORD } from "../actions/index";

export const words = (state = [], action) => {
  switch (action.type) {
    case ADD_WORD:
      return [action.word, ...state];
    default:
      return state;
  }
};

const rootReducer = combineReducers({ words });
export default rootReducer;
