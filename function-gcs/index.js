const {CloudEvents} = require('@google-cloud/functions-framework');

// Register a CloudEvent function with the Functions Framework
exports.helloGCS = (cloudEvent) => {
  console.log("Cloud EVent:", cloudEvent);
  console.log(`File ${cloudEvent.name} was uploaded to ${cloudEvent.bucket}`);
};
