/**
 * @flow
 * @relayHash f4ba014786b760c5e7ba308f31ac22ae
 */

/* eslint-disable */

'use strict';

/*::
import type {ConcreteBatch} from 'relay-runtime';
export type AppQueryResponse = {|
  +films: ?$ReadOnlyArray<?{| |}>;
|};
*/


/*
query AppQuery {
  films {
    ...FilmList_films
    id
  }
}

fragment FilmList_films on Film {
  id
  title
}
*/

const batch /*: ConcreteBatch*/ = {
  "fragment": {
    "argumentDefinitions": [],
    "kind": "Fragment",
    "metadata": null,
    "name": "AppQuery",
    "selections": [
      {
        "kind": "LinkedField",
        "alias": null,
        "args": null,
        "concreteType": "Film",
        "name": "films",
        "plural": true,
        "selections": [
          {
            "kind": "FragmentSpread",
            "name": "FilmList_films",
            "args": null
          }
        ],
        "storageKey": null
      }
    ],
    "type": "Query"
  },
  "id": null,
  "kind": "Batch",
  "metadata": {},
  "name": "AppQuery",
  "query": {
    "argumentDefinitions": [],
    "kind": "Root",
    "name": "AppQuery",
    "operation": "query",
    "selections": [
      {
        "kind": "LinkedField",
        "alias": null,
        "args": null,
        "concreteType": "Film",
        "name": "films",
        "plural": true,
        "selections": [
          {
            "kind": "ScalarField",
            "alias": null,
            "args": null,
            "name": "id",
            "storageKey": null
          },
          {
            "kind": "InlineFragment",
            "type": "Film",
            "selections": [
              {
                "kind": "ScalarField",
                "alias": null,
                "args": null,
                "name": "title",
                "storageKey": null
              }
            ]
          }
        ],
        "storageKey": null
      }
    ]
  },
  "text": "query AppQuery {\n  films {\n    ...FilmList_films\n    id\n  }\n}\n\nfragment FilmList_films on Film {\n  id\n  title\n}\n"
};

module.exports = batch;
