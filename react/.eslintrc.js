module.exports = {
  parser: "babel-eslint",
  env: {
    browser: true,
    commonjs: true,
    es6: true,
    node: true,
    jest: true,
  },
  parserOptions: {
    ecmaVersion: 2020,
    ecmaFeatures: {
      impliedStrict: true,
      jsx: true,
    },
    sourceType: "module",
  },
  plugins: ["react", "react-hooks", "jest"],
  extends: [
    "eslint:recommended",
    "plugin:react/recommended",
    "plugin:react-hooks/recommended",
    "plugin:jest/recommended"
  ],
  settings: {
    react: {
      version: "detect",
    },
  },
  rules: {},
};
