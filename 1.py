apiVersion: kubevirt.io/v1alpha1
kind: VirtualMachinePreset
metadata:
  name: large
spec:
  selector:
    matchLabels:
      kubevirt.io/size: large
  domain:
    resources:
      requests:
        memory: 1Gi
---
apiVersion: kubevirt.io/v1alpha1
kind: OfflineVirtualMachine
metadata:
  name: ubuntu
spec:
  running: true
  selector:
    matchLabels:
      guest: ubuntu
  template:
    metadata:
      labels:
        guest: ubuntu
        kubevirt.io/size: large
    spec:
      domain:
        devices:
          disks:
            - name: ubuntu
              volumeName: ubuntu
              disk:
                bus: virtio
      volumes:
        - name: ubuntu
          claimName: ubuntu1710
