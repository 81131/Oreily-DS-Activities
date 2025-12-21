def fireAlarmSystemLogic(smokeSensor: bool, heatSensor:bool,)-> None:

    #If all sensors are active
    if all([smokeSensor, heatSensor]):
        alarm = True
        alertAuth = True

    #If only one of the sensor activated alert authority. Potential system fault will lead to chaos otherwise
    elif any([smokeSensor, heatSensor]):
        alarm = False
        alertAuth = True
    else:
        alertAuth = False
        alarm = False
    return alertAuth,alarm

def fireAlarmSystemUI(smokeSensor, heatSensor):
    alertAuth, alarm = fireAlarmSystemLogic(smokeSensor,heatSensor )
    print(f"Authority alerted and alarm activated" if alertAuth and alarm else "Only authority alerted" if alertAuth and not alarm else "Safe...")

print("Both Sensors activated situation: ")
fireAlarmSystemUI(True, True)

print("\n\nOnly heat sensors activated situation: ")
fireAlarmSystemUI(False, True)

print("\n\nOnly Smole sensor activated situation: ")
fireAlarmSystemUI(True, False)

print("\n\nBoth sensor deactivated situaltion: ")
fireAlarmSystemUI(False, False)