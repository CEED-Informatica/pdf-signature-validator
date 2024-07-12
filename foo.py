import os
import subprocess

# Function to verify certificate against a CA certificate
def verify_cert(cert_file, ca_file):
    result = subprocess.run(['openssl', 'verify', '-CAfile', ca_file, cert_file], capture_output=True, text=True)
    return result.stdout.strip()

# Function to load certificates from PEM file
def load_certs_from_file(pem_file):
    with open(pem_file, 'r') as f:
        certs = f.read().split('\n\n')
    return certs

def split_pem_chain(pem_file):
    import re
    import tempfile

    # Split certificates based on the BEGIN/END CERTIFICATE delimiters
    cert_pattern = re.compile(r'(-----BEGIN CERTIFICATE-----.+?-----END CERTIFICATE-----)', re.DOTALL)

    # Read file and extract certificates
    certificates = []
    with open(pem_file, 'r') as file:
        file_content = file.read()
        certificates = re.findall(cert_pattern, file_content)

    # List to store temporary file names
    temp_files = []

    # Process each certificate and save it to a temporary file
    for cert in certificates:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(cert.strip().encode('utf-8'))  # Write certificate content to the temporary file
            temp_files.append(temp_file.name)  # Store the temporary file name

    return temp_files

def extract_pem_file(filename, output_filename):
    result = subprocess.run(['openssl', 'pkcs7', '-in',  filename, '-inform', 'DER', '-print_certs', '-out', output_filename ], capture_output=True, text=True)
    return result.returncode == 0

ROOT_CERTIFICATES_DIRECTORY='./tmp/certificates'
def get_root_certificates():
    directory = ROOT_CERTIFICATES_DIRECTORY
    certificates = os.listdir(directory)

    return[f"{directory}/{file}" for file in certificates if file.endswith('.pem')]

# Main function
def main():
    FILE='./tmp/test.pdf.sig0'
    EXTRACTED_PEM_FILE='./tmp/certs.pem'

    root_ca_files = get_root_certificates()
    extract_pem_file(FILE, output_filename=EXTRACTED_PEM_FILE)

    certs = split_pem_chain(EXTRACTED_PEM_FILE)
    # return
    # certs = load_certs_from_file(EXTRACTED_PEM_FILE)

    # Verify each certificate in the chain against each root CA certificate
    for i in range(len(certs)):
        cert = certs[i]
        if i < len(certs) - 1:
            next_cert = certs[i + 1]
            for root_ca_file in root_ca_files:
                result = verify_cert(next_cert, root_ca_file)
                print(f"Certificate {i + 1} verification result against {root_ca_file}: {result}")

    # Verify the last certificate against each root CA certificate
    last_cert = certs[-1]
    for root_ca_file in root_ca_files:
        result = verify_cert(last_cert, root_ca_file)
        print(f"Last certificate verification result against {root_ca_file}: {result}")

if __name__ == '__main__':
    main()
