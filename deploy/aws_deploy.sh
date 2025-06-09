
#!/bin/bash

# Update system and install Docker
sudo apt-get update
sudo apt-get install -y docker.io docker-compose git

# Enable Docker
sudo systemctl enable docker
sudo systemctl start docker

# Clone the GitHub repo (replace with your actual repo)
git clone https://github.com/YOUR_USERNAME/skystrike-prod.git
cd skystrike-prod

# Build and run the containers
sudo docker-compose build
sudo docker-compose up -d
