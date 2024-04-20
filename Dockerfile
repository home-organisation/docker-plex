#Last package update 20 April 2024
FROM plexinc/pms-docker:latest
LABEL Maintainer="bizalu"

# Prepare environnement
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Install custom post script
COPY custom-script/ /custom-cont-init.d
RUN chmod u+x /custom-cont-init.d/*
