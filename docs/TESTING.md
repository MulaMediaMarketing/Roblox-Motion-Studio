# Testing Strategy

## Unit tests

Required for:
- quaternion operations
- interpolation
- blending
- skeleton hierarchy traversal
- R15 mapping
- root-motion calculations
- foot-contact calculations
- motion-document validation
- Roblox KeyframeSequence generation

## Integration tests

- GLTF -> canonical skeleton
- video -> extracted motion document
- motion document -> Three.js playback state
- motion document -> Roblox exporter

## Golden tests

Maintain known input/output animation fixtures. A small change in retargeting should produce an intentional, reviewable fixture change.

## Performance tests

Track:
- video processing time
- frames processed per second
- editor frame time
- timeline scrub latency
- export time
- memory usage for long animations

## Acceptance test

The first vertical slice is complete only when:

MP4 -> pose -> R15 -> editable timeline -> Lua -> Roblox KeyframeSequence

produces a visually correct, playable result.
