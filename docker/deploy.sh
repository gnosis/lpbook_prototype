#!/bin/bash
set -euo pipefail

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_NAME" --password-stdin

echo "Tagging latest image with solver...";
docker build -t "${DOCKERHUB_PROJECT}" -f docker/Dockerfile .
docker tag "${DOCKERHUB_PROJECT}" gnosispm/"${DOCKERHUB_PROJECT}":$1
echo "Pushing image";
docker push gnosispm/"${DOCKERHUB_PROJECT}":$1

if [ "$1" == "main" ]; then
    echo "Restarting pod..."
    STATUSCODE=$(curl -s \
        --output /dev/null \
        --fail \
        --write-out "%{http_code}" \
        -H "Content-Type: application/json" \
        -u "$AUTODEPLOY_TOKEN" \
        -d '{"push_data": {"tag": "'$AUTODEPLOY_TAG'" }}' \
        -X POST \
        $AUTODEPLOY_URL)
    if test $STATUSCODE -ne 200; then
        echo "Restarting pod failed. Aborting ..."
        exit 1
    fi
fi
