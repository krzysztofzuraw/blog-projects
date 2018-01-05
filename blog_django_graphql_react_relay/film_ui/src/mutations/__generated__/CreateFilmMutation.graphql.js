/**
 * @flow
 * @relayHash e0e74363c78e919aa9e3f511dd8a98f5
 */

/* eslint-disable */

'use strict';

/*::
import type {ConcreteBatch} from 'relay-runtime';
export type CreateFilmMutationVariables = {|
  input: {
    title: string;
    actors?: ?$ReadOnlyArray<?{
      actorId: string;
    }>;
    airDate: any;
    rating: number;
    clientMutationId?: ?string;
  };
|};
export type CreateFilmMutationResponse = {|
  +createFilm: ?{|
    +film: ?{|
      +id: string;
      +title: ?string;
      +rating: ?number;
      +airDate: ?any;
      +actors: ?$ReadOnlyArray<?{|
        +firstName: ?string;
        +lastName: ?string;
      |}>;
    |};
  |};
|};
*/


/*
mutation CreateFilmMutation(
  $input: CreateFilmInput!
) {
  createFilm(input: $input) {
    film {
      id
      title
      rating
      airDate
      actors {
        firstName
        lastName
        id
      }
    }
  }
}
*/

const batch /*: ConcreteBatch*/ = {
  "fragment": {
    "argumentDefinitions": [
      {
        "kind": "LocalArgument",
        "name": "input",
        "type": "CreateFilmInput!",
        "defaultValue": null
      }
    ],
    "kind": "Fragment",
    "metadata": null,
    "name": "CreateFilmMutation",
    "selections": [
      {
        "kind": "LinkedField",
        "alias": null,
        "args": [
          {
            "kind": "Variable",
            "name": "input",
            "variableName": "input",
            "type": "CreateFilmInput!"
          }
        ],
        "concreteType": "CreateFilmPayload",
        "name": "createFilm",
        "plural": false,
        "selections": [
          {
            "kind": "LinkedField",
            "alias": null,
            "args": null,
            "concreteType": "Film",
            "name": "film",
            "plural": false,
            "selections": [
              {
                "kind": "ScalarField",
                "alias": null,
                "args": null,
                "name": "id",
                "storageKey": null
              },
              {
                "kind": "ScalarField",
                "alias": null,
                "args": null,
                "name": "title",
                "storageKey": null
              },
              {
                "kind": "ScalarField",
                "alias": null,
                "args": null,
                "name": "rating",
                "storageKey": null
              },
              {
                "kind": "ScalarField",
                "alias": null,
                "args": null,
                "name": "airDate",
                "storageKey": null
              },
              {
                "kind": "LinkedField",
                "alias": null,
                "args": null,
                "concreteType": "Actor",
                "name": "actors",
                "plural": true,
                "selections": [
                  {
                    "kind": "ScalarField",
                    "alias": null,
                    "args": null,
                    "name": "firstName",
                    "storageKey": null
                  },
                  {
                    "kind": "ScalarField",
                    "alias": null,
                    "args": null,
                    "name": "lastName",
                    "storageKey": null
                  }
                ],
                "storageKey": null
              }
            ],
            "storageKey": null
          }
        ],
        "storageKey": null
      }
    ],
    "type": "Mutation"
  },
  "id": null,
  "kind": "Batch",
  "metadata": {},
  "name": "CreateFilmMutation",
  "query": {
    "argumentDefinitions": [
      {
        "kind": "LocalArgument",
        "name": "input",
        "type": "CreateFilmInput!",
        "defaultValue": null
      }
    ],
    "kind": "Root",
    "name": "CreateFilmMutation",
    "operation": "mutation",
    "selections": [
      {
        "kind": "LinkedField",
        "alias": null,
        "args": [
          {
            "kind": "Variable",
            "name": "input",
            "variableName": "input",
            "type": "CreateFilmInput!"
          }
        ],
        "concreteType": "CreateFilmPayload",
        "name": "createFilm",
        "plural": false,
        "selections": [
          {
            "kind": "LinkedField",
            "alias": null,
            "args": null,
            "concreteType": "Film",
            "name": "film",
            "plural": false,
            "selections": [
              {
                "kind": "ScalarField",
                "alias": null,
                "args": null,
                "name": "id",
                "storageKey": null
              },
              {
                "kind": "ScalarField",
                "alias": null,
                "args": null,
                "name": "title",
                "storageKey": null
              },
              {
                "kind": "ScalarField",
                "alias": null,
                "args": null,
                "name": "rating",
                "storageKey": null
              },
              {
                "kind": "ScalarField",
                "alias": null,
                "args": null,
                "name": "airDate",
                "storageKey": null
              },
              {
                "kind": "LinkedField",
                "alias": null,
                "args": null,
                "concreteType": "Actor",
                "name": "actors",
                "plural": true,
                "selections": [
                  {
                    "kind": "ScalarField",
                    "alias": null,
                    "args": null,
                    "name": "firstName",
                    "storageKey": null
                  },
                  {
                    "kind": "ScalarField",
                    "alias": null,
                    "args": null,
                    "name": "lastName",
                    "storageKey": null
                  },
                  {
                    "kind": "ScalarField",
                    "alias": null,
                    "args": null,
                    "name": "id",
                    "storageKey": null
                  }
                ],
                "storageKey": null
              }
            ],
            "storageKey": null
          }
        ],
        "storageKey": null
      }
    ]
  },
  "text": "mutation CreateFilmMutation(\n  $input: CreateFilmInput!\n) {\n  createFilm(input: $input) {\n    film {\n      id\n      title\n      rating\n      airDate\n      actors {\n        firstName\n        lastName\n        id\n      }\n    }\n  }\n}\n"
};

module.exports = batch;
