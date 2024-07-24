---
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: ubuntu-vm
spec:
  running: true
  template:
    metadata:
      labels:
        kubevirt.io/size: small
        kubevirt.io/domain: ubuntu-vm
    spec:
      domain:
        cpu:
          cores: 2
        devices:
          disks:
            - name: containerdisk
              disk:
                bus: virtio
            - name: cloudinitdisk
              disk:
                bus: virtio
          interfaces:
            - name: default
              masquerade: {}
        resources:
          requests:
            memory: 8192Mi
      networks:
        - name: default
          pod: {}
      volumes:
        - name: containerdisk
          containerDisk:
            image: tedezed/ubuntu-container-disk:22.0
        - name: cloudinitdisk
          cloudInitNoCloud:
            userData: |
              # cloud-config
              users:
                - default
                - name: ubuntu
                  passwd: "paswrd"
                  shell: /bin/bash
                  lock-passwd: false
                  ssh_pwauth: True
                  chpasswd: { expire: False }
                  sudo: ALL=(ALL) NOPASSWD:ALL
                  groups: users, admin
---
apiVersion: v1
kind: Service
metadata:
  name: ubuntu-vm-svc
spec:
  ports:
    - port: 22
      targetPort: 22
      protocol: TCP
  selector:
    kubevirt.io/domain: ubuntu-vm
  type: NodePort
