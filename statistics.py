def calculateStats(numbers):
   if len(numbers) == 0:
      return float("nan")
   return {"avg": sum(numbers) / len(numbers), "max": max(numbers), "min": min(numbers)}


   #def __init__(self, numbers) -> None:
   #  self.numbers = numbers
