import dns.resolver
import sys
import re
import colorama
import pyfiglet
import time

def enumerate_animation():
    animation_frames = ["|", "/", "-", "\\"]
    number_of_cycles = 4  # Adjust the number of cycles you want for the animation
    delay = 0.25  # Delay between frames

    for i in range(number_of_cycles * len(animation_frames)):
        sys.stdout.write('\033[2K')
        sys.stdout.write('\r')
        sys.stdout.write(f'Enumerating: {animation_frames[i % len(animation_frames)]}')
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write('\033[2K\r')
    sys.stdout.flush()

def is_valid_domain(domain):
    pattern = re.compile(
        r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    )
    return pattern.match(domain)

def resolve_record(domain):
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'SRV', 'CNAME', 'PTR', 'NAPTR', 'HINFO', 'RP', 'LOC', 'AFSDB', 'CERT', 'DNSKEY', 'DS', 'KEY', 'NSEC', 'RRSIG', 'TLSA', 'SMIMEA', 'SSHFP', 'IPSECKEY', 'DLV']

    for record in record_types:
        try:
            if not is_valid_domain(domain):
                print('\033[91mERROR: The domain name provided is not valid.\033[0m')
                print('Please enter a valid domain name, such as "example.com".')
                sys.exit(1)
            answer = dns.resolver.resolve(domain, record)
            print('-' * 50)
            for server in answer:
                print(f'\033[92m[+] {domain}\033[0m - {record} - {server}')
        except dns.resolver.NoAnswer:
            # print(f'{domain} - {record} - No record found')
            pass
        except dns.resolver.NXDOMAIN:
            print(f'\033[92m[+] \033[0m{domain} - {record} - {server}')
            quit()
        except KeyboardInterrupt:
            print('\nUser interrupted')
            sys.exit(0)

def resolve_subdomain(domain):
    subdomains_file = "subdomains.txt"

    try:
        with open(subdomains_file, 'r') as file:
            subdomains = [line.strip() for line in file]
    except FileNotFoundError:
        print(f'File {subdomains_file} not found')
        quit()
    
    subdomain_store = []
    output_file = f"{domain}_valid_subdomains.txt"
    for subdoms in subdomains:
        try:
            ip_value = dns.resolver.resolve(f'{subdoms}.{domain}', 'A')
            if ip_value:
                subdomain_store.append(f'{subdoms}.{domain}')
                print(colorama.Fore.GREEN + f"{subdoms}.{domain} is valid")
                write_found_subdomains(output_file, subdomain_store)
        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.NoAnswer:
            pass
        except KeyboardInterrupt:
            print(colorama.Fore.YELLOW + "\nScan interrupted by user. Exiting...")
            sys.exit(1)

def write_found_subdomains(output_file, subdomain_store):
    with open(output_file, 'w') as file:
        for subdomain in subdomain_store:
            file.write(subdomain + "\n")

def main():
    colorama.init()

    try:
        domain = sys.argv[1]
    except IndexError:
        print('\033[91mSyntax ERROR - Usage: python3 sub_dns_enum.py <domain>\033[0m')
        quit()

    ascii_art = pyfiglet.figlet_format("DNScan", font="colossal")
    print(ascii_art)
    print(f'\033[92m[+] DNS Enumeration started for : {domain}\033[0m')

    enumerate_animation()

    resolve_record(domain)
    print('\n')
    print('\033[92m[+] DNS Enumeration completed\033[0m')
    print('\n')
    print(f"\033[92m[+] Initiating subdomain scan for: {domain} \033[0m\n")

    enumerate_animation()
    resolve_subdomain(domain)

if __name__ == '__main__':
    main()
