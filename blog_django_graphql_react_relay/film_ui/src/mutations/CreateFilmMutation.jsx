import { commitMutation, graphql } from "react-relay";
import { ConnectionHandler } from "relay-runtime";
import environment from "../Environment";

const mutation = graphql`
  mutation CreateFilmMutation($input: CreateFilmInput!) {
    createFilm(input: $input) {
      film {
        id
        title
        rating
        airDate
        actors {
          firstName
          lastName
        }
      }
    }
  }
`;

export default function CreateFilmMutation(title, airDate, rating) {
  const variables = {
    input: {
      title,
      airDate,
      rating,
      actors: [{ actorId: "QWN0b3I6MQ==" }]
    }
  };
  commitMutation(environment, {
    mutation,
    variables,
    onCompleted: (response, errors) => {
      console.log("Response received from server.");
    },
    onError: err => console.error(err)
  });
}
