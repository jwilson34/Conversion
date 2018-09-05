def kelvinto_celsius(temp):
	return temp - 273.15


def celsius_to_fahrenheit(temp):
	return temp*(9/5) + 32 

def kelvin_to_fahr(temp):
	temp_c= kelvin_to_celsius(temp)
	result = celsius_to_fahrenheit(temp_c)
	return result
