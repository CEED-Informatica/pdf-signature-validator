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

def extract_pem_file(filename, output_filename):
    result = subprocess.run(['openssl', 'pkcs7', '-in',  filename, '-inform', 'DER', '-print_certs', '-out', output_filename ], capture_output=True, text=True)
    return result.returncode == 0

# Main function
def main():
    FILE='./tmp/test.pdf.sig0'
    extract_pem_file(FILE, output_filename='./tmp/certs.pem')
    certs = load_certs_from_file('certs.pem')
    root_ca_files = ['root_ca_cert1.pem', 'root_ca_cert2.pem', 'root_ca_cert3.pem']  # List of your root CA certificates

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
