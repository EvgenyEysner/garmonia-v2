import js from "@eslint/js";
import pluginVue from "eslint-plugin-vue";
import tseslint from "typescript-eslint";
import eslintConfigPrettier from "eslint-config-prettier";

export default tseslint.config(
  { ignores: ["dist/**", "node_modules/**", "**/*.min.js"] },
  js.configs.recommended,
  ...tseslint.configs.recommended,
  ...pluginVue.configs["flat/recommended"],
  // .vue-Dateien: vue-eslint-parser (aus pluginVue oben) nutzt fuer die
  // <script lang="ts">-Bloecke den TypeScript-Parser.
  {
    files: ["**/*.vue"],
    languageOptions: {
      parserOptions: {
        parser: tseslint.parser,
      },
    },
  },
  // Node-Skripte / Config-Dateien laufen in der Node-Umgebung.
  {
    files: ["scripts/**/*.{js,mjs,cjs}", "*.config.{js,mjs,cjs,ts}"],
    languageOptions: {
      globals: {
        process: "readonly",
        console: "readonly",
        Buffer: "readonly",
        URL: "readonly",
      },
    },
  },
  eslintConfigPrettier,
  {
    rules: {
      "vue/multi-word-component-names": "warn",
    },
  }
);
