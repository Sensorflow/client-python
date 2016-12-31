# Protocol Buffers Stream python client

Example
-------

```python
sfm = SensorflowSerialMessenger()
import time
time.sleep(2) # If you have to wait for your devices
print(sfm.ping())
for i in range(3):
    r = sfm.notification()
    print("NOTIFICATION TYPE", r.what)

for i in sfm.read_all():
    print(i.name, [i for i in i.values])

r = sfm.read("MySensor")
print(r.name)
print([i for i in r.values])

```
