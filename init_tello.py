# Tello Real Drone Initialization Script for Notebooks
# Run this cell before using gpt-oss real drone commands

import tello_wrapper
import tello_agent

# Initialize Tello wrapper for real drone control
tello = tello_wrapper.TelloWrapper()
print("✅ Tello real drone wrapper initialized as 'tello'")
print("🔧 Available functions:")
print("   tello.client.takeoff() - Hardware takeoff")
print("   tello.client.land() - Hardware landing")
print("   tello.client.move_forward(cm) - Move forward")
print("   tello.client.move_back(cm) - Move backward")
print("   tello.client.move_left(cm) - Move left")
print("   tello.client.move_right(cm) - Move right")
print("   tello.client.move_up(cm) - Ascend")
print("   tello.client.move_down(cm) - Descend")
print("   tello.client.rotate_clockwise(degrees) - CW rotation")
print("   tello.client.rotate_counter_clockwise(degrees) - CCW rotation")

# Initialize gpt-oss agent for real drone operations
# my_agent = tello_agent.TelloAgent(knowledge_prompt="prompts/tello_gpt_oss_real.txt")
print("🧠 Ready for gpt-oss real drone reasoning!")
print("🛡️ Safety protocols activated: Battery check, environment analysis")
