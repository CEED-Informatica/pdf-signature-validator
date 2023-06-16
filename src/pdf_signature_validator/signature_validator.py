import subprocess

from .pdfsig_output_decoder import PdfSigDecoder, PdfSigDecoderException
from .error_codes import error_codes

class SignatureValidatorException(RuntimeError):
    def __init__(self, error_code, output=None ):
        super().__init__()
        self._error_code = error_code
        self._error_message = error_codes[error_code]
        self._output = output

    @property
    def error_code(self):
        return self._error_code

    @property
    def error_message(self):
        return self._error_message

    @property
    def output(self):
        return self._output

    def build_response(self):
        response = {
            'error_code': self._error_code,
            'error_message': self._error_message,
            'output': self._output
        }
        return {key: value for key, value in response.items() if value is not None}


class SignatureValidator:

    def __init__(self, pdf_filename, nssdb_path: str = None):
        self.pdf_filename = pdf_filename
        self.nssdb_path = nssdb_path

    def get_signer(self):
        try:
          pdfsig_output = SignatureValidator._run_pdfsig(self.pdf_filename, self.nssdb_path)
        except Exception as e:
          raise SignatureValidatorException('PDFSIG_ERROR', str(e))

        try:
            return PdfSigDecoder.get_signer(pdfsig_output)
        except PdfSigDecoderException as e:
            raise SignatureValidatorException(e.error_code)

    @staticmethod
    def _run(command):
        result = subprocess.run(command, capture_output=True, text=True, shell=True)

        # Check the return code to ensure the command executed successfully
        if result.returncode == 0:
            return (result.returncode, result.stdout)
        else:
          return (result.returncode, result.stderr)

    @staticmethod
    def _run_pdfsig(pdf_filename, nssdb_path):
        nssdir_option = f'-nssdir "{nssdb_path}"' if nssdb_path else ''
        command = f'pdfsig {nssdir_option} "{pdf_filename}"'
        (return_code,output) = SignatureValidator._run(command)

        if return_code != 0: raise Exception(f'pdfsig failed: {output}')

        return output

# Example usage:
# if(__name__ == '__main__'):
#   try:
#     print(SignatureValidator('test.pdf').get_signer())
#   except SignatureValidatorException as e:
#     print(e.build_response())
