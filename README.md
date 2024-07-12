<a name="readme-top"></a>

## About The Project

This project is a wrapper around `pdfisg` tool from [poppler-utils](https://poppler.freedesktop.org/) to validate and get the signer of a PDF file. It will launch `pdfsig` with the pdf and nss database specified in the constructor, and return the common name of the PDF's signer.

It is tested with a specific version of `pdfsig`: 20.09.0. Maybe it works with other versions, but it heavily depends on `pdfsig` output format.

You also have the project [pdf-signature-validator-service](https://github.com/CEED-Informatica/pdf-signature-validator-service) which export a flask endpoint for verifying pdfs files, with a Docker image with all the tools needed to run that service.


## Prerequisites

You should have `pdfsig` version 20.09 and installed in your system.

If you need to create a nss database with your custom set of certificates, you will also need `libnss3-tools`. This is an example script for creating such database:

```bash
#! /usr/bin/env bash

DATABASE=/certificates_database
CERTIFICATES_DIR=/certificates

# Create empty certificates database
rm -rf $DATABASE
mkdir $DATABASE
certutil -N -d $DATABASE --empty-password

# Adds certificates
for CERT_FILE in $CERTIFICATES_DIR/*; do
  CERT_NAME=$(basename $CERT_FILE)
  certutil -A -n $CERT_NAME -i $CERT_FILE -t ",C" -d $DATABASE
done

# Certificates are not needed anymore
# rm -rf $CERTIFICATES_DIR
```

You can test
```sh
DATABASE=/certificates_database
PDF_FILE=<your pdf file>
pdfsig -nssdir $DATABASE
```

## Usage

The module exports two classes: `SignatureValidator` and `SignatureValidatorException`.

### SignatureValidator

`SignatureValidator` takes as parameters the path of a pdf file and, optionally, the directory path of an nss database of certificates. It will return the pdf's signer common name when you call the method get_signer. It has no other methods:

```python
try:
    print(SignatureValidator('test.pdf', '/certificates_database').get_signer())
except SignatureValidatorException as e:
    print(e.build_response())
```
The call to pdfsig will check the revocation of the certificates using OCSP, if the certificate has expired, etc. If you pass a nss database it will take in account only the signers from that database.

In case the pdf or the signature is not correct, it will throw a `SignatureValidatorException`

###  SignatureValidatorException

This exception has three fields:
- `error_code`: One of the `error_codes` from `error_codes.py`.
- `error_message`: The corresponding message for the error code
- `output`: The output of pdfsig if the command has failed to run. It can be `None`.

For example, if you pass a pdf file signed by

It also has a method, `get_response()`, which will build a hash with those fields. It is intended to ease the construction of the response in API services.

### Installation

INSTALLING FROM GIT
INSTALLING FROM LOCAL DIRECTORY

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Testing

From the root folder:
```bash
python -m unittest discover -s tests -p 'test_*.py'
```


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

Alvaro Maceda - alvaro@alvaromaceda.es

Project Link: [https://github.com/CEED-Informatica/pdf-signature-validator](hhttps://github.com/CEED-Informatica/pdf-signature-validator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
