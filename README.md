# splatnet2statink-on-lambda

Forked [splatnet2statink](https://github.com/frozenpandaman/splatnet2statink) to execute it regularly on AWS Lambda.

## Requirements

are the installation of:

- virtualenv
  - python3
  - pip3
- Serverless
  - Node.js
  - NPM
- Docker

## Setup & Deploy to your AWS account

1. Make virtualenv:

```
$ virtualenv venv --python=python3
$ source venv/bin/activate
```

2. Resolve python dependencies:

```
(venv) $ pip3 install -r requirements.txt 
```

3. Create your own splatnet2statink configuration (config.txt)
  - You can do by running `splatnet2statink.py` directly without arguments which will initialize the configuration in interactively 

4. (Optional) At this point you can directly run the handler script:

```
(venv) $ python3 ./handler.py
splatnet2statink v1.3.3
Checking if there are previously-unuploaded battles...
No previously-unuploaded battles found.
```

5. Resolve NPM dependencies:

```
(venv) $ npm i
```

6. Deploy to AWS Lambda using Serverless:

```
(venv $ node_modules/.bin/sls deploy
```

## License 

[GPLv3](https://choosealicense.com/licenses/gpl-3.0/) in according with the original source.
