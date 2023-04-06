import struct
import zlib

with open('pp-min.png', 'rb') as f:
    data = f.read()

if data[:8] != b'\x89PNG\r\n\x1a\n':
    print("Not a valid PNG file.")
    exit()

def read_chunks(data):
    offset = 8
    idat_data = b''
    while offset < len(data):
        length = struct.unpack('!I', data[offset:offset + 4])[0]
        chunk_type = data[offset + 4:offset + 8]
        chunk_data = data[offset + 8:offset + 8 + length]
        if chunk_type == b'IDAT':
            idat_data += chunk_data
        offset += 8 + length + 4
    return idat_data

idat_data = read_chunks(data)

image_data = zlib.decompress(idat_data)
with open('pp-min.idat', 'wb') as f:
    f.write(image_data)

