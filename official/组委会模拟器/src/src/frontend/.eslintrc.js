module.exports = {
  root: true,

  env: {
    browser: true,
    es2021: true,
  },

  plugins: ['prettier', 'vue'],

  extends: [
    'eslint:recommended',
    'eslint-config-prettier',
    '@vue/typescript/recommended',
    'plugin:vue/vue3-recommended',
    'plugin:prettier/recommended',
  ],

  parserOptions: {
    ecmaVersion: 2021,
    ecmaFeatures: {
      jsx: true,
    },
  },

  rules: {
    'no-undef': 'off',
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-var': 'error',
    'no-useless-return': 'error',
    'prettier/prettier': 'warn',
    'vue/require-default-prop': 'off',
  },
}
