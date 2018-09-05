def kelvin_to_celsius(temp):
        """
        Convert to Celsius
        """
        return temp - 273.15


def celsius_to_fahr(temp):
        """
        Convert to Fahrenheit
        """
	return temp*(9/5) + 32 

def kelvin_to_fahr(temp):
        """
        blah blah blah
        """
	temp_c= kelvin_to_celsius(temp)
	result = celsius_to_fahrenheit(temp_c)
	return result

