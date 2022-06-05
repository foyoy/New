

import time
import os
from decimal import *
from os.path import sep as pathSep
try:
    import plyer
except:
    pass
try:
    import android
except:
    pass

from time import sleep
from kivymd.app import MDApp
from kivymd.toast import toast
from kivy.uix.popup import Popup
from kivymd.uix.behaviors import TouchBehavior
#from kivymd2.uix.filemanager import MDFileManager
import sys
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import (
    NumericProperty,
    StringProperty,
    BooleanProperty,
    OptionProperty,
    ListProperty,
    ObjectProperty,
)
from kivy.metrics import dp
from kivy.metrics import sp
from kivymd.theming import ThemableBehavior

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager,Screen,WipeTransition,FadeTransition,FallOutTransition,RiseInTransition,CardTransition        

from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.metrics import dp
from kivymd.uix.spinner import MDSpinner
from kivy.core.window import Window
from kivy.setupconfig import USE_SDL2
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.core.clipboard import Clipboard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd import images_path
from kivymd.uix.label import MDLabel
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivy.properties import (
    BoundedNumericProperty,
    ListProperty,
    OptionProperty,
    ReferenceListProperty,
)
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

from kivymd.color_definitions import hue, palette, text_colors


import requests
import time
import shutil
import threading

from kivy.clock import mainthread
from kivy.utils import platform


from datetime import datetime
from datetime import date, timedelta
import os

###################################
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton, MDRoundFlatIconButton, MDRectangleFlatButton, MDFloatingActionButton
from kivymd.uix.progressbar import MDProgressBar
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import sp
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManagerException

from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularElevationBehavior

from kivymd.uix.list import OneLineAvatarIconListItem
################################################################


__all__ = ("BackgroundColorBehavior", "SpecificBackgroundColorBehavior")

from kivy.lang import Builder
from kivy.properties import (
    BoundedNumericProperty,
    ListProperty,
    OptionProperty,
    ReferenceListProperty,
)
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

from kivymd.color_definitions import hue, palette, text_colors

import os
worm = os.getcwd()+pathSep
Window.softinput_mode = "below_target"

###############CAMARA##################
from kivy.event import EventDispatcher
from kivy.graphics.texture import Texture
from kivy.graphics import Fbo, Callback, Rectangle
from kivy.properties import (BooleanProperty, StringProperty, ObjectProperty, OptionProperty, ListProperty)
from kivy.clock import Clock

from jnius import autoclass, cast, PythonJavaClass, java_method, JavaClass, MetaJavaClass, JavaMethod

import logging
from enum import Enum

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
try:
    CameraManager = autoclass("android.hardware.camera2.CameraManager")
    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    Context = autoclass("android.content.Context")
    context = cast("android.content.Context", PythonActivity.mActivity)
except Exception as e:
    print(str(e))

try:
    CameraDevice = autoclass("android.hardware.camera2.CameraDevice")
    CaptureRequest = autoclass("android.hardware.camera2.CaptureRequest")
    CameraCharacteristics = autoclass("android.hardware.camera2.CameraCharacteristics")
except Exception as e:
    print(str(e))

ArrayList = autoclass('java.util.ArrayList')
JavaArray = autoclass('java.lang.reflect.Array')

try:
    SurfaceTexture = autoclass('android.graphics.SurfaceTexture')
    Surface = autoclass('android.view.Surface')
    GL_TEXTURE_EXTERNAL_OES = autoclass(
        'android.opengl.GLES11Ext').GL_TEXTURE_EXTERNAL_OES
    ImageFormat = autoclass('android.graphics.ImageFormat')
except Exception as e:
    print(str(e))


try:
    Handler = autoclass("android.os.Handler")
    Looper = autoclass("android.os.Looper")
except Exception as e:
    print(str(e))


try:
    MyStateCallback = autoclass("net.inclem.camera2.MyStateCallback")
    CameraActions = autoclass("net.inclem.camera2.MyStateCallback$CameraActions")
    # MyStateCallback = autoclass("org.kivy.android.MyStateCallback")

    MyCaptureSessionCallback = autoclass("net.inclem.camera2.MyCaptureSessionCallback")
    CameraCaptureEvents = autoclass("net.inclem.camera2.MyCaptureSessionCallback$CameraCaptureEvents")

    _global_handler = Handler(Looper.getMainLooper())

except Exception as e:
    print(str(e))
    
class LensFacing(Enum):
    """Values copied from CameraCharacteristics api doc, as pyjnius
    lookup doesn't work on some devices.
    """
    LENS_FACING_FRONT = 0
    LENS_FACING_BACK = 1
    LENS_FACING_EXTERNAL = 2

class ControlAfMode(Enum):
    CONTROL_AF_MODE_CONTINUOUS_PICTURE = 4

class ControlAeMode(Enum):
    CONTROL_AE_MODE_ON = 1

class Runnable(PythonJavaClass):
    __javainterfaces__ = ['java/lang/Runnable']

    def __init__(self, func):
        super(Runnable, self).__init__()
        self.func = func

    @java_method('()V')
    def run(self):
        try:
            self.func()
        except:
            import traceback
            traceback.print_exc()


