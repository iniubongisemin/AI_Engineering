### RUNNING THE HELLO-WORLD IMAGE
docker run hello-world

### RUNNING A CONTAINER IN THE BACKGROUND
docker run -d postgres

### CHECKING RUNNING CONTAINERS
docker ps

### UBUNTU INTERACTIVE CONTAINER
docker run -it ubuntu && exit

### CREATING A CONTAINER FOR A SPECIFIC DOCKER IMAGE
docker run --name <container name> <image name>

### START CONTAINER WITH A NAME
docker run --name <container-name><image-name>

### FILTER RUNNING CONTAINER ON NAME
docker ps -f "name=<container-name>"

### SEE EXISTING LOGS FOR CONTAINER
docker logs <container-id>

### SEE LIVE LOGS FOR CONTAINER
docker logs -f <container-id>

### EXIT LIVE LOG VIEW OF CONTAINER
CTRL + C

### REMOVE STOPPED CONTAINER
docker container rm <container-id>

### EX.
HELPING A COLLEAGUE
docker run -d --name colleague_project my_project

### FILTERING RUNNING CONTAINERS
docker ps -f "name=<running-container>"

### CHECKING LOGS BY CONTAINER NAME
docker logs colleague_project

### CLEANING UP
1. docker stop colleague_project
2. docker container rm colleague_project

### SEE ALL IMAGES
docker images

### PULL A PROJECT FROM DOCKER HUB
docker pull ubuntu (Automatically pulls the latest)
docker pull ubuntu:22.04

### CLEANING UP DOCKER IMAGES
docker image rm ubuntu

### CLEANING UP CONTAINERS
docker container prune

### CLEANING UP IMAGES
docker image prune -a

### BUILDING AND RUNNING A DOCKER CONTAINER
docker build .
docker run test-image

### SAVE AN IMAGE
docker save -o image.tar classify_spam:v1

### PULL IMAGE FROM PRIVATE REGISTRY
docker pull <private-registry-url>/<image-name>

### NAME AN IMAGE
docker tag <old-name><new-name>

### PUSH AN IMAGE
docker image push <image-name>

### LOGIN TO PRIVATE REGISTRY
docker login <private-registry-url>

### SHARING YOUR WORK USING DOCKER REGISTRY
### TAGGING A DOCKER IMAGE BEFORE PUSHING TO DOCKER REGISTRY
docker tag <image-name> <private-registry-url>/<image-name>
docker tag spam:v1 docker.mycompany.com/spam:v1

### PUSHING TO A REGISTRY
docker image push <image name>
docker image push docker.mycompany.com/spam:v1

### SAVE IMAGE TO FILE
docker save -o <file-name><image-name>

### LOAD IMAGE FROM FILE
docker load -i <file-name>

### RECEIVING DOCKER IMAGES >> Ex.12
docker pull docker.mycompany.com/spam_alice:v3
docker run docker.mycompany.com/spam_alice:v3
>> OPEN TAR FILES
docker load -i spam_bob.tar
docker run spam_bob:v3

### BUILDING DOCKER FILES
docker build .
>> BUILDING & NAMING DOCKER FILES
docker build -t my_first_image .

### WORKING IN THE COMMANDLINE
>> CREATE AN EMPTY FILE
touch Dockerfile
nano Dockerfile
>> ADDING TEXT TO A FILE
echo "RUN apt-get update"" >> Dockerfile
>> CHECK THE CONTENTS OF A FILE
cat Dockerfile
>> BUILD & TAG AN IMAGE IN CWD
docker build -t my_app .

### CREATING YOUR OWN DOCKERFILE
touch Dockerfile
echo "FROM ubuntu" >> Dockerfile
echo "RUN apt-get update" >> Dockerfile && echo "RUN apt-get install -y python3" >> Dockerfile
docker build -t my_python_image .

### COPYING FILES INTO AN IMAGE
echo "COPY /home/repl/pipeline.py /app/pipeline.py" >> Dockerfile

### COPYING FOLDERS INTO AN IMAGE
echo "COPY /pipeline_v3/ /app/pipeline_v3/" >> Dockerfile

### BUILD THE IMAGE
docker build -t pipeline_v3 .

### WORKING WITH DOWNLOADED FILES
>> CREATE DOCKERFILE
touch Dockerfile
>> UPDATE DOCKERFILE
echo "FROM ubuntu" >> Dockerfile && echo "RUN apt-get update" >> Dockerfile && echo "RUN apt-get install -y python3 curl unzip" >> Dockerfile
>> DOWNLOAD FILES, ZIP & UNZIP
echo "RUN curl https://assets.datacamp.com/production/repositories/6082/datasets/31a5052c6a5424cbb8d939a7a6eff9311957e7d0/pipeline_final.zip -o /pipeline_final.zip && RUN unzip /pipeline_final.zip && RUN rm /pipeline_final.zip" >> Dockerfile 
>> BUILD DOCKERFILE
docker build -t pipeline .

### ADDING A CMD
echo "CMD python3 my_pipeline.py" >> Dockerfile
docker run pipeline_debug


