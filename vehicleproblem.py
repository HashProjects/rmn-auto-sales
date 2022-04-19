import random


class VehicleProblem:
    @classmethod
    def fromNamedTuple(cls, vehicleproblem):
        return cls(vehicleproblem.purchase_id, vehicleproblem.vehicle_id, vehicleproblem.problem_id,
                   vehicleproblem.problem_description, vehicleproblem.estimated_repair_cost,
                   vehicleproblem.actual_repair_cost)

    def __init__(self,
                 purchase_id, vehicle_id, problem_id, problem_description, estimated_repair_cost, actual_repair_cost):
        self.purchase_id = purchase_id
        self.vehicle_id = vehicle_id
        self.problem_id = problem_id
        self.problem_description = problem_description
        self.estimated_repair_cost = estimated_repair_cost
        self.actual_repair_cost = actual_repair_cost

    def __str__(self):
        return "VehicleProblem({}. {} - ${})".format(self.problem_id, self.problem_description, self.estimated_repair_cost)


def generateRandomProblem():
    return VehicleProblem(0, 0, 0, random.choice(["Flat Tire", "Broken Tail Light", "Cracked Windshield", "Dirty Oil", "Low Transmission Fluid"]),
                          random.randint(25, 100), 0)