class PyCameraInterface(EventDispatcher):
    """
    Provides an API for querying details of the cameras available on Android.
    """

    camera_ids = []

    cameras = ListProperty()

    java_camera_characteristics = {}

    java_camera_manager = ObjectProperty()

    def __init__(self):
        super().__init__()
        logger.info("Starting camera interface init")
        self.java_camera_manager = cast("android.hardware.camera2.CameraManager",
                                    context.getSystemService(Context.CAMERA_SERVICE))

        self.camera_ids = self.java_camera_manager.getCameraIdList()
        characteristics_dict = self.java_camera_characteristics
        camera_manager = self.java_camera_manager
        logger.info("Got basic java objects")
        for camera_id in self.camera_ids:
            logger.info(f"Getting data for camera {camera_id}")
            characteristics_dict[camera_id] = camera_manager.getCameraCharacteristics(camera_id)
            logger.info("Got characteristics dict")

            self.cameras.append(PyCameraDevice(
                camera_id=camera_id,
                java_camera_manager=camera_manager,
                java_camera_characteristics=characteristics_dict[camera_id],
            ))
            logger.info(f"Finished interpreting camera {camera_id}")

    def select_cameras(self, **conditions):
        options = self.cameras
        outputs = []
        for camera in cameras:
            for key, value in conditions.items():
                if getattr(camera, key) != value:
                    break
            else:
                outputs.append(camera)

        return outputs

class PyCameraDevice(EventDispatcher):

    camera_id = StringProperty()

    output_texture = ObjectProperty(None, allownone=True)

    preview_active = BooleanProperty(False)
    preview_texture = ObjectProperty(None, allownone=True)
    preview_resolution = ListProperty()
    preview_fbo = ObjectProperty(None, allownone=True)
    java_preview_surface_texture = ObjectProperty(None)
    java_preview_surface = ObjectProperty(None)
    java_capture_request = ObjectProperty(None)
    java_surface_list = ObjectProperty(None)
    java_capture_session = ObjectProperty(None)

    connected = BooleanProperty(False)

    supported_resolutions = ListProperty()
    # TODO: populate this

    facing = OptionProperty("UNKNOWN", options=["UNKNOWN", "FRONT", "BACK", "EXTERNAL"])

    java_camera_characteristics = ObjectProperty()
    java_camera_manager = ObjectProperty()
    java_camera_device = ObjectProperty()
    java_stream_configuration_map = ObjectProperty()

    _open_callback = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_opened")
        self.register_event_type("on_closed")
        self.register_event_type("on_disconnected")
        self.register_event_type("on_error")

        self._java_state_callback_runnable = Runnable(self._java_state_callback)
        self._java_state_java_callback = MyStateCallback(self._java_state_callback_runnable)

        self._java_capture_session_callback_runnable = Runnable(self._java_capture_session_callback)
        self._java_capture_session_java_callback = MyCaptureSessionCallback(
            self._java_capture_session_callback_runnable)

        self._populate_camera_characteristics()

    def on_opened(self, instance):
        pass
    def on_closed(self, instance):
        pass
    def on_disconnected(self, instance):
        pass
    def on_error(self, instance, error):
        pass
    def close(self):
        self.java_camera_device.close()

    def _populate_camera_characteristics(self):
        logger.info("Populating camera characteristics")
        self.java_stream_configuration_map = self.java_camera_characteristics.get(
            CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP)
        logger.info("Got stream configuration map")

        self.supported_resolutions = [
            (size.getWidth(), size.getHeight()) for size in
            self.java_stream_configuration_map.getOutputSizes(SurfaceTexture(0).getClass())]
        logger.info("Got supported resolutions")

        facing = self.java_camera_characteristics.get(
            CameraCharacteristics.LENS_FACING)
        logger.info(f"Got facing: {facing}")
        if facing == LensFacing.LENS_FACING_BACK.value:  # CameraCharacteristics.LENS_FACING_BACK:
            self.facing = "BACK"
        elif facing == LensFacing.LENS_FACING_FRONT.value:  # CameraCharacteristics.LENS_FACING_FRONT:
            self.facing = "FRONT"
        elif facing == LensFacing.LENS_FACING_EXTERNAL.value:  # CameraCharacteristics.LENS_FACING_EXTERNAL:
            self.facing = "EXTERNAL"
        else:
            raise ValueError("Camera id {} LENS_FACING is unknown value {}".format(self.camera_id, facing))
        logger.info(f"Finished initing camera {self.camera_id}")

    def __str__(self):
        return "<PyCameraDevice facing={}>".format(self.facing)
    def __repr__(self):
        return str(self)

    def open(self, callback=None):
        self._open_callback = callback
        self.java_camera_manager.openCamera(
            self.camera_id,
            self._java_state_java_callback,
            _global_handler
        )

    def _java_state_callback(self, *args, **kwargs):
        action = MyStateCallback.camera_action.toString()
        camera_device = MyStateCallback.camera_device

        self.java_camera_device = camera_device

        logger.info("CALLBACK: camera event {}".format(action))
        if action == "OPENED":
            self.dispatch("on_opened", self)
            self.connected = True
        elif action == "DISCONNECTED":
            self.dispatch("on_disconnected", self)
            self.connected = False
        elif action == "CLOSED":
            self.dispatch("on_closed", self)
            self.connected = False
        elif action == "ERROR":
            error = MyStateCallback.camera_error
            self.dispatch("on_error", self, error)
            self.connected = False
        elif action == "UNKNOWN":
            print("UNKNOWN camera state callback item")
            self.connected = False
        else:
            raise ValueError("Received unknown camera action {}".format(action))

        if self._open_callback is not None:
            self._open_callback(self, action)

    def start_preview(self, resolution):
        if self.java_camera_device is None:
            raise ValueError("Camera device not yet opened, cannot create preview stream")

        if resolution not in self.supported_resolutions:
            raise ValueError(
                "Tried to open preview with resolution {}, not in supported resolutions {}".format(
                    resolution, self.supported_resolutions))

        if self.preview_active:
            raise ValueError("Preview already active, can't start again without stopping first")

        logger.info("Creating capture stream with resolution {}".format(resolution))

        self.preview_resolution = resolution
        self._prepare_preview_fbo(resolution)
        self.preview_texture = Texture(
            width=resolution[0], height=resolution[1], target=GL_TEXTURE_EXTERNAL_OES, colorfmt="rgba")
        logger.info("Texture id is {}".format(self.preview_texture.id))
        self.java_preview_surface_texture = SurfaceTexture(int(self.preview_texture.id))
        self.java_preview_surface_texture.setDefaultBufferSize(*resolution)
        self.java_preview_surface = Surface(self.java_preview_surface_texture)

        self.java_capture_request = self.java_camera_device.createCaptureRequest(CameraDevice.TEMPLATE_PREVIEW)
        self.java_capture_request.addTarget(self.java_preview_surface)
        self.java_capture_request.set(
            CaptureRequest.CONTROL_AF_MODE, ControlAfMode.CONTROL_AF_MODE_CONTINUOUS_PICTURE.value)  # CaptureRequest.CONTROL_AF_MODE_CONTINUOUS_PICTURE)
        self.java_capture_request.set(
            CaptureRequest.CONTROL_AE_MODE, ControlAeMode.CONTROL_AE_MODE_ON.value)  # CaptureRequest.CONTROL_AE_MODE_ON)

        self.java_surface_list = ArrayList()
        self.java_surface_list.add(self.java_preview_surface)

        self.java_camera_device.createCaptureSession(
            self.java_surface_list,
            self._java_capture_session_java_callback,
            _global_handler,
        )

        return self.preview_fbo.texture

    def _prepare_preview_fbo(self, resolution):
        self.preview_fbo = Fbo(size=resolution)
        self.preview_fbo['resolution'] = [float(f) for f in resolution]
        self.preview_fbo.shader.fs = """
            #extension GL_OES_EGL_image_external : require
            #ifdef GL_ES
                precision highp float;
            #endif

            /* Outputs from the vertex shader */
            varying vec4 frag_color;
            varying vec2 tex_coord0;

            /* uniform texture samplers */
            uniform sampler2D texture0;
            uniform samplerExternalOES texture1;
            uniform vec2 resolution;

            void main()
            {
                gl_FragColor = texture2D(texture1, tex_coord0);
            }
        """
        with self.preview_fbo:
            Rectangle(size=resolution)

    def _java_capture_session_callback(self, *args, **kwargs):
        event = MyCaptureSessionCallback.camera_capture_event.toString()
        logger.info("CALLBACK: capture event {}".format(event))

        self.java_capture_session = MyCaptureSessionCallback.camera_capture_session

        if event == "READY":
            logger.info("Doing READY actions")
            self.java_capture_session.setRepeatingRequest(self.java_capture_request.build(), None, None)
            Clock.schedule_interval(self._update_preview, 0.)

    def _update_preview(self, dt):
        self.java_preview_surface_texture.updateTexImage()
        self.preview_fbo.ask_update()
        self.preview_fbo.draw()
        self.output_texture = self.preview_fbo.texture

