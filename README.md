# DjangoUnsynqed Project
DjangoUnsqyned was a project to showcase my abilities as a developer. It includes information and qualifications about myself, and a poll system that uses a static cloud database to hold synchronize all results. 


# Deployment
The entire project is dockerized and can be found [here](https://cloud.docker.com/swarm/noxor0/repository/docker/noxor0/djangounsynqed/general). 

Requires an environment file that contains all secrets.

To deploy:
```
sudo docker run --env-file=<environment_file> -p 8000:8000 noxor0/djangounsynqed:latest
```

Will deploy the application and it will be accessible at
```
127.0.0.1:8000
```


