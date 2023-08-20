from invest.quant import buyandhold as bh

class Invest:

    # 생성자 함수
    def __init__(self, _df, _start='2000-01-01', _end='2023-12-31'):
        self.df = _df
        self.start = _start
        self.end = _end
    
    def buyandhold(self):
        self.result = bh.bnh(self.df, self.start, self.end)
        return self.result