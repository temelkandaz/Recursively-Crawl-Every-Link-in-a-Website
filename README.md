# Recursively Crawl a Website

app.py Python script recursively crawls a webpage and follows not only the links found but also the links of the links found by recursive crawling.

Please complete the following steps before using the script:
* URL of a webpage needs to be entered as URL_TO_CRAWL variable in config.py.

* Domain name needs to be entered as DOMAIN_NAME variable in config.py

* Selenium package needs to be installed for the script, requirements file may be used to install the package. (pip install -r requirements.txt)

* chromedriver needs to be installed and the path of the executable file of chromedriver needs to be entered as CHROMEDRIVER_PATH in config.py. Download page of the chromedriver: https://chromedriver.chromium.org/downloads

# Dockerizing the app

Please complete the following steps before building and running this app inside a Docker container:
* URL of a webpage needs to be entered as URL_TO_CRAWL variable in config.py.

* Domain name needs to be entered as DOMAIN_NAME variable in config.py

PS 1: There is no need to install the requirements since Dockerfile is designed to install it during the build of the container. 
PS 2: Please do not change CHROMEDRIVER_PATH in config.py since Dockerfile is designed to add the chromedriver to the predefined location. 

After completion of the above steps, the app is ready to be built and run inside a container.
