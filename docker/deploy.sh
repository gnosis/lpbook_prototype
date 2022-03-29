#!/bin/bash
set -euo pipefail

# Get login token and execute login
sudo pip install awscli
$(aws ecr get-login --no-include-email --region $AWS_REGION)

echo "Tagging latest image with solver...";
docker build --tag $REGISTRY_URI:$1 -f docker/Dockerfile .
echo "Pushing image";
docker push $REGISTRY_URI:$1

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
