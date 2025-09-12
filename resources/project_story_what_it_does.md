# What DroneGPT-OSS Does

**DroneGPT-OSS** enables natural language drone control powered by OpenAI's gpt-oss reasoning models. Users can give complex instructions like "inspect the wind turbine for damage while maintaining safe distance," and the system reasons through optimal flight paths, safety margins, and emergency protocols.

## Core Capabilities

### 1. **Natural Language Flight Control**
- **Simple Commands**: `"take off"` → gpt-oss analyzes airspace, battery, weather conditions before execution
- **Complex Instructions**: `"Fly toward WindTurbine1 along the X-axis direction and stop 10 meters before reaching it with safety analysis"`
- **Multi-step Missions**: Chains together takeoff → navigation → inspection → return sequences with reasoning at each step

### 2. **Industrial Inspection Workflows**

**Wind Turbine Blade Inspection:**
- **3-Blade Systematic Coverage**: Inspects vertical blade, 30° right diagonal, 30° left diagonal positions
- **Rear Inspection Capability**: Repositions behind turbine for complete 360° blade analysis  
- **Safety Distance Management**: Maintains 10-12 meter clearance with automatic collision avoidance
- **Example Command**: `"Now let's start inspecting the blades with gpt-oss reasoning. The first blade is pointing straight upward. Please fly 30 meters above current position with safety analysis, then return."`

**Solar Panel Grid Survey:**
- **Lawn Mower Pattern Execution**: 10 rows × 20 columns systematic coverage (200 panels total)
- **Precision Altitude Control**: Maintains exact 5-meter inspection height for consistent thermal/visual analysis
- **Alternating Direction Logic**: West-to-East on odd rows, East-to-West on even rows for efficiency
- **Example Command**: `"Use your advanced gpt-oss reasoning to execute a systematic solar panel inspection with lawn mower pattern at 5-meter altitude"`

### 3. **Advanced Spatial Reasoning**
- **3D Coordinate Planning**: Calculates optimal trajectories in complex environments with obstacles
- **Geometric Angle Calculations**: `"fly 30 degrees below horizontal Y-axis (right and downward)"` → converts to precise [x,y,z] coordinates
- **Multi-waypoint Navigation**: Plans entire mission sequences with intermediate safety checkpoints
- **Real-time Obstacle Avoidance**: Uses lidar data and spatial reasoning for dynamic path adjustments

### 4. **Sim-to-Real Hardware Integration**
**DJI Tello EDU Real Drone Control:**
- **Environmental Safety Analysis**: `"Fly forward 3 meters, passing through a door frame with safety analysis"`
- **Battery-Aware Planning**: Monitors power consumption and calculates safe flight duration
- **Physical Constraint Reasoning**: Adapts simulation commands for real hardware limitations (13-minute flight time, 8 m/s max speed)
- **Emergency Landing Protocols**: Automatic safe zone identification and abort procedures

### 5. **Multi-Level Reasoning Effort**
- **Low Effort**: Basic maneuvers (takeoff, land, simple movements) - quick responses
- **Medium Effort**: Navigation planning and obstacle avoidance - balanced analysis  
- **High Effort**: Complex mission analysis, safety protocol generation, geometric calculations

## Technical Architecture

**gpt-oss Integration:**
- Uses OpenAI's gpt-oss-120b model via HuggingFace Inference API
- Reasoning effort control: `reasoning_effort="low|medium|high"`
- Natural language → Python code generation with safety validation

**Drone Control Stack:**
- **AirSim Wrapper**: Simplified functions (`aw.takeoff()`, `aw.fly_to([x,y,z])`, `aw.get_position("WindTurbine1")`)  
- **Tello Wrapper**: Real hardware interface (`tello.client.move_forward(100)`, `tello.client.rotate_clockwise(90)`)
- **Object Detection**: Maps semantic names ("WindTurbine1", "SolarPanels") to 3D coordinates

## Real-World Applications

**Industrial Inspection:**
- Wind farm maintenance with systematic blade damage assessment
- Solar panel efficiency monitoring across large installations
- Infrastructure inspection with safety-compliant flight patterns

**Search and Rescue:**
- Natural language mission planning: `"Search the area for survivors while avoiding power lines"`
- Dynamic replanning based on environmental conditions
- Emergency response with rapid deployment protocols

**Research and Development:**
- Embodied AI testing platform for spatial reasoning research
- Sim-to-real transfer validation for autonomous systems
- Safety protocol development for commercial drone operations