#####################Main Camera#########################################

import time
import logging
from functools import partial
from enum import Enum

from kivy.app import App
from kivy.animation import Animation
from kivy import platform
from kivy.lang import Builder
from kivy.event import EventDispatcher
from kivy.properties import (
    ObjectProperty, StringProperty, ListProperty, BooleanProperty, NumericProperty, OptionProperty)
from kivy.graphics.texture import Texture
from kivy.graphics import Fbo, Callback, Rectangle
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.stencilview import StencilView
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

from colourswidget import ColourShaderWidget
from widgets import ColouredToggleButtonContainer, ColouredButton

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

#from camera2 import PyCameraInterface

try:
    from android.permissions import request_permission, check_permission, Permission
except Exception as e:
    print(str(e))
    
class PermissionRequestStates(Enum):
    UNKNOWN = "UNKNOWN"
    HAVE_PERMISSION = "HAVE_PERMISSION"
    DO_NOT_HAVE_PERMISSION = "DO_NOT_HAVE_PERMISSION"
    AWAITING_REQUEST_RESPONSE = "AWAITING_REQUEST_RESPONSE"

class OpenCameraButton(ColouredButton):
    active = BooleanProperty(False)
    def on_touch_down(self, touch):
        print("touch pos", touch.pos, self.collide_point(*touch.pos), self.active)
        if not self.active:
            return False
        return super().on_touch_down(touch)

class ColourBlindnessSelectionButton(ColouredToggleButtonContainer):
    has_red = BooleanProperty(True)
    has_green = BooleanProperty(True)
    has_blue = BooleanProperty(True)
    text = StringProperty()
    texture_size = ListProperty([0, 0])

