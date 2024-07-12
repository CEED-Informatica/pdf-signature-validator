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
