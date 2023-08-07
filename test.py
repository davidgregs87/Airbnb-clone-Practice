arg = """city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297"""
s = arg.split()
attr = [a.replace('_',' ') if a.startswith('name=') else a for a in s]
split_attr = [x.split('=') for x in attr]
new_attr = [[x.strip('"') for x in new] for new in split_attr]
attr_keys = [sublist[0] for sublist in new_attr if len(sublist) > 1]
attr_values = [sublist[1] for sublist in new_attr if len(sublist) > 1]
print(attr_values)