#!/bin/sh -e

cp /flag /dev/shm/flag

qemu-system-x86_64 \
    -device virtio-blk,drive=alpine \
    -blockdev driver=qcow2,file.filename=./alpine.qcow2,file.driver=file,node-name=alpine,read-only=true,auto-read-only=true \
    -m 256m -kernel ./vmlinuz-virt -initrd ./initramfs-virt \
    -append "root=UUID=0eb3588b-da48-4c5e-a050-209c913fa8ea modules=ext4 quiet rootfstype=ext4 console=ttyS0 quiet oops=panic panic=1" \
    -device virtio-blk,drive=flag \
    -blockdev driver=raw,file.filename=/dev/shm/flag,file.driver=file,node-name=flag,read-only=false,auto-read-only=false \
    -nographic -no-reboot -monitor /dev/null -nic none
