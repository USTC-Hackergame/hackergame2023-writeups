import subprocess
import base64

if __name__ == '__main__':
    print('Please input your file in a base64 encoded format, ends with an EOF in newline.'
          ' "\\n" is ignored when decoding.')

    data_read = ''
    while True:
        line = input().strip()
        if line == 'EOF':
            break
        data_read += line

    full_content = base64.b64decode(data_read).decode('utf-8')

    ret = subprocess.run([
        '/src/MyCalculator',
    ], input=full_content.encode())
