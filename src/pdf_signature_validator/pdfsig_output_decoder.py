import re

class PdfSigDecoderException(RuntimeError):
    def __init__(self, error_code ):
        super().__init__(error_code)
        self.error_code = error_code


not_signed_re = re.compile(r"File .* does not contain any signatures")
def _check_not_signed(command_output):
    if not_signed_re.search(command_output):
        raise PdfSigDecoderException('NOT_SIGNED')


signature_validation_re = re.compile(r"Signature Validation: (.*)")
def _check_valid_signature(command_output):
    result = signature_validation_re.search(command_output)
    if not result:
        raise PdfSigDecoderException('INVALID_SIGNATURE')

    signature_state = result.group(1)
    if signature_state != 'Signature is Valid.':
        raise PdfSigDecoderException('INVALID_SIGNATURE')


certificate_validation_re = re.compile(r"- Certificate Validation: (.*)")
def _check_valid_certificate(command_output):
    result = re.search(certificate_validation_re, command_output)
    if not result:
       raise PdfSigDecoderException('NOT_VALID_CERTIFICATE')

    signature_state = result.group(1)

    if signature_state == 'Certificate has Expired':
        raise PdfSigDecoderException('EXPIRED_CERTIFICATE')

    if signature_state == 'Certificate has been Revoked.':
        raise PdfSigDecoderException('REVOKED_CERTIFICATE')

    if signature_state != 'Certificate is Trusted.':
        raise PdfSigDecoderException('INVALID_SIGNATURE')


signer_re = re.compile(r"- Signer Certificate Common Name: (.*)")
def _get_common_name(command_output):
    result = re.search(signer_re, command_output)
    if not result:
       raise PdfSigDecoderException('PDFSIG_BAD_OUTPUT')

    return result.group(1)


class PdfSigDecoder:

    @staticmethod
    def get_signer(command_output):
        _check_not_signed(command_output)
        _check_valid_signature(command_output)
        _check_valid_certificate(command_output)
        return _get_common_name(command_output)
