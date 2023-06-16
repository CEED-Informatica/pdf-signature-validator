<a name="readme-top"></a>

## About The Project

This project is a wrapper around `pdfisg` tool from [poppler-utils](https://poppler.freedesktop.org/) to validate and get the signer of a PDF file. It will launch `pdfsig` with the pdf and nss database specified in the constructor, and return the common name of the PDF's signer.

It is tested with a specific version of `pdfsig`: 20.09.0. Maybe it works with other versions, but it heavily depends on `pdfsig` output format.

There are two additional projects: XXXX to export a flask endpoint for verifying pdfs files, and XXXX which generates a Docker image with all the tools needed to run that service.


## Prerequisites

You should have `pdfsig` version 20.09 and installed in your system.

If you need to create a nss database with your custom set of certificates, you will also need `libnss3-tools`. This is an example script for creating such database:

```bash
#! /usr/bin/env bash

DATABASE=/certificates_database
CERTIFICATES_DIR=/certificates

# Create empty certificates database
mkdir $DATABASE
certutil -N -d $DATABASE --empty-password

# Adds certificates
for CERT_FILE in $CERTIFICATES_DIR/*; do
  CERT_NAME=$(basename $CERT_FILE)
  certutil -A -n $CERT_NAME -i $CERT_FILE -t ",C" -d $DATABASE
done

# Certificates are not needed anymore
rm -rf $CERTIFICATES_DIR
```


## Usage

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.


SignatureValidator

 Example usage:
```python
try:
    print(SignatureValidator('test.pdf', '/certificates_database').get_signer())
except SignatureValidatorException as e:
    print(e.build_response())
```


SignatureValidatorException

There are many great README templates available on GitHub; however, I didn't find one that really suited my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should implement DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this template!

Use the `BLANK_README.md` to get started.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




### Installation

INSTALLING FROM GIT
INSTALLING FROM LOCAL DIRECTORY


1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the GPL v3 License. See `LICENSE.md` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<p align="right">(<a href="#readme-top">back to top</a>)</p>
