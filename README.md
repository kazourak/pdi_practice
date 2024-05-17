# pdi_practice
Few exercises to practice using Pentaho Data Integration (PDI). These exercises range from basic to more advanced tasks.

## Pentaho installation
- Install `libwebkitgtk-10-0`
```bash
sudo nano /etc/apt/sources.list
deb http://cz.archive.ubuntu.com/ubuntu bionic main universe
sudo apt-get update
sudo apt-get install libwebkitgtk-1.0-0
```
- Update Ubuntu and install dependencies
```bash
sudo apt-get update && \
sudo apt-get -y upgrade  && \
sudo apt-get -y install jq curl wget apt-transport-https ca-certificates gnupg software-properties-common && \
sudo apt-get -y install openjdk-21-jdk maven && \
sudo apt-get -y install libcanberra-gtk-module libcanberra-gtk3-module && \
sudo apt-get -y autoremove
```

- Download Pentaho https://drive.google.com/file/d/13z0THSSUiMZbwG0cJ6ylA1Si2OOMKEmg/view?usp=sharing
- `unzip` and start Pentaho
```bash
./data-integration/spoon.sh
```

## Setup project
**Just, Python and Docker**
```bash
sudo snap install docker --stable --classic && \
sudo snap install just --stable --classic && \
sudo apt install python3
```

**Start a PostgreSQL database**
```bash
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
```

## exercises requirements
- **ex00** *req:* PostgreSQL database
- **ex05** *req:* `ex04_p1.csv` and `ex04_p2.csv` file. Run ex04 to get it
- **ex06** *req:* The dirtyFakeName_50K.csv. run `just dirty` to make a another dirty version of FakeName_50K.csv

## Pentaho Schemas
**exercise 00**
![](https://github.com/kazourak/pdi_practice/blob/main/img/ex00.png)

**exercise 01**
![](https://github.com/kazourak/pdi_practice/blob/main/img/ex01.png)

**exercise 02**
![](https://github.com/kazourak/pdi_practice/blob/main/img/ex02.png)

**exercise 03**
![](https://github.com/kazourak/pdi_practice/blob/main/img/ex03.png)

**exercise 04**
![](https://github.com/kazourak/pdi_practice/blob/main/img/ex04.png)

**exercise 05**
![](https://github.com/kazourak/pdi_practice/blob/main/img/ex05.png)

**exercise 06**
![](https://github.com/kazourak/pdi_practice/blob/main/img/ex06.png)

