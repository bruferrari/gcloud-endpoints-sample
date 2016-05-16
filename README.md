# gcloud-endpoints-sample
Example of an application with Google Cloud Endpoints, Google Cloud Datastore and Python

This sample makes use of [proto-datastore](https://github.com/GoogleCloudPlatform/endpoints-proto-datastore) that's a library intended
to be used with Python and Google Cloud Endpoints, if you'd like to know more about proto-datastore please check out the link above.

# Project setup and running
* Make sure you have Python 2.7.x installed.
* To run this project you'll need Google App Engine SDK pre-installed and properly configured in your local environment.
* Configure the application property on app.yaml file with your app engine application id.
* Deploy your application on your app engine environment.
* Go to http://localhost:8080/_ah/api/explorer to access api resources.
* Go to http://localhost:8000/ to access to your Google Cloud Datastore manager.
