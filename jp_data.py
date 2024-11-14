# mymodule.py

class Jpi:
    def __init__(self):
        # jpiの値を設定
        self.value = 3.141592653589793238

    def area(self, radius):
        """円の面積を計算するメソッド"""
        return self.value * (radius ** 2)

    def around(self, digits=2):
        """jpiの値を指定した小数点で丸めるメソッド"""
        return round(self.value, digits)

# Jpiのインスタンスを作成
jpi = Jpi()
