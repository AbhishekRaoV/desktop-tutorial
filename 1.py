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
            userDataBase64: IyEvYmluL2Jhc2gKdXNlcnM6CiAtIG5hbWU6IHVidW50dQogICAgcGFzc3dkOiAiZm9vIgogICAgc2hlbGw6IC9iaW4vYmFzaAogICAgbG9ja3Bhc3N3ZDogZmFsc2UKICAgIHNzaF9wd2F1dGg6IFRydWUKICAgIGNoYXBzd2Q6IHsgZXhwaXJlOiBGYWxzZSB9CiAgICBzdWRvOiBBTEx9KEFMTCkgTk9QQVNTV0Q6QUxMClxuICAgIGdyb3VwczogdXNlcnMsIGFkbWluXG0K
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
