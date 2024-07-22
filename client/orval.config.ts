import { defineConfig } from "orval";

export default defineConfig({
  main: {
    input: "../api.yml",
    output: {
      target: "./src/shared/api/generated",
      schemas: "./src/shared/api/generated/model",
      prettier: true,
      client: "react-query",
      mode: "tags",
      override: {
        query: {
          useSuspenseQuery: true,
        },
        mutator: {
          path: "./src/shared/api/instance.ts",
          name: "apiInstance",
        },
      },
    },
  },
});
