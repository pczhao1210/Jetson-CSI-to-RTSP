# Jetson-CSI-to-RTSP
A python script allows you to capture from CSI camera (e.g. Pi Camera V2 IMX219) and act as RTSP server on Jetson Devices.

Modified from Microsoft Live Video Analytics - Utilities - USB-to-RTSP.py

## Playback USB Camera Stream Over RTSP
Out of many options, we are using VLC player to play the USB camera stream.

On the VLC menu, click on the following:

```
Media --> Open Network Stream
```

Enter the following address:

```
rtsp://127.0.0.1/stream1
```
or
```
rtsp://{your Jetson Device IP}/stream1
```


The live USB camera stream will start playing on VLC.

## LVA Integration
To use the USB camera stream in LVA, first make sure that the Docker container is accessible by LVA (i.e., your IoT Edge device has access to the container). Then, in your deployment manifest file, update the following:

```json
"name": "rtspUrl",
"value": "rtsp://<YOUR_IP_ADDRESS>/stream1"
```

Enjoy!
