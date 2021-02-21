# Smalls - The web client guide

## Project structure:
  /public\
    - index.html -- html served with all the react / js bundle\
    - robots.txt -- For google indexation purposes- really not neccesary\
  /src\
    /App\
    -- App.js\
    -- App.test.js\
    -- App.scss\
    /Posts :: The only domain the app will have\
      // All code in here\
    -- index.js -- Entry point to the app\
    -- index.scss -- Entry point to the mixins, normalize\
    -- normalize.scss\
    -- reset.scss\
    -- setupTests.js\
    -- variable.scss\
  .gitignore\
  .package.json\
  .package.lock.json\


- *index.html*
HTML served with all the react / js bundle 
- robots.txt -- For google indexation purposes- really not neccesary

- *App.js*
Main component

- */Posts*
The only domain the app will have
All code in here

- *index.js*
Entry point to the app's source code 

- *index.scss*
Entry point for all the styling relatied stuffs -the mixins, variables, normalize, reset-

- *normalize.scss*
- *reset.scss*
- *variable.scss*

- *setupTests.js*
Some default basic testing configuration.
 
- *.gitignore*
- *package.json*
- *package.lock.json*


# Create React App default guide
## Available Scripts
### `npm start`

**Note: From here not project specific** 

Builds the app for production to the `build` folder.\
See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
