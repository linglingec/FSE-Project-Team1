# FSE-Project-Team1

Download `Dockerfile` from this repository and [ubuntu image](https://hub.docker.com/_/ubuntu) on your computer. In terminal run the following code to create a docker image.

```commandline
docker build -t fse1 -f Dockerfile .
```

Run image

```commandline
docker run -it fse1
```

Run the following code to transform `57°` to radians

```commandline
./deg2rad.exe 57
```

To test the programm run 

```commandline
./test.sh
```
