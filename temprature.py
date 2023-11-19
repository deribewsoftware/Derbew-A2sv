class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin=273.15+celsius
        Fahrenheit = celsius * 1.80 + 32.00
        return [kelvin,Fahrenheit]
