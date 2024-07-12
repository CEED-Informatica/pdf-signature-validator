To see the contents of the sig0 file:

```sh
FILE=<the sig0 file>
openssl pkcs7 -in $FILE -inform DER -print_certs # To console
openssl pkcs7 -in $FILE -inform DER -print_certs -out certs.pem # To certs.pem file
```
