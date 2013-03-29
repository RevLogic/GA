class Lines:
    def __init__(self, labels, values):
        if len(labels) != len(values):
            raise ValueError
        self.lines = dict(zip(labels, values))
    
    def apply(self, gate_instance):
        self.lines = gate_instance.output(self.lines.copy())

    

