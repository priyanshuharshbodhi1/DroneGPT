# AirSim Initialization Script for Notebooks
# Run this cell before using gpt-oss drone commands

import airsim_wrapper
import airsim_agent

# Initialize AirSim wrapper for drone control
aw = airsim_wrapper.AirSimWrapper()
print("✅ AirSim wrapper initialized as 'aw'")
print("🔧 Available functions:")
print("   aw.takeoff() - Safe takeoff")
print("   aw.land() - Controlled landing") 
print("   aw.get_drone_position() - Current [x,y,z]")
print("   aw.fly_to([x,y,z]) - Navigate to position")
print("   aw.get_position('object_name') - Get object coordinates")

# Initialize gpt-oss agent (example - adjust knowledge_prompt as needed)
# my_agent = airsim_agent.AirSimAgent(knowledge_prompt="prompts/airsim_basic.txt")
print("🧠 Ready for gpt-oss reasoning integration!")
