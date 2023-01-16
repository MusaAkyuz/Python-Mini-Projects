from dronekit import connect
import dronekit_sitl

print("Starting Simulation")

sitl = dronekit_sitl.start_default()
connectionString = sitl.connection_string()

print("Connecting to vehicle on: %s" % (connectionString,))
vehicle = connect(connectionString, wait_ready=True)

print()
print("Get some vehicle attribute values : ")
print(" GPS : ", vehicle.gps_0)
print(" Battery : ", vehicle.battery)
print(" Last Heartbeat : ", vehicle.last_heartbeat)
print(" Is Armable? : ", vehicle.is_armable)
print(" System sstatus : ", vehicle.system_status.state)
print(" Mode : ", vehicle.mode.name)

vehicle.close()
sitl.stop()
print()
print("Completed")
