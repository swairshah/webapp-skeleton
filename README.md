To use complicated js dependencies use npm and webpack 

1. `npm init`

2. `npm install --save-dev webpack webpack-cli`

3. Add `webpack.config.js`

```
const path = require('path');

module.exports = {
    entry: './src/index.js', // Your main JavaScript file
           output: {
    filename: 'bundle.js', // Output bundle file
              path: path.resolve(__dirname, 'dist'), // Output directory
           },
    mode: 'development', // or 'production'
};
```

4. Add `"build": "webpack"` to `"script"` in `package.json`

5. `npm run build`
