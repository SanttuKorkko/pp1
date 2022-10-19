temperature = int(input("Temperature in Celsius: "))
kelvin = temperature + 273.15
fahrenheit = temperature * 1.8 + 32
txt = "Temperature in Kelvin is {}, and in Fahrenheit {}".format(kelvin, fahrenheit)
print(txt)