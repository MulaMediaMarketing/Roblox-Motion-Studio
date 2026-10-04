# Roblox Studio Plugin

The plugin is a thin integration layer.

Responsibilities:
- receive a validated MotionDocument/export payload
- create/update Roblox KeyframeSequence data
- provide a small import/export UI
- report actionable errors

The plugin must not contain pose estimation, retargeting, or editor logic.