class ScreenCamera(Screen): #FloatLayout
    buttons_visible = BooleanProperty(True)

    _buttons_visible_fraction = NumericProperty(1.0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.anim_to_1 = Animation(_buttons_visible_fraction=1.0, duration=0.5)
        self.anim_to_0 = Animation(_buttons_visible_fraction=0.0, duration=0.5)

    def hide_buttons(self):
        self.buttons_visible = False

    def show_buttons(self):
        self.buttons_visible = True

    def on_touch_down(self, touch):
        touch_consumed = super().on_touch_down(touch)
        if not touch_consumed:
            touch.ud["show_buttons"] = True

    def on_touch_up(self, touch):
        if touch.ud.get("show_buttons", False):
            self.buttons_visible = True
        return super().on_touch_up(touch)

    def on_buttons_visible(self, instance, value):
        Animation.cancel_all(self, "_buttons_visible_fraction")
        Animation(_buttons_visible_fraction=value, duration=0.45, t="out_cubic").start(self)

class CameraDisplayWidget(StencilView):
    texture = ObjectProperty(None, allownone=True)

    camera_resolution = ListProperty([1, 1]) #ListProperty([1, 1])

    resolution = ListProperty([1920, 1080]) #ListProperty([1, 1])

    tex_coords = ListProperty([0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0])
    correct_camera = BooleanProperty(False)

    _rect_pos = ListProperty([0, 0])
    _rect_size = ListProperty([1, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bind(
            pos=self._update_rect,
            size=self._update_rect,
            resolution=self._update_rect,
            texture=self._update_rect,
        )

    def on_correct_camera(self, instance, correct):
        print("Correct became", correct)
        if correct:
            self.tex_coords = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0]
            print("Set 0!")
        else:
            self.tex_coords = [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0]
            print("Set 1!")

    def on_tex_coords(self, instance, value):
        print("tex_coords became", self.tex_coords)

    def _update_rect(self, *args):
        self._update_rect_to_fill()

    def _update_rect_to_fit(self, *args):
        w, h = self.resolution
        aspect_ratio = h / w

        aspect_width = self.width
        aspect_height = self.width * h / w
        if aspect_height > self.height:
            aspect_height = self.height
            aspect_width = aspect_height * w / h

        aspect_height = int(aspect_height)
        aspect_width = int(aspect_width)

        self._rect_pos = [self.center_x - aspect_width / 2,
                          self.center_y - aspect_height / 2]

        self._rect_size = [aspect_width, aspect_height]

    def _update_rect_to_fill(self, *args):
        w, h = self.resolution

        aspect_ratio = h / w

        aspect_width = self.width
        aspect_height = self.width * h / w
        if aspect_height < self.height:
            aspect_height = self.height
            aspect_width = aspect_height * w / h

        aspect_height = int(aspect_height)
        aspect_width = int(aspect_width)

        self._rect_pos = [self.center_x - aspect_width / 2,
                          self.center_y - aspect_height / 2]

        self._rect_size = [aspect_width, aspect_height]

##############################################################
M="""
#:import HotReloadViewer kivymd2.utils.hot_reload_viewer.HotReloadViewer
#:import images_path kivymd.images_path
#:import MDApp kivymd.app
#:import MDTextField kivymd.uix.textfield
#:import toast kivymd.toast.toast

Screen:
    id: BG
##    canvas.before:
##        Color:
##            rgba: [1,1,1,1]
##        Rectangle:
##            pos: self.pos
##            size: self.size
##            source: app.BG
    ScreenManager:
        id: MainActivity
        Screen:
            id: SecondActivity
            name: "main"
            
            BoxLayout:
                HotReloadViewer:
                    id: jbsidis_jbsidis
                    size_hint_x: .3
                    path: app.pax
                    errors: True
                    errors_text_color: 1, 1, 0, 1
                    errors_background_color: app.theme_cls.bg_dark
##            FloatLayout:
##                ScatterLayout:
##                    CardView2:
##                        pos_hint: {"center_x": .5, "center_y": .3}


                     
<CardView2>:
    BoxLayout:
        padding: dp(20),dp(100)
        spacing: dp(20)
        orientation: "vertical"
        #pos_hint: {'center_x':.5, 'center_y':.7}
        
        MDCard:
            border_radius: "20dp"
            size_hint: (1, None)
            height: dp(250)
            padding: dp(10)
            spacing: dp(10)
            #pos_hint: {"center_x": .5, "center_y": .5}
            orientation: "vertical"
            BoxLayout:
                spacing: dp(0)
                size_hint: (.6, .3)
                FloatLayout:
                    MDIconButton:
                        id: bcx
                        pos_hint: {"center_x": .2, "center_y": .5}
                        icon: "material-design"
                AnchorLayout:
                    MDTextButton: #MDLabel:
                        id: stq
                        #size_hint: (None, 1)
                        pos_hint: {"center_x": .2, "center_y": .5}
                        markup: True
                        text: "[b]              KV Lang:"
            TextInput:
                id: sy_
                background_color: [0,0,0,0]
                foreground_color: [0,0,0,1]
                markup: True
                text: open("jbsidis.py").read()
        FloatLayout:
            MDFloatingActionButton:
                pos_hint: {"center_x": .9, "center_y": .5}
                icon: "send"
                text_color: [1,1,1,1]
                md_bg_color: [1,0,0,1]
                on_release:
                    root.eee(root.ids.sy_.text)
"""

from kivymd.uix.bottomnavigation import MDBottomNavigationBar

class Bx2(MDBottomNavigationBar):
    pass
class Bix(MDBottomNavigationBar):
    pass

from kivymd.uix.imagelist import SmartTileWithLabel
class I(BoxLayout): #ColourShaderWidget
    filter=StringProperty("none")
    source1=StringProperty()
    box_color1=ListProperty()
    text1=StringProperty()
    #source1": N,"box_color1": [.42,.05,.6,.6],"text1
class I2(BoxLayout): #ColourShaderWidget
    filter=StringProperty("none")
    source1=StringProperty()
    source=StringProperty()
    box_color1=ListProperty()
    text1=StringProperty()
    #source1": N,"box_color1": [.42,.05,.6,.6],"text1

#ABOUT
class showAbout(BoxLayout):
    pass

#REFERENCE NORMAL IMAGE
class I22(BoxLayout): #ColourShaderWidget
    source=StringProperty()

#RV RESULT
class RV(BoxLayout):
    s=StringProperty()

class Boxa(BoxLayout):
    pass

class CardView2(BoxLayout):
    def eee(self,a):
        try:
            M=open("jbsidis.py","w")
            M.write(a)
            M.close()
        except Exception as e:
            toast(str(e))
    pass

class ImageManager(BoxLayout):
    filter=StringProperty()
    pass

class L(FloatLayout):
    s=StringProperty()

class K(FloatLayout):
    s=StringProperty()

class ImageManagerx(BoxLayout):
    filter=StringProperty()
    pass
class Kulife(MDApp):
    dialog = None
    dialog_test = None
    texture = ObjectProperty(None, allownone=True)
    camera_resolution = ListProperty([1920, 1080])
    current_camera = ObjectProperty(None, allownone=True)
    cameras_to_use = ListProperty()
    camera_permission_state = OptionProperty(
        PermissionRequestStates.UNKNOWN,
        options=[PermissionRequestStates.UNKNOWN,
                 PermissionRequestStates.HAVE_PERMISSION,
                 PermissionRequestStates.DO_NOT_HAVE_PERMISSION,
                 PermissionRequestStates.AWAITING_REQUEST_RESPONSE])
    _camera_permission_state_string = StringProperty("UNKNOWN")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title="Kulife App"
        self.pax="jbsidis.py.txt"
        self.manager_list = []
        self.dir = os.getcwd()+"/images/"
        self.available_image_format = ['.png', '.jpg', '.jpeg', '.webp']
        self.Bx2=None
        self.Bix=None
        self.test=""
        Window.bind(on_keyboard=self.Android_back_click)

    def Android_back_click(self,window,key,*largs):
        if key == 27:
            app.exit_dialog()
            return True

    def exit_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Are you sure you want to exit the App?",
                auto_dismiss=False,
                buttons=[
                    MDFlatButton(
                        text="No",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.cexit_dialog,
                    ),
                    MDFlatButton(
                        text="Yes",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_application,
                    ),
                ],
            )
        self.dialog.open()

    def cexit_dialog(self, obj):
        self.dialog.dismiss(force=True)

    def close_application(self, obj):
        App.get_running_app().stop()
        Window.close()

    def homex(self):
        app.root.ids.s56.cols=2
        app.add4cameras("q.jpeg")

    def K(self):
        return K()

    def mex(self,A):
        if str(A.children).find("K")>-1:
            A.remove_widget(A.children[0])
    def on_camera_permission_state(self, instance, state):
        self._camera_permission_state_string = state.value
    def i8(self,a):
        app.root.ids.fox.text=str(a)
    def build(self):
        global app
        global test
        global Bx2
        global Bix
        self.theme_cls.theme_style = "Light"

        self.i = 0

        self.restart_btn = MDFloatingActionButton(
            icon="restart",
            pos_hint = {'x': .88, 'y': .1},
            on_release= self.show_toast
        )

        self.plbl = MDLabel(
            text="Protanopia",
            font_style="Subtitle2",
            theme_text_color= "Custom",
            text_color= (0, 0, 0, 1),
            pos_hint = {'center_x': .58, 'center_y': .85}
        )

        self.dlbl = MDLabel(
            text="Deuteranopia",
            font_style="Subtitle2",
            theme_text_color= "Custom",
            text_color= (0, 0, 0, 1),
            pos_hint = {'center_x': .55, 'center_y': .65}
        )

        self.tlbl = MDLabel(
            text="Tritanopia",
            font_style="Subtitle2",
            theme_text_color= "Custom",
            text_color= (0, 0, 0, 1),
            pos_hint = {'center_x': .58, 'center_y': .45}
        )

        self.mlbl = MDLabel(
            text="Monochromacy",
            font_style="Subtitle2",
            theme_text_color= "Custom",
            text_color= (0, 0, 0, 1),
            pos_hint = {'center_x': .55, 'center_y': .25}
        )

        self.p_percentlbl = MDLabel(
            text="",
            theme_text_color= "Custom",
            text_color= (0, 0, 0, 1),
            font_style="Subtitle2",
            pos_hint = {'x': .89, 'center_y': .85}
        )

        self.d_percentlbl = MDLabel(
            text="",
            theme_text_color= "Custom",
            text_color= (0, 0, 0, 1),
            font_style="Subtitle2",
            pos_hint = {'x': .89, 'center_y': .65}
        )

        self.t_percentlbl = MDLabel(
            text="",
            theme_text_color= "Custom",
            text_color= (0, 0, 0, 1),
            font_style="Subtitle2",
            pos_hint = {'x': .89, 'center_y': .45}
        )

        self.m_percentlbl = MDLabel(
            text="",
            theme_text_color= "Custom",
            text_color= (0, 0, 0, 1),
            font_style="Subtitle2",
            pos_hint = {'x': .89, 'center_y': .25}
        )

        self.pProgress = MDProgressBar(
            max=100,
            value=0,
            pos_hint = {'center_x': .5, 'center_y': .85},
            size_hint_x= .5
        )

        self.dProgress = MDProgressBar(
            max=100,
            value=0,
            pos_hint = {'center_x': .5, 'center_y': .65},
            size_hint_x= .5
        )

        self.tProgress = MDProgressBar(
            max=100,
            value=0,
            pos_hint = {'center_x': .5, 'center_y': .45},
            size_hint_x= .5
        )

        self.mProgress = MDProgressBar(
            max=100,
            value=0,
            pos_hint = {'center_x': .5, 'center_y': .25},
            size_hint_x= .5
        )

        self.spin = MDProgressBar(
            value = 0,
            color = get_color_from_hex("##B22222"),
            size_hint_x= .6,
            pos_hint = {'center_x': .5, 'center_y': .55},
        )

        self.spinlbl = MDLabel(
            text="",
            theme_text_color= "Custom",
            text_color= (0, 0, 0, 1),
            font_style="H6",
            halign="center"
        )

        app=MDApp.get_running_app()

        try:
            self.camera_interface = PyCameraInterface()

            Clock.schedule_interval(self.update, 0)

            self.debug_print_camera_info()

            self.inspect_cameras()

            self.restart_stream()
        except Exception as e:
            print(str(e))
        Clock.schedule_once(lambda x: app.attempt_stream_camera(app.cameras_to_use[0]),5)
        return Builder.load_file("jbsidis.py.txt")

    def on_stop(self):
        pass

    def barra(self):
        f=app.root.children
        t=f[0]
        print(t.children)
        
        if str(t.children).find("Bx2")>-1 and app.root.ids.J.current=="test":
            f[0].remove_widget(f[0].children[0])
            f[0].add_widget(Bix())
            return 0
        if str(t.children).find("Bix")>-1 and app.root.ids.J.current=="cax":
            f[0].remove_widget(f[0].children[0])
            f[0].add_widget(Bx2())
            return 0
        if str(t.children).find("Bx2")>-1 and app.root.ids.J.current=="theme":
            f[0].remove_widget(f[0].children[0])
            f[0].add_widget(Bix())
            return 0

    def pop_ref(self, image):
        pop = Popup(
            title='Reference', 
            content=Image(source=image),
            size_hint=(None, None), 
            size=(600, 600)
        )
        pop.open()


    def testInstruction(self):
        toast('Loading Test...')
        Clock.schedule_once(self.show_dialog, 5)

    
    def show_dialog(self, *args):
        if not self.dialog_test:
            self.dialog_test = MDDialog(
                title = "Before taking the test",
                #width_offset = dp(70),
                size_hint= (.8, None),
                text = "[b]Remove all glasses with colored lenses:[/b] Taking this test with only your prescription lenses or naked eye will provide you with the most accurate results. Wearing a colored lens can make your results inaccurate.\n\n[b]Turn up your screen brightness:[/b] Brighter colors are easier to perceive.\n\n[b]Test Format:[/b] You will see a series of image, these are normal, protanopia, deuteranopia, tritanopia. You will also see a reference button, which located at the bottom right corner. Tap the image to match the reference image corresponding on which image you see.",
                auto_dismiss=False,
                buttons = [
                    MDRoundFlatIconButton(
                        text="Start",
                        icon="play-circle-outline",
                        on_release = self.close_dialog,
                    ),
                ],
            )

        self.dialog_test.open()

    def close_dialog(self, obj):
        self.dialog_test.dismiss(force=True)
        app.show_toast(2)

    def show_toast(self, obj):
        app.root.ids.fl.remove_widget(self.restart_btn)
        app.root.ids.fl.remove_widget(self.plbl)
        app.root.ids.fl.remove_widget(self.dlbl)
        app.root.ids.fl.remove_widget(self.tlbl)
        app.root.ids.fl.remove_widget(self.mlbl)
        app.root.ids.fl.remove_widget(self.pProgress)
        app.root.ids.fl.remove_widget(self.dProgress)
        app.root.ids.fl.remove_widget(self.tProgress)
        app.root.ids.fl.remove_widget(self.mProgress)
        app.root.ids.fl.remove_widget(self.p_percentlbl)
        app.root.ids.fl.remove_widget(self.d_percentlbl)
        app.root.ids.fl.remove_widget(self.t_percentlbl)
        app.root.ids.fl.remove_widget(self.m_percentlbl)
        toast('Getting Ready...')

        Clock.schedule_once(lambda x: self.visiontest(1), 1)
        
    def visiontest(self,A):
        M = app.root.ids.rv5
        M.data = []

        if A == 2:
            self.anim = Clock.schedule_interval(lambda x: self.loader(2), 0.1)
            app.root.ids.fl.add_widget(self.spin)
            app.root.ids.fl.add_widget(self.spinlbl)
        if A==3:
            a1=[str(app.test).count("@@protanopia")]
            a2=[str(app.test).count("@@deuteranopia")]
            a3=[str(app.test).count("@@tritanopia")]
            a4=[str(app.test).count("@@monochromacy")]

            a1ToStr = ' '.join(map(str, a1))
            a2ToStr = ' '.join(map(str, a2))
            a3ToStr = ' '.join(map(str, a3))
            a4ToStr = ' '.join(map(str, a4))

            a1ToInt = int(a1ToStr) * 10
            a2ToInt = int(a2ToStr) * 10
            a3ToInt = int(a3ToStr) * 10
            a4ToInt = int(a4ToStr) * 10

            self.pProgress.value = a1ToInt
            self.dProgress.value = a2ToInt
            self.tProgress.value = a3ToInt
            self.mProgress.value = a4ToInt

            self.p_percentlbl.text = str(a1ToInt) + "%"
            self.d_percentlbl.text = str(a2ToInt) + "%"
            self.t_percentlbl.text = str(a3ToInt) + "%"
            self.m_percentlbl.text = str(a4ToInt) + "%"
            
            app.root.ids.fl.remove_widget(self.spin)
            app.root.ids.fl.remove_widget(self.spinlbl)

            app.root.ids.fl.add_widget(self.plbl)
            app.root.ids.fl.add_widget(self.pProgress)
            app.root.ids.fl.add_widget(self.p_percentlbl)
    
            app.root.ids.fl.add_widget(self.dlbl)
            app.root.ids.fl.add_widget(self.dProgress)
            app.root.ids.fl.add_widget(self.d_percentlbl)

            app.root.ids.fl.add_widget(self.tlbl)
            app.root.ids.fl.add_widget(self.tProgress)
            app.root.ids.fl.add_widget(self.t_percentlbl)

            app.root.ids.fl.add_widget(self.mlbl)
            app.root.ids.fl.add_widget(self.mProgress)
            app.root.ids.fl.add_widget(self.m_percentlbl)
            app.root.ids.fl.add_widget(self.restart_btn)

            app.test = ""
            
        if A==1:
            f = os.listdir("images/")

            n1 = "images/Normal/n.jpg"
            p1 = "images/Protanopia/p.png"
            d1 = "images/Deuteranopia/d.png"
            t1 = "images/Tritanopia/t.png"
            m1 = "images/Monochromacy/m.png"

            n2 = "images/Normal/nn.jpg"
            p2 = "images/Protanopia/pp.png"
            d2 = "images/Deuteranopia/dd.png"
            t2 = "images/Tritanopia/tt.png"
            m2 = "images/Monochromacy/mm.png"

            n3 = "images/Normal/nnn.jpg"
            p3 = "images/Protanopia/ppp.png"
            d3 = "images/Deuteranopia/ddd.png"
            t3 = "images/Tritanopia/ttt.png"
            m3 = "images/Monochromacy/mmm.png"

            n4 = "images/Normal/nnnn.jpg"
            p4 = "images/Protanopia/pppp.png"
            d4 = "images/Deuteranopia/dddd.png"
            t4 = "images/Tritanopia/tttt.png"
            m4 = "images/Monochromacy/mmmm.png"

            n5 = "images/Normal/nnnnn.jpg"
            p5 = "images/Protanopia/ppppp.png"
            d5 = "images/Deuteranopia/ddddd.png"
            t5 = "images/Tritanopia/ttttt.png"
            m5 = "images/Monochromacy/mmmmm.png"

            n6 = "images/Normal/nnnnnn.jpg"
            p6 = "images/Protanopia/pppppp.png"
            d6 = "images/Deuteranopia/dddddd.png"
            t6 = "images/Tritanopia/tttttt.png"
            m6 = "images/Monochromacy/mmmmmm.png"

            n7 = "images/Normal/n7.jpg"
            p7 = "images/Protanopia/p7.png"
            d7 = "images/Deuteranopia/d7.png"
            t7 = "images/Tritanopia/t7.png"
            m7 = "images/Monochromacy/m7.png"

            n8 = "images/Normal/n8.jpg"
            p8 = "images/Protanopia/p8.png"
            d8 = "images/Deuteranopia/d8.png"
            t8 = "images/Tritanopia/t8.png"
            m8 = "images/Monochromacy/m8.png"

            n9 = "images/Normal/n9.jpg"
            p9 = "images/Protanopia/p9.png"
            d9 = "images/Deuteranopia/d9.png"
            t9 = "images/Tritanopia/t9.png"
            m9 = "images/Monochromacy/m9.png"

            n10 = "images/Normal/n10.jpg"
            p10 = "images/Protanopia/p10.png"
            d10 = "images/Deuteranopia/d10.png"
            t10 = "images/Tritanopia/t10.png"
            m10 = "images/Monochromacy/m10.png"

            Clock.schedule_once(lambda x: app.test00(n1, p1, d1, t1, m1), 8)
            Clock.schedule_once(lambda x: app.test00(n2, p2, d2, t2, m2), 16)
            Clock.schedule_once(lambda x: app.test00(n3, p3, d3, t3, m3), 24)
            Clock.schedule_once(lambda x: app.test00(n4, p4, d4, t4, m4), 32)
            Clock.schedule_once(lambda x: app.test00(n5, p5, d5, t5, m5), 40)
            Clock.schedule_once(lambda x: app.test00(n6, p6, d6, t6, m6), 48)
            Clock.schedule_once(lambda x: app.test00(n7, p7, d7, t7, m7), 56)
            Clock.schedule_once(lambda x: app.test00(n8, p8, d8, t8, m8), 64)
            Clock.schedule_once(lambda x: app.test00(n9, p9, d9, t9, m9), 72)
            Clock.schedule_once(lambda x: app.test00(n10, p10, d10, t10, m10), 80)
            Clock.schedule_once(lambda x: app.visiontest(2), 88)

    def test00(self, n, p ,d ,t, m):
        M=app.root.ids.rv5

        
        listOfImages=[
            {"viewclass": "I2", "source1": p, "type": "protanopia"},
            {"viewclass": "I2", "source1": d, "type": "deuteranopia"},
            {"viewclass": "I2", "source1": t, "type": "tritanopia"},
            {"viewclass": "I2", "source1": m, "type": "monochromacy"},
        ]
        new_listOfImages = []

        while len(listOfImages) > 0:
            for t in listOfImages:
                new_listOfImages = new_listOfImages+[t]
            if len(new_listOfImages) == 4:
                break

        M.data=[]
        M.data.append(listOfImages[0])
        M.data.append(listOfImages[1])
        M.data.append(listOfImages[2])
        M.data.append(listOfImages[3])
        if self.i == 0:
            self.float_btn = MDFloatingActionButton(
                icon="image",
                pos_hint={'x': .88, 'y': .1},
                on_release= lambda x: app.pop_ref(n)
            )
            app.root.ids.fl.add_widget(self.float_btn)

    def loader(self, *args):
        self.i += 2
        self.spin.value = self.i
        self.spinlbl.text = str(self.i) + "%" 

        if self.i == 100:
            #self.i = 0
            self.anim.cancel()
            self.i = 0         
            Clock.schedule_once(lambda x: app.visiontest(3), 1)
        

    def switchTheme(self, switchObect, switchValue):
        if switchValue:
            self.theme_cls.theme_style = "Dark"
            self.plbl.text_color = 1, 1, 1, 1
            self.dlbl.text_color = 1, 1, 1, 1
            self.tlbl.text_color = 1, 1, 1, 1
            self.mlbl.text_color = 1, 1, 1, 1
            self.p_percentlbl.text_color = 1, 1, 1, 1
            self.d_percentlbl.text_color = 1, 1, 1, 1
            self.t_percentlbl.text_color = 1, 1, 1, 1
            self.m_percentlbl.text_color = 1, 1, 1, 1
            self.spinlbl.text_color = 1, 1, 1, 1
            app.root.ids.theme.text_color = 1, 1, 1, 1
        else:
            self.theme_cls.theme_style = "Light"
            self.plbl.text_color = 0, 0, 0, 1
            self.dlbl.text_color = 0, 0, 0, 1
            self.tlbl.text_color = 0, 0, 0, 1
            self.mlbl.text_color = 0, 0, 0, 1
            self.p_percentlbl.text_color = 0, 0, 0, 1
            self.d_percentlbl.text_color = 0, 0, 0, 1
            self.t_percentlbl.text_color = 0, 0, 0, 1
            self.m_percentlbl.text_color = 0, 0, 0, 1
            self.spinlbl.text_color = 0, 0, 0, 1
            app.root.ids.theme.text_color = 0, 0, 0, 1
##

    def inspect_cameras(self):
        cameras = self.camera_interface.cameras

        for camera in cameras:
            if camera.facing == "BACK":
                self.cameras_to_use.append(camera)
        for camera in cameras:
            if camera.facing == "FRONT":
                self.cameras_to_use.append(camera)

    def rotate_cameras(self):
        self.ensure_camera_closed()
        self.cameras_to_use = self.cameras_to_use[1:] + [self.cameras_to_use[0]]
        self.attempt_stream_camera(self.cameras_to_use[0])

    def restart_stream(self):
        self.ensure_camera_closed()
        Clock.schedule_once(self._restart_stream, 0)

    def _restart_stream(self, dt):
        logger.info("On restart, state is {}".format(self.camera_permission_state))
        if self.camera_permission_state in (PermissionRequestStates.UNKNOWN, PermissionRequestStates.HAVE_PERMISSION):
            self.attempt_stream_camera(self.cameras_to_use[0])
        else:
            logger.warning(
                "Did not attempt to restart camera stream as state is {}".format(self.camera_permission_state))

    def debug_print_camera_info(self):
        cameras = self.camera_interface.cameras
        camera_infos = ["Camera ID {}, facing {}".format(c.camera_id, c.facing) for c in cameras]
        for camera in cameras:
            print("Camera ID {}, facing {}, resolutions {}".format(
                camera.camera_id, camera.facing, camera.supported_resolutions))

    def stream_camera_index(self, index):
        self.attempt_stream_camera(self.camera_interface.cameras[index])

    def attempt_stream_camera(self, camera):
        """Start streaming from the given camera, if we have the CAMERA
        permission, otherwise request the permission first.
        """

        if check_permission(Permission.CAMERA):
            self.stream_camera(camera)
        else:
            self.camera_permission_state = PermissionRequestStates.AWAITING_REQUEST_RESPONSE
            request_permission(Permission.CAMERA, partial(self._request_permission_callback, camera))

    def _request_permission_callback(self, camera, permissions, alloweds):
        # Assume  that we  received info  about exactly  1 permission,
        # since we only ever ask for CAMERA
        allowed = alloweds[0]

        if allowed:
            self.camera_permission_state = PermissionRequestStates.HAVE_PERMISSION
            self.stream_camera(camera)
        else:
            self.camera_permission_state = PermissionRequestStates.DO_NOT_HAVE_PERMISSION
            print("PERMISSION FORBIDDEN")

    def stream_camera(self, camera):
        resolution = self.select_resolution(Window.size, camera.supported_resolutions, best=(1920, 1080))
        if resolution is None:
            logger.error(f"Found no good resolution in {camera.supported_resolutions} for Window.size {Window.size}")
            return
        else:
            logger.info(f"Chose resolution {resolution} from choices {camera.supported_resolutions}")
        self.camera_resolution = resolution
        camera.open(callback=self._stream_camera_open_callback)

    def _stream_camera_open_callback(self, camera, action):
        if action == "OPENED":
            logger.info("Camera opened, preparing to start preview")
            Clock.schedule_once(partial(self._stream_camera_start_preview, camera), 0)
        else:
            logger.info("Ignoring camera event {action}")

    def sss(self):
        import time
        ss=str(time.strftime("%d%m%Y %H%M%S"))
        app.root.ids.J.get_screen("cax").ids.cdw.export_to_png("images/"+ss+".png")
        app.root.ids.J.current="test"

    def _stream_camera_start_preview(self, camera, *args):
        logger.info("Starting preview of camera {camera}")
        if camera.facing == "FRONT":
            app.root.ids.J.get_screen("cax").ids.cdw.correct_camera = True
        else:
            app.root.ids.J.get_screen("cax").ids.cdw.correct_camera = False
        self.texture = camera.start_preview(tuple(self.camera_resolution))

        self.current_camera = camera

    def select_resolution(self, window_size, resolutions, best=None):
        if best in resolutions:
            return best

        if not resolutions:
            return None

        win_x, win_y = window_size
        larger_resolutions = [(x, y) for (x, y) in resolutions if (x > win_x and y > win_y)]

        if larger_resolutions:
            return min(larger_resolutions, key=lambda r: r[0] * r[1])

        smaller_resolutions = resolutions  # if we didn't find one yet, all are smaller than the requested Window size
        return max(smaller_resolutions, key=lambda r: r[0] * r[1])

    def on_texture(self, instance, value):
        print("App texture changed to {}".format(value))

    def update(self, dt):
        self.root.canvas.ask_update()

    def ensure_camera_closed(self):
        if self.current_camera is not None:
            self.current_camera.close()
            self.current_camera = None

    def on_pause(self):

        logger.info("Closing camera due to pause")
        self.ensure_camera_closed()

        return super().on_pause()

    def on_resume(self):
        logger.info("Opening camera due to resume")
        self.restart_stream()
        ######################################################
Kulife().run()
