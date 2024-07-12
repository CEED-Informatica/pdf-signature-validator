To see the contents of the sig0 file:

```sh
FILE=<the sig0 file>
openssl pkcs7 -in $FILE -inform DER -print_certs # To console
openssl pkcs7 -in $FILE -inform DER -print_certs -out certs.pem # To certs.pem file
```

Download ACCV certificates from:
https://www.accv.es/en/servicios/administracion-publica/descarga-de-certificados-jerarquia/


Convert binary .crt certificate to .pem format:

```sh
CERTIFICATE=<your .crt certificate>
openssl x509 -inform DER -in "${CERTIFICATE}" -out "${CERTIFICATE%.crt}".pem
```



ITS FAILING, IT GIVES INVALID CERTIFICATES AS VALID

https://www.openssl.org/docs/man3.0/man1/openssl-verify.html
https://www.openssl.org/docs/man3.0/man1/openssl-verification-options.html

If your openssl isn't set up to automatically use an installed set of root certificates (e.g. in /etc/ssl/certs), then you can use -CApath or -CAfile to specify the CA.


https://unix.stackexchange.com/questions/16226/how-can-i-verify-ssl-certificates-on-the-command-line

Update

As noted by Klaas van Schelven, the answer above is misleading as openssl appears to verify only single top certificate per file. So it's necessary to issue multiple verify commands for each certificate chain node placed in separate file.

https://stackoverflow.com/questions/20409534/how-does-an-ssl-certificate-chain-bundle-work

