#!/bin/bash
echo "-----------------------------------------------------------";
echo "-----------------------------------------------------------";
echo "-----------------------------------------------------------";
echo "---------	Bienvenido al instalador de Podman	---------";
echo "-----------------------------------------------------------";
echo "-----------------------------------------------------------";
echo "-----------------------------------------------------------";
echo "Se instalarán paquetes y dependencias para el correcto funcionamiento"
echo "¿Desea continuar? (y/n)"
read response
if [ "$response" = "y" ]; then
  # Actualizar la lista de paquetes
sudo apt-get update

# Instalar paquetes requeridos
sudo apt-get install -y make git gcc build-essential pkgconf libtool libsystemd-dev libprotobuf-c-dev libcap-dev libseccomp-dev libyajl-dev libgcrypt20-dev go-md2man autoconf python3 automake libglib2.0-dev curl libgpgme-dev libdevmapper-dev libbtrfs-dev containernetworking-plugins uidmap


echo "	_______________________________________________________________________	"
echo ""
echo ""
echo "		Instalando golang (compilador)....	"
echo ""
echo ""
echo "	_______________________________________________________________________	"
sleep 2

# Descargar e instalar Go
wget https://go.dev/dl/go1.20.2.linux-amd64.tar.gz
sudo tar -xvf go1.20.2.linux-amd64.tar.gz

sudo mv go /usr/local

# Configurar variables de entorno de Go
export GOROOT=/usr/local/go
export GOPATH=$HOME
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
sudo ln -s /usr/local/go/bin/go /usr/bin/go

# Habilitar la creación de usuarios no privilegiados en el kernel
sudo sysctl kernel.unprivileged_userns_clone=1
echo 'kernel.unprivileged_userns_clone=1' | sudo tee /etc/sysctl.d/userns.conf



echo "	_______________________________________________________________________	"
echo ""
echo ""
echo "		Instalando conmon (monitorizacion)...."
echo ""
echo ""
echo "	_______________________________________________________________________	"
sleep 2
# Clonar el repositorio conmon y compilarlo
git clone https://github.com/containers/conmon
cd conmon
export GOCACHE="$(mktemp -d)"
make
sudo make podman

echo "	_______________________________________________________________________	"
echo ""
echo ""
echo "		Instalando crun(runtime de containers)...."
echo ""
echo ""
echo "	_______________________________________________________________________	"
sleep 2
# Clonar el repositorio crun y compilarlo
cd /
git clone https://github.com/containers/crun
cd crun
./autogen.sh
./configure
make
sudo make install

echo "---------	Dependencias instaladas	---------"
sleep 3
echo "---------	Se va instalar Podman	---------"
echo "Toca alguna tecla para continuar.........."
read response

# Configurar directorios y archivos para Podman
cd /
sudo mkdir -p /etc/containers
sudo curl -L -o /etc/containers/registries.conf https://src.fedoraproject.org/rpms/containers-common/raw/main/f/registries.conf
sudo curl -L -o /etc/containers/policy.json https://src.fedoraproject.org/rpms/containers-common/raw/main/f/default-policy.json

# Clonar el repositorio de Podman, compilarlo e instalarlo
cd /
git clone https://github.com/containers/podman/
cd podman
make BUILDTAGS="selinux seccomp" PREFIX=/usr
sudo make install PREFIX=/usr
systemctl enable --now podman.socket
else
  echo "Podman no se va a instalar."
fi