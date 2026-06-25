RUNNING THE HELLO-WORLD IMAGE
docker run hello-world

RUNNING A CONTAINER IN THE BACKGROUND
docker run -d postgres

CHECKING RUNNING CONTAINERS
docker ps

UBUNTU INTERACTIVE CONTAINER
docker run -it ubuntu && exit

CREATING A CONTAINER FOR A SPECIFIC DOCKER IMAGE
docker run --name <container name> <image name>

EX.
HELPING A COLLEAGUE
docker run -d --name colleague_project my_project

FILTERING RUNNING CONTAINERS
docker ps -f "name=<running-container>

CHECKING LOGS BY CONTAINER NAME
docker logs colleague_project

CLEANING UP
1. docker stop colleague_project
2. docker container rm colleague_project

SEE ALL IMAGES
docker images

PULL A PROJECT FROM DOCKER HUB
docker pull ubuntu (Automatically pulls the latest)
docker pull ubuntu:22.04

CLEANING UP DOCKER IMAGES
docker image rm ubuntu


