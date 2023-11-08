# plex
This docker image is a custom image of prowlarr based on plexinc/pms-docker

# Parameters
Container images are configured using parameters passed at runtime has environment variable.

The parameters below are taken from the original image [plexinc/pms-docker](https://hub.docker.com/r/plexinc/pms-docker/) :
|  Parameters                   | Examples values           | Functions                                                                                                      |
|-------------------------------|---------------------------|----------------------------------------------------------------------------------------------------------------|
| PUID                          |  1000                     | for UserID                                                                                                     |
| PGID                          |  1000                     | for GroupID                                                                                                    |
| TZ                            |  Europe/Paris             | Specify a timezone to use, see this [List](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). |
| ALLOWED_NETWORKS              |  192.168.1.0/24           | IP/netmask entries which allow access to the server without requiring authorization                            |
| ADVERTISE_IP                  |  http://10.1.1.23:32400   | This variable defines the additional IPs on which the server may be be found                                   |
| CHANGE_CONFIG_DIR_OWNERSHIP   |  true                     | Change ownership of config directory to the plex user                                                          |
