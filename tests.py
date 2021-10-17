import unittest
from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit, convertFahrenheitToKelvin, convertFahrenheitToCelsius, convertKelvinToFahrenheit, convertKelvinToCelsius

class Conversion_Tester(unittest.TestCase):
      
    cel_to_kel = ((0, 273.15), (50, 323.15), (100, 373.15), (150, 423.15))
    cel_to_fah = ((0, 32.0), (32, 89.6), (100, 212.0), (150, 302), (200, 392))
    fah_to_kel = ((5, 258.15), (50, 283.15), (104, 313.15), (158, 343.15), (203, 368.15))
    fah_to_cel = ((32, 0), (50, 10), (104, 40), (113, 45), (158, 70))
    kel_to_cel = ((0, -273.15), (100, -173.15), (200, -73.15), (300, 26.85), (400, 126.85))
    kel_to_fah = ((0, -459.67), (100, -279.67), (200, -99.67), (300, 80.33), (400, 260.33))
    
    def Test_Conversion_CelsiusToKelvin(self):
        print('Testing')
        for cel, kel, in self.cel_to_kel:
            result = convertCelsiusToKelvin(cel)
            self.assertEqual(result, k)
            print(f'{cel} in Celsius is {kel} in Kelvin.')
            
    def Test_Conversion_CelsiusToFarenheit(self):
        print('Testing')
        for cel, fah, in self.cel_to_fah:
            result = convertCelsiusToFahrenheit(cel)
            self.assertEqual(result, fah)
            print(f'{cel} in Celsius is {fah} in Fahrenheit.')
            
    def Test_Conversion_FahrenheitToKelvin(self):
        print('Testing')
        for fah, kel, in self.fah_to_kel:
            result = convertFahrenheitToKelvin(fah)
            self.assertEqual(result, kel)
            print(f'{fah} in Fahrenheit is {kel} in Kelvin.')
            
    def Test_Conversion_FahrenheitToCelsius(self):
        print('Testing')
        for fah, cel, in self.fah_to_cel:
            result = convertFahrenheitToCelsius(fah)
            self.assertEqual(result, cel)
            print(f'{f} in Fahrenheit is {c} in Kelvin.')
            
    def Test_Conversion_KelvinToCelsius(self):
        print('Testing Kelvin to Celsius conversions.')
        for kel, cel, in self.kel_to_cel:
            result = convertKelvinToCelsius(kel)
            self.assertEqual(result, cel)
            print(f'{kel} in Kelvin is {cel} in Celsius.')
            
    def test_convertKelvinToFahrenheit(self):
        print('Testing')
        for kel, fah, in self.kel_to_fah:
            result = convertKelvinToFahrenheit(kel)
            self.assertEqual(result, fah)
            print(f'{k} in Kelvin is {f} in Fahrenheit.')
            
    

        
