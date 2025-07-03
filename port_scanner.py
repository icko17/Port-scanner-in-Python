from tqdm import tqdm
from multiprocessing.pool import ThreadPool
import socket

# Target IP address for scanning (replace with your own)
HOST = '' # <- your target IP

# Number of ports: from 1 to 65535
PORTS_TOTAL = 2 ** 16

# Maximum timeout waiting for port response (in seconds)
TIMEOUT = 1

# Check if port is open: returns port number if open, otherwise None
def is_open_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(TIMEOUT)
        return None if sock.connect_ex((HOST, port)) else port

if __name__ == '__main__':
    # Create a pool of 3000 threads
    pool = ThreadPool(3000)

    # Scan ports, show progress via tqdm
    scanned_ports = list(
        tqdm(pool.imap(is_open_port, range(1, PORTS_TOTAL)), total=PORTS_TOTAL - 1, desc=f'Scanning {HOST}')
    )

    # Output only open ports
    print([port for port in scanned_ports if port])
