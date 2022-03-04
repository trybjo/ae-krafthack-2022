# Deploy

## Azure Functions
Azure functions can be a efficient way to deploy models for inferencing without having to set up a container based API in a web app or kubernetes cluster.
Remember to add ```local.settings.json``` to ```.gitignore``` after setting up the project to avoid comitting local variables.
The azure_function_app folder contains templates suited for either batch inferencing using blob triggers, http requests or timer trigger.
Other suitable triggers could be events from EventHub or EventGrid.

## Azure ML