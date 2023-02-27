# Watson_Translator
A Translator powered by IBM Watson

[![CI](https://github.com/samanxsy/Watson_Translator/actions/workflows/CI.yaml/badge.svg)](https://github.com/samanxsy/Watson_Translator/actions/workflows/CI.yaml)


## Getting Started
These instructions will get you a copy of the project to run it on your local machine for development and testing purposes. [Version 2.0]

### Prerequisites

- Python 3.10
- Flask
- ibm-Watson
- ibm-cloud-sdk-core
- IBM Cloud account

### Installing 

1. Clone the repository to your local machine:
  - git clone https://github.com/samanxsy/Watson_Translator.git
2. Create and activate a virtual environment 
  - MacOS & Linux:
```
virtualenv .venv
source .venv/bin/activate
```
3. Install the requirements
- ```
  pip install -r requirements.txt
  ```
3. Create an IBM Cloud account <https://cloud.ibm.com/login>
4. Get your API Key and store it as an environment variable > "API_KEY"
- 
  ```
  export API_KEY="<your API key>"
  ```
5. run the program on your local host
```
gunicorn app.server:app
```

### Built With

- Python - Programming Language
- Flask - Web framework
- IBM Watson AI

### App view
![Watson-app](https://user-images.githubusercontent.com/118216325/221532711-7e42e211-e5d8-4373-9997-7f65c4750fc5.png)
![w3](https://user-images.githubusercontent.com/118216325/221532776-5aed298b-fac7-4c02-9d44-116d8757b8b3.png)
![w4](https://user-images.githubusercontent.com/118216325/221532802-0a60a951-2186-4b49-ba5e-a1e945adbbd6.png)

### Docker container
- If you want to run the application in a container, follow these steps: 
- If you don't have docker installed visit: <https://www.docker.com/>

  - Pull the Dockerimage from Docker hub: 
  ```
  docker pull samanxsy/041e3c24bd37a492be8a39dd64c9b5846c9933c0e8ea5b8d7969f398780b36a5:latest
  ```
OR
  - build a new container image using the docker file:
  ```
  docker build -t <app-name>:<version> .
  ```
  - After pulling the image or creating one, run the container using this command, pass your API_KEY as an environment variable and map the port: 
  ```
  docker run -e API_KEY=$API_KEY -p 8000:8000 <image-id>:latest
  ```
### Author

 - Saman Saybani
 
### Acknowledgments

 - This project is inspired by IBM Skills Network
 - The translation is powered by IBM Watson AI
