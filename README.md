# FSE-Project-Team1

# 0 Project description
This repository provides an implementation of the function `deg2rad` that converts the degree value into radians via the formula:
$\ 1 \ degree \ = \pi/180 \ radian$.

# 1 Installation
You can use our programm either on your computer (follow the guide 1.1) or on a docker image (follow the guide 1.2)

## 1.1 Installation on your computer

Clone the repository

```commandline
git clone https://github.com/linglingec/FSE-Project-Team1
```

Enter repository folder

```commandline
cd FSE-Project-Team1
```

Make `.sh` files executable

```
chmod +x build.sh test.sh
```

Run `build.sh` to compile the program. `deg2rad.exe` should appear in the folder. 

```commandline
./build.sh
```

## 1.2 Launching docker 

Download `Dockerfile` from this repository and [ubuntu image](https://hub.docker.com/_/ubuntu) on your computer. In terminal run the following code to create a docker image.

```commandline
docker build -t fse1 -f Dockerfile .
```

Run the image

```commandline
docker run -it fse1
```

# 2 Usage

Run the following code to transform `57°` to radians

```commandline
./deg2rad.exe 57
```

# 3 Testing

To test the programm run 

```commandline
./test.sh
```
