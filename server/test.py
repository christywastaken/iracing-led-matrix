from iracing_model import IRacing

iracing = IRacing()
iracing.check_iracing()
data_dict = iracing.get_data()
print(data_dict['flags'])

"""
537133568 pace 
2147745796 green
268697600 racing???
269221888 black - wrong way???
268697632 blue
268697601 checkered
268697602 white 
537149440 yellow? (exxtended caution rolling start)
"""