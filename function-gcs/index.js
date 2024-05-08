const {CloudEvents} = require('@google-cloud/functions-framework');

// Register a CloudEvent function with the Functions Framework
exports.helloGCS = (cloudEvent) => {
  const file = cloudEvent.data;
  console.log(`File ${file.name} was uploaded to ${file.bucket}`);
};
