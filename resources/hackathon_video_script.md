# DroneGPT: Flying Drones with gpt-oss - Video Transcript

Our project is named DroneGPT flying a drone with large language model. The project uses gpt-oss to power a drone. Flight in the airsim simulation environment. Use natural language commands. 

Why we select gpt-oss? gpt-oss features a leading reasoning model design. Allows providers of computing power to earn rewards even during idle periods. It fundamentally ensures the cost effectiveness providing developers a new and compelling option. 

Then for airsim Microsoft AirSim is an open source robot simulation platform. It is developed based on Unreal Engine for unmanned aerial vehicles and other autonomous systems. It provides a high-fidelity 3D rendering environment and rich sensor simulation. It supports software in the loop and hardware in the loop tests through API interface and other algorithms for rapid verification, deep learning, large language model. It is widely used in autonomous driving and drone control and other fields. Users can flexibly call functions through Python or C++. 

Our project is a combination of gpt-oss and airsim leveraging the powerful large model inference capabilities of gpt-oss to enable autonomous drone flight in airsim. The system adopts a typical embodied intelligence architecture where gpt-oss provides core capabilities in planning decision making and intelligent perception. 

This is the code of our project. The project code is mainly divided into several programs. The first one is actually the environment settings of airsim and gpt-oss. Then there are four examples. Below we have encapsulated gpt-oss. Here you need to fill in your API key. This is a wrapper for airsim. First you may need to download. It's all in this course. This course includes a simulation environment and gpt-oss. Just run these and set it up according to this. 

## What DroneGPT Actually Does

**DroneGPT** enables natural language drone control powered by gpt-oss reasoning models. Users can give complex instructions like "inspect the wind turbine for damage while maintaining safe distance," and the system reasons through optimal flight paths, safety margins, and emergency protocols.

**Core Capabilities:**

**Natural Language Flight Control:**
- Simple commands like "take off" → gpt-oss analyzes airspace, battery, weather conditions before execution
- Complex instructions: "Fly toward WindTurbine1 along the X-axis direction and stop 10 meters before reaching it with safety analysis"
- Multi-step missions that chain together takeoff → navigation → inspection → return sequences with reasoning at each step

**Industrial Inspection Workflows:**
- **Wind Turbine Blade Inspection:** 3-blade systematic coverage inspecting vertical blade, 30° right diagonal, 30° left diagonal positions with rear inspection capability for complete 360° blade analysis
- **Solar Panel Grid Survey:** 10 rows × 20 columns systematic coverage using lawn mower pattern with precision altitude control at exactly 5-meter inspection height
- **Safety Distance Management:** Maintains 10-12 meter clearance with automatic collision avoidance

**Advanced Spatial Reasoning:**
- 3D coordinate planning that calculates optimal trajectories in complex environments
- Geometric angle calculations: "fly 30 degrees below horizontal Y-axis" gets converted to precise [x,y,z] coordinates
- Multi-waypoint navigation with intermediate safety checkpoints
- Real-time obstacle avoidance using lidar data and spatial reasoning

**Sim-to-Real Hardware Integration:**
- DJI Tello EDU real drone control with environmental safety analysis
- Battery-aware planning that monitors power consumption and calculates safe flight duration
- Physical constraint reasoning that adapts simulation commands for real hardware limitations
- Emergency landing protocols with automatic safe zone identification

And then there are four examples below. The first one is environment setup with gpt-oss. The second one is simple drone control with natural language commands. Then it's complex control with wind turbine blade inspection. The third one is solar panel systematic survey and the last one is real drone flight with Tello for project demo.
