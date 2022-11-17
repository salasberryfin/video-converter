#!/bin/bash

HUB_REPO_NAME="salasberryfin/video-converter"
IMAGE_NAME="python-video-converter-api"
VERSION="test"

echo "Creating Docker image from Dockerfile"
docker build . -t ${IMAGE_NAME}

echo "Tagging image ${IMAGE_NAME} as ${HUB_REPO_NAME}:${VERSION}"
docker tag ${IMAGE_NAME}:latest ${HUB_REPO_NAME}:${VERSION}
echo "Pushing image ${HUB_REPO_NAME}:${VERSION} to Docker Hub"
docker image push ${HUB_REPO_NAME}:${VERSION}
