# Manual de Instalacion WebApp
## Secuencia de Comandos para instalación en Amazon EC2
## OS: Ubuntu Server | Instancia tipo: t2.small | Almacenamiento: 20Gb SSD

### Preparar Maquina: 
Debe ejecutar las siguientes lineas una a una en orden:
```bash
sudo apt-get remove docker docker-engine docker.io containerd runc

sudo apt-get update

sudo apt-get install ca-certificates curl gnupg

sudo install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Desplegar Aplicacion Web:
```bash
sudo docker build -t webapp:latest .

sudo docker run -p 8000:8000 -it webapp
```