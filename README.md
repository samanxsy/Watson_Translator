# Watson_Translator
A Translator powered by IBM Watson


## Getting Started
These instructions will get you a copy of the project to run it on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Flask
- ibm-Watson
- ibm-cloud-sdk-core
- IBM Cloud account

### Installing 

1. clone the repository to your local machine:
  - git clone https://github.com/samanxsy/Watson_Translator.git
2. Install the requirements
- ```
  pip install -r requirements.txt
  ```
3. Create an IBM Cloud account <https://cloud.ibm.com/login>
4. Get your API Key and store it as an environment variable > "watson_API_KEY"
- 
  ```
  export watson_API_KEY="<your API key>"
  ```
5. Check the paths
6. Run the program
7. To run the tests, take the Test_translator.py to the root directory

### Build With

- Python - Programming Language
- Flask - Web framework
- IBM Watson AI

### App view
![Watson_translator](https://user-images.githubusercontent.com/118216325/217238123-f689689d-5c2f-4945-8802-99cced9d694a.png)

### Containerization
- If you want to run the application in a container, follow these steps: 
- If you don't have docker installed visit: <https://www.docker.com/>

  - build the container image using the docker file:
  ```
  docker build -t watson-translator:v1.0 .
  ```
  - Run the container using this command, passing in your API_KEY as an environment variable and mapping the Flask port: 
  ```
  docker run -e watson_API_KEY=$watson_API_KEY -p 8000:8000 watson-translator:v1.0
  ```
### Author

 - Samanxsy (Saman Saybani)
 
### Acknowledgments

 - This project is inspired by IBM Skills Network
 - The translation is powered by IBM Watson AI
