from iracing_model import IRacing

iracing = IRacing()
iracing.check_iracing()
# data_dict = iracing.get_data()
# print(data_dict['flags'])

print(str(iracing.get_bb()))