import unittest
from textwrap import dedent

import sys
sys.path.append("./src/pdf_signature_validator")
from src.pdf_signature_validator.pdfsig_output_decoder import PdfSigDecoder, PdfSigDecoderException

def ml(text):
  return dedent(text).strip("\n")

class TestPdfSigDecoder(unittest.TestCase):

  '''
  The outputs are from the command line tool pdfsig version 20.09.0

  If you change the version, check that the messages are the same or
  update the module accordingly.
  '''

  def test_valid_signature(self):
    # Single valid signature, FNMT certificate
    output = ml("""\
      Digital Signature Info of: your_filename.pdf
      Signature #1:
        - Signer Certificate Common Name: SURNAME1 SURNAME2 NAME - 12345678X
        - Signer full Distinguished Name: CN=SURNAME1 SURNAME2 NAME - 12345678X,SN=SURNAME1 SURNAME2,givenName=NAME,serialNumber=IDCES-12345678X,C=ES
        - Signing Time: Mar 30 2023 10:15:25
        - Signing Hash Algorithm: SHA-256
        - Signature Type: ETSI.CAdES.detached
        - Signed Ranges: [0 - 252], [54254 - 59682]
        - Total document signed
        - Signature Validation: Signature is Valid.
        - Certificate Validation: Certificate is Trusted.
    """)
    self.assertEqual('SURNAME1 SURNAME2 NAME - 12345678X', PdfSigDecoder.get_signer(output))


  def test_not_signed(self):
    output = ml("""\
      File 'MY FILE HERE' does not contain any signatures
      """)

    with self.assertRaises(PdfSigDecoderException) as context:
      PdfSigDecoder.get_signer(output)

    self.assertEqual('NOT_SIGNED',str(context.exception))


  def test_invalid_signature(self):
    # Invalid signature, modified with hexedit
    output = ml("""\
    Syntax Error (5825): Illegal character <55> in hex string
    Syntax Error (5825): Illegal character <55> in hex string
    Digital Signature Info of: Firma_invalida.pdf
    Signature #1:
      - Signature Field Name: Signature1
      - Signer Certificate Common Name: NAME SURNAME1 SURNAME2 - NIF:12345678X
      - Signer full Distinguished Name: C=ES,O=ACCV,OU=CIUDADANOS,SN=SURNAME1 SURNAME2,givenName=NAME,serialNumber=12345678X,CN=NAME SURNAME1 SURNAME2 - NIF:12345678X
      - Signing Time: Mar 30 2023 10:15:25
      - Signing Hash Algorithm: SHA-256
      - Signature Type: ETSI.CAdES.detached
      - Signed Ranges: [0 - 252], [54254 - 59682]
      - Not total document signed
      - Signature Validation: Digest Mismatch.
    """)

    with self.assertRaises(PdfSigDecoderException) as context:
      PdfSigDecoder.get_signer(output)

    self.assertEqual('INVALID_SIGNATURE',str(context.exception))


  def test_expired_certificate(self):
    # Expired certificate FNMT
    output = ml("""\Digital Signature Info of: your_filename.pdf
    Signature #1:
      - Signer Certificate Common Name: NOMBRE SURNAME1 SURNAME2 NAME - NIF 12345678X
      - Signer full Distinguished Name: CN=NOMBRE SURNAME1 SURNAME2 NAME - NIF 12345678X,OU=500052411,OU=FNMT Clase 2 CA,O=FNMT,C=ES
      - Signing Time: Jun 06 2011 10:25:22
      - Signing Hash Algorithm: SHA-256
      - Signature Type: ETSI.CAdES.detached
      - Signed Ranges: [0 - 263], [54265 - 59498]
      - Total document signed
      - Signature Validation: Signature is Valid.
      - Certificate Validation: Certificate has Expired
    """)

    with self.assertRaises(PdfSigDecoderException) as context:
      PdfSigDecoder.get_signer(output)

    self.assertEqual('EXPIRED_CERTIFICATE',str(context.exception))

  def test_revoked_signature(self):
    # Single revoked signature, ACCV certificate
    output = ml("""\
      Digital Signature Info of: /tmp/Valido_CCVA_signed.pdf
      Signature #1:
        - Signer Certificate Common Name: ALVARO MACEDA ARRANZ - NIF:33408425M
        - Signer full Distinguished Name: C=ES,O=ACCV,OU=CIUDADANOS,SN=MACEDA ARRANZ,givenName=ALVARO,serialNumber=33408425M,CN=ALVARO MACEDA ARRANZ - NIF:33408425M
        - Signing Time: May 05 2023 12:04:11
        - Signing Hash Algorithm: SHA-256
        - Signature Type: ETSI.CAdES.detached
        - Signed Ranges: [0 - 256], [54258 - 59686]
        - Total document signed
        - Signature Validation: Signature is Valid.
        - Certificate Validation: Certificate has been Revoked.
    """)
    with self.assertRaises(PdfSigDecoderException) as context:
      PdfSigDecoder.get_signer(output)

    self.assertEqual('REVOKED_CERTIFICATE',str(context.exception))

  # TO-DO: multiple signatures

if __name__ == '__main__':
  unittest.main()
