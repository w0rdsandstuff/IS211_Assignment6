
def convertCelsiusToKelvin(celsius):
        
    kelvins = celsius + 273.15
    print("Temperature in Kelvins: ", kelvins)
    
    return kelvins


def convertCelsiusToFahrenheit(celsius):
    
    fahrenheit = celsius * 9/5 + 32
    
    print("Temperature in Fahrenheit: ", fahrenheit)
    
    return fahrenheit

def convertFahrenheitToCelsius(fahrenheit):
    celsius = ((fahrenheit - 32) * (5/9))
    print("Temperature in Celsius: ", celsius)

    return celsius
    
def convertFahrenheitToKelvin(fahrenheit):

    kelvin = ((fahrenheit - 32) * (5/9) + 273.15)
    print("Temperature in Kelvin: ", kelvin)

    return kelvin


def convertKelvinToCelsius(kelvin):
    celsius = kelvin - 273.15
    print("Temperature in Celsius: ", celsius)

    return celsius


def convertKelvinToFahrenheit(kelvin):

    fahrenheit = kelvin * 9/5 - 459.67
    print("Temperature in Fahrenheit: ", fahrenheit)

    return fahrenheit


