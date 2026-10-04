# Rig Adapter Contract

The animation engine uses a generic skeleton model.

Each target adapter supplies:
- skeleton definition
- joint hierarchy
- rest pose
- bone-length constraints
- coordinate-system conversion
- source-to-target mapping
- export implementation

## R15 first

Canonical asset:

`assets/rigs/r15/R15_Rig_MotionStudio.gltf`

The adapter normalizes Roblox's exported `HumanoidRootNode` into the engine's canonical root representation.

The adapter must preserve the Roblox R15 joint hierarchy and attachment semantics needed for accurate retargeting.

## Future targets

The same domain animation document can later be mapped to:
- Roblox R6
- Unreal Engine humanoid skeletons
- other compatible humanoid rigs

Those are separate adapters, not special cases inside the core editor.
