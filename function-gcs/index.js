const {CloudEventFunction} = require('@google-cloud/functions-framework');

// Register a CloudEvent function with the Functions Framework
CloudEventFunction('helloGCS', cloudEvent => {
  const file = cloudEvent.data;
  console.log(`File ${file.name} was uploaded to ${file.bucket}`);
});