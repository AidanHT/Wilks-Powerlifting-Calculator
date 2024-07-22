class PowerliftingScore:

    def __init__(self, name, sex, equipment, age, bw, squat, dl):
        self._name = name
        self._sex = sex
        self._equipment = equipment

        self._age = age
        self._bw = bw
        
        self._squat = squat 
        self._dl = dl
        self._bench = self.predicted_bench()

    def value(self):
        if self._sex == 'M':
            return round(self.total_lift() * (600/( (47.46178854) + (8.472061379 * self._bw) + (0.07369410346 * self._bw ** 2) + (-0.001395833811 * self._bw ** 3) + (7.07665973070743 * 10 **-6 * self._bw ** 4) + (-1.20804336482315 * 10 ** -8 * self._bw ** 5))), 2)
                                        
        elif self._sex == 'F':
            return round(self.total_lift() * (600/( (-125.4255398) + (13.71219419 * self._bw) + (-0.03307250631 * self._bw ** 2) + (-0.001050400051 * self._bw ** 3) + (9.38773881462799 * 10 ** -6 * self._bw ** 4) + (-2.3334613884954 * 10 ** -8 * self._bw ** 5))), 2)

    def name(self):
        return self._name

    def sex(self):
        return self._sex

    def equipment(self):
        return self._equipment
    
    def age(self):
        return self._age
    
    def bw(self):
        return self._bw
    
    def squat(self):
        return self._squat
    
    def deadlift(self):
        return self._dl
    
    def predicted_bench(self):
        return self._bw * 1.5
    
    def total_lift(self):
        return self._squat + self._dl + self._bench
    
    def set_name(self, new):
        self._name = new

    def set_equipment(self, new):
        self._equipment = new

    def set_age(self, new):
        self._age = new

    def set_bw(self, new):
        self._bw = new

    def set_squat(self, new):
        self._squat = new

    def set_deadlift(self, new):
        self._dl = new

    def __str__(self):
        return f'{self._name}\n * Sex: {self._sex}\n * Age: {self._age} years\n * Bodyweight: {self._bw}kg\n * Squat: {self._squat}kg\n * Deadlift: {self._dl}kg\n * Equipment: {self._equipment}'
    
    def __repr__(self):
        return f'PowerliftingScore(Name = {self._name}, Sex = {self._sex}, Age = {self._age}, Bodyweight = {self._bw}, Squat = {self._squat}, Deadlift = {self._dl}, Equipment = {self._equipment})' 

    def __gt__(self, other):
        return self.value() > other.value()
    
    def __lt__(self, other):
        return self.value() < other.value()
    
    def __ge__(self, other):
        return self.value() >= other.value()
    
    def __le__(self, other):
        return self.value() <= other.value()
    
    def __eq__(self, other):
        return self.value() == other.value()
    
    def __ne__(self, other):
        return self.value() != other.value()
    
    def __truediv__(self, other):
        return round(self.value() / other.value(), 3)
    
    def __add__(self, other):
        return round(self.value() + other.value(), 2)
    
    def __sub__(self, other):
        return round(self.value() - other.value(), 2)
