from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import json
import irsdk

class Telemtry:
    def __init__(self):
        self.current = {
            "gear": 0,
            "flags": 0,
            "brake_bias": 0,
            "track_temp": 0,
            "abs_active": 0,
            "pit_lim_active": 0,
        }
        self.previous = self.current.copy()

    def update_data(self, data):
        self.previous = self.current.copy()
        self.current.update(data)

    def has_changed(self, key):
        return self.current[key] != self.previous[key]


class LEDMatrixDisplay:
    #TODO: workout more efficient way to display pixels.
    def __init__(self):
        options = RGBMatrixOptions()
        options.rows = 32
        options.cols = 64
        options.chain_length = 1
        options.parallel = 1
        options.disable_hardware_pulsing = 1
        options.brightness = 80
        options.hardware_mapping = 'adafruit-hat'
        options.show_refresh_rate = 1
        options.limit_refresh_rate_hz = 200
        options.pwm_lsb_nanoseconds = 50
        self.telemtry = Telemtry()
        self.matrix = RGBMatrix(options=options)
        self.canvas = self.matrix.CreateFrameCanvas()
        self.font = graphics.Font()
        self.font.LoadFont('../rpi-rgb-led-matrix/fonts/5x7.bdf')
        self.flags = irsdk.Flags()
        self.engine_warnings = irsdk.EngineWarnings()
        self.matrix_coords = {}

        with open('../client/matrix_coords.txt', 'r') as f:
            self.matrix_coords = json.load(f)


    def display_flag(self, flag):
        try:
            #TODO: change to allow for multiple flags displayed?
             #if checkered flag bit is set
            if (flag & self.flags.yellow) or (flag & self.flags.yellow_waving) or (flag & self.flags.caution) or (flag & self.flags.caution_waving) != 0:
                #display yellow flag
                for coords in self.matrix_coords['flags']['plain']:
                    self.canvas.SetPixel(coords[0], coords[1], 255, 200, 0) 
            elif (flag & self.flags.black) or (flag & self.flags.disqualify) or (flag & self.flags.furled) != 0:
                #display black flag
                for coords in self.matrix_coords['flags']['black']:
                    self.canvas.SetPixel(coords[0], coords[1], 255, 255, 255)
            elif flag & self.flags.blue != 0:
                #display blue flag
                for coords in self.matrix_coords['flags']['plain']:
                    self.canvas.SetPixel(coords[0], coords[1], 0, 200, 255)
            elif flag & self.flags.green != 0: #if green flag bit is set
                #Display green flag
                for coords in self.matrix_coords['flags']['plain']:
                    self.canvas.SetPixel(coords[0], coords[1], 0, 225, 0)
            elif flag & self.flags.checkered != 0:
                #Display checkered flag
                for coords in self.matrix_coords['flags']['checkered']:
                    self.canvas.SetPixel(coords[0], coords[1], 255, 255, 255)
            elif flag & self.flags.white != 0:
                #Display white flag
                for coords in self.matrix_coords['flags']['plain']:
                    self.canvas.SetPixel(coords[0], coords[1], 255, 255, 255)
            else:
                for coords in self.matrix_coords['flags']['plain']:
                    self.canvas.SetPixel(coords[0], coords[1], 0, 0, 0) 
        
        except Exception as err:
            print(f'Error 4: {err}')


    def display_gear(self, gear: str):
        try:
            gear_int = int(gear)
            for coords in self.matrix_coords['gears'][gear_int]:
                self.canvas.SetPixel(coords[0], coords[1], 255, 0, 0)
        except IndexError as err:
            print(f'Error 1: {err}')


    def display_abs(self, abs_active: bool):
        try:
            if abs_active:
                for coords in self.matrix_coords['abs']:
                    self.canvas.SetPixel(coords[0], coords[1], 255, 0, 255)
            else: 
                for coords in self.matrix_coords['abs']:
                    self.canvas.SetPixel(coords[0], coords[1], 0, 0, 0)
        except Exception as err:
            print(f"Error 5: {err}")


    def display_bb(self, brake_bias: float):
        try:
            text_colour = graphics.Color(255,255,255)
            x = 30
            y = 12
            text = str(brake_bias)
            graphics.DrawText(self.canvas, self.font, x, y, text_colour, text)
        except Exception as err:
            print(f"Error 6: {err}")


    def display_track_temp(self, track_temp: int):
        try: 
            text_colour = graphics.Color(255,255,255)
            x = 30
            y = 24
            text = f"{str(track_temp)}°c"
            graphics.DrawText(self.canvas, self.font, x, y, text_colour, text)
        except Exception as err:
            print(f"Error 6: {err}")
            
    
    def display_pit_lim(self, pit_lim_active):
        try:
            if pit_lim_active & self.engine_warnings.pit_speed_limiter:  # Check bit is active for pit lim
                for coords in self.matrix_coords['pit_lim']:  # assuming it's a list of tuples
                    self.canvas.SetPixel(coords[0], coords[1], 50, 0, 255)
            else:
                for coords in self.matrix_coords['pit_lim']:
                    self.canvas.SetPixel(coords[0], coords[1], 0, 0, 0)
        except Exception as err:
            print(f'Error 7: {err}')



    def process_data(self, data):
        try:
            #TODO worth implementing only clearing the pixels that are being replaced?
        
            data_str = data.decode()
            data = json.loads(data_str)
            
            self.telemtry.update_data(data)

            if self.telemtry.has_changed('gear'):
                self.display_gear(self.telemtry.current['gear'])
            if self.telemtry.has_changed('flags'):
                self.display_flag(self.telemtry.current['flags'])
            if self.telemetry.has_changed('abs_active'):
                self.display_abs(self.telemetry.current['abs_active'])
            if self.telemetry.has_changed('brake_bias'):
                self.display_bb(self.telemetry.current['brake_bias'])
            if self.telemetry.has_changed('track_temp'):
                self.display_track_temp(self.telemetry.current['track_temp'])
            if self.telemetry.has_changed('pit_lim_active'):
                self.display_pit_lim(self.telemetry.current['pit_lim_active'])

            self.matrix.SwapOnVSync(self.canvas)
        except Exception as err:
            print(f"Error 2: {err}. Data: {data}")

