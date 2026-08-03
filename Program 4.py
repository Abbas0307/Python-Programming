# Electricity Bill Program

# Accept input from user
consumer_name = input("Enter Consumer Name: ")
consumer_id = input("Enter Consumer ID: ")
previous_reading = float(input("Enter Previous Meter Reading (kWh): "))
current_reading = float(input("Enter Current Meter Reading (kWh): "))
cost_per_unit = float(input("Enter Cost per Unit (₹): "))

# Calculations
total_units = current_reading - previous_reading
energy_charge = total_units * cost_per_unit
electricity_duty = energy_charge * 0.05
fixed_meter_charge = 100
net_bill = energy_charge + electricity_duty + fixed_meter_charge

# Display Bill
print("\n========== ELECTRICITY BILL ==========")
print("Consumer Name       :", consumer_name)
print("Consumer ID         :", consumer_id)
print("--------------------------------------")
print("Previous Reading    :", previous_reading, "kWh")
print("Current Reading     :", current_reading, "kWh")
print("Total Units         :", total_units, "Units")
print("--------------------------------------")
print("Energy Charge       : ₹", energy_charge)
print("Electricity Duty    : ₹", electricity_duty)
print("Fixed Meter Charge  : ₹", fixed_meter_charge)
print("--------------------------------------")
print("Net Bill Amount     : ₹", net_bill)
print("======================================")
