name: Docker Image CI

on:
  push:
    branches: [ "Master" ]
  pull_request:
    branches: [ "Master" ]

jobs:

  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Build the Docker image
      run: docker build . --file Dockerfile --tag my-image-name:$(date +%s)