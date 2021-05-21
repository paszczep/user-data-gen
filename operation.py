class Operation:

    def __init__(self, user, operation_type, duration, make, model, body_type, price_point):
        self.user_id = user
        self.operation = operation_type
        self.duration = round(duration, 3)
        self.make = make
        self.model = model
        self.body = body_type
        self.price = price_point

    def print_operation(self):
        operation_data = {'id': self.user_id,
                          'operation_type': self.operation,
                          'duration': self.duration,
                          'car_make': self.make,
                          'car_model': self.model,
                          'car_body': self.body,
                          'price_point': self.price
                          }
        return operation_data
