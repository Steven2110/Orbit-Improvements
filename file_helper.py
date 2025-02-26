import numpy as np
import math
import subprocess as sp

from constants import INPUT_TEMPLATE, PATH_IN, PATH_OUT, PATH_EXE

class FileHelper:
    def _read_file(self, file_path: str = PATH_OUT):
        f = open(file_path, "r", encoding="cp866")
        lines = f.read()
        f.close()
        return lines
    
    # For logger
    def get_coordinate(self, i):
        text = self._read_file().split()
        index = 39 + 29 * (i - 1)
        result = np.array(list(map(float, text[index:index+3])))
        return result

    def get_coordinates(self, total=100):
        text = self._read_file().split()
        indexes = [39+29*i for i in range(total)]
        result = [np.array(list(map(float, text[i:i+3]))) for i in indexes]
        return np.array(result)
    
    # For logger
    def get_velocity(self, i):
        text = self._read_file().split()
        index = 42 + 29 * (i - 1)
        result = np.array(list(map(float, text[index:index+3])))
        return result
    
    def get_velocities(self, total=100):
        text = self._read_file().split()
        indexes = [42+29*i for i in range(total)]
        result = [np.array(list(map(float, text[i:i+3]))) for i in indexes]
        return np.array(result)

    def format_scientific(self, num):
        if num == 0.0:
            return "0.00000000000000E+0000"  # Handle zero case separately

        exponent = math.floor(math.log10(abs(num)))  # Find exponent
        mantissa = num / (10**exponent)  # Normalize to 1 digit before decimal
        formatted_str = f"{mantissa:.14f}E{exponent:+05d}"  # Format output

        return formatted_str

    def configure_file(self, coordinate, velocity, date, month, year, hour, minute, second, t):
        f = open(PATH_IN, "w", encoding="cp866")
        f.write(INPUT_TEMPLATE.format(
            self.format_scientific(coordinate[0]),
            self.format_scientific(coordinate[1]),
            self.format_scientific(coordinate[2]),
            self.format_scientific(velocity[0]),
            self.format_scientific(velocity[1]),
            self.format_scientific(velocity[2]),
            date,
            month,
            year,
            hour,
            minute,
            second,
            t
        ))
        
    def run_exe_file(self):
        sp.call(PATH_EXE)
        
sp.call(PATH_EXE)