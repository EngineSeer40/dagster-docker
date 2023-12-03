# Create /mnt folders if they dont exist

if [ ! -d /mnt/sentimax]; then
  mkdir -p /mnt/sentimax;
fi

if [ ! -d /mnt/grafana]; then
  mkdir -p /mnt/grafana;
fi

if [ ! -d /mnt/gcloud]; then
  mkdir -p /mnt/gcloud;
fi

# if [ -x "$(command -v docker)" ]; then
#     echo "Docker already installed"
# else
#     echo "Installing docker"
#     sudo apt-get update
#     sudo apt-get install ca-certificates curl gnupg
#     sudo install -m 0755 -d /etc/apt/keyrings
#     curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
#     sudo chmod a+r /etc/apt/keyrings/docker.gpg
# fi