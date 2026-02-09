import socket
import struct
from threading import Thread

def scan_port(ip, port, results):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((ip, port))
        results.append(port)
    except:
        pass
    finally:
        s.close()

def scan_ports(target='127.0.0.1', start=1, end=1000):
    threads = []
    open_ports = []
    
    for port in range(start, end + 1):
        t = Thread(target=scan_port, args=(target, port, open_ports))
        threads.append(t)
        t.start()
        if len(threads) >= 100:
            for t in threads:
                t.join()
            threads = []
    
    for t in threads:
        t.join()
    
    open_ports.sort()
    return open_ports

if __name__ == "__main__":
    ports = scan_ports('127.0.0.1', 1, 1000)
    print(ports)