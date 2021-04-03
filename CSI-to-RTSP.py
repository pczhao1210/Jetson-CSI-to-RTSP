import sys
import gi
import os
import logging
logging.basicConfig(level=logging.DEBUG)

gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GObject, GLib

loop = GLib.MainLoop()
Gst.init(None)

class USBtoRtspMediaFactory(GstRtspServer.RTSPMediaFactory):
    def __init__(self):
        self.videoPipeline = os.getenv('VIDEO_PIPELINE')
        if self.videoPipeline is None:
            self.videoPipeline = "nvarguscamerasrc ! video/x-raw(memory:NVMM) ! nvv4l2h264enc ! h264parse ! rtph264pay name=pay0"

        GstRtspServer.RTSPMediaFactory.__init__(self)

    def do_create_element(self, url):
        logging.info("Video pipeline to be used: {0}".format(self.videoPipeline)) 
        return Gst.parse_launch(self.videoPipeline)

class GstreamerRtspServer():
    def __init__(self):
        self.rtspServer = GstRtspServer.RTSPServer()
        factory = USBtoRtspMediaFactory()
        factory.set_shared(True)
        mountPoints = self.rtspServer.get_mount_points()
        mountPoints.add_factory("/stream1", factory)
        self.rtspServer.attach(None)

if __name__ == '__main__':
    s = GstreamerRtspServer()
    loop.run()
