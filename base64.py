BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64_encode(data):
    result = []
    i = 0
    while i < len(data):
        chunk = data[i:i+3]
        padded = chunk + b'\x00' * (3 - len(chunk))
        num = (padded[0] << 16) + (padded[1] << 8) + padded[2]
        indices = [
            (num >> 18) & 63,
            (num >> 12) & 63,
            (num >> 6) & 63,
            num & 63
        ]
        for idx in indices:
            result.append(BASE64_CHARS[idx])
        i += 3
    
    pad_len = len(data) % 3
    if pad_len == 1:
        result[-2:] = ['=', '=']
    elif pad_len == 2:
        result[-1] = '='
    
    return ''.join(result)

def base64_decode(b64_str):
    b64_clean = b64_str.rstrip('=')
    char_to_index = {}
    for i in range(len(BASE64_CHARS)):
        char_to_index[BASE64_CHARS[i]] = i
    
    result = []
    i = 0
    while i < len(b64_clean):
        chunk = b64_clean[i:i+4]
        while len(chunk) < 4:
            chunk += 'A'
        
        indices = []
        for ch in chunk:
            indices.append(char_to_index.get(ch, 0))
        
        num = (indices[0] << 18) + (indices[1] << 12) + (indices[2] << 6) + indices[3]
        bytes_to_add = 3
        if i + 4 > len(b64_clean):
            padding_count = 4 - len(b64_clean[i:])
            bytes_to_add = 3 - padding_count
        
        for j in range(bytes_to_add):
            result.append((num >> (16 - 8*j)) & 0xFF)
        i += 4
    
    return bytes(result)

if __name__ == "__main__":
    test_data = b"123456"
    encoded = base64_encode(test_data)
    print(encoded)
    decoded = base64_decode(encoded)
    print(decoded)