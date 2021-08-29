# mini-node-exporter ✨
This application is a task for **CNCF - Chaos Mesh: Monitoring Metrics about Chaos Mesh** for Linux Foundation Mentorship Program 2021.

## Task Stats
1. **Goal 1**: Build web application and expose required endpoints. ✔️
2. **Optional Bonus 1**: Publish image on Docker Hub and create Dockerfile. ✔️
3. **Goal 2**: Provide monitoring stack of Prometheus and Grafana dashboard. ✔️
4. **Optional BOnus 2**: Orchestrate the monitoring stack via Docker compose. ✔️

## Tech Stack 📦️
1. Python
2. Flask
3. Prometheus
4. Grafana
5. Docker
6. Linux

## Project Stucture 📸
1. **Flask App** - Main application exposing different set of metrics via JSON on several endpoints.
2. **Prometheus** - Main querying application scraping metrics data from the app via `/metrics` endpoint.
3. **Grafana** - Main application for displaying metrics data in different format via dashboards.

## Build Instructions 🚀
1. Inside the /app directory, build the docker image of mini-node-exporter app from the Dockerfile using the following command in terminal.
    
    `sudo docker build --tag mini-node-exporter-app .` 
2. After the image is created, run the docker image and expose the application to port: 23333 of the docker container.
    
    `sudo docker run --name mini-node-exporter-app -p 23333:23333 mini-node-exporter-app`
3. The flask app is up & running now. Open url provided in shell: mostly `http://172.17.0.2:23333`. The localhost of your linux machine defaults to this url inside the container. Open two different terminals and enter this command to setup a watch at `/info/uptime` && `info/load` endpoints.
    
    ```
    1. watch -n 1 "curl localhost:23333/info/uptime"
    2. watch -n 1 "curl localhost:23333/info/load"
    ```
3. All the endpoints exposed by the Flask application: `/metrics | /info | /info/hostname | /info/load | /info/uptime`    
4. Browse through different endpoints of `http://172.17.0.2:23333`. Hit `/metrics` endpoint to see all the metrics scraped by Prometheus. Among the other default metrics, you would see `node_uptime` && `node_load{duration="<time>"}` metrics.
5. Once your flask app is up and working, cd back to project directory where `docker-compose.yml` is present. This compose file is responsible for launching Prometheus and Grafana. Run the following command to launch your dashboard.
    
    `sudo docker-compose up -d`
6. Now your Prometheus client and Grafana are up & running and ready for use. Go to `localhost:9090` to access Prometheus client & to `localhost:3000` to access your Grafana dashboard.
7. Inside your Grafana window, login using `admin` as username and password. Once you're in, click on the `mini-node-exporter-lfx` dashboard to see the `node_load` && `node_time` metrics in graphical format. You could also go to *explore* section and write different PromQL queries and visualize the results.
8. Insde your Prometheus window, write `{job="mini-node-exporter"}` query to see all the metrics being scraped by Prometheus. You could also perform various PromQL queries or visualize metrics in Graphs section.
9. Finally, you can kill the process by running the following command.
    
    `sudo docker-compose down -v`


## mini-app-exporter docker image: https://dockr.ly/3zqAc5I 📌
## Relevant Documentation :page_facing_up:
1. [Prometheus Docs](https://prometheus.io/docs/introduction/overview/)
2. [Prometheus python client](https://github.com/prometheus/client_python)
3. [Grafana Docs](https://grafana.com/docs/)
4. [Docker docs](https://docs.docker.com/reference/)

## Developer :construction_worker:
**Vedant Raghuwanshi**

**Contact: raghuvedant00@gmail.com**
