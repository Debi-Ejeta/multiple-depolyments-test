const {HttpFunction} = require('@google-cloud/functions-framework');

// Register an HTTP function with the Functions Framework
HttpFunction('helloHttp', (req, res) => {
  res.send('Hello from Google Cloud Functions!');
});