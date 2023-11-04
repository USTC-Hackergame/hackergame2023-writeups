from hashlib import sha1

merkle_root = None

zero_hash = sha1(b'').digest()

while True:
    print('Welcome to the O(1) login system')
    print('1. Import users')
    print('2. Login')
    choice = int(input('Choice: '))
    if choice == 1:
        print('Enter user:password per line, ends with EOF')
        data = []
        while True:
            s = input('> ').strip()
            assert len(s) < 100
            if s == 'EOF':
                break
            user, password = s.split(':')
            if user == 'admin':
                print('No way!')
                exit(-1)
            data.append(user + ':' + password)
        assert len(data) >= 2

        depth = 0
        while 2 ** depth < len(data):
            depth += 1
        buffer = [None] * (2 ** depth * 2)
        for i in range(2 ** depth):
            if i < len(data):
                buffer[2 ** depth + i] = sha1(data[i].encode()).digest()
            else:
                buffer[2 ** depth + i] = zero_hash
        for i in range(2 ** depth - 1, 0, -1):
            hash1 = buffer[i * 2]
            hash2 = buffer[i * 2 + 1]
            if hash1 > hash2:
                hash1, hash2 = hash2, hash1
            buffer[i] = sha1(hash1 + hash2).digest()
        merkle_root = buffer[1]

        print('Login credentials:')
        for i in range(len(data)):
            proof = ''
            index = 2 ** depth + i
            while index > 1:
                pair_index = index + 1 if index % 2 == 0 else index - 1
                proof += buffer[pair_index].hex()
                index //= 2
            print(data[i] + ':' + proof)
    elif choice == 2:
        if merkle_root is None:
            print('You need to import users first')
            continue
        user, password, proof = input('Login credential: ').strip().split(':')
        assert len(user) + len(password) + 1 < 100
        proof = bytes.fromhex(proof)
        assert len(proof) % 20 == 0
        proof = [proof[i * 20 : i * 20 + 20] for i in range(len(proof) // 20)]
        h = sha1((user + ':' + password).encode()).digest()
        for p in proof:
            hash1 = h
            hash2 = p
            if hash1 > hash2:
                hash1, hash2 = hash2, hash1
            h = sha1(hash1 + hash2).digest()
        if h == merkle_root:
            print(f'Hello, {user}!')
            if user == 'admin':
                print(open('flag').read())
            else:
                print('You are not admin')
        else:
            print('Invalid login credential')
