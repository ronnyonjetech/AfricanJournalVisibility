const { fontFamily } = require(`tailwindcss/defaultTheme`)
const colors = require('tailwindcss/colors')

module.exports = {
  content: [
    // ...
    'node_modules/flowbite-react/lib/esm/**/*.js'
],

  // content: ['./src/**/*.{js,html,ts,tsx, jsx}',  "./node_modules/flowbite/**/*.js", 'node_modules/flowbite-react/lib/esm/**/*.js'
  // ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Fira Sans', ...fontFamily.sans],
      },
      typography: (theme) => ({
        DEFAULT: {
          css: {
            a: {
              color: theme('colors.current'),
            },
          },
        },
      }),
    },
    colors: {
      inherit: 'inherit',
      transparent: 'transparent',
      current: 'currentColor',
      black: '#000000',
      white: '#ffffff',
      gray: colors.slate,
      primary: colors.indigo,
      secondary: colors.rose,
      tertiary: colors.emerald,
    },
  },
  // plugins: [require('@tailwindcss/forms'), require('@tailwindcss/typography'), require('flowbite/plugin')],
  plugins: [require('flowbite/plugin')],
}

module.exports = {
  content: [
    './src/**/*.{js,jsx,ts,tsx}',
    'node_modules/flowbite-react/lib/esm/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}