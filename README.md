# Generates Files in Docker

## Build Image

docker build -t <image-name> .

## Run Image

mkdir -p ./out
docker run -v $(pwd)/out:/out -it <image-name>