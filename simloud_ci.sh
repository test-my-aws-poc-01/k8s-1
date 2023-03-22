#!/bin/bash

docker image build --network host  -t $DOCKER_IMAGE_NAME -f Dockerfile .
